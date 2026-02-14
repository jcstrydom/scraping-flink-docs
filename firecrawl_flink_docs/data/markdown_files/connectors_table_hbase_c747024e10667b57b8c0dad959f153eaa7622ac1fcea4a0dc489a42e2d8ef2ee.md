# HBase SQL Connector  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#hbase-sql-connector)

Scan Source: BoundedLookup Source: Sync ModeSink: BatchSink: Streaming Upsert Mode

The HBase connector allows for reading from and writing to an HBase cluster. This document describes how to setup the HBase Connector to run SQL queries against HBase.

HBase always works in upsert mode for exchange changelog messages with the external system using a primary key defined on the DDL. The primary key must be defined on the HBase rowkey field (rowkey field must be declared). If the PRIMARY KEY clause is not declared, the HBase connector will take rowkey as the primary key by default.

## Dependencies  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#dependencies)

There is no connector (yet) available for Flink version 2.2.

The HBase connector is not part of the binary distribution.
See how to link with it for cluster execution [here](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/configuration/overview/).

## How to use HBase table  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#how-to-use-hbase-table)

All the column families in HBase table must be declared as ROW type, the field name maps to the column family name, and the nested field names map to the column qualifier names. There is no need to declare all the families and qualifiers in the schema, users can declare what’s used in the query. Except the ROW type fields, the single atomic type field (e.g. STRING, BIGINT) will be recognized as HBase rowkey. The rowkey field can be arbitrary name, but should be quoted using backticks if it is a reserved keyword.

```sql
-- register the HBase table 'mytable' in Flink SQL
CREATE TABLE hTable (
 rowkey INT,
 family1 ROW<q1 INT>,
 family2 ROW<q2 STRING, q3 BIGINT>,
 family3 ROW<q4 DOUBLE, q5 BOOLEAN, q6 STRING>,
 PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
 'connector' = 'hbase-2.2',
 'table-name' = 'mytable',
 'zookeeper.quorum' = 'localhost:2181'
);

-- use ROW(...) construction function construct column families and write data into the HBase table.
-- assuming the schema of "T" is [rowkey, f1q1, f2q2, f2q3, f3q4, f3q5, f3q6]
INSERT INTO hTable
SELECT rowkey, ROW(f1q1), ROW(f2q2, f2q3), ROW(f3q4, f3q5, f3q6) FROM T;

-- scan data from the HBase table
SELECT rowkey, family1, family3.q4, family3.q6 FROM hTable;

-- temporal join the HBase table as a dimension table
SELECT * FROM myTopic
LEFT JOIN hTable FOR SYSTEM_TIME AS OF myTopic.proctime
ON myTopic.key = hTable.rowkey;
```

## Available Metadata  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#available-metadata)

The following connector metadata can be accessed as metadata columns in a table definition.

The `R/W` column defines whether a metadata field is readable (`R`) and/or writable (`W`).
Read-only columns must be declared `VIRTUAL` to exclude them during an `INSERT INTO` operation.

| Key | Data Type | Description | R/W |
| --- | --- | --- | --- |
| `timestamp` | `TIMESTAMP_LTZ(3) NOT NULL` | Timestamp for the HBase mutation. | `W` |
| `ttl` | `BIGINT NOT NULL` | Time-to-live for the HBase mutation, in milliseconds. | `W` |

