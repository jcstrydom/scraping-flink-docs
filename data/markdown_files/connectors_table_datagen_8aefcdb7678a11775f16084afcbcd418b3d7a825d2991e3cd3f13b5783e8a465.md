> This documentation is for an out-of-date version of Apache Flink. We recommend you use the latest [stable version](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/datagen/).

# DataGen SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#datagen-sql-connector)

Scan Source: BoundedScan Source: UnBounded

The DataGen connector allows for creating tables based on in-memory data generation.
This is useful when developing queries locally without access to external systems such as Kafka.
Tables can include [Computed Column syntax](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/sql/create/#create-table) which allows for flexible record generation.

The DataGen connector is built-in, no additional dependencies are required.

## Usage  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#usage)

By default, a DataGen table will create an unbounded number of rows with a random value for each column.
Additionally, a total number of rows can be specified, resulting in a bounded table.

The DataGen connector can generate data that conforms to its defined schema, It should be noted that it handles length-constrained fields as follows:

- For fixed-length data types (char/binary), the field length can only be defined by the schema,
and does not support customization.
- For variable-length data types (varchar/varbinary), the field length is initially defined by the schema,
and the customized length cannot be greater than the schema definition.
- For super-long fields (string/bytes), the default length is 100, but can be set to a length less than 2^31.

There also exists a sequence generator, where users specify a sequence of start and end values.
If any column in a table is a sequence type, the table will be bounded and end with the first sequence completes.

Time types are always the local machines current system time.

```sql
CREATE TABLE Orders (
    order_number BIGINT,
    price        DECIMAL(32,2),
    buyer        ROW<first_name STRING, last_name STRING>,
    order_time   TIMESTAMP(3)
) WITH (
  'connector' = 'datagen'
)
```

Often, the data generator connector is used in conjunction with the `LIKE` clause to mock out physical tables.

```sql
CREATE TABLE Orders (
    order_number BIGINT,
    price        DECIMAL(32,2),
    buyer        ROW<first_name STRING, last_name STRING>,
    order_time   TIMESTAMP(3)
) WITH (...)

-- create a bounded mock table
CREATE TEMPORARY TABLE GenOrders
WITH (
    'connector' = 'datagen',
    'number-of-rows' = '10'
)
LIKE Orders (EXCLUDING ALL)
```

Furthermore, for variable sized types, varchar/string/varbinary/bytes, you can specify whether to enable variable-length data generation.

```sql
CREATE TABLE Orders (
    order_number BIGINT,
    price        DECIMAL(32,2),
    buyer        ROW<first_name STRING, last_name STRING>,
    order_time   TIMESTAMP(3),
    seller       VARCHAR(150)
) WITH (
  'connector' = 'datagen',
  'fields.seller.var-len' = 'true'
)
```

## Types  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#types)

| Type | Supported Generators | Notes |
| --- | --- | --- |
| BOOLEAN | random |  |
| CHAR | random / sequence |  |
| VARCHAR | random / sequence |  |
| BINARY | random / sequence |  |
| VARBINARY | random / sequence |  |
| STRING | random / sequence |  |
| DECIMAL | random / sequence |  |
| TINYINT | random / sequence |  |
| SMALLINT | random / sequence |  |
| INT | random / sequence |  |
| BIGINT | random / sequence |  |
| FLOAT | random / sequence |  |
| DOUBLE | random / sequence |  |
| DATE | random | Always resolves to the current date of the local machine. |
| TIME | random | Always resolves to the current time of the local machine. |
| TIMESTAMP | random | Resolves a past timestamp relative to the current timestamp of the local machine.<br> The max past can be specified by the 'max-past' option. |
| TIMESTAMP\_LTZ | random | Resolves a past timestamp relative to the current timestamp of the local machine.<br> The max past can be specified by the 'max-past' option. |
| INTERVAL YEAR TO MONTH | random |  |
| INTERVAL DAY TO MONTH | random |  |
| ROW | random | Generates a row with random subfields. |
| ARRAY | random | Generates an array with random entries. |
| MAP | random | Generates a map with random entries. |
| MULTISET | random | Generates a multiset with random entries. |

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#connector-options)

| Option | Required | Default | Type | Description |
| --- | --- | --- | --- | --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#connector) | required | (none) | String | Specify what connector to use, here should be 'datagen'. |
| ##### rows-per-second [Anchor link for: rows per second](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#rows-per-second) | optional | 10000 | Long | Rows per second to control the emit rate. |
| ##### number-of-rows [Anchor link for: number of rows](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#number-of-rows) | optional | (none) | Long | The total number of rows to emit. By default, the table is unbounded. |
| ##### scan.parallelism [Anchor link for: scan parallelism](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#scan-parallelism) | optional | (none) | Integer | Defines the parallelism of the source. If not set, the global default parallelism is used. |
| ##### fields.\#.kind [Anchor link for: fields kind](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-kind) | optional | random | String | Generator of this '#' field. Can be 'sequence' or 'random'. |
| ##### fields.\#.min [Anchor link for: fields min](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-min) | optional | (Minimum value of type) | (Type of field) | Minimum value of random generator, work for numeric types. |
| ##### fields.\#.max [Anchor link for: fields max](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-max) | optional | (Maximum value of type) | (Type of field) | Maximum value of random generator, work for numeric types. |
| ##### fields.\#.max-past [Anchor link for: fields max past](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-max-past) | optional | 0 | Duration | Maximum past of timestamp random generator, only works for timestamp types. |
| ##### fields.\#.length [Anchor link for: fields length](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-length) | optional | 100 | Integer | Size or length of the collection for generating varchar/varbinary/string/bytes/array/map/multiset types. <br> Please notice that for variable-length fields (varchar/varbinary), the default length is defined by the schema and cannot be set to a length greater than it.<br> for super-long fields (string/bytes), the default length is 100 and can be set to a length less than 2^31.<br> for constructed fields (array/map/multiset), the default number of elements is 3 and can be customized. |
| ##### fields.\#.var-len [Anchor link for: fields var len](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-var-len) | optional | false | Boolean | Whether to generate a variable-length data, please notice that it should only be used for variable-length types (varchar, string, varbinary, bytes). |
| ##### fields.\#.start [Anchor link for: fields start](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-start) | optional | (none) | (Type of field) | Start value of sequence generator. |
| ##### fields.\#.end [Anchor link for: fields end](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-end) | optional | (none) | (Type of field) | End value of sequence generator. |
| ##### fields.\#.null-rate [Anchor link for: fields null rate](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/datagen/\#fields-null-rate) | optional | (none) | (Type of field) | The proportion of null values. |