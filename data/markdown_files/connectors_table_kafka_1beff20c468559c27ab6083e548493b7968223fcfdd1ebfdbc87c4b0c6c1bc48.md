# Apache Kafka SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#apache-kafka-sql-connector)

Scan Source: UnboundedSink: Streaming Append Mode

The Kafka connector allows for reading data from and writing data into Kafka topics.

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

The Kafka connector is not part of the binary distribution.
See how to link with it for cluster execution [here](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/configuration/overview/).

## How to create a Kafka table  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#how-to-create-a-kafka-table)

The example below shows how to create a Kafka table:

```sql
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'csv'
)
```

## Available Metadata  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#available-metadata)

The following connector metadata can be accessed as metadata columns in a table definition.

The `R/W` column defines whether a metadata field is readable (`R`) and/or writable (`W`).
Read-only columns must be declared `VIRTUAL` to exclude them during an `INSERT INTO` operation.

| Key | Data Type | Description | R/W |
| --- | --- | --- | --- |
| `topic` | `STRING NOT NULL` | Topic name of the Kafka record. | `R/W` |
| `partition` | `INT NOT NULL` | Partition ID of the Kafka record. | `R` |
| `headers` | `MAP NOT NULL` | Headers of the Kafka record as a map of raw bytes. | `R/W` |
| `leader-epoch` | `INT NULL` | Leader epoch of the Kafka record if available. | `R` |
| `offset` | `BIGINT NOT NULL` | Offset of the Kafka record in the partition. | `R` |
| `timestamp` | `TIMESTAMP_LTZ(3) NOT NULL` | Timestamp of the Kafka record. | `R/W` |
| `timestamp-type` | `STRING NOT NULL` | Timestamp type of the Kafka record. Either "NoTimestampType",<br> "CreateTime" (also set when writing metadata), or "LogAppendTime". | `R` |

The extended `CREATE TABLE` example demonstrates the syntax for exposing these metadata fields:

```sql
CREATE TABLE KafkaTable (
  `event_time` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp',
  `partition` BIGINT METADATA VIRTUAL,
  `offset` BIGINT METADATA VIRTUAL,
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'csv'
);
```

**Format Metadata**

The connector is able to expose metadata of the value format for reading. Format metadata keys
are prefixed with `'value.'`.

The following example shows how to access both Kafka and Debezium metadata fields:

