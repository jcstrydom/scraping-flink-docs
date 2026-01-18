# Amazon Kinesis Data Firehose SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#amazon-kinesis-data-firehose-sql-connector)

Sink: BatchSink: Streaming Append Mode

The Kinesis Data Firehose connector allows for writing data into [Amazon Kinesis Data Firehose (KDF)](https://aws.amazon.com/kinesis/data-firehose/).

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

## How to create a Kinesis Data Firehose table  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#how-to-create-a-kinesis-data-firehose-table)

Follow the instructions from the [Amazon Kinesis Data Firehose Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-kinesis-analytics-firehose-stream.html) to set up a Kinesis Data Firehose delivery stream.
The following example shows how to create a table backed by a Kinesis Data Firehose delivery stream with minimum required options:

```sql
CREATE TABLE FirehoseTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `category_id` BIGINT,
  `behavior` STRING
)
WITH (
  'connector' = 'firehose',
  'delivery-stream' = 'user_behavior',
  'aws.region' = 'us-east-2',
  'format' = 'csv'
);
```

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#connector-options)

| Option | Required | Default | Type | Description |
| --- | --- | --- | --- | --- |
| Common Options |
| --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#connector) | required | (none) | String | Specify what connector to use. For Kinesis Data Firehose use `'firehose'`. |
| ##### delivery-stream [Anchor link for: delivery stream](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#delivery-stream) | required | (none) | String | Name of the Kinesis Data Firehose delivery stream backing this table. |
| ##### format [Anchor link for: format](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#format) | required | (none) | String | The format used to deserialize and serialize Kinesis Data Firehose records. See [Data Type Mapping](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/#data-type-mapping) for details. |
| ##### aws.region [Anchor link for: aws region](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-region) | required | (none) | String | The AWS region where the delivery stream is defined. This option is required for `KinesisFirehoseSink` creation. |
| ##### aws.endpoint [Anchor link for: aws endpoint](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-endpoint) | optional | (none) | String | The AWS endpoint for Amazon Kinesis Data Firehose. |
| ##### aws.trust.all.certificates [Anchor link for: aws trust all certificates](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-trust-all-certificates) | optional | false | Boolean | If true accepts all SSL certificates. |
| Authentication Options |
| --- |
| ##### aws.credentials.provider [Anchor link for: aws credentials provider](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-provider) | optional | AUTO | String | A credentials provider to use when authenticating against the Kinesis endpoint. See [Authentication](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/#authentication) for details. |
| ##### aws.credentials.basic.accesskeyid [Anchor link for: aws credentials basic accesskeyid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-basic-accesskeyid) | optional | (none) | String | The AWS access key ID to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.basic.secretkey [Anchor link for: aws credentials basic secretkey](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-basic-secretkey) | optional | (none) | String | The AWS secret key to use when setting credentials provider type to BASIC. |
| ##### aws.credentials.profile.path [Anchor link for: aws credentials profile path](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-profile-path) | optional | (none) | String | Optional configuration for profile path if credential provider type is set to be PROFILE. |
| ##### aws.credentials.profile.name [Anchor link for: aws credentials profile name](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-profile-name) | optional | (none) | String | Optional configuration for profile name if credential provider type is set to be PROFILE. |
| ##### aws.credentials.role.arn [Anchor link for: aws credentials role arn](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-role-arn) | optional | (none) | String | The role ARN to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.sessionName [Anchor link for: aws credentials role sessionname](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-role-sessionname) | optional | (none) | String | The role session name to use when credential provider type is set to ASSUME\_ROLE or WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.role.externalId [Anchor link for: aws credentials role externalid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-role-externalid) | optional | (none) | String | The external ID to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.stsEndpoint [Anchor link for: aws credentials role stsendpoint](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-role-stsendpoint) | optional | (none) | String | The AWS endpoint for STS (derived from the AWS region setting if not set) to use when credential provider type is set to ASSUME\_ROLE. |
| ##### aws.credentials.role.provider [Anchor link for: aws credentials role provider](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-role-provider) | optional | (none) | String | The credentials provider that provides credentials for assuming the role when credential provider type is set to ASSUME\_ROLE. Roles can be nested, so this value can again be set to ASSUME\_ROLE |
| ##### aws.credentials.webIdentityToken.file [Anchor link for: aws credentials webidentitytoken file](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-webidentitytoken-file) | optional | (none) | String | The absolute path to the web identity token file that should be used if provider type is set to WEB\_IDENTITY\_TOKEN. |
| ##### aws.credentials.custom.class [Anchor link for: aws credentials custom class](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#aws-credentials-custom-class) | required only if credential provider is set to CUSTOM | (none) | String | The full path (in Java package notation) to the user provided<br> class to use if credential provider type is set to be CUSTOM e.g. org.user\_company.auth.CustomAwsCredentialsProvider. |
| Sink Options |
| --- |
| ##### sink.http-client.max-concurrency [Anchor link for: sink http client max concurrency](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-http-client-max-concurrency) | optional | 10000 | Integer | Maximum number of allowed concurrent requests by `FirehoseAsyncClient` to be delivered to delivery stream. |
| ##### sink.http-client.read-timeout [Anchor link for: sink http client read timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-http-client-read-timeout) | optional | 360000 | Integer | Maximum amount of time in ms for requests to be sent by `FirehoseAsyncClient` to delivery stream before failure. |
| ##### sink.http-client.protocol.version [Anchor link for: sink http client protocol version](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-http-client-protocol-version) | optional | HTTP2 | String | Http version used by `FirehoseAsyncClient`. |
| ##### sink.batch.max-size [Anchor link for: sink batch max size](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-batch-max-size) | optional | 500 | Integer | Maximum batch size of elements to be passed to `FirehoseAsyncClient` to be written downstream to delivery stream. |
| ##### sink.requests.max-inflight [Anchor link for: sink requests max inflight](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-requests-max-inflight) | optional | 16 | Integer | Request threshold for uncompleted requests by `FirehoseAsyncClient`before blocking new write requests. |
| ##### sink.requests.max-buffered [Anchor link for: sink requests max buffered](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-requests-max-buffered) | optional | 10000 | String | request buffer threshold by `FirehoseAsyncClient` before blocking new write requests. |
| ##### sink.flush-buffer.size [Anchor link for: sink flush buffer size](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-flush-buffer-size) | optional | 5242880 | Long | Threshold value in bytes for writer buffer in `FirehoseAsyncClient` before flushing. |
| ##### sink.flush-buffer.timeout [Anchor link for: sink flush buffer timeout](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-flush-buffer-timeout) | optional | 5000 | Long | Threshold time in ms for an element to be in a buffer of `FirehoseAsyncClient` before flushing. |
| ##### sink.fail-on-error [Anchor link for: sink fail on error](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#sink-fail-on-error) | optional | false | Boolean | Flag used for retrying failed requests. If set any request failure will not be retried and will fail the job. |

## Authorization  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#authorization)

Make sure to [create an appropriate IAM policy](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html) to allow reading writing to the Kinesis Data Firehose delivery stream.

## Authentication  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#authentication)

Depending on your deployment you would choose a different Credentials Provider to allow access to Kinesis Data Firehose.
By default, the `AUTO` Credentials Provider is used.
If the access key ID and secret key are set in the deployment configuration, this results in using the `BASIC` provider.

A specific [AWSCredentialsProvider](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/index.html?com/amazonaws/auth/AWSCredentialsProvider.html) can be **optionally** set using the `aws.credentials.provider` setting.
Supported values are:

- `AUTO` \- Use the default AWS Credentials Provider chain that searches for credentials in the following order: `ENV_VARS`, `SYS_PROPS`, `WEB_IDENTITY_TOKEN`, `PROFILE`, and EC2/ECS credentials provider.
- `BASIC` \- Use access key ID and secret key supplied as configuration.
- `ENV_VAR` \- Use `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` environment variables.
- `SYS_PROP` \- Use Java system properties `aws.accessKeyId` and `aws.secretKey`.
- `PROFILE` \- Use an AWS credentials profile to create the AWS credentials.
- `ASSUME_ROLE` \- Create AWS credentials by assuming a role. The credentials for assuming the role must be supplied.
- `WEB_IDENTITY_TOKEN` \- Create AWS credentials by assuming a role using Web Identity Token.
- `CUSTOM` \- Provide a custom class that implements the interface `AWSCredentialsProvider` and has a constructor `MyCustomClass(java.util.Properties config)`. All connector properties will be passed down to this custom
credential provider class via the constructor.

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#data-type-mapping)

Kinesis Data Firehose stores records as Base64-encoded binary data objects, so it doesn’t have a notion of internal record structure.
Instead, Kinesis Data Firehose records are deserialized and serialized by formats, e.g. ‘avro’, ‘csv’, or ‘json’.
To determine the data type of the messages in your Kinesis Data Firehose backed tables, pick a suitable Flink format with the `format` keyword.
Please refer to the [Formats](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/formats/overview/) pages for more details.

## Notice  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/table/firehose/\#notice)

The current implementation for the Kinesis Data Firehose SQL connector only supports Kinesis Data Firehose backed sinks and doesn’t provide an implementation for source queries.
Queries similar to:

```sql
SELECT * FROM FirehoseTable;
```

should result in an error similar to

```
Connector firehose can only be used as a sink. It cannot be used as a source.
```