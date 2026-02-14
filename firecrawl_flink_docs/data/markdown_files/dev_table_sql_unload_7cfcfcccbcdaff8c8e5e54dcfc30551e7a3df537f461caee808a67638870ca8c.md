> This documentation is for an out-of-date version of Apache Flink. We recommend you use the latest [stable version](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/unload/).

# UNLOAD Statements  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/sql/unload/\#unload-statements)

UNLOAD statements are used to unload a built-in or user-defined module.

## Run a UNLOAD statement  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/sql/unload/\#run-a-unload-statement)

Java

UNLOAD statements can be executed with the `executeSql()` method of the `TableEnvironment`. The `executeSql()` method returns ‘OK’ for a successful UNLOAD operation; otherwise it will throw an exception.

The following examples show how to run a UNLOAD statement in `TableEnvironment`.

Scala

UNLOAD statements can be executed with the `executeSql()` method of the `TableEnvironment`. The `executeSql()` method returns ‘OK’ for a successful UNLOAD operation; otherwise it will throw an exception.

The following examples show how to run a UNLOAD statement in `TableEnvironment`.

Python

UNLOAD statements can be executed with the `execute_sql()` method of the `TableEnvironment`. The `execute_sql()` method returns ‘OK’ for a successful UNLOAD operation; otherwise it will throw an exception.

The following examples show how to run a UNLOAD statement in `TableEnvironment`.

SQL CLI

UNLOAD statements can be executed in [SQL CLI](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/sqlclient/).

The following examples show how to run a UNLOAD statement in SQL CLI.

Java

```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
StreamTableEnvironment tEnv = StreamTableEnvironment.create(env);

// unload a core module
tEnv.executeSql("UNLOAD MODULE core");
tEnv.executeSql("SHOW MODULES").print();
// Empty set
```

Scala

```scala
val env = StreamExecutionEnvironment.getExecutionEnvironment()
val tEnv = StreamTableEnvironment.create(env)

// unload a core module
tEnv.executeSql("UNLOAD MODULE core")
tEnv.executeSql("SHOW MODULES").print()
// Empty set
```

Python

```python
table_env = StreamTableEnvironment.create(...)

# unload a core module
table_env.execute_sql("UNLOAD MODULE core")
table_env.execute_sql("SHOW MODULES").print()
# Empty set
```

SQL CLI

```sql
Flink SQL> UNLOAD MODULE core;
[INFO] Unload module succeeded!

Flink SQL> SHOW MODULES;
Empty set
```

## UNLOAD MODULE  [\#](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/sql/unload/\#unload-module)

The following grammar gives an overview of the available syntax:

```sql
UNLOAD MODULE module_name
```