```sql
CREATE TABLE KafkaTable (
  `event_time` TIMESTAMP_LTZ(3) METADATA FROM 'value.source.timestamp' VIRTUAL,  -- from Debezium format
  `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL, -- from Debezium format
  `partition_id` BIGINT METADATA FROM 'partition' VIRTUAL,  -- from Kafka connector
  `offset` BIGINT METADATA VIRTUAL,  -- from Kafka connector
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'value.format' = 'debezium-json'
);
```

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#connector-options)

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#connector) | required | no | (none) | String | Specify what connector to use, for Kafka use `'kafka'`. |
| ##### topic [Anchor link for: topic](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#topic) | optional | yes | (none) | String | Topic name(s) to read data from when the table is used as source, or topics for writing when the table is used as sink. It also supports topic list for source by separating topic by semicolon like `'topic-1;topic-2'`. Note, only one of "topic-pattern" and "topic" can be specified. For sinks, the topic name is the topic to write data. It also supports topic list for sinks. The provided topic-list is treated as a allow list of valid values for the \`topic\` metadata column. If a list is provided, for sink table, 'topic' metadata column is writable and must be specified. |
| ##### topic-pattern [Anchor link for: topic pattern](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#topic-pattern) | optional | yes | (none) | String | The regular expression for a pattern of topic names to read from or write to. All topics with names that match the specified regular expression will be subscribed by the consumer when the job starts running. For sinks, the \`topic\` metadata column is writable, must be provided and match the \`topic-pattern\` regex. Note, only one of "topic-pattern" and "topic" can be specified. |
| ##### properties.bootstrap.servers [Anchor link for: properties bootstrap servers](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#properties-bootstrap-servers) | required | yes | (none) | String | Comma separated list of Kafka brokers. |
| ##### properties.group.id [Anchor link for: properties group id](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#properties-group-id) | optional for source, not applicable for sink | yes | (none) | String | The id of the consumer group for Kafka source. If group ID is not specified, an automatically generated id "KafkaSource-{tableIdentifier}" will be used. |
| ##### properties.\* [Anchor link for: properties](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#properties) | optional | no | (none) | String | This can set and pass arbitrary Kafka configurations. Suffix names must match the configuration key defined in [Kafka Configuration documentation](https://kafka.apache.org/documentation/#configuration). Flink will remove the "properties." key prefix and pass the transformed key and values to the underlying KafkaClient. For example, you can disable automatic topic creation via `'properties.allow.auto.create.topics' = 'false'`. But there are some configurations that do not support to set, because Flink will override them, e.g. `'auto.offset.reset'`. |
| ##### format [Anchor link for: format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#format) | required | no | (none) | String | The format used to deserialize and serialize the value part of Kafka messages.<br> Please refer to the [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page for<br> more details and more format options.<br> Note: Either this option or the `'value.format'` option are required. |
| ##### key.format [Anchor link for: key format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#key-format) | optional | no | (none) | String | The format used to deserialize and serialize the key part of Kafka messages.<br> Please refer to the [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page<br> for more details and more format options. Note: If a key format is defined, the `'key.fields'`<br> option is required as well. Otherwise the Kafka records will have an empty key. |
| ##### key.fields [Anchor link for: key fields](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#key-fields) | optional | no | \[\] | List<String> | Defines an explicit list of physical columns from the table schema that configure the data<br> type for the key format. By default, this list is empty and thus a key is undefined.<br> The list should look like `'field1;field2'`. |
| ##### key.fields-prefix [Anchor link for: key fields prefix](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#key-fields-prefix) | optional | no | (none) | String | Defines a custom prefix for all fields of the key format to avoid name clashes with fields<br> of the value format. By default, the prefix is empty. If a custom prefix is defined, both the<br> table schema and `'key.fields'` will work with prefixed names. When constructing the<br> data type of the key format, the prefix will be removed and the non-prefixed names will be used<br> within the key format. Please note that this option requires that `'value.fields-include'`<br> must be set to `'EXCEPT_KEY'`. |
| ##### value.format [Anchor link for: value format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#value-format) | required | no | (none) | String | The format used to deserialize and serialize the value part of Kafka messages.<br> Please refer to the [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page<br> for more details and more format options.<br> Note: Either this option or the `'format'` option are required. |
| ##### value.fields-include [Anchor link for: value fields include](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#value-fields-include) | optional | no | ALL | Enum<br>Possible values: \[ALL, EXCEPT\_KEY\] | Defines a strategy how to deal with key columns in the data type of the value format. By<br> default, `'ALL'` physical columns of the table schema will be included in the value<br> format which means that key columns appear in the data type for both the key and value format. |
| ##### scan.startup.mode [Anchor link for: scan startup mode](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-startup-mode) | optional | yes | group-offsets | Enum | Startup mode for Kafka consumer, valid values are `'earliest-offset'`, `'latest-offset'`, `'group-offsets'`, `'timestamp'` and `'specific-offsets'`.<br> See the following [Start Reading Position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/#start-reading-position) for more details. |
| ##### scan.startup.specific-offsets [Anchor link for: scan startup specific offsets](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-startup-specific-offsets) | optional | yes | (none) | String | Specify offsets for each partition in case of `'specific-offsets'` startup mode, e.g. `'partition:0,offset:42;partition:1,offset:300'`. |
| ##### scan.startup.timestamp-millis [Anchor link for: scan startup timestamp millis](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-startup-timestamp-millis) | optional | yes | (none) | Long | Start from the specified epoch timestamp (milliseconds) used in case of `'timestamp'` startup mode. |
| ##### scan.bounded.mode [Anchor link for: scan bounded mode](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-bounded-mode) | optional | no | unbounded | Enum | Bounded mode for Kafka consumer, valid values are `'latest-offset'`, `'group-offsets'`, `'timestamp'` and `'specific-offsets'`.<br> See the following [Bounded Ending Position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/#bounded-ending-position) for more details. |
| ##### scan.bounded.specific-offsets [Anchor link for: scan bounded specific offsets](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-bounded-specific-offsets) | optional | yes | (none) | String | Specify offsets for each partition in case of `'specific-offsets'` bounded mode, e.g. `'partition:0,offset:42;partition:1,offset:300'. If an offset<br>       for a partition is not provided it will not consume from that partition.`. |
| ##### scan.bounded.timestamp-millis [Anchor link for: scan bounded timestamp millis](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-bounded-timestamp-millis) | optional | yes | (none) | Long | End at the specified epoch timestamp (milliseconds) used in case of `'timestamp'` bounded mode. |
| ##### scan.topic-partition-discovery.interval [Anchor link for: scan topic partition discovery interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-topic-partition-discovery-interval) | optional | yes | 5 minutes | Duration | Interval for consumer to discover dynamically created Kafka topics and partitions periodically. To disable this feature, you need to explicitly set the 'scan.topic-partition-discovery.interval' value to 0. |
| ##### scan.parallelism [Anchor link for: scan parallelism](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#scan-parallelism) | optional | no | (none) | Integer | Defines the parallelism of the Kafka source operator. If not set, the global default parallelism is used. |
| ##### sink.partitioner [Anchor link for: sink partitioner](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-partitioner) | optional | yes | 'default' | String | Output partitioning from Flink's partitions into Kafka's partitions. Valid values are<br> <br>- `default`: use the kafka default partitioner to partition records.<br>- `fixed`: each Flink partition ends up in at most one Kafka partition.<br>- `round-robin`: a Flink partition is distributed to Kafka partitions sticky round-robin. It only works when record's keys are not specified.<br>- Custom `FlinkKafkaPartitioner` subclass: e.g. `'org.mycompany.MyPartitioner'`.<br> See the following [Sink Partitioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/#sink-partitioning) for more details. |
| ##### sink.semantic [Anchor link for: sink semantic](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-semantic) | optional | no | at-least-once | String | Deprecated: Please use `sink.delivery-guarantee`. |
| ##### sink.delivery-guarantee [Anchor link for: sink delivery guarantee](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-delivery-guarantee) | optional | no | at-least-once | String | Defines the delivery semantic for the Kafka sink. Valid enumerationns are `'at-least-once'`, `'exactly-once'` and `'none'`. See [Consistency guarantees](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/#consistency-guarantees) for more details. |
| ##### sink.transactional-id-prefix [Anchor link for: sink transactional id prefix](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-transactional-id-prefix) | optional | yes | (none) | String | If the delivery guarantee is configured as `'exactly-once'` this value must be set and is used a prefix for the identifier of all opened Kafka transactions. |
| ##### sink.parallelism [Anchor link for: sink parallelism](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-parallelism) | optional | no | (none) | Integer | Defines the parallelism of the Kafka sink operator. By default, the parallelism is determined by the framework using the same parallelism of the upstream chained operator. |

## Features  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#features)

### Key and Value Formats  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#key-and-value-formats)

Both the key and value part of a Kafka record can be serialized to and deserialized from raw bytes using
one of the given [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/).

**Value Format**

Since a key is optional in Kafka records, the following statement reads and writes records with a configured
value format but without a key format. The `'format'` option is a synonym for `'value.format'`. All format
options are prefixed with the format identifier.

```sql
CREATE TABLE KafkaTable (
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp',
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING
) WITH (
  'connector' = 'kafka',
  ...

  'format' = 'json',
  'json.ignore-parse-errors' = 'true'
)
```

The value format will be configured with the following data type:

```text
ROW<`user_id` BIGINT, `item_id` BIGINT, `behavior` STRING>
```

**Key and Value Format**

The following example shows how to specify and configure key and value formats. The format options are
prefixed with either the `'key'` or `'value'` plus format identifier.

```sql
CREATE TABLE KafkaTable (
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp',
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING
) WITH (
  'connector' = 'kafka',
  ...

  'key.format' = 'json',
  'key.json.ignore-parse-errors' = 'true',
  'key.fields' = 'user_id;item_id',

  'value.format' = 'json',
  'value.json.fail-on-missing-field' = 'false',
  'value.fields-include' = 'ALL'
)
```

The key format includes the fields listed in `'key.fields'` (using `';'` as the delimiter) in the same
order. Thus, it will be configured with the following data type:

```text
ROW<`user_id` BIGINT, `item_id` BIGINT>
```

Since the value format is configured with `'value.fields-include' = 'ALL'`, key fields will also end up in
the value format’s data type:

```text
ROW<`user_id` BIGINT, `item_id` BIGINT, `behavior` STRING>
```

**Overlapping Format Fields**

The connector cannot split the table’s columns into key and value fields based on schema information
if both key and value formats contain fields of the same name. The `'key.fields-prefix'` option allows
to give key columns a unique name in the table schema while keeping the original names when configuring
the key format.

The following example shows a key and value format that both contain a `version` field:

```sql
CREATE TABLE KafkaTable (
  `k_version` INT,
  `k_user_id` BIGINT,
  `k_item_id` BIGINT,
  `version` INT,
  `behavior` STRING
) WITH (
  'connector' = 'kafka',
  ...

  'key.format' = 'json',
  'key.fields-prefix' = 'k_',
  'key.fields' = 'k_version;k_user_id;k_item_id',

  'value.format' = 'json',
  'value.fields-include' = 'EXCEPT_KEY'
)
```

The value format must be configured in `'EXCEPT_KEY'` mode. The formats will be configured with
the following data types:

```text
key format:
ROW<`version` INT, `user_id` BIGINT, `item_id` BIGINT>

