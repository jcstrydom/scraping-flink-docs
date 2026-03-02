Type Parameters:`OUT` \- The output type of the operatorAll Superinterfaces:`CheckpointListener`, `KeyContext`, `Serializable`All Known Subinterfaces:`MultipleInputStreamOperator<OUT>`, `OneInputStreamOperator<IN,OUT>`, `TwoInputStreamOperator<IN1,IN2,OUT>`, `YieldingOperator<OUT>`All Known Implementing Classes:`AbstractArrowPythonAggregateFunctionOperator`, `AbstractAsyncKeyOrderedStreamOperator`, `AbstractAsyncRunnableStreamOperator`, `AbstractAsyncStateStreamingJoinOperator`, `AbstractAsyncStateStreamOperator`, `AbstractAsyncStateStreamOperatorV2`, `AbstractAsyncStateUdfStreamOperator`, `AbstractEmbeddedDataStreamPythonFunctionOperator`, `AbstractEmbeddedPythonFunctionOperator`, `AbstractEmbeddedStatelessFunctionOperator`, `AbstractExternalDataStreamPythonFunctionOperator`, `AbstractExternalOneInputPythonFunctionOperator`, `AbstractExternalPythonFunctionOperator`, `AbstractExternalTwoInputPythonFunctionOperator`, `AbstractMapBundleOperator`, `AbstractOneInputEmbeddedPythonFunctionOperator`, `AbstractOneInputPythonFunctionOperator`, `AbstractProcessTableOperator`, `AbstractPythonFunctionOperator`, `AbstractPythonScalarFunctionOperator`, `AbstractPythonStreamAggregateOperator`, `AbstractPythonStreamGroupAggregateOperator`, `AbstractStatelessFunctionOperator`, `AbstractStreamArrowPythonBoundedRangeOperator`, `AbstractStreamArrowPythonBoundedRowsOperator`, `AbstractStreamArrowPythonOverWindowAggregateFunctionOperator`, `AbstractStreamingJoinOperator`, `AbstractStreamingWriter`, `AbstractStreamOperator`, `AbstractStreamOperatorV2`, `AbstractTwoInputEmbeddedPythonFunctionOperator`, `AbstractUdfStreamOperator`, `AggregateWindowOperator`, `AlignedWindowTableFunctionOperator`, `ArrowPythonScalarFunctionOperator`, `AsyncEvictingWindowOperator`, `AsyncIntervalJoinOperator`, `AsyncKeyedCoProcessOperator`, `AsyncKeyedCoProcessOperatorWithWatermarkDelay`, `AsyncKeyedProcessOperator`, `AsyncStateStreamingJoinOperator`, `AsyncStateTableStreamOperator`, `AsyncStateWindowAggOperator`, `AsyncStateWindowJoinOperator`, `AsyncStreamFlatMap`, `AsyncWaitOperator`, `AsyncWindowOperator`, `BaseKeyedProcessOperator`, `BaseKeyedTwoInputNonBroadcastProcessOperator`, `BaseKeyedTwoOutputProcessOperator`, `BaseTwoInputStreamOperatorWithStateRetention`, `BatchArrowPythonGroupAggregateFunctionOperator`, `BatchArrowPythonGroupWindowAggregateFunctionOperator`, `BatchArrowPythonOverWindowAggregateFunctionOperator`, `BatchCoBroadcastWithKeyedOperator`, `BatchCoBroadcastWithNonKeyedOperator`, `BatchCompactCoordinator`, `BatchCompactOperator`, `BatchFileWriter`, `BatchGroupedReduceOperator`, `BatchMultipleInputStreamOperator`, `BootstrapStreamTaskRunner`, `BroadcastStateBootstrapOperator`, `BufferDataOverWindowOperator`, `CacheTransformationTranslator.IdentityStreamOperator`, `CacheTransformationTranslator.NoOpStreamOperator`, `CepOperator`, `CoBroadcastWithKeyedOperator`, `CoBroadcastWithNonKeyedOperator`, `CollectSinkOperator`, `CompactCoordinator`, `CompactCoordinator`, `CompactCoordinatorStateHandler`, `CompactFileWriter`, `CompactOperator`, `CompactorOperator`, `CompactorOperatorStateHandler`, `ConstraintEnforcer`, `ContinuousFileReaderOperator`, `CoProcessOperator`, `CoStreamFlatMap`, `CoStreamMap`, `DelegateOperatorTransformation.DelegateOperator`, `DynamicFilteringDataCollectorOperator`, `EmbeddedPythonBatchCoBroadcastProcessOperator`, `EmbeddedPythonBatchKeyedCoBroadcastProcessOperator`, `EmbeddedPythonCoProcessOperator`, `EmbeddedPythonKeyedCoProcessOperator`, `EmbeddedPythonKeyedProcessOperator`, `EmbeddedPythonProcessOperator`, `EmbeddedPythonScalarFunctionOperator`, `EmbeddedPythonTableFunctionOperator`, `EmbeddedPythonWindowOperator`, `EvictingWindowOperator`, `ExternalPythonBatchCoBroadcastProcessOperator`, `ExternalPythonBatchKeyedCoBroadcastProcessOperator`, `ExternalPythonCoProcessOperator`, `ExternalPythonKeyedCoProcessOperator`, `ExternalPythonKeyedProcessOperator`, `ExternalPythonProcessOperator`, `FusionStreamOperatorBase`, `GenericWriteAheadSink`, `GlobalCommitterOperator`, `GlobalRuntimeFilterBuilderOperator`, `GroupReduceOperator`, `HashJoinOperator`, `InputConversionOperator`, `IntervalJoinOperator`, `KeyedCoProcessOperator`, `KeyedCoProcessOperatorWithWatermarkDelay`, `KeyedMapBundleOperator`, `KeyedProcessOperator`, `KeyedProcessOperator`, `KeyedSortPartitionOperator`, `KeyedStateBootstrapOperator`, `KeyedTwoInputBroadcastProcessOperator`, `KeyedTwoInputNonBroadcastProcessOperator`, `KeyedTwoOutputProcessOperator`, `LegacyKeyedCoProcessOperator`, `LegacyKeyedProcessOperator`, `LimitOperator`, `LocalRuntimeFilterBuilderOperator`, `LocalSlicingWindowAggOperator`, `MapBundleOperator`, `MapPartitionOperator`, `MiniBatchStreamingJoinOperator`, `MultipleInputStreamOperatorBase`, `NonBufferOverWindowOperator`, `OneInputWindowProcessOperator`, `OutputConversionOperator`, `PartitionAggregateOperator`, `PartitionCommitter`, `PartitionReduceOperator`, `ProcessOperator`, `ProcessOperator`, `ProcessRowTableOperator`, `ProcessSetTableOperator`, `ProcTimeMiniBatchAssignerOperator`, `ProcTimeSortOperator`, `PythonScalarFunctionOperator`, `PythonStreamGroupAggregateOperator`, `PythonStreamGroupTableAggregateOperator`, `PythonStreamGroupWindowAggregateOperator`, `PythonTableFunctionOperator`, `QueryableAppendingStateOperator`, `QueryableValueStateOperator`, `RankOperator`, `RowKindSetter`, `RowTimeMiniBatchAssginerOperator`, `RowTimeSortOperator`, `SinkOperator`, `SinkUpsertMaterializer`, `SinkUpsertMaterializerV2`, `SortLimitOperator`, `SortMergeJoinOperator`, `SortOperator`, `SortPartitionOperator`, `SourceOperator`, `StateBootstrapOperator`, `StateBootstrapWrapperOperator`, `StreamArrowPythonGroupWindowAggregateFunctionOperator`, `StreamArrowPythonProcTimeBoundedRangeOperator`, `StreamArrowPythonProcTimeBoundedRowsOperator`, `StreamArrowPythonRowTimeBoundedRangeOperator`, `StreamArrowPythonRowTimeBoundedRowsOperator`, `StreamFilter`, `StreamFlatMap`, `StreamGroupedReduceAsyncStateOperator`, `StreamGroupedReduceOperator`, `StreamingDeltaJoinOperator`, `StreamingFileWriter`, `StreamingJoinOperator`, `StreamingMultiJoinOperator`, `StreamingSemiAntiJoinOperator`, `StreamMap`, `StreamProject`, `StreamRecordTimestampInserter`, `StreamSink`, `StreamSortOperator`, `StreamSource`, `TableAbstractCoUdfStreamOperator`, `TableAggregateWindowOperator`, `TableKeyedAsyncWaitOperator`, `TableStreamOperator`, `TemporalProcessTimeJoinOperator`, `TemporalRowTimeJoinOperator`, `TimestampsAndWatermarksOperator`, `TwoInputBroadcastProcessOperator`, `TwoInputNonBroadcastJoinProcessOperator`, `TwoInputNonBroadcastProcessOperator`, `TwoInputNonBroadcastWindowProcessOperator`, `TwoOutputProcessOperator`, `TwoOutputWindowProcessOperator`, `UnalignedWindowTableFunctionOperator`, `UnionStreamOperator`, `WatermarkAssignerOperator`, `WindowAggOperator`, `WindowJoinOperator`, `WindowOperator`, `WindowOperator`, `WindowTableFunctionOperatorBase`

