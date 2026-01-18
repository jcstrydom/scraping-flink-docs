# Upsert Kafka SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#upsert-kafka-sql-connector)

Scan Source: UnboundedSink: Streaming Upsert Mode

The Upsert Kafka connector allows for reading data from and writing data into Kafka topics in the upsert fashion.

As a source, the upsert-kafka connector produces a changelog stream, where each data record represents
an update or delete event. More precisely, the value in a data record is interpreted as an UPDATE of
the last value for the same key, if any (if a corresponding key doesn’t exist yet, the update will
be considered an INSERT). Using the table analogy, a data record in a changelog stream is interpreted
as an UPSERT aka INSERT/UPDATE because any existing row with the same key is overwritten. Also, null
values are interpreted in a special way: a record with a null value represents a “DELETE”.

As a sink, the upsert-kafka connector can consume a changelog stream. It will write INSERT/UPDATE\_AFTER
data as normal Kafka messages value, and write DELETE data as Kafka messages with null values
(indicate tombstone for the key). Flink will guarantee the message ordering on the primary key by
partition data on the values of the primary key columns, so the update/deletion messages on the same
key will fall into the same partition.

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

The Upsert Kafka connector is not part of the binary distribution.
See how to link with it for cluster execution [here](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/configuration/overview/).

## Full Example  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#full-example)

The example below shows how to create and use an Upsert Kafka table:

```sql
CREATE TABLE pageviews_per_region (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = 'pageviews_per_region',
  'properties.bootstrap.servers' = '...',
  'key.format' = 'avro',
  'value.format' = 'avro'
);

CREATE TABLE pageviews (
  user_id BIGINT,
  page_id BIGINT,
  viewtime TIMESTAMP,
  user_region STRING,
  WATERMARK FOR viewtime AS viewtime - INTERVAL '2' SECOND
) WITH (
  'connector' = 'kafka',
  'topic' = 'pageviews',
  'properties.bootstrap.servers' = '...',
  'format' = 'json'
);

-- calculate the pv, uv and insert into the upsert-kafka sink
INSERT INTO pageviews_per_region
SELECT
  user_region,
  COUNT(*),
  COUNT(DISTINCT user_id)
FROM pageviews
GROUP BY user_region;
```

Attention Make sure to define the primary key in the DDL.

## Available Metadata  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#available-metadata)