value format:
ROW<`version` INT, `behavior` STRING>
```

### Topic and Partition Discovery  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#topic-and-partition-discovery)

The config option `topic` and `topic-pattern` specifies the topics or topic pattern to consume for source. The config option `topic` can accept topic list using semicolon separator like ’topic-1;topic-2’.
The config option `topic-pattern` will use regular expression to discover the matched topic. For example, if the `topic-pattern` is `test-topic-[0-9]`, then all topics with names that match the specified regular expression (starting with `test-topic-` and ending with a single digit)) will be subscribed by the consumer when the job starts running.

To allow the consumer to discover dynamically created topics after the job started running, set a non-negative value for `scan.topic-partition-discovery.interval`. This allows the consumer to discover partitions of new topics with names that also match the specified pattern.

Please refer to [Kafka DataStream Connector documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kafka/#kafka-consumers-topic-and-partition-discovery) for more about topic and partition discovery.

Note that topic list and topic pattern only work in sources. In sinks, Flink currently only supports a single topic.

### Start Reading Position  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#start-reading-position)

The config option `scan.startup.mode` specifies the startup mode for Kafka consumer. The valid enumerations are:

- `group-offsets`: start from committed offsets in ZK / Kafka brokers of a specific consumer group.
- `earliest-offset`: start from the earliest offset possible.
- `latest-offset`: start from the latest offset.
- `timestamp`: start from user-supplied timestamp for each partition.
- `specific-offsets`: start from user-supplied specific offsets for each partition.

The default option value is `group-offsets` which indicates to consume from last committed offsets in ZK / Kafka brokers.

If `timestamp` is specified, another config option `scan.startup.timestamp-millis` is required to specify a specific startup timestamp in milliseconds since January 1, 1970 00:00:00.000 GMT.

If `specific-offsets` is specified, another config option `scan.startup.specific-offsets` is required to specify specific startup offsets for each partition,
e.g. an option value `partition:0,offset:42;partition:1,offset:300` indicates offset `42` for partition `0` and offset `300` for partition `1`.

### Bounded Ending Position  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#bounded-ending-position)

The config option `scan.bounded.mode` specifies the bounded mode for Kafka consumer. The valid enumerations are:

- \`group-offsets\`: bounded by committed offsets in ZooKeeper / Kafka brokers of a specific consumer group. This is evaluated at the start of consumption from a given partition.
- \`latest-offset\`: bounded by latest offsets. This is evaluated at the start of consumption from a given partition.
- \`timestamp\`: bounded by a user-supplied timestamp.
- \`specific-offsets\`: bounded by user-supplied specific offsets for each partition.

If config option value `scan.bounded.mode` is not set the default is an unbounded table.

If `timestamp` is specified, another config option `scan.bounded.timestamp-millis` is required to specify a specific bounded timestamp in milliseconds since January 1, 1970 00:00:00.000 GMT.

If `specific-offsets` is specified, another config option `scan.bounded.specific-offsets` is required to specify specific bounded offsets for each partition,
e.g. an option value `partition:0,offset:42;partition:1,offset:300` indicates offset `42` for partition `0` and offset `300` for partition `1`. If an offset for a partition is not provided it will not consume from that partition.

### CDC Changelog Source  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#cdc-changelog-source)

Flink natively supports Kafka as a CDC changelog source. If messages in a Kafka topic are change event captured from other databases using a CDC tool, you can use the corresponding Flink CDC format to interpret the messages as INSERT/UPDATE/DELETE statements into a Flink SQL table.

The changelog source is a very useful feature in many cases, such as synchronizing incremental data from databases to other systems, auditing logs, materialized views on databases, temporal join changing history of a database table and so on.

Flink provides several CDC formats:

- [debezium](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/debezium/)
- [canal](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/canal/)
- [maxwell](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/maxwell/)

### Sink Partitioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#sink-partitioning)

The config option `sink.partitioner` specifies output partitioning from Flink’s partitions into Kafka’s partitions.
By default, Flink uses the [Kafka default partitioner](https://github.com/apache/kafka/blob/trunk/clients/src/main/java/org/apache/kafka/clients/producer/internals/DefaultPartitioner.java) to partition records. It uses the [sticky partition strategy](https://www.confluent.io/blog/apache-kafka-producer-improvements-sticky-partitioner/) for records with null keys and uses a murmur2 hash to compute the partition for a record with the key defined.

In order to control the routing of rows into partitions, a custom sink partitioner can be provided. The ‘fixed’ partitioner will write the records in the same Flink partition into the same Kafka partition, which could reduce the cost of the network connections.

### Consistency guarantees  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#consistency-guarantees)

By default, a Kafka sink ingests data with at-least-once guarantees into a Kafka topic if the query is executed with [checkpointing enabled](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/checkpointing/#enabling-and-configuring-checkpointing).

With Flink’s checkpointing enabled, the `kafka` connector can provide exactly-once delivery guarantees.

Besides enabling Flink’s checkpointing, you can also choose three different modes of operating chosen by passing appropriate `sink.delivery-guarantee` option:

- `none`: Flink will not guarantee anything. Produced records can be lost or they can be duplicated.
- `at-least-once` (default setting): This guarantees that no records will be lost (although they can be duplicated).
- `exactly-once`: Kafka transactions will be used to provide exactly-once semantic. Whenever you write
to Kafka using transactions, do not forget about setting desired `isolation.level` (`read_uncommitted`
or `read_committed` \- the latter one is the default value) for any application consuming records
from Kafka.

Please refer to [Kafka documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kafka/#kafka-producers-and-fault-tolerance) for more caveats about delivery guarantees.

### Source Per-Partition Watermarks  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#source-per-partition-watermarks)

Flink supports to emit per-partition watermarks for Kafka. Watermarks are generated inside the Kafka
consumer. The per-partition watermarks are merged in the same way as watermarks are merged during streaming
shuffles. The output watermark of the source is determined by the minimum watermark among the partitions
it reads. If some partitions in the topics are idle, the watermark generator will not advance. You can
alleviate this problem by setting the [`'table.exec.source.idle-timeout'`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/config/#table-exec-source-idle-timeout)
option in the table configuration.

Please refer to [Kafka watermark strategies](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/event-time/generating_watermarks/#watermark-strategies-and-the-kafka-connector)
for more details.

### Security  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#security)

In order to enable security configurations including encryption and authentication, you just need to setup security
configurations with “properties.” prefix in table options. The code snippet below shows configuring Kafka table to
use PLAIN as SASL mechanism and provide JAAS configuration when using SQL client JAR :

```sql
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN',
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username=\"username\" password=\"password\";'
)
```

For a more complex example, use SASL\_SSL as the security protocol and use SCRAM-SHA-256 as SASL mechanism when using SQL client JAR :

```sql
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_SSL',
  /* SSL configurations */
  /* Configure the path of truststore (CA) provided by the server */
  'properties.ssl.truststore.location' = '/path/to/kafka.client.truststore.jks',
  'properties.ssl.truststore.password' = 'test1234',
  /* Configure the path of keystore (private key) if client authentication is required */
  'properties.ssl.keystore.location' = '/path/to/kafka.client.keystore.jks',
  'properties.ssl.keystore.password' = 'test1234',
  /* SASL configurations */
  /* Set SASL mechanism as SCRAM-SHA-256 */
  'properties.sasl.mechanism' = 'SCRAM-SHA-256',
  /* Set JAAS configurations */
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.scram.ScramLoginModule required username=\"username\" password=\"password\";'
)
```

Please note that the class path of the login module in `sasl.jaas.config` might be different if you relocate Kafka
client dependencies, so you may need to rewrite it with the actual class path of the module in the JAR.
SQL client JAR has relocated Kafka client dependencies to `org.apache.flink.kafka.shaded.org.apache.kafka`,
then the path of plain login module in code snippets above need to be
`org.apache.flink.kafka.shaded.org.apache.kafka.common.security.plain.PlainLoginModule` when using SQL client JAR.

For detailed explanations of security configurations, please refer to
[the “Security” section in Apache Kafka documentation](https://kafka.apache.org/documentation/#security).

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/\#data-type-mapping)

Kafka stores message keys and values as bytes, so Kafka doesn’t have schema or data types. The Kafka messages are deserialized and serialized by formats, e.g. csv, json, avro.
Thus, the data type mapping is determined by specific formats. Please refer to [Formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) pages for more details.