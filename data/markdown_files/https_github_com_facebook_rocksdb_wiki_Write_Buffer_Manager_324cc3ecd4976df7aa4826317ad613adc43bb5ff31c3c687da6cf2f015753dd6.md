[Skip to content](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) to refresh your session.Dismiss alert

{{ message }}

[facebook](https://github.com/facebook)/ **[rocksdb](https://github.com/facebook/rocksdb)** Public

- [Notifications](https://github.com/login?return_to=%2Ffacebook%2Frocksdb) You must be signed in to change notification settings
- [Fork\\
6.7k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)
- [Star\\
31.4k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)


# Write Buffer Manager

[Jump to bottom](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#wiki-pages-box)

Akanksha Mahajan edited this page on Oct 17, 2021Oct 18, 2021
·
[14 revisions](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager/_history)

Write buffer manager helps users control the total memory used by memtables across multiple column families and/or DB instances.
Users can enable this control by 2 ways:

1. Limit the total memtable usage across multiple column families and DBs under a threshold.
2. Cost the memtable memory usage to block cache so that memory of RocksDB can be capped by the single limit.

The usage of a write buffer manager is similar to rate\_limiter and sst\_file\_manager. Users can create one write buffer manager object and pass it to all the options of column families or DBs whose memtable size they want to be controlled by this object.

For more details refer, [write\_buffer\_manager option](https://github.com/facebook/rocksdb/blob/f35f7f2704d9803908de7eb8864f260312d173b4/include/rocksdb/options.h#L761) and [write\_buffer\_manager.h](https://github.com/facebook/rocksdb/blob/main/include/rocksdb/write_buffer_manager.h)

## Limit total memory of memtables

[Permalink: Limit total memory of memtables](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#limit-total-memory-of-memtables)

A memory limit is given when creating the write buffer manager object. RocksDB will try to limit the total memory to under this limit.

In version 5.6 or higher, a flush will be triggered on one column family of the DB you are inserting to,

1. If mutable memtable size exceeds about 90% of the limit,
2. If the total memory is over the limit, more aggressive flush may also be triggered only if the mutable memtable size also exceeds 50% of the limit. Both checks are needed because if already more than half memory is being flushed, triggering more flush may not help.

Before version 5.6, a flush will be triggered if the total mutable memtable size exceeds the limit.

In version 5.6 or higher, the total memory is counted as total memory allocated in the arena, even if some of that may not yet be used by memtable. In earlier versions, the memory is counted as memory actually used by memtables.

## Cost memory used in memtable to block cache

[Permalink: Cost memory used in memtable to block cache](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#cost-memory-used-in-memtable-to-block-cache)

Since version 5.6, users can set up RocksDB to cost memory used by memtables to block cache. This can happen no matter whether you enable memtable memory limit or not. This option is added to manage memory (memtables + block cache) under a single limit.

In most cases, blocks that are actually used in block cache are just a smaller percentage than data cached in block cache, so when users enable this feature, the block cache capacity will cover the memory usage for both block cache and memtables. If users also enable `cache_index_and_filter_blocks`, then the three major types of memory of RocksDB (cache\_index\_and\_filter\_blocks, memtables and data blocks cached) will be capped by the single cap.

### Implementation:

[Permalink: Implementation:](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#implementation)

For every, let's say 1MB memory allocated memtable, WriteBufferManager will put dummy 1MB entries (empty) to the block cache so that the block cache can track the size correctly for memtables and evict blocks to make room if needed. In case the memory used by the memtable shrinks, WriteBufferManager will not immediately remove the dummy blocks but shrink memory cost in the block cache if the total memory used by memtables is less than 3/4 of what we reserve in the block cache. We do this because we don't want to free the memory costed in the block cache immediately when a memtable is freed, as block cache insertion is expensive and might happen again in a very near future due to a memtable usage increase soon. We want to shrink the memory cost in block cache when the memory is unlikely to come back.

To enable this feature,

- pass the block cache you are using to the WriteBufferManager you are going to use.
- still pass the parameter of WriteBufferManager as the maximum memory you want RocksDB to use for memtables.
- set the capacity of your block cache to be the sum of the memory used for cached data blocks and memtables.

\`
WriteBufferManager(size\_t buffer\_size, std::shared\_ptr cache = {})

## Stalls

[Permalink: Stalls](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager#stalls)

WriteBufferManager provides an option `allow_stall`that can be passed to WriteBufferManager constructor. If set true, it will enable stalling of all writers when memory usage exceeds buffer\_size (soft limit). It will wait for flush to complete and memory usage to drop down. Applications can avoid it by setting `no_slowdown = true` in `WriteOptions`

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