* * *

[@PublicEvolving](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/annotation/PublicEvolving.html "annotation in org.apache.flink.annotation")public interface StreamOperator<OUT>
extends [CheckpointListener](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/api/common/state/CheckpointListener.html "interface in org.apache.flink.api.common.state"), [KeyContext](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/KeyContext.html "interface in org.apache.flink.streaming.api.operators"), [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")

Basic interface for stream operators. Implementers would implement one of [`OneInputStreamOperator`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/OneInputStreamOperator.html "interface in org.apache.flink.streaming.api.operators") or [`TwoInputStreamOperator`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/TwoInputStreamOperator.html "interface in org.apache.flink.streaming.api.operators") to create operators that process
elements.



The class [`AbstractStreamOperator`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/AbstractStreamOperator.html "class in org.apache.flink.streaming.api.operators") offers
default implementation for the lifecycle and properties methods.



Methods of `StreamOperator` are guaranteed not to be called concurrently. Also, if using
the timer service, timer callbacks are also guaranteed not to be called concurrently with methods
on `StreamOperator`.

- ## Method Summary





All MethodsInstance MethodsAbstract MethodsDefault Methods







Modifier and Type



Method



Description



`void`



`close()`





This method is called at the very end of the operator's life, both in the case of a
successful completion of the operation, and in the case of a failure and canceling.





`void`



`finish()`





This method is called at the end of data processing.





`OperatorMetricGroup`



`getMetricGroup()`







`default OperatorAttributes`



`getOperatorAttributes()`





Called to get the OperatorAttributes of the operator.





`OperatorID`



`getOperatorID()`







`void`



`initializeState(StreamTaskStateInitializer streamTaskStateManager)`





Provides a context to initialize all state in the operator.





`void`



`open()`





This method is called immediately before any elements are processed, it should contain the
operator's initialization logic.





`void`



`prepareSnapshotPreBarrier(long checkpointId)`





This method is called when the operator should do a snapshot, before it emits its own
checkpoint barrier.





`void`



`setKeyContextElement1(StreamRecord<?> record)`







`void`



`setKeyContextElement2(StreamRecord<?> record)`







`OperatorSnapshotFutures`



`snapshotState(long checkpointId,
long timestamp,
CheckpointOptions checkpointOptions,
CheckpointStreamFactory storageLocation)`





Called to draw a state snapshot from the operator.













### Methods inherited from interface org.apache.flink.api.common.state. [CheckpointListener](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/api/common/state/CheckpointListener.html "interface in org.apache.flink.api.common.state")

`notifyCheckpointAborted, notifyCheckpointComplete`





### Methods inherited from interface org.apache.flink.streaming.api.operators. [KeyContext](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/KeyContext.html "interface in org.apache.flink.streaming.api.operators")

`getCurrentKey, setCurrentKey`


- ## Method Details



  - ### open



    voidopen()
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    This method is called immediately before any elements are processed, it should contain the
    operator's initialization logic.

    Throws:`Exception` \- An exception in this method causes the operator to fail.
  - ### finish



    voidfinish()
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    This method is called at the end of data processing.



    The method is expected to flush all remaining buffered data. Exceptions during this
    flushing of buffered data should be propagated, in order to cause the operation to be
    recognized as failed, because the last data items are not processed properly.





    **After this method is called, no more records can be produced for the downstream**
    **operators.**



    **WARNING:** It is not safe to use this method to commit any transactions or other side
    effects! You can use this method to flush any buffered data that can later on be committed
    e.g. in a [`CheckpointListener.notifyCheckpointComplete(long)`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/api/common/state/CheckpointListener.html#notifyCheckpointComplete(long)).





    **NOTE:** This method does not need to close any resources. You should release external
    resources in the [`close()`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/StreamOperator.html#close()) method.



    Throws:`Exception` \- An exception in this method causes the operator to fail.
  - ### close



    voidclose()
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    This method is called at the very end of the operator's life, both in the case of a
    successful completion of the operation, and in the case of a failure and canceling.



    This method is expected to make a thorough effort to release all resources that the
    operator has acquired.





    **NOTE:** It can not emit any records! If you need to emit records at the end of
    processing, do so in the [`finish()`](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/StreamOperator.html#finish()) method.



    Throws:`Exception`
  - ### prepareSnapshotPreBarrier



    voidprepareSnapshotPreBarrier(long checkpointId)
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    This method is called when the operator should do a snapshot, before it emits its own
    checkpoint barrier.



    This method is intended not for any actual state persistence, but only for emitting some
    data before emitting the checkpoint barrier. Operators that maintain some small transient
    state that is inefficient to checkpoint (especially when it would need to be checkpointed in
    a re-scalable way) but can simply be sent downstream before the checkpoint. An example are
    opportunistic pre-aggregation operators, which have small the pre-aggregation state that is
    frequently flushed downstream.





    **Important:** This method should not be used for any actual state snapshot logic,
    because it will inherently be within the synchronous part of the operator's checkpoint. If
    heavy work is done within this method, it will affect latency and downstream checkpoint
    alignments.



    Parameters:`checkpointId` \- The ID of the checkpoint.Throws:`Exception` \- Throwing an exception here causes the operator to fail and go into
     recovery.
  - ### snapshotState



    [OperatorSnapshotFutures](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/OperatorSnapshotFutures.html "class in org.apache.flink.streaming.api.operators")snapshotState(long checkpointId,
    long timestamp,
    [CheckpointOptions](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/runtime/checkpoint/CheckpointOptions.html "class in org.apache.flink.runtime.checkpoint") checkpointOptions,
    [CheckpointStreamFactory](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/runtime/state/CheckpointStreamFactory.html "interface in org.apache.flink.runtime.state") storageLocation)
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    Called to draw a state snapshot from the operator.

    Returns:a runnable future to the state handle that points to the snapshotted state. For
     synchronous implementations, the runnable might already be finished.Throws:`Exception` \- exception that happened during snapshotting.
  - ### initializeState



    voidinitializeState( [StreamTaskStateInitializer](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/StreamTaskStateInitializer.html "interface in org.apache.flink.streaming.api.operators") streamTaskStateManager)
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")



    Provides a context to initialize all state in the operator.

    Throws:`Exception`
  - ### setKeyContextElement1



    voidsetKeyContextElement1( [StreamRecord](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/runtime/streamrecord/StreamRecord.html "class in org.apache.flink.streaming.runtime.streamrecord") <?> record)
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

    Throws:`Exception`
  - ### setKeyContextElement2



    voidsetKeyContextElement2( [StreamRecord](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/runtime/streamrecord/StreamRecord.html "class in org.apache.flink.streaming.runtime.streamrecord") <?> record)
    throws [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

    Throws:`Exception`
  - ### getMetricGroup



    [OperatorMetricGroup](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/metrics/groups/OperatorMetricGroup.html "interface in org.apache.flink.metrics.groups")getMetricGroup()

  - ### getOperatorID



    [OperatorID](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/runtime/jobgraph/OperatorID.html "class in org.apache.flink.runtime.jobgraph")getOperatorID()

  - ### getOperatorAttributes



    [@Experimental](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/annotation/Experimental.html "annotation in org.apache.flink.annotation")default[OperatorAttributes](https://nightlies.apache.org/flink/flink-docs-release-2.2/api/java//org/apache/flink/streaming/api/operators/OperatorAttributes.html "class in org.apache.flink.streaming.api.operators")getOperatorAttributes()



    Called to get the OperatorAttributes of the operator. If there is no defined attribute, a
    default OperatorAttributes is built.

    Returns:OperatorAttributes of the operator.