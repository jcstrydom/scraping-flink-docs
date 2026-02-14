Navigate the docs…

# Algebra

Relational algebra is at the heart of Calcite. Every query is
represented as a tree of relational operators. You can translate from
SQL to relational algebra, or you can build the tree directly.

Planner rules transform expression trees using mathematical identities
that preserve semantics. For example, it is valid to push a filter
into an input of an inner join if the filter does not reference
columns from the other input.

Calcite optimizes queries by repeatedly applying planner rules to a
relational expression. A cost model guides the process, and the
planner engine generates an alternative expression that has the same
semantics as the original but a lower cost.

The planning process is extensible. You can add your own relational
operators, planner rules, cost model, and statistics.

## Algebra builder [Permalink](https://calcite.apache.org/docs/algebra.html\#algebra-builder "Permalink")

The simplest way to build a relational expression is to use the algebra builder,
[RelBuilder](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.html).
Here is an example:

### TableScan [Permalink](https://calcite.apache.org/docs/algebra.html\#tablescan "Permalink")

```java
final FrameworkConfig config;
final RelBuilder builder = RelBuilder.create(config);
final RelNode node = builder
  .scan("EMP")
  .build();
System.out.println(RelOptUtil.toString(node));
```

(You can find the full code for this and other examples in
[RelBuilderExample.java](https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/examples/RelBuilderExample.java).)

The code prints

```text
LogicalTableScan(table=[[scott, EMP]])
```

It has created a scan of the `EMP` table; equivalent to the SQL

```sql
SELECT *
FROM scott.EMP;
```

### Adding a Project [Permalink](https://calcite.apache.org/docs/algebra.html\#adding-a-project "Permalink")

Now, let’s add a Project, the equivalent of

```sql
SELECT ename, deptno
FROM scott.EMP;
```

We just add a call to the `project` method before calling
`build`:

```java
final RelNode node = builder
  .scan("EMP")
  .project(builder.field("DEPTNO"), builder.field("ENAME"))
  .build();
System.out.println(RelOptUtil.toString(node));
```

and the output is

```text
LogicalProject(DEPTNO=[$7], ENAME=[$1])
  LogicalTableScan(table=[[scott, EMP]])
```

The two calls to `builder.field` create simple expressions
that return the fields from the input relational expression,
namely the TableScan created by the `scan` call.

Calcite has converted them to field references by ordinal,
`$7` and `$1`.

### Adding a Filter and Aggregate [Permalink](https://calcite.apache.org/docs/algebra.html\#adding-a-filter-and-aggregate "Permalink")

A query with an Aggregate, and a Filter:

```java
final RelNode node = builder
  .scan("EMP")
  .aggregate(builder.groupKey("DEPTNO"),
      builder.count(false, "C"),
      builder.sum(false, "S", builder.field("SAL")))
  .filter(
      builder.call(SqlStdOperatorTable.GREATER_THAN,
          builder.field("C"),
          builder.literal(10)))
  .build();
System.out.println(RelOptUtil.toString(node));
```

is equivalent to SQL

```sql
SELECT deptno, count(*) AS c, sum(sal) AS s
FROM emp
GROUP BY deptno
HAVING count(*) > 10
```

and produces

```text
LogicalFilter(condition=[>($1, 10)])
  LogicalAggregate(group=[{7}], C=[COUNT()], S=[SUM($5)])
    LogicalTableScan(table=[[scott, EMP]])
```

### Push and pop [Permalink](https://calcite.apache.org/docs/algebra.html\#push-and-pop "Permalink")

The builder uses a stack to store the relational expression produced by
one step and pass it as an input to the next step. This allows the
methods that produce relational expressions to produce a builder.

Most of the time, the only stack method you will use is `build()`, to get the
last relational expression, namely the root of the tree.

Sometimes the stack becomes so deeply nested it gets confusing. To keep things
straight, you can remove expressions from the stack. For example, here we are
building a bushy join:

```text
.
               join
             /      \
        join          join
      /      \      /      \
CUSTOMERS ORDERS LINE_ITEMS PRODUCTS
```

We build it in three stages. Store the intermediate results in variables
`left` and `right`, and use `push()` to put them back on the stack when it is
time to create the final `Join`:

```java
final RelNode left = builder
  .scan("CUSTOMERS")
  .scan("ORDERS")
  .join(JoinRelType.INNER, "ORDER_ID")
  .build();

final RelNode right = builder
  .scan("LINE_ITEMS")
  .scan("PRODUCTS")
  .join(JoinRelType.INNER, "PRODUCT_ID")
  .build();

final RelNode result = builder
  .push(left)
  .push(right)
  .join(JoinRelType.INNER, "ORDER_ID")
  .build();
```

### Switch Convention [Permalink](https://calcite.apache.org/docs/algebra.html\#switch-convention "Permalink")

The default RelBuilder creates logical RelNode without coventions. But you could
switch to use a different convention through `adoptConvention()`:

```java
final RelNode result = builder
  .push(input)
  .adoptConvention(EnumerableConvention.INSTANCE)
  .sort(toCollation)
  .build();
```

In this case, we create an EnumerableSort on top of the input RelNode.

### Field names and ordinals [Permalink](https://calcite.apache.org/docs/algebra.html\#field-names-and-ordinals "Permalink")

You can reference a field by name or ordinal.

Ordinals are zero-based. Each operator guarantees the order in which its output
fields occur. For example, `Project` returns the fields generated by
each of the scalar expressions.

The field names of an operator are guaranteed to be unique, but sometimes that
means that the names are not exactly what you expect. For example, when you
join EMP to DEPT, one of the output fields will be called DEPTNO and another
will be called something like DEPTNO\_1.

Some relational expression methods give you more control over field names:

- `project` lets you wrap expressions using `alias(expr, fieldName)`. It
removes the wrapper but keeps the suggested name (as long as it is unique).
- `values(String[] fieldNames, Object... values)` accepts an array of field
names. If any element of the array is null, the builder will generate a unique
name.

If an expression projects an input field, or a cast of an input field, it will
use the name of that input field.

Once the unique field names have been assigned, the names are immutable.
If you have a particular `RelNode` instance, you can rely on the field names not
changing. In fact, the whole relational expression is immutable.

