> This documentation is for an out-of-date version of Apache Flink. We recommend you use the latest [stable version](https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/checkpoints/).

# Checkpoints  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#checkpoints)

## Overview  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#overview)

Checkpoints make state in Flink fault tolerant by allowing state and the
corresponding stream positions to be recovered, thereby giving the application
the same semantics as a failure-free execution.

See [Checkpointing](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/checkpointing/) for how to enable and
configure checkpoints for your program.

To understand the differences between checkpoints and [savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/savepoints/) see [checkpoints vs. savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints_vs_savepoints/).

## Checkpoint Storage  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#checkpoint-storage)

When checkpointing is enabled, managed state is persisted to ensure consistent recovery in case of failures.
Where the state is persisted during checkpointing depends on the chosen **Checkpoint Storage**.

## Available Checkpoint Storage Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#available-checkpoint-storage-options)

Out of the box, Flink bundles these checkpoint storage types:

- _JobManagerCheckpointStorage_
- _FileSystemCheckpointStorage_

> If a checkpoint directory is configured `FileSystemCheckpointStorage` will be used, otherwise the system will use the `JobManagerCheckpointStorage`.

### The JobManagerCheckpointStorage  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#the-jobmanagercheckpointstorage)

The _JobManagerCheckpointStorage_ stores checkpoint snapshots in the JobManager’s heap.

It can be configured to fail the checkpoint if it goes over a certain size to avoid `OutOfMemoryError`’s on the JobManager. To set this feature, users can instantiate a `JobManagerCheckpointStorage` with the corresponding max size:

```java
new JobManagerCheckpointStorage(MAX_MEM_STATE_SIZE);
```

Limitations of the `JobManagerCheckpointStorage`:

- The size of each individual state is by default limited to 5 MB. This value can be increased in the constructor of the `JobManagerCheckpointStorage`.
- Irrespective of the configured maximal state size, the state cannot be larger than the Pekko frame size (see [Configuration](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/deployment/config/)).
- The aggregate state must fit into the JobManager memory.

The JobManagerCheckpointStorage is encouraged for:

- Local development and debugging
- Jobs that use very little state, such as jobs that consist only of record-at-a-time functions (Map, FlatMap, Filter, …). The Kafka Consumer requires very little state.

### The FileSystemCheckpointStorage  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#the-filesystemcheckpointstorage)

The _FileSystemCheckpointStorage_ is configured with a file system URL (type, address, path), such as “hdfs://namenode:40010/flink/checkpoints” or “file:///data/flink/checkpoints”.

Upon checkpointing, it writes state snapshots into files in the configured file system and directory. Minimal metadata is stored in the JobManager’s memory (or, in high-availability mode, in the metadata checkpoint).

If a checkpoint directory is specified, `FileSystemCheckpointStorage` will be used to persist checkpoint snapshots.

The `FileSystemCheckpointStorage` is encouraged for:

- All high-availability setups.

## Retained Checkpoints  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#retained-checkpoints)

Checkpoints are by default not retained and are only used to resume a
job from failures. They are deleted when a program is cancelled.
You can, however, configure periodic checkpoints to be retained.
Depending on the configuration these _retained_ checkpoints are _not_
automatically cleaned up when the job fails or is canceled.
This way, you will have a checkpoint around to resume from if your job fails.

```java
CheckpointConfig config = env.getCheckpointConfig();
config.setExternalizedCheckpointRetention(ExternalizedCheckpointRetention.RETAIN_ON_CANCELLATION);
```

The `ExternalizedCheckpointRetention` mode configures what happens with checkpoints when you cancel the job:

- **`ExternalizedCheckpointRetention.RETAIN_ON_CANCELLATION`**: Retain the checkpoint when the job is cancelled. Note that you have to manually clean up the checkpoint state after cancellation in this case.

- **`ExternalizedCheckpointRetention.DELETE_ON_CANCELLATION`**: Delete the checkpoint when the job is cancelled. The checkpoint state will only be available if the job fails.


### Directory Structure  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#directory-structure)

Similarly to [savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/savepoints/), a checkpoint consists
of a meta data file and, depending on the state backend, some additional data
files. The meta data file and data files are stored in the directory that is
configured via `execution.checkpointing.dir` in the configuration files,
and also can be specified for per job in the code.

The current checkpoint directory layout ( [introduced by FLINK-8531](https://issues.apache.org/jira/browse/FLINK-8531)) is as follows:

```yaml
/user-defined-checkpoint-dir
    /{job-id}
        |
        + --shared/
        + --taskowned/
        + --chk-1/
        + --chk-2/
        + --chk-3/
        ...
```

The **SHARED** directory is for state that is possibly part of multiple checkpoints, **TASKOWNED** is for state that must never be dropped by the JobManager, and **EXCLUSIVE** is for state that belongs to one checkpoint only.

> The checkpoint directory is not part of a public API and can be changed in the future release.

#### Configure globally via configuration files  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#configure-globally-via-configuration-files)

```yaml
execution.checkpointing.dir: hdfs:///checkpoints/
```

#### Configure for per job on the checkpoint configuration  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#configure-for-per-job-on-the-checkpoint-configuration)

```java
Configuration config = new Configuration();
config.set(CheckpointingOptions.CHECKPOINT_STORAGE, "filesystem");
config.set(CheckpointingOptions.CHECKPOINTS_DIRECTORY, "hdfs:///checkpoints-data/");
env.configure(config);
```

#### Configure with checkpoint storage instance  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#configure-with-checkpoint-storage-instance)

Alternatively, checkpoint storage can be set by specifying the desired checkpoint storage instance which allows for setting low level configurations such as write buffer sizes.

```java
Configuration config = new Configuration();
config.set(CheckpointingOptions.CHECKPOINT_STORAGE, "filesystem");
config.set(CheckpointingOptions.CHECKPOINTS_DIRECTORY, "hdfs:///checkpoints-data/");
config.set(CheckpointingOptions.FS_WRITE_BUFFER_SIZE, FILE_SIZE_THESHOLD);
env.configure(config);
```

### Resuming from a retained checkpoint  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/\#resuming-from-a-retained-checkpoint)

A job may be resumed from a checkpoint just as from a savepoint
by using the checkpoint’s meta data file instead (see the
[savepoint restore guide](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/savepoints/#resuming-from-savepoints)). Note that if the
meta data file is not self-contained, the jobmanager needs to have access to
the data files it refers to (see [Directory Structure](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/#directory-structure)
above).

```shell
$ bin/flink run -s :checkpointMetaDataPath [:runArgs]
```