Navigate the docs…

# Adapters

## Schema adapters [Permalink](https://calcite.apache.org/docs/adapter.html\#schema-adapters "Permalink")

A schema adapter allows Calcite to read particular kind of data,
presenting the data as tables within a schema.

- [Arrow adapter](https://calcite.apache.org/docs/arrow_adapter.html) ( [calcite-arrow](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/arrow/package-summary.html))
- [Cassandra adapter](https://calcite.apache.org/docs/cassandra_adapter.html) ( [calcite-cassandra](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/cassandra/package-summary.html))
- CSV adapter ( [example/csv](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/csv/package-summary.html))
- [Druid adapter](https://calcite.apache.org/docs/druid_adapter.html) ( [calcite-druid](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/druid/package-summary.html))
- [Elasticsearch adapter](https://calcite.apache.org/docs/elasticsearch_adapter.html)
( [calcite-elasticsearch](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/elasticsearch/package-summary.html))
- [File adapter](https://calcite.apache.org/docs/file_adapter.html) ( [calcite-file](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/file/package-summary.html))
- [Geode adapter](https://calcite.apache.org/docs/geode_adapter.html) ( [calcite-geode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/geode/rel/package-summary.html))
- [InnoDB adapter](https://calcite.apache.org/docs/innodb_adapter.html) ( [calcite-innodb](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/innodb/package-summary.html))
- JDBC adapter (part of [calcite-core](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/jdbc/package-summary.html))
- MongoDB adapter ( [calcite-mongodb](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/mongodb/package-summary.html))
- [OS adapter](https://calcite.apache.org/docs/os_adapter.html) ( [calcite-os](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/os/package-summary.html))
- [Pig adapter](https://calcite.apache.org/docs/pig_adapter.html) ( [calcite-pig](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/pig/package-summary.html))
- [Redis adapter](https://calcite.apache.org/docs/redis_adapter.html) ( [calcite-redis](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/redis/package-summary.html))
- Solr cloud adapter ( [solr-sql](https://github.com/bluejoe2008/solr-sql))
- Spark adapter ( [calcite-spark](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/spark/package-summary.html))
- Splunk adapter ( [calcite-splunk](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/splunk/package-summary.html))
- Eclipse Memory Analyzer (MAT) adapter ( [mat-calcite-plugin](https://github.com/vlsi/mat-calcite-plugin))
- [Apache Kafka adapter](https://calcite.apache.org/docs/kafka_adapter.html)

### Other language interfaces [Permalink](https://calcite.apache.org/docs/adapter.html\#other-language-interfaces "Permalink")

- Piglet ( [calcite-piglet](https://calcite.apache.org/javadocAggregate/org/apache/calcite/piglet/package-summary.html)) runs queries in a subset of [Pig Latin](https://pig.apache.org/docs/latest/basic.html)

## Engines [Permalink](https://calcite.apache.org/docs/adapter.html\#engines "Permalink")

Many projects and products use Apache Calcite for SQL parsing,
query optimization, data virtualization/federation,
and materialized view rewrite. Some of them are listed on the
[“powered by Calcite”](https://calcite.apache.org/docs/powered_by.html)
page.

## Drivers [Permalink](https://calcite.apache.org/docs/adapter.html\#drivers "Permalink")

A driver allows you to connect to Calcite from your application.

- [JDBC driver](https://calcite.apache.org/javadocAggregate/org/apache/calcite/jdbc/package-summary.html)

The JDBC driver is powered by
[Avatica](https://calcite.apache.org/avatica/docs/).
Connections can be local or remote (JSON over HTTP or Protobuf over HTTP).

The basic form of the JDBC connect string is

jdbc:calcite:property=value;property2=value2

where `property`, `property2` are properties as described below.
(Connect strings are compliant with OLE DB Connect String syntax,
as implemented by Avatica’s
[ConnectStringParser](https://calcite.apache.org/avatica/javadocAggregate/org/apache/calcite/avatica/ConnectStringParser.html).)

## JDBC connect string parameters [Permalink](https://calcite.apache.org/docs/adapter.html\#jdbc-connect-string-parameters "Permalink")

| Property | Description |
| --- | --- |
| [approximateDecimal](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#APPROXIMATE_DECIMAL) | Whether approximate results from aggregate functions on `DECIMAL` types are acceptable. |
| [approximateDistinctCount](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#APPROXIMATE_DISTINCT_COUNT) | Whether approximate results from `COUNT(DISTINCT ...)` aggregate functions are acceptable. |
| [approximateTopN](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#APPROXIMATE_TOP_N) | Whether approximate results from “Top N” queries (`ORDER BY aggFun() DESC LIMIT n`) are acceptable. |
| [caseSensitive](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#CASE_SENSITIVE) | Whether identifiers are matched case-sensitively. If not specified, value from `lex` is used. |
| [conformance](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#CONFORMANCE) | SQL conformance level. Values: DEFAULT (the default, similar to PRAGMATIC\_2003), LENIENT, MYSQL\_5, ORACLE\_10, ORACLE\_12, PRAGMATIC\_99, PRAGMATIC\_2003, STRICT\_92, STRICT\_99, STRICT\_2003, SQL\_SERVER\_2008. |
| [createMaterializations](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#CREATE_MATERIALIZATIONS) | Whether Calcite should create materializations. Default false. |
| [defaultNullCollation](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#DEFAULT_NULL_COLLATION) | How NULL values should be sorted if neither NULLS FIRST nor NULLS LAST are specified in a query. The default, HIGH, sorts NULL values the same as Oracle. |
| [druidFetch](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#DRUID_FETCH) | How many rows the Druid adapter should fetch at a time when executing SELECT queries. |
| [forceDecorrelate](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#FORCE_DECORRELATE) | Whether the planner should try de-correlating as much as possible. Default true. |
| [fun](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#FUN) | Collection of built-in functions and operators. Valid values are “standard” (the default), “oracle”, “spatial”, and may be combined using commas, for example “oracle,spatial”. |
| [lex](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#LEX) | Lexical policy. Values are BIG\_QUERY, JAVA, MYSQL, MYSQL\_ANSI, ORACLE (default), SQL\_SERVER. |
| [materializationsEnabled](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#MATERIALIZATIONS_ENABLED) | Whether Calcite should use materializations. Default false. |
| [model](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#MODEL) | URI of the JSON/YAML model file or inline like `inline:{...}` for JSON and `inline:...` for YAML. |
| [parserFactory](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#PARSER_FACTORY) | Parser factory. The name of a class that implements [`interface SqlParserImplFactory`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/parser/SqlParserImplFactory.html) and has a public default constructor or an `INSTANCE` constant. |
| [quoting](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#QUOTING) | How identifiers are quoted. Values are DOUBLE\_QUOTE, BACK\_TICK, BACK\_TICK\_BACKSLASH, BRACKET. If not specified, value from `lex` is used. |
| [quotedCasing](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#QUOTED_CASING) | How identifiers are stored if they are quoted. Values are UNCHANGED, TO\_UPPER, TO\_LOWER. If not specified, value from `lex` is used. |
| [schema](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#SCHEMA) | Name of initial schema. |
| [schemaFactory](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#SCHEMA_FACTORY) | Schema factory. The name of a class that implements [`interface SchemaFactory`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/SchemaFactory.html) and has a public default constructor or an `INSTANCE` constant. Ignored if `model` is specified. |
| [schemaType](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#SCHEMA_TYPE) | Schema type. Value must be “MAP” (the default), “JDBC”, or “CUSTOM” (implicit if `schemaFactory` is specified). Ignored if `model` is specified. |
| [spark](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#SPARK) | Specifies whether Spark should be used as the engine for processing that cannot be pushed to the source system. If false (the default), Calcite generates code that implements the Enumerable interface. |
| [timeZone](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#TIME_ZONE) | Time zone, for example “gmt-3”. Default is the JVM’s time zone. |
| [typeSystem](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#TYPE_SYSTEM) | Type system. The name of a class that implements [`interface RelDataTypeSystem`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/type/RelDataTypeSystem.html) and has a public default constructor or an `INSTANCE` constant. |
| [unquotedCasing](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#UNQUOTED_CASING) | How identifiers are stored if they are not quoted. Values are UNCHANGED, TO\_UPPER, TO\_LOWER. If not specified, value from `lex` is used. |
| [typeCoercion](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#TYPE_COERCION) | Whether to make implicit type coercion when type mismatch during sql node validation, default is true. |

To make a connection to a single schema based on a built-in schema type, you don’t need to specify
a model. For example,

```text
jdbc:calcite:schemaType=JDBC; schema.jdbcUser=SCOTT; schema.jdbcPassword=TIGER; schema.jdbcUrl=jdbc:hsqldb:res:foodmart
```

creates a connection with a schema mapped via the JDBC schema adapter to the foodmart database.

Similarly, you can connect to a single schema based on a user-defined schema adapter.
For example,

```text
jdbc:calcite:schemaFactory=org.apache.calcite.adapter.cassandra.CassandraSchemaFactory; schema.host=localhost; schema.keyspace=twissandra
```

makes a connection to the Cassandra adapter, equivalent to writing the following model file:

```json
{
  "version": "1.0",
  "defaultSchema": "foodmart",
  "schemas": [\
    {\
      type: 'custom',\
      name: 'twissandra',\
      factory: 'org.apache.calcite.adapter.cassandra.CassandraSchemaFactory',\
      operand: {\
        host: 'localhost',\
        keyspace: 'twissandra'\
      }\
    }\
  ]
}
```

Note how each key in the `operand` section appears with a `schema.` prefix in the connect string.

## Server [Permalink](https://calcite.apache.org/docs/adapter.html\#server "Permalink")

Calcite’s core module (`calcite-core`) supports SQL queries (`SELECT`) and DML
operations (`INSERT`, `UPDATE`, `DELETE`, `MERGE`)
but does not support DDL operations such as `CREATE SCHEMA` or `CREATE TABLE`.
As we shall see, DDL complicates the state model of the repository and makes
the parser more difficult to extend, so we left DDL out of the core.

The server module (`calcite-server`) adds DDL support to Calcite.
It extends the SQL parser,
[using the same mechanism used by sub-projects](https://calcite.apache.org/docs/adapter.html#extending-the-parser),
adding some DDL commands:

- `CREATE` and `DROP SCHEMA`
- `CREATE` and `DROP FOREIGN SCHEMA`
- `CREATE` and `DROP TABLE` (including `CREATE TABLE ... AS SELECT`)
- `CREATE` and `DROP MATERIALIZED VIEW`
- `CREATE` and `DROP VIEW`
- `CREATE` and `DROP FUNCTION`
- `CREATE` and `DROP TYPE`

Commands are described in the [SQL reference](https://calcite.apache.org/docs/reference.html#ddl-extensions).

To enable, include `calcite-server.jar` in your class path, and add
`parserFactory=org.apache.calcite.server.ServerDdlExecutor#PARSER_FACTORY`
to the JDBC connect string (see connect string property
[parserFactory](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#PARSER_FACTORY)).
Here is an example using the `sqlline` shell.

```sql
$ ./sqlline
sqlline version 1.3.0
> !connect jdbc:calcite:parserFactory=org.apache.calcite.server.ServerDdlExecutor#PARSER_FACTORY sa ""
> CREATE TABLE t (i INTEGER, j VARCHAR(10));
No rows affected (0.293 seconds)
> INSERT INTO t VALUES (1, 'a'), (2, 'bc');
2 rows affected (0.873 seconds)
> CREATE VIEW v AS SELECT * FROM t WHERE i > 1;
No rows affected (0.072 seconds)
> SELECT count(*) FROM v;
+---------------------+
|       EXPR$0        |
+---------------------+
| 1                   |
+---------------------+
1 row selected (0.148 seconds)
> !quit
```

The `calcite-server` module is optional.
One of its goals is to showcase Calcite’s capabilities
(for example materialized views, foreign tables and generated columns) using
concise examples that you can try from the SQL command line.
All of the capabilities used by `calcite-server` are available via APIs in
`calcite-core`.

If you are the author of a sub-project, it is unlikely that your syntax
extensions match those in `calcite-server`, so we recommend that you add your
SQL syntax extensions by [extending the core parser](https://calcite.apache.org/docs/adapter.html#extending-the-parser);
if you want DDL commands, you may be able to copy-paste from `calcite-server`
into your project.

At present, the repository is not persisted. As you execute DDL commands, you
are modifying an in-memory repository by adding and removing objects
reachable from a root
[`Schema`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/Schema.html).
All commands within the same SQL session will see those objects.
You can create the same objects in a future session by executing the same
script of SQL commands.

Calcite could also act as a data virtualization or federation server:
Calcite manages data in multiple foreign schemas, but to a client the data
all seems to be in the same place. Calcite chooses where processing should
occur, and whether to create copies of data for efficiency.
The `calcite-server` module is a step towards that goal; an
industry-strength solution would require further on packaging (to make Calcite
runnable as a service), repository persistence, authorization and security.

## Extensibility [Permalink](https://calcite.apache.org/docs/adapter.html\#extensibility "Permalink")

There are many other APIs that allow you to extend Calcite’s capabilities.

In this section, we briefly describe those APIs, to give you an idea of what is
possible. To fully use these APIs you will need to read other documentation
such as the javadoc for the interfaces, and possibly seek out the tests that
we have written for them.

### Functions and operators [Permalink](https://calcite.apache.org/docs/adapter.html\#functions-and-operators "Permalink")

There are several ways to add operators or functions to Calcite.
We’ll describe the simplest (and least powerful) first.

_User-defined functions_ are the simplest (but least powerful).
They are straightforward to write (you just write a Java class and register it
in your schema) but do not offer much flexibility in the number and type of
arguments, resolving overloaded functions, or deriving the return type.

If you want that flexibility, you probably need to write a
_user-defined operator_
(see [`interface SqlOperator`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/SqlOperator.html)).

If your operator does not adhere to standard SQL function syntax,
“`f(arg1, arg2, ...)`”, then you need to
[extend the parser](https://calcite.apache.org/docs/adapter.html#extending-the-parser).

There are many good examples in the tests:
[`class UdfTest`](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/test/UdfTest.java)
tests user-defined functions and user-defined aggregate functions.

### Aggregate functions [Permalink](https://calcite.apache.org/docs/adapter.html\#aggregate-functions "Permalink")

_User-defined aggregate functions_ are similar to user-defined functions,
but each function has several corresponding Java methods, one for each
stage in the life-cycle of an aggregate:

- `init` creates an accumulator;
- `add` adds one row’s value to an accumulator;
- `merge` combines two accumulators into one;
- `result` finalizes an accumulator and converts it to a result.

For example, the methods (in pseudo-code) for `SUM(int)` are as follows:

```java
struct Accumulator {
  final int sum;
}
Accumulator init() {
  return new Accumulator(0);
}
Accumulator add(Accumulator a, int x) {
  return new Accumulator(a.sum + x);
}
Accumulator merge(Accumulator a, Accumulator a2) {
  return new Accumulator(a.sum + a2.sum);
}
int result(Accumulator a) {
  return a.sum;
}
```

Here is the sequence of calls to compute the sum of two rows with column values 4 and 7:

```java
a = init()    # a = {0}
a = add(a, 4) # a = {4}
a = add(a, 7) # a = {11}
return result(a) # returns 11
```

### Window functions [Permalink](https://calcite.apache.org/docs/adapter.html\#window-functions "Permalink")

A window function is similar to an aggregate function but it is applied to a set
of rows gathered by an `OVER` clause rather than by a `GROUP BY` clause.
Every aggregate function can be used as a window function, but there are some
key differences. The rows seen by a window function may be ordered, and
window functions that rely upon order (`RANK`, for example) cannot be used as
aggregate functions.

Another difference is that windows are _non-disjoint_: a particular row can
appear in more than one window. For example, 9:37 appears in both the
9:00-10:00 hour and also the 9:15-9:45 hour.

Window functions are computed incrementally: when the clock ticks from
10:14 to 10:15, two rows might enter the window and three rows leave.
For this, window functions have an extra life-cycle operation:

- `remove` removes a value from an accumulator.

It pseudo-code for `SUM(int)` would be:

```java
Accumulator remove(Accumulator a, int x) {
  return new Accumulator(a.sum - x);
}
```

Here is the sequence of calls to compute the moving sum,
over the previous 2 rows, of 4 rows with values 4, 7, 2 and 3:

```java
a = init()       # a = {0}
a = add(a, 4)    # a = {4}
emit result(a)   # emits 4
a = add(a, 7)    # a = {11}
emit result(a)   # emits 11
a = remove(a, 4) # a = {7}
a = add(a, 2)    # a = {9}
emit result(a)   # emits 9
a = remove(a, 7) # a = {2}
a = add(a, 3)    # a = {5}
emit result(a)   # emits 5
```

### Grouped window functions [Permalink](https://calcite.apache.org/docs/adapter.html\#grouped-window-functions "Permalink")

Grouped window functions are functions that operate the `GROUP BY` clause
to gather together records into sets. The built-in grouped window functions
are `HOP`, `TUMBLE` and `SESSION`.
You can define additional functions by implementing
[`interface SqlGroupedWindowFunction`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/SqlGroupedWindowFunction.html).

### Table functions and table macros [Permalink](https://calcite.apache.org/docs/adapter.html\#table-functions-and-table-macros "Permalink")

_User-defined table functions_
are defined in a similar way to regular “scalar” user-defined functions,
but are used in the `FROM` clause of a query. The following query uses a table
function called `Ramp`:

```sql
SELECT * FROM TABLE(Ramp(3, 4))
```

_User-defined table macros_ use the same SQL syntax as table functions,
but are defined differently. Rather than generating data, they generate a
relational expression.
Table macros are invoked during query preparation and the relational expression
they produce can then be optimized.
(Calcite’s implementation of views uses table macros.)

[`class TableFunctionTest`](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/test/TableFunctionTest.java)
tests table functions and contains several useful examples.

### Extending the parser [Permalink](https://calcite.apache.org/docs/adapter.html\#extending-the-parser "Permalink")

Suppose you need to extend Calcite’s SQL grammar in a way that will be
compatible with future changes to the grammar. Making a copy of the grammar file
`Parser.jj` in your project would be foolish, because the grammar is edited
quite frequently.

Fortunately, `Parser.jj` is actually an
[Apache FreeMarker](https://freemarker.apache.org/)
template that contains variables that can be substituted.
The parser in `calcite-core` instantiates the template with default values of
the variables, typically empty, but you can override.
If your project would like a different parser, you can provide your
own `config.fmpp` and `parserImpls.ftl` files and therefore generate an
extended parser.

The `calcite-server` module, which was created in
\[ [CALCITE-707](https://issues.apache.org/jira/browse/CALCITE-707)\] and
adds DDL statements such as `CREATE TABLE`, is an example that you could follow.
Also see
[`class ExtensionSqlParserTest`](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/sql/parser/parserextensiontesting/ExtensionSqlParserTest.java).

### Customizing SQL dialect accepted and generated [Permalink](https://calcite.apache.org/docs/adapter.html\#customizing-sql-dialect-accepted-and-generated "Permalink")

To customize what SQL extensions the parser should accept, implement
[`interface SqlConformance`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html)
or use one of the built-in values in
[`enum SqlConformanceEnum`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformanceEnum.html).

To control how SQL is generated for an external database (usually via the JDBC
adapter), use
[`class SqlDialect`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/SqlDialect.html).
The dialect also describes the engine’s capabilities, such as whether it
supports `OFFSET` and `FETCH` clauses.

### Defining a custom schema [Permalink](https://calcite.apache.org/docs/adapter.html\#defining-a-custom-schema "Permalink")

To define a custom schema, you need to implement
[`interface SchemaFactory`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/SchemaFactory.html).

During query preparation, Calcite will call this interface to find out
what tables and sub-schemas your schema contains. When a table in your schema
is referenced in a query, Calcite will ask your schema to create an instance of
[`interface Table`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/Table.html).

That table will be wrapped in a
[`TableScan`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableScan.html)
and will undergo the query optimization process.

### Reflective schema [Permalink](https://calcite.apache.org/docs/adapter.html\#reflective-schema "Permalink")

A reflective schema
( [`class ReflectiveSchema`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/java/ReflectiveSchema.html))
is a way of wrapping a Java object so that it appears
as a schema. Its collection-valued fields will appear as tables.

It is not a schema factory but an actual schema; you have to create the object
and wrap it in the schema by calling APIs.

See
[`class ReflectiveSchemaTest`](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/test/ReflectiveSchemaTest.java).

### Defining a custom table [Permalink](https://calcite.apache.org/docs/adapter.html\#defining-a-custom-table "Permalink")

To define a custom table, you need to implement
[`interface TableFactory`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TableFactory.html).
Whereas a schema factory a set of named tables, a table factory produces a
single table when bound to a schema with a particular name (and optionally a
set of extra operands).

### Modifying data [Permalink](https://calcite.apache.org/docs/adapter.html\#modifying-data "Permalink")

If your table is to support DML operations (INSERT, UPDATE, DELETE, MERGE),
your implementation of `interface Table` must implement
[`interface ModifiableTable`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/ModifiableTable.html).

### Streaming [Permalink](https://calcite.apache.org/docs/adapter.html\#streaming "Permalink")

If your table is to support streaming queries,
your implementation of `interface Table` must implement
[`interface StreamableTable`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/StreamableTable.html).

See
[`class StreamTest`](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/test/StreamTest.java)
for examples.

### Pushing operations down to your table [Permalink](https://calcite.apache.org/docs/adapter.html\#pushing-operations-down-to-your-table "Permalink")

If you wish to push processing down to your custom table’s source system,
consider implementing either
[`interface FilterableTable`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/FilterableTable.html)
or
[`interface ProjectableFilterableTable`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/ProjectableFilterableTable.html).

If you want more control, you should write a [planner rule](https://calcite.apache.org/docs/adapter.html#planner-rule).
This will allow you to push down expressions, to make a cost-based decision
about whether to push down processing, and push down more complex operations
such as join, aggregation, and sort.

### Type system [Permalink](https://calcite.apache.org/docs/adapter.html\#type-system "Permalink")

You can customize some aspects of the type system by implementing
[`interface RelDataTypeSystem`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/type/RelDataTypeSystem.html).

### Relational operators [Permalink](https://calcite.apache.org/docs/adapter.html\#relational-operators "Permalink")

All relational operators implement
[`interface RelNode`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/RelNode.html)
and most extend
[`class AbstractRelNode`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/AbstractRelNode.html).
The core operators (used by
[`SqlToRelConverter`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql2rel/SqlToRelConverter.html)
and covering conventional relational algebra) are
[`TableScan`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableScan.html),
[`TableModify`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableModify.html),
[`Values`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Values.html),
[`Project`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Project.html),
[`Filter`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Filter.html),
[`Aggregate`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Aggregate.html),
[`Join`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Join.html),
[`Sort`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Sort.html),
[`Union`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Union.html),
[`Intersect`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Intersect.html),
[`Minus`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Minus.html),
[`Window`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Window.html) and
[`Match`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Match.html).

Each of these has a “pure” logical sub-class,
[`LogicalProject`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/logical/LogicalProject.html)
and so forth. Any given adapter will have counterparts for the operations that
its engine can implement efficiently; for example, the Cassandra adapter has
[`CassandraProject`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/cassandra/CassandraProject.html)
but there is no `CassandraJoin`.

You can define your own sub-class of `RelNode` to add a new operator, or
an implementation of an existing operator in a particular engine.

To make an operator useful and powerful, you will need
[planner rules](https://calcite.apache.org/docs/adapter.html#planner-rule) to combine it with existing operators.
(And also provide metadata, see [below](https://calcite.apache.org/docs/adapter.html#statistics-and-cost)).
This being algebra, the effects are combinatorial: you write a few
rules, but they combine to handle an exponential number of query patterns.

If possible, make your operator a sub-class of an existing
operator; then you may be able to re-use or adapt its rules.
Even better, if your operator is a logical operation that you can rewrite
(again, via a planner rule) in terms of existing operators, you should do that.
You will be able to re-use the rules, metadata and implementations of those
operators with no extra work.

### Planner rule [Permalink](https://calcite.apache.org/docs/adapter.html\#planner-rule "Permalink")

A planner rule
( [`class RelOptRule`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/plan/RelOptRule.html))
transforms a relational expression into an equivalent relational expression.

A planner engine has many planner rules registered and fires them
to transform the input query into something more efficient. Planner rules are
therefore central to the optimization process, but surprisingly each planner
rule does not concern itself with cost. The planner engine is responsible for
firing rules in a sequence that produces an optimal plan, but each individual
rules only concerns itself with correctness.

Calcite has two built-in planner engines:
[`class VolcanoPlanner`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/plan/volcano/VolcanoPlanner.html)
uses dynamic programming and is good for exhaustive search, whereas
[`class HepPlanner`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/plan/hep/HepPlanner.html)
fires a sequence of rules in a more fixed order.

### Calling conventions [Permalink](https://calcite.apache.org/docs/adapter.html\#calling-conventions "Permalink")

A calling convention is a protocol used by a particular data engine.
For example, the Cassandra engine has a collection of relational operators,
`CassandraProject`, `CassandraFilter` and so forth, and these operators can be
connected to each other without the data having to be converted from one format
to another.

If data needs to be converted from one calling convention to another, Calcite
uses a special sub-class of relational expression called a converter
(see [`interface Converter`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/convert/Converter.html)).
But of course converting data has a runtime cost.

When planning a query that uses multiple engines, Calcite “colors” regions of
the relational expression tree according to their calling convention. The
planner pushes operations into data sources by firing rules. If the engine does
not support a particular operation, the rule will not fire. Sometimes an
operation can occur in more than one place, and ultimately the best plan is
chosen according to cost.

A calling convention is a class that implements
[`interface Convention`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/plan/Convention.html),
an auxiliary interface (for instance
[`interface CassandraRel`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/cassandra/CassandraRel.html)),
and a set of sub-classes of
[`class RelNode`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/RelNode.html)
that implement that interface for the core relational operators
( [`Project`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Project.html),
[`Filter`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Filter.html),
[`Aggregate`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Aggregate.html),
and so forth).

### Built-in SQL implementation [Permalink](https://calcite.apache.org/docs/adapter.html\#built-in-sql-implementation "Permalink")

How does Calcite implement SQL, if an adapter does not implement all of the core
relational operators?

The answer is a particular built-in calling convention,
[`EnumerableConvention`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/adapter/enumerable/EnumerableConvention.html).
Relational expressions of enumerable convention are implemented as “built-ins”:
Calcite generates Java code, compiles it, and executes inside its own JVM.
Enumerable convention is less efficient than, say, a distributed engine
running over column-oriented data files, but it can implement all core
relational operators and all built-in SQL functions and operators. If a data
source cannot implement a relational operator, enumerable convention is
a fall-back.

### Statistics and cost [Permalink](https://calcite.apache.org/docs/adapter.html\#statistics-and-cost "Permalink")

Calcite has a metadata system that allows you to define cost functions and
statistics about relational operators, collectively referred to as _metadata_.
Each kind of metadata has an interface with (usually) one method.
For example, selectivity is defined by
[`class RelMdSelectivity`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdSelectivity.html)
and the method
[`getSelectivity(RelNode rel, RexNode predicate)`](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMetadataQuery.html#getSelectivity(org.apache.calcite.rel.RelNode,org.apache.calcite.rex.RexNode)).

There are many built-in kinds of metadata, including
[collation](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdCollation.html),
[column origins](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdColumnOrigins.html),
[column uniqueness](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdColumnUniqueness.html),
[distinct row count](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdDistinctRowCount.html),
[distribution](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdDistribution.html),
[explain visibility](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdExplainVisibility.html),
[expression lineage](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdExpressionLineage.html),
[max row count](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdMaxRowCount.html),
[node types](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdNodeTypes.html),
[parallelism](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdParallelism.html),
[percentage original rows](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdPercentageOriginalRows.html),
[population size](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdPopulationSize.html),
[predicates](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdPredicates.html),
[row count](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdRowCount.html),
[selectivity](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdSelectivity.html),
[size](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdSize.html),
[table references](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdTableReferences.html), and
[unique keys](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/metadata/RelMdUniqueKeys.html);
you can also define your own.

You can then supply a _metadata provider_ that computes that kind of metadata
for particular sub-classes of `RelNode`. Metadata providers can handle built-in
and extended metadata types, and built-in and extended `RelNode` types.
While preparing a query Calcite combines all of the applicable metadata
providers and maintains a cache so that a given piece of metadata (for example
the selectivity of the condition `x > 10` in a particular `Filter` operator)
is computed only once.

[Previous](https://calcite.apache.org/docs/algebra.html)

[Next](https://calcite.apache.org/docs/spatial.html)