But if a relational expression has passed through several rewrite rules (see
[RelOptRule](https://calcite.apache.org/javadocAggregate/org/apache/calcite/plan/RelOptRule.html)), the field
names of the resulting expression might not look much like the originals.
At that point it is better to reference fields by ordinal.

When you are building a relational expression that accepts multiple inputs,
you need to build field references that take that into account. This occurs
most often when building join conditions.

Suppose you are building a join on EMP,
which has 8 fields \[EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO\]
and DEPT,
which has 3 fields \[DEPTNO, DNAME, LOC\].
Internally, Calcite represents those fields as offsets into
a combined input row with 11 fields: the first field of the left input is
field #0 (0-based, remember), and the first field of the right input is
field #8.

But through the builder API, you specify which field of which input.
To reference “SAL”, internal field #5,
write `builder.field(2, 0, "SAL")`, `builder.field(2, "EMP", "SAL")`,
or `builder.field(2, 0, 5)`.
This means “the field #5 of input #0 of two inputs”.
(Why does it need to know that there are two inputs? Because they are stored on
the stack; input #1 is at the top of the stack, and input #0 is below it.
If we did not tell the builder that were two inputs, it would not know how deep
to go for input #0.)

Similarly, to reference “DNAME”, internal field #9 (8 + 1),
write `builder.field(2, 1, "DNAME")`, `builder.field(2, "DEPT", "DNAME")`,
or `builder.field(2, 1, 1)`.

### Recursive Queries [Permalink](https://calcite.apache.org/docs/algebra.html\#recursive-queries "Permalink")

Warning: The current API is experimental and subject to change without notice.
A SQL recursive query, e.g. this one that generates the sequence 1, 2, 3, …10:

```sql
WITH RECURSIVE aux(i) AS (
  VALUES (1)
  UNION ALL
  SELECT i+1 FROM aux WHERE i < 10
)
SELECT * FROM aux
```

can be generated using a scan on a TransientTable and a RepeatUnion:

```java
final RelNode node = builder
  .values(new String[] { "i" }, 1)
  .transientScan("aux")
  .filter(
      builder.call(
          SqlStdOperatorTable.LESS_THAN,
          builder.field(0),
          builder.literal(10)))
  .project(
      builder.call(
          SqlStdOperatorTable.PLUS,
          builder.field(0),
          builder.literal(1)))
  .repeatUnion("aux", true)
  .build();
System.out.println(RelOptUtil.toString(node));
```

which produces:

```text
LogicalRepeatUnion(all=[true])
  LogicalTableSpool(readType=[LAZY], writeType=[LAZY], tableName=[aux])
    LogicalValues(tuples=[[{ 1 }]])
  LogicalTableSpool(readType=[LAZY], writeType=[LAZY], tableName=[aux])
    LogicalProject($f0=[+($0, 1)])
      LogicalFilter(condition=[<($0, 10)])
        LogicalTableScan(table=[[aux]])
```

### API summary [Permalink](https://calcite.apache.org/docs/algebra.html\#api-summary "Permalink")

#### Relational operators [Permalink](https://calcite.apache.org/docs/algebra.html\#relational-operators "Permalink")

The following methods create a relational expression
( [RelNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/RelNode.html)),
push it onto the stack, and
return the `RelBuilder`.

| Method | Description |
| --- | --- |
| `scan(tableName)` | Creates a [TableScan](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableScan.html). |
| `functionScan(operator, n, expr...)`<br>`functionScan(operator, n, exprList)` | Creates a [TableFunctionScan](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableFunctionScan.html) of the `n` most recent relational expressions. |
| `transientScan(tableName [, rowType])` | Creates a [TableScan](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/TableScan.html) on a [TransientTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TransientTable.html) with the given type (if not specified, the most recent relational expression’s type will be used). |
| `values(fieldNames, value...)`<br>`values(rowType, tupleList)` | Creates a [Values](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Values.html). |
| `filter([variablesSet, ] exprList)`<br>`filter([variablesSet, ] expr...)` | Creates a [Filter](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Filter.html) over the AND of the given predicates; if `variablesSet` is specified, the predicates may reference those variables. |
| `project(expr...)`<br>`project(exprList [, fieldNames])` | Creates a [Project](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Project.html). To override the default name, wrap expressions using `alias`, or specify the `fieldNames` argument. |
| `projectPlus(expr...)`<br>`projectPlus(exprList)` | Variant of `project` that keeps original fields and appends the given expressions. |
| `projectExcept(expr...)`<br>`projectExcept(exprList)` | Variant of `project` that keeps original fields and removes the given expressions. |
| `permute(mapping)` | Creates a [Project](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Project.html) that permutes the fields using `mapping`. |
| `convert(rowType [, rename])` | Creates a [Project](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Project.html) that converts the fields to the given types, optionally also renaming them. |
| `aggregate(groupKey, aggCall...)`<br>`aggregate(groupKey, aggCallList)` | Creates an [Aggregate](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Aggregate.html). |
| `distinct()` | Creates an [Aggregate](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Aggregate.html) that eliminates duplicate records. |
| `pivot(groupKey, aggCalls, axes, values)` | Adds a pivot operation, implemented by generating an [Aggregate](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Aggregate.html) with a column for each combination of measures and values |
| `unpivot(includeNulls, measureNames, axisNames, axisMap)` | Adds an unpivot operation, implemented by generating a [Join](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Join.html) to a [Values](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Values.html) that converts each row to several rows |
| `sort(fieldOrdinal...)`<br>`sort(expr...)`<br>`sort(exprList)` | Creates a [Sort](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Sort.html).<br>In the first form, field ordinals are 0-based, and a negative ordinal indicates descending; for example, -2 means field 1 descending.<br>In the other forms, you can wrap expressions in `as`, `nullsFirst` or `nullsLast`. |
| `sortLimit(offset, fetch, expr...)`<br>`sortLimit(offset, fetch, exprList)` | Creates a [Sort](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Sort.html) with offset and limit. |
| `limit(offset, fetch)` | Creates a [Sort](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Sort.html) that does not sort, only applies with offset and limit. |
| `exchange(distribution)` | Creates an [Exchange](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Exchange.html). |
| `sortExchange(distribution, collation)` | Creates a [SortExchange](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/SortExchange.html). |
| `correlate(joinType, correlationId, requiredField...)`<br>`correlate(joinType, correlationId, requiredFieldList)` | Creates a [Correlate](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Correlate.html) of the two most recent relational expressions, with a variable name and required field expressions for the left relation. |
| `join(joinType, expr...)`<br>`join(joinType, exprList)`<br>`join(joinType, fieldName...)` | Creates a [Join](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Join.html) of the two most recent relational expressions.<br>The first form joins on a boolean expression (multiple conditions are combined using AND).<br>The last form joins on named fields; each side must have a field of each name. |
| `semiJoin(expr)` | Creates a [Join](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Join.html) with SEMI join type of the two most recent relational expressions. |
| `antiJoin(expr)` | Creates a [Join](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Join.html) with ANTI join type of the two most recent relational expressions. |
| `union(all [, n])` | Creates a [Union](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Union.html) of the `n` (default two) most recent relational expressions. |
| `intersect(all [, n])` | Creates an [Intersect](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Intersect.html) of the `n` (default two) most recent relational expressions. |
| `minus(all)` | Creates a [Minus](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Minus.html) of the two most recent relational expressions. |
| `repeatUnion(tableName, all [, n])` | Creates a [RepeatUnion](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/RepeatUnion.html) associated to a [TransientTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TransientTable.html) of the two most recent relational expressions, with `n` maximum number of iterations (default -1, i.e. no limit). |
| `sample(bernoulli, rate [, repeatableSeed])` | Creates a [sample](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Sample.html) of at given sampling rate. |
| `snapshot(period)` | Creates a [Snapshot](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Snapshot.html) of the given snapshot period. |
| `match(pattern, strictStart,``strictEnd, patterns, measures,``after, subsets, allRows,``partitionKeys, orderKeys,``interval)` | Creates a [Match](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/Match.html). |

Argument types:

- `expr`, `interval` [RexNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexNode.html)
- `expr...`, `requiredField...` Array of
[RexNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexNode.html)
- `exprList`, `measureList`, `partitionKeys`, `orderKeys`,
`requiredFieldList` Iterable of
[RexNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexNode.html)
- `fieldOrdinal` Ordinal of a field within its row (starting from 0)
- `fieldName` Name of a field, unique within its row
- `fieldName...` Array of String
- `fieldNames` Iterable of String
- `rowType` [RelDataType](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/type/RelDataType.html)
- `groupKey` [RelBuilder.GroupKey](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.GroupKey.html)
- `aggCall...` Array of [RelBuilder.AggCall](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.AggCall.html)
- `aggCallList` Iterable of [RelBuilder.AggCall](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.AggCall.html)
- `value...` Array of Object
- `value` Object
- `tupleList` Iterable of List of [RexLiteral](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexLiteral.html)
- `all`, `distinct`, `strictStart`, `strictEnd`, `allRows` boolean
- `alias` String
- `correlationId` [CorrelationId](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/CorrelationId.html)
- `variablesSet` Iterable of
[CorrelationId](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/CorrelationId.html)
- `varHolder` [Holder](https://calcite.apache.org/javadocAggregate/org/apache/calcite/util/Holder.html) of [RexCorrelVariable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexCorrelVariable.html)
- `patterns` Map whose key is String, value is [RexNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexNode.html)
- `subsets` Map whose key is String, value is a sorted set of String
- `distribution` [RelDistribution](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/RelDistribution.html)
- `collation` [RelCollation](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/RelCollation.html)
- `operator` [SqlOperator](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/SqlOperator.html)
- `joinType` [JoinRelType](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rel/core/JoinRelType.html)

The builder methods perform various optimizations, including:

- `project` returns its input if asked to project all columns in order
- `filter` flattens the condition (so an `AND` and `OR` may have more than 2 children),
simplifies (converting say `x = 1 AND TRUE` to `x = 1`)
- If you apply `sort` then `limit`, the effect is as if you had called `sortLimit`

There are annotation methods that add information to the top relational
expression on the stack:

| Method | Description |
| --- | --- |
| `as(alias)` | Assigns a table alias to the top relational expression on the stack |
| `variable(varHolder)` | Creates a correlation variable referencing the top relational expression |

#### Stack methods [Permalink](https://calcite.apache.org/docs/algebra.html\#stack-methods "Permalink")

| Method | Description |
| --- | --- |
| `build()` | Pops the most recently created relational expression off the stack |
| `push(rel)` | Pushes a relational expression onto the stack. Relational methods such as `scan`, above, call this method, but user code generally does not |
| `pushAll(collection)` | Pushes a collection of relational expressions onto the stack |
| `peek()` | Returns the relational expression most recently put onto the stack, but does not remove it |

#### Scalar expression methods [Permalink](https://calcite.apache.org/docs/algebra.html\#scalar-expression-methods "Permalink")

The following methods return a scalar expression
( [RexNode](https://calcite.apache.org/javadocAggregate/org/apache/calcite/rex/RexNode.html)).

Many of them use the contents of the stack. For example, `field("DEPTNO")`
returns a reference to the “DEPTNO” field of the relational expression just
added to the stack.

| Method | Description |
| --- | --- |
| `literal(value)` | Constant |
| `field(fieldName)` | Reference, by name, to a field of the top-most relational expression |
| `field(fieldOrdinal)` | Reference, by ordinal, to a field of the top-most relational expression |
| `field(inputCount, inputOrdinal, fieldName)` | Reference, by name, to a field of the (`inputCount` \- `inputOrdinal`)th relational expression |
| `field(inputCount, inputOrdinal, fieldOrdinal)` | Reference, by ordinal, to a field of the (`inputCount` \- `inputOrdinal`)th relational expression |
| `field(inputCount, alias, fieldName)` | Reference, by table alias and field name, to a field at most `inputCount - 1` elements from the top of the stack |
| `field(alias, fieldName)` | Reference, by table alias and field name, to a field of the top-most relational expressions |
| `field(expr, fieldName)` | Reference, by name, to a field of a record-valued expression |
| `field(expr, fieldOrdinal)` | Reference, by ordinal, to a field of a record-valued expression |
| `fields(fieldOrdinalList)` | List of expressions referencing input fields by ordinal |
| `fields(mapping)` | List of expressions referencing input fields by a given mapping |
| `fields(collation)` | List of expressions, `exprList`, such that `sort(exprList)` would replicate collation |
| `call(op, expr...)`<br>`call(op, exprList)` | Call to a function or operator |
| `and(expr...)`<br>`and(exprList)` | Logical AND. Flattens nested ANDs, and optimizes cases involving TRUE and FALSE. |
| `or(expr...)`<br>`or(exprList)` | Logical OR. Flattens nested ORs, and optimizes cases involving TRUE and FALSE. |
| `not(expr)` | Logical NOT |
| `equals(expr, expr)` | Equals |
| `isNull(expr)` | Checks whether an expression is null |
| `isNotNull(expr)` | Checks whether an expression is not null |
| `alias(expr, fieldName)` | Renames an expression (only valid as an argument to `project`) |
| `cast(expr, typeName)`<br>`cast(expr, typeName, precision)`<br>`cast(expr, typeName, precision, scale)` | Converts an expression to a given type |
| `desc(expr)` | Changes sort direction to descending (only valid as an argument to `sort` or `sortLimit`) |
| `nullsFirst(expr)` | Changes sort order to nulls first (only valid as an argument to `sort` or `sortLimit`) |
| `nullsLast(expr)` | Changes sort order to nulls last (only valid as an argument to `sort` or `sortLimit`) |
| `cursor(n, input)` | Reference to `input`th (0-based) relational input of a `TableFunctionScan` with `n` inputs (see `functionScan`) |

#### Sub-query methods [Permalink](https://calcite.apache.org/docs/algebra.html\#sub-query-methods "Permalink")

The following methods convert a sub-query into a scalar value (a `BOOLEAN` in
the case of `in`, `exists`, `some`, `all`, `unique`;
any scalar type for `scalarQuery`).
an `ARRAY` for `arrayQuery`,
a `MAP` for `mapQuery`,
and a `MULTISET` for `multisetQuery`).

In all the following, `relFn` is a function that takes a `RelBuilder` argument
and returns a `RelNode`. You typically implement it as a lambda; the method
calls your code with a `RelBuilder` that has the correct context, and your code
returns the `RelNode` that is to be the sub-query.

| Method | Description |
| --- | --- |
| `all(expr, op, relFn)` | Returns whether _expr_ has a particular relation to all of the values of the sub-query |
| `arrayQuery(relFn)` | Returns the rows of a sub-query as an `ARRAY` |
| `exists(relFn)` | Tests whether sub-query is non-empty |
| `in(expr, relFn)`<br>`in(exprList, relFn)` | Tests whether a value occurs in a sub-query |
| `mapQuery(relFn)` | Returns the rows of a sub-query as a `MAP` |
| `multisetQuery(relFn)` | Returns the rows of a sub-query as a `MULTISET` |
| `scalarQuery(relFn)` | Returns the value of the sole column of the sole row of a sub-query |
| `some(expr, op, relFn)` | Returns whether _expr_ has a particular relation to one or more of the values of the sub-query |
| `unique(relFn)` | Returns whether the rows of a sub-query are unique |

#### Pattern methods [Permalink](https://calcite.apache.org/docs/algebra.html\#pattern-methods "Permalink")

The following methods return patterns for use in `match`.

| Method | Description |
| --- | --- |
| `patternConcat(pattern...)` | Concatenates patterns |
| `patternAlter(pattern...)` | Alternates patterns |
| `patternQuantify(pattern, min, max)` | Quantifies a pattern |
| `patternPermute(pattern...)` | Permutes a pattern |
| `patternExclude(pattern)` | Excludes a pattern |

#### Group key methods [Permalink](https://calcite.apache.org/docs/algebra.html\#group-key-methods "Permalink")

The following methods return a
[RelBuilder.GroupKey](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.GroupKey.html).

| Method | Description |
| --- | --- |
| `groupKey(fieldName...)`<br>`groupKey(fieldOrdinal...)`<br>`groupKey(expr...)`<br>`groupKey(exprList)` | Creates a group key of the given expressions |
| `groupKey(exprList, exprListList)` | Creates a group key of the given expressions with grouping sets |
| `groupKey(bitSet [, bitSets])` | Creates a group key of the given input columns, with multiple grouping sets if `bitSets` is specified |

#### Aggregate call methods [Permalink](https://calcite.apache.org/docs/algebra.html\#aggregate-call-methods "Permalink")

The following methods return an
[RelBuilder.AggCall](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.AggCall.html).

| Method | Description |
| --- | --- |
| `aggregateCall(op, expr...)`<br>`aggregateCall(op, exprList)` | Creates a call to a given aggregate function |
| `count([ distinct, alias, ] expr...)`<br>`count([ distinct, alias, ] exprList)` | Creates a call to the `COUNT` aggregate function |
| `countStar(alias)` | Creates a call to the `COUNT(*)` aggregate function |
| `literalAgg(value)` | Creates a call to an aggregate function that always evaluates to _value_ |
| `max([ alias, ] expr)` | Creates a call to the `MAX` aggregate function |
| `min([ alias, ] expr)` | Creates a call to the `MIN` aggregate function |
| `sum([ distinct, alias, ] expr)` | Creates a call to the `SUM` aggregate function |

To further modify the `AggCall`, call its methods:

| Method | Description |
| --- | --- |
| `approximate(approximate)` | Allows approximate value for the aggregate of `approximate` |
| `as(alias)` | Assigns a column alias to this expression (see SQL `AS`) |
| `distinct()` | Eliminates duplicate values before aggregating (see SQL `DISTINCT`) |
| `distinct(distinct)` | Eliminates duplicate values before aggregating if `distinct` |
| `filter(expr)` | Filters rows before aggregating (see SQL `FILTER (WHERE ...)`) |
| `sort(expr...)`<br>`sort(exprList)` | Sorts rows before aggregating (see SQL `WITHIN GROUP`) |
| `unique(expr...)`<br>`unique(exprList)` | Makes rows unique before aggregating (see SQL `WITHIN DISTINCT`) |
| `over()` | Converts this `AggCall` into a windowed aggregate (see `OverCall` below) |

#### Windowed aggregate call methods [Permalink](https://calcite.apache.org/docs/algebra.html\#windowed-aggregate-call-methods "Permalink")

To create an
[RelBuilder.OverCall](https://calcite.apache.org/javadocAggregate/org/apache/calcite/tools/RelBuilder.OverCall.html),
which represents a call to a windowed aggregate function, create an aggregate
call and then call its `over()` method, for instance `count().over()`.

To further modify the `OverCall`, call its methods:

| Method | Description |
| --- | --- |
| `rangeUnbounded()` | Creates an unbounded range-based window, `RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` |
| `rangeFrom(lower)` | Creates a range-based window bounded below, `RANGE BETWEEN lower AND CURRENT ROW` |
| `rangeTo(upper)` | Creates a range-based window bounded above, `RANGE BETWEEN CURRENT ROW AND upper` |
| `rangeBetween(lower, upper)` | Creates a range-based window, `RANGE BETWEEN lower AND upper` |
| `rowsUnbounded()` | Creates an unbounded row-based window, `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` |
| `rowsFrom(lower)` | Creates a row-based window bounded below, `ROWS BETWEEN lower AND CURRENT ROW` |
| `rowsTo(upper)` | Creates a row-based window bounded above, `ROWS BETWEEN CURRENT ROW AND upper` |
| `rowsBetween(lower, upper)` | Creates a rows-based window, `ROWS BETWEEN lower AND upper` |
| `exclude(excludeType)` | Exclude certain rows from the frame (see SQL `EXCLUDE`) |
| `partitionBy(expr...)`<br>`partitionBy(exprList)` | Partitions the window on the given expressions (see SQL `PARTITION BY`) |
| `orderBy(expr...)`<br>`sort(exprList)` | Sorts the rows in the window (see SQL `ORDER BY`) |
| `allowPartial(b)` | Sets whether to allow partial width windows; default true |
| `nullWhenCountZero(b)` | Sets whether whether the aggregate function should evaluate to null if no rows are in the window; default false |
| `as(alias)` | Assigns a column alias (see SQL `AS`) and converts this `OverCall` to a `RexNode` |
| `toRex()` | Converts this `OverCall` to a `RexNode` |

[Previous](https://calcite.apache.org/docs/tutorial.html)

[Next](https://calcite.apache.org/docs/adapter.html)