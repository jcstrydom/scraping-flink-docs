> This documentation is for an out-of-date version of Apache Flink. We recommend you use the latest [stable version](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/overview/).

# DataStream Connectors  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#datastream-connectors)

## Predefined Sources and Sinks  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#predefined-sources-and-sinks)

A few basic data sources and sinks are built into Flink and are always available.
The [predefined data sources](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/overview/#data-sources) include reading from files, directories, and sockets, and
ingesting data from collections and iterators.
The [predefined data sinks](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/overview/#data-sinks) support writing to files, to stdout and stderr, and to sockets.

## Flink Project Connectors  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#flink-project-connectors)

Connectors provide code for interfacing with various third-party systems.
Currently these systems are supported as part of the Apache Flink project:

- [Apache Kafka](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kafka/) (source/sink)
- [Apache Cassandra](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/cassandra/) (source/sink)
- [Amazon DynamoDB](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/dynamodb/) (sink)
- [Amazon Kinesis Data Streams](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/) (source/sink)
- [Amazon Kinesis Data Firehose](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/firehose/) (sink)
- [DataGen](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/datagen/) (source)
- [Elasticsearch](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/elasticsearch/) (sink)
- [Opensearch](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/opensearch/) (sink)
- [FileSystem](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/filesystem/) (source/sink)
- [RabbitMQ](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/rabbitmq/) (source/sink)
- [Google PubSub](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/pubsub/) (source/sink)
- [Hybrid Source](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/hybridsource/) (source)
- [Apache Pulsar](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/pulsar/) (source)
- [JDBC](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/jdbc/) (sink)
- [MongoDB](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/mongodb/) (source/sink)
- [Prometheus](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/prometheus/) (sink)

Keep in mind that to use one of these connectors in an application, additional third party
components are usually required, e.g. servers for the data stores or message queues.
Note also that while the streaming connectors listed in this section are part of the
Flink project and are included in source releases, they are not included in the binary distributions.
Further instructions can be found in the corresponding subsections.

## Connectors in Apache Bahir  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#connectors-in-apache-bahir)

Additional streaming connectors for Flink are being released through [Apache Bahir](https://bahir.apache.org/), including:

- [Apache ActiveMQ](https://bahir.apache.org/docs/flink/current/flink-streaming-activemq/) (source/sink)
- [Apache Flume](https://bahir.apache.org/docs/flink/current/flink-streaming-flume/) (sink)
- [Redis](https://bahir.apache.org/docs/flink/current/flink-streaming-redis/) (sink)
- [Akka](https://bahir.apache.org/docs/flink/current/flink-streaming-akka/) (sink)
- [Netty](https://bahir.apache.org/docs/flink/current/flink-streaming-netty/) (source)

## Other Ways to Connect to Flink  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#other-ways-to-connect-to-flink)

### Data Enrichment via Async I/O  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/overview/\#data-enrichment-via-async-io)

Using a connector isn’t the only way to get data in and out of Flink.
One common pattern is to query an external database or web service in a `Map` or `FlatMap`
in order to enrich the primary datastream.
Flink offers an API for [Asynchronous I/O](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/operators/asyncio/)
to make it easier to do this kind of enrichment efficiently and robustly.