See the [regular Kafka connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kafka/#available-metadata) for a list
of all available metadata fields.

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#connector-options)

| Option | Required | Default | Type | Description |
| --- | --- | --- | --- | --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#connector) | required | (none) | String | Specify which connector to use, for the Upsert Kafka use: `'upsert-kafka'`. |
| ##### topic [Anchor link for: topic](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#topic) | required | (none) | String | Topic name(s) to read data from when the table is used as source, or topics for writing when the table is used as sink. It also supports topic list for source by separating topic by semicolon like `'topic-1;topic-2'`. Note, only one of "topic-pattern" and "topic" can be specified. For sinks, the topic name is the topic to write data. It also supports topic list for sinks. The provided topic-list is treated as a allow list of valid values for the \`topic\` metadata column. If a list is provided, for sink table, 'topic' metadata column is writable and must be specified. |
| ##### properties.bootstrap.servers [Anchor link for: properties bootstrap servers](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#properties-bootstrap-servers) | required | (none) | String | Comma separated list of Kafka brokers. |
| ##### properties.\* [Anchor link for: properties](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#properties) | optional | (none) | String | This can set and pass arbitrary Kafka configurations. Suffix names must match the configuration key defined in [Kafka Configuration documentation](https://kafka.apache.org/documentation/#configuration). Flink will remove the "properties." key prefix and pass the transformed key and values to the underlying KafkaClient. For example, you can disable automatic topic creation via `'properties.allow.auto.create.topics' = 'false'`. But there are some configurations that do not support to set, because Flink will override them, e.g. `'auto.offset.reset'`. |
| ##### key.format [Anchor link for: key format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#key-format) | required | (none) | String | The format used to deserialize and serialize the key part of Kafka messages.<br>Please refer to the [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page<br>for more details and more format options.<br>Attention Compared to the regular Kafka connector, the<br> key fields are specified by the `PRIMARY KEY` syntax. |
| ##### key.fields-prefix [Anchor link for: key fields prefix](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#key-fields-prefix) | optional | (none) | String | Defines a custom prefix for all fields of the key format to avoid name clashes with fields<br> of the value format. By default, the prefix is empty. If a custom prefix is defined, both the<br> table schema and `'key.fields'` will work with prefixed names. When constructing the<br> data type of the key format, the prefix will be removed and the non-prefixed names will be used<br> within the key format. Please note that this option requires that `'value.fields-include'`<br> must be set to `'EXCEPT_KEY'`. |
| ##### value.format [Anchor link for: value format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#value-format) | required | (none) | String | The format used to deserialize and serialize the value part of Kafka messages.<br> Please refer to the [formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page<br> for more details and more format options. |
| ##### value.fields-include [Anchor link for: value fields include](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#value-fields-include) | optional | ALL | Enum<br>Possible values: \[ALL, EXCEPT\_KEY\] | Defines a strategy how to deal with key columns in the data type of the value format. By<br> default, `'ALL'` physical columns of the table schema will be included in the value<br> format which means that key columns appear in the data type for both the key and value format. |
| ##### scan.parallelism [Anchor link for: scan parallelism](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#scan-parallelism) | optional | no | (none) | Integer | Defines the parallelism of the upsert-kafka source operator. If not set, the global default parallelism is used. |
| ##### sink.parallelism [Anchor link for: sink parallelism](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#sink-parallelism) | optional | (none) | Integer | Defines the parallelism of the upsert-kafka sink operator. By default, the parallelism is determined by the framework using the same parallelism of the upstream chained operator. |
| ##### sink.buffer-flush.max-rows [Anchor link for: sink buffer flush max rows](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#sink-buffer-flush-max-rows) | optional | 0 | Integer | The max size of buffered records before flush.<br> When the sink receives many updates on the same key, the buffer will retain the last record of the same key.<br> This can help to reduce data shuffling and avoid possible tombstone messages to Kafka topic. Can be set to '0' to disable it.<br> By default, this is disabled. Note both `'sink.buffer-flush.max-rows'` and<br> `'sink.buffer-flush.interval'` must be set to be greater than zero to enable sink buffer flushing. |
| ##### sink.buffer-flush.interval [Anchor link for: sink buffer flush interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#sink-buffer-flush-interval) | optional | 0 | Duration | The flush interval mills, over this time, asynchronous threads will flush data.<br> When the sink receives many updates on the same key, the buffer will retain the last record of the same key.<br> This can help to reduce data shuffling and avoid possible tombstone messages to Kafka topic. Can be set to '0' to disable it.<br> By default, this is disabled. Note both `'sink.buffer-flush.max-rows'` and<br> `'sink.buffer-flush.interval'` must be set to be greater than zero to enable sink buffer flushing. |
| ##### sink.delivery-guarantee [Anchor link for: sink delivery guarantee](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#sink-delivery-guarantee) | optional | no | at-least-once | String | Defines the delivery semantic for the upsert-kafka sink. Valid enumerationns are `'at-least-once'`, `'exactly-once'` and `'none'`. See [Consistency guarantees](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/#consistency-guarantees) for more details. |
| ##### sink.transactional-id-prefix [Anchor link for: sink transactional id prefix](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#sink-transactional-id-prefix) | optional | yes | (none) | String | If the delivery guarantee is configured as `'exactly-once'` this value must be set and is used a prefix for the identifier of all opened Kafka transactions. |

## Features  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#features)

### Key and Value Formats  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#key-and-value-formats)

See the [regular Kafka connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kafka/#key-and-value-formats) for more
explanation around key and value formats. However, note that this connector requires both a key and
value format where the key fields are derived from the `PRIMARY KEY` constraint.

The following example shows how to specify and configure key and value formats. The format options are
prefixed with either the `'key'` or `'value'` plus format identifier.

SQL

```sql
CREATE TABLE KafkaTable (
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp',
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  PRIMARY KEY (`user_id`) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  ...

  'key.format' = 'json',
  'key.json.ignore-parse-errors' = 'true',

  'value.format' = 'json',
  'value.json.fail-on-missing-field' = 'false',
  'value.fields-include' = 'EXCEPT_KEY'
)
```

### Primary Key Constraints  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#primary-key-constraints)

The Upsert Kafka always works in the upsert fashion and requires to define the primary key in the DDL.
With the assumption that records with the same key should be ordered in the same partition, the
primary key semantic on the changelog source means the materialized changelog is unique on the primary
keys. The primary key definition will also control which fields should end up in Kafka’s key.

### Consistency Guarantees  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#consistency-guarantees)

By default, an Upsert Kafka sink ingests data with at-least-once guarantees into a Kafka topic if
the query is executed with [checkpointing enabled](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/checkpointing/#enabling-and-configuring-checkpointing).

This means, Flink may write duplicate records with the same key into the Kafka topic. But as the
connector is working in the upsert mode, the last record on the same key will take effect when
reading back as a source. Therefore, the upsert-kafka connector achieves idempotent writes just like
the [HBase sink](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/hbase/).

With Flink’s checkpointing enabled, the `upsert-kafka` connector can provide exactly-once delivery guarantees.

Besides enabling Flink’s checkpointing, you can also choose three different modes of operating chosen by passing appropriate `sink.delivery-guarantee` option:

- `none`: Flink will not guarantee anything. Produced records can be lost or they can be duplicated.
- `at-least-once` (default setting): This guarantees that no records will be lost (although they can be duplicated).
- `exactly-once`: Kafka transactions will be used to provide exactly-once semantic. Whenever you write
to Kafka using transactions, do not forget about setting desired `isolation.level` (`read_uncommitted`
or `read_committed` \- the latter one is the default value) for any application consuming records
from Kafka.

Please refer to [Kafka connector documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kafka/#kafka-producers-and-fault-tolerance) for more caveats about delivery guarantees.

### Source Per-Partition Watermarks  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#source-per-partition-watermarks)

Flink supports to emit per-partition watermarks for Upsert Kafka. Watermarks are generated inside the Kafka
consumer. The per-partition watermarks are merged in the same way as watermarks are merged during streaming
shuffles. The output watermark of the source is determined by the minimum watermark among the partitions
it reads. If some partitions in the topics are idle, the watermark generator will not advance. You can
alleviate this problem by setting the [`'table.exec.source.idle-timeout'`](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/config/#table-exec-source-idle-timeout)
option in the table configuration.

Please refer to [Kafka watermark strategies](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/event-time/generating_watermarks/#watermark-strategies-and-the-kafka-connector)
for more details.

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/upsert-kafka/\#data-type-mapping)

Upsert Kafka stores message keys and values as bytes, so Upsert Kafka doesn’t have schema or data types.
The messages are serialized and deserialized by formats, e.g. csv, json, avro. Thus, the data type mapping
is determined by specific formats. Please refer to [Formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/)
pages for more details.