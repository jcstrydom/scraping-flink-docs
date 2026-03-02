# Operators  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#operators)

Operators transform one or more DataStreams into a new DataStream. Programs can combine
multiple transformations into sophisticated dataflow topologies.

This section gives a description of the basic transformations, the effective physical
partitioning after applying those as well as insights into Flink’s operator chaining.

## DataStream Transformations  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-transformations)

### Map  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#map)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream)

Takes one element and produces one element. A map function that doubles the values of the input stream:

Java

```java
DataStream<Integer> dataStream = //...
dataStream.map(new MapFunction<Integer, Integer>() {
    @Override
    public Integer map(Integer value) throws Exception {
        return 2 * value;
    }
});
```

Python

```python
data_stream = env.from_collection(collection=[1, 2, 3, 4, 5])
data_stream.map(lambda x: 2 * x, output_type=Types.INT())
```

### FlatMap  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#flatmap)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-1)

Takes one element and produces zero, one, or more elements. A flatmap function that splits sentences to words:

Java

```java
dataStream.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public void flatMap(String value, Collector<String> out)
        throws Exception {
        for(String word: value.split(" ")){
            out.collect(word);
        }
    }
});
```

Python

```python
data_stream = env.from_collection(collection=['hello apache flink', 'streaming compute'])
data_stream.flat_map(lambda x: x.split(' '), output_type=Types.STRING())
```

### Filter  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#filter)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-2)

Evaluates a boolean function for each element and retains those for which the function returns true. A filter that filters out zero values:

Java

```java
dataStream.filter(new FilterFunction<Integer>() {
    @Override
    public boolean filter(Integer value) throws Exception {
        return value != 0;
    }
});
```

Python

```python
data_stream = env.from_collection(collection=[0, 1, 2, 3, 4, 5])
data_stream.filter(lambda x: x != 0)
```

### KeyBy  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#keyby)

#### DataStream → KeyedStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-keyedstream)