## Connector Options  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#connector-options)

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| ##### connector [Anchor link for: connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#connector) | required | no | (none) | String | Specify what connector to use, valid values are:<br> <br>- `hbase-2.2`: connect to HBase 2.2.x cluster |
| ##### table-name [Anchor link for: table name](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#table-name) | required | yes | (none) | String | The name of HBase table to connect. By default, the table is in 'default' namespace. To assign the table a specified namespace you need to use 'namespace:table'. |
| ##### zookeeper.quorum [Anchor link for: zookeeper quorum](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#zookeeper-quorum) | required | yes | (none) | String | The HBase Zookeeper quorum. |
| ##### zookeeper.znode.parent [Anchor link for: zookeeper znode parent](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#zookeeper-znode-parent) | optional | yes | /hbase | String | The root dir in Zookeeper for HBase cluster. |
| ##### null-string-literal [Anchor link for: null string literal](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#null-string-literal) | optional | yes | null | String | Representation for null values for string fields. HBase source and sink encodes/decodes empty bytes as null values for all types except string type. |
| ##### sink.buffer-flush.max-size [Anchor link for: sink buffer flush max size](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#sink-buffer-flush-max-size) | optional | yes | 2mb | MemorySize | Writing option, maximum size in memory of buffered rows for each writing request.<br> This can improve performance for writing data to HBase database, but may increase the latency.<br> Can be set to `'0'` to disable it. |
| ##### sink.buffer-flush.max-rows [Anchor link for: sink buffer flush max rows](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#sink-buffer-flush-max-rows) | optional | yes | 1000 | Integer | Writing option, maximum number of rows to buffer for each writing request.<br> This can improve performance for writing data to HBase database, but may increase the latency.<br> Can be set to `'0'` to disable it. |
| ##### sink.buffer-flush.interval [Anchor link for: sink buffer flush interval](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#sink-buffer-flush-interval) | optional | yes | 1s | Duration | Writing option, the interval to flush any buffered rows.<br> This can improve performance for writing data to HBase database, but may increase the latency.<br> Can be set to `'0'` to disable it. Note, both `'sink.buffer-flush.max-size'` and `'sink.buffer-flush.max-rows'`<br> can be set to `'0'` with the flush interval set allowing for complete async processing of buffered actions. |
| ##### sink.ignore-null-value [Anchor link for: sink ignore null value](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#sink-ignore-null-value) | optional | yes | false | Boolean | Writing option, whether ignore null value or not. |
| ##### sink.parallelism [Anchor link for: sink parallelism](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#sink-parallelism) | optional | no | (none) | Integer | Defines the parallelism of the HBase sink operator. By default, the parallelism is determined by the framework using the same parallelism of the upstream chained operator. |
| ##### lookup.async [Anchor link for: lookup async](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-async) | optional | no | false | Boolean | Whether async lookup are enabled. If true, the lookup will be async. Note, async only supports hbase-2.2 connector. |
| ##### lookup.cache [Anchor link for: lookup cache](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-cache) | optional | yes | NONE | Enum<br>Possible values: NONE, PARTIAL | The cache strategy for the lookup table. Currently supports NONE (no caching) and PARTIAL (caching entries on lookup operation in external database). |
| ##### lookup.partial-cache.max-rows [Anchor link for: lookup partial cache max rows](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-partial-cache-max-rows) | optional | yes | (none) | Long | The max number of rows of lookup cache, over this value, the oldest rows will be expired. <br> "lookup.cache" must be set to "PARTIAL" to use this option. |
| ##### lookup.partial-cache.expire-after-write [Anchor link for: lookup partial cache expire after write](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-partial-cache-expire-after-write) | optional | yes | (none) | Duration | The max time to live for each rows in lookup cache after writing into the cache<br> "lookup.cache" must be set to "PARTIAL" to use this option. |
| ##### lookup.partial-cache.expire-after-access [Anchor link for: lookup partial cache expire after access](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-partial-cache-expire-after-access) | optional | yes | (none) | Duration | The max time to live for each rows in lookup cache after accessing the entry in the cache.<br> "lookup.cache" must be set to "PARTIAL" to use this option. |
| ##### lookup.partial-cache.caching-missing-key [Anchor link for: lookup partial cache caching missing key](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-partial-cache-caching-missing-key) | optional | yes | true | Boolean | Whether to store an empty value into the cache if the lookup key doesn't match any rows in the table. <br> "lookup.cache" must be set to "PARTIAL" to use this option. |
| ##### lookup.max-retries [Anchor link for: lookup max retries](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-max-retries) | optional | yes | 3 | Integer | The max retry times if lookup database failed. |
| ##### properties.\* [Anchor link for: properties](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#properties) | optional | no | (none) | String | This can set and pass arbitrary HBase configurations. Suffix names must match the configuration key defined in [HBase Configuration documentation](http://hbase.apache.org/2.3/book.html#hbase_default_configurations). Flink will remove the "properties." key prefix and pass the transformed key and values to the underlying HBaseClient. For example, you can add a kerberos authentication parameter `'properties.hbase.security.authentication' = 'kerberos'`. |

### Deprecated Options  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#deprecated-options)

These deprecated options has been replaced by new options listed above and will be removed eventually. Please consider using new options first.

| Option | Required | Forwarded | Default | Type | Description |
| --- | --- | --- | --- | --- | --- |
| ##### lookup.cache.max-rows [Anchor link for: lookup cache max rows](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-cache-max-rows) | optional | yes | (none) | Integer | Please set "lookup.cache" = "PARTIAL" and use "lookup.partial-cache.max-rows" instead. |
| ##### lookup.cache.ttl [Anchor link for: lookup cache ttl](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#lookup-cache-ttl) | optional | yes | (none) | Duration | Please set "lookup.cache" = "PARTIAL" and use "lookup.partial-cache.expire-after-write" instead. |

## Data Type Mapping  [\#](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/hbase/\#data-type-mapping)

HBase stores all data as byte arrays. The data needs to be serialized and deserialized during read and write operation

When serializing and de-serializing, Flink HBase connector uses utility class `org.apache.hadoop.hbase.util.Bytes` provided by HBase (Hadoop) to convert Flink Data Types to and from byte arrays.

Flink HBase connector encodes `null` values to empty bytes, and decode empty bytes to `null` values for all data types except string type. For string type, the null literal is determined by `null-string-literal` option.

The data type mappings are as follows:

|
|

| Flink SQL type | HBase conversion |
| --- | --- |
| `CHAR / VARCHAR / STRING` | ```java<br>byte[] toBytes(String s)<br>String toString(byte[] b)<br>``` |
| `BOOLEAN` | ```java<br>byte[] toBytes(boolean b)<br>boolean toBoolean(byte[] b)<br>``` |
| `BINARY / VARBINARY` | Returns `byte[]` as is. |
| `DECIMAL` | ```java<br>byte[] toBytes(BigDecimal v)<br>BigDecimal toBigDecimal(byte[] b)<br>``` |
| `TINYINT` | ```java<br>new byte[] { val }<br>bytes[0] // returns first and only byte from bytes<br>``` |
| `SMALLINT` | ```java<br>byte[] toBytes(short val)<br>short toShort(byte[] bytes)<br>``` |
| `INT` | ```java<br>byte[] toBytes(int val)<br>int toInt(byte[] bytes)<br>``` |
| `BIGINT` | ```java<br>byte[] toBytes(long val)<br>long toLong(byte[] bytes)<br>``` |
| `FLOAT` | ```java<br>byte[] toBytes(float val)<br>float toFloat(byte[] bytes)<br>``` |
| `DOUBLE` | ```java<br>byte[] toBytes(double val)<br>double toDouble(byte[] bytes)<br>``` |
| `DATE` | Stores the number of days since epoch as int value. |
| `TIME` | Stores the number of milliseconds of the day as int value. |
| `TIMESTAMP` | Stores the milliseconds since epoch as long value. |
| `ARRAY` | Not supported |
| `MAP / MULTISET` | Not supported |
| `ROW` | Not supported |