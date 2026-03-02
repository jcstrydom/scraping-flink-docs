[Skip to content](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction) to refresh your session.Dismiss alert

{{ message }}

[facebook](https://github.com/facebook)/ **[rocksdb](https://github.com/facebook/rocksdb)** Public

- [Notifications](https://github.com/login?return_to=%2Ffacebook%2Frocksdb) You must be signed in to change notification settings
- [Fork\\
6.7k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)
- [Star\\
31.4k](https://github.com/login?return_to=%2Ffacebook%2Frocksdb)


# Leveled Compaction

[Jump to bottom](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#wiki-pages-box)

Changyu Bi edited this page on Nov 14, 2023Nov 14, 2023
·
[38 revisions](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction/_history)

## Structure of the files

[Permalink: Structure of the files](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#structure-of-the-files)

Files on disk are organized in multiple levels. We call them level-1, level-2, etc, or L1, L2, etc, for short. A special level-0 (or L0 for short) contains files just flushed from in-memory write buffer (memtable). Each level (except level 0) is one data sorted run:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/level_structure.png)

Inside each level (except level 0), data is range partitioned into multiple SST files:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/level_files.png)

The level is a sorted run because keys in each SST file are sorted (See [Block-based Table Format](https://github.com/facebook/rocksdb/wiki/Rocksdb-BlockBasedTable-Format) as an example). To identify a position for a key, we first binary search the start/end key of all files to identify which file possibly contains the key, and then binary search inside the file to locate the exact position. In all, it is a full binary search across all the keys in the level.

All non-0 levels have target sizes. Compaction's goal will be to restrict data size of those levels to be under the target. The size targets are usually exponentially increasing:
![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/level_targets.png)

## Compactions

[Permalink: Compactions](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#compactions)

Compaction triggers when number of L0 files reaches `level0_file_num_compaction_trigger`, files of L0 will be merged into L1. Normally we have to pick up all the L0 files because they usually are overlapping:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/pre_l0_compaction.png)

After the compaction, it may push the size of L1 to exceed its target:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/post_l0_compaction.png)

In this case, we will pick at least one file from L1 and merge it with the overlapping range of L2. The result files will be placed in L2:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/pre_l1_compaction.png)

If the results push the next level's size exceeds the target, we do the same as previously -- pick up a file and merge it into the next level:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/post_l1_compaction.png)

and then

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/pre_l2_compaction.png)

and then

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/post_l2_compaction.png)

Multiple compactions can be executed in parallel if needed:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/multi_thread_compaction.png)

Maximum number of compactions allowed is controlled by `max_background_compactions`.

However, L0 to L1 compaction is not parallelized by default. In some cases, it may become a bottleneck that limit the total compaction speed. RocksDB supports subcompaction-based parallelization only for L0 to L1. To enable it, users can set `max_subcompactions` to more than 1. Then, we'll try to partition the range and use multiple threads to execute it:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/subcompaction.png)

