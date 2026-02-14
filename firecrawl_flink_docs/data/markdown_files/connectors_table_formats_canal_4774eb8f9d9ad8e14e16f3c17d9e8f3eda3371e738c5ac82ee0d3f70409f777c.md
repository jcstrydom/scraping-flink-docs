> This documentation is for an out-of-date version of Apache Flink. We recommend you use the latest [stable version](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/formats/canal/).

# Canal Format  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-format)

Changelog-Data-Capture FormatFormat: Serialization SchemaFormat: Deserialization Schema

[Canal](https://github.com/alibaba/canal/wiki) is a CDC (Changelog Data Capture) tool that can stream changes in real-time from MySQL into other systems. Canal provides a unified format schema for changelog and supports to serialize messages using JSON and [protobuf](https://developers.google.com/protocol-buffers) (protobuf is the default format for Canal).

Flink supports to interpret Canal JSON messages as INSERT/UPDATE/DELETE messages into Flink SQL system. This is useful in many cases to leverage this feature, such as

- synchronizing incremental data from databases to other systems
- auditing logs
- real-time materialized views on databases
- temporal join changing history of a database table and so on.

Flink also supports to encode the INSERT/UPDATE/DELETE messages in Flink SQL as Canal JSON messages, and emit to storage like Kafka.
However, currently Flink can’t combine UPDATE\_BEFORE and UPDATE\_AFTER into a single UPDATE message. Therefore, Flink encodes UPDATE\_BEFORE and UPDATE\_AFTER as DELETE and INSERT Canal messages.

_Note: Support for interpreting Canal protobuf messages is on the roadmap._

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#dependencies)

In order to use the Canal format the following
dependencies are required for both projects using a build automation tool (such as Maven or SBT)
and SQL Client with SQL JAR bundles.

| Maven dependency | SQL Client |
| --- | --- |
| ```xml<br><dependency><br>  <groupId>org.apache.flink</groupId><br>  <artifactId>flink-json</artifactId><br>  <version>1.20.3</version><br></dependency><br>```<br>Copied to clipboard! | Built-in |

_Note: please refer to [Canal documentation](https://github.com/alibaba/canal/wiki) about how to deploy Canal to synchronize changelog to message queues._

## How to use Canal format  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#how-to-use-canal-format)

Canal provides a unified format for changelog, here is a simple example for an update operation captured from a MySQL `products` table:

```json
{
  "data": [\
    {\
      "id": "111",\
      "name": "scooter",\
      "description": "Big 2-wheel scooter",\
      "weight": "5.18"\
    }\
  ],
  "database": "inventory",
  "es": 1589373560000,
  "id": 9,
  "isDdl": false,
  "mysqlType": {
    "id": "INTEGER",
    "name": "VARCHAR(255)",
    "description": "VARCHAR(512)",
    "weight": "FLOAT"
  },
  "old": [\
    {\
      "weight": "5.15"\
    }\
  ],
  "pkNames": [\
    "id"\
  ],
  "sql": "",
  "sqlType": {
    "id": 4,
    "name": 12,
    "description": 12,
    "weight": 7
  },
  "table": "products",
  "ts": 1589373560798,
  "type": "UPDATE"
}
```

_Note: please refer to [Canal documentation](https://github.com/alibaba/canal/wiki) about the meaning of each fields._

The MySQL `products` table has 4 columns (`id`, `name`, `description` and `weight`). The above JSON message is an update change event on the `products` table where the `weight` value of the row with `id = 111` is changed from `5.18` to `5.15`.
Assuming the messages have been synchronized to Kafka topic `products_binlog`, then we can use the following DDL to consume this topic and interpret the change events.

```sql
CREATE TABLE topic_products (
  -- schema is totally the same to the MySQL "products" table
  id BIGINT,
  name STRING,
  description STRING,
  weight DECIMAL(10, 2)
) WITH (
 'connector' = 'kafka',
 'topic' = 'products_binlog',
 'properties.bootstrap.servers' = 'localhost:9092',
 'properties.group.id' = 'testGroup',
 'format' = 'canal-json'  -- using canal-json as the format
)
```

After registering the topic as a Flink table, you can consume the Canal messages as a changelog source.

```sql
-- a real-time materialized view on the MySQL "products"
-- which calculates the latest average of weight for the same products
SELECT name, AVG(weight) FROM topic_products GROUP BY name;

-- synchronize all the data and incremental changes of MySQL "products" table to
-- Elasticsearch "products" index for future searching
INSERT INTO elasticsearch_products
SELECT * FROM topic_products;
```

## Available Metadata  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#available-metadata)

The following format metadata can be exposed as read-only (`VIRTUAL`) columns in a table definition.

> Format metadata fields are only available if the
> corresponding connector forwards format metadata. Currently, only the Kafka connector is able to expose
> metadata fields for its value format.

| Key | Data Type | Description |
| --- | --- | --- |
| `database` | `STRING NULL` | The originating database. Corresponds to the `database` field in the<br> Canal record if available. |
| `table` | `STRING NULL` | The originating database table. Corresponds to the `table` field in the<br> Canal record if available. |
| `sql-type` | `MAP<STRING, INT> NULL` | Map of various sql types. Corresponds to the `sqlType` field in the <br> Canal record if available. |
| `pk-names` | `ARRAY<STRING> NULL` | Array of primary key names. Corresponds to the `pkNames` field in the <br> Canal record if available. |
| `ingestion-timestamp` | `TIMESTAMP_LTZ(3) NULL` | The timestamp at which the connector processed the event. Corresponds to the `ts`<br> field in the Canal record. |

The following example shows how to access Canal metadata fields in Kafka:

```sql
CREATE TABLE KafkaTable (
  origin_database STRING METADATA FROM 'value.database' VIRTUAL,
  origin_table STRING METADATA FROM 'value.table' VIRTUAL,
  origin_sql_type MAP<STRING, INT> METADATA FROM 'value.sql-type' VIRTUAL,
  origin_pk_names ARRAY<STRING> METADATA FROM 'value.pk-names' VIRTUAL,
  origin_ts TIMESTAMP(3) METADATA FROM 'value.ingestion-timestamp' VIRTUAL,
  user_id BIGINT,
  item_id BIGINT,
  behavior STRING
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'value.format' = 'canal-json'
);
```

## Format Options  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#format-options)

| Option | Required | Default | Type | Description |
| --- | --- | --- | --- | --- |
| ##### format [Anchor link for: format](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#format) | required | (none) | String | Specify what format to use, here should be `'canal-json'`. |
| ##### canal-json.ignore-parse-errors [Anchor link for: canal json ignore parse errors](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-ignore-parse-errors) | optional | false | Boolean | Skip fields and rows with parse errors instead of failing.<br> Fields are set to null in case of errors. |
| ##### canal-json.timestamp-format.standard [Anchor link for: canal json timestamp format standard](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-timestamp-format-standard) | optional | `'SQL'` | String | Specify the input and output timestamp format. Currently supported values are `'SQL'` and `'ISO-8601'`:<br> <br>- Option `'SQL'` will parse input timestamp in "yyyy-MM-dd HH:mm:ss.s{precision}" format, e.g '2020-12-30 12:13:14.123' and output timestamp in the same format.<br>- Option `'ISO-8601'` will parse input timestamp in "yyyy-MM-ddTHH:mm:ss.s{precision}" format, e.g '2020-12-30T12:13:14.123' and output timestamp in the same format. |
| ##### canal-json.map-null-key.mode [Anchor link for: canal json map null key mode](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-map-null-key-mode) | optional | `'FAIL'` | String | Specify the handling mode when serializing null keys for map data. Currently supported values are `'FAIL'`, `'DROP'` and `'LITERAL'`:<br> <br>- Option `'FAIL'` will throw exception when encountering map value with null key.<br>- Option `'DROP'` will drop null key entries for map data.<br>- Option `'LITERAL'` will replace null key with string literal. The string literal is defined by `canal-json.map-null-key.literal` option. |
| ##### canal-json.map-null-key.literal [Anchor link for: canal json map null key literal](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-map-null-key-literal) | optional | 'null' | String | Specify string literal to replace null key when `'canal-json.map-null-key.mode'` is LITERAL. |
| ##### canal-json.encode.decimal-as-plain-number [Anchor link for: canal json encode decimal as plain number](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-encode-decimal-as-plain-number) | optional | false | Boolean | Encode all decimals as plain numbers instead of possible scientific notations. By default, decimals may be written using scientific notation. For example, `0.000000027` is encoded as `2.7E-8` by default, and will be written as `0.000000027` if set this option to true. |
| ##### canal-json.database.include [Anchor link for: canal json database include](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-database-include) | optional | (none) | String | An optional regular expression to only read the specific databases changelog rows by regular matching the "database" meta field in the Canal record. The pattern string is compatible with Java's [Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html). |
| ##### canal-json.table.include [Anchor link for: canal json table include](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#canal-json-table-include) | optional | (none) | String | An optional regular expression to only read the specific tables changelog rows by regular matching the "table" meta field in the Canal record. The pattern string is compatible with Java's [Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html). |

## Caveats  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#caveats)

### Duplicate change events  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#duplicate-change-events)

Under normal operating scenarios, the Canal application delivers every change event **exactly-once**. Flink works pretty well when consuming Canal produced events in this situation.
However, Canal application works in **at-least-once** delivery if any failover happens.
That means, in the abnormal situations, Canal may deliver duplicate change events to message queues and Flink will get the duplicate events.
This may cause Flink query to get wrong results or unexpected exceptions. Thus, it is recommended to set job configuration [`table.exec.source.cdc-events-duplicate`](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/config/#table-exec-source-cdc-events-duplicate) to `true` and define PRIMARY KEY on the source in this situation.
Framework will generate an additional stateful operator, and use the primary key to deduplicate the change events and produce a normalized changelog stream.

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/canal/\#data-type-mapping)

Currently, the Canal format uses JSON format for serialization and deserialization. Please refer to [JSON format documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/formats/json/#data-type-mapping) for more details about the data type mapping.