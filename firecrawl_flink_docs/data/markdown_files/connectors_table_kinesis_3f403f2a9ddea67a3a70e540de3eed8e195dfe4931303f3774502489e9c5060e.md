# Amazon Kinesis Data Streams SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#amazon-kinesis-data-streams-sql-connector)

Scan Source: UnboundedSink: BatchSink: Streaming Append Mode

The Kinesis connector allows for reading data from and writing data into [Amazon Kinesis Data Streams (KDS)](https://aws.amazon.com/kinesis/data-streams/).

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

The Kinesis connector is not part of the binary distribution.
See how to link with it for cluster execution [here](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/configuration/overview/).

### Versioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#versioning)

There are two available Table API and SQL distributions for the Kinesis connector.
This has resulted from an ongoing migration from the deprecated `SourceFunction` and `SinkFunction` interfaces to the new `Source` and `Sink` interfaces.

The Table API and SQL interfaces in Flink only allow one TableFactory for each connector identifier.
Only one TableFactory with identifier `kinesis` can be included in your application’s dependencies.

The following table clarifies the underlying interface that is used depending on the distribution selected:

| Dependency | Connector Version | Source connector identifier (interface) | Sink connector identifier (interface) |
| --- | --- | --- | --- |
| `flink-sql-connector-aws-kinesis-streams` | `5.x` or later | `kinesis`(`Source`) | `kinesis`(`Sink`) |
| `flink-sql-connector-aws-kinesis-streams` | `4.x` or earlier | N/A (no source packaged) | `kinesis`(`Sink`) |
| `flink-sql-connector-kinesis` | `5.x` or later | `kinesis`(`Source`), `kinesis-legacy`(`SourceFunction`) | `kinesis`(`Sink`) |
| `flink-sql-connector-kinesis` | `4.x` or earlier | `kinesis`(`SourceFunction`) | `kinesis`(`Sink`) |

> Only include one artifact, either `flink-sql-connector-aws-kinesis-streams` or `flink-sql-connector-kinesis`. Including both will result in clashing TableFactory names.

These docs are targeted for versions 5.x onwards. The main configuration section targets `kinesis` identifier.
For legacy configuration, please see [Configuration (`kinesis-legacy`)](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#connector-options-kinesis-legacy)

### Migrating from v4.x to v5.x  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#migrating-from-v4x-to-v5x)

There is no state compatibility between Table API and SQL API between 4.x and 5.x.
This is due to the underlying implementation being changed.

Consider starting the job with v5.x `kinesis` table with `source.init.position` of `AT_TIMESTAMP` slightly before the time when the job with v4.x `kinesis` table was stopped.
Note that this may result in some re-processed some records.

## How to create a Kinesis data stream table  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#how-to-create-a-kinesis-data-stream-table)

Follow the instructions from the [Amazon KDS Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) to set up a Kinesis stream.
The following example shows how to create a table backed by a Kinesis data stream:

```sql
CREATE TABLE KinesisTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `category_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP(3)
)
PARTITIONED BY (user_id, item_id)
WITH (
  'connector' = 'kinesis',
  'stream.arn' = 'arn:aws:kinesis:us-east-1:012345678901:stream/my-stream-name',
  'aws.region' = 'us-east-1',
  'source.init.position' = 'LATEST',
  'format' = 'csv'
);
```

## Available Metadata  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#available-metadata)

> The `kinesis` table Source has a known bug that means `VIRTUAL` columns are not supported.
> Please use `kinesis-legacy` until [the fix](https://issues.apache.org/jira/browse/FLINK-36671) is completed.

The following metadata can be exposed as read-only (`VIRTUAL`) columns in a table definition. This is only available in the `kinesis-legacy` connector only.

| Key | Data Type | Description |
| --- | --- | --- |
| `timestamp` | `TIMESTAMP_LTZ(3) NOT NULL` | The approximate time when the record was inserted into the stream. |
| `shard-id` | `VARCHAR(128) NOT NULL` | The unique identifier of the shard within the stream from which the record was read. |
| `sequence-number` | `VARCHAR(128) NOT NULL` | The unique identifier of the record within its shard. |

The extended `CREATE TABLE` example demonstrates the syntax for exposing these metadata fields:

```sql
CREATE TABLE KinesisTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `category_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP(3),
  `arrival_time` TIMESTAMP(3) METADATA FROM 'timestamp' VIRTUAL,
  `shard_id` VARCHAR(128) NOT NULL METADATA FROM 'shard-id' VIRTUAL,
  `sequence_number` VARCHAR(128) NOT NULL METADATA FROM 'sequence-number' VIRTUAL
)
PARTITIONED BY (user_id, item_id)
WITH (
  'connector' = 'kinesis-legacy',
  'stream' = 'user_behavior',
  'aws.region' = 'us-east-2',
  'scan.stream.initpos' = 'LATEST',
  'format' = 'csv'
);
```

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#connector-options)

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| Common Options |
| --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#connector) | required | no | (none) | String | Specify what connector to use. For Kinesis use `'kinesis'` or `'kinesis-legacy'`. See [Versioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#versioning) for details. |
| ##### stream.arn [Anchor link for: stream arn](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#stream-arn) | required | yes | (none) | String | Name of the Kinesis data stream backing this table. |
| ##### format [Anchor link for: format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#format) | required | no | (none) | String | The format used to deserialize and serialize Kinesis data stream records. See [Data Type Mapping](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#data-type-mapping) for details. |
| ##### aws.region [Anchor link for: aws region](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-region) | required | no | (none) | String | The AWS region where the stream is defined. |
| ##### aws.endpoint [Anchor link for: aws endpoint](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-endpoint) | optional | no | (none) | String | The AWS endpoint for Kinesis (derived from the AWS region setting if not set). |
| ##### aws.trust.all.certificates [Anchor link for: aws trust all certificates](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-trust-all-certificates) | optional | no | false | Boolean | If true accepts all SSL certificates. This is not recommended for production environments, but should only be used for testing purposes. |
| Authentication Options |
| --- |
| ##### aws.credentials.provider [Anchor link for: aws credentials provider](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-provider) | optional | no | AUTO | String | A credentials provider to use when authenticating against the Kinesis endpoint. See [Authentication](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#authentication) for details. |
| ##### aws.credentials.basic.accesskeyid [Anchor link for: aws credentials basic accesskeyid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-basic-accesskeyid) | optional | no | (none) | String | The AWS access key ID to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.basic.secretkey [Anchor link for: aws credentials basic secretkey](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-basic-secretkey) | optional | no | (none) | String | The AWS secret key to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.profile.path [Anchor link for: aws credentials profile path](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-profile-path) | optional | no | (none) | String | Optional configuration for profile path if credential provider type is set to be PROFILE. |
| ##### aws.credentials.profile.name [Anchor link for: aws credentials profile name](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-profile-name) | optional | no | (none) | String | Optional configuration for profile name if credential provider type is set to be PROFILE. |
| ##### aws.credentials.role.arn [Anchor link for: aws credentials role arn](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-arn) | optional | no | (none) | String | The role ARN to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.sessionName [Anchor link for: aws credentials role sessionname](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-sessionname) | optional | no | (none) | String | The role session name to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.externalId [Anchor link for: aws credentials role externalid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-externalid) | optional | no | (none) | String | The external ID to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.stsEndpoint [Anchor link for: aws credentials role stsendpoint](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-stsendpoint) | optional | no | (none) | String | The AWS endpoint for STS (derived from the AWS region setting if not set) to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.provider [Anchor link for: aws credentials role provider](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-provider) | optional | no | (none) | String | The credentials provider that provides credentials for assuming the role when credential provider type is set to ASSUME\_ROLE. Roles can be nested, so this value can again be set to ASSUME\_ROLE |
| ##### aws.credentials.webIdentityToken.file [Anchor link for: aws credentials webidentitytoken file](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-webidentitytoken-file) | optional | no | (none) | String | The absolute path to the web identity token file that should be used if provider type is set to WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.custom.class [Anchor link for: aws credentials custom class](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-custom-class) | required only if credential provider is set to CUSTOM | no | (none) | String | The full path (in Java package notation) to the user provided<br> class to use if credential provider type is set to be CUSTOM e.g. org.user\_company.auth.CustomAwsCredentialsProvider. |
| Source Options |
| --- |
| ##### source.init.position [Anchor link for: source init position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-init-position) | optional | no | LATEST | String | Initial position to be used when reading from the table. |
| ##### source.init.timestamp [Anchor link for: source init timestamp](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-init-timestamp) | optional | no | (none) | String | The initial timestamp to start reading Kinesis stream from (when `source.init.position` is AT\_TIMESTAMP). |
| ##### source.init.timestamp.format [Anchor link for: source init timestamp format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-init-timestamp-format) | optional | no | yyyy-MM-dd'T'HH:mm:ss.SSSXXX | String | The date format of initial timestamp to start reading Kinesis stream from (when `source.init.position` is AT\_TIMESTAMP). |
| ##### source.shard.discovery.interval [Anchor link for: source shard discovery interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-shard-discovery-interval) | optional | no | 10 s | Duration | The interval between each attempt to discover new shards. |
| ##### source.reader.type [Anchor link for: source reader type](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-reader-type) | optional | no | POLLING | String | The `ReaderType` to use for sources (`POLLING|EFO`). |
| ##### source.shard.get-records.max-record-count [Anchor link for: source shard get records max record count](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-shard-get-records-max-record-count) | optional | no | 10000 | Integer | Only applicable to POLLING `ReaderType`. The maximum number of records to try to get each time we fetch records from a AWS Kinesis shard. |
| ##### source.efo.consumer.name [Anchor link for: source efo consumer name](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-consumer-name) | optional | no | (none) | String | Only applicable to EFO `ReaderType`. The name of the EFO consumer to register with KDS. |
| ##### source.efo.lifecycle [Anchor link for: source efo lifecycle](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-lifecycle) | optional | no | JOB\_MANAGED | String | Only applicable to EFO `ReaderType`. Determine if the EFO consumer is managed by the Flink job `JOB_MANAGED|SELF_MANAGED`. |
| ##### source.efo.subscription.timeout [Anchor link for: source efo subscription timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-subscription-timeout) | optional | no | 60 s | Duration | Only applicable to EFO `ReaderType`. Timeout for EFO Consumer subscription. |
| ##### source.efo.deregister.timeout [Anchor link for: source efo deregister timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-deregister-timeout) | optional | no | 10 s | Duration | Only applicable to EFO `ReaderType`. Timeout for consumer deregistration. When timeout is reached, code will continue as per normal. |
| ##### source.efo.describe.retry-strategy.attempts.max [Anchor link for: source efo describe retry strategy attempts max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-describe-retry-strategy-attempts-max) | optional | no | 100 | Integer | Only applicable to EFO `ReaderType`. Maximum number of attempts for the exponential backoff retry strategy when calling `DescribeStreamConsumer`. |
| ##### source.efo.describe.retry-strategy.delay.min [Anchor link for: source efo describe retry strategy delay min](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-describe-retry-strategy-delay-min) | optional | no | 2 s | Duration | Only applicable to EFO `ReaderType`. Base delay for the exponential backoff retry strategy when calling `DescribeStreamConsumer`. |
| ##### source.efo.describe.retry-strategy.delay.max [Anchor link for: source efo describe retry strategy delay max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#source-efo-describe-retry-strategy-delay-max) | optional | no | 60 s | Duration | Only applicable to EFO `ReaderType`. Max delay for the exponential backoff retry strategy when calling `DescribeStreamConsumer`. |
| Sink Options |
| --- |
| ##### sink.partitioner [Anchor link for: sink partitioner](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-partitioner) | optional | yes | random or row-based | String | Optional output partitioning from Flink's partitions into Kinesis shards. See [Sink Partitioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#sink-partitioning) for details. |
| ##### sink.partitioner-field-delimiter [Anchor link for: sink partitioner field delimiter](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-partitioner-field-delimiter) | optional | yes | \| | String | Optional field delimiter for a fields-based partitioner derived from a PARTITION BY clause. See [Sink Partitioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#sink-partitioning) for details. |
| ##### sink.producer.\* [Anchor link for: sink producer](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-producer) | optional | no | (none) |  | Deprecated options previously used by the legacy connector.<br> Options with equivalant alternatives in `KinesisStreamsSink` are matched <br> to their respective properties. Unsupported options are logged out to user as warnings. |
| ##### sink.http-client.max-concurrency [Anchor link for: sink http client max concurrency](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-max-concurrency) | optional | no | 10000 | Integer | Maximum number of allowed concurrent requests by `KinesisAsyncClient`. |
| ##### sink.http-client.read-timeout [Anchor link for: sink http client read timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-read-timeout) | optional | no | 360000 | Integer | Maximum amount of time in ms for requests to be sent by `KinesisAsyncClient`. |
| ##### sink.http-client.protocol.version [Anchor link for: sink http client protocol version](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-protocol-version) | optional | no | HTTP2 | String | Http version used by Kinesis Client. |
| ##### sink.batch.max-size [Anchor link for: sink batch max size](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-batch-max-size) | optional | yes | 500 | Integer | Maximum batch size of elements to be passed to `KinesisAsyncClient` to be written downstream. |
| ##### sink.requests.max-inflight [Anchor link for: sink requests max inflight](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-requests-max-inflight) | optional | yes | 16 | Integer | Request threshold for uncompleted requests by `KinesisAsyncClient`before blocking new write requests and applying backpressure. |
| ##### sink.requests.max-buffered [Anchor link for: sink requests max buffered](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-requests-max-buffered) | optional | yes | 10000 | String | Request buffer threshold for buffered requests by `KinesisAsyncClient` before blocking new write requests and applying backpressure. |
| ##### sink.flush-buffer.size [Anchor link for: sink flush buffer size](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-flush-buffer-size) | optional | yes | 5242880 | Long | Threshold value in bytes for writer buffer in `KinesisAsyncClient` before flushing. |
| ##### sink.flush-buffer.timeout [Anchor link for: sink flush buffer timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-flush-buffer-timeout) | optional | yes | 5000 | Long | Threshold time in milliseconds for an element to be in a buffer of`KinesisAsyncClient` before flushing. |
| ##### sink.fail-on-error [Anchor link for: sink fail on error](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-fail-on-error) | optional | yes | false | Boolean | Flag used for retrying failed requests. If set any request failure will not be retried and will fail the job. |

## Features  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#features)

> Refer to the [Kinesis Datastream API](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kinesis/) documentation for more detailed description of features.

### Sink Partitioning  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-partitioning)

Kinesis data streams consist of one or more shards, and the `sink.partitioner` option allows you to control how records written into a multi-shard Kinesis-backed table will be partitioned between its shards.
Valid values are:

- `fixed`: Kinesis `PartitionKey` values derived from the Flink subtask index, so each Flink partition ends up in at most one Kinesis partition (assuming that no re-sharding takes place at runtime).
- `random`: Kinesis `PartitionKey` values are assigned randomly. This is the default value for tables not defined with a `PARTITION BY` clause.
- Custom `FixedKinesisPartitioner` subclass: e.g. `'org.mycompany.MyPartitioner'`.

> Records written into tables defining a `PARTITION BY` clause will always be partitioned based on a concatenated projection of the `PARTITION BY` fields.
> In this case, the `sink.partitioner` field cannot be used to modify this behavior (attempting to do this results in a configuration error).
> You can, however, use the `sink.partitioner-field-delimiter` option to set the delimiter of field values in the concatenated [PartitionKey](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html#Streams-PutRecord-request-PartitionKey) string (an empty string is also a valid delimiter).

# Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#data-type-mapping)

Kinesis stores records as Base64-encoded binary data objects, so it doesn’t have a notion of internal record structure.
Instead, Kinesis records are deserialized and serialized by formats, e.g. ‘avro’, ‘csv’, or ‘json’.
To determine the data type of the messages in your Kinesis-backed tables, pick a suitable Flink format with the `format` keyword.
Please refer to the [Formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) pages for more details.

## Connector Options (`kinesis-legacy`)  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#connector-options-kinesis-legacy)

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| Common Options |
| --- |
| ##### connector [Anchor link for: connector 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#connector-1) | required | no | (none) | String | Specify what connector to use. For Kinesis use `'kinesis'`. |
| ##### stream [Anchor link for: stream](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#stream) | required | yes | (none) | String | Name of the Kinesis data stream backing this table. |
| ##### format [Anchor link for: format 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#format-1) | required | no | (none) | String | The format used to deserialize and serialize Kinesis data stream records. See [Data Type Mapping](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#data-type-mapping) for details. |
| ##### aws.region [Anchor link for: aws region 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-region-1) | optional | no | (none) | String | The AWS region where the stream is defined. Either this or `aws.endpoint` are required. |
| ##### aws.endpoint [Anchor link for: aws endpoint 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-endpoint-1) | optional | no | (none) | String | The AWS endpoint for Kinesis (derived from the AWS region setting if not set). Either this or `aws.region` are required. |
| ##### aws.trust.all.certificates [Anchor link for: aws trust all certificates 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-trust-all-certificates-1) | optional | no | false | Boolean | If true accepts all SSL certificates. |
| Authentication Options |
| --- |
| ##### aws.credentials.provider [Anchor link for: aws credentials provider 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-provider-1) | optional | no | AUTO | String | A credentials provider to use when authenticating against the Kinesis endpoint. See [Authentication](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#authentication) for details. |
| ##### aws.credentials.basic.accesskeyid [Anchor link for: aws credentials basic accesskeyid 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-basic-accesskeyid-1) | optional | no | (none) | String | The AWS access key ID to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.basic.secretkey [Anchor link for: aws credentials basic secretkey 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-basic-secretkey-1) | optional | no | (none) | String | The AWS secret key to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.profile.path [Anchor link for: aws credentials profile path 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-profile-path-1) | optional | no | (none) | String | Optional configuration for profile path if credential provider type is set to be PROFILE. |
| ##### aws.credentials.profile.name [Anchor link for: aws credentials profile name 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-profile-name-1) | optional | no | (none) | String | Optional configuration for profile name if credential provider type is set to be PROFILE. |
| ##### aws.credentials.role.arn [Anchor link for: aws credentials role arn 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-arn-1) | optional | no | (none) | String | The role ARN to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.sessionName [Anchor link for: aws credentials role sessionname 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-sessionname-1) | optional | no | (none) | String | The role session name to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.externalId [Anchor link for: aws credentials role externalid 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-externalid-1) | optional | no | (none) | String | The external ID to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.stsEndpoint [Anchor link for: aws credentials role stsendpoint 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-stsendpoint-1) | optional | no | (none) | String | The AWS endpoint for STS (derived from the AWS region setting if not set) to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.provider [Anchor link for: aws credentials role provider 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-role-provider-1) | optional | no | (none) | String | The credentials provider that provides credentials for assuming the role when credential provider type is set to ASSUME\_ROLE. Roles can be nested, so this value can again be set to ASSUME\_ROLE |
| ##### aws.credentials.webIdentityToken.file [Anchor link for: aws credentials webidentitytoken file 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-webidentitytoken-file-1) | optional | no | (none) | String | The absolute path to the web identity token file that should be used if provider type is set to WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.custom.class [Anchor link for: aws credentials custom class 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#aws-credentials-custom-class-1) | required only if credential provider is set to CUSTOM | no | (none) | String | The full path (in Java package notation) to the user provided<br> class to use if credential provider type is set to be CUSTOM e.g. org.user\_company.auth.CustomAwsCredentialsProvider. |
| Source Options |
| --- |
| ##### scan.stream.initpos [Anchor link for: scan stream initpos](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-initpos) | optional | no | LATEST | String | Initial position to be used when reading from the table. See [Start Reading Position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#start-reading-position) for details. |
| ##### scan.stream.initpos-timestamp [Anchor link for: scan stream initpos timestamp](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-initpos-timestamp) | optional | no | (none) | String | The initial timestamp to start reading Kinesis stream from (when `scan.stream.initpos` is AT\_TIMESTAMP). See [Start Reading Position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#start-reading-position) for details. |
| ##### scan.stream.initpos-timestamp-format [Anchor link for: scan stream initpos timestamp format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-initpos-timestamp-format) | optional | no | yyyy-MM-dd'T'HH:mm:ss.SSSXXX | String | The date format of initial timestamp to start reading Kinesis stream from (when `scan.stream.initpos` is AT\_TIMESTAMP). See [Start Reading Position](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#start-reading-position) for details. |
| ##### scan.stream.recordpublisher [Anchor link for: scan stream recordpublisher](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-recordpublisher) | optional | no | POLLING | String | The `RecordPublisher` type to use for sources. |
| ##### scan.stream.efo.consumername [Anchor link for: scan stream efo consumername](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-efo-consumername) | optional | no | (none) | String | The name of the EFO consumer to register with KDS. |
| ##### scan.stream.efo.registration [Anchor link for: scan stream efo registration](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-efo-registration) | optional | no | LAZY | String | Determine how and when consumer de-/registration is performed (LAZY\|EAGER\|NONE). |
| ##### scan.stream.efo.consumerarn [Anchor link for: scan stream efo consumerarn](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-efo-consumerarn) | optional | no | (none) | String | The prefix of consumer ARN for a given stream. |
| ##### scan.stream.efo.http-client.max-concurrency [Anchor link for: scan stream efo http client max concurrency](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-efo-http-client-max-concurrency) | optional | no | 10000 | Integer | Maximum number of allowed concurrent requests for the EFO client. |
| ##### scan.shard-assigner [Anchor link for: scan shard assigner](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-assigner) | optional | no | default | String | The shard assigner used to map shards to Flink subtasks (default\|uniform). You can also supply your own shard assigner via the Java Service Provider Interfaces (SPI). |
| ##### scan.stream.describe.maxretries [Anchor link for: scan stream describe maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describe-maxretries) | optional | no | 50 | Integer | The maximum number of `describeStream` attempts if we get a recoverable exception. |
| ##### scan.stream.describe.backoff.base [Anchor link for: scan stream describe backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describe-backoff-base) | optional | no | 2000 | Long | The base backoff time (in milliseconds) between each `describeStream` attempt (for consuming from DynamoDB streams). |
| ##### scan.stream.describe.backoff.max [Anchor link for: scan stream describe backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describe-backoff-max) | optional | no | 5000 | Long | The maximum backoff time (in milliseconds) between each `describeStream` attempt (for consuming from DynamoDB streams). |
| ##### scan.stream.describe.backoff.expconst [Anchor link for: scan stream describe backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describe-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `describeStream` attempt (for consuming from DynamoDB streams). |
| ##### scan.list.shards.maxretries [Anchor link for: scan list shards maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-list-shards-maxretries) | optional | no | 10 | Integer | The maximum number of `listShards` attempts if we get a recoverable exception. |
| ##### scan.list.shards.backoff.base [Anchor link for: scan list shards backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-list-shards-backoff-base) | optional | no | 1000 | Long | The base backoff time (in milliseconds) between each `listShards` attempt. |
| ##### scan.list.shards.backoff.max [Anchor link for: scan list shards backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-list-shards-backoff-max) | optional | no | 5000 | Long | The maximum backoff time (in milliseconds) between each `listShards` attempt. |
| ##### scan.list.shards.backoff.expconst [Anchor link for: scan list shards backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-list-shards-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `listShards` attempt. |
| ##### scan.stream.describestreamconsumer.maxretries [Anchor link for: scan stream describestreamconsumer maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describestreamconsumer-maxretries) | optional | no | 50 | Integer | The maximum number of `describeStreamConsumer` attempts if we get a recoverable exception. |
| ##### scan.stream.describestreamconsumer.backoff.base [Anchor link for: scan stream describestreamconsumer backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describestreamconsumer-backoff-base) | optional | no | 2000 | Long | The base backoff time (in milliseconds) between each `describeStreamConsumer` attempt. |
| ##### scan.stream.describestreamconsumer.backoff.max [Anchor link for: scan stream describestreamconsumer backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describestreamconsumer-backoff-max) | optional | no | 5000 | Long | The maximum backoff time (in milliseconds) between each `describeStreamConsumer` attempt. |
| ##### scan.stream.describestreamconsumer.backoff.expconst [Anchor link for: scan stream describestreamconsumer backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-describestreamconsumer-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `describeStreamConsumer` attempt. |
| ##### scan.stream.registerstreamconsumer.maxretries [Anchor link for: scan stream registerstreamconsumer maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-registerstreamconsumer-maxretries) | optional | no | 10 | Integer | The maximum number of `registerStream` attempts if we get a recoverable exception. |
| ##### scan.stream.registerstreamconsumer.timeout [Anchor link for: scan stream registerstreamconsumer timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-registerstreamconsumer-timeout) | optional | no | 60 | Integer | The maximum time in seconds to wait for a stream consumer to become active before giving up. |
| ##### scan.stream.registerstreamconsumer.backoff.base [Anchor link for: scan stream registerstreamconsumer backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-registerstreamconsumer-backoff-base) | optional | no | 500 | Long | The base backoff time (in milliseconds) between each `registerStream` attempt. |
| ##### scan.stream.registerstreamconsumer.backoff.max [Anchor link for: scan stream registerstreamconsumer backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-registerstreamconsumer-backoff-max) | optional | no | 2000 | Long | The maximum backoff time (in milliseconds) between each `registerStream` attempt. |
| ##### scan.stream.registerstreamconsumer.backoff.expconst [Anchor link for: scan stream registerstreamconsumer backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-registerstreamconsumer-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `registerStream` attempt. |
| ##### scan.stream.deregisterstreamconsumer.maxretries [Anchor link for: scan stream deregisterstreamconsumer maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-deregisterstreamconsumer-maxretries) | optional | no | 10 | Integer | The maximum number of `deregisterStream` attempts if we get a recoverable exception. |
| ##### scan.stream.deregisterstreamconsumer.timeout [Anchor link for: scan stream deregisterstreamconsumer timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-deregisterstreamconsumer-timeout) | optional | no | 60 | Integer | The maximum time in seconds to wait for a stream consumer to deregister before giving up. |
| ##### scan.stream.deregisterstreamconsumer.backoff.base [Anchor link for: scan stream deregisterstreamconsumer backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-deregisterstreamconsumer-backoff-base) | optional | no | 500 | Long | The base backoff time (in milliseconds) between each `deregisterStream` attempt. |
| ##### scan.stream.deregisterstreamconsumer.backoff.max [Anchor link for: scan stream deregisterstreamconsumer backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-deregisterstreamconsumer-backoff-max) | optional | no | 2000 | Long | The maximum backoff time (in milliseconds) between each `deregisterStream` attempt. |
| ##### scan.stream.deregisterstreamconsumer.backoff.expconst [Anchor link for: scan stream deregisterstreamconsumer backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-stream-deregisterstreamconsumer-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `deregisterStream` attempt. |
| ##### scan.shard.subscribetoshard.maxretries [Anchor link for: scan shard subscribetoshard maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-subscribetoshard-maxretries) | optional | no | 10 | Integer | The maximum number of `subscribeToShard` attempts if we get a recoverable exception. |
| ##### scan.shard.subscribetoshard.backoff.base [Anchor link for: scan shard subscribetoshard backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-subscribetoshard-backoff-base) | optional | no | 1000 | Long | The base backoff time (in milliseconds) between each `subscribeToShard` attempt. |
| ##### scan.shard.subscribetoshard.backoff.max [Anchor link for: scan shard subscribetoshard backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-subscribetoshard-backoff-max) | optional | no | 2000 | Long | The maximum backoff time (in milliseconds) between each `subscribeToShard` attempt. |
| ##### scan.shard.subscribetoshard.backoff.expconst [Anchor link for: scan shard subscribetoshard backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-subscribetoshard-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `subscribeToShard` attempt. |
| ##### scan.shard.getrecords.maxrecordcount [Anchor link for: scan shard getrecords maxrecordcount](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-maxrecordcount) | optional | no | 10000 | Integer | The maximum number of records to try to get each time we fetch records from a AWS Kinesis shard. |
| ##### scan.shard.getrecords.maxretries [Anchor link for: scan shard getrecords maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-maxretries) | optional | no | 3 | Integer | The maximum number of `getRecords` attempts if we get a recoverable exception. |
| ##### scan.shard.getrecords.backoff.base [Anchor link for: scan shard getrecords backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-backoff-base) | optional | no | 300 | Long | The base backoff time (in milliseconds) between `getRecords` attempts if we get a ProvisionedThroughputExceededException. |
| ##### scan.shard.getrecords.backoff.max [Anchor link for: scan shard getrecords backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-backoff-max) | optional | no | 1000 | Long | The maximum backoff time (in milliseconds) between `getRecords` attempts if we get a ProvisionedThroughputExceededException. |
| ##### scan.shard.getrecords.backoff.expconst [Anchor link for: scan shard getrecords backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `getRecords` attempt. |
| ##### scan.shard.getrecords.intervalmillis [Anchor link for: scan shard getrecords intervalmillis](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getrecords-intervalmillis) | optional | no | 200 | Long | The interval (in milliseconds) between each `getRecords` request to a AWS Kinesis shard in milliseconds. |
| ##### scan.shard.getiterator.maxretries [Anchor link for: scan shard getiterator maxretries](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getiterator-maxretries) | optional | no | 3 | Integer | The maximum number of `getShardIterator` attempts if we get ProvisionedThroughputExceededException. |
| ##### scan.shard.getiterator.backoff.base [Anchor link for: scan shard getiterator backoff base](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getiterator-backoff-base) | optional | no | 300 | Long | The base backoff time (in milliseconds) between `getShardIterator` attempts if we get a ProvisionedThroughputExceededException. |
| ##### scan.shard.getiterator.backoff.max [Anchor link for: scan shard getiterator backoff max](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getiterator-backoff-max) | optional | no | 1000 | Long | The maximum backoff time (in milliseconds) between `getShardIterator` attempts if we get a ProvisionedThroughputExceededException. |
| ##### scan.shard.getiterator.backoff.expconst [Anchor link for: scan shard getiterator backoff expconst](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-getiterator-backoff-expconst) | optional | no | 1.5 | Double | The power constant for exponential backoff between each `getShardIterator` attempt. |
| ##### scan.shard.discovery.intervalmillis [Anchor link for: scan shard discovery intervalmillis](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-discovery-intervalmillis) | optional | no | 10000 | Integer | The interval between each attempt to discover new shards. |
| ##### scan.shard.adaptivereads [Anchor link for: scan shard adaptivereads](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-adaptivereads) | optional | no | false | Boolean | The config to turn on adaptive reads from a shard. See the `AdaptivePollingRecordPublisher` documentation for details. |
| ##### scan.shard.idle.interval [Anchor link for: scan shard idle interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-shard-idle-interval) | optional | no | -1 | Long | The interval (in milliseconds) after which to consider a shard idle for purposes of watermark generation. A positive value will allow the watermark to progress even when some shards don't receive new records. |
| ##### shard.consumer.error.recoverable\[0\].exception [Anchor link for: shard consumer error recoverable 0 exception](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#shard-consumer-error-recoverable-0-exception) | optional | no | (none) | String | User-specified Exception to retry indefinitely. Example value: \`java.net.UnknownHostException\`. This configuration is a zero-based array. As such, the specified exceptions must start with index 0. Specified exceptions must be valid Throwables in classpath, or connector will fail to initialize and fail fast. |
| ##### scan.watermark.sync.interval [Anchor link for: scan watermark sync interval](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-watermark-sync-interval) | optional | no | 30000 | Long | The interval (in milliseconds) for periodically synchronizing the shared watermark state. |
| ##### scan.watermark.lookahead.millis [Anchor link for: scan watermark lookahead millis](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-watermark-lookahead-millis) | optional | no | 0 | Long | The maximum delta (in milliseconds) allowed for the reader to advance ahead of the shared global watermark. |
| ##### scan.watermark.sync.queue.capacity [Anchor link for: scan watermark sync queue capacity](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#scan-watermark-sync-queue-capacity) | optional | no | 100 | Integer | The maximum number of records that will be buffered before suspending consumption of a shard. |
| Sink Options |
| --- |
| ##### sink.partitioner [Anchor link for: sink partitioner 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-partitioner-1) | optional | yes | random or row-based | String | Optional output partitioning from Flink's partitions into Kinesis shards. See [Sink Partitioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#sink-partitioning) for details. |
| ##### sink.partitioner-field-delimiter [Anchor link for: sink partitioner field delimiter 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-partitioner-field-delimiter-1) | optional | yes | \| | String | Optional field delimiter for a fields-based partitioner derived from a PARTITION BY clause. See [Sink Partitioning](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/#sink-partitioning) for details. |
| ##### sink.producer.\* [Anchor link for: sink producer 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-producer-1) | optional | no | (none) |  | Deprecated options previously used by the legacy connector.<br> Options with equivalant alternatives in `KinesisStreamsSink` are matched <br> to their respective properties. Unsupported options are logged out to user as warnings. |
| ##### sink.http-client.max-concurrency [Anchor link for: sink http client max concurrency 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-max-concurrency-1) | optional | no | 10000 | Integer | Maximum number of allowed concurrent requests by `KinesisAsyncClient`. |
| ##### sink.http-client.read-timeout [Anchor link for: sink http client read timeout 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-read-timeout-1) | optional | no | 360000 | Integer | Maximum amount of time in ms for requests to be sent by `KinesisAsyncClient`. |
| ##### sink.http-client.protocol.version [Anchor link for: sink http client protocol version 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-http-client-protocol-version-1) | optional | no | HTTP2 | String | Http version used by Kinesis Client. |
| ##### sink.batch.max-size [Anchor link for: sink batch max size 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-batch-max-size-1) | optional | yes | 500 | Integer | Maximum batch size of elements to be passed to `KinesisAsyncClient` to be written downstream. |
| ##### sink.requests.max-inflight [Anchor link for: sink requests max inflight 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-requests-max-inflight-1) | optional | yes | 16 | Integer | Request threshold for uncompleted requests by `KinesisAsyncClient`before blocking new write requests and applying backpressure. |
| ##### sink.requests.max-buffered [Anchor link for: sink requests max buffered 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-requests-max-buffered-1) | optional | yes | 10000 | String | Request buffer threshold for buffered requests by `KinesisAsyncClient` before blocking new write requests and applying backpressure. |
| ##### sink.flush-buffer.size [Anchor link for: sink flush buffer size 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-flush-buffer-size-1) | optional | yes | 5242880 | Long | Threshold value in bytes for writer buffer in `KinesisAsyncClient` before flushing. |
| ##### sink.flush-buffer.timeout [Anchor link for: sink flush buffer timeout 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-flush-buffer-timeout-1) | optional | yes | 5000 | Long | Threshold time in milliseconds for an element to be in a buffer of`KinesisAsyncClient` before flushing. |
| ##### sink.fail-on-error [Anchor link for: sink fail on error 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/kinesis/\#sink-fail-on-error-1) | optional | yes | false | Boolean | Flag used for retrying failed requests. If set any request failure will not be retried and will fail the job. |