See more about subcompaction in [https://github.com/facebook/rocksdb/wiki/Subcompaction](https://github.com/facebook/rocksdb/wiki/Subcompaction).

## Compaction Picking

[Permalink: Compaction Picking](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#compaction-picking)

When multiple levels trigger the compaction condition, RocksDB needs to pick which level to compact first. A score is generated for each level:

- For non-zero levels, the score is total size of the level divided by the target size. If there are already files picked that are being compacted into the next level, the size of those files is not included into the total size, because they will soon go away.

- for level-0, the score is the total number of files, divided by `level0_file_num_compaction_trigger`, or total size over `max_bytes_for_level_base`, which ever is larger. (if the file size is smaller than `level0_file_num_compaction_trigger`, compaction won't trigger from level 0, no matter how big the score is.)


We compare the score of each level, and the level with highest score takes the priority to compact.

Which file(s) to compact from the level are explained in [Choose Level Compaction Files](https://github.com/facebook/rocksdb/wiki/Choose-Level-Compaction-Files).

## Option `level_compaction_dynamic_level_bytes` and Levels' Target Size

[Permalink: Option level_compaction_dynamic_level_bytes and Levels' Target Size](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#option-level_compaction_dynamic_level_bytes-and-levels-target-size)

There are two flavors of leveled compaction depending on the option `level_compaction_dynamic_level_bytes`:

### `level_compaction_dynamic_level_bytes` is `false`

[Permalink: level_compaction_dynamic_level_bytes is false](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#level_compaction_dynamic_level_bytes-is-false)

If `level_compaction_dynamic_level_bytes` is false, then level targets are determined as following: L1's target will be `max_bytes_for_level_base`. And then `Target_Size(Ln+1) = Target_Size(Ln) * max_bytes_for_level_multiplier * max_bytes_for_level_multiplier_additional[n]`. `max_bytes_for_level_multiplier_additional` is by default all 1.

For example, if `max_bytes_for_level_base = 16384`, `max_bytes_for_level_multiplier = 10` and `max_bytes_for_level_multiplier_additional` is not set, then size of L1, L2, L3 and L4 will be 16384, 163840, 1638400, and 16384000, respectively.

### `level_compaction_dynamic_level_bytes` is `true` (Recommended, default since version 8.4)

[Permalink: level_compaction_dynamic_level_bytes is true (Recommended, default since version 8.4)](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#level_compaction_dynamic_level_bytes-is-true-recommended-default-since-version-84)

Note that `max_bytes_for_level_multiplier_additional` is ignored when this option is true.

#### Guaranteed Space Amp Upper Bound

[Permalink: Guaranteed Space Amp Upper Bound](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#guaranteed-space-amp-upper-bound)

Target size of the last level (`num_levels`-1) will be actual size of largest level (which is usually the last level). And then `Target_Size(Ln-1) = Target_Size(Ln) / max_bytes_for_level_multiplier`. We won't fill any level whose target will be lower than `max_bytes_for_level_base / max_bytes_for_level_multiplier`. These levels will be kept empty and all L0 compaction will skip those levels and directly go to the first level with valid target size.

For example, if `max_bytes_for_level_base` is 1GB, `num_levels=6` and the actual size of last level is 276GB, then the target size of L1-L6 will be 0, 0, 0.276GB, 2.76GB, 27.6GB and 276GB, respectively.

This is to guarantee a stable LSM-tree structure, where 90% of data is stored in the last level, which can't be guaranteed if `level_compaction_dynamic_level_bytes` is `false`. For example, in the previous example:

![](https://github.com/facebook/rocksdb/raw/gh-pages-old/pictures/dynamic_level.png)

We can guarantee 90% of data is stored in the last level, 9% data in the second last level. There will be multiple benefits to it.

#### More Adaptive Compaction To Write Traffic

[Permalink: More Adaptive Compaction To Write Traffic](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#more-adaptive-compaction-to-write-traffic)

To help leveled compaction handle temporary spike of writes more smoothly, we make the following adjustment to target size when determining compaction priority.
With `level_compaction_dynamic_level_bytes = true`, when computing compaction score, we include `total_downcompact_bytes` as part of target size, i.e., compaction score of Ln becomes `Ln size / (Ln target size + total_downcompact_bytes)`. The value of `total_downcompact_bytes` for Ln is the estimated total bytes to be compacted down from L0 ... Ln-1 to Ln. When write traffic is heavy, there is more compaction debt. `total_downcompact_bytes` will be larger for higher levels which makes lower level prioritized for compaction to handle the heavy write traffic.

Note that leveled compaction still cannot efficiently handle write rate that is too much higher than capacity based on the configuration. Works on going to further improve it.

#### Migrating From `level_compaction_dynamic_level_bytes=false` To `level_compaction_dynamic_level_bytes=true`

[Permalink: Migrating From level_compaction_dynamic_level_bytes=false To level_compaction_dynamic_level_bytes=true](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#migrating-from-level_compaction_dynamic_level_bytesfalse-to-level_compaction_dynamic_level_bytestrue)

Before RocksDB version 8.2, users are expected to do a full manual compaction to compact all files into the last level of LSM. Then they can reopen the DB to turn on this option.

RocksDB version 8.2 adds support for automatic migration when this option is turned on. There are two steps for this migration:

1. During DB open, files in an LSM are trivially moved down to fill the LSM starting from the last level. For example, if before DB open, an LSM with 7 levels looks like:

```
L0:
L1: F1
L2:
L3: F2
L4: F3
L5: F4 F5 F6
L6:
```

After the trivial moves are done during DB open, the LSM becomes:

```
L0:
L1:
L2:
L3: F1
L4: F2
L5: F3
L6: F4 F5 F6
```

2. **Automatic Drain Of Unnecessary Levels:** From the above we know that any level with `target size < max_bytes_for_level_base / max_bytes_for_level_multiplier` are not needed and should be kept empty. It is possible that a DB is using more levels than needed (remember that `level_compaction_dynamic_level_bytes=false` does not guarantee space amp compared to `level_compaction_dynamic_level_bytes=true`). This can also happen when a user deletes a lot of DB data. Since RocksDB version 8.2, RocksDB will try to drain these unnecessary levels in the background through compaction. These draining compactions are assigned lower priorities and happen when there is no other background compaction needed. For example, suppose that in the above LSM, only L6, L5 and L4 are needed. Then L3 will be gradually compacted down to make a "stable LSM structure" that is expected when `level_compaction_dynamic_level_bytes=true`.

```
Support max_bytes_for_level_base = 10MB, max_bytes_for_level_multiplier = 2. Then L3 is not needed for the LSM below and will be compacted down during background compactions.

L0:
L1:
L2:
L3: F1 (target = 4MB < max_bytes_for_level_base / max_bytes_for_level_multiplier)
L4: F2 (target = 8MB)
L5: F3 (target = 16MB)
L6: F4 F5 F6 (actual size = 32MB, target size = 32MB)
```

Note that this migration automation also works when a user is switching from Universal to Leveled compaction as long as the number of levels is not smaller than number of non-empty levels in the LSM.

## Intra-L0 Compaction

[Permalink: Intra-L0 Compaction](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#intra-l0-compaction)

Too many L0 files hurt read performance in most queries. To address the issue, RocksDB may choose to compact some L0 files together to a larger file. This sacrifices write amplification by one but may significantly improve read amplification in L0 and in turn increase the capability RocksDB can hold data in L0. This would generate other benefits which would be explained below. Additional write amplification of 1 is far smaller than the usual write amplification of leveled compaction, which is often larger than 10. So we believe it is a good trade-off.
Maximum size of Intra-L0 compaction is also bounded by `options.max_compaction_bytes`. If the option takes a reasonable value, total L0 size will still be bounded, even with Intra-L0 files.

## TTL

[Permalink: TTL](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#ttl)

A file could exist in the LSM tree without going through the compaction process for a really long time if there are no updates to the data in the file's key range. For example, in certain use cases, the keys are "soft deleted" -- set the values to be empty instead of actually issuing a Delete. There might not be any more writes to this "deleted" key range, and if so, such data could remain in the LSM for a really long time resulting in wasted space.

A dynamic `ttl` column-family option has been introduced to solve this problem. Files (and, in turn, data) older than TTL will be scheduled for compaction when there is no other background work. This will make the data go through the regular compaction process, reach to the bottommost level and get rid of old unwanted data.
This also has the (good) side-effect of all the data in the non-bottommost level being newer than ttl, and all data in the bottommost level older than ttl. Note that it could lead to more writes as RocksDB would schedule more compactions.

## Periodic compaction

[Permalink: Periodic compaction](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction#periodic-compaction)

If compaction filter is present, RocksDB ensures that data go through compaction filter after a certain amount of time. This is achieved via `options.periodic_compaction_seconds`. Setting it to 0 disables this feature. Leaving it the default value, i.e. UINT64\_MAX - 1, indicates that RocksDB controls the feature. At the moment, RocksDB will change the value to 30 days. Whenever RocksDB tries to pick a compaction, files older than 30 days will be eligible for compaction and be compacted to the same level when there is no other background work.

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