Logically partitions a stream into disjoint partitions. All records with the same key are assigned to the same partition. Internally, _keyBy()_ is implemented with hash partitioning. There are different ways to [specify keys](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/state/#keyed-datastream).

Java

```java
dataStream.keyBy(value -> value.getSomeKey());
dataStream.keyBy(value -> value.f0);
```

Python

```python
data_stream = env.from_collection(collection=[(1, 'a'), (2, 'a'), (3, 'b')])
data_stream.key_by(lambda x: x[1], key_type=Types.STRING()) // Key by the result of KeySelector
```

> A type **cannot be a key if**:
>
> 1. it is a POJO type but does not override the `hashCode()` method and relies on the `Object.hashCode()` implementation.
> 2. it is an array of any type.

### Reduce  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#reduce)

#### KeyedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#keyedstream-rarr-datastream)

A “rolling” reduce on a keyed data stream. Combines the current element with the last reduced value and emits the new value.

A reduce function that creates a stream of partial sums:

Java

```java
keyedStream.reduce(new ReduceFunction<Integer>() {
    @Override
    public Integer reduce(Integer value1, Integer value2)
    throws Exception {
        return value1 + value2;
    }
});
```

Python

```python
data_stream = env.from_collection(collection=[(1, 'a'), (2, 'a'), (3, 'a'), (4, 'b')], type_info=Types.TUPLE([Types.INT(), Types.STRING()]))
data_stream.key_by(lambda x: x[1]).reduce(lambda a, b: (a[0] + b[0], b[1]))
```

### Window  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#window)

#### KeyedStream → WindowedStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#keyedstream-rarr-windowedstream)

Windows can be defined on already partitioned KeyedStreams. Windows group the data in each key according to some characteristic (e.g., the data that arrived within the last 5 seconds).
See [windows](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/windows/) for a complete description of windows.

Java

```java
dataStream
  .keyBy(value -> value.f0)
  .window(TumblingEventTimeWindows.of(Duration.ofSeconds(5)));
```

Python

```python
data_stream.key_by(lambda x: x[1]).window(TumblingEventTimeWindows.of(Duration.ofSeconds(5)))
```

### WindowAll  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#windowall)

#### DataStream → AllWindowedStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-allwindowedstream)

Windows can be defined on regular DataStreams. Windows group all the stream events according to some characteristic (e.g., the data that arrived within the last 5 seconds). See [windows](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/windows/) for a complete description of windows.

> This is in many cases a non-parallel transformation. All records will be gathered in one task for the windowAll operator.

Java

```java
dataStream
  .windowAll(TumblingEventTimeWindows.of(Duration.ofSeconds(5)));
```

Python

```python
data_stream.window_all(TumblingEventTimeWindows.of(Duration.ofSeconds(5)))
```

### Window Apply  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#window-apply)

#### WindowedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#windowedstream-rarr-datastream)

#### AllWindowedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#allwindowedstream-rarr-datastream)

Applies a general function to the window as a whole. Below is a function that manually sums the elements of a window.

> If you are using a windowAll transformation, you need to use an `AllWindowFunction` instead.

Java

```java
windowedStream.apply(new WindowFunction<Tuple2<String,Integer>, Integer, Tuple, Window>() {
    public void apply (Tuple tuple,
            Window window,
            Iterable<Tuple2<String, Integer>> values,
            Collector<Integer> out) throws Exception {
        int sum = 0;
        for (value t: values) {
            sum += t.f1;
        }
        out.collect (new Integer(sum));
    }
});

// applying an AllWindowFunction on non-keyed window stream
allWindowedStream.apply (new AllWindowFunction<Tuple2<String,Integer>, Integer, Window>() {
    public void apply (Window window,
            Iterable<Tuple2<String, Integer>> values,
            Collector<Integer> out) throws Exception {
        int sum = 0;
        for (value t: values) {
            sum += t.f1;
        }
        out.collect (new Integer(sum));
    }
});
```

Python

```python
class MyWindowFunction(WindowFunction[tuple, int, int, TimeWindow]):

    def apply(self, key: int, window: TimeWindow, inputs: Iterable[tuple]) -> Iterable[int]:
        sum = 0
        for input in inputs:
            sum += input[1]
        yield sum

class MyAllWindowFunction(AllWindowFunction[tuple, int, TimeWindow]):

    def apply(self, window: TimeWindow, inputs: Iterable[tuple]) -> Iterable[int]:
        sum = 0
        for input in inputs:
            sum += input[1]
        yield sum

windowed_stream.apply(MyWindowFunction())

# applying an AllWindowFunction on non-keyed window stream
all_windowed_stream.apply(MyAllWindowFunction())
```

### WindowReduce  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#windowreduce)

#### WindowedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#windowedstream-rarr-datastream-1)

Applies a functional reduce function to the window and returns the reduced value.

Java

```java
windowedStream.reduce (new ReduceFunction<Tuple2<String,Integer>>() {
    public Tuple2<String, Integer> reduce(Tuple2<String, Integer> value1, Tuple2<String, Integer> value2) throws Exception {
        return new Tuple2<String,Integer>(value1.f0, value1.f1 + value2.f1);
    }
});
```

Python

```python
class MyReduceFunction(ReduceFunction):

    def reduce(self, value1, value2):
        return value1[0], value1[1] + value2[1]

windowed_stream.reduce(MyReduceFunction())
```

### Union  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#union)

#### DataStream\* → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-3)

Union of two or more data streams creating a new stream containing all the elements from all the streams. Note: If you union a data stream with itself you will get each element twice in the resulting stream.

Java

```java
dataStream.union(otherStream1, otherStream2, ...);
```

Python

```python
data_stream.union(otherStream1, otherStream2, ...)
```

### Window Join  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#window-join)

#### DataStream,DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastreamdatastream-rarr-datastream)

Join two data streams on a given key and a common window.

Java

```java
dataStream.join(otherStream)
    .where(<key selector>).equalTo(<key selector>)
    .window(TumblingEventTimeWindows.of(Duration.ofSeconds(3)))
    .apply (new JoinFunction () {...});
```

Python

This feature is not yet supported in Python

### Interval Join  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#interval-join)

#### KeyedStream,KeyedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#keyedstreamkeyedstream-rarr-datastream)

Join two elements e1 and e2 of two keyed streams with a common key over a given time interval, so that `e1.timestamp + lowerBound <= e2.timestamp <= e1.timestamp + upperBound`.

Java

```java
// this will join the two streams so that
// key1 == key2 && leftTs - 2 < rightTs < leftTs + 2
keyedStream.intervalJoin(otherKeyedStream)
    .between(Duration.ofMillis(-2), Duration.ofMillis(2)) // lower and upper bound
    .upperBoundExclusive(true) // optional
    .lowerBoundExclusive(true) // optional
    .process(new IntervalJoinFunction() {...});
```

Python

This feature is not yet supported in Python

### Window CoGroup  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#window-cogroup)

#### DataStream,DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastreamdatastream-rarr-datastream-1)

Cogroups two data streams on a given key and a common window.

Java

```java
dataStream.coGroup(otherStream)
    .where(0).equalTo(1)
    .window(TumblingEventTimeWindows.of(Duration.ofSeconds(3)))
    .apply (new CoGroupFunction () {...});
```

Python

This feature is not yet supported in Python

### Connect  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#connect)

#### DataStream,DataStream → ConnectedStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastreamdatastream-rarr-connectedstream)

“Connects” two data streams retaining their types. Connect allowing for shared state between the two streams.

Java

```java
DataStream<Integer> someStream = //...
DataStream<String> otherStream = //...

ConnectedStreams<Integer, String> connectedStreams = someStream.connect(otherStream);
```

Python

```python
stream_1 = ...
stream_2 = ...
connected_streams = stream_1.connect(stream_2)
```

### CoMap, CoFlatMap  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#comap-coflatmap)

#### ConnectedStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#connectedstream-rarr-datastream)

Similar to map and flatMap on a connected data stream

Java

```java
connectedStreams.map(new CoMapFunction<Integer, String, Boolean>() {
    @Override
    public Boolean map1(Integer value) {
        return true;
    }

    @Override
    public Boolean map2(String value) {
        return false;
    }
});
connectedStreams.flatMap(new CoFlatMapFunction<Integer, String, String>() {

   @Override
   public void flatMap1(Integer value, Collector<String> out) {
       out.collect(value.toString());
   }

   @Override
   public void flatMap2(String value, Collector<String> out) {
       for (String word: value.split(" ")) {
         out.collect(word);
       }
   }
});
```

Python

```python
class MyCoMapFunction(CoMapFunction):

    def map1(self, value):
        return value[0] + 1, value[1]

    def map2(self, value):
        return value[0], value[1] + 'flink'

class MyCoFlatMapFunction(CoFlatMapFunction):

    def flat_map1(self, value)
        for i in range(value[0]):
            yield i

    def flat_map2(self, value):
        yield value[0] + 1

connectedStreams.map(MyCoMapFunction())
connectedStreams.flat_map(MyCoFlatMapFunction())
```

### Cache  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#cache)

#### DataStream → CachedDataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-cacheddatastream)

Cache the intermediate result of the transformation. Currently, only jobs that run with batch
execution mode are supported. The cache intermediate result is generated lazily at the first time
the intermediate result is computed so that the result can be reused by later jobs. If the cache is
lost, it will be recomputed using the original transformations.

Java

```java
DataStream<Integer> dataStream = //...
CachedDataStream<Integer> cachedDataStream = dataStream.cache();
cachedDataStream.print(); // Do anything with the cachedDataStream
...
env.execute(); // Execute and create cache.

cachedDataStream.print(); // Consume cached result.
env.execute();
```

Python

```python
data_stream = ... # DataStream
cached_data_stream = data_stream.cache()
cached_data_stream.print()
# ...
env.execute() # Execute and create cache.

cached_data_stream.print() # Consume cached result.
env.execute()
```

### Full Window Partition  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#full-window-partition)

#### DataStream → PartitionWindowedStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-partitionwindowedstream)

Collects all records of each partition separately into a full window and processes them. The window
emission will be triggered at the end of inputs.
This approach is primarily applicable to batch processing scenarios.
For non-keyed DataStream, a partition contains all records of a subtask.
For KeyedStream, a partition contains all records of a key.

```java
DataStream<Integer> dataStream = //...
PartitionWindowedStream<Integer> partitionWindowedDataStream = dataStream.fullWindowPartition();
// do full window partition processing with PartitionWindowedStream
DataStream<Integer> resultStream = partitionWindowedDataStream.mapPartition(
    new MapPartitionFunction<Integer, Integer>() {
        @Override
        public void mapPartition(
                Iterable<Integer> values, Collector<Integer> out) {
            int result = 0;
            for (Integer value : values) {
                result += value;
            }
            out.collect(result);
        }
    }
);
```

## Physical Partitioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#physical-partitioning)

Flink also gives low-level control (if desired) on the exact stream partitioning after a transformation, via the following functions.

### Custom Partitioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#custom-partitioning)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-4)

Uses a user-defined Partitioner to select the target task for each element.

Java

```java
dataStream.partitionCustom(partitioner, "someKey");
dataStream.partitionCustom(partitioner, 0);
```

Python

```python
data_stream = env.from_collection(collection=[(2, 'a'), (2, 'a'), (3, 'b')])
data_stream.partition_custom(lambda key, num_partition: key % partition, lambda x: x[0])
```

### Random Partitioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#random-partitioning)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-5)

Partitions elements randomly according to a uniform distribution.

Java

```java
dataStream.shuffle();
```

Python

```python
data_stream.shuffle()
```

### Rescaling  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#rescaling)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-6)

Partitions elements, round-robin, to a subset of downstream operations. This is useful if you want to have pipelines where you, for example, fan out from each parallel instance of a source to a subset of several mappers to distribute load but don’t want the full rebalance that rebalance() would incur. This would require only local data transfers instead of transferring data over network, depending on other configuration values such as the number of slots of TaskManagers.

The subset of downstream operations to which the upstream operation sends elements depends on the degree of parallelism of both the upstream and downstream operation. For example, if the upstream operation has parallelism 2 and the downstream operation has parallelism 6, then one upstream operation would distribute elements to three downstream operations while the other upstream operation would distribute to the other three downstream operations. If, on the other hand, the downstream operation has parallelism 2 while the upstream operation has parallelism 6 then three upstream operations would distribute to one downstream operation while the other three upstream operations would distribute to the other downstream operation.

In cases where the different parallelisms are not multiples of each other one or several downstream operations will have a differing number of inputs from upstream operations.

Please see this figure for a visualization of the connection pattern in the above example:

![Checkpoint barriers in data streams](https://nightlies.apache.org/flink/flink-docs-release-2.2/fig/rescale.svg)

Java

```java
dataStream.rescale();
```

Python

```python
data_stream.rescale()
```

### Broadcasting  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#broadcasting)

#### DataStream → DataStream  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#datastream-rarr-datastream-7)

Broadcasts elements to every partition.

Java

```java
dataStream.broadcast();
```

Python

```python
data_stream.broadcast()
```

## Task Chaining and Resource Groups  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#task-chaining-and-resource-groups)

Chaining two subsequent transformations means co-locating them within the same thread for better performance. Flink by default chains operators if this is possible (e.g., two subsequent map transformations). The API gives fine-grained control over chaining if desired:

Use `StreamExecutionEnvironment.disableOperatorChaining()` if you want to disable chaining in the whole job. For more fine grained control, the following functions are available. Note that these functions can only be used right after a DataStream transformation as they refer to the previous transformation. For example, you can use `someStream.map(...).startNewChain()`, but you cannot use `someStream.startNewChain()`.

A resource group is a slot in Flink, see slots. You can manually isolate operators in separate slots if desired.

### Start New Chain  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#start-new-chain)

Begin a new chain, starting with this operator.
The two mappers will be chained, and filter will not be chained to the first mapper.

Java

```java
someStream.filter(...).map(...).startNewChain().map(...);
```

Python

```python
some_stream.filter(...).map(...).start_new_chain().map(...)
```

### Disable Chaining  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#disable-chaining)

Do not chain the map operator.

Java

```java
someStream.map(...).disableChaining();
```

Python

```python
some_stream.map(...).disable_chaining()
```

### Set Slot Sharing Group  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#set-slot-sharing-group)

Set the slot sharing group of an operation. Flink will put operations with the same slot sharing group into the same slot while keeping operations that don’t have the slot sharing group in other slots. This can be used to isolate slots. The slot sharing group is inherited from input operations if all input operations are in the same slot sharing group. The name of the default slot sharing group is “default”, operations can explicitly be put into this group by calling slotSharingGroup(“default”).

Java

```java
someStream.filter(...).slotSharingGroup("name");
```

Python

```python
some_stream.filter(...).slot_sharing_group("name")
```

## Name And Description  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/operators/overview/\#name-and-description)

Operators and job vertices in flink have a name and a description.
Both name and description are introduction about what an operator or a job vertex is doing, but they are used differently.

The name of operator and job vertex will be used in web ui, thread name, logging, metrics, etc.
The name of a job vertex is constructed based on the name of operators in it.
The name needs to be as concise as possible to avoid high pressure on external systems.

The description will be used in the execution plan and displayed as the details of a job vertex in web UI.
The description of a job vertex is constructed based on the description of operators in it.
The description can contain detail information about operators to facilitate debugging at runtime.

Java

```java
someStream.filter(...).name("filter").setDescription("x in (1, 2, 3, 4) and y > 1");
```

Python

```python
some_stream.filter(...).name("filter").set_description("x in (1, 2, 3, 4) and y > 1")
```

The format of description of a job vertex is a tree format string by default.
Users can set `pipeline.vertex-description-mode` to `CASCADING`, if they want to set description to be the cascading format as in former versions.

Operators generated by Flink SQL will have a name consisted by type of operator and id, and a detailed description, by default.
Users can set `table.exec.simplify-operator-name-enabled` to `false`, if they want to set name to be the detailed description as in former versions.

When the topology of the pipeline is complex, users can add a topological index in the name of vertex by set `pipeline.vertex-name-include-index-prefix` to `true`,
so that we can easily find the vertex in the graph according to logs or metrics tags.