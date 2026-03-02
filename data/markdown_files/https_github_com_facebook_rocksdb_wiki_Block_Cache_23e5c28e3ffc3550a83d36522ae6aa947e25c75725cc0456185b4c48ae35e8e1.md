[Skip to content](https://github.com/facebook/rocksdb/wiki/Block-Cache#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Block-Cache) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Block-Cache) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Block-Cache) to refresh your session.Dismiss alert

{{ message }}

[facebook](https://github.com/facebook)/ **[rocksdb](https://github.com/facebook/rocksdb)** Public

- [Notifications](https://github.com/login?return_to=%2Ffacebook%2Frocksdb) You must be signed in to change notification settings
- [Fork\\
6.7k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)
- [Star\\
31.4k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)


# Block Cache

[Jump to bottom](https://github.com/facebook/rocksdb/wiki/Block-Cache#wiki-pages-box)

Peter Dillinger edited this page on Apr 4, 2023Apr 4, 2023
·
[35 revisions](https://github.com/facebook/rocksdb/wiki/Block-Cache/_history)

Block cache is where RocksDB caches data in memory for reads. User can pass in a `Cache` object to a RocksDB instance with a desired capacity (size). A `Cache` object can be shared by multiple RocksDB instances in the same process, allowing users to control the overall cache capacity. The block cache stores uncompressed blocks. Optionally user can set a second block cache storing compressed blocks. Reads will fetch data blocks first from uncompressed block cache, then compressed block cache. The compressed block cache can be a replacement of OS page cache, if [Direct-IO](https://github.com/facebook/rocksdb/wiki/Direct-IO) is used.

There are two cache implementations in RocksDB, namely `LRUCache` and `ClockCache`. Both types of the cache are sharded to mitigate lock contention. Capacity is divided evenly to each shard and shards don't share capacity. By default each cache will be sharded into at most 64 shards, which provides a reasonable balance of scalability with parallel reads and locality of block cache metadata with lighter read loads. The minimum capacity for cache shards is 512KB, to limit the risk of random assignments thrashing one shard.

### Usage

[Permalink: Usage](https://github.com/facebook/rocksdb/wiki/Block-Cache#usage)

Out of box, RocksDB will use LRU-based block cache implementation with 32MB capacity (8MB before version 8.2). This is only recommended for applications that are not heavily dependent on RocksDB read performance but prefer RocksDB to keep a modest memory footprint.
To set a customized block cache, call `NewLRUCache()` or `HyperClockCacheOptions::MakeSharedCache()` to create a cache object, and set it to block based table options.

```
std::shared_ptr<Cache> cache = NewLRUCache(capacity);
BlockBasedTableOptions table_options;
table_options.block_cache = cache;
Options options;
options.table_factory.reset(NewBlockBasedTableFactory(table_options));
```

RocksDB will create the default block cache if `block_cache` is set to `nullptr`. To disable block cache completely:

```
table_options.no_block_cache = true;
```

Advanced users can customize Cache behavior with a CacheWrapper, but block cache implementations have become so specialized and evolving that it is not practical for users to build and maintain their own implementation.

### LRU Cache

[Permalink: LRU Cache](https://github.com/facebook/rocksdb/wiki/Block-Cache#lru-cache)

Out of box, RocksDB will use LRU-based block cache implementation with 32MB capacity. Each shard of the cache maintains its own LRU list and its own hash table for lookup. Synchronization is done via a per-shard mutex. Both lookup and insert to the cache would require a locking mutex of the shard, because the LRU list makes every cache read a likely write to the cache metadata. User can create an LRU cache by calling `NewLRUCache()`. The function provides several useful options to set to the cache:

- `capacity`: Total size of the cache.
- `num_shard_bits`: The number of bits from cache keys to use as shard id. The cache will be sharded into `2^num_shard_bits` shards.
- `strict_capacity_limit`: In rare case, block cache size can go larger than its capacity. This is when ongoing reads or iterations over DB pin blocks in block cache, and the total size of pinned blocks exceeds the capacity. If there are further reads which try to insert blocks into block cache, if `strict_capacity_limit=false`(default), the cache will fail to respect its capacity limit and allow the insertion. This can create undesired OOM error that crashes the DB if the host don't have enough memory. Setting the option to `true` will reject further insertion to the cache and fail the read or iteration, though this can have undesired effects. The option works on per-shard basis, means it is possible one shard is rejecting insert when it is full, while another shard still have extra unpinned space.
- `high_pri_pool_ratio`: The ratio of capacity reserved for high priority blocks. See [Caching Index, Filter, and Compression Dictionary Blocks](https://github.com/facebook/rocksdb/wiki/Block-Cache#caching-index-filter-and-compression-dictionary-blocks) section below for more information.

### HyperClockCache

[Permalink: HyperClockCache](https://github.com/facebook/rocksdb/wiki/Block-Cache#hyperclockcache)

Due to limitations, this feature is currently for advanced usage only. We hope to make it more generally applicable soon. [Some performance data is here.](http://smalldatum.blogspot.com/2022/10/hyping-hyper-clock-cache-in-rocksdb.html)

### Caching Index, Filter, and Compression Dictionary Blocks

[Permalink: Caching Index, Filter, and Compression Dictionary Blocks](https://github.com/facebook/rocksdb/wiki/Block-Cache#caching-index-filter-and-compression-dictionary-blocks)

By default index, filter, and compression dictionary blocks (with the exception of the partitions of [partitioned indexes/filters](https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters)) are cached outside of block cache, and users won't be able to control how much memory should be used to cache these blocks, other than setting `max_open_files`. Users can opt to cache index and filter blocks in block cache, which allows for better control of memory used by RocksDB. To cache index, filter, and compression dictionary blocks in block cache:

```
BlockBasedTableOptions table_options;
table_options.cache_index_and_filter_blocks = true;
```

Note that the partitions of partitioned indexes/filters are as a rule stored in the block cache, regardless of the value of the above option.

By putting index, filter, and compression dictionary blocks in block cache, these blocks have to compete against data blocks for staying in cache. Although index and filter blocks are being accessed more frequently than data blocks, there are scenarios where these blocks can be thrashing. This is undesired because index and filter blocks tend to be much larger than data blocks, and they are usually of higher value to stay in cache (the latter is also true for compression dictionary blocks). There are two options to tune to mitigate the problem:

- `cache_index_and_filter_blocks_with_high_priority`: Set priority to high for index, filter, and compression dictionary blocks in block cache. For partitioned indexes/filters, this affects the priority of the partitions as well. It only affect `LRUCache` so far, and need to use together with `high_pri_pool_ratio` when calling `NewLRUCache()`. If the feature is enabled, LRU-list in LRU cache will be split into two parts, one for high-pri blocks and one for low-pri blocks. Data blocks will be inserted to the head of low-pri pool. Index, filter, and compression dictionary blocks will be inserted to the head of high-pri pool. If the total usage in the high-pri pool exceed `capacity * high_pri_pool_ratio`, the block at the tail of high-pri pool will overflow to the head of low-pri pool, after which it will compete against data blocks to stay in cache. Eviction will start from the tail of low-pri pool.

- `pin_l0_filter_and_index_blocks_in_cache`: Pin level-0 file's index and filter blocks in block cache, to avoid them from being evicted. Starting with RocksDB version 6.4, this option also affects compression dictionary blocks. Level-0 index and filters are typically accessed more frequently. Also they tend to be smaller in size so hopefully pinning them in cache won't consume too much capacity.

- `pin_top_level_index_and_filter`: only applicable to partitioned indexes/filters. If `true`, the top level of the partitioned index/filter structure will be pinned in the cache, regardless of the LSM tree level (that is, unlike the previous option, this affects files on all LSM tree levels, not just L0).


### Simulated Cache

[Permalink: Simulated Cache](https://github.com/facebook/rocksdb/wiki/Block-Cache#simulated-cache)

`SimCache` is an utility to predict cache hit rate if cache capacity or number of shards is changed. It wraps around the real `Cache` object that the DB is using, and runs a shadow LRU cache simulating the given capacity and number of shards, and measure cache hits and misses of the shadow cache. The utility is useful when user wants to open a DB with, say, 4GB cache size, but would like to know what the cache hit rate will become if cache size enlarge to, say, 64GB. To create a simulated cache:

```
// This cache is the actual cache use by the DB.
std::shared_ptr<Cache> cache = NewLRUCache(capacity);
// This is the simulated cache.
std::shared_ptr<Cache> sim_cache = NewSimCache(cache, sim_capacity, sim_num_shard_bits);
BlockBasedTableOptions table_options;
table_options.block_cache = sim_cache;
```

The extra memory overhead of the simulated cache is less than 2% of `sim_capacity`.

### Statistics

[Permalink: Statistics](https://github.com/facebook/rocksdb/wiki/Block-Cache#statistics)

A list of block cache counters can be accessed through `Options.statistics` if it is non-null.

```
// total block cache misses
// REQUIRES: BLOCK_CACHE_MISS == BLOCK_CACHE_INDEX_MISS +
//                               BLOCK_CACHE_FILTER_MISS +
//                               BLOCK_CACHE_DATA_MISS;
BLOCK_CACHE_MISS = 0,
// total block cache hit
// REQUIRES: BLOCK_CACHE_HIT == BLOCK_CACHE_INDEX_HIT +
//                              BLOCK_CACHE_FILTER_HIT +
//                              BLOCK_CACHE_DATA_HIT;
BLOCK_CACHE_HIT,
// # of blocks added to block cache.
BLOCK_CACHE_ADD,
// # of failures when adding blocks to block cache.
BLOCK_CACHE_ADD_FAILURES,
// # of times cache miss when accessing index block from block cache.
BLOCK_CACHE_INDEX_MISS,
// # of times cache hit when accessing index block from block cache.
BLOCK_CACHE_INDEX_HIT,
// # of times cache miss when accessing filter block from block cache.
BLOCK_CACHE_FILTER_MISS,
// # of times cache hit when accessing filter block from block cache.
BLOCK_CACHE_FILTER_HIT,
// # of times cache miss when accessing data block from block cache.
BLOCK_CACHE_DATA_MISS,
// # of times cache hit when accessing data block from block cache.
BLOCK_CACHE_DATA_HIT,
// # of bytes read from cache.
BLOCK_CACHE_BYTES_READ,
// # of bytes written into cache.
BLOCK_CACHE_BYTES_WRITE,
```

See also: [Memory-usage-in-RocksDB#block-cache](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#block-cache)

**Contents**

- [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki/Home)
- [Overview](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview)
- [RocksDB FAQ](https://github.com/facebook/rocksdb/wiki/RocksDB-FAQ)
- [Terminology](https://github.com/facebook/rocksdb/wiki/Terminology)
- [Requirements](https://github.com/facebook/rocksdb/wiki/Platform-Requirements)
- [Contributors' Guide](https://github.com/facebook/rocksdb/wiki/RocksDB-Contribution-Guide)
- [Release Methodology](https://github.com/facebook/rocksdb/wiki/RocksDB-Release-Methodology)
- [RocksDB Users and Use Cases](https://github.com/facebook/rocksdb/wiki/RocksDB-Users-and-Use-Cases)
- [RocksDB Public Communication and Information Channels](https://github.com/facebook/rocksdb/wiki/RocksDB-Public-Communication-and-Information-Channels)
- [Basic Operations](https://github.com/facebook/rocksdb/wiki/Basic-Operations)  - [Iterator](https://github.com/facebook/rocksdb/wiki/Iterator)
  - [Prefix seek](https://github.com/facebook/rocksdb/wiki/Prefix-Seek)
  - [SeekForPrev](https://github.com/facebook/rocksdb/wiki/SeekForPrev)
  - [Tailing Iterator](https://github.com/facebook/rocksdb/wiki/Tailing-Iterator)
  - [Compaction Filter](https://github.com/facebook/rocksdb/wiki/Compaction-Filter)
  - [Multi Column Family Iterator](https://github.com/facebook/rocksdb/wiki/Multi-Column-Family-Iterator)
  - [Read-Modify-Write (Merge) Operator](https://github.com/facebook/rocksdb/wiki/Merge-Operator)
  - [Column Families](https://github.com/facebook/rocksdb/wiki/Column-Families)
  - [Creating and Ingesting SST files](https://github.com/facebook/rocksdb/wiki/Creating-and-Ingesting-SST-files)
  - [Single Delete](https://github.com/facebook/rocksdb/wiki/Single-Delete)
  - [SST Partitioner](https://github.com/facebook/rocksdb/wiki/SST-Partitioner)
  - [Low Priority Write](https://github.com/facebook/rocksdb/wiki/Low-Priority-Write)
  - [Time to Live (TTL) Support](https://github.com/facebook/rocksdb/wiki/Time-to-Live)
  - [Transactions](https://github.com/facebook/rocksdb/wiki/Transactions)
  - [Snapshot](https://github.com/facebook/rocksdb/wiki/Snapshot)
  - [DeleteRange](https://github.com/facebook/rocksdb/wiki/DeleteRange)
  - [Atomic flush](https://github.com/facebook/rocksdb/wiki/Atomic-flush)
  - [Read-only and Secondary instances](https://github.com/facebook/rocksdb/wiki/Read-only-and-Secondary-instances)
  - [Approximate Size](https://github.com/facebook/rocksdb/wiki/Approximate-Size)
  - [User-defined Timestamp](https://github.com/facebook/rocksdb/wiki/User-defined-Timestamp)
  - [Wide Columns](https://github.com/facebook/rocksdb/wiki/Wide-Columns)
  - [BlobDB](https://github.com/facebook/rocksdb/wiki/BlobDB)
  - [Online Verification](https://github.com/facebook/rocksdb/wiki/Online-Verification)
- **Options**  - [Setup Options and Basic Tuning](https://github.com/facebook/rocksdb/wiki/Setup-Options-and-Basic-Tuning)
  - [Option String and Option Map](https://github.com/facebook/rocksdb/wiki/Option-String-and-Option-Map)
  - [RocksDB Options File](https://github.com/facebook/rocksdb/wiki/RocksDB-Options-File)
- [MemTable](https://github.com/facebook/rocksdb/wiki/MemTable)
- [Journal](https://github.com/facebook/rocksdb/wiki/Journal)  - [Write Ahead Log (WAL)](https://github.com/facebook/rocksdb/wiki/Write-Ahead-Log-%28WAL%29)    - [Write Ahead Log File Format](https://github.com/facebook/rocksdb/wiki/Write-Ahead-Log-File-Format)
    - [WAL Recovery Modes](https://github.com/facebook/rocksdb/wiki/WAL-Recovery-Modes)
    - [WAL Performance](https://github.com/facebook/rocksdb/wiki/WAL-Performance)
    - [WAL Compression](https://github.com/facebook/rocksdb/wiki/WAL-Compression)
  - [MANIFEST](https://github.com/facebook/rocksdb/wiki/MANIFEST)
  - [Track WAL in MANIFEST](https://github.com/facebook/rocksdb/wiki/Track-WAL-in-MANIFEST)
- **Cache**  - [Block Cache](https://github.com/facebook/rocksdb/wiki/Block-Cache)
  - [SecondaryCache (Experimental)](https://github.com/facebook/rocksdb/wiki/SecondaryCache-%28Experimental%29)
- [Write Buffer Manager](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager)
- [Compaction](https://github.com/facebook/rocksdb/wiki/Compaction)  - [Leveled Compaction](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction)
  - [Universal compaction style](https://github.com/facebook/rocksdb/wiki/Universal-Compaction)
  - [FIFO compaction style](https://github.com/facebook/rocksdb/wiki/FIFO-compaction-style)
  - [Manual Compaction](https://github.com/facebook/rocksdb/wiki/Manual-Compaction)
  - [Subcompaction](https://github.com/facebook/rocksdb/wiki/Subcompaction)
  - [Choose Level Compaction Files](https://github.com/facebook/rocksdb/wiki/Choose-Level-Compaction-Files)
  - [Managing Disk Space Utilization](https://github.com/facebook/rocksdb/wiki/Managing-Disk-Space-Utilization)
  - [Trivial Move Compaction](https://github.com/facebook/rocksdb/wiki/Compaction-Trivial-Move)
  - [Remote Compaction](https://github.com/facebook/rocksdb/wiki/Remote-Compaction)
- **SST File Formats**  - [Block-based Table Format](https://github.com/facebook/rocksdb/wiki/Rocksdb-BlockBasedTable-Format)
  - [PlainTable Format](https://github.com/facebook/rocksdb/wiki/PlainTable-Format)
  - [CuckooTable Format](https://github.com/facebook/rocksdb/wiki/CuckooTable-Format)
  - [External Table](https://github.com/facebook/rocksdb/wiki/External-Table-%28Experimental%29)
  - [Index Block Format](https://github.com/facebook/rocksdb/wiki/Index-Block-Format)
  - [Bloom Filter](https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter)
  - [Data Block Hash Index](https://github.com/facebook/rocksdb/wiki/Data-Block-Hash-Index)
- [IO](https://github.com/facebook/rocksdb/wiki/IO)  - [Rate Limiter](https://github.com/facebook/rocksdb/wiki/Rate-Limiter)
  - [SST File Manager](https://github.com/facebook/rocksdb/wiki/SST-File-Manager)
  - [Direct I/O](https://github.com/facebook/rocksdb/wiki/Direct-IO)
- [Compression](https://github.com/facebook/rocksdb/wiki/Compression)   - [Dictionary Compression](https://github.com/facebook/rocksdb/wiki/Dictionary-Compression)
- [Full File Checksum and Checksum Handoff](https://github.com/facebook/rocksdb/wiki/Full-File-Checksum-and-Checksum-Handoff)
- [Background Error Handling](https://github.com/facebook/rocksdb/wiki/Background-Error-Handling)
- [Huge Page TLB Support](https://github.com/facebook/rocksdb/wiki/Allocating-Some-Indexes-and-Bloom-Filters-using-Huge-Page-TLB)
- [Tiered Storage (Experimental)](https://github.com/facebook/rocksdb/wiki/Tiered-Storage-%28Experimental%29)
- **Logging and Monitoring**  - [Logger](https://github.com/facebook/rocksdb/wiki/Logger)
  - [Statistics](https://github.com/facebook/rocksdb/wiki/Statistics)
  - [Compaction Stats and DB Status](https://github.com/facebook/rocksdb/wiki/Compaction-Stats-and-DB-Status)
  - [Perf Context and IO Stats Context](https://github.com/facebook/rocksdb/wiki/Perf-Context-and-IO-Stats-Context)
  - [EventListener](https://github.com/facebook/rocksdb/wiki/EventListener)
- [Known Issues](https://github.com/facebook/rocksdb/wiki/Known-Issues)
- [Troubleshooting Guide](https://github.com/facebook/rocksdb/wiki/RocksDB-Troubleshooting-Guide)
- [Tests](https://github.com/facebook/rocksdb/wiki/Tests)  - [Stress Test](https://github.com/facebook/rocksdb/wiki/Stress-test)
  - [Fuzzing](https://github.com/facebook/rocksdb/wiki/Fuzz-Test)
  - [Benchmarking](https://github.com/facebook/rocksdb/wiki/Benchmarking-tools)
- **Tools / Utilities**  - [Administration and Data Access Tool](https://github.com/facebook/rocksdb/wiki/Administration-and-Data-Access-Tool)
  - [How to Backup RocksDB?](https://github.com/facebook/rocksdb/wiki/How-to-backup-RocksDB)
  - [Replication Helpers](https://github.com/facebook/rocksdb/wiki/Replication-Helpers)
  - [Checkpoints](https://github.com/facebook/rocksdb/wiki/Checkpoints)
  - [How to persist in-memory RocksDB database](https://github.com/facebook/rocksdb/wiki/How-to-persist-in-memory-RocksDB-database)
  - [Third-party language bindings](https://github.com/facebook/rocksdb/wiki/Third-party-language-bindings)
  - [RocksDB Trace, Replay, Analyzer, and Workload Generation](https://github.com/facebook/rocksdb/wiki/RocksDB-Trace%2C-Replay%2C-Analyzer%2C-and-Workload-Generation)
  - [Block cache analysis and simulation tools](https://github.com/facebook/rocksdb/wiki/Block-cache-analysis-and-simulation-tools)
  - [IO Tracer and Parser](https://github.com/facebook/rocksdb/wiki/IO-Tracer-and-Parser)
- **Implementation Details**  - [Delete Stale Files](https://github.com/facebook/rocksdb/wiki/Delete-Stale-Files)
  - [Partitioned Index/Filters](https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters)
  - [WritePrepared-Transactions](https://github.com/facebook/rocksdb/wiki/WritePrepared-Transactions)
  - [WriteUnprepared-Transactions](https://github.com/facebook/rocksdb/wiki/WriteUnprepared-Transactions)
  - [How we keep track of live SST files](https://github.com/facebook/rocksdb/wiki/How-we-keep-track-of-live-SST-files)
  - [How we index SST](https://github.com/facebook/rocksdb/wiki/Indexing-SST-Files-for-Better-Lookup-Performance)
  - [Merge Operator Implementation](https://github.com/facebook/rocksdb/wiki/Merge-Operator-Implementation)
  - [RocksDB Repairer](https://github.com/facebook/rocksdb/wiki/RocksDB-Repairer)
  - [Write Batch With Index](https://github.com/facebook/rocksdb/wiki/Write-Batch-With-Index)
  - [Two Phase Commit](https://github.com/facebook/rocksdb/wiki/Two-Phase-Commit-Implementation)
  - [Iterator's Implementation](https://github.com/facebook/rocksdb/wiki/Iterator-Implementation)
  - [Simulation Cache](https://github.com/facebook/rocksdb/wiki/Simulation-Cache)
  - [\[To Be Deprecated\] Persistent Read Cache](https://github.com/facebook/rocksdb/wiki/%5BTo-Be-Deprecated%5D-Persistent-Read-Cache)
  - [DeleteRange Implementation](https://github.com/facebook/rocksdb/wiki/DeleteRange-Implementation)
  - [unordered\_write](https://github.com/facebook/rocksdb/wiki/unordered_write)
- **Extending RocksDB**  - [RocksDB Configurable Objects](https://github.com/facebook/rocksdb/wiki/RocksDB-Configurable-Objects)
  - [The Customizable Class](https://github.com/facebook/rocksdb/wiki/The-Customizable-Class)
  - [Object Registry](https://github.com/facebook/rocksdb/wiki/Object-Registry)
- **RocksJava**  - [RocksJava Basics](https://github.com/facebook/rocksdb/wiki/RocksJava-Basics)
  - [Logging in RocksJava](https://github.com/facebook/rocksdb/wiki/Logging-in-RocksJava)
  - [JNI Debugging](https://github.com/facebook/rocksdb/wiki/JNI-Debugging)
  - [RocksJava API TODO](https://github.com/facebook/rocksdb/wiki/RocksJava-API-TODO)
  - [RocksJava Performance on Flash Storage](https://github.com/facebook/rocksdb/wiki/RocksJava-Performance-on-Flash-Storage)
  - [Tuning RocksDB from Java](https://github.com/facebook/rocksdb/wiki/Tuning-RocksDB-from-Java)
- **Performance**  - [Performance Benchmarks](https://github.com/facebook/rocksdb/wiki/Performance-Benchmarks)
  - [In Memory Workload Performance](https://github.com/facebook/rocksdb/wiki/RocksDB-In-Memory-Workload-Performance-Benchmarks)
  - [Read-Modify-Write (Merge) Performance](https://github.com/facebook/rocksdb/wiki/Read-Modify-Write-Benchmarks)
  - [Delete A Range Of Keys](https://github.com/facebook/rocksdb/wiki/Delete-A-Range-Of-Keys)
  - [Write Stalls](https://github.com/facebook/rocksdb/wiki/Write-Stalls)
  - [Pipelined Write](https://github.com/facebook/rocksdb/wiki/Pipelined-Write)
  - [MultiGet Performance](https://github.com/facebook/rocksdb/wiki/MultiGet-Performance)
  - [Tuning Guide](https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide)
  - [Memory usage in RocksDB](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB)
  - [Speed-Up DB Open](https://github.com/facebook/rocksdb/wiki/Speed-Up-DB-Open)
  - [Implement Queue Service Using RocksDB](https://github.com/facebook/rocksdb/wiki/Implement-Queue-Service-Using-RocksDB)
  - [Asynchronous IO](https://github.com/facebook/rocksdb/wiki/Asynchronous-IO)
  - [Off-peak in RocksDB](https://github.com/facebook/rocksdb/wiki/Daily-Off%E2%80%90peak-Time-Option)
- [Projects Being Developed](https://github.com/facebook/rocksdb/wiki/Projects-Being-Developed)
- **Misc**  - [Building on Windows](https://github.com/facebook/rocksdb/wiki/Building-on-Windows)
  - [Developing with an IDE](https://github.com/facebook/rocksdb/wiki/Developing-with-an-IDE)
  - [Open Projects](https://github.com/facebook/rocksdb/wiki/Open-Projects)
  - [Talks](https://github.com/facebook/rocksdb/wiki/Talks)
  - [Publication](https://github.com/facebook/rocksdb/wiki/Publication)
  - [Features Not in LevelDB](https://github.com/facebook/rocksdb/wiki/Features-Not-in-LevelDB)
  - [How to ask a performance-related question?](https://github.com/facebook/rocksdb/wiki/How-to-ask-a-performance-related-question)
  - [Articles about Rocks](https://github.com/facebook/rocksdb/wiki/Articles-about-Rocks)

### Clone this wiki locally