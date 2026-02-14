# User-Defined Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#user-defined-functions)

Most operations require a user-defined function. This section lists different
ways of how they can be specified. We also cover `Accumulators`, which can be
used to gain insights into your Flink application.

## Implementing an interface  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#implementing-an-interface)

The most basic way is to implement one of the provided interfaces:

```java
class MyMapFunction implements MapFunction<String, Integer> {
  public Integer map(String value) { return Integer.parseInt(value); }
}
data.map(new MyMapFunction());
```

## Anonymous classes  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#anonymous-classes)

You can pass a function as an anonymous class:

```java
data.map(new MapFunction<String, Integer> () {
  public Integer map(String value) { return Integer.parseInt(value); }
});
```

## Java 8 Lambdas  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#java-8-lambdas)

Flink also supports Java 8 Lambdas in the Java API.

```java
data.filter(s -> s.startsWith("http://"));
```

```java
data.reduce((i1,i2) -> i1 + i2);
```

## Rich functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#rich-functions)

All transformations that require a user-defined function can
instead take as argument a _rich_ function. For example, instead of

```java
class MyMapFunction implements MapFunction<String, Integer> {
  public Integer map(String value) { return Integer.parseInt(value); }
}
```

you can write

```java
class MyMapFunction extends RichMapFunction<String, Integer> {
  public Integer map(String value) { return Integer.parseInt(value); }
}
```

and pass the function as usual to a `map` transformation:

```java
data.map(new MyMapFunction());
```

Rich functions can also be defined as an anonymous class:

```java
data.map (new RichMapFunction<String, Integer>() {
  public Integer map(String value) { return Integer.parseInt(value); }
});
```

## Accumulators & Counters  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/user_defined_functions/\#accumulators--counters)

Accumulators are simple constructs with an **add operation** and a **final accumulated result**,
which is available after the job ended.

The most straightforward accumulator is a **counter**: You can increment it using the
`Accumulator.add(V value)` method. At the end of the job Flink will sum up (merge) all partial
results and send the result to the client. Accumulators are useful during debugging or if you
quickly want to find out more about your data.

Flink currently has the following **built-in accumulators**. Each of them implements the

[Accumulator](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/Accumulator.java)

interface.

- [**IntCounter**](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/IntCounter.java)
,

[**LongCounter**](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/LongCounter.java)

and
[**DoubleCounter**](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/DoubleCounter.java)
:
See below for an example using a counter.
- [**Histogram**](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/Histogram.java)
:
A histogram implementation for a discrete number of bins. Internally it is just a map from Integer
to Integer. You can use this to compute distributions of values, e.g. the distribution of
words-per-line for a word count program.

**How to use accumulators:**

First you have to create an accumulator object (here a counter) in the user-defined transformation
function where you want to use it.

```java
private IntCounter numLines = new IntCounter();
```

Second you have to register the accumulator object, typically in the `open()` method of the
_rich_ function. Here you also define the name.

```java
getRuntimeContext().addAccumulator("num-lines", this.numLines);
```

You can now use the accumulator anywhere in the operator function, including in the `open()` and
`close()` methods.

```java
this.numLines.add(1);
```

The overall result will be stored in the `JobExecutionResult` object which is
returned from the `execute()` method of the execution environment
(currently this only works if the execution waits for the
completion of the job).

```java
myJobExecutionResult.getAccumulatorResult("num-lines");
```

All accumulators share a single namespace per job. Thus you can use the same accumulator in
different operator functions of your job. Flink will internally merge all accumulators with the same
name.

**Custom accumulators:**

To implement your own accumulator you simply have to write your implementation of the Accumulator
interface. Feel free to create a pull request if you think your custom accumulator should be shipped
with Flink.

You have the choice to implement either

[Accumulator](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/Accumulator.java)

or
[SimpleAccumulator](https://github.com/apache/flink/blob/release-2.2//flink-core/src/main/java/org/apache/flink/api/common/accumulators/SimpleAccumulator.java)
.

`Accumulator<V,R>` is most flexible: It defines a type `V` for the value to add, and a
result type `R` for the final result. E.g. for a histogram, `V` is a number and `R` is
a histogram. `SimpleAccumulator` is for the cases where both types are the same, e.g. for counters.