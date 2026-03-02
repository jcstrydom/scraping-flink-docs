# Memory tuning guide  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#memory-tuning-guide)

In addition to the [main memory setup guide](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup/), this section explains how to set up memory
depending on the use case and which options are important for each case.

## Configure memory for standalone deployment  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-memory-for-standalone-deployment)

It is recommended to configure [total Flink memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup/#configure-total-memory)
( [`taskmanager.memory.flink.size`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#taskmanager-memory-flink-size) or [`jobmanager.memory.flink.size`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#jobmanager-memory-flink-size))
or its components for [standalone deployment](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/resource-providers/standalone/overview/) where you want to declare how much memory
is given to Flink itself. Additionally, you can adjust _JVM metaspace_ if it causes [problems](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_trouble/#outofmemoryerror-metaspace).

The _total Process memory_ is not relevant because _JVM overhead_ is not controlled by Flink or the deployment environment,
only physical resources of the executing machine matter in this case.

## Configure memory for containers  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-memory-for-containers)

It is recommended to configure [total process memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup/#configure-total-memory)
( [`taskmanager.memory.process.size`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#taskmanager-memory-process-size) or [`jobmanager.memory.process.size`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#jobmanager-memory-process-size))
for the containerized deployments ( [Kubernetes](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/resource-providers/standalone/kubernetes/) or [Yarn](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/resource-providers/yarn/)).
It declares how much memory in total should be assigned to the Flink _JVM process_ and corresponds to the size of the requested container.

Note If you configure the _total Flink memory_ Flink will implicitly add JVM memory components
to derive the _total process memory_ and request a container with the memory of that derived size.

> **Warning:** If Flink or user code allocates unmanaged off-heap (native) memory beyond the container size
> the job can fail because the deployment environment can kill the offending containers.

See also description of [container memory exceeded](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_trouble/#container-memory-exceeded) failure.

## Configure memory for Netty4  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-memory-for-netty4)

As the version of Apache Pekko was updated, now Flink RPC also uses Netty4. Netty4 introduces some changes regarding byte buffers compared to Netty3 that is worth mentioning.
Mainly Netty4 brought pooled byte buffers, which enables better performance, but it allocates slightly more memory.

### Configure byte buffer allocator type  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-byte-buffer-allocator-type)

> Be aware that specifying the byte buffer allocator type will affect both Flink RPC and [Flink’s shuffle](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/%28//nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/execution_mode/#task-scheduling-and-network-shuffle%29) performance!

In highly resource-limited use-cases it might make sense to fine-tune these configurations.
This can be done via setting the following JVM property for the TaskManager(s) and/or JobManager(s): `org.apache.flink.shaded.netty4.io.netty.allocator.type`.
The possible allocator types are the following:

- `pooled`: use `PooledByteBufAllocator.DEFAULT`
- `unpooled`: use `UnpooledByteBufAllocator.DEFAULT`
- `adaptive`: use `AdaptiveByteBufAllocator`

#### Example  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#example)

```yaml
# In <flink-root-dir>/conf/config.yaml
env:
  java:
    opts:
      jobmanager: -Dorg.apache.flink.shaded.netty4.io.netty.allocator.type=unpooled
      taskmanager: -Dorg.apache.flink.shaded.netty4.io.netty.allocator.type=unpooled
```

For more information about these byte buffer allocators please check the relevant parts of the [Netty4 documentation](https://netty.io/wiki/new-and-noteworthy-in-4.0.html#buffer-api-changes).

### Enable reflection in JDK >= 11  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#enable-reflection-in-jdk--11)

Since by default Flink has `--add-opens=java.base/java.lang.reflect=ALL-UNNAMED`, using reflection in Netty4 should also not be a problem in most environments.
Setting `org.apache.flink.shaded.netty4.io.netty.tryReflectionSetAccessible` enables some optimizations that reduces GC pressure, and improves performance.

#### Example  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#example-1)

```yaml
# In <flink-root-dir>/conf/config.yaml
env:
  java:
    opts:
      jobmanager: -Dorg.apache.flink.shaded.netty4.io.netty.tryReflectionSetAccessible=true
      taskmanager: -Dorg.apache.flink.shaded.netty4.io.netty.tryReflectionSetAccessible=true
```

## Configure memory for state backends  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-memory-for-state-backends)

This is only relevant for TaskManagers.

When deploying a Flink streaming application, the type of [state backend](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/state/state_backends/) used
will dictate the optimal memory configurations of your cluster.

### HashMap state backend  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#hashmap-state-backend)

When running a stateless job or using the [HashMapStateBackend](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/state/state_backends/#the-hashmapstatebackend)), set [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory) to zero.
This will ensure that the maximum amount of heap memory is allocated for user code on the JVM.

### RocksDB state backend  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#rocksdb-state-backend)

The [EmbeddedRocksDBStateBackend](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/state/state_backends/#the-embeddedrocksdbstatebackend) uses native memory. By default,
RocksDB is set up to limit native memory allocation to the size of the [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory).
Therefore, it is important to reserve enough _managed memory_ for your state. If you disable the default RocksDB memory control,
TaskManagers can be killed in containerized deployments if RocksDB allocates memory above the limit of the requested container size
(the [total process memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup/#configure-total-memory)).
See also [how to tune RocksDB memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/state/large_state_tuning/#tuning-rocksdb-memory)
and [state.backend.rocksdb.memory.managed](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#state-backend-rocksdb-memory-managed).

## Configure memory for batch jobs  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_tuning/\#configure-memory-for-batch-jobs)

This is only relevant for TaskManagers.

Flink’s batch operators leverage [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory) to run more efficiently.
In doing so, some operations can be performed directly on raw data without having to be deserialized into Java objects.
This means that [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory) configurations have practical effects
on the performance of your applications. Flink will attempt to allocate and use as much [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory)
as configured for batch jobs but not go beyond its limits. This prevents `OutOfMemoryError`’s because Flink knows precisely
how much memory it has to leverage. If the [managed memory](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/memory/mem_setup_tm/#managed-memory) is not sufficient,
Flink will gracefully spill to disk.