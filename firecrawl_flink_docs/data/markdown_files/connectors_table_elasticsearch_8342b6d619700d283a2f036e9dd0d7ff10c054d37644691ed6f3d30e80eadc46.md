# Elasticsearch SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#elasticsearch-sql-connector)

Sink: BatchSink: Streaming Append & Upsert Mode

The Elasticsearch connector allows for writing into an index of the Elasticsearch engine. This document describes how to setup the Elasticsearch Connector to run SQL queries against Elasticsearch.

The connector can operate in upsert mode for exchanging UPDATE/DELETE messages with the external system using the primary key defined on the DDL.

If no primary key is defined on the DDL, the connector can only operate in append mode for exchanging INSERT only messages with external system.

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

The Elasticsearch connector is not part of the binary distribution.
See how to link with it for cluster execution [here](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/configuration/overview/).

## How to create an Elasticsearch table  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#how-to-create-an-elasticsearch-table)

The example below shows how to create an Elasticsearch sink table:

```sql
CREATE TABLE myUserTable (
  user_id STRING,
  user_name STRING,
  uv BIGINT,
  pv BIGINT,
  PRIMARY KEY (user_id) NOT ENFORCED
) WITH (
  'connector' = 'elasticsearch-7',
  'hosts' = 'http://localhost:9200',
  'index' = 'users'
);
```

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#connector-options)

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#connector) | required | no | (none) | String | Specify what connector to use, valid values are:<br> <br>- `elasticsearch-6`: connect to Elasticsearch 6.x cluster.<br>- `elasticsearch-7`: connect to Elasticsearch 7.x cluster. |
| ##### hosts [Anchor link for: hosts](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#hosts) | required | yes | (none) | String | One or more Elasticsearch hosts to connect to, e.g. `'http://host_name:9092;http://host_name:9093'`. |
| ##### index [Anchor link for: index](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#index) | required | yes | (none) | String | Elasticsearch index for every record. Can be a static index (e.g. `'myIndex'`) or<br> a dynamic index (e.g. `'index-{log_ts|yyyy-MM-dd}'`).<br> See the following [Dynamic Index](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/#dynamic-index) section for more details. |
| ##### document-type [Anchor link for: document type](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#document-type) | required in 6.x | yes in 6.x | (none) | String | Elasticsearch document type. Not necessary anymore in `elasticsearch-7`. |
| ##### document-id.key-delimiter [Anchor link for: document id key delimiter](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#document-id-key-delimiter) | optional | yes | \_ | String | Delimiter for composite keys ("\_" by default), e.g., "$" would result in IDs "KEY1$KEY2$KEY3". |
| ##### username [Anchor link for: username](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#username) | optional | yes | (none) | String | Username used to connect to Elasticsearch instance. Please notice that Elasticsearch doesn't pre-bundled security feature, but you can enable it by following the [guideline](https://www.elastic.co/guide/en/elasticsearch/reference/master/configuring-security.html) to secure an Elasticsearch cluster. |
| ##### password [Anchor link for: password](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#password) | optional | yes | (none) | String | Password used to connect to Elasticsearch instance. If `username` is configured, this option must be configured with non-empty string as well. |
| ##### failure-handler [Anchor link for: failure handler](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#failure-handler) | optional | yes | fail | String | Failure handling strategy in case a request to Elasticsearch fails. Valid strategies are:<br> <br>- `fail`: throws an exception if a request fails and thus causes a job failure.<br>- `ignore`: ignores failures and drops the request.<br>- `retry-rejected`: re-adds requests that have failed due to queue capacity saturation.<br>- custom class name: for failure handling with a ActionRequestFailureHandler subclass. |
| ##### sink.flush-on-checkpoint [Anchor link for: sink flush on checkpoint](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-flush-on-checkpoint) | optional |  | true | Boolean | Flush on checkpoint or not. When disabled, a sink will not wait for all pending action requests<br> to be acknowledged by Elasticsearch on checkpoints. Thus, a sink does NOT provide any strong<br> guarantees for at-least-once delivery of action requests. |
| ##### sink.bulk-flush.max-actions [Anchor link for: sink bulk flush max actions](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-max-actions) | optional | yes | 1000 | Integer | Maximum number of buffered actions per bulk request.<br> Can be set to `'0'` to disable it. |
| ##### sink.bulk-flush.max-size [Anchor link for: sink bulk flush max size](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-max-size) | optional | yes | 2mb | MemorySize | Maximum size in memory of buffered actions per bulk request. Must be in MB granularity.<br> Can be set to `'0'` to disable it. |
| ##### sink.bulk-flush.interval [Anchor link for: sink bulk flush interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-interval) | optional | yes | 1s | Duration | The interval to flush buffered actions.<br> Can be set to `'0'` to disable it. Note, both `'sink.bulk-flush.max-size'` and `'sink.bulk-flush.max-actions'`<br> can be set to `'0'` with the flush interval set allowing for complete async processing of buffered actions. |
| ##### sink.bulk-flush.backoff.strategy [Anchor link for: sink bulk flush backoff strategy](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-backoff-strategy) | optional | yes | DISABLED | String | Specify how to perform retries if any flush actions failed due to a temporary request error. Valid strategies are:<br> <br>- `DISABLED`: no retry performed, i.e. fail after the first request error.<br>- `CONSTANT`: wait for backoff delay between retries.<br>- `EXPONENTIAL`: initially wait for backoff delay and increase exponentially between retries. |
| ##### sink.bulk-flush.backoff.max-retries [Anchor link for: sink bulk flush backoff max retries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-backoff-max-retries) | optional | yes | (none) | Integer | Maximum number of backoff retries. |
| ##### sink.bulk-flush.backoff.delay [Anchor link for: sink bulk flush backoff delay](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#sink-bulk-flush-backoff-delay) | optional | yes | (none) | Duration | Delay between each backoff attempt. For `CONSTANT` backoff, this is simply the delay between each retry. For `EXPONENTIAL` backoff, this is the initial base delay. |
| ##### connection.path-prefix [Anchor link for: connection path prefix](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#connection-path-prefix) | optional | yes | (none) | String | Prefix string to be added to every REST communication, e.g., `'/v1'`. |
| ##### format [Anchor link for: format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#format) | optional | no | json | String | Elasticsearch connector supports to specify a format. The format must produce a valid json document.<br> By default uses built-in `'json'` format. Please refer to [JSON Format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) page for more details. |

