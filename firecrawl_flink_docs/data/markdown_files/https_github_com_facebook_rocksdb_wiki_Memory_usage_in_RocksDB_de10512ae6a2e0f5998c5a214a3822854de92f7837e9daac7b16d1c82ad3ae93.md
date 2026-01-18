[Skip to content](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB) to refresh your session.Dismiss alert

{{ message }}

[facebook](https://github.com/facebook)/ **[rocksdb](https://github.com/facebook/rocksdb)** Public

- [Notifications](https://github.com/login?return_to=%2Ffacebook%2Frocksdb) You must be signed in to change notification settings
- [Fork\\
6.7k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)
- [Star\\
31.4k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)


# Memory usage in RocksDB

[Jump to bottom](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#wiki-pages-box)

Yu Zhang edited this page on Jan 23, 2025Jan 23, 2025
·
[18 revisions](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB/_history)

Here we try to explain how RocksDB uses memory. There are a couple of components in RocksDB that contribute to memory usage:

1. Block cache
2. Indexes and bloom filters
3. Memtables
4. Blocks pinned by iterators

We will describe each of them in turn.

For some ongoing projects that improve memory efficiency. See [Improving Memory Efficiency](https://github.com/facebook/rocksdb/wiki/Projects-Being-Developed#improving-memory-efficiency).

For operational purposes, we've been working towards charging all kinds of memory usage to a single RocksDB memory budget. This started out with the memtables but has been extended to various other kinds of allocations since then. See [https://github.com/facebook/rocksdb/blob/68112b3beb885c9ec8bc410e15b05e7e27e3c9ee/include/rocksdb/table.h#L323-L388](https://github.com/facebook/rocksdb/blob/68112b3beb885c9ec8bc410e15b05e7e27e3c9ee/include/rocksdb/table.h#L323-L388) for more.

## Block cache

[Permalink: Block cache](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#block-cache)

Block cache is where RocksDB caches uncompressed data blocks. You can configure block cache's size by setting block\_cache property of BlockBasedTableOptions:

```
rocksdb::BlockBasedTableOptions table_options;
table_options.block_cache = rocksdb::NewLRUCache(1 * 1024 * 1024 * 1024LL);
rocksdb::Options options;
options.table_factory.reset(new rocksdb::BlockBasedTableFactory(table_options));
```

If the data block is not found in block cache, RocksDB reads it from file using buffered IO. That means it also uses the OS's page cache for raw file blocks, usually containing compressed data. In a way, RocksDB's cache is two-tiered: block cache and page cache. Counter-intuitively, decreasing block cache size will not increase IO. The memory saved will likely be used for page cache, so even more data will be cached. However, CPU usage might grow because RocksDB needs to decompress pages it reads from page cache.

To learn how much memory block cache is using, you can call a function GetUsage() on block cache object or call getProperty() on DB object:

```
table_options.block_cache->GetUsage();
db->getProperty("rocksdb.block-cache-usage")
```

In MongoRocks, you can get the size of block cache by calling

```
> db.serverStatus()["rocksdb"]["block-cache-usage"]
```

## Indexes and filter blocks

[Permalink: Indexes and filter blocks](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#indexes-and-filter-blocks)

Indexes and filter blocks can be big memory users and by default they don't count in memory you allocate for block cache. This can sometimes cause confusion for users: you allocate 10GB for block cache, but RocksDB is using 15GB of memory. The difference is usually explained by index and bloom filter blocks.

We continuously make index and filter more compact. To take advantage of recent improvements, use more recent format version through `BlockBasedTableOptions.format_version`. Some other newer features need to be explicitly enabled:

- Set `BlockBasedTableOptions.optimize_filters_for_memory` for more jemalloc friendly bloom filter sizing.
- Also consider to use the new [Ribbon Filter](https://github.com/facebook/rocksdb/blob/003e72b2019c6727c3e89b1d0f85d8fd75f698ac/include/rocksdb/filter_policy.h#L219-L236)

See [RocksDB Bloom Filter](https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter) for more information on bloom filters.

Here's how you can roughly calculate and manage sizes of index and filter blocks:

1. For each data block we store three information in the index: a key, a offset and size. Therefore, there are two ways you can reduce the size of the index. If you increase block size, the number of blocks will decrease, so the index size will also reduce linearly. By default our block size is 4KB, although we usually run with 16-32KB in production. The second way to reduce the index size is the reduce key size, although that might not be an option for some use-cases.
2. Calculating the size of filter blocks is easy. If you configure bloom filters with 10 bits per key (default, which gives 1% of false positives), the bloom filter size is `number_of_keys * 10 bits`. There's one trick you can play here, though. If you're certain that Get() will mostly find a key you're looking for, you can set `options.optimize_filters_for_hits = true`. With this option turned on, we will not build bloom filters on the last level, which contains 90% of the database. Thus, the memory usage for bloom filters will be 10X less. You will pay one IO for each Get() that doesn't find data in the database, though.

There are two options that configure how much index and filter blocks we fit in memory:

1. If you set `cache_index_and_filter_blocks` to true, index and filter blocks will be stored in block cache, together with all other data blocks. This also means they can be paged out. If your access pattern is very local (i.e. you have some very cold key ranges), this setting might make sense. However, in most cases it will hurt your performance, since you need to have index and filter to access a certain file. An exception to `cache_index_and_filter_blocks=true` is for L0 when setting `pin_l0_filter_and_index_blocks_in_cache=true`, which can be a good compromise setting.
2. If `cache_index_and_filter_blocks` is false (which is default), the number of index/filter blocks is controlled by option `max_open_files`. If you are certain that your ulimit will always be bigger than number of files in the database, we recommend setting `max_open_files` to -1, which means infinity. This option will preload all filter and index blocks and will not need to maintain LRU of files. Setting `max_open_files` to -1 will get you the best possible performance.

However, regardless of options, by default each column family in each database instance will have its own block cache instance, with its own memory limit. To share a single block cache, set `block_cache` in your various `BlockBasedTableOptions` to use the same shared\_ptr, or share the same `BlockBasedTableOptions` for your various factories, or share the same BlockBasedTableFactory for `table_factory` in your various `Options` or `ColumnFamilyOptions`, etc.

To learn how much memory is being used by index and filter blocks, you can use RocksDB's GetProperty() API:

```
std::string out;
db->GetProperty("rocksdb.estimate-table-readers-mem", &out);
```

In MongoRocks, just call this API from the mongo shell:

```
> db.serverStatus()["rocksdb"]["estimate-table-readers-mem"]
```

In [partitioned index/filters](https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters) the indexes and filters for each partition are always stored in block cache. The top-level index can be configured to be stored in heap or block cache via `cache_index_and_filter_blocks`.

## Memtable

[Permalink: Memtable](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#memtable)

You can think of memtables as in-memory write buffers. Each new key-value pair is first written to the memtable. Memtable size is controlled by the option `write_buffer_size`. It's usually not a big memory consumer unless using many column families and/or database instances. However, memtable size inversely affects write amplification: more memory to the memtable yields less write amplification. If you increase your memtable size, be sure to also increase your L1 size! L1 size is controlled by the option `max_bytes_for_level_base`.

To get the current memtable size, you can use:

```
std::string out;
db->GetProperty("rocksdb.cur-size-all-mem-tables", &out);
```

In MongoRocks, the equivalent call is

```
> db.serverStatus()["rocksdb"]["cur-size-all-mem-tables"]
```

Since version 5.6, you can cost the memory budget of memtables as a part of block cache. Check [Write Buffer Manager](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) for the information.

Similar to block cache, by default memtable sizes are per column family, per database instance. Use a [Write Buffer Manager](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) to cap memtable memory across column families and/or database instances.

## Blocks pinned by iterators

[Permalink: Blocks pinned by iterators](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#blocks-pinned-by-iterators)

Blocks pinned by iterators usually don't contribute much to the overall memory usage. However, in some cases, when you have 100k read transactions happening simultaneously, it might put a strain on memory. Memory usage for pinned blocks is easy to calculate for most cases. Each iterator pins exactly one data block for each L0 file plus one data block for each L1+ level. So the total memory usage from pinned blocks is approximately `num_iterators * block_size * ((num_levels-1) + num_l0_files)`. However when `ReadOptions.pin_data` is set to true and the underlying SST file format supports it, an iterator could be pinning all iterated blocks through its lifetime. To get the statistics about this pinned memory usage, call GetPinnedUsage() on block cache object or call getProperty() on db object:

```
    table_options.block_cache->GetPinnedUsage();
    db->getProperties("rocksdb.block-cache-pinned-usage");
```

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

You can’t perform that action at this time.