## Features  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#features)

### Key Handling  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#key-handling)

The Elasticsearch sink can work in either upsert mode or append mode, depending on whether a primary key is defined.
If a primary key is defined, the Elasticsearch sink works in upsert mode which can consume queries containing UPDATE/DELETE messages.
If a primary key is not defined, the Elasticsearch sink works in append mode which can only consume queries containing INSERT only messages.

In the Elasticsearch connector, the primary key is used to calculate the Elasticsearch document id, which is a string of up to 512 bytes. It cannot have whitespaces.
The Elasticsearch connector generates a document ID string for every row by concatenating all primary key fields in the order defined in the DDL using a key delimiter specified by `document-id.key-delimiter`.
Certain types are not allowed as a primary key field as they do not have a good string representation, e.g. `BYTES`, `ROW`, `ARRAY`, `MAP`, etc.
If no primary key is specified, Elasticsearch will generate a document id automatically.

See [CREATE TABLE DDL](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/sql/create/#create-table) for more details about the PRIMARY KEY syntax.

### Dynamic Index  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#dynamic-index)

The Elasticsearch sink supports both static index and dynamic index.

If you want to have a static index, the `index` option value should be a plain string, e.g. `'myusers'`, all the records will be consistently written into “myusers” index.

If you want to have a dynamic index, you can use `{field_name}` to reference a field value in the record to dynamically generate a target index.
You can also use `'{field_name|date_format_string}'` to convert a field value of `TIMESTAMP/DATE/TIME` type into the format specified by the `date_format_string`.
The `date_format_string` is compatible with Java’s [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/index.html).
For example, if the option value is `'myusers-{log_ts|yyyy-MM-dd}'`, then a record with `log_ts` field value `2020-03-27 12:25:55` will be written into “myusers-2020-03-27” index.

You can also use `'{now()|date_format_string}'` to convert the current system time to the format specified by `date_format_string`. The corresponding time type of `now()` is `TIMESTAMP_WITH_LTZ`.
When formatting the system time as a string, the time zone configured in the session through `table.local-time-zone` will be used. You can use `NOW()`, `now()`, `CURRENT_TIMESTAMP`, `current_timestamp`.

**NOTE:** When using the dynamic index generated by the current system time, for changelog stream, there is no guarantee that the records with the same primary key can generate the same index name.
Therefore, the dynamic index based on the system time can only support append only stream.

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/elasticsearch/\#data-type-mapping)

Elasticsearch stores document in a JSON string. So the data type mapping is between Flink data type and JSON data type.
Flink uses built-in `'json'` format for Elasticsearch connector. Please refer to [JSON Format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/json/) page for more type mapping details.