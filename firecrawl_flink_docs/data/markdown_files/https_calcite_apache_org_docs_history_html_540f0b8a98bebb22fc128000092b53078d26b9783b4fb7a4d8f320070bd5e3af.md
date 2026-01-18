Navigate the docs…

# History

For a full list of releases, see
[github](https://github.com/apache/calcite/tags).
Downloads are available on the
[downloads page](https://calcite.apache.org/downloads/).

## [1.41.0](https://github.com/apache/calcite/releases/tag/calcite-1.41.0) / 2025-11-01 [Permalink](https://calcite.apache.org/docs/history.html\#v1-41-0 "Permalink")

This release comes 5 months after [1.40.0](https://calcite.apache.org/docs/history.html#v1-40-0),
contains contributions from 41 contributors, and resolves 155 issues.

Highlights include support for several `UNSIGNED` types in the type system,
get functional dependency metadata in `RelMetadataQuery`,
supporting various join types on DPhyp join reorder algorithm,
a new API for finding common relational sub-expressions,
and new bitwise operators. Regarding this last feature, it can be possible for a certain bitwise operator and its
corresponding already existing SQL function to have discrepancies on operand type checker and return type inference when
unsigned parameters are involved; this shall be aligned in future versions.

Contributors to this release:
Aleksey Plekhanov,
Alessandro Solimando,
Arnaud Jegou,
Chris Dennis,
Claude Brisson,
Denys Kuzmenko,
Dmitry Sysolyatin,
Gian Merlino,
Guillaume Massé,
Ian Bertolacci,
Istvan Toth,
iwanttobepowerful,
Julian Hyde,
Juntao Zhang,
Konstantin Orlov,
lincoln-lil,
liuyuhanalex,
Lucas Brenner,
Michael Mior,
Michal Stutzmann,
Mihai Budiu,
Niels Pardon,
Richard Antal,
Ruben Quesada Lopez (release manager),
Sergey Nuyanzin,
Silun Dong,
Soumyakanti Das,
Stamatis Zampetakis,
suibianwanwan,
TJ Banghart,
Wang Zhao,
wuxiaojun,
Xiaochen Zhou,
xiaojun,
Xiong Duan,
Xiong Tenghui,
xuzifu666,
Yu Xu,
Zhe Hu,
Zhen Chen,
Zhengqiang Duan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 23;
Guava versions 21.0 to 33.4.8-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-41-0 "Permalink")

- \[ [CALCITE-7029](https://issues.apache.org/jira/browse/CALCITE-7029)\]
This feature introduced `RexNodeAndFieldIndex` (a new subclass of `RexVariable`) and its corresponding
`visitNodeAndFieldIndex` method in the `RexVisitor` and `RexBiVisitor` interfaces; so any implementations of
these interfaces will have to implement this method.

- \[ [CALCITE-7125](https://issues.apache.org/jira/browse/CALCITE-7125)\]
This change brings back the original behavior of `CoreRules#INTERSECT_TO_DISTINCT` rule, which had been altered in 1.40.0
due to [CALCITE-6893](https://issues.apache.org/jira/browse/CALCITE-6893) (it removed the partial aggregate pushdown
on the union branches). The [CALCITE-6893](https://issues.apache.org/jira/browse/CALCITE-6893) behavior can still
be obtained with the new version of the rule `CoreRules#INTERSECT_TO_DISTINCT_NO_AGGREGATE_PUSHDOWN`.

- \[ [CALCITE-5716](https://issues.apache.org/jira/browse/CALCITE-5716)\]
Prior to this change, `SubQueryRemoveRule` was able to process a plan created with `RelBuilder` API containing a `Filter`
with a `RexSubQuery` with a correlated variable which was (incorrectly) not declared on the `variablesSet` of the `Filter`.
This will be no longer the case and, in this type of scenario, the `Filter` operator must declare the correlated variables
used on the sub-queries inside its condition in order to be properly handled by `SubQueryRemoveRule`.


#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-41-0 "Permalink")

- \[ [CALCITE-1466](https://issues.apache.org/jira/browse/CALCITE-1466)\] Support for `UNSIGNED` types of `TINYINT`, `SMALLINT`, `INT`, `BIGINT` in the type system
- \[ [CALCITE-7111](https://issues.apache.org/jira/browse/CALCITE-7111)\] Add an API for finding common relational sub-expressions
- \[ [CALCITE-5913](https://issues.apache.org/jira/browse/CALCITE-5913)\] Support to get functional dependency metadata in `RelMetadataQuery`
- \[ [CALCITE-7029](https://issues.apache.org/jira/browse/CALCITE-7029)\] Support DPhyp to handle various join types
- \[ [CALCITE-7189](https://issues.apache.org/jira/browse/CALCITE-7189)\] Support MySQL-style non-standard `GROUP BY`
- \[ [CALCITE-7184](https://issues.apache.org/jira/browse/CALCITE-7184)\] Support for bitwise `AND` (`&`) operator in SQL
- \[ [CALCITE-6731](https://issues.apache.org/jira/browse/CALCITE-6731)\] Support bitwise `XOR` (`^`) operator in SQL
- \[ [CALCITE-7109](https://issues.apache.org/jira/browse/CALCITE-7109)\] Support bitwise leftshift (`<<`) operator and implement `LEFT_SHIFT` function in SQL
- \[ [CALCITE-7190](https://issues.apache.org/jira/browse/CALCITE-7190)\] `FETCH` and `OFFSET` in `SortMergeRule` only supports `BIGINT`
- \[ [CALCITE-7181](https://issues.apache.org/jira/browse/CALCITE-7181)\] `FETCH` in `SortRemoveRedundantRule` do not support `BIGINT`
- \[ [CALCITE-7178](https://issues.apache.org/jira/browse/CALCITE-7178)\] `FETCH` and `OFFSET` in `EnumerableMergeUnionRule` do not support `BIGINT`
- \[ [CALCITE-7176](https://issues.apache.org/jira/browse/CALCITE-7176)\] `FETCH` and `OFFSET` in `SortMergeRule` do not support `BIGINT`
- \[ [CALCITE-7156](https://issues.apache.org/jira/browse/CALCITE-7156)\] `OFFSET` and `FETCH` in `EnumerableLimit` need to support `BIGINT`
- \[ [CALCITE-7160](https://issues.apache.org/jira/browse/CALCITE-7160)\] Simplify `AND`/`OR` with `DISTINCT` predicates to `SEARCH`
- \[ [CALCITE-7140](https://issues.apache.org/jira/browse/CALCITE-7140)\] Improve constant reduction of expressions containing `SqlRowOperator`
- \[ [CALCITE-7116](https://issues.apache.org/jira/browse/CALCITE-7116)\] Optimize queries with `GROUPING SETS` by converting them into equivalent `UNION ALL` of `GROUP BY` operations
- \[ [CALCITE-7104](https://issues.apache.org/jira/browse/CALCITE-7104)\] Remove duplicate sort keys
- \[ [CALCITE-7095](https://issues.apache.org/jira/browse/CALCITE-7095)\] Allow `MAP<VARIANT, X>` to be indexed by any type of key
- \[ [CALCITE-7090](https://issues.apache.org/jira/browse/CALCITE-7090)\] Support `LogicalRepeatUnion` in `RelHomogeneousShuttle`
- \[ [CALCITE-7089](https://issues.apache.org/jira/browse/CALCITE-7089)\] Implement a rule for converting a `RIGHT JOIN` to a `LEFT JOIN`
- \[ [CALCITE-7077](https://issues.apache.org/jira/browse/CALCITE-7077)\] Implement a rule to rewrite `FULL JOIN` as `LEFT JOIN` and `RIGHT JOIN`
- \[ [CALCITE-7086](https://issues.apache.org/jira/browse/CALCITE-7086)\] Implement a rule that performs the inverse operation of `AggregateCaseToFilterRule`
- \[ [CALCITE-7068](https://issues.apache.org/jira/browse/CALCITE-7068)\] ElasticSearch adapter support `LIKE` operator
- \[ [CALCITE-7042](https://issues.apache.org/jira/browse/CALCITE-7042)\] Eliminate nested `TRIM` calls, exploiting the fact that `TRIM` is idempotent
- \[ [CALCITE-6763](https://issues.apache.org/jira/browse/CALCITE-6763)\] Optimize logic to select the tiles with the fewest rows
- \[ [CALCITE-5094](https://issues.apache.org/jira/browse/CALCITE-5094)\] Calcite JDBC Adapter and Avatica should support MySQL `UNSIGNED` types of `TINYINT`, `SMALLINT`, `INT`, `BIGINT`
- \[ [CALCITE-7080](https://issues.apache.org/jira/browse/CALCITE-7080)\] Support unparse when operator is `UPDATE`
- \[ [CALCITE-7021](https://issues.apache.org/jira/browse/CALCITE-7021)\] Support parse `CAST('1' AS INTERVAL)`
- \[ [CALCITE-7249](https://issues.apache.org/jira/browse/CALCITE-7249)\] Support unsigned types in `RelMdSize`
- \[ [CALCITE-1440](https://issues.apache.org/jira/browse/CALCITE-1440)\] Add Combine `RelNode` for converting multiple SQL statements to unified `RelNode` Tree

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-41-0 "Permalink")

- \[ [CALCITE-7183](https://issues.apache.org/jira/browse/CALCITE-7183)\] Upgrade Avatica to 1.27.0
- \[ [CALCITE-7175](https://issues.apache.org/jira/browse/CALCITE-7175)\] Update Jackson from 2.15.0 to 2.18.4.1
- \[ [CALCITE-7177](https://issues.apache.org/jira/browse/CALCITE-7177)\] Upgrade Guava from 33.4.0-jre to 33.4.8-jre
- \[ [CALCITE-7180](https://issues.apache.org/jira/browse/CALCITE-7180)\] Upgrade Github actions versions
- \[ [CALCITE-7163](https://issues.apache.org/jira/browse/CALCITE-7163)\] Upgrade Sonar Gradle Plugin to version 6.3.1.5724
- \[ [CALCITE-7108](https://issues.apache.org/jira/browse/CALCITE-7108)\] Upgrade aggdesigner-algorithm from 6.0 to 6.1
- \[ [CALCITE-7098](https://issues.apache.org/jira/browse/CALCITE-7098)\] Update json-smart from 2.3 to 2.6.0
- \[ [CALCITE-7097](https://issues.apache.org/jira/browse/CALCITE-7097)\] Update commons-lang to 3.18.0
- Bump rexml from 3.4.1 to 3.4.2 in /site
- Bump nokogiri from 1.18.8 to 1.18.9 in /site

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-41-0 "Permalink")

- \[ [CALCITE-7194](https://issues.apache.org/jira/browse/CALCITE-7194)\] Simplify comparisons between function calls and literals to `SEARCH`
- \[ [CALCITE-7240](https://issues.apache.org/jira/browse/CALCITE-7240)\] Handle `SEARCH` in DateRangeRules
- \[ [CALCITE-7228](https://issues.apache.org/jira/browse/CALCITE-7228)\] Validator rejects legal `ASOF JOIN` program
- \[ [CALCITE-7034](https://issues.apache.org/jira/browse/CALCITE-7034)\] `IllegalArgumentException` when correlate subQuery in `ON` clause and use rightside columns
- \[ [CALCITE-7070](https://issues.apache.org/jira/browse/CALCITE-7070)\] `FILTER_REDUCE_EXPRESSIONS` crashes on expression `BETWEEN ( NULL) AND X`
- \[ [CALCITE-7201](https://issues.apache.org/jira/browse/CALCITE-7201)\] `ClassCastException` in `RexInterpreter#search` with different `NUMERIC` values
- \[ [CALCITE-7238](https://issues.apache.org/jira/browse/CALCITE-7238)\] Query that creates a `ROW` value triggers an assertion failure in `SqlToRelConverter`
- \[ [CALCITE-6028](https://issues.apache.org/jira/browse/CALCITE-6028)\] Join on with more than 20 in conditions will report a null pointer error
- \[ [CALCITE-7230](https://issues.apache.org/jira/browse/CALCITE-7230)\] Compiler rejects comparisons between `NULL` and a `ROW` value
- \[ [CALCITE-7225](https://issues.apache.org/jira/browse/CALCITE-7225)\] Comparing `ROW` values with different lengths causes an `IndexOutOfBoudsException`
- \[ [CALCITE-7222](https://issues.apache.org/jira/browse/CALCITE-7222)\] `SortRemoveDuplicateKeysRule` miss fetch and offset information
- \[ [CALCITE-7010](https://issues.apache.org/jira/browse/CALCITE-7010)\] The well-known count bug
- \[ [CALCITE-5743](https://issues.apache.org/jira/browse/CALCITE-5743)\] Query gives incorrect result when `COUNT` appears in the correlated subquery select list
- \[ [CALCITE-5421](https://issues.apache.org/jira/browse/CALCITE-5421)\] `SqlToRelConverter` should populate `correlateId` for join with correlated query in `HAVING` condition
- \[ [CALCITE-5199](https://issues.apache.org/jira/browse/CALCITE-5199)\] The `leastRestrictiveStructuredType` method should reserve the `StructKind` instead of override it to `FULLY_QUALIFIED`
- \[ [CALCITE-5568](https://issues.apache.org/jira/browse/CALCITE-5568)\] Decorrelate will fail if the `RelNode` tree has `LogicalValues`
- \[ [CALCITE-7231](https://issues.apache.org/jira/browse/CALCITE-7231)\] Validator crashes with `AssertionFailure` on query with `ROW` and `IN`
- \[ [CALCITE-7220](https://issues.apache.org/jira/browse/CALCITE-7220)\] `RelToSqlConverter` throws exception for `UPDATE` with self-referencing column in `SET`
- \[ [CALCITE-7218](https://issues.apache.org/jira/browse/CALCITE-7218)\] `ArrowSet` needs to maintain a minimal set of functional dependencies
- \[ [CALCITE-7217](https://issues.apache.org/jira/browse/CALCITE-7217)\] `LATERAL` is lost after validation
- \[ [CALCITE-7216](https://issues.apache.org/jira/browse/CALCITE-7216)\] `SqlOperator.inferReturnType` throws the wrong exception on error
- \[ [CALCITE-7212](https://issues.apache.org/jira/browse/CALCITE-7212)\] `VariablesSet` of `Project` is lost during `RelStructuredTypeFlattener` processing
- \[ [CALCITE-7210](https://issues.apache.org/jira/browse/CALCITE-7210)\] `BINARY` literal values may not match their type
- \[ [CALCITE-7195](https://issues.apache.org/jira/browse/CALCITE-7195)\] `COALESCE` type inference rejects legal arguments
- \[ [CALCITE-7193](https://issues.apache.org/jira/browse/CALCITE-7193)\] In an aggregation validator treats lambda variable names as column names
- \[ [CALCITE-7192](https://issues.apache.org/jira/browse/CALCITE-7192)\] `AggregateReduceFunctionsRule` lost `FILTER` condition in `STDDEV`/`VAR` function decomposition
- \[ [CALCITE-7191](https://issues.apache.org/jira/browse/CALCITE-7191)\] Hypergraph creation with incorrect hyperedges
- \[ [CALCITE-7186](https://issues.apache.org/jira/browse/CALCITE-7186)\] Add mapping from `Character[]` to `VARCHAR` in Java `UDF`
- \[ [CALCITE-7159](https://issues.apache.org/jira/browse/CALCITE-7159)\] `LogicalAsofJoin``deepEquals` can throw for legal expressions
- \[ [CALCITE-7158](https://issues.apache.org/jira/browse/CALCITE-7158)\] `NULL` cannot be cast to `UUID`
- \[ [CALCITE-7157](https://issues.apache.org/jira/browse/CALCITE-7157)\] PostgreSQL does not support string literal in `ORDER BY` clause
- \[ [CALCITE-7154](https://issues.apache.org/jira/browse/CALCITE-7154)\] When the `offset` or `limit` of a `SORT` operation is of type `BIGINT` row count calculation overflows
- \[ [CALCITE-4617](https://issues.apache.org/jira/browse/CALCITE-4617)\] Wrong `offset` when `SortJoinTransposeRule` pushes a `Sort` with an `offset`
- \[ [CALCITE-7149](https://issues.apache.org/jira/browse/CALCITE-7149)\] Constant `TIMESTAMPADD` expression causes assertion failure in validator
- \[ [CALCITE-7147](https://issues.apache.org/jira/browse/CALCITE-7147)\] Comparison of `INTEGER` and `BOOLEAN` produces strange results
- \[ [CALCITE-7146](https://issues.apache.org/jira/browse/CALCITE-7146)\] `TIMESTAMPDIFF` accepts arguments with mismatched types
- \[ [CALCITE-7144](https://issues.apache.org/jira/browse/CALCITE-7144)\] `LIMIT` should not be pushed through projections containing window functions
- \[ [CALCITE-7135](https://issues.apache.org/jira/browse/CALCITE-7135)\] `SqlToRelConverter` throws `AssertionError` on `ARRAY` subquery order by a field that is not present on the final projection
- \[ [CALCITE-7134](https://issues.apache.org/jira/browse/CALCITE-7134)\] Incorrect type inference for some aggregate functions when groupSets contains `{}`
- \[ [CALCITE-7132](https://issues.apache.org/jira/browse/CALCITE-7132)\] Inconsistency with type coercion and character types
- \[ [CALCITE-7131](https://issues.apache.org/jira/browse/CALCITE-7131)\] `SqlImplementor.toSql` does not handle `Geometry` literals
- \[ [CALCITE-7128](https://issues.apache.org/jira/browse/CALCITE-7128)\] `SqlImplementor.toSql` does not handle `UUID` literals
- \[ [CALCITE-7127](https://issues.apache.org/jira/browse/CALCITE-7127)\] `RelToSqlConverter` corrupts condition inside an anti-join with `WHERE NOT EXISTS`
- \[ [CALCITE-7126](https://issues.apache.org/jira/browse/CALCITE-7126)\] The calculation result of grouping function is wrong
- \[ [CALCITE-7125](https://issues.apache.org/jira/browse/CALCITE-7125)\] Impossible to get a plan with partial aggregate push-down via `IntersectToDistinctRule`
- \[ [CALCITE-7118](https://issues.apache.org/jira/browse/CALCITE-7118)\] Rex-to-Lix Translation fails to correctly truncate/pad `RexDynamicParam` values
- \[ [CALCITE-7114](https://issues.apache.org/jira/browse/CALCITE-7114)\] Invalid unparse for cast to array type in Spark
- \[ [CALCITE-7113](https://issues.apache.org/jira/browse/CALCITE-7113)\] `RelJson` cannot serialize `RexLambda`
- \[ [CALCITE-7112](https://issues.apache.org/jira/browse/CALCITE-7112)\] Correlation variable in `HAVING` clause causes `UnsupportedOperationException` in RelToSql conversion
- \[ [CALCITE-7105](https://issues.apache.org/jira/browse/CALCITE-7105)\] `ARRAY_CONCAT` should only accept arguments with type `ARRAY`
- \[ [CALCITE-7102](https://issues.apache.org/jira/browse/CALCITE-7102)\] Should return Presto `SqlConformance` when `DatabaseProduct` is Presto
- \[ [CALCITE-7096](https://issues.apache.org/jira/browse/CALCITE-7096)\] Invalid unparse for `EXTRACT` in StarRocks/Doris
- \[ [CALCITE-7073](https://issues.apache.org/jira/browse/CALCITE-7073)\] If the Java return type of a `UDF` is `ByteString`, Calcite should deduce that the SQL type is `VARBINARY`
- \[ [CALCITE-5583](https://issues.apache.org/jira/browse/CALCITE-5583)\] JDBC adapter does not generate `SELECT *` when duplicate field names
- \[ [CALCITE-7074](https://issues.apache.org/jira/browse/CALCITE-7074)\] `IN`-list that includes `NULL` converted to `Values` return wrong result
- \[ [CALCITE-7076](https://issues.apache.org/jira/browse/CALCITE-7076)\] `IN`-list that includes `NULL` converted to `Values` throws exception when there is a non-null column being compared with a `NULL` value
- \[ [CALCITE-7094](https://issues.apache.org/jira/browse/CALCITE-7094)\] Using a type alias as a constructor function causes a validator assertion failure
- \[ [CALCITE-7088](https://issues.apache.org/jira/browse/CALCITE-7088)\] Multiple consecutive `%` in the string matched by `LIKE` should simplify to a single `%`
- \[ [CALCITE-7083](https://issues.apache.org/jira/browse/CALCITE-7083)\] `RelMdDistinctRowCount` aggregates implementation problems
- \[ [CALCITE-7081](https://issues.apache.org/jira/browse/CALCITE-7081)\] Invalid unparse for cast to nested type in ClickHouse
- \[ [CALCITE-7079](https://issues.apache.org/jira/browse/CALCITE-7079)\] MongoDB Adapter unable to translate multiple `NOT EQUALS` expressions combined with `AND`
- \[ [CALCITE-7070](https://issues.apache.org/jira/browse/CALCITE-7070)\] `FILTER_REDUCE_EXPRESSIONS` crashes on expression `BETWEEN ( NULL) AND X`
- \[ [CALCITE-7069](https://issues.apache.org/jira/browse/CALCITE-7069)\] Invalid unparse for `INT UNSIGNED` and `BIGINT UNSIGNED` in MysqlSqlDialect
- \[ [CALCITE-7067](https://issues.apache.org/jira/browse/CALCITE-7067)\] Maximum precision of `UNSIGNED BIGINT` type in MysqlSqlDialect should be 20
- \[ [CALCITE-7066](https://issues.apache.org/jira/browse/CALCITE-7066)\] `UNSIGNED` types are not supported by databases like Oracle, SQL Server
- \[ [CALCITE-7065](https://issues.apache.org/jira/browse/CALCITE-7065)\] `CoreRules.PROJECT_REDUCE_EXPRESSIONS` crashes when applied to a lambda
- \[ [CALCITE-7009](https://issues.apache.org/jira/browse/CALCITE-7009)\] `AssertionError` when converting query containing multiple correlated subqueries referencing different tables in `FROM`
- \[ [CALCITE-7064](https://issues.apache.org/jira/browse/CALCITE-7064)\] Test introduced in `CALCITE-7009` breaks the build for main
- \[ [CALCITE-7062](https://issues.apache.org/jira/browse/CALCITE-7062)\] Row type of SetOp may ignore a column’s nullability
- \[ [CALCITE-7061](https://issues.apache.org/jira/browse/CALCITE-7061)\] `RelMdSize` does not handle nested `ARRAY`/`MAP` constructor calls
- \[ [CALCITE-7058](https://issues.apache.org/jira/browse/CALCITE-7058)\] Decorrelator may produce different column names
- \[ [CALCITE-7056](https://issues.apache.org/jira/browse/CALCITE-7056)\] Convert `RelNode` to Sql failed when the `RelNode` includes quantify operators
- \[ [CALCITE-7055](https://issues.apache.org/jira/browse/CALCITE-7055)\] Invalid unparse for cast to array type in StarRocks
- \[ [CALCITE-7054](https://issues.apache.org/jira/browse/CALCITE-7054)\] Runtime conversion of `DECIMAL MULTISET` to `INT MULTISET` or `DECIMAL ARRAY` to `INT MULTISET` fails with a `ClassCastException`
- \[ [CALCITE-7052](https://issues.apache.org/jira/browse/CALCITE-7052)\] When conformance specifies `isGroupbyAlias = true` the validator rejects legal queries
- \[ [CALCITE-7051](https://issues.apache.org/jira/browse/CALCITE-7051)\] `NATURAL JOIN` and `JOIN` with `USING` does not match the appropriate columns when `caseSensitive` is `false`
- \[ [CALCITE-7072](https://issues.apache.org/jira/browse/CALCITE-7072)\] Validator should not insert aliases on subexpressions
- \[ [CALCITE-7162](https://issues.apache.org/jira/browse/CALCITE-7162)\] `AggregateMergeRule` type mismatch on `MIN`/`MAX`
- \[ [CALCITE-4756](https://issues.apache.org/jira/browse/CALCITE-4756)\] When subquery include `NULL` value, Calcite should return the right result
- \[ [CALCITE-7050](https://issues.apache.org/jira/browse/CALCITE-7050)\] Invalid unparse for `FULL JOIN` in MySQLDialect
- \[ [CALCITE-7048](https://issues.apache.org/jira/browse/CALCITE-7048)\] Derived types with `FLOAT` type arguments are handled incorrectly in Presto
- \[ [CALCITE-7047](https://issues.apache.org/jira/browse/CALCITE-7047)\] Improve Volcano planner selection of sort conversion rules
- \[ [CALCITE-7044](https://issues.apache.org/jira/browse/CALCITE-7044)\] Add internal operator `CAST NOT NULL` to enhance rewrite `COALESCE` operator
- \[ [CALCITE-7233](https://issues.apache.org/jira/browse/CALCITE-7233)\] `SqlToRelConverter` throws `UnsupportedOperationException` after the introduction of the internal `CAST_NOT_NULL` operator
- \[ [CALCITE-7043](https://issues.apache.org/jira/browse/CALCITE-7043)\] Type inferred for `SqlItemOperator` has incorrect nullability
- \[ [CALCITE-7032](https://issues.apache.org/jira/browse/CALCITE-7032)\] Simplify `NULL > ALL (ARRAY[1,2,NULL])` to `NULL`
- \[ [CALCITE-7024](https://issues.apache.org/jira/browse/CALCITE-7024)\] Decorrelator does not always produce a query with the same type signature
- \[ [CALCITE-6952](https://issues.apache.org/jira/browse/CALCITE-6952)\] JDBC adapter for StarRocks generates incorrect SQL for `REAL` datatype
- \[ [CALCITE-6950](https://issues.apache.org/jira/browse/CALCITE-6950)\] Use `ANY` operator to check if an element exists in an array throws exception
- \[ [CALCITE-6386](https://issues.apache.org/jira/browse/CALCITE-6386)\] Elasticsearch adapter throws `NullPointerException` when used with model.json and no username, password or pathPrefix
- \[ [CALCITE-6080](https://issues.apache.org/jira/browse/CALCITE-6080)\] The simplified form after applying `AggregateReduceFunctionsRule` is giving wrong results for `STDDEV`, `Covariance` with `double` and `decimal` types
- \[ [CALCITE-4993](https://issues.apache.org/jira/browse/CALCITE-4993)\] Simplify `EQUALS` or `NOT-EQUALS` with other number comparison
- \[ [CALCITE-4915](https://issues.apache.org/jira/browse/CALCITE-4915)\] Test for query with unqualified common column and `NATURAL JOIN`
- \[ [CALCITE-4723](https://issues.apache.org/jira/browse/CALCITE-4723)\] Check whether JDBC adapter generates `GROUP BY ()` against Oracle, DB2, MSSQL
- \[ [CALCITE-1583](https://issues.apache.org/jira/browse/CALCITE-1583)\] Wrong results for query with correlated subqueries with aggregate subquery expression
- \[ [CALCITE-7053](https://issues.apache.org/jira/browse/CALCITE-7053)\] In `HepPlanner`, move down the collectGarbage to topological order for better optimizer performance
- \[ [CALCITE-7049](https://issues.apache.org/jira/browse/CALCITE-7049)\] When performing garbage collection, `HepPlanner` should clear the metadata cache
- \[ [CALCITE-7221](https://issues.apache.org/jira/browse/CALCITE-7221)\] Make `HepPlanner.getVertexParents()` protected
- \[ [CALCITE-7219](https://issues.apache.org/jira/browse/CALCITE-7219)\] Enhance functional dependency computation performance using the existing caching mechanisms
- \[ [CALCITE-7215](https://issues.apache.org/jira/browse/CALCITE-7215)\] Simplify `SEARCH` operand in `RexSimplify.simplifySearch`
- \[ [CALCITE-7203](https://issues.apache.org/jira/browse/CALCITE-7203)\] `IntersectToSemiJoinRule` should compute once the join keys and reuse them to avoid duplicates
- \[ [CALCITE-7199](https://issues.apache.org/jira/browse/CALCITE-7199)\] Improve column uniqueness computation for Join
- \[ [CALCITE-7174](https://issues.apache.org/jira/browse/CALCITE-7174)\] Improve lossless cast detection for numeric types
- \[ [CALCITE-7173](https://issues.apache.org/jira/browse/CALCITE-7173)\] Improve `RelMdDistinctRowCount` estimation for lossless casts
- \[ [CALCITE-7155](https://issues.apache.org/jira/browse/CALCITE-7155)\] Some optimization can be done according to error prone suggestions
- \[ [CALCITE-7153](https://issues.apache.org/jira/browse/CALCITE-7153)\] Mixed wildcards of `_` and `%` need to be simplified in `LIKE` operator
- \[ [CALCITE-7141](https://issues.apache.org/jira/browse/CALCITE-7141)\] Add missing getter to `FunctionSqlType`
- \[ [CALCITE-7130](https://issues.apache.org/jira/browse/CALCITE-7130)\] `DiffRepository` does not enforce any order on XML resources
- \[ [CALCITE-5716](https://issues.apache.org/jira/browse/CALCITE-5716)\] Two level nested correlated subquery translates to incorrect `ON` condition
- \[ [CALCITE-3190](https://issues.apache.org/jira/browse/CALCITE-3190)\] ElasticsearchJson throws `Exception` when `visitMappingProperties`
- Add getter method for `Uncollect.itemAliases`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-41-0 "Permalink")

- \[ [CALCITE-7129](https://issues.apache.org/jira/browse/CALCITE-7129)\] Drop `@RuleConfig` annotation used in Quidem tests
- \[ [CALCITE-7060](https://issues.apache.org/jira/browse/CALCITE-7060)\] Enable dumping high-level plans in quidem tests
- \[ [CALCITE-7179](https://issues.apache.org/jira/browse/CALCITE-7179)\] Improve error message for QuidemTest
- \[ [CALCITE-7235](https://issues.apache.org/jira/browse/CALCITE-7235)\] Support Flexible HEP and Volcano Planner Rule Configuration in Quidem Tests
- \[ [CALCITE-7253](https://issues.apache.org/jira/browse/CALCITE-7253)\] Add default programs like `DecorrelateProgram` to the Hep-Rule Test
- \[ [CALCITE-7071](https://issues.apache.org/jira/browse/CALCITE-7071)\] Add test for replacing `JOIN` node with its child node when `JOIN` condition is `false`
- \[ [CALCITE-7161](https://issues.apache.org/jira/browse/CALCITE-7161)\] Calcite-snapshots Jenkins builds fail due to corrupted caches
- Enable some disabled quidem tests

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-41-0 "Permalink")

- \[ [CALCITE-7137](https://issues.apache.org/jira/browse/CALCITE-7137)\] Small nit: method name wrong in documentation for hint strategy
- Add link to new blog post on Calcite constant folding
- Update ASF logo links
- Fix aspect ratio for ASF logos

## [1.40.0](https://github.com/apache/calcite/releases/tag/calcite-1.40.0) / 2025-05-28 [Permalink](https://calcite.apache.org/docs/history.html\#v1-40-0 "Permalink")

This release comes 2 months after [1.39.0](https://calcite.apache.org/docs/history.html#v1-39-0),
contains contributions from 20 contributors, and resolves 102 issues.

Highlights include
the addition of several improvements and additional optimization rules, notably advanced set operation handling with new rules for converting INTERSECT to semi-joins and EXISTS subqueries, MINUS to anti-joins and filters, and optimizing UNIONs with common sources,
join optimization is improved through predicate expansion from disjunctions and specialized handling of complex join conditions,
additional optimizations include new rules for MIN/MAX aggregates and smarter filter-sort interactions,
addition of Doris, DuckDB, SQLite, and Trino dialects, as well as improved support for ClickHouse,
support for aliases referencing lateral columns,
support for defining which rule sets to apply for individual Quidem tests.

Contributors to this release:
Alessandro Solimando (release manager),
Chuxin Chen,
Evgeniy Stanilovsky,
Julian Hyde,
Juntao Zhang,
Kurt Alfred Kluever,
Mihai Budiu,
Niels Pardon,
Ruben Quesada Lopez,
Sergey Nuyanzin,
Silun Dong,
Stamatis Zampetakis,
suibianwanwan,
sulees,
Ulrich Kramer,
wangdiao,
Wei Zhou,
Xiong Duan,
Yu Xu,
Zhen Chen,
zhuyufeng

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 23;
Guava versions 21.0 to 33.3.0-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-40-0 "Permalink")

- \[ [CALCITE-6920](https://issues.apache.org/jira/browse/CALCITE-6920)\]
The fix introduces a new property of the type system called `mapKeysCanBeNullable()` which indicates if keys in a map can be nullable.

- \[ [CALCITE-6901](https://issues.apache.org/jira/browse/CALCITE-6901)\]
changes the way `SINGLE_VALUE` is rewritten `MySQL` dialect leading to a different exception thrown in case of multiple values.
Before: `SQL error [1140] [42000]: In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column '*****'; this is incompatible with sql_mode=only_full_group_by`
After: `SQL error [1242] [21000]: Subquery returns more than 1 row`

- \[ [CALCITE-6944](https://issues.apache.org/jira/browse/CALCITE-6944)\]
`toSqlString` now doesn’t add an extra pair of parentheses for table functions.
Before: `F(A => (TABLE T PARTITION BY F1 ORDER BY F2), B => 1)`
After: `F(A => TABLE T PARTITION BY F1 ORDER BY F2, B => 1)`

- \[ [CALCITE-6964](https://issues.apache.org/jira/browse/CALCITE-6964)\]
`SqlDelete#getOperandList` now returns the elements from the source `SELECT` component.

- \[ [CALCITE-6989](https://issues.apache.org/jira/browse/CALCITE-6989)\]
`RexBuilder#makeIn` now creates a `SEARCH` expression for `ARRAY` literals, similarly to what it does for `ROW` literals.
Taking `RexBuilder#makeIn($0, ARRAY [100, 200], ARRAY [300, 400])` as an example you have:
Before: `OR(=($0, ARRAY(100, 200)), =($0, ARRAY(300, 400)))`
After: `SEARCH($0, Sarg[[100:INTEGER, 200:INTEGER]:INTEGER NOT NULL ARRAY, [300:INTEGER, 400:INTEGER]:INTEGER NOT NULL ARRAY]:INTEGER NOT NULL ARRAY)`

- \[ [CALCITE-6959](https://issues.apache.org/jira/browse/CALCITE-6959)\]
- \[ [CALCITE-6961](https://issues.apache.org/jira/browse/CALCITE-6961)\]
Addition of non-default methods for `LogicalAsofJoin` and `LogicalRepeatUnion`, respectively, to `RelShuttle`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-40-0 "Permalink")

- \[ [CALCITE-6878](https://issues.apache.org/jira/browse/CALCITE-6878)\] Implement `FilterSortTransposeRule`
- \[ [CALCITE-6836](https://issues.apache.org/jira/browse/CALCITE-6836)\] Add Rule to convert `INTERSECT` to `EXISTS`
- \[ [CALCITE-6900](https://issues.apache.org/jira/browse/CALCITE-6900)\] Support `Char` type cast in ClickHouse Dialect
- \[ [CALCITE-6825](https://issues.apache.org/jira/browse/CALCITE-6825)\] Add support for `ALL`, `SOME`, `ANY` in `RelToSqlConverter`
- \[ [CALCITE-6888](https://issues.apache.org/jira/browse/CALCITE-6888)\] Doris dialect implementation
- \[ [CALCITE-6820](https://issues.apache.org/jira/browse/CALCITE-6820)\] Trino dialect implementation
- \[ [CALCITE-6891](https://issues.apache.org/jira/browse/CALCITE-6891)\] Implement `IntersectReorderRule`
- \[ [CALCITE-6880](https://issues.apache.org/jira/browse/CALCITE-6880)\] Implement `IntersectToSemiJoinRule`
- \[ [CALCITE-6893](https://issues.apache.org/jira/browse/CALCITE-6893)\] Remove agg from Union children in `IntersectToDistinctRule`
- \[ [CALCITE-6948](https://issues.apache.org/jira/browse/CALCITE-6948)\] Implement `MinusToAntiJoinRule`
- \[ [CALCITE-6927](https://issues.apache.org/jira/browse/CALCITE-6927)\] Add rule for join condition remove `IS NOT DISTINCT FROM`
- \[ [CALCITE-6930](https://issues.apache.org/jira/browse/CALCITE-6930)\] Implementing `JoinConditionOrExpansionRule`
- \[ [CALCITE-6914](https://issues.apache.org/jira/browse/CALCITE-6914)\] Expand join-dependent predicates from disjunction
- \[ [CALCITE-6953](https://issues.apache.org/jira/browse/CALCITE-6953)\] Extend `UnionEliminatorRule` to support `Intersect` and `Minus`
- \[ [CALCITE-6966](https://issues.apache.org/jira/browse/CALCITE-6966)\] Change `JoinConditionOrExpansionRule` name and accept more predicates that will allow the expansion to be performed
- \[ [CALCITE-6969](https://issues.apache.org/jira/browse/CALCITE-6969)\] Support ClickHouse in `SqlLibrary`
- \[ [CALCITE-6973](https://issues.apache.org/jira/browse/CALCITE-6973)\] Add rule to convert `Minus` to `Filter`
- \[ [CALCITE-6988](https://issues.apache.org/jira/browse/CALCITE-6988)\] DuckDB dialect implementation
- \[ [CALCITE-6946](https://issues.apache.org/jira/browse/CALCITE-6946)\] Expand predicates from disjunction for inputs of Join
- \[ [CALCITE-6939](https://issues.apache.org/jira/browse/CALCITE-6939)\] Add support for Lateral Column Alias
- \[ [CALCITE-6985](https://issues.apache.org/jira/browse/CALCITE-6985)\] Add rule to transform `MIN`/`MAX` with `ORDER BY` and `LIMIT 1`
- \[ [CALCITE-7000](https://issues.apache.org/jira/browse/CALCITE-7000)\] Extend `IntersectToSemiJoinRule` to support n-way inputs
- \[ [CALCITE-6997](https://issues.apache.org/jira/browse/CALCITE-6997)\] SQLite dialect implementation
- \[ [CALCITE-7002](https://issues.apache.org/jira/browse/CALCITE-7002)\] Create an optimization rule to eliminate `UNION` from the same source with different filters
- \[ [CALCITE-7019](https://issues.apache.org/jira/browse/CALCITE-7019)\] Simplify `NULL IN (20, 10)` to `NULL`
- \[ [CALCITE-7008](https://issues.apache.org/jira/browse/CALCITE-7008)\] Extend `MinusToAntiJoinRule` to support n-way inputs
- \[ [CALCITE-6951](https://issues.apache.org/jira/browse/CALCITE-6951)\] Add `STRING_TO_ARRAY` function(enabled in PostgreSQL Library)
- \[ [CALCITE-7014](https://issues.apache.org/jira/browse/CALCITE-7014)\] Support `EQUAL`/`GreaterThanOrEqual`/`LessThanOrEqual` expressions to `RexNode` In `CalcitePrepare`
- \[ [CALCITE-7030](https://issues.apache.org/jira/browse/CALCITE-7030)\] Enhance `TopologicalOrderIterator` to support `BOTTOM_UP`
- \[ [CALCITE-6887](https://issues.apache.org/jira/browse/CALCITE-6887)\] `ReduceExpressionsRule` applied to ‘`IN` subquery’ should make the values distinct if the subquery is a `Values` composed of literals

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-40-0 "Permalink")

- \[ [CALCITE-6975](https://issues.apache.org/jira/browse/CALCITE-6975)\] Upgrade `Quidem` version to 0.12
- Bump `nokogiri` from 1.18.2 to 1.18.8 in `/site`
- Bump `json` from 2.10.1 to 2.10.2 in `/site`
- \[ [CALCITE-7018](https://issues.apache.org/jira/browse/CALCITE-7018)\] Upgrade `Janino` from 3.1.11 to 3.1.12

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-40-0 "Permalink")

- \[ [CALCITE-6875](https://issues.apache.org/jira/browse/CALCITE-6875)\] `EnumerableFilterRule`/`EnumerableProjectRule` should not convert a `Logical Filter`/`Project` to `Enumerable Filter`/`Project` when it contains Subquery
- \[ [CALCITE-6892](https://issues.apache.org/jira/browse/CALCITE-6892)\] `CHAR_LENGTH` Function is not recognized in DerbySQL
- \[ [CALCITE-6901](https://issues.apache.org/jira/browse/CALCITE-6901)\] `SINGLE_VALUE` rewrite to wrong sql in MySQL dialect
- \[ [CALCITE-6903](https://issues.apache.org/jira/browse/CALCITE-6903)\] `CalciteSchema#getSubSchemaMap` must consider implicit sub-schemas
- \[ [CALCITE-6897](https://issues.apache.org/jira/browse/CALCITE-6897)\] `AbstractConverter` of root node is not needed in topdown mode
- \[ [CALCITE-6431](https://issues.apache.org/jira/browse/CALCITE-6431)\] Implement the `SINGLE_VALUE` aggregation in `HiveSqlDialect` And `SparkSQLDialect`
- \[ [CALCITE-6910](https://issues.apache.org/jira/browse/CALCITE-6910)\] `RelToSql` does not handle `ASOF` joins
- \[ [CALCITE-6913](https://issues.apache.org/jira/browse/CALCITE-6913)\] Some casts inserted by type coercion do not have source position information
- \[ [CALCITE-6834](https://issues.apache.org/jira/browse/CALCITE-6834)\] In query that applies `COALESCE` to nullable `SUM`,`EnumerableProjectToCalcRule` throws `AssertionError`
- \[ [CALCITE-6920](https://issues.apache.org/jira/browse/CALCITE-6920)\] The type derived for a cast to `INT ARRAY` always has non-nullable elements
- \[ [CALCITE-2109](https://issues.apache.org/jira/browse/CALCITE-2109)\] MongoAdapter: Support `in` condition with `and` condition
- \[ [CALCITE-6911](https://issues.apache.org/jira/browse/CALCITE-6911)\] `SqlItemOperator.inferReturnType` throws `AssertionError` for out of bounds accesses
- \[ [CALCITE-6909](https://issues.apache.org/jira/browse/CALCITE-6909)\] ClickHouse dialect should limit the Precision and Scale of the `Decimal` type to be within 76
- \[ [CALCITE-6931](https://issues.apache.org/jira/browse/CALCITE-6931)\] `STARTSWITH`/`ENDSWITH` in SPARK should not convert to `STARTS_WITH`/`ENDS_WITH`
- \[ [CALCITE-6835](https://issues.apache.org/jira/browse/CALCITE-6835)\] Invalid unparse for `IS TRUE`,`IS FALSE`,`IS NOT TRUE` and `IS NOT FALSE` in `StarRocksDialect`
- \[ [CALCITE-6904](https://issues.apache.org/jira/browse/CALCITE-6904)\] `IS_NOT_DISTINCT_FROM` is incorrectly handled by `EnumerableJoinRule`
- \[ [CALCITE-6936](https://issues.apache.org/jira/browse/CALCITE-6936)\] Table function parameter matching should always be case-insensitive
- \[ [CALCITE-6923](https://issues.apache.org/jira/browse/CALCITE-6923)\] `REGEXP_REPLACE_PG_...`: backward references behave differently than in postgres
- \[ [CALCITE-6921](https://issues.apache.org/jira/browse/CALCITE-6921)\] `REGEXP_REPLACE` with empty string causes `Exception`
- \[ [CALCITE-6943](https://issues.apache.org/jira/browse/CALCITE-6943)\] Calcite JDBC adapter for Hive should translate `APPROX_COUNT_DISTINCT` to `COUNT DISTINCT`
- \[ [CALCITE-6938](https://issues.apache.org/jira/browse/CALCITE-6938)\] Support zero value creation of nested data types
- \[ [CALCITE-6941](https://issues.apache.org/jira/browse/CALCITE-6941)\] `Array`/`Map` value constructor is unparsed incorrectly in ClickHouse
- \[ [CALCITE-6945](https://issues.apache.org/jira/browse/CALCITE-6945)\] Use `LITERAL_AGG` to simplify `SubQueryRemoveRule` by avoiding the extra Project
- \[ [CALCITE-6949](https://issues.apache.org/jira/browse/CALCITE-6949)\] ClickHouse not support `floor``date` to `SECOND`/`MILLISECOND`/`MICROSECOND`/`NANOSECOND`
- \[ [CALCITE-6840](https://issues.apache.org/jira/browse/CALCITE-6840)\] Hive/Phoenix Dialect should not cast to `REAL` type directly
- \[ [CALCITE-6959](https://issues.apache.org/jira/browse/CALCITE-6959)\] Support `LogicalAsofJoin` in `RelShuttle`
- \[ [CALCITE-6958](https://issues.apache.org/jira/browse/CALCITE-6958)\] JDBC adapter for MySQL not support `floor``date` to `MILLISECOND`/`MICROSECOND`
- \[ [CALCITE-6954](https://issues.apache.org/jira/browse/CALCITE-6954)\] `SqlTypeFactoryImpl#leastRestrictive` returns non-canonical collection types
- \[ [CALCITE-6961](https://issues.apache.org/jira/browse/CALCITE-6961)\] Support `LogicalRepeatUnion` in `RelShuttle`
- \[ [CALCITE-6955](https://issues.apache.org/jira/browse/CALCITE-6955)\] `PruneEmptyRules` does not handle the all attribute of `SetOp` correctly
- \[ [CALCITE-2636](https://issues.apache.org/jira/browse/CALCITE-2636)\] SQL parser has quadratic running time when SQL string is very large
- \[ [CALCITE-6944](https://issues.apache.org/jira/browse/CALCITE-6944)\] Align `toSqlString` with SQL std for Table Args in PTF
- \[ [CALCITE-6964](https://issues.apache.org/jira/browse/CALCITE-6964)\] `SqlDelete#getOperandList` return operands’ both order and size not match with `SqlDelete#setOperand`
- \[ [CALCITE-6967](https://issues.apache.org/jira/browse/CALCITE-6967)\] Unparsing `STARTS_WITH`/`ENDS_WITH`/`BIT` functions is incorrect for the Clickhouse dialect
- \[ [CALCITE-5985](https://issues.apache.org/jira/browse/CALCITE-5985)\] `FilterTableFunctionTransposeRule` should not use “Logical” `RelNodes`
- \[ [CALCITE-6980](https://issues.apache.org/jira/browse/CALCITE-6980)\] `RelJson` cannot serialize binary literals
- \[ [CALCITE-6974](https://issues.apache.org/jira/browse/CALCITE-6974)\] Default typesystem has incorrect limits for `DECIMAL` for Presto/MySQL/Phoenix
- \[ [CALCITE-6979](https://issues.apache.org/jira/browse/CALCITE-6979)\] Invalid unparse for `IS TRUE`,`IS FALSE`,`IS NOT TRUE` and `IS NOT FALSE` in `ClickHouseDialect`
- \[ [CALCITE-6594](https://issues.apache.org/jira/browse/CALCITE-6594)\] `RelMdSize` does not handle `ARRAY` constructor calls
- \[ [CALCITE-6984](https://issues.apache.org/jira/browse/CALCITE-6984)\] `FamilyOperandTypeChecker` with a Predicate describing optional arguments does not reject mistyped expressions
- \[ [CALCITE-6986](https://issues.apache.org/jira/browse/CALCITE-6986)\] Parser rejects SQL sources that produce an empty statement list
- \[ [CALCITE-6983](https://issues.apache.org/jira/browse/CALCITE-6983)\] `SortJoinTransposeRule` should not push `SORT` past a `JOIN` when `SORT`’s fetch is `DynamicParam`
- \[ [CALCITE-6432](https://issues.apache.org/jira/browse/CALCITE-6432)\] Infinite loop for `JoinPushTransitivePredicatesRule` when there are multiple project expressions reference the same input field
- \[ [CALCITE-6992](https://issues.apache.org/jira/browse/CALCITE-6992)\] `RelJson` cannot serialize `UUID` literals
- \[ [CALCITE-6989](https://issues.apache.org/jira/browse/CALCITE-6989)\] Enhance `RexBuilder#makeIn` to create `SEARCH` for `ARRAY` literals
- \[ [CALCITE-6977](https://issues.apache.org/jira/browse/CALCITE-6977)\] Unparse `DELETE` SQL throws unsupported exception
- \[ [CALCITE-6981](https://issues.apache.org/jira/browse/CALCITE-6981)\] Runtime conversion of `DECIMAL ARRAY` to `INT ARRAY` fails with a `ClassCastException`
- \[ [CALCITE-6995](https://issues.apache.org/jira/browse/CALCITE-6995)\] Support `FULL JOIN` in StarRocks/Doris Dialect
- \[ [CALCITE-5387](https://issues.apache.org/jira/browse/CALCITE-5387)\] Type-mismatch on nullability in `JoinPushTransitivePredicatesRule``RelRule`
- \[ [CALCITE-6999](https://issues.apache.org/jira/browse/CALCITE-6999)\] Invalid unparse for `TRIM` in `PrestoDialect`
- \[ [CALCITE-7006](https://issues.apache.org/jira/browse/CALCITE-7006)\] Incorrect `left join` results with `IS NOT DISTINCT FROM` under specific plan
- \[ [CALCITE-6962](https://issues.apache.org/jira/browse/CALCITE-6962)\] `Exists` subquery returns incorrect result when `or` condition involves null column
- \[ [CALCITE-7005](https://issues.apache.org/jira/browse/CALCITE-7005)\] Invalid unparse for `IS TRUE`,`IS FALSE`,`IS NOT TRUE` and `IS NOT FALSE` in Hive/Presto Dialect
- \[ [CALCITE-6991](https://issues.apache.org/jira/browse/CALCITE-6991)\] Validator cannot infer type for `COALESCE` when call is not expanded
- \[ [CALCITE-7013](https://issues.apache.org/jira/browse/CALCITE-7013)\] Support building `RexLiterals` from `Character` values
- \[ [CALCITE-7001](https://issues.apache.org/jira/browse/CALCITE-7001)\] Cast of malformed literal to `TIMESTAMP WITH LOCAL TIME ZONE` need to throw informative error
- \[ [CALCITE-7025](https://issues.apache.org/jira/browse/CALCITE-7025)\] Verifying the Quantify operator without compatible types, should throw an exception about the Quantify Operator
- \[ [CALCITE-6866](https://issues.apache.org/jira/browse/CALCITE-6866)\] `PostgreSQLDialect` support to unparse `LISTAGG` aggregate function
- \[ [CALCITE-7022](https://issues.apache.org/jira/browse/CALCITE-7022)\] Decouple `ModelHandler` from `CalciteConnection`
- \[ [CALCITE-5638](https://issues.apache.org/jira/browse/CALCITE-5638)\] Columns trimmer need to consider sub queries
- \[ [CALCITE-7027](https://issues.apache.org/jira/browse/CALCITE-7027)\] Improve error message in case of several `UNION`, `INTERSECT`, `EXCEPT` in a query
- Documentation Supplement for `MinusToAntiJoinRule`
- Use `StandardCharsets` in `RuleMatchVisualizer.java`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-40-0 "Permalink")

- \[ [CALCITE-6895](https://issues.apache.org/jira/browse/CALCITE-6895)\] Change `JdbcTest.testVersion` to strictly match minor version in `gradle.properties`
- \[ [CALCITE-6915](https://issues.apache.org/jira/browse/CALCITE-6915)\] Generalize terminology Linter to allow pattern based checks in commit messages
- \[ [CALCITE-6960](https://issues.apache.org/jira/browse/CALCITE-6960)\] The tests for `SemiJoinRemoveRule` should explicitly include a semi join
- \[ [CALCITE-6957](https://issues.apache.org/jira/browse/CALCITE-6957)\] The `RelOptRulesTest` tests should fail if the xml file contains tests that do not exist in Java
- \[ [CALCITE-6335](https://issues.apache.org/jira/browse/CALCITE-6335)\] Quidem tests should allow specifying optimization passes to apply to programs
- \[ [CALCITE-6883](https://issues.apache.org/jira/browse/CALCITE-6883)\] Add Javadoc for `RelRoot#isTrivial` variants and refactor related tests
- \[ [CALCITE-6998](https://issues.apache.org/jira/browse/CALCITE-6998)\] The command `!set planner-rules` does not support rules with multiple `Config`

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-40-0 "Permalink")

- \[ [CALCITE-6934](https://issues.apache.org/jira/browse/CALCITE-6934)\] The examples for DDL extension on the official website cannot run
- Update documentation for example0 in `RelBuilderExample`

## [1.39.0](https://github.com/apache/calcite/releases/tag/calcite-1.39.0) / 2025-03-16 [Permalink](https://calcite.apache.org/docs/history.html\#v1-39-0 "Permalink")

This release comes 5 months after [1.38.0](https://calcite.apache.org/docs/history.html#v1-38-0),
contains contributions from 45 contributors, and resolves 209 issues.
Highlights include
the support of the `VARIANT` and `UUID` data types,
the support of checked arithmetic,
the addition of an optimal join enumeration algorithm based on dynamic programming (DPhyp),
new operators and data type support in Arrow adapter,
enhanced SQL compatibility with additional functions across Oracle, PostgreSQL, Hive, Spark, and MSSQL.

Contributors to this release:
Aleksey Plekhanov,
Alessandro Solimando,
Anton Kovalevsky,
Binhua Hu,
Cancai Cai,
Claude Brisson,
Clay Johnson,
Dmitry Sysolyatin,
Dongsheng He,
Francis Chuang,
Heng Xiao,
Hongyu Guo,
Hugh Pearse,
Illes Solt,
Jiajun Xie,
Joey Tong,
Julian Hyde,
Krisztian Kasa,
Lino Rosa,
Mihai Budiu,
Niels Pardon,
Oliver Lee,
Qi Zhu,
Rafael Acevedo,
Ruben Quesada Lopez,
Silun Dong,
Sreeharsha Ramanavarapu,
Stamatis Zampetakis (release manager),
suibianwanwan,
Tanner Clary,
tison,
TJ Banghart,
Ulrich Kramer,
Viggo Chen,
Vikram Ahuja,
Wang Zhao,
Xiaochen Zhou,
Xiong Duan,
Yanjing Wang,
YiwenWu,
Yu Xu,
Zhe Hu,
Zhen Chen,
Zhengqiang Duan,
Zoltan Haindrich.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 23;
Guava versions 21.0 to 33.3.0-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-39-0 "Permalink")

- \[ [CALCITE-6764](https://issues.apache.org/jira/browse/CALCITE-6764)\]
introduces a new method
`RelDataTypeFactory#enforceTypeWithNullability` in the existing
`RelDataTypeFactory` interface. The behavior of the new function is
similar to the existing API `createTypeWithNullability`; however, the
existing implementations of the `createTypeWithNullability` API cannot
create nullable record (`ROW`) types. Nullable record types are
legitimate in several SQL dialects.

- \[ [CALCITE-6685](https://issues.apache.org/jira/browse/CALCITE-6685)\]
introduces support for checked arithmetic on short integer types. A
new `SqlConformance.checkedArithmetic()` attribute is added to control
this behavior. The `BIG_QUERY` and `SQL_SERVER_2008` conformance have
been changed to use checked arithmetic, matching the specification of
these dialects.

- \[ [CALCITE-6704](https://issues.apache.org/jira/browse/CALCITE-6704)\]
Limit result size of `RelMdUniqueKeys` handler. Certain query patterns can lead
to an exponentially large number of unique keys that can cause crashes and OOM
errors. To prevent this kind of issues the `RelMdUniqueKeys` handler is now using
a limit to restrict the number of keys for each relational expression. The limit
is set to `1000` by default. The value is reasonably large to ensure that
most common use-cases will not be affected and at the same time bounds exponentially
large results set to a manageable value. Users that need a bigger/smaller limit
should create a new instance of `RelMdUniqueKeys` and register it using the
metadata provider of their choice.

- \[ [CALCITE-6728](https://issues.apache.org/jira/browse/CALCITE-6728)\]
introduces new methods to lookup tables and sub schemas inside schemas.
The methods used before (`Schema:getTable(String name)`, `Schema:getTableNames()`,
`Schema.getSubSchema(String name)` and `Schema.getSubSchemaNames(String name)`)
have been marked as deprecated.

- \[ [CALCITE-6766](https://issues.apache.org/jira/browse/CALCITE-6766)\] Move `DATEADD` and `DATEDIFF` from PostgreSQL to Redshift library
- \[ [CALCITE-6664](https://issues.apache.org/jira/browse/CALCITE-6664)\] Replace `GREATEST`, `LEAST` functions in Spark library with the implementation of PostgreSQL Library
- \[ [CALCITE-4758](https://issues.apache.org/jira/browse/CALCITE-4758)\] Wrong result when `SOME` sub-query in `SqlNodeList` is converted to `VALUES`

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-39-0 "Permalink")

- \[ [CALCITE-4918](https://issues.apache.org/jira/browse/CALCITE-4918)\] Support `VARIANT` data type
- \[ [CALCITE-6685](https://issues.apache.org/jira/browse/CALCITE-6685)\] Support checked arithmetic
- \[ [CALCITE-6846](https://issues.apache.org/jira/browse/CALCITE-6846)\] Support basic DPhyp join reorder algorithm
- \[ [CALCITE-5409](https://issues.apache.org/jira/browse/CALCITE-5409)\] Implement `BatchNestedLoopJoin` for JDBC
- \[ [CALCITE-6738](https://issues.apache.org/jira/browse/CALCITE-6738)\] Support a `UUID` type natively
- \[ [CALCITE-6668](https://issues.apache.org/jira/browse/CALCITE-6668)\] Support `IS TRUE`/`IS FALSE` operator in Arrow adapter
- \[ [CALCITE-6760](https://issues.apache.org/jira/browse/CALCITE-6760)\] Support `TIME` data type in Arrow adapter
- \[ [CALCITE-6690](https://issues.apache.org/jira/browse/CALCITE-6690)\] Support `DECIMAL` with precision and scale in Arrow adapter
- \[ [CALCITE-6730](https://issues.apache.org/jira/browse/CALCITE-6730)\] Add `CONVERT` function (enabled in Oracle library)
- \[ [CALCITE-6666](https://issues.apache.org/jira/browse/CALCITE-6666)\] Support Oracle `SYSDATE` and `SYSTIMESTAMP` functions
- \[ [CALCITE-6821](https://issues.apache.org/jira/browse/CALCITE-6821)\] Support `CRC32` function for Hive and Spark library
- \[ [CALCITE-6844](https://issues.apache.org/jira/browse/CALCITE-6844)\] Enable various existing `ARRAY` functions in Hive
- \[ [CALCITE-6800](https://issues.apache.org/jira/browse/CALCITE-6800)\] Enable a few existing functions to Hive library
- \[ [CALCITE-6831](https://issues.apache.org/jira/browse/CALCITE-6831)\] Add `ARRAY_SLICE` function（enabled in Hive Library)
- \[ [CALCITE-6689](https://issues.apache.org/jira/browse/CALCITE-6689)\] Add `INSTR` function in Hive library
- \[ [CALCITE-6815](https://issues.apache.org/jira/browse/CALCITE-6815)\] Support `BIN` function for Spark and Hive Library
- \[ [CALCITE-6812](https://issues.apache.org/jira/browse/CALCITE-6812)\] Support `BASE64` and `UNBASE64` functions for Hive
- \[ [CALCITE-6805](https://issues.apache.org/jira/browse/CALCITE-6805)\] Support `HEX` function for Hive and Spark Library
- \[ [CALCITE-4860](https://issues.apache.org/jira/browse/CALCITE-4860)\] Support `NULLS FIRST` and `NULLS LAST` query in Elasticsearch adapter
- \[ [CALCITE-6726](https://issues.apache.org/jira/browse/CALCITE-6726)\] Support `%` (modulo) operator in MSSQL
- \[ [CALCITE-6678](https://issues.apache.org/jira/browse/CALCITE-6678)\] Support `DUAL` table query when db provides this feature
- \[ [CALCITE-6645](https://issues.apache.org/jira/browse/CALCITE-6645)\] Support user-defined function without parentheses when db dialect’s `allowNiladicParentheses` property is false
- \[ [CALCITE-6663](https://issues.apache.org/jira/browse/CALCITE-6663)\] Support `SPLIT_PART` function for PostgreSQL
- \[ [CALCITE-5612](https://issues.apache.org/jira/browse/CALCITE-5612)\] Support PostgreSQL’s `SET TRANSACTION` command in Babel parser
- \[ [CALCITE-6643](https://issues.apache.org/jira/browse/CALCITE-6643)\] Enable `LENGTH`/`CHAR_LENGTH` function in `PrestoSqlDialect`
- \[ [CALCITE-6633](https://issues.apache.org/jira/browse/CALCITE-6633)\] Add `CEILING` to MSSQL dialect
- \[ [CALCITE-6612](https://issues.apache.org/jira/browse/CALCITE-6612)\] Add `DATE_SUB` function(enabled in Spark library)
- \[ [CALCITE-6618](https://issues.apache.org/jira/browse/CALCITE-6618)\] Support `NOT EQUALS` operator in Arrow adapter

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-39-0 "Permalink")

- \[ [CALCITE-6871](https://issues.apache.org/jira/browse/CALCITE-6871)\] Upgrade avatica from 1.25.0 to 1.26.0
- \[ [CALCITE-6794](https://issues.apache.org/jira/browse/CALCITE-6794)\] Site Gemfile contains vulnerable ruby libraries
- \[ [CALCITE-6782](https://issues.apache.org/jira/browse/CALCITE-6782)\] Upgrade Cassandra to 4.1.6 and Cassandra driver to 4.18.1

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-39-0 "Permalink")

- \[ [CALCITE-6885](https://issues.apache.org/jira/browse/CALCITE-6885)\] `SqlToRelConverter#convertUsing` should not fail if `commonTypeForBinaryComparison` returns null
- \[ [CALCITE-6650](https://issues.apache.org/jira/browse/CALCITE-6650)\] Optimize the `IN`/`SOME` sub-query using metadata row count
- \[ [CALCITE-6877](https://issues.apache.org/jira/browse/CALCITE-6877)\] Generate `LogicalProject` in `RelRoot.project()` when mapping is not name trivial
- \[ [CALCITE-6879](https://issues.apache.org/jira/browse/CALCITE-6879)\] Support `APPROX_DISTINCT_COUNT` for more dialects
- \[ [CALCITE-6876](https://issues.apache.org/jira/browse/CALCITE-6876)\] Druid Adapter support more functions
- \[ [CALCITE-6788](https://issues.apache.org/jira/browse/CALCITE-6788)\] `LoptOptimizeJoinRule` should be able to delegate costs to the planner
- \[ [CALCITE-6870](https://issues.apache.org/jira/browse/CALCITE-6870)\] `FilterToCalcRule`/`ProjectToCalcRule` should not convert a `Filter`/`Project` to `Calc` when it contains sub-query
- \[ [CALCITE-6874](https://issues.apache.org/jira/browse/CALCITE-6874)\] `FilterCalcMergeRule`/`ProjectCalcMergeRule` should not merge a `Filter`/`Project` to `Calc` when it contains sub-query
- \[ [CALCITE-6873](https://issues.apache.org/jira/browse/CALCITE-6873)\] `FilterProjectTransposeRule` should not push the `Filter` past the `Project` when the `Filter` contains a sub-query with correlation
- \[ [CALCITE-6867](https://issues.apache.org/jira/browse/CALCITE-6867)\] Druid Adapter transforms an SQL `NOT IN` filter to a Druid `IN` filter
- \[ [CALCITE-6850](https://issues.apache.org/jira/browse/CALCITE-6850)\] `ProjectRemoveRule` with two projects does not keep field names from the top one
- \[ [CALCITE-6864](https://issues.apache.org/jira/browse/CALCITE-6864)\] `ProjectAggregateMergeRule` loses the project’s field names
- \[ [CALCITE-6652](https://issues.apache.org/jira/browse/CALCITE-6652)\] `RelDecorrelator` can’t decorrelate query with `LIMIT` 1
- \[ [CALCITE-6837](https://issues.apache.org/jira/browse/CALCITE-6837)\] Invalid code generated for `ROW_NUMBER` function in `Enumerable` convention
- \[ [CALCITE-6274](https://issues.apache.org/jira/browse/CALCITE-6274)\] Join between Elasticsearch indexes returns empty result
- \[ [CALCITE-6853](https://issues.apache.org/jira/browse/CALCITE-6853)\] Nested window aggregate throws `UnsupportedOperationException` with the default `ValidatorConfig`
- \[ [CALCITE-6847](https://issues.apache.org/jira/browse/CALCITE-6847)\] ClickHouse doesn’t support `TRUE`/`FALSE` keywords in join predicate
- \[ [CALCITE-6819](https://issues.apache.org/jira/browse/CALCITE-6819)\] MSSQL doesn’t support `TRUE`/`FALSE` keywords in join predicate
- \[ [CALCITE-6832](https://issues.apache.org/jira/browse/CALCITE-6832)\] Redundant `fields`/`nullable` entries in `STRUCT` serialization to JSON
- \[ [CALCITE-6839](https://issues.apache.org/jira/browse/CALCITE-6839)\] SUM function throws overflow exceptions due to incorrect return types
- \[ [CALCITE-6833](https://issues.apache.org/jira/browse/CALCITE-6833)\] JDBC adapter generates invalid table alias for semi-join in `UNION`
- \[ [CALCITE-6824](https://issues.apache.org/jira/browse/CALCITE-6824)\] Sub-query in join conditions rewrite fails if referencing a column from the right-hand side table
- \[ [CALCITE-6838](https://issues.apache.org/jira/browse/CALCITE-6838)\] `RelToSqlConverter` should generate double parentheses when the input to `UNNEST` is a query statement
- \[ [CALCITE-6785](https://issues.apache.org/jira/browse/CALCITE-6785)\] `RelToSqlConverter` generate wrong sql when `UNNEST` has a correlate variable
- \[ [CALCITE-6804](https://issues.apache.org/jira/browse/CALCITE-6804)\] Anti-join with `WHERE NOT EXISTS` syntax has corrupted condition
- \[ [CALCITE-6817](https://issues.apache.org/jira/browse/CALCITE-6817)\] Add string representation of default nulls direction for `RelNode`
- \[ [CALCITE-6818](https://issues.apache.org/jira/browse/CALCITE-6818)\] Write `LIMIT` for fetch operations in Snowflake
- \[ [CALCITE-6790](https://issues.apache.org/jira/browse/CALCITE-6790)\] Write `LIMIT` for fetch operations in Vertica
- \[ [CALCITE-6813](https://issues.apache.org/jira/browse/CALCITE-6813)\] `UNNEST` infers incorrect nullability for the result when applied to an array that contains nullable `ROW` values
- \[ [CALCITE-6796](https://issues.apache.org/jira/browse/CALCITE-6796)\] Convert Type from `BINARY` to `VARBINARY` in PrestoDialect
- \[ [CALCITE-6771](https://issues.apache.org/jira/browse/CALCITE-6771)\] Convert Type from `FLOAT` to `DOUBLE` in PrestoDialect
- \[ [CALCITE-6503](https://issues.apache.org/jira/browse/CALCITE-6503)\] `JdbcAdapter` cannot push down `NOT IN` sub-queries
- \[ [CALCITE-6303](https://issues.apache.org/jira/browse/CALCITE-6303)\] UNION with CTE(s) results in exception during query validation
- \[ [CALCITE-4561](https://issues.apache.org/jira/browse/CALCITE-4561)\] Wrong results for plan with `EnumerableHashJoin` (semi) on nullable colunms
- \[ [CALCITE-6791](https://issues.apache.org/jira/browse/CALCITE-6791)\] Search pattern during matching in `REPLACE` function should be case insensitive in MSSQL
- \[ [CALCITE-6786](https://issues.apache.org/jira/browse/CALCITE-6786)\] `ANY`/`SOME` operator yields multiple rows in correlated queries
- \[ [CALCITE-2295](https://issues.apache.org/jira/browse/CALCITE-2295)\] Correlated sub-query with project generates wrong plan
- \[ [CALCITE-6756](https://issues.apache.org/jira/browse/CALCITE-6756)\] Preserve `CAST` of `STRING` operand in binary comparison for PostgreSQL
- \[ [CALCITE-6778](https://issues.apache.org/jira/browse/CALCITE-6778)\] `SOME` rewrite for correlated queries does not handle null values correctly
- \[ [CALCITE-6764](https://issues.apache.org/jira/browse/CALCITE-6764)\] Field access from a nullable `ROW` should be nullable
- \[ [CALCITE-6744](https://issues.apache.org/jira/browse/CALCITE-6744)\] `RelMetadataQuery.getColumnOrigins` should return null when column origin includes correlation variables
- \[ [CALCITE-6754](https://issues.apache.org/jira/browse/CALCITE-6754)\] Remove deprecated method calling in `Driver`
- \[ [CALCITE-5626](https://issues.apache.org/jira/browse/CALCITE-5626)\] Sub-query with fully-qualified table name throws ‘table not found’ during validation
- \[ [CALCITE-6301](https://issues.apache.org/jira/browse/CALCITE-6301)\] Following “must-filter” columns, add “bypass” columns
- \[ [CALCITE-6776](https://issues.apache.org/jira/browse/CALCITE-6776)\] Multiple expanded `IS NOT DISTINCT FROM` cannot be collapsed back
- \[ [CALCITE-6779](https://issues.apache.org/jira/browse/CALCITE-6779)\] Casts from `UUID` to `DATE` should be invalid
- \[ [CALCITE-6777](https://issues.apache.org/jira/browse/CALCITE-6777)\] Conversion between `UUID` and `BINARY` produces wrong results
- \[ [CALCITE-6774](https://issues.apache.org/jira/browse/CALCITE-6774)\] `REPLACE` function returns wrong result when search pattern is an empty string
- \[ [CALCITE-6413](https://issues.apache.org/jira/browse/CALCITE-6413)\] `SqlValidator` does not invoke `TypeCoercionImpl::binaryComparisonCoercion` for both `NATURAL` and `USING` join conditions
- \[ [CALCITE-6775](https://issues.apache.org/jira/browse/CALCITE-6775)\] `ToChar` and `ToTimestamp` PG implementors should use translator’s root instead of creating a new root expression
- \[ [CALCITE-6770](https://issues.apache.org/jira/browse/CALCITE-6770)\] Preserve column names when casts are inserted in projects
- \[ [CALCITE-6745](https://issues.apache.org/jira/browse/CALCITE-6745)\] UDF without parameters cannot be validated when use default conformance
- \[ [CALCITE-6762](https://issues.apache.org/jira/browse/CALCITE-6762)\] Preserving the `CAST` conversion for operands in Presto
- \[ [CALCITE-6749](https://issues.apache.org/jira/browse/CALCITE-6749)\] `RelMdUtil#setAggChildKeys` may return an incorrect result
- \[ [CALCITE-6699](https://issues.apache.org/jira/browse/CALCITE-6699)\] Invalid unparse for `VARCHAR` in StarRocksDialect
- \[ [CALCITE-3772](https://issues.apache.org/jira/browse/CALCITE-3772)\] `RelFieldTrimmer` incorrectly trims fields when the query includes correlated sub-query
- \[ [CALCITE-6751](https://issues.apache.org/jira/browse/CALCITE-6751)\] Reduction of `CAST` from string to interval is incorrect
- \[ [CALCITE-6759](https://issues.apache.org/jira/browse/CALCITE-6759)\] `RelToSqlConverter` returns the wrong result when `Aggregate` is on `Sort`
- \[ [CALCITE-6759](https://issues.apache.org/jira/browse/CALCITE-6759)\] `SqlToRelConverter` should not remove `ORDER BY` in sub-query if it has an `OFFSET`
- \[ [CALCITE-6761](https://issues.apache.org/jira/browse/CALCITE-6761)\] StarRocks generates incorrect SQL for certain units in the `EXTRACT` function
- \[ [CALCITE-6746](https://issues.apache.org/jira/browse/CALCITE-6746)\] `ProjectWindowTranspose` rule is unsound
- \[ [CALCITE-6727](https://issues.apache.org/jira/browse/CALCITE-6727)\] Column uniqueness constrain should only apply to inner join
- \[ [CALCITE-6649](https://issues.apache.org/jira/browse/CALCITE-6649)\] Enhance `RelMdPredicates` pull up predicate from project
- \[ [CALCITE-6740](https://issues.apache.org/jira/browse/CALCITE-6740)\] `RexToLixTranslator` generates code with many redundant structures
- \[ [CALCITE-6742](https://issues.apache.org/jira/browse/CALCITE-6742)\] `StandardConvertletTable.convertCall` loses casts from `ROW` comparisons
- \[ [CALCITE-6741](https://issues.apache.org/jira/browse/CALCITE-6741)\] The type of a comparison is nullable when either operand is nullable
- \[ [CALCITE-6665](https://issues.apache.org/jira/browse/CALCITE-6665)\] Add `isEmpty` metadata to check if a relational expression returns no rows
- \[ [CALCITE-6691](https://issues.apache.org/jira/browse/CALCITE-6691)\] `QUALIFY` on project references wrong columns
- \[ [CALCITE-6735](https://issues.apache.org/jira/browse/CALCITE-6735)\] Type coercion for comparisons does not coerce `ROW` types
- \[ [CALCITE-6734](https://issues.apache.org/jira/browse/CALCITE-6734)\] `RelFieldTrimmer` should trim `Aggregate`’s input fields which are arguments of unused aggregate functions
- \[ [CALCITE-6736](https://issues.apache.org/jira/browse/CALCITE-6736)\] Validator accepts comparisons between arrays, multisets, maps without regard to element types
- \[ [CALCITE-6737](https://issues.apache.org/jira/browse/CALCITE-6737)\] `LoptOptimizeJoinRule` can not identify selfjoin on unique join keys
- \[ [CALCITE-6725](https://issues.apache.org/jira/browse/CALCITE-6725)\] The caching mechanism key in `ElasticsearchSchemaFactory` is affected by the order of hosts
- \[ [CALCITE-6733](https://issues.apache.org/jira/browse/CALCITE-6733)\] Type inferred by coercion for comparisons with decimal is too narrow
- \[ [CALCITE-6700](https://issues.apache.org/jira/browse/CALCITE-6700)\] MySQL `BIT_COUNT` function should return result when parameter is `BOOLEAN`, `STRING`, `DATE`, `TIME` and `TIMESTAMP` type
- \[ [CALCITE-6566](https://issues.apache.org/jira/browse/CALCITE-6566)\] JDBC adapter should generate `PI` function with parentheses in most dialects
- \[ [CALCITE-6221](https://issues.apache.org/jira/browse/CALCITE-6221)\] JDBC adapter generates invalid query when the same table is joined multiple times
- \[ [CALCITE-6714](https://issues.apache.org/jira/browse/CALCITE-6714)\] Cast literal to interval gives the wrong result if literal is casted
- \[ [CALCITE-6715](https://issues.apache.org/jira/browse/CALCITE-6715)\] Enhance `RelFieldTrimmer` to trim `LogicalCorrelate` nodes
- \[ [CALCITE-6146](https://issues.apache.org/jira/browse/CALCITE-6146)\] Target charset should be used when comparing two strings through `CONVERT`/`TRANSLATE` function during validation
- \[ [CALCITE-6723](https://issues.apache.org/jira/browse/CALCITE-6723)\] Type inference for `ARRAY_INSERT` function is incorrect
- \[ [CALCITE-6721](https://issues.apache.org/jira/browse/CALCITE-6721)\] Incorrect implementation of `SqlFunction.checkedDivide`
- \[ [CALCITE-6711](https://issues.apache.org/jira/browse/CALCITE-6711)\] Functions whose output value can be null should return a nullable type
- \[ [CALCITE-6720](https://issues.apache.org/jira/browse/CALCITE-6720)\] Refactor cross product logic in `RelMdUniqueKeys#getPassedThroughCols` using `Linq4j#product`
- \[ [CALCITE-6688](https://issues.apache.org/jira/browse/CALCITE-6688)\] Allow operators of `SqlKind.SYMMETRICAL` to be reversed
- \[ [CALCITE-4954](https://issues.apache.org/jira/browse/CALCITE-4954)\] Group `TEXT` field failed in Elasticsearch adapter
- \[ [CALCITE-6713](https://issues.apache.org/jira/browse/CALCITE-6713)\] `NVL2`’s return data type should be nullable if and only if at least one of the second and third parameters are nullable
- \[ [CALCITE-6712](https://issues.apache.org/jira/browse/CALCITE-6712)\] `FROM_BASE64` and `PARSE_URL` return data type should always be nullable
- \[ [CALCITE-6709](https://issues.apache.org/jira/browse/CALCITE-6709)\] Parser accepts a call to `TRIM` with no arguments
- \[ [CALCITE-6706](https://issues.apache.org/jira/browse/CALCITE-6706)\] Checked arithmetic does not take effect in sub-queries
- \[ [CALCITE-6707](https://issues.apache.org/jira/browse/CALCITE-6707)\] Type inference for `CHR` function is wrong
- \[ [CALCITE-6684](https://issues.apache.org/jira/browse/CALCITE-6684)\] Support Arrow filter pushdown conditions that have subexpressions of a decimal type
- \[ [CALCITE-6705](https://issues.apache.org/jira/browse/CALCITE-6705)\] Allow for dialect-specific unparsing for numeric literals
- \[ [CALCITE-6640](https://issues.apache.org/jira/browse/CALCITE-6640)\] `RelMdUniqueKeys` generates non-minimal keys when columns are repeated in projections
- \[ [CALCITE-6703](https://issues.apache.org/jira/browse/CALCITE-6703)\] `RelJson` cannot handle timestamps prior to 1970-01-25 20:31:23.648
- \[ [CALCITE-5590](https://issues.apache.org/jira/browse/CALCITE-5590)\] `NullPointerException` when converting `IN` expression that is used inside `SELECT` list and `GROUP BY`
- \[ [CALCITE-6647](https://issues.apache.org/jira/browse/CALCITE-6647)\] `SortUnionTransposeRule` should not push sort past a union when sort’s fetch is `DynamicParam`
- \[ [CALCITE-6586](https://issues.apache.org/jira/browse/CALCITE-6586)\] Rules not firing due to `RelMdPredicates` returning `null` in `VolcanoPlanner`
- \[ [CALCITE-6614](https://issues.apache.org/jira/browse/CALCITE-6614)\] `InnodbFilterRule` incorrectly constructs condition when creating `InnodbFilter`
- \[ [CALCITE-6615](https://issues.apache.org/jira/browse/CALCITE-6615)\] `BindableTableScan``estimateRowCount` does not calculate push down filters
- \[ [CALCITE-6680](https://issues.apache.org/jira/browse/CALCITE-6680)\] `RexImpTable` erroneously declares `NullPolicy.NONE` for `IS_EMPTY`
- \[ [CALCITE-6674](https://issues.apache.org/jira/browse/CALCITE-6674)\] Make `RelDecorrelator` rules configurable
- \[ [CALCITE-6682](https://issues.apache.org/jira/browse/CALCITE-6682)\] Framing unsupported error message lacks `LAG`/`LEAD` functions
- \[ [CALCITE-4512](https://issues.apache.org/jira/browse/CALCITE-4512)\] `GROUP BY` expression with argument name same with `SELECT` field and alias causes validation error
- \[ [CALCITE-6677](https://issues.apache.org/jira/browse/CALCITE-6677)\] `HAVING` clauses fail validation when type coercion is applied to `GROUP BY` clause
- \[ [CALCITE-6651](https://issues.apache.org/jira/browse/CALCITE-6651)\] Use `RelBuilder` in `SqlToRelConverter` to construct `Union`
- \[ [CALCITE-6350](https://issues.apache.org/jira/browse/CALCITE-6350)\] Unexpected result from `UNION` with literals expression
- \[ [CALCITE-6662](https://issues.apache.org/jira/browse/CALCITE-6662)\] `RelJson.rangePointFromJson` cannot create Double numerics
- \[ [CALCITE-4590](https://issues.apache.org/jira/browse/CALCITE-4590)\] Incorrect query result with fixed-length string
- \[ [CALCITE-6655](https://issues.apache.org/jira/browse/CALCITE-6655)\] Aggregation of deeply nested window not detected when unparsing
- \[ [CALCITE-6605](https://issues.apache.org/jira/browse/CALCITE-6605)\] Lattice SQL supports complex column expressions
- \[ [CALCITE-5532](https://issues.apache.org/jira/browse/CALCITE-5532)\] `CompositeOperandTypeChecker` should check operands without type coercion first
- \[ [CALCITE-6642](https://issues.apache.org/jira/browse/CALCITE-6642)\] `AggregateUnionTransposeRule` should account for changes in nullability of pushed down aggregates
- \[ [CALCITE-6641](https://issues.apache.org/jira/browse/CALCITE-6641)\] Compiling programs with `ASOF` joins can report obscure errors
- \[ [CALCITE-6607](https://issues.apache.org/jira/browse/CALCITE-6607)\] `RexExecutor` can throw during evaluation
- \[ [CALCITE-6639](https://issues.apache.org/jira/browse/CALCITE-6639)\] Optimization that pulls up predicates causes `ASOF` JOIN validation failure
- \[ [CALCITE-6632](https://issues.apache.org/jira/browse/CALCITE-6632)\] Wrong optimization because window missing constants in digest
- \[ [CALCITE-6637](https://issues.apache.org/jira/browse/CALCITE-6637)\] Date type results should not be automatically converted to `TIMESTAMP` in Arrow adapter
- \[ [CALCITE-6604](https://issues.apache.org/jira/browse/CALCITE-6604)\] Add support for `SqlWindowTableFunction` in `RelToSqlConverter`
- \[ [CALCITE-5156](https://issues.apache.org/jira/browse/CALCITE-5156)\] Support implicit integer types cast for `IN` sub-query
- \[ [CALCITE-6638](https://issues.apache.org/jira/browse/CALCITE-6638)\] Expression simplification such as `1 > a or 1 <= a or a is null` to `TRUE` is incorrect when casts are not lossless
- \[ [CALCITE-6631](https://issues.apache.org/jira/browse/CALCITE-6631)\] Common type for a comparison operator is wrong when comparing a Java type long with a SQL type `INTEGER`
- \[ [CALCITE-6608](https://issues.apache.org/jira/browse/CALCITE-6608)\] `RexBuilder#makeIn` should create `EQUALS` instead of `SEARCH` for single point values
- \[ [CALCITE-6623](https://issues.apache.org/jira/browse/CALCITE-6623)\] MongoDB adapter throws a `ClassCastException` when `Decimal128` or `Binary` types are used, or when a primitive value is cast to a string
- \[ [CALCITE-5036](https://issues.apache.org/jira/browse/CALCITE-5036)\] Remove RexSimplify from RelMdPredicates#getPredicates to avoid performance regression
- Reduced the number of type checks
- Remove `IN_FENNEL` operator
- Remove unused properties in CalciteResource.properties
- Add method `ImmutableBitSet.stream()`
- Casts between time intervals do not require scaling
- Implement `VARIANT` functions `TYPEOF`, `VARIANTNULL`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-39-0 "Permalink")

- \[ [CALCITE-6865](https://issues.apache.org/jira/browse/CALCITE-6865)\] Sonar analysis fails due to OOM
- \[ [CALCITE-6856](https://issues.apache.org/jira/browse/CALCITE-6856)\] Add JOIN test for MongoDB adapter
- \[ [CALCITE-6827](https://issues.apache.org/jira/browse/CALCITE-6827)\] Build failure due to json-smart version mismatch
- \[ [CALCITE-6806](https://issues.apache.org/jira/browse/CALCITE-6806)\] Add CI action to ensure site remains buildable after changes
- \[ [CALCITE-6747](https://issues.apache.org/jira/browse/CALCITE-6747)\] Multiple SLF4J bindings in Spark unit test
- \[ [CALCITE-6810](https://issues.apache.org/jira/browse/CALCITE-6810)\] Update tests for `CONVERT_TIMEZONE` and `CONCAT` function in RedShift library
- \[ [CALCITE-6801](https://issues.apache.org/jira/browse/CALCITE-6801)\] Linter should disallow tags such as ‘Chore’ in commit messages
- \[ [CALCITE-6803](https://issues.apache.org/jira/browse/CALCITE-6803)\] Publish website: error while trying to write to /home/
- \[ [CALCITE-5127](https://issues.apache.org/jira/browse/CALCITE-5127)\] Enable tests in unnest.iq
- \[ [CALCITE-6780](https://issues.apache.org/jira/browse/CALCITE-6780)\] `AbstractSqlTester` fails to build query for expression `TRIM(string)`
- \[ [CALCITE-6769](https://issues.apache.org/jira/browse/CALCITE-6769)\] Migrate Build Scan publication to develocity.apache.org
- \[ [CALCITE-6732](https://issues.apache.org/jira/browse/CALCITE-6732)\] `CHR` and `REPEAT` function are not covered by Redshift library in `SqlOperatorTest`
- \[ [CALCITE-6724](https://issues.apache.org/jira/browse/CALCITE-6724)\] `MockTable` support for multiple (individual & composite) keys
- \[ [CALCITE-6676](https://issues.apache.org/jira/browse/CALCITE-6676)\] `DiffRepository` does not update log (\_actual) file when assertion fails
- \[ [CALCITE-6635](https://issues.apache.org/jira/browse/CALCITE-6635)\] Refactor Arrow adapter Test
- \[ [CALCITE-6592](https://issues.apache.org/jira/browse/CALCITE-6592)\] Add test for `RelMdPredicates` pull up predicate from `UNION` when it’s input predicates include `NULL` values
- Add `IS_UNKNOWN` operator test in Arrow Adapter
- Add `TRIM` function unit test for Hsqldb

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-39-0 "Permalink")

- \[ [CALCITE-6758](https://issues.apache.org/jira/browse/CALCITE-6758)\] Update Elasticsearch adapter tutorial document
- \[ [CALCITE-6698](https://issues.apache.org/jira/browse/CALCITE-6698)\] Add Javadoc to `PartiallyOrderedSet#getNonChildren` and `getNonParents` to clarify their behavior
- \[ [CALCITE-6613](https://issues.apache.org/jira/browse/CALCITE-6613)\] Make the Background code examples in Calcite official documentation clearer
- \[ [CALCITE-6610](https://issues.apache.org/jira/browse/CALCITE-6610)\] ASF matomo integration for website analytics
- \[ [CALCITE-6845](https://issues.apache.org/jira/browse/CALCITE-6845)\] Self-host website images
- \[ [CALCITE-6843](https://issues.apache.org/jira/browse/CALCITE-6843)\] Self-host Lato font on website due to ASF’s content security policy
- Site: Reformat `CONCAT_WS` and `REVERSE` document
- Site: Add talks from Calcite Meetup February 2025
- Update document for resolve in SqlValidatorScope
- Update javadoc for the fun connect string parameter
- Improve document in RelBuilder
- Modify `DAYNAME` and `MONTHNAME` doc description when set different locale

## [1.38.0](https://github.com/apache/calcite/releases/tag/calcite-1.38.0) / 2024-10-15 [Permalink](https://calcite.apache.org/docs/history.html\#v1-38-0 "Permalink")

This release comes 5 months after [1.37.0](https://calcite.apache.org/docs/history.html#v1-37-0),
contains contributions from 39 contributors, and resolves 165 issues.
Highlights include the
[`AS MEASURE`](https://issues.apache.org/jira/browse/CALCITE-4496)
clause to define measures and use them in
[simple queries](https://issues.apache.org/jira/browse/CALCITE-6519),
[`ASOF` join](https://issues.apache.org/jira/browse/CALCITE-6372),
the
[`EXCLUDE`](https://issues.apache.org/jira/browse/CALCITE-5855)
clause in window aggregates, Postgres-compatible implementations of the
[`TO_DATE`, `TO_TIMESTAMP`](https://issues.apache.org/jira/browse/CALCITE-6449)
and
[`TO_CHAR`](https://issues.apache.org/jira/browse/CALCITE-6358)
functions, and the extension of the type system to allow
[types with negative scale](https://issues.apache.org/jira/browse/CALCITE-6560).

Contributors to this release:
Aleksey Plekhanov,
Alessandro Solimando,
Barry Kelly,
Bowen Yang,
Cancai Cai,
Clay Johnson,
Cyril de Catheu,
Dawid Wysakowicz,
Evgeniy Stanilovsky,
Fan Luo,
Gian Merlino,
Ian Bertolacci,
Itiel Sadeh,
James Duong,
Jiabao Sun,
Jiajun Xie,
jianhong.hu,
Jie Cheng,
Julian Hyde (release manager),
Konstantin Orlov,
Krisztian Kasa,
Michael Mior,
Mihai Budiu,
Mou Wu,
Niels Pardon,
Nitish Kumar,
Norman Jordan,
Pranava B,
Rodrigo Rueda,
Ruben Quesada Lopez,
Sergey Nuyanzin,
Stamatis Zampetakis,
suibianwanwan,
Tim Grein,
TJ Banghart,
Wegdan Ghazi,
Xiong Duan,
YiwenWu,
Zoltan Haindrich.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 23;
Guava versions 21.0 to 33.3.0-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-38-0 "Permalink")

_Cast to DECIMAL_. In previous versions of Calcite the casts to
`DECIMAL` types were treated as no-ops. After the fix of
\[ [CALCITE-6322](https://issues.apache.org/jira/browse/CALCITE-6322)\],
calculations that use `DECIMAL` values may produce slightly
different results.

_Represention of floating point values in `RexLiteral`_.
Previously, floating point values were encoded into `BigDecimal`
values. This caused precision loss
when representing the results of simplifying expressions whose
results are floating point. After the fix of
\[ [CALCITE-2067](https://issues.apache.org/jira/browse/CALCITE-2067)\],
`RexLiteral` stores the value of a SQL `DOUBLE`, `FLOAT` or `REAL` values
using a Java `double`. The result of `RexLiteral.getValue()` accordingly
changes type in this case.

_Deprecated methods in `interface RelDataTypeSystem`_.
\[ [CALCITE-6598](https://issues.apache.org/jira/browse/CALCITE-6598)\]
deprecates methods `getMaxNumericScale()` and `getMaxNumericPrecision()`,
to be consistent with `getMinScale(SqlTypeName)` added in
\[ [CALCITE-6560](https://issues.apache.org/jira/browse/CALCITE-6560)\].
From 1.38, you should instead call `getMaxScale(DECIMAL)` and
`getMaxPrecision(DECIMAL)`. If you have overridden these methods, Calcite will
continue to call your overriding method in 1.38 but will cease in 1.39.
To avoid this _breaking change in 1.39_, during 1.38 you should move your
override logic to the `getMaxScale` and `getMaxPrecision` methods.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-38-0 "Permalink")

- \[ [CALCITE-6603](https://issues.apache.org/jira/browse/CALCITE-6603)\]
Lattice SQL supports generation of specified dialects
- \[ [CALCITE-6560](https://issues.apache.org/jira/browse/CALCITE-6560)\]
Allow types with negative scale
- \[ [CALCITE-6576](https://issues.apache.org/jira/browse/CALCITE-6576)\]
In `SET` clause of `UPDATE` statement, allow column identifiers to be prefixed
with table alias
- \[ [CALCITE-6584](https://issues.apache.org/jira/browse/CALCITE-6584)\]
Validate prefixed column identifiers in `SET` clause of `UPDATE` statement
- \[ [CALCITE-4838](https://issues.apache.org/jira/browse/CALCITE-4838)\]
Add `RoundingMode` in `RelDataTypeSystem` to specify the rounding behavior
- \[ [CALCITE-6020](https://issues.apache.org/jira/browse/CALCITE-6020)\]
Add planner rule, `class ProjectOverSumToSum0Rule`, that converts `SUM` to
`SUM0`
- \[ [CALCITE-6372](https://issues.apache.org/jira/browse/CALCITE-6372)\]
Add `ASOF` join
- \[ [CALCITE-6519](https://issues.apache.org/jira/browse/CALCITE-6519)\]
Support non-aggregate query that uses measure in `ORDER BY`
- \[ [CALCITE-4496](https://issues.apache.org/jira/browse/CALCITE-4496)\]
Measure columns (`SELECT ... AS MEASURE`)
- \[ [CALCITE-5802](https://issues.apache.org/jira/browse/CALCITE-5802)\]
In `RelBuilder`, add method `aggregateRex`, to allow aggregating complex
expressions such as “`1 + SUM(x + 2)`”
- \[ [CALCITE-6444](https://issues.apache.org/jira/browse/CALCITE-6444)\]
Add a function library for Amazon Redshift
- \[ [CALCITE-6427](https://issues.apache.org/jira/browse/CALCITE-6427)\]
Use a higher precision for `DECIMAL` intermediate results for some aggregate
functions like `STDDEV`
- \[ [CALCITE-5855](https://issues.apache.org/jira/browse/CALCITE-5855)\]
Support frame exclusion in window functions, e.g.
`OVER (... EXCLUDE CURRENT ROW)`
- \[ [CALCITE-6365](https://issues.apache.org/jira/browse/CALCITE-6365)\]
Support `RETURNING` clause of `JSON_QUERY` function

New functions:

- \[ [CALCITE-3592](https://issues.apache.org/jira/browse/CALCITE-3592)\]
Implement `BITNOT` scalar function
- \[ [CALCITE-6527](https://issues.apache.org/jira/browse/CALCITE-6527)\]
Add `DATE_ADD` function (enabled in Spark library)
- \[ [CALCITE-6549](https://issues.apache.org/jira/browse/CALCITE-6549)\]
Add `LOG1P` function (enabled in Spark library)
- \[ [CALCITE-3779](https://issues.apache.org/jira/browse/CALCITE-3779)\]
Implement `BITAND`, `BITOR`, `BITXOR` scalar functions
- \[ [CALCITE-3697](https://issues.apache.org/jira/browse/CALCITE-3697)\]
Implement `BITCOUNT` scalar function
- \[ [CALCITE-5807](https://issues.apache.org/jira/browse/CALCITE-5807)\]
Add `SUBSTRING_INDEX` function (enabled in Spark library)
- \[ [CALCITE-6396](https://issues.apache.org/jira/browse/CALCITE-6396)\]
Add `ADD_MONTHS` function (enabled in Oracle, Spark library)
- \[ [CALCITE-6310](https://issues.apache.org/jira/browse/CALCITE-6310)\]
Add `REGEXP_REPLACE` function (enabled in Postgres library)
- \[ [CALCITE-6472](https://issues.apache.org/jira/browse/CALCITE-6472)\]
Add degree-based trigonometric functions to Postgres function library
- \[ [CALCITE-6312](https://issues.apache.org/jira/browse/CALCITE-6312)\]
Add `LOG` function (enabled in Postgres library)
- \[ [CALCITE-6445](https://issues.apache.org/jira/browse/CALCITE-6445)\]
Add `REVERSE` function (enabled in Spark library)
- \[ [CALCITE-6449](https://issues.apache.org/jira/browse/CALCITE-6449)\]
Enable Postgres implementations of `TO_DATE` and `TO_TIMESTAMP` functions
- \[ [CALCITE-5634](https://issues.apache.org/jira/browse/CALCITE-5634)\]
Enable `GREATEST`, `LEAST` functions in Postgres library
- \[ [CALCITE-6446](https://issues.apache.org/jira/browse/CALCITE-6446)\]
Add `CONCAT_WS` function (enabled in Spark library)
- \[ [CALCITE-6454](https://issues.apache.org/jira/browse/CALCITE-6454)\]
Implement array comparison operators
- \[ [CALCITE-6325](https://issues.apache.org/jira/browse/CALCITE-6325)\]
Add `LOG` function (enabled in MySQL and Spark library)
- \[ [CALCITE-6392](https://issues.apache.org/jira/browse/CALCITE-6392)\]
Support all Postgres 14 date/time patterns for `TO_DATE` and `TO_TIMESTAMP`
- \[ [CALCITE-6441](https://issues.apache.org/jira/browse/CALCITE-6441)\]
Add `BOOLAGG_AND`, `BOOLAGG_OR` aggregate functions (enabled in Snowflake
library)
- \[ [CALCITE-6311](https://issues.apache.org/jira/browse/CALCITE-6311)\]
Support Postgres `DATE_PART` function
- \[ [CALCITE-6424](https://issues.apache.org/jira/browse/CALCITE-6424)\]
Enable `RLIKE` function in MySQL library
- \[ [CALCITE-6397](https://issues.apache.org/jira/browse/CALCITE-6397)\]
Add `NVL2` function (enabled in Oracle, Spark library)
- \[ [CALCITE-6358](https://issues.apache.org/jira/browse/CALCITE-6358)\]
Support all Postgres 14 date/time patterns for `TO_CHAR` function
- \[ [CALCITE-6313](https://issues.apache.org/jira/browse/CALCITE-6313)\]
Add `POWER` function for Postgres
- \[ [CALCITE-6483](https://issues.apache.org/jira/browse/CALCITE-6483)\]
Enable `LEN` and `LENGTH` in the correct function libraries

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-38-0 "Permalink")

- \[ [CALCITE-6587](https://issues.apache.org/jira/browse/CALCITE-6587)\]
Support Java 23 and Guava 33.3.0; also upgrade
Hadoop from 2.7.5 to 2.10.2
- \[ [CALCITE-5737](https://issues.apache.org/jira/browse/CALCITE-5737)\]
Support JDK 21 and JDK 22; also upgrade
asm from 7.2 to 9.6;
byte-buddy from 1.9.3 to 1.14.15;
forbiddenapis from 3.5.1 to 3.7;
mockito from 2.23.4 to 3.12.4
- \[ [CALCITE-6174](https://issues.apache.org/jira/browse/CALCITE-6174)\]
Upgrade gradle from 7.6.1 to 8.7

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-38-0 "Permalink")

- \[ [CALCITE-6620](https://issues.apache.org/jira/browse/CALCITE-6620)\]
`VALUES` created by `RelBuilder` do not have a homogeneous type
- \[ [CALCITE-6617](https://issues.apache.org/jira/browse/CALCITE-6617)\]
`TypeCoercion` is not applied correctly to comparisons
- \[ [CALCITE-6598](https://issues.apache.org/jira/browse/CALCITE-6598)\]
In `interface RelDataTypeSystem`, deprecate methods `getMaxNumericScale` and
`getMaxNumericPrecision`
- \[ [CALCITE-6599](https://issues.apache.org/jira/browse/CALCITE-6599)\]
`RelMdPredicates` should pull up more predicates from `VALUES` when there are
several literals
- \[ [CALCITE-6585](https://issues.apache.org/jira/browse/CALCITE-6585)\]
In the Postgres `TO_CHAR` function, improve caching
- \[ [CALCITE-6593](https://issues.apache.org/jira/browse/CALCITE-6593)\]
`EnumerableHashJoin` throws `NullPointerException` when outer-joining tables
with many fields and unmatching rows
- \[ [CALCITE-6600](https://issues.apache.org/jira/browse/CALCITE-6600)\]
`AggregateJoinTransposeRule` throws `ArrayIndexOutOfBoundsException` when
applied on a `SemiJoin`
- \[ [CALCITE-6595](https://issues.apache.org/jira/browse/CALCITE-6595)\]
Preserve collation on non-distinct aggregate calls in
`AggregateExpandWithinDistinctRule`
- \[ [CALCITE-6596](https://issues.apache.org/jira/browse/CALCITE-6596)\]
Enable function-level cache by default
- \[ [CALCITE-6498](https://issues.apache.org/jira/browse/CALCITE-6498)\]
Elasticsearch multi-field mappings do not work
- \[ [CALCITE-6374](https://issues.apache.org/jira/browse/CALCITE-6374)\]
`LatticeSuggester` throws `NullPointerException` when aggregate call is covered
with `CAST`
- \[ [CALCITE-6226](https://issues.apache.org/jira/browse/CALCITE-6226)\]
Wrong `ISOWEEK` and no `ISOYEAR` in BigQuery `FORMAT_DATE` function
- \[ [CALCITE-6522](https://issues.apache.org/jira/browse/CALCITE-6522)\]
`MAP_KEYS` and `MAP_VALUES` functions should throw if a key value is null
- \[ [CALCITE-6071](https://issues.apache.org/jira/browse/CALCITE-6071)\]
`RexCall` should carry source position information for runtime error reporting
- \[ [CALCITE-6581](https://issues.apache.org/jira/browse/CALCITE-6581)\]
Incorrect `INTERVAL` math for `WEEK` and `QUARTER`
- Check for correlation variables in project when constructing aggregate in
`SqlToRelConverter.createAggImpl`
- \[ [CALCITE-6550](https://issues.apache.org/jira/browse/CALCITE-6550)\]
Improve SQL function overloading
- \[ [CALCITE-6343](https://issues.apache.org/jira/browse/CALCITE-6343)\]
Ensure that `AS` operator doesn’t change return type of measures
- \[ [CALCITE-6408](https://issues.apache.org/jira/browse/CALCITE-6408)\]
Not-null `ThreadLocal`
- \[ [CALCITE-6563](https://issues.apache.org/jira/browse/CALCITE-6563)\]
`RelToSqlConverter` should not merge two window functions
- \[ [CALCITE-6569](https://issues.apache.org/jira/browse/CALCITE-6569)\]
`RelToSqlConverter` missing `IGNORE NULLS` for window function
- \[ [CALCITE-6565](https://issues.apache.org/jira/browse/CALCITE-6565)\]
JDBC adapter for MSSQL generates incorrect SQL for `CHAR` without precision
- \[ [CALCITE-6557](https://issues.apache.org/jira/browse/CALCITE-6557)\]
`AggregateMergeRule` throws `AssertionError` “type mismatch”
- \[ [CALCITE-6559](https://issues.apache.org/jira/browse/CALCITE-6559)\]
Query with measure that applies `AVG` to `SMALLINT` throws `AssertionError`
“Cannot add expression of different type to set”
- \[ [CALCITE-4871](https://issues.apache.org/jira/browse/CALCITE-4871)\]
`CAST` a literal to `DECIMAL` type returns wrong result
- \[ [CALCITE-6555](https://issues.apache.org/jira/browse/CALCITE-6555)\]
`RelBuilder.aggregateRex` wrongly thinks aggregate functions of “`GROUP BY ()`”
queries are `NOT NULL`
- \[ [CALCITE-5613](https://issues.apache.org/jira/browse/CALCITE-5613)\]
Assert for number of args for metadata methods at `CacheGeneratorUtil`
- Use `ACCEPT_SUB_QUERY` when parsing operands to square-bracketed array
constructor function
- \[ [CALCITE-6543](https://issues.apache.org/jira/browse/CALCITE-6543)\]
In `RelOptCostImpl`, change the `toString()` method to be consistent with
`VolcanoCost`
- \[ [CALCITE-6547](https://issues.apache.org/jira/browse/CALCITE-6547)\]
Result type inferred for `STDDEV_SAMP` is incorrect
- \[ [CALCITE-6546](https://issues.apache.org/jira/browse/CALCITE-6546)\]
In JDBC adapter for Hive, must generate an alias for a sub-query in the `FROM`
clause
- \[ [CALCITE-4806](https://issues.apache.org/jira/browse/CALCITE-4806)\]
Lossy `CAST` is incorrectly simplified
- \[ [CALCITE-5883](https://issues.apache.org/jira/browse/CALCITE-5883)\]
`ROWS` window aggregates ignore frames when there is no `ORDER BY` clause
- \[ [CALCITE-6540](https://issues.apache.org/jira/browse/CALCITE-6540)\]
`RelOptUtil.pushDownJoinConditions` does not correctly adjust the match
condition of an `ASOF` join
- \[ [CALCITE-6534](https://issues.apache.org/jira/browse/CALCITE-6534)\]
Adjust type when pulling up `Calc` in `JoinUnifyRule`
- \[ [CALCITE-6533](https://issues.apache.org/jira/browse/CALCITE-6533)\]
Division between `INTEGER` and `DECIMAL` produces incorrect result
- \[ [CALCITE-6346](https://issues.apache.org/jira/browse/CALCITE-6346)\]
JdbcAdapter loses cast for dynamic filter arguments
- \[ [CALCITE-6501](https://issues.apache.org/jira/browse/CALCITE-6501)\]
`AssertionError` in `JoinUnifyRule` due to type mismatch
- \[ [CALCITE-6518](https://issues.apache.org/jira/browse/CALCITE-6518)\]
`ClassCastException` during validation when loading multiple libraries
- \[ [CALCITE-6464](https://issues.apache.org/jira/browse/CALCITE-6464)\]
Type inference for `DECIMAL` division seems incorrect
- \[ [CALCITE-6433](https://issues.apache.org/jira/browse/CALCITE-6433)\]
`SUBSTRING` function can return incorrect empty result
- \[ [CALCITE-6481](https://issues.apache.org/jira/browse/CALCITE-6481)\]
Optimize `VALUES - UNION - VALUES` to a single `VALUES` the `IN`-list contains
`CAST` and it is converted to `VALUES`
- \[ [CALCITE-6513](https://issues.apache.org/jira/browse/CALCITE-6513)\]
`FilterProjectTransposeRule` may cause `OutOfMemoryError` when `Project`
expressions are complex
- \[ [CALCITE-6471](https://issues.apache.org/jira/browse/CALCITE-6471)\]
Improve performance of `SqlToRelConverter` by preventing unconditional
conversion of `SqlNode` instances to string for null-check messages
- \[ [CALCITE-6480](https://issues.apache.org/jira/browse/CALCITE-6480)\]
JDBC adapter for Oracle should not generate `CASE WHEN` expression that returns
a `BOOLEAN` value, because Oracle does not support it
- \[ [CALCITE-6506](https://issues.apache.org/jira/browse/CALCITE-6506)\]
Type inference for `IN`-list is incorrect
- \[ [CALCITE-6478](https://issues.apache.org/jira/browse/CALCITE-6478)\]
JSON functions should return `NULL` when input is `NULL`
- \[ [CALCITE-6322](https://issues.apache.org/jira/browse/CALCITE-6322)\]
Casts to `DECIMAL` types are ignored
- \[ [CALCITE-3522](https://issues.apache.org/jira/browse/CALCITE-3522)\]
`SqlValidator.validateLiteral` rejects literals with a `DECIMAL` type that
require more than 64 bits
- \[ [CALCITE-6266](https://issues.apache.org/jira/browse/CALCITE-6266)\]
`SqlValidatorException` with `LATERAL TABLE` and `JOIN`
- \[ [CALCITE-6507](https://issues.apache.org/jira/browse/CALCITE-6507)\]
Random functions are incorrectly considered deterministic
- \[ [CALCITE-6502](https://issues.apache.org/jira/browse/CALCITE-6502)\]
Parser loses position information for `Expression3`
- \[ [CALCITE-6473](https://issues.apache.org/jira/browse/CALCITE-6473)\]
`HAVING` clauses may not contain window functions
- \[ [CALCITE-6482](https://issues.apache.org/jira/browse/CALCITE-6482)\]
Oracle dialect convert `BOOLEAN` literal when version < 23
- \[ [CALCITE-6495](https://issues.apache.org/jira/browse/CALCITE-6495)\]
Allow `ProjectSetOpTransposeRule` to work with any subclass of `Project`
- \[ [CALCITE-6485](https://issues.apache.org/jira/browse/CALCITE-6485)\]
`AssertionError` when an `IN`-list containing `NULL` has an implicit coercion
type converter
- \[ [CALCITE-6169](https://issues.apache.org/jira/browse/CALCITE-6169)\]
`EnumUtils.convert` does not implement the correct SQL cast semantics
- \[ [CALCITE-6218](https://issues.apache.org/jira/browse/CALCITE-6218)\]
`RelToSqlConverter` fails to convert correlated lateral joins
- \[ [CALCITE-6488](https://issues.apache.org/jira/browse/CALCITE-6488)\]
Ensure collations created by `RelCollations` are canonized once
- \[ [CALCITE-6295](https://issues.apache.org/jira/browse/CALCITE-6295)\]
Support `IS NOT NULL` in Arrow adapter
- \[ [CALCITE-6296](https://issues.apache.org/jira/browse/CALCITE-6296)\]
Support `IS NULL` in Arrow adapter
- \[ [CALCITE-6475](https://issues.apache.org/jira/browse/CALCITE-6475)\]
`RelToSqlConverter` fails when the `IN`-list contains `NULL` and it is
converted to `VALUES`
- \[ [CALCITE-6474](https://issues.apache.org/jira/browse/CALCITE-6474)\]
`Aggregate` with constant key can get a `RowCount` greater than its
`MaxRowCount`
- \[ [CALCITE-6450](https://issues.apache.org/jira/browse/CALCITE-6450)\]
Postgres `CONCAT_WS` function throws exception when parameter type is
`(<CHAR(1)>, <INTEGER ARRAY>)`
- \[ [CALCITE-6462](https://issues.apache.org/jira/browse/CALCITE-6462)\]
`VolcanoPlanner` internal valid may throw exception when log trace is enabled
- \[ [CALCITE-6468](https://issues.apache.org/jira/browse/CALCITE-6468)\]
`RelDecorrelator` throws `AssertionError` if correlated variable is used as
`Aggregate` group key
- \[ [CALCITE-3094](https://issues.apache.org/jira/browse/CALCITE-3094)\]
Code of method grows beyond 64 KB when joining two tables with many fields
- \[ [CALCITE-6453](https://issues.apache.org/jira/browse/CALCITE-6453)\]
Simplify casts which are result of constant reduction
- \[ [CALCITE-6388](https://issues.apache.org/jira/browse/CALCITE-6388)\]
`PsTableFunction` throws `NumberFormatException` when the `user` column has
spaces
- \[ [CALCITE-6435](https://issues.apache.org/jira/browse/CALCITE-6435)\]
`SqlToRelConverter` incorrectly simplifies some `IN` expressions
- \[ [CALCITE-6460](https://issues.apache.org/jira/browse/CALCITE-6460)\]
`SortRemoveConstantKeysRule` fails with `AssertionError` due to mismatched
collation on resulting `Sort`
- \[ [CALCITE-6401](https://issues.apache.org/jira/browse/CALCITE-6401)\]
JDBC adapter cannot push down `JOIN` whose condition includes `IS TRUE`,
`IS NULL`, dynamic parameter, `CAST`, literal comparison
- \[ [CALCITE-6436](https://issues.apache.org/jira/browse/CALCITE-6436)\]
JDBC adapter generates SQL missing parentheses when comparing 3 values with
the same precedence, such as “`(a = b) = c`”
- \[ [CALCITE-6369](https://issues.apache.org/jira/browse/CALCITE-6369)\]
Expanding `*` (star) gives `ArrayIndexOutOfBoundsException` with redundant
columns and `USING`
- \[ [CALCITE-6442](https://issues.apache.org/jira/browse/CALCITE-6442)\]
Validator rejects `FILTER` in `OVER` windows
- \[ [CALCITE-6380](https://issues.apache.org/jira/browse/CALCITE-6380)\]
Casts from `INTERVAL` and `STRING` to `DECIMAL` are incorrect
- \[ [CALCITE-6008](https://issues.apache.org/jira/browse/CALCITE-6008)\]
`ARRAY_AGG` should return `ARRAY NULL` when there are no input rows
- \[ [CALCITE-6414](https://issues.apache.org/jira/browse/CALCITE-6414)\]
JDBC adapter should generate `BOOLOR_AGG`, `BOOLAND_AGG` for `MAX`, `MIN` on
`BOOLEAN` values in Snowflake dialect
- \[ [CALCITE-6434](https://issues.apache.org/jira/browse/CALCITE-6434)\]
JDBC adapter generates wrong SQL for Spark and Hive because it fails to quote
an identifier containing “`$`”
- \[ [CALCITE-6426](https://issues.apache.org/jira/browse/CALCITE-6426)\]
JDBC adapter for StarRocks generates invalid SQL for `INT` and `BIGINT` types
- \[ [CALCITE-6430](https://issues.apache.org/jira/browse/CALCITE-6430)\]
JDBC adapter for Postgres, MySQL and HSQLDB generates incorrect SQL for
`SINGLE_VALUE` when the sub-query returns one not-`NULL` value and `NULL` value
- \[ [CALCITE-6429](https://issues.apache.org/jira/browse/CALCITE-6429)\]
Arrow adapter should default to the Enumerable convention for unsupported
filters
- \[ [CALCITE-6370](https://issues.apache.org/jira/browse/CALCITE-6370)\]
`AS` operator problems with `USING` clause
- \[ [CALCITE-6422](https://issues.apache.org/jira/browse/CALCITE-6422)\]
Query with “`<>`” throws `NullPointerException` during materialized view
matching
- \[ [CALCITE-6423](https://issues.apache.org/jira/browse/CALCITE-6423)\]
JDBC adapter for MySQL generates invalid SQL for `CHAR` without precision
- \[ [CALCITE-6244](https://issues.apache.org/jira/browse/CALCITE-6244)\]
Improve `Expressions#constant` to allow Java records
- \[ [CALCITE-6419](https://issues.apache.org/jira/browse/CALCITE-6419)\]
JDBC adapter for Hive and Spark generates invalid SQL for `VARCHAR` without
precision
- \[ [CALCITE-6417](https://issues.apache.org/jira/browse/CALCITE-6417)\]
JDBC adapter for Hive generates wrong SQL for `MAP` and `ARRAY` value
constructors
- \[ [CALCITE-6416](https://issues.apache.org/jira/browse/CALCITE-6416)\]
Remove unnecessary `SUBSTRING` rewrite in `SparkSqlDialect`
- \[ [CALCITE-6415](https://issues.apache.org/jira/browse/CALCITE-6415)\]
Invalid unparse for `TIMESTAMP` with `HiveSqlDialect`
- \[ [CALCITE-6340](https://issues.apache.org/jira/browse/CALCITE-6340)\]
`RelBuilder` drops traits when aggregating over duplicate projected fields
- \[ [CALCITE-6400](https://issues.apache.org/jira/browse/CALCITE-6400)\]
`MAP_ENTRIES` function should throw if a key value is null
- \[ [CALCITE-6389](https://issues.apache.org/jira/browse/CALCITE-6389)\]
`RexBuilder.removeCastFromLiteral` does not preserve semantics for some types of
literal
- \[ [CALCITE-6382](https://issues.apache.org/jira/browse/CALCITE-6382)\]
Type inference for `SqlLeadLagAggFunction` is incorrect
- \[ [CALCITE-6395](https://issues.apache.org/jira/browse/CALCITE-6395)\]
Significant precision loss when representing `REAL` literals
- \[ [CALCITE-6377](https://issues.apache.org/jira/browse/CALCITE-6377)\]
`TIME` expression causes `IllegalStateException`
- \[ [CALCITE-6361](https://issues.apache.org/jira/browse/CALCITE-6361)\]
`Uncollect.deriveUncollectRowType` throws `AssertionError` if the input value
is not a collection
- \[ [CALCITE-6376](https://issues.apache.org/jira/browse/CALCITE-6376)\]
Selecting 6 columns with `QUALIFY` operation results in exception

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-38-0 "Permalink")

- \[ [CALCITE-6609](https://issues.apache.org/jira/browse/CALCITE-6609)\]
Remove redundant warning suppression for Guava’s `Beta` and `Unstable` APIs
- \[ [CALCITE-6493](https://issues.apache.org/jira/browse/CALCITE-6493)\]
Add MySQL and other professional term restrictions
- \[ [CALCITE-6580](https://issues.apache.org/jira/browse/CALCITE-6580)\]
Remove uses of method `Locale.setDefault`
- Try automatically marking PRs as stale
- \[ [CALCITE-6572](https://issues.apache.org/jira/browse/CALCITE-6572)\]
Add more tests for `NULL` arguments to `TO_CHAR` functions
- Add tests for year month intervals
- Add `cast.iq`, a Quidem test for `CAST`
- \[ [CALCITE-6552](https://issues.apache.org/jira/browse/CALCITE-6552)\]
Enable CheckerFramework in ‘server’ module
- Remove `FENNEL_VM`; enable some disabled tests
- \[ [CALCITE-6526](https://issues.apache.org/jira/browse/CALCITE-6526)\]
Refactor `DEVELOCITY_ACCESS_KEY` definition in one place
- \[ [CALCITE-5034](https://issues.apache.org/jira/browse/CALCITE-5034)\]
Remove unused remote S3 build cache
- Enable more tests in `RelBuilderExample`
- \[ [CALCITE-6515](https://issues.apache.org/jira/browse/CALCITE-6515)\]
Remove constants describing which bugs have been fixed in Bug
- \[ [CALCITE-6514](https://issues.apache.org/jira/browse/CALCITE-6514)\]
Enable tests about `AssertionError` while translating `IN`-list that contains
`NULL`
- \[ [CALCITE-6496](https://issues.apache.org/jira/browse/CALCITE-6496)\]
Enable tests from `outer.iq`
- \[ [CALCITE-6490](https://issues.apache.org/jira/browse/CALCITE-6490)\]
Missing tests for `SqlFunctions.overlay`
- \[ [CALCITE-6511](https://issues.apache.org/jira/browse/CALCITE-6511)\]
Migrate from Gradle Enterprise Gradle Plugin to Develocity Gradle Plugin
- \[ [CALCITE-6484](https://issues.apache.org/jira/browse/CALCITE-6484)\]
Sonar analysis fails intermittently due to `OutOfMemoryError`
- \[ [CALCITE-6497](https://issues.apache.org/jira/browse/CALCITE-6497)\]
Use helper setup method throughout whole `ElasticsearchAdapterTest`
- Add Steelwheels data set
- \[ [CALCITE-6470](https://issues.apache.org/jira/browse/CALCITE-6470)\]
Run specific JMH benchmarks without modifying sources
- \[ [CALCITE-6466](https://issues.apache.org/jira/browse/CALCITE-6466)\]
Add benchmark for SQL parser instantiation
- Add `testSortRemoveConstantKeyWhenOrderByIsNull` in `RelOptRulesTest`
- Test case for
\[ [CALCITE-4921](https://issues.apache.org/jira/browse/CALCITE-4921)\]
Nested `NATURAL JOIN` or `JOIN` with `USING` can’t find common column
- Remove conditional `stream.iq` execution

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-38-0 "Permalink")

- \[ [CALCITE-6531](https://issues.apache.org/jira/browse/CALCITE-6531)\]
Correct Javadoc example in `SqlStaticAggFunction.constant`
- Change Mihai Budiu’s role
- \[ [CALCITE-6487](https://issues.apache.org/jira/browse/CALCITE-6487)\]
`TRIM` function documentation refers to `string1` two times
- Improve `OVERLAY` operator docs and fix typo in exception
- Document `MAP` types in grammar
- \[ [CALCITE-6428](https://issues.apache.org/jira/browse/CALCITE-6428)\]
Typo in adapter documentation
- \[ [CALCITE-6383](https://issues.apache.org/jira/browse/CALCITE-6383)\]
`class SameOperandTypeChecker` is incorrectly documented

## [1.37.0](https://github.com/apache/calcite/releases/tag/calcite-1.37.0) / 2024-05-06 [Permalink](https://calcite.apache.org/docs/history.html\#v1-37-0 "Permalink")

This release comes 5 months after [1.36.0](https://calcite.apache.org/docs/history.html#v1-36-0),
contains contributions from 46 contributors, and resolves 138 issues.
It’s worth highlighting the introduction of adapter for Apache Arrow
(\[ [CALCITE-2040](https://issues.apache.org/jira/browse/CALCITE-2040)\]),
StarRocks dialect
(\[ [CALCITE-6257](https://issues.apache.org/jira/browse/CALCITE-6257)\]).
The release also added support for lambda expressions in SQL
(\[ [CALCITE-3679](https://issues.apache.org/jira/browse/CALCITE-3679)\]),
‘must-filter’ columns
(\[ [CALCITE-6219](https://issues.apache.org/jira/browse/CALCITE-6219)\]).
For table function calls it is now possible to use them without `TABLE()` wrapper
in `FROM`
(\[ [CALCITE-6254](https://issues.apache.org/jira/browse/CALCITE-6254)\]).
Furthermore, there is support for optional `FORMAT` of `CAST` operator from SQL:2016
(\[ [CALCITE-6254](https://issues.apache.org/jira/browse/CALCITE-6254)\])
and more than 15 new SQL functions in various libraries such as BigQuery,
Postgres and Spark.

Contributors to this release:
abhishekagarwal87,
Adam Kennedy,
Alessandro Solimando,
Barry Kelly,
Benchao Li,
Bruno Volpato,
caicancai,
chen768959,
Clint Wylie,
Corvin Kuebler,
Devaspati Krishnatri,
Dmitry Sysolyatin,
Dylan Chen,
Forward Xu,
Francis Chuang,
Hanumath Maduri,
Hongyu Guo,
James Duong,
Jerin John,
Jiajun Xie,
Julian Hyde,
Leonid Chistov,
maweibin,
Mihai Budiu,
Mingcan Wang,
Niels Pardon,
Norman Jordan,
Oliver Lee,
Paul Jackson,
Ran Tao,
Rob D’Hondt,
Ruben Quesada Lopez,
Sergey Nuyanzin (release manager),
Stamatis Zampetakis,
Tanner Clary,
Tim Nieradzik,
TJ Banghart,
Ulrich Kramer,
Will Noble,
xinqiu.hu,
Yingyu Wang,
YiwenWu,
Yubin Li,
Zhengqiang Duan,
zhujiang,
zstan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 19;
Guava versions 21.0 to 32.1.3-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-37-0 "Permalink")

- In the context of
\[ [CALCITE-6015](https://issues.apache.org/jira/browse/CALCITE-6015)\]
the visibility of the method `SqlCall.getCallSignature` has been converted
from `protected` to `public`.
Any subclass overriding it will need to be adjusted accordingly.
- \[ [CALCITE-6321](https://issues.apache.org/jira/browse/CALCITE-6321)\]
Add `copy(List<RexLiteral>)` method to `Window` class
- As a consequence of the support for lambda expressions
(\[ [CALCITE-3679](https://issues.apache.org/jira/browse/CALCITE-3679)\])
new methods have been added to `RexVisitor`and `RexBiVisitor`;
any class implementing one of them will have to implement the new methods.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-37-0 "Permalink")

- Supporting new functions
  - \[ [CALCITE-6205](https://issues.apache.org/jira/browse/CALCITE-6205)\]
    Add `BITAND_AGG`, `BITOR_AGG` functions (enabled in Snowflake library)
  - \[ [CALCITE-6156](https://issues.apache.org/jira/browse/CALCITE-6156)\]
    Add `ENDSWITH`, `STARTSWITH` functions (enabled in Postgres, Snowflake libraries)
  - \[ [CALCITE-6116](https://issues.apache.org/jira/browse/CALCITE-6116)\]
    Add `EXISTS` function (enabled in Spark library)
  - \[ [CALCITE-6182](https://issues.apache.org/jira/browse/CALCITE-6182)\]
    Add `LENGTH`/`LEN` functions (enabled in Snowflake library)
  - \[ [CALCITE-6224](https://issues.apache.org/jira/browse/CALCITE-6224)\]
    Add `LOG2` function (enabled in MySQL, Spark library)
  - \[ [CALCITE-6223](https://issues.apache.org/jira/browse/CALCITE-6223)\]
    Add `MAP_CONTAINS_KEY` function (enabled in Spark library)
  - \[ [CALCITE-6314](https://issues.apache.org/jira/browse/CALCITE-6314)\]
    Add `RANDOM` function (enabled in Postgres library)
  - \[ [CALCITE-6315](https://issues.apache.org/jira/browse/CALCITE-6315)\]
    Support Postgres `TO_CHAR`, `TO_DATE`, `TO_TIMESTAMP`
  - \[ [CALCITE-6278](https://issues.apache.org/jira/browse/CALCITE-6278)\]
    Add `REGEXP`, `REGEXP_LIKE` function (enabled in Spark library)
  - \[ [CALCITE-6309](https://issues.apache.org/jira/browse/CALCITE-6309)\]
    Add `REGEXP_LIKE` function (enabled in MySQL, Oracle, Postgres and Spark
    libraries)
  - \[ [CALCITE-6179](https://issues.apache.org/jira/browse/CALCITE-6179)\]
    Support `WEEKOFMONTH` function format and add test
- \[ [CALCITE-6215](https://issues.apache.org/jira/browse/CALCITE-6215)\]
Support century format datetime/timestamp in pg
- \[ [CALCITE-6268](https://issues.apache.org/jira/browse/CALCITE-6268)\]
Support implementing custom `JdbcSchema`
- \[ [CALCITE-6255](https://issues.apache.org/jira/browse/CALCITE-6255)\]
Support BigQuery-style `JSON_OBJECT` invocation syntax
- \[ [CALCITE-6219](https://issues.apache.org/jira/browse/CALCITE-6219)\]
‘Must-filter’ columns
- \[ [CALCITE-2980](https://issues.apache.org/jira/browse/CALCITE-2980)\]
Implement the `FORMAT` clause of the `CAST` operator
- \[ [CALCITE-3679](https://issues.apache.org/jira/browse/CALCITE-3679)\]
Allow lambda expressions in SQL queries
- \[ [CALCITE-3329](https://issues.apache.org/jira/browse/CALCITE-3329)\]
Implement osquery for OS adapter
- \[ [CALCITE-2040](https://issues.apache.org/jira/browse/CALCITE-2040)\]
Create adapter for Apache Arrow
- \[ [CALCITE-6257](https://issues.apache.org/jira/browse/CALCITE-6257)\]
StarRocks dialect implementation
- \[ [CALCITE-6254](https://issues.apache.org/jira/browse/CALCITE-6254)\]
Support table function calls in `FROM` clause without `TABLE()` wrapper
- \[ [CALCITE-6138](https://issues.apache.org/jira/browse/CALCITE-6138)\]
Add parser support for `TIME WITH TIME ZONE` and `TIMESTAMP WITH TIME ZONE` as
a data type

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-37-0 "Permalink")

- \[ [CALCITE-6124](https://issues.apache.org/jira/browse/CALCITE-6124)\]
Bump json-path from 2.7.0 to 2.8.0
- \[ [CALCITE-6229](https://issues.apache.org/jira/browse/CALCITE-6229)\]
Bump json-path from 2.8.0 to 2.9.0
- \[ [CALCITE-6378](https://issues.apache.org/jira/browse/CALCITE-6378)\]
Bump Redis Docker image from 2.8.19 to 7.2.4
- \[ [CALCITE-6356](https://issues.apache.org/jira/browse/CALCITE-6356)\]
Upgrade Calcite to Avatica 1.25.0
- \[ [CALCITE-6243](https://issues.apache.org/jira/browse/CALCITE-6243)\]
Upgrade Cassandra to 4.1.3 and DataStax driver for Cassandra to 4.17.0
- \[ [CALCITE-6181](https://issues.apache.org/jira/browse/CALCITE-6181)\]
Upgrade Janino from 3.1.9 to 3.1.11
- \[ [CALCITE-6119](https://issues.apache.org/jira/browse/CALCITE-6119)\]
Upgrade testcontainers to 1.19.3
- \[ [CALCITE-6081](https://issues.apache.org/jira/browse/CALCITE-6081)\]
Remove bouncycastle dependency

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-37-0 "Permalink")

- \[ [CALCITE-6355](https://issues.apache.org/jira/browse/CALCITE-6355)\]
`RelToSqlConverter[ORDER BY]` generates an incorrect order by when
`NULLS LAST` is used in non-projected field
- \[ [CALCITE-6210](https://issues.apache.org/jira/browse/CALCITE-6210)\]
Cast to `VARBINARY` causes an assertion failure
- \[ [CALCITE-5289](https://issues.apache.org/jira/browse/CALCITE-5289)\]
Assertion failure in `MultiJoinOptimizeBushyRule`
- \[ [CALCITE-6345](https://issues.apache.org/jira/browse/CALCITE-6345)\]
Intervals with more than 100 years are not supported
- \[ [CALCITE-6265](https://issues.apache.org/jira/browse/CALCITE-6265)\]
Type coercion is failing for numeric values in prepared statements (follow-up)
- \[ [CALCITE-6248](https://issues.apache.org/jira/browse/CALCITE-6248)\]
Illegal dates are accepted by casts
- \[ [CALCITE-6282](https://issues.apache.org/jira/browse/CALCITE-6282)\]
Avatica ignores time precision when returning `TIME` results
- \[ [CALCITE-6338](https://issues.apache.org/jira/browse/CALCITE-6338)\]
`RelMdCollation#project` can return an incomplete list of collations in the
presence of aliasing
- \[ [CALCITE-5976](https://issues.apache.org/jira/browse/CALCITE-5976)\]
Function `ARRAY_PREPEND`/`ARRAY_APPEND`/`ARRAY_INSERT` gives exception when
inserted element type not equals array component type
- \[ [CALCITE-6349](https://issues.apache.org/jira/browse/CALCITE-6349)\]
`CoreRules.PROJECT_REDUCE_EXPRESSIONS` crashes on expressions with `ARRAY_REPEAT`
- \[ [CALCITE-6333](https://issues.apache.org/jira/browse/CALCITE-6333)\]
`NullPointerException` in `AggregateExpandDistinctAggregatesRule.doRewrite`
when rewriting filtered distinct aggregation
- \[ [CALCITE-6285](https://issues.apache.org/jira/browse/CALCITE-6285)\]
Function `ARRAY_INSERT` produces an incorrect result for negative indices
- \[ [CALCITE-6015](https://issues.apache.org/jira/browse/CALCITE-6015)\]
`AssertionError` during optimization of `EXTRACT` expression
- \[ [CALCITE-6317](https://issues.apache.org/jira/browse/CALCITE-6317)\]
Incorrect constant replacement when group keys are `NULL`
- \[ [CALCITE-6348](https://issues.apache.org/jira/browse/CALCITE-6348)\]
`ARRAY_OVERLAP` with a `NULL` argument crashes the compiler
- \[ [CALCITE-6347](https://issues.apache.org/jira/browse/CALCITE-6347)\]
`ARRAY_REPEAT` with a string argument causes a compiler crash
- \[ [CALCITE-6127](https://issues.apache.org/jira/browse/CALCITE-6127)\]
The spark array function gives `NullPointerException` when element is row type
- \[ [CALCITE-6074](https://issues.apache.org/jira/browse/CALCITE-6074)\]
The size of `REAL`, `DOUBLE`, and `FLOAT` is not consistent
- \[ [CALCITE-6115](https://issues.apache.org/jira/browse/CALCITE-6115)\]
Interval type specifier with zero fractional second precision does not pass
validation
- \[ [CALCITE-5955](https://issues.apache.org/jira/browse/CALCITE-5955)\]
BigQuery `PERCENTILE` functions are unparsed incorrectly
- \[ [CALCITE-6048](https://issues.apache.org/jira/browse/CALCITE-6048)\]
`ServerTest#testTruncateTable` fails intermittently due to method not found
exception
- \[ [CALCITE-5811](https://issues.apache.org/jira/browse/CALCITE-5811)\]
Error messages produced for constant out-of-bounds arguments are confusing
- \[ [CALCITE-6128](https://issues.apache.org/jira/browse/CALCITE-6128)\]
`RelBuilder.limit` should apply offset and fetch to previous Sort operator,
if possible
- \[ [CALCITE-6118](https://issues.apache.org/jira/browse/CALCITE-6118)\]
Missing empty `ARRAY` function usage in reference doc
- \[ [CALCITE-6121](https://issues.apache.org/jira/browse/CALCITE-6121)\]
Invalid unparse for `TIMESTAMP` with `SparkSqlDialect`
- \[ [CALCITE-6109](https://issues.apache.org/jira/browse/CALCITE-6109)\]
Linq4j `OptimizeShuttle` should not create new instances of
`TernaryExpression` if it does not do any optimization
- \[ [CALCITE-6095](https://issues.apache.org/jira/browse/CALCITE-6095)\]
Arithmetic expression with `VARBINARY` value causes AssertionFailure
- \[ [CALCITE-6150](https://issues.apache.org/jira/browse/CALCITE-6150)\]
JDBC adapter for ClickHouse generates incorrect SQL for certain units in the
`EXTRACT` function
- \[ [CALCITE-6117](https://issues.apache.org/jira/browse/CALCITE-6117)\]
Converting `SAFE_CAST` from `RexCall` to `SqlCall` fails to add the type as an
argument
- \[ [CALCITE-6211](https://issues.apache.org/jira/browse/CALCITE-6211)\]
`SUBSTRING` with `Integer.MIN_VALUE` as a second parameter raise unexpected
exception
- \[ [CALCITE-6213](https://issues.apache.org/jira/browse/CALCITE-6213)\]
The default behavior of `NullCollation` in Presto is `LAST`
- \[ [CALCITE-6227](https://issues.apache.org/jira/browse/CALCITE-6227)\]
`ELEMENT(NULL)` causes an assertion failure
- \[ [CALCITE-6168](https://issues.apache.org/jira/browse/CALCITE-6168)\]
`RexExecutor` can throw during compilation
- \[ [CALCITE-5130](https://issues.apache.org/jira/browse/CALCITE-5130)\]
`AssertionError`: “Conversion to relational algebra failed to preserve datatypes”
when union `VARCHAR` literal and `CAST(null AS INTEGER)`
- \[ [CALCITE-6178](https://issues.apache.org/jira/browse/CALCITE-6178)\]
`WITH RECURSIVE` query when cloned using `SqlShuttle` loses `RECURSIVE` property
- \[ [CALCITE-6332](https://issues.apache.org/jira/browse/CALCITE-6332)\]
Optimization `CoreRules.AGGREGATE_EXPAND_DISTINCT_AGGREGATES_TO_JOIN` produces
incorrect results for aggregates with groupSets
- \[ [CALCITE-6353](https://issues.apache.org/jira/browse/CALCITE-6353)\]
Optimization `CoreRules.PROJECT_REDUCE_EXPRESSIONS` crashes while optimizing
`ARRAY_CONCAT` expression
- \[ [CALCITE-6262](https://issues.apache.org/jira/browse/CALCITE-6262)\]
`CURRENT_TIMESTAMP(P)` ignores `DataTypeSystem#getMaxPrecision`
- \[ [CALCITE-6283](https://issues.apache.org/jira/browse/CALCITE-6283)\]
Function `ARRAY_APPEND` with a `NULL` array argument crashes with
`NullPointerException`
- \[ [CALCITE-6306](https://issues.apache.org/jira/browse/CALCITE-6306)\]
JDBC adapter should not generate `FILTER` (`WHERE`) in MySQL and StarRocks dialect
- \[ [CALCITE-5893](https://issues.apache.org/jira/browse/CALCITE-5893)\]
Wrong `NULL` operand behavior of
`ARRAY_CONTAINS`/`ARRAY_EXCEPT`/`ARRAY_INTERSECT` in Spark library
- \[ [CALCITE-6290](https://issues.apache.org/jira/browse/CALCITE-6290)\]
Incorrect return type for BigQuery `TRUNC`
- \[ [CALCITE-6252](https://issues.apache.org/jira/browse/CALCITE-6252)\]
BigQuery `FORMAT_DATE` uses the wrong calendar for Julian dates
- \[ [CALCITE-6214](https://issues.apache.org/jira/browse/CALCITE-6214)\]
Remove `DISTINCT` in aggregate function if field is unique
- \[ [CALCITE-6258](https://issues.apache.org/jira/browse/CALCITE-6258)\]
Map value constructor is unparsed incorrectly for `PrestoSqlDialect`
- \[ [CALCITE-6249](https://issues.apache.org/jira/browse/CALCITE-6249)\]
`RelNode::estimatedRowCount` should not be used in `computeSelfCost`
- \[ [CALCITE-6251](https://issues.apache.org/jira/browse/CALCITE-6251)\]
`InnerEnumerator` in `EnumerableDefaults::correlateBatchJoin` is not closed
- \[ [CALCITE-6247](https://issues.apache.org/jira/browse/CALCITE-6247)\]
BigQuery `FORMAT_DATE` function handles incorrectly the `%e` format specifier
- \[ [CALCITE-6238](https://issues.apache.org/jira/browse/CALCITE-6238)\]
Exception while evaluating `ROUND`/`TRUNCATE` functions
- \[ [CALCITE-6228](https://issues.apache.org/jira/browse/CALCITE-6228)\]
`ELEMENT` function infers incorrect return type
- \[ [CALCITE-5647](https://issues.apache.org/jira/browse/CALCITE-5647)\]
`RelMdPopulationSize` should use `mq.getRowCount(rel)` instead of
`rel.estimateRowCount(mq)`
- \[ [CALCITE-6241](https://issues.apache.org/jira/browse/CALCITE-6241)\]
Enable a few existing functions to Spark library
- \[ [CALCITE-6094](https://issues.apache.org/jira/browse/CALCITE-6094)\]
`Linq4j.ConstantExpression.write` crashes on special FP values
- \[ [CALCITE-6190](https://issues.apache.org/jira/browse/CALCITE-6190)\]
Incorrect precision derivation for negative numeric types
- \[ [CALCITE-6202](https://issues.apache.org/jira/browse/CALCITE-6202)\]
`sqlsh` does not print error message when query fails
- \[ [CALCITE-6200](https://issues.apache.org/jira/browse/CALCITE-6200)\]
`RelJson` throw `UnsupportedOperationException` for `RexDynamicParam`
- \[ [CALCITE-6044](https://issues.apache.org/jira/browse/CALCITE-6044)\]
`RelMetadataQuery` should regard single-row relational expressions as unique
- \[ [CALCITE-5846](https://issues.apache.org/jira/browse/CALCITE-5846)\]
Preserve filters on non-distinct aggCalls in `AggregateExpandWithinDistinctRule`
- \[ [CALCITE-6100](https://issues.apache.org/jira/browse/CALCITE-6100)\]
The `equalsDeep` of `SqlRowTypeNameSpec` should use `equalsDeep` for fieldTypes
rather than reference comparison
- \[ [CALCITE-6183](https://issues.apache.org/jira/browse/CALCITE-6183)\]
The second parameter of `RexProgramBuilder#registerInternal` is always false
- \[ [CALCITE-6149](https://issues.apache.org/jira/browse/CALCITE-6149)\]
Unparse for `CAST` Nullable with `ClickHouseSqlDialect`
- \[ [CALCITE-5649](https://issues.apache.org/jira/browse/CALCITE-5649)\]
Get row count statistics from `ReflectiveSchema`
- \[ [CALCITE-6220](https://issues.apache.org/jira/browse/CALCITE-6220)\]
Rewrite `MIN`/`MAX(bool)` as `BOOL_AND`/`BOOL_OR` for Postgres, Redshift
- \[ [CALCITE-6321](https://issues.apache.org/jira/browse/CALCITE-6321)\]
Add `copy(List<RexLiteral>)` method to Window class
- \[ [CALCITE-6337](https://issues.apache.org/jira/browse/CALCITE-6337)\]
Distinguish naked measure support between inside and outside aggregation
- \[ [CALCITE-6323](https://issues.apache.org/jira/browse/CALCITE-6323)\]
Serialize return type during `RelJson.toJson(RexNode node)` for `SqlKind.SAFE_CAST`
- \[ [CALCITE-6111](https://issues.apache.org/jira/browse/CALCITE-6111)\]
Explicit cast from expression to numeric type doesn’t check overflow
- \[ [CALCITE-6162](https://issues.apache.org/jira/browse/CALCITE-6162)\]
Add rule(s) to remove joins with constant single tuple relations
- \[ [CALCITE-6192](https://issues.apache.org/jira/browse/CALCITE-6192)\]
`DEFAULT` expression with `NULL` value throws unexpected exception
- \[ [CALCITE-6147](https://issues.apache.org/jira/browse/CALCITE-6147)\]
`CAST(CAST(EMPNO AS VARCHAR) AS INT)` should be simplified to `EMPNO`
- \[ [CALCITE-6102](https://issues.apache.org/jira/browse/CALCITE-6102)\]
`SqlWriter` in `SqlInsert`’s unparse start a list but does not end it
- \[ [CALCITE-5607](https://issues.apache.org/jira/browse/CALCITE-5607)\]
Serialize return type during `RelJson.toJson(RexNode node)` for `SqlKind.MINUS`
- \[ [CALCITE-6269](https://issues.apache.org/jira/browse/CALCITE-6269)\]
Fix missing/broken BigQuery date-time format elements
- \[ [CALCITE-6231](https://issues.apache.org/jira/browse/CALCITE-6231)\]
JDBC adapter generates `UNNEST` when it should generate `UNNEST ... WITH ORDINALITY`
- \[ [CALCITE-6208](https://issues.apache.org/jira/browse/CALCITE-6208)\]
Update `JSON_VALUE` return type inference to make explicit array return types
be nullable with nullable elements
- \[ [CALCITE-6199](https://issues.apache.org/jira/browse/CALCITE-6199)\]
Trim unused fields for `SNAPSHOT` and `SAMPLE` if table has `VIRTUAL` column
- \[ [CALCITE-6063](https://issues.apache.org/jira/browse/CALCITE-6063)\]
If `ARRAY` subquery has `ORDER BY` (without `LIMIT`), rows are not sorted
- \[ [CALCITE-6032](https://issues.apache.org/jira/browse/CALCITE-6032)\]
Multilevel correlated query is failing in `RelDecorrelator` code path

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-37-0 "Permalink")

- \[ [CALCITE-6103](https://issues.apache.org/jira/browse/CALCITE-6103)\]
Use eclipse-temurin image to build and publish javadocs for the website
- \[ [CALCITE-6131](https://issues.apache.org/jira/browse/CALCITE-6131)\]
There are duplicate sample tests in `SqlTypeUtilTest`
- \[ [CALCITE-6125](https://issues.apache.org/jira/browse/CALCITE-6125)\]
Automate generation of contributor names in release notes by adding a git
mailmap file
- \[ [CALCITE-6165](https://issues.apache.org/jira/browse/CALCITE-6165)\]
Add `DATE_ADD` test and `DATE_DIFF` test on `SqlOperatorTest`
- \[ [CALCITE-6184](https://issues.apache.org/jira/browse/CALCITE-6184)\]
Add `checkNullTest` on `SqlOperatorTest`
- \[ [CALCITE-6187](https://issues.apache.org/jira/browse/CALCITE-6187)\]
Linter should disallow tags such as `[MINOR]` in commit messages
- \[ [CALCITE-6273](https://issues.apache.org/jira/browse/CALCITE-6273)\]
Add sqrt negative test in `SqlOperatorTest`
- \[ [CALCITE-6189](https://issues.apache.org/jira/browse/CALCITE-6189)\]
Improve `FormatElementEnumTest`
- \[ [CALCITE-6234](https://issues.apache.org/jira/browse/CALCITE-6234)\]
Add tests on `SqlOperatorTest` for `to_char` function
- \[ [CALCITE-6172](https://issues.apache.org/jira/browse/CALCITE-6172)\]
Allow aliased operators to re-use existing tests
- \[ [CALCITE-6359](https://issues.apache.org/jira/browse/CALCITE-6359)\]
Update GitHub Actions workflows to use docker compose v2
- \[ [CALCITE-6092](https://issues.apache.org/jira/browse/CALCITE-6092)\]
Skip breaking `CAST` String to `TIME` tests until fixed in Avatica 1.24.0
- \[ [CALCITE-6384](https://issues.apache.org/jira/browse/CALCITE-6384)\]
Add ASF header to `buildcache.yml`, `gradle-wrapper-validation.yml`
- \[ [CALCITE-6385](https://issues.apache.org/jira/browse/CALCITE-6385)\]
LintTest fails when run in source distribution
- \[ [CALCITE-6387](https://issues.apache.org/jira/browse/CALCITE-6387)\]
Make Arrow adapter passing tests with jdk17+
- \[ [CALCITE-6390](https://issues.apache.org/jira/browse/CALCITE-6390)\]
Exclude Arrow project on Windows builds

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-37-0 "Permalink")

- Site: Switch PMC Chair to Benchao Li
- Site: Troubleshooting/Website publishing improvements in release guide
- Site: Remove committer by request process
- \[ [CALCITE-6083](https://issues.apache.org/jira/browse/CALCITE-6083)\]
On web site, ensure contributors file is sorted
- \[ [CALCITE-6098](https://issues.apache.org/jira/browse/CALCITE-6098)\]
Update `LICENSE` and `NOTICE` for Jekyll website template
- \[ [CALCITE-6250](https://issues.apache.org/jira/browse/CALCITE-6250)\]
Limitations of MongoDB adapter are not documented
- \[ [CALCITE-6256](https://issues.apache.org/jira/browse/CALCITE-6256)\]
Incorrect rendering of HTML on InnoDB adapter page
- Add `.gitignore` and `.ratignore` for jenv
- \[ [CALCITE-6097](https://issues.apache.org/jira/browse/CALCITE-6097)\]
Gridism CSS dependency is mispelled in `LICENSE`
- \[ [CALCITE-6096](https://issues.apache.org/jira/browse/CALCITE-6096)\]
Remove obsolete html5shiv and respond entries from `LICENSE`
- \[ [CALCITE-6194](https://issues.apache.org/jira/browse/CALCITE-6194)\]
Contributor rules do not give instructions about how to quote commits
- \[ [CALCITE-6212](https://issues.apache.org/jira/browse/CALCITE-6212)\]
Config `locale = 'en_US'` for javadoc task
- \[ [CALCITE-6316](https://issues.apache.org/jira/browse/CALCITE-6316)\]
Update Javadoc for `RelWriterTest#testDeserializeMinusDateOperator`
- \[ [CALCITE-6105](https://issues.apache.org/jira/browse/CALCITE-6105)\]
Documentation does not specify the behavior of `SPLIT` function for empty
string arguments

## [1.36.0](https://github.com/apache/calcite/releases/tag/calcite-1.36.0) / 2023-11-10 [Permalink](https://calcite.apache.org/docs/history.html\#v1-36-0 "Permalink")

This release comes 3 months after [1.35.0](https://calcite.apache.org/docs/history.html#v1-35-0),
contains contributions from 30 contributors, and resolves 125 issues.

Among other new features, it’s worth highlighting the adding of 30 new
SQL functions in various libraries such as BigQuery and Spark, many
improvements hardening `TABLESAMPLE`, and also the following features:

- \[ [CALCITE-129](https://issues.apache.org/jira/browse/CALCITE-129)\]
Support recursive `WITH` queries
- \[ [CALCITE-6022](https://issues.apache.org/jira/browse/CALCITE-6022)\]
Support `CREATE TABLE ... LIKE DDL` in server module
- \[ [CALCITE-5962](https://issues.apache.org/jira/browse/CALCITE-5962)\]
Support parse Spark-style syntax `LEFT ANTI JOIN` in Babel parser
- \[ [CALCITE-5184](https://issues.apache.org/jira/browse/CALCITE-5184)\]
Support `LIMIT start, ALL` in MySQL conformance, equivalent to `OFFSET start`
- \[ [CALCITE-5889](https://issues.apache.org/jira/browse/CALCITE-5889)\]
Add a `RelRule` that converts `Minus` into `UNION ALL..GROUP BY...WHERE`

In addition to new features, it’s also worth highlighting the
integrating of
[SQL Logic Test suite](https://issues.apache.org/jira/browse/CALCITE-5615).

Contributors to this release:
Benchao Li (release manager),
Cancai Cai,
Claude Brisson,
Evgeniy Stanilovskiy,
Hanumath Maduri,
Hongyu Guo,
Itiel Sadeh,
Jerin John,
Jiajun Xie,
Julian Hyde,
Kaustubh Beedkar,
Lei Shen,
Leonid Chistov,
Michael Mior,
Mihai Budiu,
Mingcan Wang,
Oliver Lee,
Ran Tao,
Ruben Quesada Lopez,
Runkang He,
Tanner Clary,
Thomas Rebele,
Tim Nieradzik,
Wang Zhao,
Wegdan Ghazi,
Wenrui Meng,
Xiaogang Zhou,
ZhangJian He,
Zhengqiang Duan,
Zoltan Haindrich.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 19;
Guava versions 21.0 to 32.1.3-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-36-0 "Permalink")

None.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-36-0 "Permalink")

- Supporting new SQL functions in BigQuery, Hive and Spark libraries:
  - \[ [CALCITE-5826](https://issues.apache.org/jira/browse/CALCITE-5826)\]
    Add `FIND_IN_SET` function (enabled in Hive and Spark libraries)
  - \[ [CALCITE-5979](https://issues.apache.org/jira/browse/CALCITE-5979)\]
    Enable `REGEXP_REPLACE` function in BigQuery library
  - \[ [CALCITE-6077](https://issues.apache.org/jira/browse/CALCITE-6077)\]
    Add `FACTORIAL` function (enabled in Hive and Spark libraries)
  - \[ [CALCITE-5918](https://issues.apache.org/jira/browse/CALCITE-5918)\]
    Add `MAP` function (enabled in Spark library)
  - \[ [CALCITE-5825](https://issues.apache.org/jira/browse/CALCITE-5825)\]
    Add `URL_ENCODE` and `URL_DECODE` function (enabled in Spark library)
  - \[ [CALCITE-6021](https://issues.apache.org/jira/browse/CALCITE-6021)\]
    Add `CURRENT_DATETIME` function (enabled in BigQuery library)
  - \[ [CALCITE-5993](https://issues.apache.org/jira/browse/CALCITE-5993)\]
    Add `CODE_POINTS_TO_STRING`, `TO_CODE_POINTS` function (enabled in BigQuery library)
  - \[ [CALCITE-5978](https://issues.apache.org/jira/browse/CALCITE-5978)\]
    Add `REGEXP_INSTR` function (enabled in BigQuery library)
  - \[ [CALCITE-5935](https://issues.apache.org/jira/browse/CALCITE-5935)\]
    Add `CODE_POINTS_TO_BYTES` function (enabled in BigQuery library)
  - \[ [CALCITE-5933](https://issues.apache.org/jira/browse/CALCITE-5933)\]
    Add `SAFE_DIVIDE` function (enabled in BigQuery library)
  - \[ [CALCITE-5821](https://issues.apache.org/jira/browse/CALCITE-5821)\]
    Add `FORMAT_NUMBER` function (enabled in Hive and Spark library)
  - \[ [CALCITE-5911](https://issues.apache.org/jira/browse/CALCITE-5911)\]
    Add `REGEXP_EXTRACT_ALL` function (enabled in BigQuery library)
  - \[ [CALCITE-5910](https://issues.apache.org/jira/browse/CALCITE-5910)\]
    Add `REGEXP_EXTRACT` and `REGEXP_SUBSTR` functions (enabled in BigQuery library)
  - \[ [CALCITE-5766](https://issues.apache.org/jira/browse/CALCITE-5766)\]
    Add `SAFE_NEGATE` function (enabled for BigQuery library)
  - \[ [CALCITE-5770](https://issues.apache.org/jira/browse/CALCITE-5770)\]
    Add `SAFE_SUBTRACT` function (enabled in BigQuery library)
  - \[ [CALCITE-5848](https://issues.apache.org/jira/browse/CALCITE-5848)\]
    Add `BIT_GET` and `GETBIT` functions (enabled in Spark library)
  - \[ [CALCITE-5644](https://issues.apache.org/jira/browse/CALCITE-5644)\]
    Add `CONTAINS_SUBSTR` function (enabled in BigQuery library)
  - \[ [CALCITE-5640](https://issues.apache.org/jira/browse/CALCITE-5640)\]
    Add `SAFE_ADD` function (enabled in BigQuery library)
  - \[ [CALCITE-5830](https://issues.apache.org/jira/browse/CALCITE-5830)\]
    Add `ARRAY_INSERT` function(enabled in Spark library)
  - \[ [CALCITE-5873](https://issues.apache.org/jira/browse/CALCITE-5873)\]
    Add `REGEXP_CONTAINS` function (enabled in BigQuery library)
  - \[ [CALCITE-5827](https://issues.apache.org/jira/browse/CALCITE-5827)\]
    Add `IS_INF` and `IS_NAN` functions (enabled in BigQuery library)
  - \[ [CALCITE-5831](https://issues.apache.org/jira/browse/CALCITE-5831)\]
    Add `SOUNDEX` function (enabled in Spark library)
  - \[ [CALCITE-5735](https://issues.apache.org/jira/browse/CALCITE-5735)\]
    Add `SAFE_MULTIPLY` function (enabled for BigQuery)
  - \[ [CALCITE-5820](https://issues.apache.org/jira/browse/CALCITE-5820)\]
    Add `PARSE_URL` function (enabled in Hive and Spark library)
  - \[ [CALCITE-5851](https://issues.apache.org/jira/browse/CALCITE-5851)\]
    Add `LEVENSHTEIN` function (enabled in Hive and Spark library)
- \[ [CALCITE-129](https://issues.apache.org/jira/browse/CALCITE-129)\]
Support recursive `WITH` queries
- \[ [CALCITE-6011](https://issues.apache.org/jira/browse/CALCITE-6011)\]
Add `FilterWindowTransposeRule` to push a `Filter` past a `Window`
- \[ [CALCITE-6038](https://issues.apache.org/jira/browse/CALCITE-6038)\]
Remove `ORDER BY ... LIMIT n` when input has at most one row, n >= 1, and
there is no `OFFSET` clause
- \[ [CALCITE-6022](https://issues.apache.org/jira/browse/CALCITE-6022)\]
Support `CREATE TABLE ... LIKE DDL` in server module
- \[ [CALCITE-6031](https://issues.apache.org/jira/browse/CALCITE-6031)\]
Add the planner rule that pushes `Filter` past `Sample`
- \[ [CALCITE-4189](https://issues.apache.org/jira/browse/CALCITE-4189)\]
Simplify `p OR (p IS NOT TRUE)` to `TRUE`
- \[ [CALCITE-6009](https://issues.apache.org/jira/browse/CALCITE-6009)\]
Add optimization to remove redundant `LIMIT` that is more than input row count
- \[ [CALCITE-5570](https://issues.apache.org/jira/browse/CALCITE-5570)\]
Support nested map type for `SqlDataTypeSpec`
- \[ [CALCITE-5962](https://issues.apache.org/jira/browse/CALCITE-5962)\]
Support parse Spark-style syntax `LEFT ANTI JOIN` in Babel parser
- \[ [CALCITE-5940](https://issues.apache.org/jira/browse/CALCITE-5940)\]
Add a `RelRule` to merge `Limit`
- \[ [CALCITE-5971](https://issues.apache.org/jira/browse/CALCITE-5971)\]
Add `SampleToFilterRule` to rewrite bernoulli `Sample` to `Filter`
- \[ [CALCITE-5994](https://issues.apache.org/jira/browse/CALCITE-5994)\]
Add optimization rule to remove `Sort` when its input’s row number is less or
equal to one
- \[ [CALCITE-5836](https://issues.apache.org/jira/browse/CALCITE-5836)\]
Implement Rel2Sql for `MERGE`
- \[ [CALCITE-5889](https://issues.apache.org/jira/browse/CALCITE-5889)\]
Add a `RelRule` that converts `Minus` into `UNION ALL..GROUP BY...WHERE`
- \[ [CALCITE-5944](https://issues.apache.org/jira/browse/CALCITE-5944)\]
Add metadata for `Sample`
- \[ [CALCITE-5941](https://issues.apache.org/jira/browse/CALCITE-5941)\]
Support `LITERAL_AGG` in `Interpreter`
- \[ [CALCITE-985](https://issues.apache.org/jira/browse/CALCITE-985)\]
Validate `MERGE`
- \[ [CALCITE-5870](https://issues.apache.org/jira/browse/CALCITE-5870)\]
Allow literals like `DECIMAL '12.3'` (consistent with Postgres)
- \[ [CALCITE-5916](https://issues.apache.org/jira/browse/CALCITE-5916)\]
In `RelBuilder`, add `sample()` method (equivalent to SQL `TABLESAMPLE` clause)
- \[ [CALCITE-5184](https://issues.apache.org/jira/browse/CALCITE-5184)\]
Support `LIMIT start, ALL` in MySQL conformance, equivalent to `OFFSET start`

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-36-0 "Permalink")

- \[ [CALCITE-5763](https://issues.apache.org/jira/browse/CALCITE-5763)\]
Increase minimum Guava version to 21.0, maximum version to 32.1.3-jre, and
stop building on Guava 19.0
- \[ [CALCITE-5938](https://issues.apache.org/jira/browse/CALCITE-5938)\]
Update HSQLDB to Version 2.7.2 (using JDK8 JAR, default supports JDK11+)
- \[ [CALCITE-6004](https://issues.apache.org/jira/browse/CALCITE-6004)\]
Replace deprecated mongo-java-driver dependency
- \[ [CALCITE-5966](https://issues.apache.org/jira/browse/CALCITE-5966)\]
Upgrade commons-dbcp2 to 2.9.0

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-36-0 "Permalink")

- \[ [CALCITE-6088](https://issues.apache.org/jira/browse/CALCITE-6088)\]
`SqlItemOperator` fails in `RelToSqlConverter`
- \[ [CALCITE-5863](https://issues.apache.org/jira/browse/CALCITE-5863)\]
Calcite rejects valid query with multiple `ORDER BY` columns and constant
`RANGE` bounds in window functions
- \[ [CALCITE-5984](https://issues.apache.org/jira/browse/CALCITE-5984)\]
Allow disabling field trimming in `Prepare` via
`SqlToRelConverter.Config#isTrimUnusedFields`
- \[ [CALCITE-5990](https://issues.apache.org/jira/browse/CALCITE-5990)\]
Explicit cast to numeric type doesn’t check overflow
- \[ [CALCITE-6052](https://issues.apache.org/jira/browse/CALCITE-6052)\]
`SqlImplementor` writes `REAL`, `FLOAT`, or `DOUBLE` literals as `DECIMAL` literals
- \[ [CALCITE-6041](https://issues.apache.org/jira/browse/CALCITE-6041)\]
`MAP` sub-query gives `NullPointerException`
- \[ [CALCITE-6037](https://issues.apache.org/jira/browse/CALCITE-6037)\]
The function category of
`ARRAY`/`EXTRACT_VALUE`/`XML_TRANSFORM`/`EXTRACT_XML`/`EXISTSNODE` is incorrect
- \[ [CALCITE-6024](https://issues.apache.org/jira/browse/CALCITE-6024)\]
A more efficient implementation of `SqlOperatorTable`, backed by an immutable
multi-map keyed by upper-case operator name
- \[ [CALCITE-5949](https://issues.apache.org/jira/browse/CALCITE-5949)\]
`RexExecutable` should return unchanged original expressions when it fails
- \[ [CALCITE-6013](https://issues.apache.org/jira/browse/CALCITE-6013)\]
`RelBuilder` should simplify plan by pruning unused measures
- \[ [CALCITE-6040](https://issues.apache.org/jira/browse/CALCITE-6040)\]
The operand type inference of `SqlMapValueConstructor` is incorrect
- \[ [CALCITE-6030](https://issues.apache.org/jira/browse/CALCITE-6030)\]
`DATE_PART` is not handled by the `RexToLixTranslator`
- Following
\[ [CALCITE-5570](https://issues.apache.org/jira/browse/CALCITE-5570)\]
Support nested map type for `SqlDataTypeSpec`
- \[ [CALCITE-6050](https://issues.apache.org/jira/browse/CALCITE-6050)\]
Add interface `ImmutablePairList`
- \[ [CALCITE-5950](https://issues.apache.org/jira/browse/CALCITE-5950)\]
`DEFAULT` expression is ignored during `INSERT`
- \[ [CALCITE-6006](https://issues.apache.org/jira/browse/CALCITE-6006)\]
`RelToSqlConverter` loses charset information
- \[ [CALCITE-5948](https://issues.apache.org/jira/browse/CALCITE-5948)\]
Use explicit casting if element type in `ARRAY`/`MAP` does not equal derived
component type
- \[ [CALCITE-5989](https://issues.apache.org/jira/browse/CALCITE-5989)\]
Type inference for `RPAD` and `LPAD` functions (BIGQUERY) is incorrect
- \[ [CALCITE-5982](https://issues.apache.org/jira/browse/CALCITE-5982)\]
Allow implementations of `CalciteMeta` to return extra columns in their
responses to `DatabaseMetaData.getTables` and `getColumns` requests
- \[ [CALCITE-6007](https://issues.apache.org/jira/browse/CALCITE-6007)\]
Sub-query that contains `WITH` and has no alias generates invalid SQL after
expansion
- \[ [CALCITE-6003](https://issues.apache.org/jira/browse/CALCITE-6003)\]
`JSON_ARRAY()` with no arguments does not unparse correctly
- \[ [CALCITE-6026](https://issues.apache.org/jira/browse/CALCITE-6026)\]
MongoDB: Column is not quoted in `ORDER BY` clause and throws JsonParseException
- \[ [CALCITE-6005](https://issues.apache.org/jira/browse/CALCITE-6005)\]
`POLYGON` string representation is different on Apple silicon
- \[ [CALCITE-5974](https://issues.apache.org/jira/browse/CALCITE-5974)\]
Elasticsearch adapter throws `ClassCastException` when index mapping sets
`dynamic_templates` without `properties`
- \[ [CALCITE-5995](https://issues.apache.org/jira/browse/CALCITE-5995)\]
`JSON_VALUE`, `JSON_EXISTS`, `JSON_QUERY` functions should cache generated
objects between calls
- \[ [CALCITE-5960](https://issues.apache.org/jira/browse/CALCITE-5960)\]
`CAST` throws NullPointerException if `SqlTypeFamily` of targetType is null
- \[ [CALCITE-5997](https://issues.apache.org/jira/browse/CALCITE-5997)\]
`OFFSET` operator is incorrectly unparsed
- \[ [CALCITE-5961](https://issues.apache.org/jira/browse/CALCITE-5961)\]
Type inference of `ARRAY_COMPACT` is incorrect
- \[ [CALCITE-5999](https://issues.apache.org/jira/browse/CALCITE-5999)\]
`DECIMAL` literals as sometimes unparsed looking as `DOUBLE` literals
- \[ [CALCITE-5988](https://issues.apache.org/jira/browse/CALCITE-5988)\]
`SqlImplementor.toSql` cannot emit `VARBINARY` literals
- \[ [CALCITE-5996](https://issues.apache.org/jira/browse/CALCITE-5996)\]
`TRANSLATE` operator is incorrectly unparsed
- \[ [CALCITE-5862](https://issues.apache.org/jira/browse/CALCITE-5862)\]
Incorrect semantics of `ARRAY` function (Spark library) when elements have
Numeric and Character types
- \[ [CALCITE-5931](https://issues.apache.org/jira/browse/CALCITE-5931)\]
Allow round decimals like `1.00` in window ranges
- \[ [CALCITE-5732](https://issues.apache.org/jira/browse/CALCITE-5732)\]
`EnumerableHashJoin` and `EnumerableMergeJoin` on composite key return rows
matching condition `NULL = NULL`
- \[ [CALCITE-5967](https://issues.apache.org/jira/browse/CALCITE-5967)\]
`UnsupportedOperationException` while implementing a call that requires a
special collator
- \[ [CALCITE-5952](https://issues.apache.org/jira/browse/CALCITE-5952)\]
`SemiJoinJoinTransposeRule` should check if JoinType supports pushing
predicates into its inputs
- \[ [CALCITE-5953](https://issues.apache.org/jira/browse/CALCITE-5953)\]
`AggregateCaseToFilterRule` may make inaccurate `SUM` transformations
- \[ [CALCITE-5861](https://issues.apache.org/jira/browse/CALCITE-5861)\]
`ReduceExpressionsRule` rules should constant-fold expressions in window bounds
- \[ [CALCITE-5965](https://issues.apache.org/jira/browse/CALCITE-5965)\]
Avoid unnecessary String concatenations in the `RexFieldAccess` constructor to
improve the performance
- \[ [CALCITE-5914](https://issues.apache.org/jira/browse/CALCITE-5914)\]
Cache compiled regular expressions in SQL function runtime
- Refactor: In `ReflectUtil`, add methods isStatic and isPublic
- Refactor: In `RexImpTable`, ensure that every method is in BuiltInMethod
- \[ [CALCITE-5922](https://issues.apache.org/jira/browse/CALCITE-5922)\]
The SQL generated for the `POSITION` function(with 3 input arguments) by the
`SparkSqlDialect` is not recognized by Spark SQL
- \[ [CALCITE-5920](https://issues.apache.org/jira/browse/CALCITE-5920)\]
Reset `PERCENTILE_CONT`/`PERCENTILE_DISC` to reserved keywords
- \[ [CALCITE-5946](https://issues.apache.org/jira/browse/CALCITE-5946)\]
`TimeString` should allow fractional seconds ending in zero
- \[ [CALCITE-5906](https://issues.apache.org/jira/browse/CALCITE-5906)\]
JDBC adapter should generate `TABLESAMPLE`
- \[ [CALCITE-5895](https://issues.apache.org/jira/browse/CALCITE-5895)\]
`TABLESAMPLE (0)` should return no rows
- \[ [CALCITE-5813](https://issues.apache.org/jira/browse/CALCITE-5813)\]
Type inference for sql functions `REPEAT`, `SPACE`, `XML_TRANSFORM`, and
`XML_EXTRACT` is incorrect
- \[ [CALCITE-5908](https://issues.apache.org/jira/browse/CALCITE-5908)\]
Refactor: Remove unnecessary null checks in `CalciteSchema`
- \[ [CALCITE-5843](https://issues.apache.org/jira/browse/CALCITE-5843)\]
Constant expression with nested casts causes a compiler crash
- \[ [CALCITE-5885](https://issues.apache.org/jira/browse/CALCITE-5885)\]
`SqlNode#toSqlString()` does not honor dialect’s `supportsCharSet()` flag on
nested types
- \[ [CALCITE-5869](https://issues.apache.org/jira/browse/CALCITE-5869)\]
`LEAST_RESTRICTIVE` does not use inner type of `MEASURE` for comparisons
- \[ [CALCITE-5903](https://issues.apache.org/jira/browse/CALCITE-5903)\]
`RelMdCollation` does not define collations for `EnumerableLimit`
- \[ [CALCITE-5882](https://issues.apache.org/jira/browse/CALCITE-5882)\]
Compile-time evaluation of `SPLIT` function returns incorrect result
- \[ [CALCITE-5879](https://issues.apache.org/jira/browse/CALCITE-5879)\]
`AssertionError` during constant reduction of `SPLIT` expression that returns null
- \[ [CALCITE-5875](https://issues.apache.org/jira/browse/CALCITE-5875)\]
Remove unnecessary null checks in Redis adapter
- \[ [CALCITE-5859](https://issues.apache.org/jira/browse/CALCITE-5859)\]
Compile-time evaluation of `LEFT(NULL, n)` should not throw `RuntimeException`
- \[ [CALCITE-5837](https://issues.apache.org/jira/browse/CALCITE-5837)\]
`RexUtil#pullFactors` output’s order should be deterministic even when the
`RexNode` kind is `OR`
- \[ [CALCITE-5877](https://issues.apache.org/jira/browse/CALCITE-5877)\]
`AssertionError` during `MOD` operation if result scale is greater than maximum
numeric scale
- \[ [CALCITE-5841](https://issues.apache.org/jira/browse/CALCITE-5841)\]
Improve singleton implementation for `ChinookAvaticaServer` in calcite-plus
- Following \[ [CALCITE-5688](https://issues.apache.org/jira/browse/CALCITE-5688)\]
Eliminate warnings in server parser

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-36-0 "Permalink")

- \[ [CALCITE-5921](https://issues.apache.org/jira/browse/CALCITE-5921)\]
`SqlOperatorFixture.checkFails` and `checkAggFails` don’t check runtime failure
- \[ [CALCITE-5923](https://issues.apache.org/jira/browse/CALCITE-5923)\]
`SqlOperatorTest` using `safeParameters` are not using overridable fixture
- \[ [CALCITE-6014](https://issues.apache.org/jira/browse/CALCITE-6014)\]
Create a `SqlOperatorFixture` that parses, unparses, and then parses again before executing
- Incorrect test fixture used by `SqlOperatorTest.testLeastFunc`
- \[ [CALCITE-5980](https://issues.apache.org/jira/browse/CALCITE-5980)\]
QuidemTests are not effectively executed on Windows
- \[ [CALCITE-5615](https://issues.apache.org/jira/browse/CALCITE-5615)\]
Run SQL Logic Test suite using Calcite’s HSQLDB JDBC adapter
- \[ [CALCITE-5909](https://issues.apache.org/jira/browse/CALCITE-5909)\]
`SqlParserTest.testNoUnintendedNewReservedKeywords` fails in IDE while passes in command line
- Refactor `RelDataTypeSystemTest` to use test fixture
- Add various lint checks
- Code style: lint
- In `Puffin`, allow an action to test whether it is looking at the last line of a source

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-36-0 "Permalink")

- Site: Add Runkang He as committer
- Site: Add Hongyu Guo as committer
- Site: Add Lei Shen as committer
- Site: Add Ran Tao as committer
- Site: Add Mihai Budiu as committer
- Site: Add Apache Wayang (incubating) to powered-by page
- \[ [CALCITE-5884](https://issues.apache.org/jira/browse/CALCITE-5884)\]
`ARRAY_TO_STRING` function should return `NULL` if its `nullValue` argument is `NULL`
- \[ [CALCITE-6075](https://issues.apache.org/jira/browse/CALCITE-6075)\]
Site: Cloning source code from GitHub using git protocol fails
- Add example for `MAP` type in reference docs
- \[ [CALCITE-6033](https://issues.apache.org/jira/browse/CALCITE-6033)\]
Correct broken links on adapter page
- \[ [CALCITE-6017](https://issues.apache.org/jira/browse/CALCITE-6017)\]
Update the GitHub link of released versions
- \[ [CALCITE-5905](https://issues.apache.org/jira/browse/CALCITE-5905)\]
Documentation for `CREATE TYPE` is incorrect
- Remove mentions of binary distribution from README
- Update broken link in `RelMetadataProvider` Javadoc
- The parameter names of `SqlTypeMappingRules.Builder#add` are misleading

## [1.35.0](https://github.com/apache/calcite/releases/tag/calcite-1.35.0) / 2023-07-26 [Permalink](https://calcite.apache.org/docs/history.html\#v1-35-0 "Permalink")

This release comes 4 months after [1.34.0](https://calcite.apache.org/docs/history.html#v1-34-0),
contains contributions from 36 contributors, and resolves 140 issues.

Among other new features, it adds more than 40 new SQL functions in
various libraries such as BigQuery and Spark.

It is worth highlighting the following improvements:

- Some improvements in calcite core.
  - \[ [CALCITE-5703](https://issues.apache.org/jira/browse/CALCITE-5703)\]
    Reduce amount of generated runtime code
  - \[ [CALCITE-5479](https://issues.apache.org/jira/browse/CALCITE-5479)\]
    `FamilyOperandTypeChecker` is not readily composable in sequences
  - \[ [CALCITE-5425](https://issues.apache.org/jira/browse/CALCITE-5425)\]
    Should not pushdown Filter through Aggregate without group keys
  - \[ [CALCITE-5506](https://issues.apache.org/jira/browse/CALCITE-5506)\]
    `RelToSqlConverter` should retain the aggregation logic when Project without
    `RexInputRef` on the Aggregate
- Some improvements in simplifying an expression.
  - \[ [CALCITE-5769](https://issues.apache.org/jira/browse/CALCITE-5769)\]
    Optimizing `CAST(e AS t) IS NOT NULL` to `e IS NOT NULL`
  - \[ [CALCITE-5780](https://issues.apache.org/jira/browse/CALCITE-5780)\]
    Simplify `1 > x OR 1 <= x OR x IS NULL` to `TRUE`
  - \[ [CALCITE-5798](https://issues.apache.org/jira/browse/CALCITE-5798)\]
    Improve simplification of `(x < y) IS NOT TRUE` when x and y are not nullable
  - \[ [CALCITE-5759](https://issues.apache.org/jira/browse/CALCITE-5759)\]
    `SEARCH(1, Sarg[IS NOT NULL])` should be simplified to `TRUE`
  - \[ [CALCITE-5639](https://issues.apache.org/jira/browse/CALCITE-5639)\]
    `RexSimplify` should remove `IS NOT NULL` check when `LIKE` comparison is present

Contributors to this release:
Adam Kennedy,
Aitozi,
Akshay Dayal,
Benchao Li,
Charles Givre,
Clay Johnson,
Dmitry Sysolyatin,
Evgeny Stanilovsky,
Feng Guo,
Gian Merlino,
Guillaume Massé,
Hongyu Guo,
Ian Bertolacci,
Itiel Sadeh,
Jacky Lau,
Jiajun Xie,
Jiang Zhu
Joey Moore,
Julian Hyde,
Lei Zhang,
Leonid Chistov,
Mihai Budiu,
NobiGo (release manager),
Oliver Lee,
Ran Tao,
Roman Kondakov,
Ruben Quesada Lopez,
Runkang He,
Sergey Nuyanzin,
Stamatis Zampetakis,
TJ Banghart,
Tanner Clary,
Tim Nieradzik,
Will Noble,
Zhe Hu,
Zou Dan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 19;
Guava versions 16.0.1 to 31.1-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-35-0 "Permalink")

- \[ [CALCITE-5823](https://issues.apache.org/jira/browse/CALCITE-5823)\]
Remove commons-collections dependency from innodb.
- The way of Locale parsing changed within \[ [CALCITE-5746](https://issues.apache.org/jira/browse/CALCITE-5746)\]
Now locale’s language tag should match IETF BCP 47 language tag or be empty.
- \[ [CALCITE-5477](https://issues.apache.org/jira/browse/CALCITE-5477)\]
Build with Guava 19.0.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-35-0 "Permalink")

- Supporting new SQL functions in BigQuery:
  - \[ [CALCITE-5728](https://issues.apache.org/jira/browse/CALCITE-5728)\]
    Add `ARRAY_TO_STRING` function (enabled in BigQuery library)
  - \[ [CALCITE-5476](https://issues.apache.org/jira/browse/CALCITE-5476)\]
    Add `DATETIME_TRUNC` function (enabled in BigQuery library)
  - \[ [CALCITE-5565](https://issues.apache.org/jira/browse/CALCITE-5565)\]
    Add `LOG` function (enabled in BigQuery library)
  - \[ [CALCITE-5543](https://issues.apache.org/jira/browse/CALCITE-5543)\]
    Add functions `PARSE_DATE`, `PARSE_DATETIME`, `PARSE_TIME`, `PARSE_TIMESTAMP` (enabled in BigQuery library)
  - \[ [CALCITE-5564](https://issues.apache.org/jira/browse/CALCITE-5564)\]
    Add parsing and validation for `PERCENTILE_CONT`/`PERCENTILE_DISC` functions (enabled in BigQuery)
  - \[ [CALCITE-5557](https://issues.apache.org/jira/browse/CALCITE-5557)\]
    Add `SAFE_CAST` function (enabled in BigQuery library)
  - \[ [CALCITE-5580](https://issues.apache.org/jira/browse/CALCITE-5580)\]
    Add `SPLIT` function (enabled in BigQuery library)
  - \[ [CALCITE-5709](https://issues.apache.org/jira/browse/CALCITE-5709)\]
    Add `TO_BASE32` and `FROM_BASE32` functions (enabled in BigQuery library)
  - \[ [CALCITE-5782](https://issues.apache.org/jira/browse/CALCITE-5782)\]
    Add `TO_HEX` and `FROM_HEX` functions (enabled in BigQuery library)
  - \[ [CALCITE-5660](https://issues.apache.org/jira/browse/CALCITE-5660)\]
    Add array subscript operators `OFFSET`, `ORDINAL`, `SAFE_OFFSET`, `SAFE_ORDINAL` (enabled in BigQuery library)
- Supporting new SQL functions in Spark:
  - \[ [CALCITE-5624](https://issues.apache.org/jira/browse/CALCITE-5624)\]
    Add `ARRAY` function (enabled in Spark library)
  - \[ [CALCITE-5751](https://issues.apache.org/jira/browse/CALCITE-5751)\]
    Add `ARRAY_APPEND`, `ARRAY_POSITION`, `ARRAY_REMOVE`, `ARRAY_PREPEND` function (enabled in Spark library)
  - \[ [CALCITE-5707](https://issues.apache.org/jira/browse/CALCITE-5707)\]
    Add `ARRAY_CONTAINS` function (enabled in Spark library)
  - \[ [CALCITE-5734](https://issues.apache.org/jira/browse/CALCITE-5734)\]
    Add `ARRAY_COMPACT` function (enabled in Spark library)
  - \[ [CALCITE-5704](https://issues.apache.org/jira/browse/CALCITE-5704)\]
    Add `ARRAY_EXCEPT`, `ARRAY_INTERSECT`, `ARRAY_UNION` function (enabled in Spark library)
  - \[ [CALCITE-5657](https://issues.apache.org/jira/browse/CALCITE-5657)\]
    Add `ARRAY_DISTINCT` function (enabled in Spark library)
  - \[ [CALCITE-5778](https://issues.apache.org/jira/browse/CALCITE-5778)\]
    Add `ARRAY_JOIN`, `ARRAYS_OVERLAP`, `ARRAYS_ZIP` function (enabled in Spark library)
  - \[ [CALCITE-5710](https://issues.apache.org/jira/browse/CALCITE-5710)\]
    Add `ARRAY_MAX`, `ARRAY_MIN` function (enabled in Spark library)
  - \[ [CALCITE-5700](https://issues.apache.org/jira/browse/CALCITE-5700)\]
    Add `ARRAY_SIZE`, `ARRAY_REPEAT` function (enabled in Spark library)
  - \[ [CALCITE-5822](https://issues.apache.org/jira/browse/CALCITE-5822)\]
    Add `BIT_LENGTH` function (enabled in Spark library)
  - \[ [CALCITE-5772](https://issues.apache.org/jira/browse/CALCITE-5772)\]
    Add `MAP_CONCAT`, `MAP_FROM_ENTRIES` function (enabled in Spark library)
  - \[ [CALCITE-5714](https://issues.apache.org/jira/browse/CALCITE-5714)\]
    Add `MAP_ENTRIES` function (enabled in Spark library)
  - \[ [CALCITE-5744](https://issues.apache.org/jira/browse/CALCITE-5744)\]
    Add `MAP_FROM_ARRAYS`, `STR_TO_MAP` function (enabled in Spark library)
  - \[ [CALCITE-5695](https://issues.apache.org/jira/browse/CALCITE-5695)\]
    Add `MAP_KEYS`, `MAP_VALUES` function (enabled in Spark library)
  - \[ [CALCITE-5738](https://issues.apache.org/jira/browse/CALCITE-5738)\]
    Add `SORT_ARRAY` function (enabled in Spark library)
- Supporting new SQL functions in BigQuery, MSSql, MySQL, Oracle and Postgres:
  - \[ [CALCITE-5548](https://issues.apache.org/jira/browse/CALCITE-5548)\]
    Add MSSQL-style `CONVERT` function (enabled in MSSql library)
  - \[ [CALCITE-5741](https://issues.apache.org/jira/browse/CALCITE-5741)\]
    Add `CONCAT_WS` function (enabled in MSSQL, MySQL, Postgres libraries)
  - \[ [CALCITE-3959](https://issues.apache.org/jira/browse/CALCITE-3959)\]
    Add `INSTR` function (enabled in BigQuery, MySQL, Oracle libraries)
  - \[ [CALCITE-5642](https://issues.apache.org/jira/browse/CALCITE-5642)\]
    Add `SHA256`, `SHA512` functions (enabled in BigQuery and Postgres libraries)
  - \[ [CALCITE-5585](https://issues.apache.org/jira/browse/CALCITE-5585)\]
    Add `STRPOS` function (enabled in BigQuery, Postgres libraries)
  - \[ [CALCITE-5619](https://issues.apache.org/jira/browse/CALCITE-5619)\]
    Add `TO_CHAR(<TIMESTAMP>, <STRING>)` function (enabled in MySQL, Oracle,
    Postgres libraries)
  - \[ [CALCITE-4771](https://issues.apache.org/jira/browse/CALCITE-4771)\]
    Add `TRY_CAST` function (enabled in MSSQL library)
- \[ [CALCITE-5761](https://issues.apache.org/jira/browse/CALCITE-5761)\]
Allow `DECADE`, `CENTURY`, and `MILLENNIUM` time units in `DATE_TRUNC`,
`TIMESTAMP_TRUNC`, `DATETIME_TRUNC` functions
- \[ [CALCITE-5783](https://issues.apache.org/jira/browse/CALCITE-5783)\]
Support hint for `TableFunctionScan`
- \[ [CALCITE-5593](https://issues.apache.org/jira/browse/CALCITE-5593)\]
Elasticsearch adapter should support aliases
- \[ [CALCITE-5411](https://issues.apache.org/jira/browse/CALCITE-5411)\]
`SparkSqlDialect` should support `ROLLUP` and `CUBE` aggregate functions
- \[ [CALCITE-5664](https://issues.apache.org/jira/browse/CALCITE-5664)\]
Add `CONVERT(string USING transcodingName)` function, also known as TRANSLATE
- \[ [CALCITE-5610](https://issues.apache.org/jira/browse/CALCITE-5610)\]
Add `COTH`, `CSCH`, `SECH` functions
- \[ [CALCITE-111](https://issues.apache.org/jira/browse/CALCITE-111)\]
Support `CONVERT` function, for changing character sets
- \[ [CALCITE-5606](https://issues.apache.org/jira/browse/CALCITE-5606)\]
Add `SqlLibrary.ALL`
- \[ [CALCITE-5746](https://issues.apache.org/jira/browse/CALCITE-5746)\]
Support JDK 19
- \[ [CALCITE-5662](https://issues.apache.org/jira/browse/CALCITE-5662)\]
Allow `CAST(BOOLEAN as INTEGER)` (if enabled by conformance)
- \[ [CALCITE-4334](https://issues.apache.org/jira/browse/CALCITE-4334)\]
`LITERAL_AGG`, an internal aggregate function that returns a constant value
- \[ [CALCITE-5688](https://issues.apache.org/jira/browse/CALCITE-5688)\]
Support `TRUNCATE TABLE` DDL statement in server parser
- \[ [CALCITE-5711](https://issues.apache.org/jira/browse/CALCITE-5711)\]
Implement the `SINGLE_VALUE` aggregation in Postgres Dialect
- \[ [CALCITE-5608](https://issues.apache.org/jira/browse/CALCITE-5608)\]
Implement `ASINH`, `ACOSH`, `ATANH` functions
- \[ [CALCITE-5602](https://issues.apache.org/jira/browse/CALCITE-5602)\]
Implement `CSC` and `SEC` functions
- \[ [CALCITE-5367](https://issues.apache.org/jira/browse/CALCITE-5367)\]
Implement spatial type functions
- \[ [CALCITE-5160](https://issues.apache.org/jira/browse/CALCITE-5160)\]
`ANY`/`SOME`, `ALL` operators should support collection expressions
- \[ [CALCITE-5403](https://issues.apache.org/jira/browse/CALCITE-5403)\]
Babel parser should parse Postgres’s `SET`, `RESET`, `BEGIN`, `SHOW`, `ROLLBACK`, `COMMIT` commands

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-35-0 "Permalink")

- \[ [CALCITE-5440](https://issues.apache.org/jira/browse/CALCITE-5440)\]
Bump gradle from 7.4.2 to 7.6.1
- \[ [CALCITE-5361](https://issues.apache.org/jira/browse/CALCITE-5361)\]
Update janino from 3.1.8 to 3.1.9
- \[ [CALCITE-5587](https://issues.apache.org/jira/browse/CALCITE-5587)\]
Upgrade geode-core from 1.10.0 to 1.15.1
- \[ [CALCITE-5819](https://issues.apache.org/jira/browse/CALCITE-5819)\]
Upgrade commons-collections from 3.x to 4.4
- Upgrade Jackson from 2.14.1 to 2.15.0
- Bump vlsi-release-plugins from 1.84 to 1.90

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-35-0 "Permalink")

- \[ [CALCITE-5747](https://issues.apache.org/jira/browse/CALCITE-5747)\]
Conflicting `FLOOR` return type between Calcite and BigQuery
- \[ [CALCITE-5865](https://issues.apache.org/jira/browse/CALCITE-5865)\]
ClassCastException with `FLOOR` and `CEIL` on conformances that are not builtin
- \[ [CALCITE-5779](https://issues.apache.org/jira/browse/CALCITE-5779)\]
Implicit column alias for single-column table function should work
- \[ [CALCITE-5788](https://issues.apache.org/jira/browse/CALCITE-5788)\]
Order of metadata handler methods is inconsistent in different java versions
- \[ [CALCITE-5790](https://issues.apache.org/jira/browse/CALCITE-5790)\]
Validator should disallow a query with \* but no `FROM` clause
- \[ [CALCITE-5771](https://issues.apache.org/jira/browse/CALCITE-5771)\]
Apply two different `NULL` semantics for `CONCAT` function (enabled in MySQL, Postgres, BigQuery and MSSQL)
- \[ [CALCITE-5759](https://issues.apache.org/jira/browse/CALCITE-5759)\]
`SEARCH(1, Sarg[IS NOT NULL])` should be simplified to `TRUE`
- \[ [CALCITE-5425](https://issues.apache.org/jira/browse/CALCITE-5425)\]
Should not pushdown Filter through Aggregate without group keys
- \[ [CALCITE-5745](https://issues.apache.org/jira/browse/CALCITE-5745)\]
`CONCAT` function (enabled in Oracle library) should only return `NULL` when both arguments are `NULL`
- \[ [CALCITE-5755](https://issues.apache.org/jira/browse/CALCITE-5755)\]
In `Sarg`, allow `TimestampString` values to be serialized to/from JSON
- \[ [CALCITE-5767](https://issues.apache.org/jira/browse/CALCITE-5767)\]
JDBC adapter for MSSQL adds `GROUPING` to `ORDER BY` clause twice when emulating `NULLS LAST`
- \[ [CALCITE-5381](https://issues.apache.org/jira/browse/CALCITE-5381)\]
Add `convertCorrelateToJoin` config property to `RelBuilder`
- \[ [CALCITE-5554](https://issues.apache.org/jira/browse/CALCITE-5554)\]
In `EXTRACT` function, add `DAYOFWEEK` and `DAYOFYEAR` as synonyms for `DOW`, `DOY`
- \[ [CALCITE-5506](https://issues.apache.org/jira/browse/CALCITE-5506)\]
`RelToSqlConverter` should retain the aggregation logic when Project without `RexInputRef` on the Aggregate
- \[ [CALCITE-5680](https://issues.apache.org/jira/browse/CALCITE-5680)\]
Wrong plan for multiple `IN` sub-queries with only literal operands
- \[ [CALCITE-5547](https://issues.apache.org/jira/browse/CALCITE-5547)\]
`JOIN USING` returns incorrect column names
- \[ [CALCITE-5653](https://issues.apache.org/jira/browse/CALCITE-5653)\]
`SELECT DISTINCT` aggregate function with `ORDER BY` gives invalid validation error
- \[ [CALCITE-5621](https://issues.apache.org/jira/browse/CALCITE-5621)\]
Allow user-defined type declarations (UDTs) in the root of the JSON catalog
- \[ [CALCITE-5530](https://issues.apache.org/jira/browse/CALCITE-5530)\]
`RelToSqlConverter[ORDER BY]` generates an incorrect field alias when 2 projection fields have the same name
- \[ [CALCITE-5679](https://issues.apache.org/jira/browse/CALCITE-5679)\]
`HepPlanner#buildFinalPlan`: do not clear metadata cache if RelNode has not changed
- \[ [CALCITE-5614](https://issues.apache.org/jira/browse/CALCITE-5614)\]
Serialize `Sarg` values to and from JSON
- \[ [CALCITE-4698](https://issues.apache.org/jira/browse/CALCITE-4698)\]
Result type of datetime ‘+’ operators and `TIMESTAMPADD` function should be the same as the operand type
- \[ [CALCITE-5671](https://issues.apache.org/jira/browse/CALCITE-5671)\]
Add option to disable SSL certificate validation to ES adapter
- \[ [CALCITE-5675](https://issues.apache.org/jira/browse/CALCITE-5675)\]
Infer predicates for anti-join
- \[ [CALCITE-5639](https://issues.apache.org/jira/browse/CALCITE-5639)\]
`RexSimplify` should remove `IS NOT NULL` check when `LIKE` comparison is present
- \[ [CALCITE-5670](https://issues.apache.org/jira/browse/CALCITE-5670)\]
Assertion error in `SemiJoinJoinTransposeRule` when Semi-Join has keys from both tables of the bottom Join
- \[ [CALCITE-5646](https://issues.apache.org/jira/browse/CALCITE-5646)\]
`JoinDeriveIsNotNullFilterRule` incorrectly handles `COALESCE` in join condition
- \[ [CALCITE-5563](https://issues.apache.org/jira/browse/CALCITE-5563)\]
Reduce loops to optimize `RelSubset#getParents` and `RelSubset#getParentSubsets`
- \[ [CALCITE-5651](https://issues.apache.org/jira/browse/CALCITE-5651)\]
Inferred scale for decimal should not exceed maximum allowed scale
- \[ [CALCITE-5655](https://issues.apache.org/jira/browse/CALCITE-5655)\]
Wrong plan for multiple `IN`/`SOME` sub-queries with OR predicate
- \[ [CALCITE-5650](https://issues.apache.org/jira/browse/CALCITE-5650)\]
Obtain typesystem from dialect in `RelToSqlConverterTest`
- \[ [CALCITE-5648](https://issues.apache.org/jira/browse/CALCITE-5648)\]
`SqlDelegatingConformance` incorrectly delegates to `SqlConformanceEnum.DEFAULT`
- \[ [CALCITE-5538](https://issues.apache.org/jira/browse/CALCITE-5538)\]
Allow creating `TimestampString` with fractional seconds ending in 0
- \[ [CALCITE-5605](https://issues.apache.org/jira/browse/CALCITE-5605)\]
Add BigQuery as supported library for `CHR`
- \[ [CALCITE-5571](https://issues.apache.org/jira/browse/CALCITE-5571)\]
Remove `org.jetbrains.annotations` from java source code
- \[ [CALCITE-4555](https://issues.apache.org/jira/browse/CALCITE-4555)\]
Invalid zero literal value is used for `TIMESTAMP WITH LOCAL TIME ZONE` type in `RexBuilder`
- \[ [CALCITE-5722](https://issues.apache.org/jira/browse/CALCITE-5722)\]
`Sarg.isComplementedPoints` fails with anti-points which are equal under `compareTo` but not `equals`
- \[ [CALCITE-5730](https://issues.apache.org/jira/browse/CALCITE-5730)\]
Initial null values can be dropped by `EnumerableLimitSort` with offset
- \[ [CALCITE-5723](https://issues.apache.org/jira/browse/CALCITE-5723)\]
Oracle dialect generates SQL that cannot be recognized by lower version Oracle Server(<12) when unparsing OffsetFetch
- \[ [CALCITE-5553](https://issues.apache.org/jira/browse/CALCITE-5553)\]
`RelStructuredTypeFlattener` produces bad plan for single field struct
- \[ [CALCITE-5669](https://issues.apache.org/jira/browse/CALCITE-5669)\]
Add rules to remove `Correlate` when one of its inputs is empty
- \[ [CALCITE-4554](https://issues.apache.org/jira/browse/CALCITE-4554)\]
Support `TIMESTAMP WITH LOCAL TIME ZONE` for `Snapshot` and `MatchRecognize`
- \[ [CALCITE-5677](https://issues.apache.org/jira/browse/CALCITE-5677)\]
`SUBSTR` signature incorrect for BigQuery
- \[ [CALCITE-5674](https://issues.apache.org/jira/browse/CALCITE-5674)\]
`CAST` expr to target type should respect nullable when it is complex type (follow-up)
- \[ [CALCITE-5705](https://issues.apache.org/jira/browse/CALCITE-5705)\]
Generalize `RemoveEmptySingleRule` to work with arbitrary relations and pruning configurations
- \[ [CALCITE-5668](https://issues.apache.org/jira/browse/CALCITE-5668)\]
When parsing SQL in Postgres dialect, allow unquoted table names to contain dollar sign, letters with diacritical marks and non-Latin letters
- \[ [CALCITE-5699](https://issues.apache.org/jira/browse/CALCITE-5699)\]
Negated posix regex expressions throw NullPointerException when applied to NULL values
- \[ [CALCITE-5691](https://issues.apache.org/jira/browse/CALCITE-5691)\]
`IN` sub-query inside `FILTER` clause throws IndexOutOfBoundsException
- \[ [CALCITE-5674](https://issues.apache.org/jira/browse/CALCITE-5674)\]
`CAST` expr to target type should respect nullable when it is complex type
- \[ [CALCITE-5698](https://issues.apache.org/jira/browse/CALCITE-5698)\]
`EXTRACT` from `INTERVAL` should return negative numbers if interval is negative
- \[ [CALCITE-5757](https://issues.apache.org/jira/browse/CALCITE-5757)\]
BigQuery `DATE_TRUNC` return type should be `ARG0` and `TIMESTAMP_TRUNC`/`DATETIME_TRUNC` should return `TIMESTAMP` for `DATE`/`TIMESTAMPs` and `TIMESTAMP_LTZ` for `TIMESTAMP_LTZ`
- \[ [CALCITE-5768](https://issues.apache.org/jira/browse/CALCITE-5768)\]
JDBC adapter should insert a subquery for a query with `ORDER BY` ordinal
- \[ [CALCITE-5676](https://issues.apache.org/jira/browse/CALCITE-5676)\]
In JDBC `DatabaseMetaData.getColumns`, set DATA\_TYPE and TYPE\_NAME metadata values for `MEASURE` types
- \[ [CALCITE-5401](https://issues.apache.org/jira/browse/CALCITE-5401)\]
Rule fired by `HepPlanner` can return Volcano’s `RelSubset`
- \[ [CALCITE-5721](https://issues.apache.org/jira/browse/CALCITE-5721)\]
Capture build scans on ge.apache.org to benefit from deep build insights
- \[ [CALCITE-5703](https://issues.apache.org/jira/browse/CALCITE-5703)\]
Reduce amount of generated runtime code
- \[ [CALCITE-5717](https://issues.apache.org/jira/browse/CALCITE-5717)\]
`RelBuilder.project` of literals on a single-row `Aggregate` should create a Values
- \[ [CALCITE-5697](https://issues.apache.org/jira/browse/CALCITE-5697)\]
`RelBuilder.convert` does not match nullability if top of stack is a Project
- \[ [CALCITE-5839](https://issues.apache.org/jira/browse/CALCITE-5839)\]
`EnumerableInterpretable#StaticFieldDetector` can overwrite its flag and return an incorrect result
- \[ [CALCITE-5479](https://issues.apache.org/jira/browse/CALCITE-5479)\]
`FamilyOperandTypeChecker` is not readily composable in sequences
- \[ [CALCITE-5824](https://issues.apache.org/jira/browse/CALCITE-5824)\]
Handle IndexCondition null pointQueryKey list in innodb
- \[ [CALCITE-5769](https://issues.apache.org/jira/browse/CALCITE-5769)\]
Optimizing `CAST(e AS t) IS NOT NULL` to `e IS NOT NULL`
- \[ [CALCITE-5780](https://issues.apache.org/jira/browse/CALCITE-5780)\]
Simplify `1 > x OR 1 <= x OR x IS NULL` to `TRUE`
- \[ [CALCITE-5708](https://issues.apache.org/jira/browse/CALCITE-5708)\]
`SUBSTRING` validation error if any parameter is a NULL literal
- \[ [CALCITE-5816](https://issues.apache.org/jira/browse/CALCITE-5816)\]
Only return left-hand table columns when validate `LEFT SEMI JOIN` query
- \[ [CALCITE-5798](https://issues.apache.org/jira/browse/CALCITE-5798)\]
Improve simplification of `(x < y) IS NOT TRUE` when x and y are not nullable
- \[ [CALCITE-5810](https://issues.apache.org/jira/browse/CALCITE-5810)\]
Prevent overflow in substring length computation
- \[ [CALCITE-5793](https://issues.apache.org/jira/browse/CALCITE-5793)\]
JDBC adapter should use `NULLS FIRST`, `NULLS LAST` syntax for BigQuery
- \[ [CALCITE-5789](https://issues.apache.org/jira/browse/CALCITE-5789)\]
Query with two nested subqueries where the inner-most references the outer-most table returns wrong result
- Add .gitignore for Java VSCode plugin
- Refactor: In tests, pass ‘typeSystem’ connection property value via a ThreadLocal
- Refactor: In `RexImpTable`, create field ‘variableName’ to implement method ‘getVariableName()’
- Refactor: Move class `AggConverter` out of `SqlToRelConverter`
- Refactor: Use `PairList`
- Refactor: Make `SqlValidatorScope` mandatory
- Refactor: Add fields `AggregateCall.rexList` and `RelBuilder.AggCall.preOperands`
- Refactor: Add `RelNode.stripped`
- Refactor: `RelBuilder.variable(Holder)` becomes `variable(Supplier)`
- Refactor: In `ImmutableBitSet`, specialize forEach, and add forEachInt, anyMatch, allMatch

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-35-0 "Permalink")

- \[ [CALCITE-5785](https://issues.apache.org/jira/browse/CALCITE-5785)\]
Gradle remote build caching is broken for :babel:fmppMain and :server:fmppMain tasks
- \[ [CALCITE-5611](https://issues.apache.org/jira/browse/CALCITE-5611)\]
In `SqlOperatorTest`, show SQL for failed tests
- \[ [CALCITE-5726](https://issues.apache.org/jira/browse/CALCITE-5726)\]
Canonize use of Hamcrest matchers in test code
- \[ [CALCITE-5765](https://issues.apache.org/jira/browse/CALCITE-5765)\]
Add `LintTest`, to apply custom lint rules to source code
- \[ [CALCITE-5773](https://issues.apache.org/jira/browse/CALCITE-5773)\]
Gradle show tasks fails when creating javadocAggregateIncludingTests
- \[ [CALCITE-5786](https://issues.apache.org/jira/browse/CALCITE-5786)\]
`QuidemTest` and `DiffRepository` are not compatible with Gradle incremental builds since they write to build/resources
- \[ [CALCITE-5574](https://issues.apache.org/jira/browse/CALCITE-5574)\]
Break `MockCatalogReaderSimple#init` into smaller methods
- \[ [CALCITE-5727](https://issues.apache.org/jira/browse/CALCITE-5727)\]
`RelOptFixture#checkUnchanged` should assert planAfter is not present
- \[ [CALCITE-5596](https://issues.apache.org/jira/browse/CALCITE-5596)\]
Elasticsearch adapter test fails on Apple silicon
- \[ [CALCITE-5764](https://issues.apache.org/jira/browse/CALCITE-5764)\]
Add `Puffin`
- \[ [CALCITE-5706](https://issues.apache.org/jira/browse/CALCITE-5706)\]
Add class `PairList`
- \[ [CALCITE-5762](https://issues.apache.org/jira/browse/CALCITE-5762)\]
Create class `TestUnsafe`, that contains unsafe methods used by tests
- In tests, don’t allow multi-line strings as argument to CalciteAssert.returnsUnordered
- Disable JIRA worklog notifications for GitHub PRs
- Code style: Lint
- Code style: improve Javadoc
- Code style: disallow ‘))’ and ‘).’ at the start of a line

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-35-0 "Permalink")

- Site: Add TJ Banghart as committer
- Site: Add Dan Zou as committer
- Site: Add Zhe Hu as committer
- Site: Add Yong Liu as committer
- Site: Add Oliver Lee as committer
- Site: Add Tanner Clary as committer
- Site: Add talks from Calcite Meetup March 2023
- Site: Clarify that SQL does not support recursive queries yet
- Site: Troubleshooting/Website publishing improvements in release guide
- Bump nokogiri from 1.13.4 to 1.14.3 in /site
- Update javadoc for `RelColumnOrigin#isDerived` method

## [1.34.0](https://github.com/apache/calcite/releases/tag/calcite-1.34.0) / 2023-03-14 [Permalink](https://calcite.apache.org/docs/history.html\#v1-34-0 "Permalink")

This release comes 1 month after [1.33.0](https://calcite.apache.org/docs/history.html#v1-33-0),
contains contributions from 18 contributors, and resolves 34 issues. It’s worth highlighting the
introduction of QUALIFY clause (\[ [CALCITE-5268](https://issues.apache.org/jira/browse/CALCITE-5268)\]),
which facilitates filtering the results of window functions. Among other improvements and fixes, it
adds roughly 15 new functions in BigQuery library for handling dates, times, and timestamps, and
provides a fix (\[ [CALCITE-5522](https://issues.apache.org/jira/browse/CALCITE-5522)\])
for a small breaking change in `DATE_TRUNC` function
(\[ [CALCITE-5447](https://issues.apache.org/jira/browse/CALCITE-5447)\]), which was
introduced accidentally in [1.33.0](https://calcite.apache.org/docs/history.html#v1-33-0).

Contributors to this release:
Alessandro Solimando,
Benchao Li,
Brandon Chong,
Dmitry Sysolyatin,
Francis Chuang,
Gian Merlino,
Guillaume Massé,
Jiajun Xie,
Julian Hyde,
Moritz Mack,
Oliver Lee,
Peng Wang,
Stamatis Zampetakis (release manager),
Tanner Clary,
Tim Nieradzik,
TJ Banghart,
xinqiu.hu,
Zou Dan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 18;
Guava versions 16.0.1 to 31.1-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-34-0 "Permalink")

\[ [CALCITE-3870](https://issues.apache.org/jira/browse/CALCITE-3870)\]
Change the default value of
[SqlToRelConverter.Config.expand](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql2rel/SqlToRelConverter.Config.html#isExpand())
from true to false. From now on `SqlToRelConverter`, handles sub-queries (such
as `IN`, `EXISTS`, and scalar sub-queries) by converting them to `RexSubQuery`
expressions, rather than expanding them. To expand these `RexSubQuery`
expressions, the `SubQueryRemoveRule` rule must be enabled in the planning
phase.
To keep the old behavior (which is discouraged but still supported),
initialize `SqlToRelConverter` using `SqlToRelConverter.config().withExpand(true)` as the value for
the `config` argument.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-34-0 "Permalink")

- \[ [CALCITE-5268](https://issues.apache.org/jira/browse/CALCITE-5268)\]
Add `QUALIFY` clause
- \[ [CALCITE-5469](https://issues.apache.org/jira/browse/CALCITE-5469)\]
Add `DATETIME_ADD`, `DATETIME_DIFF`, `DATE_ADD`, `DATE_DIFF` functions (enabled in BigQuery library)
- \[ [CALCITE-5484](https://issues.apache.org/jira/browse/CALCITE-5484)\]
Add `DATETIME_SUB` function (enabled in BigQuery library)
- \[ [CALCITE-5357](https://issues.apache.org/jira/browse/CALCITE-5357)\]
Add `FORMAT_TIME`, `FORMAT_DATE`, `FORMAT_DATETIME`, `FORMAT_TIMESTAMP` functions (enabled in BigQuery library)
- \[ [CALCITE-5508](https://issues.apache.org/jira/browse/CALCITE-5508)\]
Add constructor functions for `DATE`, `TIME`, `TIMESTAMP`, `DATETIME` (enabled in BigQuery library)

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-34-0 "Permalink")

- Bump Quidem from 0.10 to 0.11

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-34-0 "Permalink")

- \[ [CALCITE-5545](https://issues.apache.org/jira/browse/CALCITE-5545)\]
Allow for overriding `SqlValidator` to enable custom `SqlNode` validation
- \[ [CALCITE-5504](https://issues.apache.org/jira/browse/CALCITE-5504)\]
Array value constructor is unparsed incorrectly for `SparkSqlDialect`
- \[ [CALCITE-5518](https://issues.apache.org/jira/browse/CALCITE-5518)\]
`RelToSqlConverter` generates invalid order of `ROLLUP` fields
- \[ [CALCITE-5510](https://issues.apache.org/jira/browse/CALCITE-5510)\]
`RelToSqlConverter` should use ordinal for `ORDER BY` if the dialect allows
- \[ [CALCITE-5478](https://issues.apache.org/jira/browse/CALCITE-5478)\]
Use highest input precision for datetimes in `SqlTypeFactoryImpl.leastRestrictive`
- \[ [CALCITE-5522](https://issues.apache.org/jira/browse/CALCITE-5522)\]
Babel parser cannot handle some overloads of the `DATE_TRUNC` function
- \[ [CALCITE-5531](https://issues.apache.org/jira/browse/CALCITE-5531)\]
`COALESCE` function throws `ClassCastException`
- \[ [CALCITE-5507](https://issues.apache.org/jira/browse/CALCITE-5507)\]
`HAVING` alias fails for mixed usage of alias and aggregate function
- \[ [CALCITE-5503](https://issues.apache.org/jira/browse/CALCITE-5503)\]
`CheapestPlanReplacer` should reuse repeated nodes in a DAG plan
- \[ [CALCITE-5468](https://issues.apache.org/jira/browse/CALCITE-5468)\]
`SqlToRelConverter` throws if `ORDER BY` contains `IN`
- \[ [CALCITE-5515](https://issues.apache.org/jira/browse/CALCITE-5515)\]
Add keyspace parameter to `CassandraSchema` and `CassandraTable`
- \[ [CALCITE-5416](https://issues.apache.org/jira/browse/CALCITE-5416)\]
JDBC adapter for MySQL 5 incorrectly combines `GROUP BY ROLLUP` and `ORDER BY` clauses
- \[ [CALCITE-5505](https://issues.apache.org/jira/browse/CALCITE-5505)\]
JavaCC warns about missing LOOKAHEAD directives in Parser.jj
- \[ [CALCITE-5514](https://issues.apache.org/jira/browse/CALCITE-5514)\]
In `RelJson`, add a public `toRex()` instance method
- \[ [CALCITE-5442](https://issues.apache.org/jira/browse/CALCITE-5442)\]
Tweak janino code generation in `EnumerableInterpretable` to allow debugging
- \[ [CALCITE-5521](https://issues.apache.org/jira/browse/CALCITE-5521)\]
Remove redundant rowtype check in `RelSubset#add`
- \[ [CALCITE-5483](https://issues.apache.org/jira/browse/CALCITE-5483)\]
`ProjectAggregateMergeRule` throws exception if literal is non-numeric
- `TryThreadLocal` values are now not-null by default

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-34-0 "Permalink")

- \[ [CALCITE-5546](https://issues.apache.org/jira/browse/CALCITE-5546)\]
Code style: Break long assignment expressions after ‘=’
- \[ [CALCITE-5501](https://issues.apache.org/jira/browse/CALCITE-5501)\]
`SqlToRelConverterTest.checkActualAndReferenceFiles` fails intermittently in Jenkins CI
- Add test for \[ [CALCITE-5524](https://issues.apache.org/jira/browse/CALCITE-5524)\] JDBC adapter generates `LIMIT`, `OFFSET` in wrong order for Presto dialect
- Add tests for \[ [CALCITE-2980](https://issues.apache.org/jira/browse/CALCITE-2980)\] Implement the `FORMAT` clause of the `CAST` operator
- \[ [CALCITE-5537](https://issues.apache.org/jira/browse/CALCITE-5537)\]
Slow test case failures in `LatticeSuggesterTest`
- Autostyle: Disallow space or newline before ‘)’ in method declaration or call

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-34-0 "Permalink")

- \[ [CALCITE-5555](https://issues.apache.org/jira/browse/CALCITE-5555)\]
Remove obsolete instructions for processing requests for new JIRA accounts
- \[ [CALCITE-5550](https://issues.apache.org/jira/browse/CALCITE-5550)\]
Update instructions for requesting Jira account to use self-serve facility
- `CompositeOperandTypeChecker`’s javadoc uses wrong class name

## [1.33.0](https://github.com/apache/calcite/releases/tag/calcite-1.33.0) / 2023-02-06 [Permalink](https://calcite.apache.org/docs/history.html\#v1-33-0 "Permalink")

This release comes five months after [1.32.0](https://calcite.apache.org/docs/history.html#v1-32-0),
contains contributions from 33 contributors, and resolves 107 issues.

Among others, it is worth highlighting the following improvements:

- Many improvements to the BigQuery dialect as part of \[ [CALCITE-5180](https://issues.apache.org/jira/browse/CALCITE-5180)\]

  - \[ [CALCITE-5269](https://issues.apache.org/jira/browse/CALCITE-5269)\]
    Implement BigQuery `TIME_TRUNC` and `TIMESTAMP_TRUNC` functions
  - \[ [CALCITE-5360](https://issues.apache.org/jira/browse/CALCITE-5360)\]
    Implement `TIMESTAMP_ADD` function (compatible with BigQuery)
  - \[ [CALCITE-5389](https://issues.apache.org/jira/browse/CALCITE-5389)\]
    Add `STARTS_WITH` and `ENDS_WITH` functions (for `BIG_QUERY` compatibility)
  - \[ [CALCITE-5404](https://issues.apache.org/jira/browse/CALCITE-5404)\]
    Implement BigQuery’s `POW()` and `TRUNC()` math functions
  - \[ [CALCITE-5423](https://issues.apache.org/jira/browse/CALCITE-5423)\]
    Implement `TIMESTAMP_DIFF` function (compatible with BigQuery)
  - \[ [CALCITE-5430](https://issues.apache.org/jira/browse/CALCITE-5430)\]
    Implement `IFNULL()` for BigQuery dialect
  - \[ [CALCITE-5432](https://issues.apache.org/jira/browse/CALCITE-5432)\]
    Implement BigQuery `TIME_ADD`/`TIME_DIFF`
  - \[ [CALCITE-5436](https://issues.apache.org/jira/browse/CALCITE-5436)\]
    Implement `DATE_SUB`, `TIME_SUB`, `TIMESTAMP_SUB` (compatible w/ BigQuery)
  - \[ [CALCITE-5447](https://issues.apache.org/jira/browse/CALCITE-5447)\]
    Add `DATE_TRUNC` for BigQuery
- \[ [CALCITE-5105](https://issues.apache.org/jira/browse/CALCITE-5105)\]
Add `MEASURE` type and `AGGREGATE` aggregate function
- \[ [CALCITE-5155](https://issues.apache.org/jira/browse/CALCITE-5155)\]
Custom time frames
- \[ [CALCITE-5280](https://issues.apache.org/jira/browse/CALCITE-5280)\]
Implement geometry aggregate functions
- \[ [CALCITE-5314](https://issues.apache.org/jira/browse/CALCITE-5314)\]
Prune empty parts of a query by exploiting stats/metadata

Contributors to this release:
Aitozi,
Aleksey Plekhanov,
Alessandro Solimando,
Benchao Li,
Bertil Chapuis,
Christophe Le Saec,
Dmitry Sysolyatin,
Francis Chuang,
Gian Merlino,
Greg Hart,
Hanumath Maduri,
Istvan Toth,
Jake Xie,
James Turton,
Jasmin Trada,
Jess Balint (release manager),
Julian Hyde,
Kevin Risden,
Krisztian Kasa,
Liya Fan,
Mou Wu,
Oliver Lee,
Scott Reynolds,
Sergey Nuyanzin,
Stamatis Zampetakis,
TJ Banghart,
Tanner Clary,
Thomas Rebele,
Tim Nieradzik,
Volodymyr Vysotskyi,
Xurenhe,
Zhengqiang Duan,
Zou Dan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 18;
Guava versions 16.0.1 to 31.1-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-33-0 "Permalink")

- \[ [CALCITE-5293](https://issues.apache.org/jira/browse/CALCITE-5293)\]
Support general set operators in `PruneEmptyRules`. The default configuration of `PruneEmptyRules` for Set operators has changed: the rules matching scope has increased.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-33-0 "Permalink")

- \[ [CALCITE-2884](https://issues.apache.org/jira/browse/CALCITE-2884)\]
Implement `JSON_INSERT`, `JSON_REPLACE`, `JSON_SET`
- \[ [CALCITE-4186](https://issues.apache.org/jira/browse/CALCITE-4186)\]
Add `ST_CoveredBy` spatial function
- \[ [CALCITE-5105](https://issues.apache.org/jira/browse/CALCITE-5105)\]
Add `MEASURE` type and `AGGREGATE` aggregate function
- \[ [CALCITE-5127](https://issues.apache.org/jira/browse/CALCITE-5127)\]
Support correlation variables in Project
- \[ [CALCITE-5155](https://issues.apache.org/jira/browse/CALCITE-5155)\]
Custom time frames
- \[ [CALCITE-5159](https://issues.apache.org/jira/browse/CALCITE-5159)\]
`ARRAY` string constructor, and implicit cast from string literal (enabled in Postgres conformance)
- \[ [CALCITE-5269](https://issues.apache.org/jira/browse/CALCITE-5269)\]
Implement BigQuery `TIME_TRUNC` and `TIMESTAMP_TRUNC` functions
- \[ [CALCITE-5280](https://issues.apache.org/jira/browse/CALCITE-5280)\]
Implement geometry aggregate functions
- \[ [CALCITE-5281](https://issues.apache.org/jira/browse/CALCITE-5281)\]
Implement geometry set returning functions (SRF)
- \[ [CALCITE-5283](https://issues.apache.org/jira/browse/CALCITE-5283)\]
Add `ARG_MIN`, `ARG_MAX` (aka `MIN_BY`, `MAX_BY`) aggregate functions
- \[ [CALCITE-5360](https://issues.apache.org/jira/browse/CALCITE-5360)\]
Implement `TIMESTAMP_ADD` function (compatible with BigQuery)
- \[ [CALCITE-5362](https://issues.apache.org/jira/browse/CALCITE-5362)\]
Implement geometry measurement functions
- \[ [CALCITE-5389](https://issues.apache.org/jira/browse/CALCITE-5389)\]
Add `STARTS_WITH` and `ENDS_WITH` functions (for `BIG_QUERY` compatibility)
- \[ [CALCITE-5393](https://issues.apache.org/jira/browse/CALCITE-5393)\]
`VALUE` as an synonym for `VALUES` keyword (enabled in MySQL conformance)
- \[ [CALCITE-5404](https://issues.apache.org/jira/browse/CALCITE-5404)\]
Implement BigQuery’s `POW()` and `TRUNC()` math functions
- \[ [CALCITE-5423](https://issues.apache.org/jira/browse/CALCITE-5423)\]
Implement `TIMESTAMP_DIFF` function (compatible with BigQuery)
- \[ [CALCITE-5430](https://issues.apache.org/jira/browse/CALCITE-5430)\]
Implement `IFNULL()` for BigQuery dialect
- \[ [CALCITE-5432](https://issues.apache.org/jira/browse/CALCITE-5432)\]
Implement BigQuery `TIME_ADD`/`TIME_DIFF`
- \[ [CALCITE-5436](https://issues.apache.org/jira/browse/CALCITE-5436)\]
Implement `DATE_SUB`, `TIME_SUB`, `TIMESTAMP_SUB` (compatible w/ BigQuery)
- \[ [CALCITE-5447](https://issues.apache.org/jira/browse/CALCITE-5447)\]
Add `DATE_TRUNC` for BigQuery
- \[ [CALCITE-5451](https://issues.apache.org/jira/browse/CALCITE-5451)\]
Implement `LPAD()` and `RPAD()` functions
- \[ [CALCITE-5495](https://issues.apache.org/jira/browse/CALCITE-5495)\]
Allow `WEEK` and `QUARTER` in `INTERVAL` literals

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-33-0 "Permalink")

- \[ [CALCITE-5341](https://issues.apache.org/jira/browse/CALCITE-5341)\]
Upgrade Calcite to Avatica 1.23.0
- \[ [CALCITE-5351](https://issues.apache.org/jira/browse/CALCITE-5351)\]
Bump jackson to 2.13.4 and jackson databind to 2.13.4.2 to avoid CVEs
- \[ [CALCITE-5356](https://issues.apache.org/jira/browse/CALCITE-5356)\]
Update junit4 to 4.13.2 and junit5 to 5.9.1
- \[ [CALCITE-5374](https://issues.apache.org/jira/browse/CALCITE-5374)\]
Upgrade jackson version to 2.14.0

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-33-0 "Permalink")

- \[ [CALCITE-4351](https://issues.apache.org/jira/browse/CALCITE-4351)\]
`RelMdUtil#numDistinctVals` always returns 0 for large inputs
- \[ [CALCITE-4632](https://issues.apache.org/jira/browse/CALCITE-4632)\]
Exception in `RelToSqlConverter`: “Cannot convert x to DECIMAL(n, m) due to overflow”
- \[ [CALCITE-4804](https://issues.apache.org/jira/browse/CALCITE-4804)\]
Support `Snapshot` operator serialization and deserialization
- \[ [CALCITE-4972](https://issues.apache.org/jira/browse/CALCITE-4972)\]
Subfields of array columns containing structs are not qualified in `getFieldOrigins`
- \[ [CALCITE-4982](https://issues.apache.org/jira/browse/CALCITE-4982)\]
Do not push ‘cast to not null’ through `Join` in `ProjectJoinTransposeRule`
- \[ [CALCITE-5141](https://issues.apache.org/jira/browse/CALCITE-5141)\]
Incomplete implicit type conversion for insert values
- \[ [CALCITE-5209](https://issues.apache.org/jira/browse/CALCITE-5209)\]
Proper sub-query handling if it is used inside select list and group by
- \[ [CALCITE-5217](https://issues.apache.org/jira/browse/CALCITE-5217)\]
Implement `unparseSqlIntervalLiteral` in the Firebolt dialect
- \[ [CALCITE-5230](https://issues.apache.org/jira/browse/CALCITE-5230)\]
Return type of `PERCENTILE_DISC` should be the same as sort expression
- \[ [CALCITE-5252](https://issues.apache.org/jira/browse/CALCITE-5252)\]
JDBC adapter sometimes miss parentheses around `SELECT` in `WITH_ITEM` body
- \[ [CALCITE-5253](https://issues.apache.org/jira/browse/CALCITE-5253)\]
`NATURAL` join and `USING` should fail if join columns are not unique - expression validation partially broken
- \[ [CALCITE-5259](https://issues.apache.org/jira/browse/CALCITE-5259)\]
Add `getParameterRowType` method to `Planner` interface
- \[ [CALCITE-5264](https://issues.apache.org/jira/browse/CALCITE-5264)\]
`HintStrategy` rule exclusion does not match innermost rels
- \[ [CALCITE-5265](https://issues.apache.org/jira/browse/CALCITE-5265)\]
JDBC adapter sometimes adds unnecessary parentheses around `SELECT` in `INSERT`
- \[ [CALCITE-5267](https://issues.apache.org/jira/browse/CALCITE-5267)\]
Remove unused variable ‘newCasts’ in `AggregateCaseToFilterRule`
- \[ [CALCITE-5276](https://issues.apache.org/jira/browse/CALCITE-5276)\]
Implicitly convert strings to geometries
- \[ [CALCITE-5286](https://issues.apache.org/jira/browse/CALCITE-5286)\]
Join with parameterized `LIMIT` throws `AssertionError` “not a literal”
- \[ [CALCITE-5288](https://issues.apache.org/jira/browse/CALCITE-5288)\]
Expression `(a > 5 and a < 15) or (a > 10 and a < 20)` should be simplified to `SEARCH(a, Sarg[(5..20)])`
- \[ [CALCITE-5291](https://issues.apache.org/jira/browse/CALCITE-5291)\]
Make BigQuery lexical policy case insensitive
- \[ [CALCITE-5293](https://issues.apache.org/jira/browse/CALCITE-5293)\]
Support general set operators in `PruneEmptyRules`
- \[ [CALCITE-5294](https://issues.apache.org/jira/browse/CALCITE-5294)\]
Prune the null-generating side of an outer join if it is empty
- \[ [CALCITE-5296](https://issues.apache.org/jira/browse/CALCITE-5296)\]
In a query with `ROLLUP`, validator wrongly infers that a column is `NOT NULL`
- \[ [CALCITE-5297](https://issues.apache.org/jira/browse/CALCITE-5297)\]
Casting dynamic variable twice throws exception
- \[ [CALCITE-5298](https://issues.apache.org/jira/browse/CALCITE-5298)\]
CalciteSystemProperty `calcite.test.dataset` path check fails under Java Security Manager
- \[ [CALCITE-5299](https://issues.apache.org/jira/browse/CALCITE-5299)\]
JDBC adapter sometimes adds unnecessary parentheses around `SELECT` in `WITH` body
- \[ [CALCITE-5305](https://issues.apache.org/jira/browse/CALCITE-5305)\]
Character literals with C-style escapes
- \[ [CALCITE-5310](https://issues.apache.org/jira/browse/CALCITE-5310)\]
`JSON_OBJECT` in scalar sub-query throws `AssertionError`
- \[ [CALCITE-5314](https://issues.apache.org/jira/browse/CALCITE-5314)\]
Prune empty parts of a query by exploiting stats/metadata
- \[ [CALCITE-5326](https://issues.apache.org/jira/browse/CALCITE-5326)\]
`SqlMerge` generate extra bracket on `toSqlString`
- \[ [CALCITE-5332](https://issues.apache.org/jira/browse/CALCITE-5332)\]
Configuring `PruneEmptyRules` is cumbersome
- \[ [CALCITE-5336](https://issues.apache.org/jira/browse/CALCITE-5336)\]
Support inferring constants from predicates with `IS NOT DISTINCT FROM` operator
- \[ [CALCITE-5337](https://issues.apache.org/jira/browse/CALCITE-5337)\]
`UnionPullUpConstantsRule` produces an invalid plan when pulling up constants for nullable fields
- \[ [CALCITE-5339](https://issues.apache.org/jira/browse/CALCITE-5339)\]
Use `Method#getParameterCount` rather than `Method#getParameters` to get length
- \[ [CALCITE-5342](https://issues.apache.org/jira/browse/CALCITE-5342)\]
Refactor SqlFunctions `lastDay`, `addMonths`, `subtractMonths` to use `DateTimeUtils` from Avatica
- \[ [CALCITE-5348](https://issues.apache.org/jira/browse/CALCITE-5348)\]
When translating `ORDER BY` in `OVER`, use the session’s default null collation (e.g. `NULLS LAST`)
- \[ [CALCITE-5349](https://issues.apache.org/jira/browse/CALCITE-5349)\]
`RelJson` deserialization should support `SqlLibraryOperators`
- \[ [CALCITE-5355](https://issues.apache.org/jira/browse/CALCITE-5355)\]
Use the Presto SQL dialect for AWS Athena
- \[ [CALCITE-5377](https://issues.apache.org/jira/browse/CALCITE-5377)\]
`RelFieldTrimmer` support Sort with dynamic param
- \[ [CALCITE-5383](https://issues.apache.org/jira/browse/CALCITE-5383)\]
Update `CONCAT` function to allow `BIG_QUERY`
- \[ [CALCITE-5385](https://issues.apache.org/jira/browse/CALCITE-5385)\]
Add BigQuery as supported library for implemented functions
- \[ [CALCITE-5388](https://issues.apache.org/jira/browse/CALCITE-5388)\]
`tempList` expression inside `EnumerableWindow.getPartitionIterator` should be unoptimized
- \[ [CALCITE-5391](https://issues.apache.org/jira/browse/CALCITE-5391)\]
`JoinOnUniqueToSemiJoinRule` should preserve field names, if possible
- \[ [CALCITE-5392](https://issues.apache.org/jira/browse/CALCITE-5392)\]
Support `Snapshot` in `RelMdExpressionLineage`
- \[ [CALCITE-5394](https://issues.apache.org/jira/browse/CALCITE-5394)\]
`RelToSqlConverter` fails when semi-join is under a join node
- \[ [CALCITE-5395](https://issues.apache.org/jira/browse/CALCITE-5395)\]
`RelToSqlConverter` fails when `SELECT *` is under a semi-join node
- \[ [CALCITE-5405](https://issues.apache.org/jira/browse/CALCITE-5405)\]
MongoDB: Invalid `TIMESTAMP` conversion
- \[ [CALCITE-5407](https://issues.apache.org/jira/browse/CALCITE-5407)\]
MongoDB: Invalid `ARRAY` conversion
- \[ [CALCITE-5408](https://issues.apache.org/jira/browse/CALCITE-5408)\]
Return type of `PERCENTILE_CONT` should be the same as sort expression
- \[ [CALCITE-5410](https://issues.apache.org/jira/browse/CALCITE-5410)\]
Assertion error on `PERCENT_REMAINDER` operator with `DECIMAL` type
- \[ [CALCITE-5414](https://issues.apache.org/jira/browse/CALCITE-5414)\]
Use `DateTimeUtils` to correctly convert between `java.sql` types and Unix timestamps
- \[ [CALCITE-5424](https://issues.apache.org/jira/browse/CALCITE-5424)\]
Customize handling of literals based on type system
- \[ [CALCITE-5439](https://issues.apache.org/jira/browse/CALCITE-5439)\]
Validation of Pivot fails after creating a deep copy of `SqlNode`
- \[ [CALCITE-5450](https://issues.apache.org/jira/browse/CALCITE-5450)\]
Add support for `WEEK(WEEKDAY)` for custom time frames to relevant functions
- \[ [CALCITE-5452](https://issues.apache.org/jira/browse/CALCITE-5452)\]
Add BigQuery `LENGTH()` as synonym for `CHAR_LENGTH()`
- \[ [CALCITE-5454](https://issues.apache.org/jira/browse/CALCITE-5454)\]
Update BigQuery Conformance for `!=` and `%` operators
- \[ [CALCITE-5466](https://issues.apache.org/jira/browse/CALCITE-5466)\]
Constant condition can’t be reduced after correlate
- \[ [CALCITE-5471](https://issues.apache.org/jira/browse/CALCITE-5471)\]
`RelSupplier.SqlRelSupplier#apply` should use `.project()`, not `.rel`
- \[ [CALCITE-5489](https://issues.apache.org/jira/browse/CALCITE-5489)\]
When creating a `RexCall` to `TIMESTAMP_DIFF` function, cannot convert a `TIMESTAMP` literal to a `org.apache.calcite.avatica.util.TimeUnit`
- \[ [CALCITE-5491](https://issues.apache.org/jira/browse/CALCITE-5491)\]
Allow `TIME` and `DATE` to be args for `TIMESTAMPDIFF`
- \[ [CALCITE-5493](https://issues.apache.org/jira/browse/CALCITE-5493)\]
Time zone tests in `SqlFunctions` should pass in `Europe/London`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-33-0 "Permalink")

- \[ [CALCITE-5197](https://issues.apache.org/jira/browse/CALCITE-5197)\]
Bump gradle to 7.4.2 and add checksum autoupdate
- \[ [CALCITE-5306](https://issues.apache.org/jira/browse/CALCITE-5306)\]
Remove JDK15/16 EOL non-LTS JDKs in CI
- \[ [CALCITE-5340](https://issues.apache.org/jira/browse/CALCITE-5340)\]
Tests should fail when actual and expected XML reference files are not identical
- \[ [CALCITE-5417](https://issues.apache.org/jira/browse/CALCITE-5417)\]
Include Proj4J as an api dependency once the license allows it
- \[ [CALCITE-5427](https://issues.apache.org/jira/browse/CALCITE-5427)\]
Provide code quality/coverage metrics with SonarCloud and JaCoCo
- \[ [CALCITE-5428](https://issues.apache.org/jira/browse/CALCITE-5428)\]
Reduce minimum Guava version to 16.0.1
- \[ [CALCITE-5433](https://issues.apache.org/jira/browse/CALCITE-5433)\]
Druid tests hang/fail intermittently in CI
- \[ [CALCITE-5474](https://issues.apache.org/jira/browse/CALCITE-5474)\]
Disable Sonar quality gates to avoid checks appearing as failures
- \[ [CALCITE-5475](https://issues.apache.org/jira/browse/CALCITE-5475)\]
Improve test coverage accuracy by aggregating modules

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-33-0 "Permalink")

- \[ [CALCITE-5239](https://issues.apache.org/jira/browse/CALCITE-5239)\]
Site: JDBC Adapter’s current limitations is incorrect
- \[ [CALCITE-5287](https://issues.apache.org/jira/browse/CALCITE-5287)\]
SQL reference page is missing from website

## [1.32.0](https://github.com/apache/calcite/releases/tag/calcite-1.32.0) / 2022-09-10 [Permalink](https://calcite.apache.org/docs/history.html\#v1-32-0 "Permalink")

This release
[fixes](https://issues.apache.org/jira/browse/CALCITE-5263) [CVE-2022-39135](http://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-39135),
an XML External Entity (XEE) vulnerability that allows a SQL query to
read the contents of files via the SQL functions `EXISTS_NODE`,
`EXTRACT_XML`, `XML_TRANSFORM` or `EXTRACT_VALUE`.

Coming 1 month after [1.31.0](https://calcite.apache.org/docs/history.html#v1-31-0) with 19 issues fixed by 17
contributors, this release also
[replaces\\
the ESRI spatial engine with JTS and proj4j](https://issues.apache.org/jira/browse/CALCITE-4294), adds
[65\\
spatial SQL functions](https://issues.apache.org/jira/browse/CALCITE-5262) including `ST_Centroid`, `ST_Covers` and
`ST_GeomFromGeoJSON`, adds the
[CHAR](https://issues.apache.org/jira/browse/CALCITE-5241)
SQL function, and improves the return type of the
[ARRAY and\\
MULTISET](https://issues.apache.org/jira/browse/CALCITE-4999) functions.

Contributors to this release:
Alessandro Solimando,
Ali Mansour,
Andrei Sereda,
Benchao Li,
Bertil Chapuis,
Chunwei Lei,
David Handermann,
Dmitry Sysolyatin,
Jiajun Bernoulli,
Jing Zhang,
Julian Hyde (release manager),
Lincoln Lee,
Mou Wu,
Ruben Quesada Lopez,
Stamatis Zampetakis,
TJ Banghart,
Zhengqiang Duan.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 18;
Guava versions 16.0.1 to 31.1-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-32-0 "Permalink")

None.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-32-0 "Permalink")

- \[ [CALCITE-5262](https://issues.apache.org/jira/browse/CALCITE-5262)\]
Add many spatial functions, including support for WKB (well-known binary) and
GeoJSON
- \[ [CALCITE-5241](https://issues.apache.org/jira/browse/CALCITE-5241)\]
Implement `CHAR` function for MySQL and Spark, also JDBC `{fn CHAR(n)}`
- \[ [CALCITE-5251](https://issues.apache.org/jira/browse/CALCITE-5251)\]
Support SQL hint for `Snapshot`
- \[ [CALCITE-4802](https://issues.apache.org/jira/browse/CALCITE-4802)\]
Support `IF(condition, then, else)` statements in Babel parser
- \[ [CALCITE-4999](https://issues.apache.org/jira/browse/CALCITE-4999)\]
`ARRAY`, `MULTISET` functions should return a collection of scalars if a
sub-query returns 1 column
- \[ [CALCITE-5126](https://issues.apache.org/jira/browse/CALCITE-5126)\]
Implicit column alias for single-column `UNNEST` should work with any
single-column `UNNEST`’s input

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-32-0 "Permalink")

- \[ [CALCITE-5278](https://issues.apache.org/jira/browse/CALCITE-5278)\]
Upgrade Janino from 3.1.6 to 3.1.8
- \[ [CALCITE-5232](https://issues.apache.org/jira/browse/CALCITE-5232)\]
Upgrade protobuf-java from 3.17.1 to 3.21.5

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-32-0 "Permalink")

- \[ [CALCITE-5270](https://issues.apache.org/jira/browse/CALCITE-5270)\]
JDBC adapter should not generate `FILTER (WHERE ...)` in Firebolt dialect
- \[ [CALCITE-5277](https://issues.apache.org/jira/browse/CALCITE-5277)\]
Increase `BINDABLE_CACHE` hit rate by making the order of
`EnumerableRelImplementor.stashedParameters` deterministic
- \[ [CALCITE-5263](https://issues.apache.org/jira/browse/CALCITE-5263)\]
SQL functions `EXISTS_NODE`, `EXTRACT_XML`, `XML_TRANSFORM` and `EXTRACT_VALUE`
allow user files to be read via XML External Entity (XEE) vulnerability
[CVE-2022-39135](http://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-39135)
(fixed by using a secure implementation of XML `DocumentBuilder`)
- \[ [CALCITE-4294](https://issues.apache.org/jira/browse/CALCITE-4294)\]
Use JTS and proj4j rather than ESRI as the underlying library for geospatial
(`ST_`) functions
- \[ [CALCITE-5247](https://issues.apache.org/jira/browse/CALCITE-5247)\]
`FilterJoinRule` cannot simplify left join to inner join for
`WHERE RHS.C1 IS NOT NULL OR RHS.C2 IS NOT NULL`
- \[ [CALCITE-5243](https://issues.apache.org/jira/browse/CALCITE-5243)\]
`SELECT NULL AS C` causes
`NoSuchMethodException: java.sql.ResultSet.getVoid(int)`
- \[ [CALCITE-5201](https://issues.apache.org/jira/browse/CALCITE-5201)\]
Improve `SemiJoinRule` to match `Join`’s right input which is unique for join
keys
- \[ [CALCITE-4223](https://issues.apache.org/jira/browse/CALCITE-4223)\]
Metadata handlers for `TableScan` should see whether the `RelOptTable`
implements the handler
- \[ [CALCITE-5178](https://issues.apache.org/jira/browse/CALCITE-5178)\]
Single column with `ROW` type generates wrong plan

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-32-0 "Permalink")

- \[ [CALCITE-5274](https://issues.apache.org/jira/browse/CALCITE-5274)\]
In `DiffRepository`, use a more secure `DocumentBuilderFactory` instance
- Add tests for correlated CTEs
- \[ [CALCITE-5192](https://issues.apache.org/jira/browse/CALCITE-5192)\]
`CodeGenerationBenchmark` throws `IllegalStateException`

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-32-0 "Permalink")

- \[ [CALCITE-5275](https://issues.apache.org/jira/browse/CALCITE-5275)\]
Release notes for Calcite 1.32.0
- Cosmetic changes to release notes
- Remove redundant ‘the’ in javadoc
- Change sereda’s role from Committer to PMC
- Fix 1.31.0 release date to 2022-08-02 (was 2022-08-01)
- Fix checkstyle violation for Calcite 1.31 release note

## [1.31.0](https://github.com/apache/calcite/releases/tag/calcite-1.31.0) / 2022-08-02 [Permalink](https://calcite.apache.org/docs/history.html\#v1-31-0 "Permalink")

This release comes four months after [1.30.0](https://calcite.apache.org/docs/history.html#v1-30-0),
contains contributions from 28 contributors, and resolves 81 issues.

Among others, it is worth highlighting the following improvements:

- \[ [CALCITE-4865](https://issues.apache.org/jira/browse/CALCITE-4865)\]
Allow table functions to be polymorphic
- \[ [CALCITE-5107](https://issues.apache.org/jira/browse/CALCITE-5107)\]
Support SQL hint for `Filter`, `SetOp`, `Sort`, `Window`, `Values`
- \[ [CALCITE-35](https://issues.apache.org/jira/browse/CALCITE-35)\]
Support parsing parenthesized joins
- \[ [CALCITE-3890](https://issues.apache.org/jira/browse/CALCITE-3890)\]
Derive `IS NOT NULL` filter for the inputs of inner join
- \[ [CALCITE-5085](https://issues.apache.org/jira/browse/CALCITE-5085)\]
Firebolt dialect implementation

Contributors to this release:
Ada Wang,
Andrei Sereda (release manager),
Benchao Li,
Chunwei Lei,
Daniel Henneberger,
Dmitry Sysolyatin,
Francis Chuang,
godfreyhe,
hannerwang,
henneberger,
Jing Zhang,
Julian Hyde,
Konstantin Orlov,
Liya Fan,
Michael Mior,
NobiGo,
onTheQT,
Roman Kondakov,
Ruben Quesada Lopez,
Sergey Nuyanzin,
Stamatis Zampetakis,
Viliam Durina,
Vladimir Ozerov,
Volodymyr Vysotskyi,
Wenrui Meng,
xiejiajun,
xurenhe,
zhangyue.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 18;
Guava versions 19.0 to 31.1-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-31-0 "Permalink")

- \[ [CALCITE-4936](https://issues.apache.org/jira/browse/CALCITE-4936)\]
Generalize `FilterCalcMergeRule`/`ProjectCalcMergeRule` to accept any
`Filter`/`Project`/`Calc` operator.

  - Old behavior: The Project operator is transformed into Calc.
  - New behavior: The Project operator is not transformed and the rule becomes NOOP.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-31-0 "Permalink")

- \[ [CALCITE-4865](https://issues.apache.org/jira/browse/CALCITE-4865)\]
Allow table functions to be polymorphic
- \[ [CALCITE-5089](https://issues.apache.org/jira/browse/CALCITE-5089)\]
Allow `GROUP BY ALL` or `DISTINCT` set quantifier on `GROUPING SETS`
- \[ [CALCITE-5085](https://issues.apache.org/jira/browse/CALCITE-5085)\]
Firebolt dialect implementation
- \[ [CALCITE-5086](https://issues.apache.org/jira/browse/CALCITE-5086)\]
SQL parser should allow `OFFSET` to occur before `LIMIT`
- \[ [CALCITE-5125](https://issues.apache.org/jira/browse/CALCITE-5125)\]
Extend `||` operator to work with arrays

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-31-0 "Permalink")

- \[ [CALCITE-5196](https://issues.apache.org/jira/browse/CALCITE-5196)\]
Bump apiguardian to 1.1.2
- \[ [CALCITE-5221](https://issues.apache.org/jira/browse/CALCITE-5221)\]
Upgrade Avatica version to 1.22.0. Vulnerability fix
[CVE-2022-36364](http://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-36364)
(see [CALCITE-5218](https://issues.apache.org/jira/browse/CALCITE-5218))
- \[ [CALCITE-5115](https://issues.apache.org/jira/browse/CALCITE-5115)\]
Upgrade jackson-databind from 2.9.10.1 to 2.13.2.1, and jackson from 2.10.0 to 2.13.2.1
- \[ [CALCITE-5112](https://issues.apache.org/jira/browse/CALCITE-5112)\]
Upgrade Jetty from 9.4.15.v20190215 to 9.4.46.v20220331
- \[ [CALCITE-5070](https://issues.apache.org/jira/browse/CALCITE-5070)\]
Upgrade Jekyll and ruby gems for site generation
- \[ [CALCITE-5037](https://issues.apache.org/jira/browse/CALCITE-5037)\]
Upgrade HSQLDB to 2.5.2

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-31-0 "Permalink")

- \[ [CALCITE-35](https://issues.apache.org/jira/browse/CALCITE-35)\]
Support parsing parenthesized joins
- \[ [CALCITE-5169](https://issues.apache.org/jira/browse/CALCITE-5169)\]
`xx < 1 OR xx > 1` cannot be simplified to `xx <> 1`
- \[ [CALCITE-4448](https://issues.apache.org/jira/browse/CALCITE-4448)\]
Use `TableMacro` user-defined table functions with `QueryableTable`
- \[ [CALCITE-5000](https://issues.apache.org/jira/browse/CALCITE-5000)\]
Expand `AGGREGATE_REDUCE_FUNCTIONS`, when arg of agg-call exists in the
aggregate’s group
- \[ [CALCITE-5091](https://issues.apache.org/jira/browse/CALCITE-5091)\]
`RelMdRowCount` can return more accurate rowCount when fetch is deterministic
and offset is dynamic
- \[ [CALCITE-5149](https://issues.apache.org/jira/browse/CALCITE-5149)\]
Refine `RelMdColumnUniqueness` for Aggregate by considering intersect keys
between target keys and group keys
- \[ [CALCITE-5036](https://issues.apache.org/jira/browse/CALCITE-5036)\]
`RelMdPredicates` support to analyze constant key for the operator of
`IS_NOT_DISTINCT_FROM`
- \[ [CALCITE-5044](https://issues.apache.org/jira/browse/CALCITE-5044)\]
JDBC adapter generates integer literal in `ORDER BY`, which some dialects
wrongly interpret as a reference to a field
- \[ [CALCITE-4936](https://issues.apache.org/jira/browse/CALCITE-4936)\]
Generalize `FilterCalcMergeRule`/`ProjectCalcMergeRule` to accept any
`Filter`/`Project`/`Calc` operator
- \[ [CALCITE-5083](https://issues.apache.org/jira/browse/CALCITE-5083)\]
In `RelBuilder.project_`, do not unwrap SARGs
- \[ [CALCITE-5061](https://issues.apache.org/jira/browse/CALCITE-5061)\]
Improve recursive application of the field trimming
- \[ [CALCITE-3890](https://issues.apache.org/jira/browse/CALCITE-3890)\]
Derive `IS NOT NULL` filter for the inputs of inner join
- \[ [CALCITE-5118](https://issues.apache.org/jira/browse/CALCITE-5118)\]
`SqlDatePartFunction#rewriteCall` should check operands length
- \[ [CALCITE-5162](https://issues.apache.org/jira/browse/CALCITE-5162)\]
`RelMdUniqueKeys` can return more precise unique keys for Aggregate
- \[ [CALCITE-5073](https://issues.apache.org/jira/browse/CALCITE-5073)\]
`JoinConditionPushRule` cannot infer `LHS.C1 = LHS.C2` from
`LHS.C1 = RHS.C1 AND LHS.C2 = RHS.C1`
- \[ [CALCITE-5107](https://issues.apache.org/jira/browse/CALCITE-5107)\]
Support SQL hint for `Filter`, `SetOp`, `Sort`, `Window`, `Values`
- \[ [CALCITE-5194](https://issues.apache.org/jira/browse/CALCITE-5194)\]
Cannot parse parenthesized `UNION` in `FROM`
- \[ [CALCITE-5206](https://issues.apache.org/jira/browse/CALCITE-5206)\]
Parser allows `MERGE` with mismatched parentheses
- \[ [CALCITE-4746](https://issues.apache.org/jira/browse/CALCITE-4746)\]
`PIVOT` with aggregate and no without alias fails in Babel parser
- \[ [CALCITE-5045](https://issues.apache.org/jira/browse/CALCITE-5045)\]
Alias within GroupingSets throws type mis-match exception
- \[ [CALCITE-5145](https://issues.apache.org/jira/browse/CALCITE-5145)\]
`CASE` statement within `GROUPING SETS` throws type mis-match exception
- \[ [CALCITE-5195](https://issues.apache.org/jira/browse/CALCITE-5195)\]
`ArrayIndexOutOfBoundsException` when inferring more equal conditions from join
condition for semi join
- \[ [CALCITE-5157](https://issues.apache.org/jira/browse/CALCITE-5157)\]
Query that applies dot operator (field access) to parenthesized expression
throws `ClassCastException`
- \[ [CALCITE-5191](https://issues.apache.org/jira/browse/CALCITE-5191)\]
Allow `ORDER BY` alias in BigQuery
- \[ [CALCITE-5134](https://issues.apache.org/jira/browse/CALCITE-5134)\]
Queries with subquery inside select list does not work if subquery uses table
from left join
- \[ [CALCITE-5177](https://issues.apache.org/jira/browse/CALCITE-5177)\]
Query loses hint after decorrelation
- \[ [CALCITE-5143](https://issues.apache.org/jira/browse/CALCITE-5143)\]
Allow custom time unit abbreviations in `FLOOR`, `CEIL`, `EXTRACT`,
`DATE_PART`, `DATEADD`, `DATEDIFF` and similar functions
- \[ [CALCITE-5179](https://issues.apache.org/jira/browse/CALCITE-5179)\]
In `RelToSqlConverter`, `AssertionError` for values with more than two items
when `SqlDialect#supportsAliasedValues` is false
- \[ [CALCITE-4907](https://issues.apache.org/jira/browse/CALCITE-4907)\]
JDBC adapter cannot push down join ON `TRUE` (cartesian product)
- \[ [CALCITE-5147](https://issues.apache.org/jira/browse/CALCITE-5147)\]
Allow `DATE`, `TIME`, `TIMESTAMP`, `INTERVAL` literals in BigQuery dialect
- \[ [CALCITE-5013](https://issues.apache.org/jira/browse/CALCITE-5013)\]
Unparse `SqlSetOperator` should be retained parentheses when generating SQL for
`UNION ... LIMIT`
- \[ [CALCITE-4897](https://issues.apache.org/jira/browse/CALCITE-4897)\]
Implicit type conversion is not complete for set operation in DML
- \[ [CALCITE-5027](https://issues.apache.org/jira/browse/CALCITE-5027)\]
Incorrect format for timestamp literals in `SqlDialect.quoteTimestampLiteral`
- \[ [CALCITE-5153](https://issues.apache.org/jira/browse/CALCITE-5153)\]
Create an immutable version of `ListSqlOperatorTable`
- \[ [CALCITE-5139](https://issues.apache.org/jira/browse/CALCITE-5139)\]
Improve Join print plan to add the `CorrelationId` info
- \[ [CALCITE-5003](https://issues.apache.org/jira/browse/CALCITE-5003)\]
`MergeUnion` on types with different collators produces wrong result
- \[ [CALCITE-5117](https://issues.apache.org/jira/browse/CALCITE-5117)\]
Optimize the `EXISTS` sub-query using `RelMdRowCount` metadata
- \[ [CALCITE-4861](https://issues.apache.org/jira/browse/CALCITE-4861)\]
Optimization of chained `CAST` calls can lead to unexpected behavior
- \[ [CALCITE-5048](https://issues.apache.org/jira/browse/CALCITE-5048)\]
Query with parameterized `LIMIT` and correlated sub-query throws
`AssertionError`, “not a literal”
- \[ [CALCITE-5032](https://issues.apache.org/jira/browse/CALCITE-5032)\]
`RelOptUtil#splitJoinCondition` returns wrong when there is no equal condition
- \[ [CALCITE-4992](https://issues.apache.org/jira/browse/CALCITE-4992)\]
Resource leak in Elasticsearch adapter
- \[ [CALCITE-4401](https://issues.apache.org/jira/browse/CALCITE-4401)\]
`SqlJoin.toString` throws `RuntimeException`, “No list started”
- \[ [CALCITE-5088](https://issues.apache.org/jira/browse/CALCITE-5088)\]
`JsonBuilder` should escape backslashes in JSON strings
- \[ [CALCITE-5021](https://issues.apache.org/jira/browse/CALCITE-5021)\]
Double `JOIN` is created for `NOT IN` when `IN`-list that the values all
non-nullable is converted to `Values`
- \[ [CALCITE-5064](https://issues.apache.org/jira/browse/CALCITE-5064)\]
Dialect factory returns ANSI SQL dialect for BigQuery
- \[ [CALCITE-4989](https://issues.apache.org/jira/browse/CALCITE-4989)\]
Nested JSON\_OBJECT creation does not produce proper JSON
- \[ [CALCITE-5050](https://issues.apache.org/jira/browse/CALCITE-5050)\]
Metadata (`RelMdRowCount`) should reflect the fact that an `Aggregate` with no
`GROUP BY` always returns 1 row
- \[ [CALCITE-4913](https://issues.apache.org/jira/browse/CALCITE-4913)\]
Deduplicate correlated variables in `SELECT` clause
- \[ [CALCITE-5150](https://issues.apache.org/jira/browse/CALCITE-5150)\]
Parser should parse subquery with order by inside array constructor
- \[ [CALCITE-5171](https://issues.apache.org/jira/browse/CALCITE-5171)\]
`NATURAL` join and `USING` should fail if join columns are not unique
- \[ [CALCITE-5170](https://issues.apache.org/jira/browse/CALCITE-5170)\]
Assertion error on range distribution creation
- \[ [CALCITE-5163](https://issues.apache.org/jira/browse/CALCITE-5163)\]
`MysqlSqlDialect` support to unparse `LISTAGG` aggregate function
- \[ [CALCITE-5166](https://issues.apache.org/jira/browse/CALCITE-5166)\]
Method `accept(RelShuttle)` is not overridden in `LogicalCalc` and
`LogicalTableModify`
- \[ [CALCITE-5137](https://issues.apache.org/jira/browse/CALCITE-5137)\]
`EnumerableUncollect` throws `NullPointerException` if input has ((List) null)
- \[ [CALCITE-5081](https://issues.apache.org/jira/browse/CALCITE-5081)\]
Group keys of Aggregate are wrongly changed during decorrelation
- \[ [CALCITE-5138](https://issues.apache.org/jira/browse/CALCITE-5138)\]
Join on condition generates wrong plan when the condition is sub-query
- \[ [CALCITE-5131](https://issues.apache.org/jira/browse/CALCITE-5131)\]
Remove redundant type cast

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-31-0 "Permalink")

- \[ [CALCITE-5095](https://issues.apache.org/jira/browse/CALCITE-5095)\]
Support Java 18 and Guava 31.1-jre
- \[ [CALCITE-5140](https://issues.apache.org/jira/browse/CALCITE-5140)\]
Spark, Piglet tests fail in GitHub CI with OpenJ9
- \[ [CALCITE-4147](https://issues.apache.org/jira/browse/CALCITE-4147)\]
Rename master branch to main
- \[ [CALCITE-5038](https://issues.apache.org/jira/browse/CALCITE-5038)\]
Making `AGGREGATE_ANY_PULL_UP_CONSTANTS`’s test case more rigorous

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-31-0 "Permalink")

- \[ [CALCITE-5092](https://issues.apache.org/jira/browse/CALCITE-5092)\]
Update [site/README.md](https://github.com/apache/calcite/blob/main/site/README.md)
about how to release the site
- Site: Add Jing Zhang as committer
- Site: Add Benchao Li as committer
- Site: Add Chunwei Lei and Vladimir Ozerov as PMC members
- Site: Outline process for becoming Calcite committer by request
- Site: Remove missing avatar for Ted Dunning
- Site: Fix release announcement for 1.30.0
- \[ [CALCITE-5075](https://issues.apache.org/jira/browse/CALCITE-5075)\]
Build fails due to rat check on Gemfile.lock
- \[ [CALCITE-5079](https://issues.apache.org/jira/browse/CALCITE-5079)\]
Update code demo of tutorial
- \[ [CALCITE-5102](https://issues.apache.org/jira/browse/CALCITE-5102)\]
Update github-pages gem for site build
- \[ [CALCITE-5106](https://issues.apache.org/jira/browse/CALCITE-5106)\]
Upgrade to Jekyll 4 and remove unnecessary dependencies from gemfile for site
- \[ [CALCITE-5108](https://issues.apache.org/jira/browse/CALCITE-5108)\]
Make website GDPR-compliant
- \[ [CALCITE-5110](https://issues.apache.org/jira/browse/CALCITE-5110)\]
Geode adapter’s java doc url is invalid
- \[ [CALCITE-5165](https://issues.apache.org/jira/browse/CALCITE-5165)\]
Improve javadoc
- \[ [CALCITE-3129](https://issues.apache.org/jira/browse/CALCITE-3129)\]
Automate website builds
- \[ [CALCITE-5111](https://issues.apache.org/jira/browse/CALCITE-5111)\]
jekyll-cache directory should be ignored by git
- \[ [CALCITE-5015](https://issues.apache.org/jira/browse/CALCITE-5015)\]
Fix typo in `PartiallyOrderedSet`

## [1.30.0](https://github.com/apache/calcite/releases/tag/calcite-1.30.0) / 2022-03-20 [Permalink](https://calcite.apache.org/docs/history.html\#v1-30-0 "Permalink")

This release comes over two months after [1.29.0](https://calcite.apache.org/docs/history.html#v1-29-0),
contains contributions from 29 authors,
and resolves 36 issues.

Among others, it is worth highlighting the following.

- [Babel parser support MySQL NULL-safe equal operator ‘<=>’](https://issues.apache.org/jira/browse/CALCITE-4980)
- [Support SQL hints for temporal table join](https://issues.apache.org/jira/browse/CALCITE-4967)
- [Fluent test fixtures so that dependent projects can write parser, validator and rules tests](https://issues.apache.org/jira/browse/CALCITE-4885)
- [Vulnerability issue CVE-2021-27568 fixed](https://issues.apache.org/jira/browse/CALCITE-5030)

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 17;
Guava versions 19.0 to 31.0.1-jre;
other software versions as specified in gradle.properties.

Contributors to this release:
Alessandro Solimando,
Bill Neil,
Chen Kai,
Eugen Stan,
Feng Zhu,
Jacques Nadeau,
Jake Xie,
Jay Narale,
Jiatao Tao,
Jing Zhang,
Julian Hyde,
Liya Fan (release manager),
LM Kang,
mans2singh,
Marco Jorge,
Marieke Gueye,
NobiGo,
Roman Puchkovskiy,
Ruben Quesada Lopez,
Scott Reynolds,
Soumyakanti Das,
Stamatis Zampetakis,
Vova Vysotskyi,
Will Noble,
Xiong Duan,
Xurenhe,
Yanjing Wang,
Yiqun Zhang,
Zhe Hu.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-30-0 "Permalink")

- \[ [CALCITE-4980](https://issues.apache.org/jira/browse/CALCITE-4980)\]
Babel parser support MySQL NULL-safe equal operator ‘<=>’
- \[ [CALCITE-4967](https://issues.apache.org/jira/browse/CALCITE-4967)\]
Support SQL hints for temporal table join
- \[ [CALCITE-4885](https://issues.apache.org/jira/browse/CALCITE-4885)\]
Fluent test fixtures so that dependent projects can write parser, validator and rules tests

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-30-0 "Permalink")

- \[ [CALCITE-5040](https://issues.apache.org/jira/browse/CALCITE-5040)\]
`SqlTypeFactoryTest.testUnknownCreateWithNullabilityTypeConsistency` fails
- \[ [CALCITE-5019](https://issues.apache.org/jira/browse/CALCITE-5019)\]
Avoid multiple scans when table is `ProjectableFilterableTable` and projections and filters act on different columns
- \[ [CALCITE-5011](https://issues.apache.org/jira/browse/CALCITE-5011)\]
`CassandraAdapterDataTypesTest` fails with initialization error
- \[ [CALCITE-5008](https://issues.apache.org/jira/browse/CALCITE-5008)\]
Ignore synthetic and static methods in `MetadataDef`
- \[ [CALCITE-4997](https://issues.apache.org/jira/browse/CALCITE-4997)\]
Keep `APPROX_COUNT_DISTINCT` in some `SqlDialect`s
- \[ [CALCITE-4996](https://issues.apache.org/jira/browse/CALCITE-4996)\]
In `RelJson`, add a `readExpression` method that converts JSON to a `RexNode` expression
- \[ [CALCITE-4995](https://issues.apache.org/jira/browse/CALCITE-4995)\]
`AssertionError` caused by `RelFieldTrimmer` on `SEMI/ANTI` join
- \[ [CALCITE-4994](https://issues.apache.org/jira/browse/CALCITE-4994)\]
SQL-to-RelNode conversion is slow if table contains hundreds of fields
- \[ [CALCITE-4991](https://issues.apache.org/jira/browse/CALCITE-4991)\]
Improve `RuleEventLogger` to also print input rels in `FULL_PLAN` mode
- \[ [CALCITE-4988](https://issues.apache.org/jira/browse/CALCITE-4988)\]
`((A IS NOT NULL OR B) AND A IS NOT NULL)` can’t be simplify to `(A IS NOT NULL)` When `A` is deterministic
- \[ [CALCITE-4986](https://issues.apache.org/jira/browse/CALCITE-4986)\]
Make `HepProgram` thread-safe
- \[ [CALCITE-4968](https://issues.apache.org/jira/browse/CALCITE-4968)\]
Use `TOP N` for MsSQL instead of `FETCH` without `OFFSET`
- \[ [CALCITE-4965](https://issues.apache.org/jira/browse/CALCITE-4965)\]
`IS NOT NULL` failed in Elasticsearch Adapter
- \[ [CALCITE-4963](https://issues.apache.org/jira/browse/CALCITE-4963)\]
Make it easier to implement interface `SqlDialectFactory`
- \[ [CALCITE-4953](https://issues.apache.org/jira/browse/CALCITE-4953)\]
Deprecate `TableAccessMap` class
- \[ [CALCITE-4952](https://issues.apache.org/jira/browse/CALCITE-4952)\]
Introduce a simplistic `RelMetadataQuery` option
- \[ [CALCITE-4912](https://issues.apache.org/jira/browse/CALCITE-4912)\]
Confusing javadoc of `RexSimplify.simplify`
- \[ [CALCITE-4901](https://issues.apache.org/jira/browse/CALCITE-4901)\]
JDBC adapter incorrectly adds `ORDER BY` columns to the `SELECT` list of generated SQL query
- \[ [CALCITE-4877](https://issues.apache.org/jira/browse/CALCITE-4877)\]
Support Snapshot in `RelMdColumnOrigins`
- \[ [CALCITE-4872](https://issues.apache.org/jira/browse/CALCITE-4872)\]
Add `UNKNOWN` value to enum `SqlTypeName`, distinct from the `NULL` type
- \[ [CALCITE-4702](https://issues.apache.org/jira/browse/CALCITE-4702)\]
Error when executing query with `GROUP BY` constant via JDBC adapter
- \[ [CALCITE-4683](https://issues.apache.org/jira/browse/CALCITE-4683)\]
IN-list converted to JOIN throws type mismatch exception
- \[ [CALCITE-4323](https://issues.apache.org/jira/browse/CALCITE-4323)\]
If a view definition has an `ORDER BY` clause, retain the sort if the view is used in a query at top level
- \[ [CALCITE-4054](https://issues.apache.org/jira/browse/CALCITE-4054)\]
`RepeatUnion` containing a `Correlate` with a `transientScan` on its RHS
causes `NullPointerException`
- \[ [CALCITE-3673](https://issues.apache.org/jira/browse/CALCITE-3673)\]
`ListTransientTable` should not leave tables in the schema
- \[ [CALCITE-3627](https://issues.apache.org/jira/browse/CALCITE-3627)\]
Incorrect null semantic for `ROW` function
- \[ [CALCITE-1794](https://issues.apache.org/jira/browse/CALCITE-1794)\]
Expressions with numeric comparisons are not simplified when `CAST` is present

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-30-0 "Permalink")

- \[ [CALCITE-5006](https://issues.apache.org/jira/browse/CALCITE-5006)\]
Gradle tasks for launching JDBC integration tests are not working
- \[ [CALCITE-4960](https://issues.apache.org/jira/browse/CALCITE-4960)\]
Enable unit tests in Elasticsearch Adapter

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-30-0 "Permalink")

- \[ [CALCITE-5030](https://issues.apache.org/jira/browse/CALCITE-5030)\]
Upgrade jsonpath version from 2.4.0 to 2.7.0
- \[ [CALCITE-5025](https://issues.apache.org/jira/browse/CALCITE-5025)\]
Upgrade commons-io version from 2.4 to 2.11.0
- \[ [CALCITE-5007](https://issues.apache.org/jira/browse/CALCITE-5007)\]
Upgrade H2 database version to 2.1.210
- \[ [CALCITE-4973](https://issues.apache.org/jira/browse/CALCITE-4973)\]
Upgrade log4j2 version to 2.17.1

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-30-0 "Permalink")

- Site: Update PMC Chair
- Site: Add external resources section in the community page
- Site: Add “calcite-clj - Use Calcite with Clojure” in talks section
- Site: Add Alessandro Solimando as committer
- Site: Change the javadoc title to Apache Calcite API
- Site: For tables that display results, center the content horizontally
- Site: Add syntax highlighting to SQL statements
- Site: Improve HTML tables display & update CSV tutorial

## [1.29.0](https://github.com/apache/calcite/releases/tag/calcite-1.29.0) / 2021-12-26 [Permalink](https://calcite.apache.org/docs/history.html\#v1-29-0 "Permalink")

This release comes two months after [1.28.0](https://calcite.apache.org/docs/history.html#v1-28-0),
contains contributions from 23 authors,
and resolves 47 issues.

This release upgrades
[log4j2 to 2.17.0](https://issues.apache.org/jira/browse/CALCITE-4950)
to fix security vulnerabilities such as
[CVE-2021-44228](http://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-44228)
and
[CVE-2021-45105](http://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-45105).

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 17;
Guava versions 19.0 to 31.0.1-jre;
other software versions as specified in gradle.properties.

Contributors to this release:
Ada Wong,
Aleksey Plekhanov,
Alessandro Solimando,
Chunwei Lei,
Francesco Gini,
Jacques Nadeau,
Jay Narale,
Julian Hyde,
liuyanze,
Louis Kuang,
NobiGo,
Ruben Quesada Lopez,
Rui Wang (release manager),
Sergey Nuyanzin,
Stamatis Zampetakis,
Thomas Rebele,
Vladimir Sitnikov,
Will Noble,
Zhe Hu.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-29-0 "Permalink")

- \[ [CALCITE-4822](https://issues.apache.org/jira/browse/CALCITE-4822)\]
Add `ARRAY_CONCAT`, `ARRAY_REVERSE`, `ARRAY_LENGTH` functions for BigQuery dialect
- \[ [CALCITE-4877](https://issues.apache.org/jira/browse/CALCITE-4877)\]
When a plugin class is not found, make the exception more explicit
- \[ [CALCITE-4841](https://issues.apache.org/jira/browse/CALCITE-4841)\]
Support `decimal` column type in CSV and File adapters
- \[ [CALCITE-4925](https://issues.apache.org/jira/browse/CALCITE-4925)\]
`AggregateReduceFunctionsRule` should accept arbitrary predicates

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-29-0 "Permalink")

- \[ [CALCITE-4839](https://issues.apache.org/jira/browse/CALCITE-4839)\]
Remove remnants of `ImmutableBeans` post 1.28 release
- \[ [CALCITE-4795](https://issues.apache.org/jira/browse/CALCITE-4795)\]
In class `SqlBasicCall`, make the `operands` field private
- \[ [CALCITE-4818](https://issues.apache.org/jira/browse/CALCITE-4818)\]
`AggregateExpandDistinctAggregatesRule` must infer correct data type for top
aggregate calls
- \[ [CALCITE-4551](https://issues.apache.org/jira/browse/CALCITE-4551)\]
Reusing immutable metadata cache keys
- \[ [CALCITE-4131](https://issues.apache.org/jira/browse/CALCITE-4131)\]
The `XmlFunctions` exception handled by `System.out`
- \[ [CALCITE-4875](https://issues.apache.org/jira/browse/CALCITE-4875)\]
`NVL` function incorrectly changes nullability of its operands
- \[ [CALCITE-4844](https://issues.apache.org/jira/browse/CALCITE-4844)\]
`IN`-list that references columns is wrongly converted to `Values`, and gives
incorrect results
- \[ [CALCITE-4846](https://issues.apache.org/jira/browse/CALCITE-4846)\]
`IN`-list that includes `NULL` converted to `Values` throws exception
- \[ [CALCITE-4884](https://issues.apache.org/jira/browse/CALCITE-4884)\]
Provide a new constructor for `RelJsonWriter` to allow customized `JsonBuilder`
- \[ [CALCITE-4876](https://issues.apache.org/jira/browse/CALCITE-4876)\]
JDBC adapter generates wrong SQL in Calcite dialect when `EnumerableIntersect`
is followed by `EnumerableLimit`
- \[ [CALCITE-4883](https://issues.apache.org/jira/browse/CALCITE-4883)\]
When `Exchange` is created from externalized JSON, `RelDistribution` is not
correctly set in its `traitSet`
- \[ [CALCITE-4783](https://issues.apache.org/jira/browse/CALCITE-4783)\]
`RelFieldTrimmer` incorrectly drops filter condition
- Log plan after physical tweaks in new line
- \[ [CALCITE-4927](https://issues.apache.org/jira/browse/CALCITE-4927)\]
Remove deprecated method `RelBuilder.groupKey(ImmutableBitSet, ImmutableList)`
that clashes with newer API method
- \[ [CALCITE-4928](https://issues.apache.org/jira/browse/CALCITE-4928)\]
Decouple Janino from `RelMetadataQuery`
- \[ [CALCITE-4932](https://issues.apache.org/jira/browse/CALCITE-4932)\]
Deprecate `JdbcCalc` and remove `JdbcCalcRule`
- \[ [CALCITE-4894](https://issues.apache.org/jira/browse/CALCITE-4894)\]
Materialized view rewriting fails for conjunctive top expressions in `SELECT`
clause
- \[ [CALCITE-4929](https://issues.apache.org/jira/browse/CALCITE-4929)\]
Add default methods for `getDef` on metadata handlers
- Improve debug message in `IterativeRuleDriver`
- Remove duplicate entries from `RelOptRules.CALC_RULES`
- \[ [CALCITE-4906](https://issues.apache.org/jira/browse/CALCITE-4906)\]
Wrong result for scalar sub-query (single value aggregation) from empty input
- \[ [CALCITE-4941](https://issues.apache.org/jira/browse/CALCITE-4941)\]
`SemiJoinRule` loses hints
- \[ [CALCITE-4895](https://issues.apache.org/jira/browse/CALCITE-4895)\]
`MAP` type in user-defined function (UDF) cannot be created from externalized
JSON
- \[ [CALCITE-4946](https://issues.apache.org/jira/browse/CALCITE-4946)\]
Add method `RelBuilder.size()`
- \[ [CALCITE-4704](https://issues.apache.org/jira/browse/CALCITE-4704)\]
Log produced plan after rule application using explain formatting
- \[ [CALCITE-4700](https://issues.apache.org/jira/browse/CALCITE-4700)\]
`AggregateUnionTransposeRule` produces wrong `groupingSets` for the top
`Aggregate`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-29-0 "Permalink")

- Exclude kotlin-stdlib from `:core` runtime dependencies
- Clarify why squash commits option in GitHub PR merge is disabled
- Keep backslash when autoformatting `...\n" +`
- Use GitHub Action concurrency feature to cancel stale CI executions
- Set timeout for running Druid tests in GitHub CI
- \[ [CALCITE-4917](https://issues.apache.org/jira/browse/CALCITE-4917)\]
Add test for `a IS NOT NULL AND a = b` simplification
- \[ [CALCITE-4851](https://issues.apache.org/jira/browse/CALCITE-4851)\]
Build gives lots of ‘`Execution optimizations have been disabled`’ warnings

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-29-0 "Permalink")

- \[ [CALCITE-4847](https://issues.apache.org/jira/browse/CALCITE-4847)\]
Support Java 16 and 17
- \[ [CALCITE-4858](https://issues.apache.org/jira/browse/CALCITE-4858)\]
Use Log4j2 instead of unsupported Log4j (1.x) in tests
- \[ [CALCITE-4768](https://issues.apache.org/jira/browse/CALCITE-4768)\]
Upgrade DataStax Driver for Apache Cassandra® version to latest 4.x
- Bump `com.github.vlsi.vlsi-release-plugins` to 1.76
- Update Gradle to 7.3
- \[ [CALCITE-4937](https://issues.apache.org/jira/browse/CALCITE-4937)\]
Upgrade Calcite to Avatica 1.20
- \[ [CALCITE-4938](https://issues.apache.org/jira/browse/CALCITE-4938)\]
Upgrade SQLLine to 1.12.0
- \[ [CALCITE-4948](https://issues.apache.org/jira/browse/CALCITE-4948)\]
Upgrade Elasticsearch to 7.10.2
- \[ [CALCITE-4950](https://issues.apache.org/jira/browse/CALCITE-4950)\]
Upgrade log4j2 version 2.17.0

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-29-0 "Permalink")

- Site: Add Xiong Duan as committer
- Site: Fix typo in reference.md

## [1.28.0](https://github.com/apache/calcite/releases/tag/calcite-1.28.0) / 2021-10-19 [Permalink](https://calcite.apache.org/docs/history.html\#v1-28-0 "Permalink")

This release comes four months after [1.27.0](https://calcite.apache.org/docs/history.html#v1-27-0),
contains contributions from 38 authors,
and resolves 76 issues.
New features include the
[UNIQUE](https://issues.apache.org/jira/browse/CALCITE-4486)
sub-query predicate, the
[MODE](https://issues.apache.org/jira/browse/CALCITE-4661) aggregate function,
[PERCENTILE\_CONT and PERCENTILE\_DISC](https://issues.apache.org/jira/browse/CALCITE-4644)
inverse distribution functions, an
[Exasol dialect](https://issues.apache.org/jira/browse/CALCITE-4614)
for the JDBC adapter, and improvements to
[materialized](https://issues.apache.org/jira/browse/CALCITE-4779) [view](https://issues.apache.org/jira/browse/CALCITE-3935) [recognition](https://issues.apache.org/jira/browse/CALCITE-4774).

This release contains some breaking changes due to the
[replacement of ImmutableBeans with Immutables](https://issues.apache.org/jira/browse/CALCITE-4787);
the changes concern custom planner rule configurations, in particular
`interface RelRule.Config`, and are fully described in the
[news item](https://calcite.apache.org/news/2021/10/19/release-1.28.0).
Two APIs are deprecated and will be [removed in release 1.29](https://calcite.apache.org/docs/history.html#to-be-removed-in-1-29-0).

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 15;
Guava versions 19.0 to 31.0.1-jre;
other software versions as specified in gradle.properties.

Contributors to this release:
Alessandro Solimando,
Alon Eldar,
Amir Gajst,
Bruce Irschick,
dz,
Evgeniy Stanilovskiy,
Feng Zhu,
Grzegorz Gierlach,
Haisheng Yuan,
Jack Scott,
Jacky Yin,
Jacques Nadeau,
James Starr,
Jesus Camacho Rodriguez,
Jianhui Dong,
Jiasen Sheng,
Julian Hyde (release manager),
Liu Enze,
Michael Mior,
Narayanan Venkateswaran,
Nick Riasanovsky,
NobiGo,
Rafay Qureshi,
Ruben Quesada Lopez,
Sergey Nuyanzin,
Stamatis Zampetakis,
Taras Ledkov,
Thomas Rebele,
TJ Banghart,
Ulrich Kramer,
Vladimir Ozerov,
Vladimir Sitnikov,
Will Noble,
Xurenhe,
Yanjing Wang,
Yingyu Wang,
YuKong.

#### Deprecated for removal next release [Permalink](https://calcite.apache.org/docs/history.html\#to-be-removed-in-1-29-0 "Permalink")

- In 1.28,
\[ [CALCITE-4787](https://issues.apache.org/jira/browse/CALCITE-4787)\]
added `class  Immutables` and deprecated `ImmutableBeans`; in 1.29,
\[ [CALCITE-4839](https://issues.apache.org/jira/browse/CALCITE-4839)\]
will remove `ImmutableBeans`
- In 1.28,
\[ [CALCITE-4795](https://issues.apache.org/jira/browse/CALCITE-4795)\]
deprecated the `operands` field of `SqlBasicCall`. Before 1.29, we will make
that field private.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-28-0 "Permalink")

- \[ [CALCITE-4719](https://issues.apache.org/jira/browse/CALCITE-4719)\]
Add variants of `RexSubQuery` that collect sub-queries into `MULTISET`, `ARRAY`
and `MAP` collections
- \[ [CALCITE-3524](https://issues.apache.org/jira/browse/CALCITE-3524)\]
In `RelBuilder`, add methods for creating various kinds of sub-query
- \[ [CALCITE-2736](https://issues.apache.org/jira/browse/CALCITE-2736)\]
`ReduceExpressionsRule` never reduces dynamic expressions but this should be
configurable
- \[ [CALCITE-4847](https://issues.apache.org/jira/browse/CALCITE-4847)\]
Parse SQL with BigQuery-style quoted identifiers and character literals
- \[ [CALCITE-4805](https://issues.apache.org/jira/browse/CALCITE-4805)\]
Calcite should convert a small `IN`-list as if the user had written `OR`, even
if the `IN`-list contains `NULL`
- \[ [CALCITE-4779](https://issues.apache.org/jira/browse/CALCITE-4779)\]
If `GROUP BY` clause contains literal, materialized view recognition fails
- \[ [CALCITE-4486](https://issues.apache.org/jira/browse/CALCITE-4486)\]
`UNIQUE` sub-query
- \[ [CALCITE-3935](https://issues.apache.org/jira/browse/CALCITE-3935)\]
Enhance join materialization, support to pull-up filters under join of left or
right
- \[ [CALCITE-4767](https://issues.apache.org/jira/browse/CALCITE-4767)\]
JDBC adapter wrongly quotes backticks inside BigQuery identifiers
- \[ [CALCITE-4774](https://issues.apache.org/jira/browse/CALCITE-4774)\]
Materialized view recognition fails for equivalent predicates
- \[ [CALCITE-4742](https://issues.apache.org/jira/browse/CALCITE-4742)\]
Implement `SOME <>` sub-query
- \[ [CALCITE-4726](https://issues.apache.org/jira/browse/CALCITE-4726)\]
Support aggregate calls with a `FILTER` clause in
`AggregateExpandWithinDistinctRule`
- \[ [CALCITE-4748](https://issues.apache.org/jira/browse/CALCITE-4748)\]
If there are duplicate `GROUPING SETS`, Calcite should return duplicate rows
- \[ [CALCITE-4665](https://issues.apache.org/jira/browse/CALCITE-4665)\]
Allow `Aggregate.groupKey` to be a strict superset of `Aggregate.groupKeys`
- \[ [CALCITE-4724](https://issues.apache.org/jira/browse/CALCITE-4724)\]
In JDBC adapter for ClickHouse, implement `Values` by generating `SELECT`
without `FROM`
- \[ [CALCITE-4673](https://issues.apache.org/jira/browse/CALCITE-4673)\]
If arguments to a table function are correlation variables, `SqlToRelConverter`
should eliminate duplicate variables
- \[ [CALCITE-4642](https://issues.apache.org/jira/browse/CALCITE-4642)\]
Use `RelDataTypeSystem` from `Config` in `Planner`
- \[ [CALCITE-4661](https://issues.apache.org/jira/browse/CALCITE-4661)\]
Add `MODE` aggregate function
- \[ [CALCITE-4420](https://issues.apache.org/jira/browse/CALCITE-4420)\]
Some simple arithmetic operations can be simplified
- \[ [CALCITE-4640](https://issues.apache.org/jira/browse/CALCITE-4640)\]
Propagate table scan hints to JDBC
- \[ [CALCITE-4668](https://issues.apache.org/jira/browse/CALCITE-4668)\]
`RelBuilder.join` should convert `Correlate` to `Join` if correlation variable
is unused
- \[ [CALCITE-4644](https://issues.apache.org/jira/browse/CALCITE-4644)\]
Add `PERCENTILE_CONT` and `PERCENTILE_DISC` functions
- \[ [CALCITE-4614](https://issues.apache.org/jira/browse/CALCITE-4614)\]
Exasol dialect implementation
- \[ [CALCITE-4158](https://issues.apache.org/jira/browse/CALCITE-4158)\]
In generated SQL, “`*`” should be followed by space
- \[ [CALCITE-4606](https://issues.apache.org/jira/browse/CALCITE-4606)\]
In Elasticsearch adapter, translate `SEARCH` call to `termsQuery`
- \[ [CALCITE-4499](https://issues.apache.org/jira/browse/CALCITE-4499)\]
`FilterJoinRule` misses opportunity to push `Filter` to `SemiJoin` input

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-28-0 "Permalink")

- \[ [CALCITE-4848](https://issues.apache.org/jira/browse/CALCITE-4848)\]
Adding a `HAVING` condition to a query with a dynamic parameter makes the result
always empty
- \[ [CALCITE-4550](https://issues.apache.org/jira/browse/CALCITE-4550)\]
Simplify `JaninoRelMetadataProvider` API for binding methods
- \[ [CALCITE-4740](https://issues.apache.org/jira/browse/CALCITE-4740)\]
JDBC adapter generates incorrect `HAVING` clause in BigQuery dialect
- Refactor: Introduce field `SqlUtil.GENERATED_EXPR_ALIAS_PREFIX`
- \[ [CALCITE-4616](https://issues.apache.org/jira/browse/CALCITE-4616)\]
`AggregateUnionTransposeRule` causes row type mismatch when some inputs have
unique grouping key
- \[ [CALCITE-4795](https://issues.apache.org/jira/browse/CALCITE-4795)\]
In class `SqlBasicCall`, deprecated the `operands` field
- \[ [CALCITE-4628](https://issues.apache.org/jira/browse/CALCITE-4628)\]
If `SqlImplementor` fails, include the `RelNode` in the exception
- \[ [CALCITE-4757](https://issues.apache.org/jira/browse/CALCITE-4757)\]
In Avatica, support columns of type `NULL` in query results
- \[ [CALCITE-4602](https://issues.apache.org/jira/browse/CALCITE-4602)\]
`ClassCastException` retrieving from `ARRAY` that has mixed `INTEGER` and
`DECIMAL` elements
- \[ [CALCITE-4600](https://issues.apache.org/jira/browse/CALCITE-4600)\]
`ClassCastException` retrieving from an `ARRAY` that has `DATE`, `TIME` or
`TIMESTAMP` elements
- \[ [CALCITE-3338](https://issues.apache.org/jira/browse/CALCITE-3338)\]
Error with `executeBatch` and `preparedStatement` when using `RemoteMeta`
- \[ [CALCITE-4811](https://issues.apache.org/jira/browse/CALCITE-4811)\]
`Coalesce(null, row)` fails with `NullPointerException`
- \[ [CALCITE-3583](https://issues.apache.org/jira/browse/CALCITE-3583)\]
`Exchange` operator deserialize fails when the `RexInput` has no `RelCollation`
- \[ [CALCITE-3745](https://issues.apache.org/jira/browse/CALCITE-3745)\]
`CompileException` in `UnitCompiler` when using multiple class loaders
- \[ [CALCITE-4834](https://issues.apache.org/jira/browse/CALCITE-4834)\]
`JaninoRelMetadataProvider` uses hardcoded class name
- \[ [CALCITE-4819](https://issues.apache.org/jira/browse/CALCITE-4819)\]
`SemiJoin` operator is not skipped in materialized view-based rewriting
algorithm
- \[ [CALCITE-4546](https://issues.apache.org/jira/browse/CALCITE-4546)\]
Change metadata dispatch to avoid registration of all `RelNode` subtypes
- \[ [CALCITE-4787](https://issues.apache.org/jira/browse/CALCITE-4787)\]
Replace `ImmutableBeans` with `Immutables` in `core` module

  - \[ [CALCITE-4830](https://issues.apache.org/jira/browse/CALCITE-4830)\]
    Remove remaining uses of `ImmutableBeans` and deprecate
  - \[ [CALCITE-4825](https://issues.apache.org/jira/browse/CALCITE-4825)\]
    Move remaining core/main off of `ImmutableBeans`
- \[ [CALCITE-4532](https://issues.apache.org/jira/browse/CALCITE-4532)\]
Correct code generated for primitive-object `ConstantExpression`
- \[ [CALCITE-3409](https://issues.apache.org/jira/browse/CALCITE-3409)\]
Add a method in `RelOptMaterializations` to allow registering `UnifyRule`
- \[ [CALCITE-4773](https://issues.apache.org/jira/browse/CALCITE-4773)\]
`RelDecorrelator`’s `RemoveSingleAggregateRule` can produce result with wrong
row type
- \[ [CALCITE-4544](https://issues.apache.org/jira/browse/CALCITE-4544)\]
Deprecate `Metadata` API backed by Java Reflection
- \[ [CALCITE-4772](https://issues.apache.org/jira/browse/CALCITE-4772)\]
`PushProjector` should retain alias when handling `RexCall`
- Remove obsolete/misleading comments in `RelOptUtil#classifyFilters`
- \[ [CALCITE-4784](https://issues.apache.org/jira/browse/CALCITE-4784)\]
Ensure `Correlate#requiredColumns` is subset of columns in left relation
- \[ [CALCITE-4177](https://issues.apache.org/jira/browse/CALCITE-4177)\]
`RelJson` should throw if asked to deserialize a call to an unknown operator
- Add `RelBuilder.lessThan`, and use `RelBuilder` shorthands
- \[ [CALCITE-4766](https://issues.apache.org/jira/browse/CALCITE-4766)\]
Remove unreachable code from `SqlValidatorImpl#performUnconditionalRewrites`
for `Values` node
- \[ [CALCITE-4747](https://issues.apache.org/jira/browse/CALCITE-4747)\]
In `HepPlanner`, remove outdated graph edges
- \[ [CALCITE-4760](https://issues.apache.org/jira/browse/CALCITE-4760)\]
`RelBuilder` creation fails with error ‘`No suitable driver found for
jdbc:calcite:`’ in shaded Calcite
- \[ [CALCITE-4584](https://issues.apache.org/jira/browse/CALCITE-4584)\]
Using function in `PARTITION BY` list of `OVER` window causes conversion
exception
- \[ [CALCITE-4734](https://issues.apache.org/jira/browse/CALCITE-4734)\]
If there are duplicate `RexNode` in `MutableCalc`, `SubstitutionVisitor` should
return right rebuild `RexNode`
- \[ [CALCITE-4741](https://issues.apache.org/jira/browse/CALCITE-4741)\]
`AbstractRelNode#getId` can overflow into a negative value, causing
`CompileException` in the `implement` methods of certain `Enumerable`
sub-classes
- \[ [CALCITE-4652](https://issues.apache.org/jira/browse/CALCITE-4652)\]
`AggregateExpandDistinctAggregatesRule` must cast top aggregates to original
type
- \[ [CALCITE-4716](https://issues.apache.org/jira/browse/CALCITE-4716)\]
`ClassCastException` converting Sarg in `RelNode` to SQL
- \[ [CALCITE-4706](https://issues.apache.org/jira/browse/CALCITE-4706)\]
JDBC adapter generates casts exceeding Redshift’s data types bounds
- \[ [CALCITE-4485](https://issues.apache.org/jira/browse/CALCITE-4485)\]
JDBC adapter generates invalid SQL when one of the joins is `INNER JOIN ... ON
TRUE`
- \[ [CALCITE-4623](https://issues.apache.org/jira/browse/CALCITE-4623)\]
`SemiJoinRule` should not match semi-join
- \[ [CALCITE-4692](https://issues.apache.org/jira/browse/CALCITE-4692)\]
Redshift does not support `DOUBLE` or `TINYINT` datatypes
- \[ [CALCITE-4690](https://issues.apache.org/jira/browse/CALCITE-4690)\]
Error when executing query with `CHARACTER SET` in Redshift
- \[ [CALCITE-4675](https://issues.apache.org/jira/browse/CALCITE-4675)\]
Error executing query with SUM and multiplication via JDBC adapter
- \[ [CALCITE-4674](https://issues.apache.org/jira/browse/CALCITE-4674)\]
Excess quotes in generated SQL when “`*`” is a column alias
- \[ [CALCITE-3775](https://issues.apache.org/jira/browse/CALCITE-3775)\]
Implicit lookup methods in `SimpleCalciteSchema` ignore case sensitivity
parameter
- \[ [CALCITE-4638](https://issues.apache.org/jira/browse/CALCITE-4638)\]
`VolcanoPlanner` fails to recognize transformation rule correctly in the
top-down mode
- \[ [CALCITE-4655](https://issues.apache.org/jira/browse/CALCITE-4655)\]
`JdbcTable.scan` throws `NullPointerException`
- \[ [CALCITE-4636](https://issues.apache.org/jira/browse/CALCITE-4636)\]
Switch out of agg mode when constructing `RelCollation` for aggregate functions
- \[ [CALCITE-4619](https://issues.apache.org/jira/browse/CALCITE-4619)\]
`FULL JOIN` plan cannot be executed in MySQL

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-28-0 "Permalink")

- Bump JDK from 15 to 17 in seed build cache CI jobs
- \[ [CALCITE-4798](https://issues.apache.org/jira/browse/CALCITE-4798)\]
Gradle build fails due to deprecated metadata APIs
- Use jdk16 instead of jdk17 since jdk17 is not yet available at AppVeyor
- Fix string reference to `HrSchema` in `MaterializationTest` with
`HrSchema.class.getName()`
- \[ [CALCITE-4829](https://issues.apache.org/jira/browse/CALCITE-4829)\]
Bump Gradle to 7.2 and test with Java 17 at GitHub Actions
- Fix `ErrorProne` violations in `testkit`
- Add missing `@Override` annotations
- \[ [CALCITE-4821](https://issues.apache.org/jira/browse/CALCITE-4821)\]
Move utility test classes into `calcite-testkit` and unpublish `-test.jar`
- \[ [CALCITE-4823](https://issues.apache.org/jira/browse/CALCITE-4823)\]
Suppress warnings for `java.security.AccessController` deprecation
- Skip `EqualsHashCode` verification in `ErrorProne`: it is already verified with
`Checkstyle`
- \[ [CALCITE-4790](https://issues.apache.org/jira/browse/CALCITE-4790)\]
Make Gradle pass the `user.timezone` property to the test JVM
- \[ [CALCITE-4793](https://issues.apache.org/jira/browse/CALCITE-4793)\]
`CassandraAdapterDataTypesTest.testCollectionsInnerValues` fails depending on
the user timezone
- Replace deprecated `com.google.common.io.Files.createTempDir()` with
`java.nio.file.Files.createTempDirectory()` in ElasticSearch tests
- \[ [CALCITE-4789](https://issues.apache.org/jira/browse/CALCITE-4789)\]
Build is broken on Guava versions < 21
- Enable `JdbcTest#testBushy` and update expected plan
- `RelOptRulesTest` improvements
- \[ [CALCITE-4312](https://issues.apache.org/jira/browse/CALCITE-4312)\]
Improve content of `prepareVote` draft email

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-28-0 "Permalink")

- Bump Guava maximum version up to 31.0.1-jre
- \[ [CALCITE-4762](https://issues.apache.org/jira/browse/CALCITE-4762)\]
Upgrade Calcite to Avatica 1.19
- \[ [CALCITE-4836](https://issues.apache.org/jira/browse/CALCITE-4836)\]
Upgrade protobuf-java 3.6.1 → 3.17.1
- Bump JUnit5 to 5.8.1

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-28-0 "Permalink")

- \[ [CALCITE-4835](https://issues.apache.org/jira/browse/CALCITE-4835)\]
Release Calcite 1.28.0
- Site: Pronouns, talks
- Site: Add Zhaohui Xu as committer
- Site: Update fengzhu’s organization and add pronouns
- Site: Remove vote email from release instructions, and minor improvements
- Site: Add upcoming talk about Morel and update past talks section
- Site: Remove contributors name from commit summary
- \[ [CALCITE-4656](https://issues.apache.org/jira/browse/CALCITE-4656)\]
Broken CI links on develop web page
- \[ [CALCITE-4796](https://issues.apache.org/jira/browse/CALCITE-4796)\]
Travis links in `README.md` should point to `app.travis-ci.com` instead of
`travis-ci.org`
- Site: HTTP to HTTPS redirection is not working
- Site: Add zabetak’s pronouns
- Site: Add michaelmior’s pronouns
- Site: Update jhyde’s organization and add pronouns
- Site is not published due to bad yaml file suffix
- Site: Add upcoming talk at ApacheCon’21 and info about tutorial at BOSS21
- Site: Sort table of aggregate functions
- Site: Deploy using `.asf.yml`
- Site: Add Vladimir Ozerov as committer
- Site: Remove nowadays redundant minified javascript files

## [1.27.0](https://github.com/apache/calcite/releases/tag/calcite-1.27.0) / 2021-06-03 [Permalink](https://calcite.apache.org/docs/history.html\#v1-27-0 "Permalink")

This release comes eight months after [1.26.0](https://calcite.apache.org/docs/history.html#v1-26-0). It includes more than 150 resolved
issues, comprising a few new features, three minor breaking changes, many bug-fixes and small
improvements, as well as code quality enhancements and better test coverage.

Among others, it is worth highlighting the following:

- [InnoDB adapter](https://issues.apache.org/jira/browse/CALCITE-4034)
- [Three-valued logic for SEARCH operator](https://issues.apache.org/jira/browse/CALCITE-4446)
- [MergeUnion operator in Enumerable convention](https://issues.apache.org/jira/browse/CALCITE-3221)
- [Explain plan with DOT format](https://issues.apache.org/jira/browse/CALCITE-4260)
- [ErrorProne code quality checks](https://issues.apache.org/jira/browse/CALCITE-4314)

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 15;
Guava versions 19.0 to 29.0-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-27-0 "Permalink")

- \[ [CALCITE-4251](https://issues.apache.org/jira/browse/CALCITE-4521)\]
Get the origin column, even if it is derived
- \[ [CALCITE-4570](https://issues.apache.org/jira/browse/CALCITE-4570)\]
Always validate preconditions in Filter/Correlate/Snapshot expressions when
assertions are enabled
- \[ [CALCITE-4427](https://issues.apache.org/jira/browse/CALCITE-4427)\]
Make `SUBSTRING` operator comply with ISO standard SQL

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-27-0 "Permalink")

- \[ [CALCITE-4564](https://issues.apache.org/jira/browse/CALCITE-4564)\]
Initialization context for non-static user-defined functions (UDFs)
- \[ [CALCITE-4477](https://issues.apache.org/jira/browse/CALCITE-4477)\]
In `Interpreter`, support table-valued functions
- \[ [CALCITE-4418](https://issues.apache.org/jira/browse/CALCITE-4418)\]
Allow Interpreter to read from JDBC input
- \[ [CALCITE-3574](https://issues.apache.org/jira/browse/CALCITE-3574)\]
Add `RLIKE` operator (similar to `LIKE`, but Hive- and Spark-specific)
(Shradha Ambekar)
- \[ [CALCITE-4483](https://issues.apache.org/jira/browse/CALCITE-4483)\]
`WITHIN DISTINCT` clause for aggregate functions (experimental)
- \[ [CALCITE-3221](https://issues.apache.org/jira/browse/CALCITE-3221)\]
Add `MergeUnion` operator in `Enumerable` convention
- \[ [CALCITE-4349](https://issues.apache.org/jira/browse/CALCITE-4349)\]
`GROUP_CONCAT` aggregate function (MySQL’s equivalent of `LISTAGG`)
- \[ [CALCITE-4443](https://issues.apache.org/jira/browse/CALCITE-4443)\]
Add `ILIKE` operator (as `LIKE`, but case-insensitive and Postgres-specific)
(Ondřej Štumpf)
- \[ [CALCITE-4456](https://issues.apache.org/jira/browse/CALCITE-4456)\]
Allows all value expressions in `ROW`
- \[ [CALCITE-4433](https://issues.apache.org/jira/browse/CALCITE-4433)\]
Add `UNPIVOT` operator to SQL
- \[ [CALCITE-4408](https://issues.apache.org/jira/browse/CALCITE-4408)\]
Implement Oracle `SUBSTR` function (James Starr)
- \[ [CALCITE-4374](https://issues.apache.org/jira/browse/CALCITE-4374)\]
Support materialized view recognition when query distinct aggregate on target
`GROUP BY` columns (xzh)
- \[ [CALCITE-4369](https://issues.apache.org/jira/browse/CALCITE-4369)\]
Support `COUNTIF` aggregate function for BigQuery (Aryeh Hillman)
- \[ [CALCITE-4354](https://issues.apache.org/jira/browse/CALCITE-4354)\]
Allow `ITEM` operator on `ROW/STRUCT` data types (Alessandro Solimando)
- \[ [CALCITE-4335](https://issues.apache.org/jira/browse/CALCITE-4335)\]
`ARRAY_AGG`, `ARRAY_CONCAT_AGG`, `STRING_AGG` aggregate functions for BigQuery
- \[ [CALCITE-2935](https://issues.apache.org/jira/browse/CALCITE-2935)\]
Support `BOOL_AND`, `BOOL_OR`, `LOGICAL_AND`, `LOGICAL_OR` aggregate functions
(ShuMingLi)
- \[ [CALCITE-3731](https://issues.apache.org/jira/browse/CALCITE-3731)\]
Add `IF` function for BigQuery, Hive and Spark dialects (Vaibhav Jain)
- \[ [CALCITE-4260](https://issues.apache.org/jira/browse/CALCITE-4260)\]
Support plan explain with `DOT` format (Liya Fan)
- \[ [CALCITE-4297](https://issues.apache.org/jira/browse/CALCITE-4297)\]
Allow BigQuery to parse and validate niladic functions (Mr. Swett)
- \[ [CALCITE-4034](https://issues.apache.org/jira/browse/CALCITE-4034)\]
`InnoDB` adapter (neoremind)

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-27-0 "Permalink")

- \[ [CALCITE-4497](https://issues.apache.org/jira/browse/CALCITE-4497)\]
In `RelBuilder`, support windowed aggregate functions (OVER)
- \[ [CALCITE-4620](https://issues.apache.org/jira/browse/CALCITE-4620)\]
Join on `CASE` causes `AssertionError` in `RelToSqlConverter`
- \[ [CALCITE-4446](https://issues.apache.org/jira/browse/CALCITE-4446)\]
Implement three-valued logic for SEARCH operator
- \[ [CALCITE-4621](https://issues.apache.org/jira/browse/CALCITE-4621)\]
`SemiJoinRule` throws `AssertionError` on `ANTI` join
- \[ [CALCITE-4610](https://issues.apache.org/jira/browse/CALCITE-4610)\]
Join on range causes `AssertionError` in `RelToSqlConverter`
- \[ [CALCITE-4609](https://issues.apache.org/jira/browse/CALCITE-4609)\]
`AggregateRemoveRule` throws while handling `AVG`
- \[ [CALCITE-4603](https://issues.apache.org/jira/browse/CALCITE-4603)\]
Least restrictive type considers only the last element in collections of collections
- \[ [CALCITE-4548](https://issues.apache.org/jira/browse/CALCITE-4548)\]
`SqlToRelConverter#convertExpression` cannot convert `SqlNode` with sub query (jibiyr)
- \[ [CALCITE-2317](https://issues.apache.org/jira/browse/CALCITE-2317)\]
Support JDBC `DatabaseMetaData#getFunctions` (Malte Bellmann)
- \[ [CALCITE-4594](https://issues.apache.org/jira/browse/CALCITE-4594)\]
Interpreter returns wrong result when `VALUES` has zero fields
- \[ [CALCITE-4510](https://issues.apache.org/jira/browse/CALCITE-4510)\]
`RexLiteral` can produce wrong digest for some user defined types
- \[ [CALCITE-4560](https://issues.apache.org/jira/browse/CALCITE-4560)\]
Wrong plan when decorrelating `EXISTS` subquery with `COALESCE` in the predicate
- \[ [CALCITE-4574](https://issues.apache.org/jira/browse/CALCITE-4574)\]
Wrong/Invalid plans when using `RelBuilder#join` with correlations
- \[ [CALCITE-4591](https://issues.apache.org/jira/browse/CALCITE-4591)\]
`RelRunner` should throw SQLException if prepare fails
- \[ [CALCITE-4585](https://issues.apache.org/jira/browse/CALCITE-4585)\]
Improve error message from `RelRunner` (NobiGo)
- \[ [CALCITE-4586](https://issues.apache.org/jira/browse/CALCITE-4586)\]
In piglet, allow creating a `PigRelBuilder` with custom `config.simplify()`
(Jiatao Tao)
- \[ [CALCITE-4583](https://issues.apache.org/jira/browse/CALCITE-4583)\]
Control simplification in `RelBuilder#filter` with `config.simplify()` (Jiatao
Tao)
- \[ [CALCITE-4571](https://issues.apache.org/jira/browse/CALCITE-4571)\]
In piglet, a Pig Latin script with multiple `STORE` commands causes the merging
of multiple SQL statements (Mahesh Kumar Behera)
- \[ [CALCITE-4569](https://issues.apache.org/jira/browse/CALCITE-4569)\]
In piglet, allow creating a `PigConverter` with custom properties (Mahesh Kumar
Behera)
- \[ [CALCITE-4572](https://issues.apache.org/jira/browse/CALCITE-4572)\]
Piglet fails if Pig Latin script contains `RANK` or `FILTER` operators (Mahesh
Kumar Behera)
- \[ [CALCITE-4579](https://issues.apache.org/jira/browse/CALCITE-4579)\]
Piglet throws `ClassCastException` if Pig Latin script contains `FLATTEN` or
`STRSPLIT` operators (Mahesh Kumar Behera)
- \[ [CALCITE-4515](https://issues.apache.org/jira/browse/CALCITE-4515)\]
Do not generate the new join tree from commute/associate rules if there are
“always TRUE” conditions (Vladimir Ozerov)
- \[ [CALCITE-4535](https://issues.apache.org/jira/browse/CALCITE-4535)\]
`ServerDdlExecutor` cannot execute `DROP` commands with qualified object names
(Vladimir Ozerov)
- \[ [CALCITE-4511](https://issues.apache.org/jira/browse/CALCITE-4511)\]
Distinct row count and population size for constant columns should be 1
- \[ [CALCITE-4562](https://issues.apache.org/jira/browse/CALCITE-4562)\]
Improve simplification of “x IS TRUE” and “x LIKE ‘%’”
- \[ [CALCITE-4556](https://issues.apache.org/jira/browse/CALCITE-4556)\]
`CalciteMetaImpl#createEmptyResultSet` should not pass class to
`CursorFactory#deduce` (Alessandro Solimando)
- \[ [CALCITE-4522](https://issues.apache.org/jira/browse/CALCITE-4522)\]
CPU cost of `Sort` should be lower if sort keys are empty (huangqixiang)
- \[ [CALCITE-4552](https://issues.apache.org/jira/browse/CALCITE-4552)\]
`Interpreter` does not close resources held by its nodes on close
- Add method RelJsonReader.readType
- \[ [CALCITE-4524](https://issues.apache.org/jira/browse/CALCITE-4524)\]
Make some fields non-nullable (`SqlSelect.selectList`,
`DataContext.getTypeFactory`)
- \[ [CALCITE-4533](https://issues.apache.org/jira/browse/CALCITE-4533)\]
Incorrect semantics of `REPLACE` and `IF NOT EXISTS` keywords in
`CREATE TABLE/SCHEMA` commands (Vladimir Ozerov)
- \[ [CALCITE-4342](https://issues.apache.org/jira/browse/CALCITE-4342)\]
More aggregate functions should be marked as splittable and ignore distinct
optionality (Liya Fan)
- \[ [CALCITE-4526](https://issues.apache.org/jira/browse/CALCITE-4526)\]
`SqlSnapshot#unparse` loses the `AS` keyword when the table has alias (jibiyr)
- \[ [CALCITE-4276](https://issues.apache.org/jira/browse/CALCITE-4276)\]
`MaterializedViewOnlyAggregateRule` performs invalid rewrite on query that
contains join and time-rollup function (`FLOOR`) (Justin Swett)
- \[ [CALCITE-2000](https://issues.apache.org/jira/browse/CALCITE-2000)\]
`UNNEST` a collection that has a field with nested data generates an `Exception`
- \[ [CALCITE-4514](https://issues.apache.org/jira/browse/CALCITE-4514)\]
When merging `RelSets`, fine-tune which set is merged into which, for efficiency
(Botong Huang)
- \[ [CALCITE-4437](https://issues.apache.org/jira/browse/CALCITE-4437)\]
`Sort` should be decorrelated even though it has fetch or limit when it
is not inside a `Correlate` (Thomas Rebele)
- \[ [CALCITE-4265](https://issues.apache.org/jira/browse/CALCITE-4265)\]
Improve error message when `CAST` to unknown type (Louis Kuang)
- \[ [CALCITE-4494](https://issues.apache.org/jira/browse/CALCITE-4494)\]
Improve performance of checking `RelNode` presence in `RelSubset` (Igor Lozynskyi)
- In `RelBuilder`, remove not-null arguments to `COUNT`
- \[ [CALCITE-4199](https://issues.apache.org/jira/browse/CALCITE-4199)\]
`RelBuilder` throws `NullPointerException` while implementing `GROUP_ID()`
- \[ [CALCITE-4491](https://issues.apache.org/jira/browse/CALCITE-4491)\]
Aggregation of window function produces invalid SQL for Postgres (Dominik
Labuda)
- \[ [CALCITE-4426](https://issues.apache.org/jira/browse/CALCITE-4426)\]
Short-circuit evaluating when comparing two `RelTraitSets` (Jiatao Tao)
- \[ [CALCITE-4482](https://issues.apache.org/jira/browse/CALCITE-4482)\]
Extract the default `SqlWriterConfig` in `SqlPrettyWriter`, reduce the overhead of
`ImmutableBeans#create` (Jiatao Tao)
- \[ [CALCITE-4461](https://issues.apache.org/jira/browse/CALCITE-4461)\]
Do not use `Logical` nodes inside `Enumerable` rules (Vladimir Ozerov)
- \[ [CALCITE-4479](https://issues.apache.org/jira/browse/CALCITE-4479)\]
`vFloat in (1.0, 2.0)` throws `UnsupportedOperationException`
- \[ [CALCITE-4474](https://issues.apache.org/jira/browse/CALCITE-4474)\]
`SqlSimpleParser` inner Tokenizer should not recognize the sql of TokenType.ID
or some keywords in some case (wangjie)
- \[ [CALCITE-4431](https://issues.apache.org/jira/browse/CALCITE-4431)\]
Use `requireNonNull(var, "var")` instead of `requireNonNull(var)` for better error
messages
- \[ [CALCITE-4466](https://issues.apache.org/jira/browse/CALCITE-4466)\]
Do not invoke `RelTraitDef#convert` when the source trait satisfies the target
trait (Vladimir Ozerov)
- \[ [CALCITE-4463](https://issues.apache.org/jira/browse/CALCITE-4463)\]
JDBC adapter for Spark generates incorrect `ORDER BY` syntax (Yanjing Wang)
- \[ [CALCITE-4453](https://issues.apache.org/jira/browse/CALCITE-4453)\]
`RexExecutorImpl#compile` should use `RexBuilder`’s type factory if possible
- \[ [CALCITE-4450](https://issues.apache.org/jira/browse/CALCITE-4450)\]
ElasticSearch query with `VARCHAR` literal projection fails with
`JsonParseException`
- \[ [CALCITE-4449](https://issues.apache.org/jira/browse/CALCITE-4449)\]
Generate nicer SQL for Sarg `x IS NULL OR x NOT IN (1, 2)`
- \[ [CALCITE-4434](https://issues.apache.org/jira/browse/CALCITE-4434)\]
Cannot implement `CASE row WHEN row`
- \[ [CALCITE-4425](https://issues.apache.org/jira/browse/CALCITE-4425)\]
Class `DefaultEdge` lacks a proper `toString` implementation (Liya Fan)
- Change return type of `RelBuilder#literal` from `RexNode` to `RexLiteral`
- \[ [CALCITE-4435](https://issues.apache.org/jira/browse/CALCITE-4435)\]
Incorrect logic for validating `RexFieldAccess`
- \[ [CALCITE-4436](https://issues.apache.org/jira/browse/CALCITE-4436)\]
Use the fields order from the struct type for `ITEM(STRUCT, INDEX)` access
(Alessandro Solimando)
- \[ [CALCITE-4429](https://issues.apache.org/jira/browse/CALCITE-4429)\]
`RelOptUtil#createCastRel` should throw if source and target row types have
different number of fields
- \[ [CALCITE-4419](https://issues.apache.org/jira/browse/CALCITE-4419)\]
POSIX regex operators cannot be used within `RelBuilder`
- \[ [CALCITE-4411](https://issues.apache.org/jira/browse/CALCITE-4411)\]
`RelNode` to SQL loses `DISTINCT` on window aggregation (Jiatao Tao)
- \[ [CALCITE-4284](https://issues.apache.org/jira/browse/CALCITE-4284)\]
`ImmutableBeans`: make reference properties non-nullable by default
- \[ [CALCITE-4199](https://issues.apache.org/jira/browse/CALCITE-4199)\]
Add nullability annotations
- \[ [CALCITE-4199](https://issues.apache.org/jira/browse/CALCITE-4199)\]
Add package-level NonNull annotations to calcite packages
- \[ [CALCITE-4214](https://issues.apache.org/jira/browse/CALCITE-4214)\]
Make `RelDataType#getSqlTypeName` non-nullable
- \[ [CALCITE-4251](https://issues.apache.org/jira/browse/CALCITE-4251)\]
`NullPointerException` in `LoptMultiJoin` when `mq#getColumnOrigin(left, i)`
returns `null`
- \[ [CALCITE-4415](https://issues.apache.org/jira/browse/CALCITE-4415)\]
`SqlStdOperatorTable.NOT_LIKE` has a wrong implementor
- \[ [CALCITE-4317](https://issues.apache.org/jira/browse/CALCITE-4317)\]
`RelFieldTrimmer` after trimming all the fields in an aggregate should not
return a zero field Aggregate (Rafay)
- \[ [CALCITE-4414](https://issues.apache.org/jira/browse/CALCITE-4414)\]
`RelMdSelectivity#getSelectivity` for `Calc` propagates predicate with wrong
references
- \[ [CALCITE-4409](https://issues.apache.org/jira/browse/CALCITE-4409)\]
Improve exception when `RelBuilder` tries to create a field on a non-struct
expression
- \[ [CALCITE-4393](https://issues.apache.org/jira/browse/CALCITE-4393)\]
`ExceptionInInitializerError` due to `NullPointerException` in `SqlCallBinding`
caused by circular dependency
- \[ [CALCITE-4251](https://issues.apache.org/jira/browse/CALCITE-4251)\]
Support `Calc` and `SetOp` operator in `RelMdAllPredicates` (Xu Zhaohui)
- \[ [CALCITE-4402](https://issues.apache.org/jira/browse/CALCITE-4402)\]
`SqlCall#equalsDeep` does not take into account the function quantifier (Huang
Qixiang)
- \[ [CALCITE-4251](https://issues.apache.org/jira/browse/CALCITE-4251)\]
Get the origin column, even if it is derived (xzh)
- \[ [CALCITE-4406](https://issues.apache.org/jira/browse/CALCITE-4406)\]
`SqlTableRef` operator should create a `SqlTableRef` as the call
- \[ [CALCITE-4277](https://issues.apache.org/jira/browse/CALCITE-4277)\]
When `RelNode` has been removed from its subset, skip the origin rule match (Jiatao
Tao)
- \[ [CALCITE-4392](https://issues.apache.org/jira/browse/CALCITE-4392)\]
The operation of checking types equal ignoring null can be more efficient
- \[ [CALCITE-4383](https://issues.apache.org/jira/browse/CALCITE-4383)\]
In `RelBuilder`, optimize `VALUES ... UNION ALL ... VALUES` to a single `VALUES`
with multiple rows
- \[ [CALCITE-4394](https://issues.apache.org/jira/browse/CALCITE-4394)\]
When generating code for a function call, take the inferred types of the
operands into account
- \[ [CALCITE-4389](https://issues.apache.org/jira/browse/CALCITE-4389)\]
Calls to `ROW` and implicit row constructor sometimes print too many spaces
- \[ [CALCITE-4380](https://issues.apache.org/jira/browse/CALCITE-4380)\]
Make class `SqlNodeList` implement `List<SqlNode>`
- \[ [CALCITE-4390](https://issues.apache.org/jira/browse/CALCITE-4390)\]
`SqlMatchRecognize` returns wrong operand list (Dawid Wysakowicz)
- \[ [CALCITE-4364](https://issues.apache.org/jira/browse/CALCITE-4364)\]
`a IN (1, 2) AND a = 1` should be simplified to `a = 1`
- \[ [CALCITE-4273](https://issues.apache.org/jira/browse/CALCITE-4273)\]
Support get expression lineage for Calc
- \[ [CALCITE-4350](https://issues.apache.org/jira/browse/CALCITE-4350)\]
The reverse operation of collation direction is overly relaxed (Liya Fan)
- \[ [CALCITE-4345](https://issues.apache.org/jira/browse/CALCITE-4345)\]
`AggregateCaseToFilterRule` throws `NullPointerException` when converting `CASE`
without `ELSE` (Jiatao Tao)
- \[ [CALCITE-4233](https://issues.apache.org/jira/browse/CALCITE-4233)\]
In Elasticsearch adapter, support generating disjunction max (dis\_max) queries
(shlok7296)
- \[ [CALCITE-4106](https://issues.apache.org/jira/browse/CALCITE-4106)\]
Consider `listCoerced` in `TypeCoercionImpl#inOperationCoercion` (Jiatao Tao)
- \[ [CALCITE-4352](https://issues.apache.org/jira/browse/CALCITE-4352)\]
`RexSimplify` incorrectly drops `IS NULL` and `IS NOT NULL` from `SEARCH`
expressions
- BigQuery dialect should allow `GROUP BY` ordinal
- \[ [CALCITE-4332](https://issues.apache.org/jira/browse/CALCITE-4332)\]
Improve error when planning rule produces a relational expression with wrong
row type
- \[ [CALCITE-4225](https://issues.apache.org/jira/browse/CALCITE-4225)\]
Make `RelDecorrelator` pluggable
- \[ [CALCITE-4305](https://issues.apache.org/jira/browse/CALCITE-4305)\]
Implicit column alias for single-column `VALUES`, and `UNNEST` of `ARRAY` and
`MULTISET` constructors
- Add an overloaded `SqlOperator#createCall`
- \[ [CALCITE-4321](https://issues.apache.org/jira/browse/CALCITE-4321)\]
JDBC adapter omits `FILTER (WHERE ...)` expressions when generating SQL
(Jeremiah Rhoads Hall)
- \[ [CALCITE-4325](https://issues.apache.org/jira/browse/CALCITE-4325)\]
`RexSimplify` incorrectly simplifies complex expressions that contain Sarg and
`IS NULL`
- \[ [CALCITE-4240](https://issues.apache.org/jira/browse/CALCITE-4240)\]
`SqlTypeUtil#getMaxPrecisionScaleDecimal` returns a decimal with same
precision and scale (Jiatao Tao)
- \[ [CALCITE-4333](https://issues.apache.org/jira/browse/CALCITE-4333)\]
`Sort` rel should be decorrelated even though it has fetch or limit when its
parent is not a `Correlate`
- \[ [CALCITE-4302](https://issues.apache.org/jira/browse/CALCITE-4302)\]
Avoid cost re-propagation in `VolcanoPlanner` (Botong Huang)
- \[ [CALCITE-4324](https://issues.apache.org/jira/browse/CALCITE-4324)\]
Avoid sqlline classpath caching by default, add sqlline and sqlsh tests
- \[ [CALCITE-4315](https://issues.apache.org/jira/browse/CALCITE-4315)\]
`NPE` in `RelMdUtil#checkInputForCollationAndLimit`
- \[ [CALCITE-4316](https://issues.apache.org/jira/browse/CALCITE-4316)\]
`NPE` when division includes nulls
- Add method RelBuilder.isDistinctFrom()
- Add class SqlBasicAggFunction
- Add generic info to `Map` & `Array` annotation
- Refactor: Add method SqlOperator.reverse()
- Refactor: Make HintStrategyTable immutable
- Refactor: move CassandraRules.reverseDirection into Direction
- Remove the insecure, unused `TrustAllSslSocketFactory` class (intrigus-lgtm)
- Remove multiple blank lines after package statements
- Remove multiple blank lines after import statements
- Cleanup code after errorprone upgrade: `IdentityHashMapUsage`, `JdkObsolete`
→ `JavaUtilDate`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-27-0 "Permalink")

- \[ [CALCITE-4613](https://issues.apache.org/jira/browse/CALCITE-4613)\]
OWASP dependency-check tasks fail due to missing resources
- \[ [CALCITE-4576](https://issues.apache.org/jira/browse/CALCITE-4576)\]
Release process should not overwrite LICENSE file
- \[ [CALCITE-4575](https://issues.apache.org/jira/browse/CALCITE-4575)\]
Remove Gradle wrapper from source distribution
- Remove `System.out.println` from `DiffRepository`
- `DiffRepository` should write a test’s resource file only when it is modified
- \[ [CALCITE-4593](https://issues.apache.org/jira/browse/CALCITE-4593)\]
`DiffRepository` tests should fail if new XML resources are not in alphabetical
order
- \[ [CALCITE-4587](https://issues.apache.org/jira/browse/CALCITE-4587)\]
Set `spark.driver.bindAddress` explicitly to avoid `BindException` thrown by
Spark (Jiatao Tao)
- Add Matcher#matches to ForbiddenApis to avoid its accidental use
- Apply com.autonomousapps.dependency-analysis plugin only when
  -PenableDependencyAnalysis is provided on a command line
- Fuzz testing for SEARCH operator, and refactor RexSimplify
- \[ [CALCITE-4344](https://issues.apache.org/jira/browse/CALCITE-4344)\]
Run `Redis` tests using Docker containers
- Make sure FmppTask re-executes in case default\_config.fmpp changes
- Use max-parallel=3 to reduce the usage of the shared GitHub Actions executors
- \[ [CALCITE-4140](https://issues.apache.org/jira/browse/CALCITE-4140)\]
Use Wasabi S3 for remote build cache
- Use Sonatype OSSRH repository instead of JCenter in build plugins
- \[ [CALCITE-4459](https://issues.apache.org/jira/browse/CALCITE-4459)\]
Verify the bytecode with Jandex by default
- \[ [CALCITE-4470](https://issues.apache.org/jira/browse/CALCITE-4470)\]
Add optional bytecode verification with Jandex
- Cancel stale workflows in GitHub Actions CI
- Add ErrorProne and the Checker Framework verifications to Travis CI
- Test case for \[ [CALCITE-1382](https://issues.apache.org/jira/browse/CALCITE-1382)\]
`ClassCastException` in JDBC Adapter
- Require Java 1.8.0u202 or later for the build
- Make sure compileJava is re-executed in case of the minor javac version changes
- \[ [CALCITE-4422](https://issues.apache.org/jira/browse/CALCITE-4422)\]
Add `MethodCanBeStatic` check via ErrorProne
- \[ [CALCITE-4199](https://issues.apache.org/jira/browse/CALCITE-4199)\]
Add CheckerFramework to GitHub Actions CI
- Add OpenJ9 1.8 CI job at GitHub Actions
- Add markdown to .gitattributes
- Set diff pattern for CSS files in .gitattributes
- Remove files that change often from Travis cache, remove broken files
automatically
- Make buildSrc jars reproducible for better caching
- Refactor `SqlToRelTestBase` to allow custom `Context` in tests
- Exclude root project from javadoc aggregate tasks
- \[ [CALCITE-4301](https://issues.apache.org/jira/browse/CALCITE-4301)\]
Unit test `testCollectionsInnerValues()` for Cassandra adapter is wrong
(Alessandro Solimando)
- Refactor `ResultSetEnumerable` to avoid nested lambdas
- \[ [CALCITE-4314](https://issues.apache.org/jira/browse/CALCITE-4314)\]
Enable ErrorProne checking and resolve identified problems

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-27-0 "Permalink")

- Bump commons-codec from 1.12 to 1.13 (Jaromir Hamala)
- \[ [CALCITE-4528](https://issues.apache.org/jira/browse/CALCITE-4528)\]
Upgrade Avatica version to 1.18.0
- Bump Gradle 6.8.1 -> 6.8.3
- Update dependency declarations: adjust api vs implementation, remove unused
ones
- \[ [CALCITE-4506](https://issues.apache.org/jira/browse/CALCITE-4506)\]
Upgrade SQLLine to 1.11.0
- Bump checkerframework 3.9.1 -> 3.10.0, errorprone 2.4.0 -> 2.5.1
- Bump checkerframework 3.7 -> 3.9.1
- Bump Gradle 6.7 -> 6.8.1
- Bump AppVeyor image from 2017 to 2019 to test with newer Java: 1.8u162 ->
1.8u221, 13 -> 15
- Bump de.thetaphi.forbiddenapis from 2.7 to 3.1
- \[ [CALCITE-4343](https://issues.apache.org/jira/browse/CALCITE-4343)\]
Bump Jedis from 2.9.0 to 3.3.0 (Tugdual Grall)
- \[ [CALCITE-4339](https://issues.apache.org/jira/browse/CALCITE-4339)\]
Update Gradle: 6.6 -> 6.7
- Use jackson-bom to specify Jackson versions

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-27-0 "Permalink")

- \[ [CALCITE-4625](https://issues.apache.org/jira/browse/CALCITE-4625)\]
Update version in NOTICE, README, and howto.md
- \[ [CALCITE-4601](https://issues.apache.org/jira/browse/CALCITE-4601)\]
Invalid Javadoc URL in `SchemaFactory` of CSV adapter
- Update release instructions

## [1.26.0](https://github.com/apache/calcite/releases/tag/calcite-1.26.0) / 2020-10-06 [Permalink](https://calcite.apache.org/docs/history.html\#v1-26-0 "Permalink")

This release comes about two months after [1.25.0](https://calcite.apache.org/docs/history.html#v1-25-0). It includes more than 70 resolved
issues, comprising a lot of new features and bug-fixes. Among others, it is worth highlighting the following.

- [SEARCH operator and Sarg literal](https://issues.apache.org/jira/browse/CALCITE-4173)
- [PIVOT operator in SQL](https://issues.apache.org/jira/browse/CALCITE-3752)
- [Spatial index based on Hilbert space-filling curve](https://issues.apache.org/jira/browse/CALCITE-1861)
- [Provide utility to visualize RelNode](https://issues.apache.org/jira/browse/CALCITE-4197)
- [Support JDK 15 and Guava version 29.0-jre](https://issues.apache.org/jira/browse/CALCITE-4259)

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using JDK/OpenJDK versions 8 to 15;
Guava versions 19.0 to 29.0-jre;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-26-0 "Permalink")

- \[ [CALCITE-2082](https://issues.apache.org/jira/browse/CALCITE-2082)\]
Do not store types or type factories inside operators

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-26-0 "Permalink")

- \[ [CALCITE-4173](https://issues.apache.org/jira/browse/CALCITE-4173)\]
Add internal `SEARCH` operator and `Sarg` literal that represents a set of values or ranges
- \[ [CALCITE-3752](https://issues.apache.org/jira/browse/CALCITE-3752)\]
Add `PIVOT` operator to SQL
- \[ [CALCITE-1861](https://issues.apache.org/jira/browse/CALCITE-1861)\]
Spatial index, based on Hilbert space-filling curve
- \[ [CALCITE-3920](https://issues.apache.org/jira/browse/CALCITE-3920)\]
Improve `ORDER BY` computation in Enumerable convention by exploiting `LIMIT` (Thomas Rebele)
- \[ [CALCITE-4015](https://issues.apache.org/jira/browse/CALCITE-4015)\]
Pass through parent collation request on subset or superset of join keys for `EnumerableMergeJoin`
- \[ [CALCITE-3782](https://issues.apache.org/jira/browse/CALCITE-3782)\]
Bitwise functions `BIT_AND`, `BIT_OR` and `BIT_XOR` support binary and varbinary type (Hailong Wang)
- \[ [CALCITE-4197](https://issues.apache.org/jira/browse/CALCITE-4197)\]
Provide utility to visualize `RelNode` plans (Liya Fan)
- \[ [CALCITE-4113](https://issues.apache.org/jira/browse/CALCITE-4113)\]
Support `LEFT JOIN` in `EnumerableMergeJoin`

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-26-0 "Permalink")

- \[ [CALCITE-2833](https://issues.apache.org/jira/browse/CALCITE-2833)\]
In JDBC adapter for Hive and BigQuery, implement `Values` by generating `SELECT` without `FROM` (Stuti Gupta)
- \[ [CALCITE-4160](https://issues.apache.org/jira/browse/CALCITE-4160)\]
Add configuration (`SqlToRelConverter.Config`) to retain `ORDER BY` in sub-query (Jiatao Tao)
- \[ [CALCITE-3399](https://issues.apache.org/jira/browse/CALCITE-3399)\]
Field-pruning for set operators (except `UNION ALL`) changes query semantics (Jin Xing)
- \[ [CALCITE-4182](https://issues.apache.org/jira/browse/CALCITE-4182)\]
Support materialized view recognition when query has constant filter for missing columns in `GROUP BY` list of materialized view (Wang Yanlin)
- \[ [CALCITE-4171](https://issues.apache.org/jira/browse/CALCITE-4171)\]
Support named parameters for table window functions
- \[ [CALCITE-4167](https://issues.apache.org/jira/browse/CALCITE-4167)\]
Group by `COALESCE IN` throws `NullPointerException`
- \[ [CALCITE-4172](https://issues.apache.org/jira/browse/CALCITE-4172)\]
Expand columnar identifiers before resolving (James Starr)
- \[ [CALCITE-4180](https://issues.apache.org/jira/browse/CALCITE-4180)\]
Support for Elasticsearch basic authentication (fageiguanbing)
- \[ [CALCITE-4241](https://issues.apache.org/jira/browse/CALCITE-4241)\]
Some improvements to metadata query
- \[ [CALCITE-4170](https://issues.apache.org/jira/browse/CALCITE-4170)\]
Improve simplification of `<>` predicates
- \[ [CALCITE-4159](https://issues.apache.org/jira/browse/CALCITE-4159)\]
Simplify always-true expressions (such as `LIKE '%'`) to `TRUE`
- \[ [CALCITE-4192](https://issues.apache.org/jira/browse/CALCITE-4192)\]
`RelMdColumnOrigins` gets the wrong index of group by columns after `RelNode` was optimized by `AggregateProjectMergeRule` rule (FangZheng Li)
- \[ [CALCITE-4203](https://issues.apache.org/jira/browse/CALCITE-4203)\]
`RelMdUniqueKeys` should not return empty when meeting `Intersect` and `Minus` if its input has unique keys
- \[ [CALCITE-4207](https://issues.apache.org/jira/browse/CALCITE-4207)\]
Validation fails for positional aggregate with `CURRENT_DATE` in `CASE` expression
- \[ [CALCITE-4206](https://issues.apache.org/jira/browse/CALCITE-4206)\]
`RelDecorrelator` outputs wrong plan for correlate sort with fetch limit
- \[ [CALCITE-4209](https://issues.apache.org/jira/browse/CALCITE-4209)\]
In `RelBuilder`, add an option to not simplify `LIMIT 0` to an empty relation
- \[ [CALCITE-4208](https://issues.apache.org/jira/browse/CALCITE-4208)\]
Improve metadata row count for `Join`
- \[ [CALCITE-4210](https://issues.apache.org/jira/browse/CALCITE-4210)\]
Replaying subqueries in `ON` clauses (James Starr)
- \[ [CALCITE-4214](https://issues.apache.org/jira/browse/CALCITE-4214)\]
Make `RelDataType.getSqlTypeName` non-nullable
- \[ [CALCITE-4217](https://issues.apache.org/jira/browse/CALCITE-4217)\]
Unlock `RelCrossType#getFieldCount()`
- \[ [CALCITE-4220](https://issues.apache.org/jira/browse/CALCITE-4220)\]
In `SqlToRelConverter`, use `RelBuilder` for creating `Aggregate`
- \[ [CALCITE-4226](https://issues.apache.org/jira/browse/CALCITE-4226)\]
Add `Mappings#asListNonNull` as a null-safe alternative for `Mappings#asList`
- \[ [CALCITE-4237](https://issues.apache.org/jira/browse/CALCITE-4237)\]
`AssertionError` in `SqlTypeFactoryImpl.leastRestrictive` when running slow tests
- \[ [CALCITE-4254](https://issues.apache.org/jira/browse/CALCITE-4254)\]
`ImmutableBeans` should make an immutable copy of property values of type `List`, `Set`, or `Map`
- \[ [CALCITE-4249](https://issues.apache.org/jira/browse/CALCITE-4249)\]
JDBC adapter cannot translate `NOT LIKE` in join condition
- \[ [CALCITE-4266](https://issues.apache.org/jira/browse/CALCITE-4266)\]
JDBC adapter throws `UnsupportedOperationException` if query contains range predicate on columns from sub-query
- \[ [CALCITE-4176](https://issues.apache.org/jira/browse/CALCITE-4176)\]
Key descriptor can be optional in `SESSION` table function
- \[ [CALCITE-4279](https://issues.apache.org/jira/browse/CALCITE-4279)\]
`SEARCH` operator cannot be pushed into Druid
- \[ [CALCITE-4280](https://issues.apache.org/jira/browse/CALCITE-4280)\]
Replace Guava’s `Lists.transform` and `Iterables.transform` with `Util.transform`
- \[ [CALCITE-4282](https://issues.apache.org/jira/browse/CALCITE-4282)\]
Promote the window table functions window attribute data type with precision 3
- \[ [CALCITE-4287](https://issues.apache.org/jira/browse/CALCITE-4287)\]
`AggregateJoinRemoveRule` and `ProjectJoinRemoveRule` are not fired if the last column of the join’s left input is referenced (Liya Fan)
- \[ [CALCITE-4238](https://issues.apache.org/jira/browse/CALCITE-4238)\]
Create a default parser configuration, to reduce redundant information in sub-parsers
- \[ [CALCITE-4289](https://issues.apache.org/jira/browse/CALCITE-4289)\]
Wrong signature for `SqlTumbleTableFunction`
- \[ [CALCITE-4295](https://issues.apache.org/jira/browse/CALCITE-4295)\]
Composite of two checkers with `SqlOperandCountRange` throws `IllegalArgumentException` (Zhenghua Gao)
- \[ [CALCITE-4190](https://issues.apache.org/jira/browse/CALCITE-4190)\]
`OR` simplification incorrectly loses term
- \[ [CALCITE-4195](https://issues.apache.org/jira/browse/CALCITE-4195)\]
Cast between types with different collators must be evaluated as not monotonic
- \[ [CALCITE-4200](https://issues.apache.org/jira/browse/CALCITE-4200)\]
`ExceptionInInitializerError` when initializing DruidRules
- \[ [CALCITE-4201](https://issues.apache.org/jira/browse/CALCITE-4201)\]
`AssertionError` when registering Druid rules due to conflict in description
- \[ [CALCITE-4221](https://issues.apache.org/jira/browse/CALCITE-4221)\]
Update stale integration tests in Druid adapter
- \[ [CALCITE-4239](https://issues.apache.org/jira/browse/CALCITE-4239)\]
`RelMdUniqueKeys` returns wrong unique keys for `Aggregate` with grouping sets
- \[ [CALCITE-4271](https://issues.apache.org/jira/browse/CALCITE-4271)\]
`RelBuilder.in` should allow duplicate values
- \[ [CALCITE-4258](https://issues.apache.org/jira/browse/CALCITE-4258)\]
`SqlToRelConverter`: `SELECT 1 IS DISTINCT FROM NULL` fails with `AssertionError`
- \[ [CALCITE-4246](https://issues.apache.org/jira/browse/CALCITE-4246)\]
When parsing SQL in BigQuery dialect, allow unquoted table names to contain hyphens
- \[ [CALCITE-4230](https://issues.apache.org/jira/browse/CALCITE-4230)\]
When parsing SQL in BigQuery dialect, split quoted table names that contain dots
- \[ [CALCITE-4247](https://issues.apache.org/jira/browse/CALCITE-4247)\]
When parsing SQL in BigQuery dialect, character literals may be enclosed in single- or double-quotes, and use backslashes as escapes
- \[ [CALCITE-4215](https://issues.apache.org/jira/browse/CALCITE-4215)\]
Ensure `org.apache.calcite.schema.Statistic` uses `null` vs `emptyList` appropriately
- \[ [CALCITE-4227](https://issues.apache.org/jira/browse/CALCITE-4227)\]
`ImmutableIntList#toArray(Integer[])` should support arguments larger than the collection itself
- \[ [CALCITE-4228](https://issues.apache.org/jira/browse/CALCITE-4228)\]
`FlatLists.Flat6List#append` should not throw NPE if there are null elements in the list
- \[ [CALCITE-4229](https://issues.apache.org/jira/browse/CALCITE-4229)\]
`Add Util.throwAsRuntime` and `Util.causeOrSelf` to simplify exception re-throwing
- \[ [CALCITE-4269](https://issues.apache.org/jira/browse/CALCITE-4269)\]
Improvement on enumerable implementation for `HOP` and `SESSION`
- \[ [CALCITE-4275](https://issues.apache.org/jira/browse/CALCITE-4275)\]
`EnumerableMergeJoin#create` does not set `EnumerableConvention` in the trait set
- \[ [CALCITE-4283](https://issues.apache.org/jira/browse/CALCITE-4283)\]
Do not force implement `SqlTableFunction` when creating table function scan
- \[ [CALCITE-4261](https://issues.apache.org/jira/browse/CALCITE-4261)\]
Join with three tables causes `IllegalArgumentException` in `EnumerableBatchNestedLoopJoinRule`
- \[ [CALCITE-4288](https://issues.apache.org/jira/browse/CALCITE-4288)\]
Create `SqlTypeUtil#deriveType(SqlCallBinding)` to make type computation simpler
- \[ [CALCITE-4216](https://issues.apache.org/jira/browse/CALCITE-4216)\]
Make `org.apache.calcite.rel.type.RelDataType#getFamily` non-nullable
- \[ [CALCITE-4298](https://issues.apache.org/jira/browse/CALCITE-4298)\]
Avoid disabling hostname verification on HTTPS connections
- \[ [CALCITE-4300](https://issues.apache.org/jira/browse/CALCITE-4300)\]
`EnumerableBatchNestedLoopJoin` dynamic code generation can lead to variable name issues if two EBNLJ are nested
- \[ [CALCITE-4224](https://issues.apache.org/jira/browse/CALCITE-4224)\]
Add a method for `RelNode` to output its relational expression string (Jiatao Tao)
- \[ [CALCITE-4248](https://issues.apache.org/jira/browse/CALCITE-4248)\]
Deprecate `SqlParser.ConfigBuilder`
- Remove `ArrayList` allocation from `Mappings#bijection`, and add helpful message in case NPE is thrown
- Improve positions in SQL validator error messages
- Simplify `Pair.left(Iterable)` and `Pair.right(Iterable)` implementation
- Refactor `Pair` comparison to use `Comparator.nullsFirst` and `.naturalOrder`
- Obsolete `SqlToRelConverter.ConfigBuilder`, and refactor `SqlToRelConverterTest`
- Refactor `SqlParserTest`
- Minor refactoring of `DruidAdapterIT` and `DruidAdapter2IT`

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-26-0 "Permalink")

- \[ [CALCITE-4278](https://issues.apache.org/jira/browse/CALCITE-4278)\]
Add Druid adapter tests in GitHub CI
- \[ [CALCITE-4259](https://issues.apache.org/jira/browse/CALCITE-4259)\]
Support JDK 15 and Guava version 29.0-jre
- \[ [CALCITE-4184](https://issues.apache.org/jira/browse/CALCITE-4184)\]
Update Gradle: 6.3 -> 6.6
- \[ [CALCITE-4168](https://issues.apache.org/jira/browse/CALCITE-4168)\]
Configure Gradle Local Build Cache
- \[ [CALCITE-4185](https://issues.apache.org/jira/browse/CALCITE-4185)\]
Remove dependency between checkstyle and compilation tasks
- Add `MaxMetaspaceSize=512m` to avoid metaspace issues when building Calcite
- Make project buildable from folders that include special characters
- Use `merge=union` strategy to avoid false merge conflicts on `CalciteResource.properties`
- Add GC options to GitHub and Travis CI so they fail on low memory condition faster
- Update Checkstyle from 8.27 to 8.28 to support `package-info` files with imports
- Update `org.nosphere.apache.rat` plugin from 0.5.2 to 0.7.0, and print files with unapproved licenses to console

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-26-0 "Permalink")

- \[ [CALCITE-3841](https://issues.apache.org/jira/browse/CALCITE-3841)\]
Change downloads page to use downloads.apache.org
- Fix documentation errors
- Site: Add Rui Wang as committer, Ruben Quesada Lopez as PMC

## [1.25.0](https://github.com/apache/calcite/releases/tag/calcite-1.25.0) / 2020-08-22 [Permalink](https://calcite.apache.org/docs/history.html\#v1-25-0 "Permalink")

This release comes shortly after [1.24.0](https://calcite.apache.org/docs/history.html#v1-24-0) and removes methods
which were deprecated in the previous version. It also introduces other breaking changes so
make sure to consult corresponding section. Notable improvements in this release are:

- [Interval Expressions](https://issues.apache.org/jira/browse/CALCITE-4134)
(e.g. `INTERVAL '1' HOUR`, `INTERVAL -'1:2' HOUR TO MINUTE`)
- [Character Literals as Aliases](https://issues.apache.org/jira/browse/CALCITE-4080)
- [Refactor How Planner Rules are Parameterized](https://issues.apache.org/jira/browse/CALCITE-3923)
- [Spacial Functions](https://issues.apache.org/jira/browse/CALCITE-2160)

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13, 14 and OpenJDK 8, 9, 10, 11, 12, 13, 14;
Guava versions 19.0 to 28.2-jre; other software versions as specified in
gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-25-0 "Permalink")

- \[ [CALCITE-2569](https://issues.apache.org/jira/browse/CALCITE-2569)\]
UDFs that are table functions must implement `SqlTableFunction` and have `CURSOR` as their return type
- \[ [CALCITE-3923](https://issues.apache.org/jira/browse/CALCITE-3923)\]
Refactor how planner rules are parameterized
- \[ [CALCITE-4079](https://issues.apache.org/jira/browse/CALCITE-4079)\]
Dialect constants in `SqlDialect` can cause class initialization deadlock
- \[ [CALCITE-4128](https://issues.apache.org/jira/browse/CALCITE-4128)\]
Remove dependency of File adapter on Example CSV adapter

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-25-0 "Permalink")

- \[ [CALCITE-2160](https://issues.apache.org/jira/browse/CALCITE-2160)\]
Spatial: Add functions `ST_MakeGrid` and `ST_MakeGridPoints`
- \[ [CALCITE-4134](https://issues.apache.org/jira/browse/CALCITE-4134)\]
Interval expressions
- \[ [CALCITE-4154](https://issues.apache.org/jira/browse/CALCITE-4154)\]
Add a rule, `ProjectAggregateMergeRule`, to merge a `Project` onto an `Aggregate`
- \[ [CALCITE-4080](https://issues.apache.org/jira/browse/CALCITE-4080)\]
Allow character literals as column aliases, if `SqlConformance.allowCharLiteralAlias()`

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-25-0 "Permalink")

- \[ [CALCITE-4139](https://issues.apache.org/jira/browse/CALCITE-4139)\]
Prevent NPE in `ListTransientTable`
- \[ [CALCITE-2854](https://issues.apache.org/jira/browse/CALCITE-2854)\]
Codegen compile error when implementing unary minus function with data type `BigDecimal` (Qi Yu)
- \[ [CALCITE-3957](https://issues.apache.org/jira/browse/CALCITE-3957)\]
`AggregateMergeRule` should merge `SUM0` into `COUNT` even if `GROUP BY` is empty
- \[ [CALCITE-4150](https://issues.apache.org/jira/browse/CALCITE-4150)\]
JDBC adapter throws `UnsupportedOperationException` when generating SQL for untyped `NULL` literal (Anton Haidai)
- \[ [CALCITE-4118](https://issues.apache.org/jira/browse/CALCITE-4118)\]
RexSimplify might remove `CAST` from RexNode incorrectly
- \[ [CALCITE-4145](https://issues.apache.org/jira/browse/CALCITE-4145)\]
Exception when query from UDF field with structured type
- \[ [CALCITE-4081](https://issues.apache.org/jira/browse/CALCITE-4081)\]
Round-tripping a DECIMAL literal throws validation error
- \[ [CALCITE-4132](https://issues.apache.org/jira/browse/CALCITE-4132)\]
Estimate the number of distinct values more accurately (Liya Fan)
- \[ [CALCITE-4102](https://issues.apache.org/jira/browse/CALCITE-4102)\]
Some improvements to aggregate related operations (Liya Fan)

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-25-0 "Permalink")

- \[ [CALCITE-4141](https://issues.apache.org/jira/browse/CALCITE-4141)\]
Make checkstyle tasks relocatable to support Gradle build cache
- \[ [CALCITE-4137](https://issues.apache.org/jira/browse/CALCITE-4137)\]
Checkstyle should ensure that every class has a Javadoc comment
- \[ [CALCITE-4156](https://issues.apache.org/jira/browse/CALCITE-4156)\]
`ReflectiveRelMetadataProvider` constructor should throw an exception (instead of assertion) when called with an empty map
- \[ [CALCITE-4022](https://issues.apache.org/jira/browse/CALCITE-4022)\]
Support unparse special syntax for `INSERT` (Xu Zhaohui)
- \[ [CALCITE-4115](https://issues.apache.org/jira/browse/CALCITE-4115)\]
Improve the prompt of using SQL keywords for sql parses (part2)
- \[ [CALCITE-4129](https://issues.apache.org/jira/browse/CALCITE-4129)\]
Support deep equality check for `RelNode`
- \[ [CALCITE-4111](https://issues.apache.org/jira/browse/CALCITE-4111)\]
Remove `VolcanoPlannerPhase` in Planner (Jiatao Tao)
- \[ [CALCITE-4114](https://issues.apache.org/jira/browse/CALCITE-4114)\]
Remove method `CalciteAssert.forceDecorrelate` (Jiatao Tao)

## [1.24.0](https://github.com/apache/calcite/releases/tag/calcite-1.24.0) / 2020-07-24 [Permalink](https://calcite.apache.org/docs/history.html\#v1-24-0 "Permalink")

This release comes about two months after 1.23.0. It includes more than 80 resolved
issues, comprising a lot of new features as well as performance improvements
and bug-fixes. Among others, it is worth highlighting the following.

- Support [top-down rule applying and upper bound space pruning](https://issues.apache.org/jira/browse/CALCITE-3916)
- Support [OFFSET](https://issues.apache.org/jira/browse/CALCITE-4000) parameter in `TUMBLE/HOP`
table functions
- A new [Presto dialect implementation](https://issues.apache.org/jira/browse/CALCITE-3724)
- [Hoist](https://issues.apache.org/jira/browse/CALCITE-4087), a utility to replace literals in a
SQL string with placeholders

In this release, quite a few instance variables are deprecated and will be
removed before 1.25, such as `EnumerableToBindableConverterRule.INSTANCE`,
`CassandraToEnumerableConverterRule.INSTANCE` and so on. Besides, some methods
in `RelNode` are changed from ‘to removed before 2.0’ to ‘to be removed before 1.25’,
including `isDistinct()`, `isKey(ImmutableBitSet)`, `getQuery()`, `getRows()`,
`getVariablesStopped()`, `computeSelfCost()`, `isValid(boolean)`, `getCollationList()`,
`getChildExps()`. All deprecated APIs are strongly recommended to be replaced by their
replacements as soon as possible( [CALCITE-3923](https://issues.apache.org/jira/browse/CALCITE-3896),
[CALCITE-4079](https://issues.apache.org/jira/browse/CALCITE-3896)).

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13, 14 and OpenJDK 8, 9, 10, 11, 12, 13, 14;
Guava versions 19.0 to 28.2-jre; other software versions as specified in
gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-24-0 "Permalink")

- \[ [CALCITE-4032](https://issues.apache.org/jira/browse/CALCITE-4032)\]
Mark `CalcMergeRule` as `TransformationRule`. With this change, the `CalcMergeRule`
won’t match `PhysicalNode`(including `EnumerableCalc`) in `VolcanoPlanner`
- \[ [CALCITE-4003](https://issues.apache.org/jira/browse/CALCITE-4003)\]
Disallow cross convention matching and `PhysicalNode` generation in `TransformationRule`
- \[ [CALCITE-3786](https://issues.apache.org/jira/browse/CALCITE-3786)\]
Change `RelNode#recomputeDigest()` return type from `String` to `void`

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-24-0 "Permalink")

- \[ [CALCITE-4000](https://issues.apache.org/jira/browse/CALCITE-4000)\]
Support `OFFSET` parameter in `TUMBLE/HOP` table functions (Rui Wang)
- \[ [CALCITE-3916](https://issues.apache.org/jira/browse/CALCITE-3916)\]
Support top-down rule applying and upper bound space pruning
- \[ [CALCITE-3941](https://issues.apache.org/jira/browse/CALCITE-3941)\]
Add the default strict mode to the path in the Json functions
- \[ [CALCITE-3724](https://issues.apache.org/jira/browse/CALCITE-3724)\]
Presto dialect implementation
- \[ [CALCITE-3946](https://issues.apache.org/jira/browse/CALCITE-3946)\]
Add parser support for `MULTISET/SET` and `VOLATILE` modifiers in `CREATE TABLE` statements (Drew Schmitt)
- \[ [CALCITE-4089](https://issues.apache.org/jira/browse/CALCITE-4089)\]
In Babel, allow `CAST(integer AS DATE)` even though it is illegal in Calcite SQL
- \[ [CALCITE-4087](https://issues.apache.org/jira/browse/CALCITE-4087)\]
`Hoist`, a utility to replace literals in a SQL string with placeholders

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-24-0 "Permalink")

- \[ [CALCITE-4073](https://issues.apache.org/jira/browse/CALCITE-4073)\]
Add a new component `RexNormalize` for more effect rex nodes normalization
- \[ [CALCITE-3224](https://issues.apache.org/jira/browse/CALCITE-3224)\]
New implementation of `RexNode-to-Expression` code generation
- \[ [CALCITE-4056](https://issues.apache.org/jira/browse/CALCITE-4056)\]
Remove `Digest` from `RelNode` and `RexCall`
- \[ [CALCITE-4008](https://issues.apache.org/jira/browse/CALCITE-4008)\]
Implement Code generation for `EnumerableSortedAggregate` (Rui Wang)
- \[ [CALCITE-3972](https://issues.apache.org/jira/browse/CALCITE-3972)\]
Allow `RelBuilder` to create `RelNode` with convention (Xiening Dai)
- \[ [CALCITE-4060](https://issues.apache.org/jira/browse/CALCITE-4060)\]
Supports implicit type coercion for `NOT IN`
- \[ [CALCITE-4127](https://issues.apache.org/jira/browse/CALCITE-4127)\]
Remove final from `AbstractRelNode#getRelTypeName`
- \[ [CALCITE-4124](https://issues.apache.org/jira/browse/CALCITE-4124)\]
Stop invalidating metadata cache in `VolcanoRuleCall`
- \[ [CALCITE-4123](https://issues.apache.org/jira/browse/CALCITE-4123)\]
Make `EnumerableMergeJoin` constructor protected
- \[ [CALCITE-4085](https://issues.apache.org/jira/browse/CALCITE-4085)\]
Improve return type nullability for `SqlDotOperator` & `SqlItemOperator` (Dawid Wysakowicz)
- \[ [CALCITE-3936](https://issues.apache.org/jira/browse/CALCITE-3936)\]
JDBC adapter, when generating SQL, changes target of ambiguous `HAVING` clause with a `Project` on `Filter` on `Aggregate`
- \[ [CALCITE-4112](https://issues.apache.org/jira/browse/CALCITE-4112)\]
Refine the usage of `CalciteConnectionConfig` in `DecorrelateProgram` & some minor code refactoring (Jiatao Tao)
- \[ [CALCITE-4116](https://issues.apache.org/jira/browse/CALCITE-4116)\]
Remove unused code for tracking `RexNode`’s nullable state in codegen
- \[ [CALCITE-4105](https://issues.apache.org/jira/browse/CALCITE-4105)\]
Replace `Pair` with `Flat2List` in `RelDigestWriter`
- \[ [CALCITE-4092](https://issues.apache.org/jira/browse/CALCITE-4092)\]
`NPE` using `WITH` clause without a corresponding `SELECT FROM` (James Kim)
- \[ [CALCITE-4115](https://issues.apache.org/jira/browse/CALCITE-4115)\]
Improve the prompt of using SQL keywords for sql parser
- \[ [CALCITE-4094](https://issues.apache.org/jira/browse/CALCITE-4094)\]
Allow `SqlOperator` of `SqlKind#OTHER_FUNCTION` to define a `Strong.Policy`
- \[ [CALCITE-3834](https://issues.apache.org/jira/browse/CALCITE-3834)\]
Support `AntiJoin` in `EnumerableMergeJoin`
- \[ [CALCITE-4098](https://issues.apache.org/jira/browse/CALCITE-4098)\]
Remove redundant code in `RelJson.toJson(RelDistribution)` (Jiatao Tao)
- \[ [CALCITE-4066](https://issues.apache.org/jira/browse/CALCITE-4066)\]
`SqlTypeUtil#convertTypeToSpec` cover `Array/Multiset/Row` types (Jiatao Tao)
- \[ [CALCITE-4059](https://issues.apache.org/jira/browse/CALCITE-4059)\]
`SqlTypeUtil#equalSansNullability` consider `Array/Map` type (Jiatao Tao)
- \[ [CALCITE-4026](https://issues.apache.org/jira/browse/CALCITE-4026)\]
`CassandraFilter` has generated wrong condition expression for filter with non string literal (Wenhui Tang)
- \[ [CALCITE-4077](https://issues.apache.org/jira/browse/CALCITE-4077)\]
Exception when joined with built-in table functions
- \[ [CALCITE-4097](https://issues.apache.org/jira/browse/CALCITE-4097)\]
Avoid requesting unnecessary trait request when deriving traits
- \[ [CALCITE-4033](https://issues.apache.org/jira/browse/CALCITE-4033)\]
Does not produce parenthesized table expressions for `UNNEST` (Rui Wang)
- \[ [CALCITE-4049](https://issues.apache.org/jira/browse/CALCITE-4049)\]
Improve the implementation of the shortest-path algorithm
- \[ [CALCITE-3929](https://issues.apache.org/jira/browse/CALCITE-3929)\]
When deserialize UDAF aggregate call from json string, throws `NPE` (Xu Zhaohui)
- \[ [CALCITE-4062](https://issues.apache.org/jira/browse/CALCITE-4062)\]
Support deserialize UDF array type from json string (Xu Zhaohui)
- \[ [CALCITE-4090](https://issues.apache.org/jira/browse/CALCITE-4090)\]
When generating SQL for DB2, a complex `SELECT` above a sub-query generates a bad table alias (Steven Talbot)
- \[ [CALCITE-4083](https://issues.apache.org/jira/browse/CALCITE-4083)\]
`RelTraitSet` failed to canonize traits
- \[ [CALCITE-4019](https://issues.apache.org/jira/browse/CALCITE-4019)\]
Visit `SqlInsert` with `SqlShuttle` cause `NullPointerException` (Xu ZhaoHui)
- \[ [CALCITE-4063](https://issues.apache.org/jira/browse/CALCITE-4063)\]
Unnest an array of single-item structs causes `ClassCastException`
- \[ [CALCITE-3907](https://issues.apache.org/jira/browse/CALCITE-3907)\]
Use username and password parameters on delegation
- \[ [CALCITE-3951](https://issues.apache.org/jira/browse/CALCITE-3951)\]
Support different string comparison based on `SqlCollation`
- \[ [CALCITE-4020](https://issues.apache.org/jira/browse/CALCITE-4020)\]
Support `Calc` operator in `RelFieldTrimmer` (Xu Zhaohui)
- \[ [CALCITE-4057](https://issues.apache.org/jira/browse/CALCITE-4057)\]
Support trait propagation for `EnumerableBatchNestedLoopJoin` (Rui Wang)
- \[ [CALCITE-4016](https://issues.apache.org/jira/browse/CALCITE-4016)\]
Support trait propagation for `EnumerableCalc`
- \[ [CALCITE-4055](https://issues.apache.org/jira/browse/CALCITE-4055)\]
`RelFieldTrimmer` loses hints
- \[ [CALCITE-3975](https://issues.apache.org/jira/browse/CALCITE-3975)\]
Add options to `ProjectFilterTransposeRule` to push down project and filter expressions whole, not just field references
- \[ [CALCITE-4038](https://issues.apache.org/jira/browse/CALCITE-4038)\]
Refactor `RexVisitor`, `RexBiVisitor`, `RelOptUtil.InputFinder`
- \[ [CALCITE-4053](https://issues.apache.org/jira/browse/CALCITE-4053)\]
`RexSimplify` should not pass exprs containing non-const subExprs to `RexExecutor` (Shuo Cheng)
- \[ [CALCITE-4018](https://issues.apache.org/jira/browse/CALCITE-4018)\]
Support trait propagation for `EnumerableValues`
- \[ [CALCITE-4049](https://issues.apache.org/jira/browse/CALCITE-4049)\]
Reduce the time complexity of getting shortest distances
- \[ [CALCITE-4041](https://issues.apache.org/jira/browse/CALCITE-4041)\]
Support trait propagation for `EnumerableCorrelate`
- \[ [CALCITE-4007](https://issues.apache.org/jira/browse/CALCITE-4007)\]
`MergeJoin` collation check should not be limited to join key’s order
- \[ [CALCITE-4012](https://issues.apache.org/jira/browse/CALCITE-4012)\]
Support trait propagation for `EnumerableHashJoin` and `EnumerableNestedLoopJoin` (Rui Wang)
- \[ [CALCITE-4040](https://issues.apache.org/jira/browse/CALCITE-4040)\]
An aggregate function that does not support roll up throws an exception when it is rolled up (Xu Zhaohui)
- \[ [CALCITE-4030](https://issues.apache.org/jira/browse/CALCITE-4030)\]
Reinstate assertion check for trait derivation in `OptimizeTask`
- \[ [CALCITE-4042](https://issues.apache.org/jira/browse/CALCITE-4042)\]
`JoinCommuteRule` must not match `SEMI` / `ANTI` join
- \[ [CALCITE-4043](https://issues.apache.org/jira/browse/CALCITE-4043)\]
Improve `IllegalArgumentException` message in `RelBuilder#field`
- \[ [CALCITE-3991](https://issues.apache.org/jira/browse/CALCITE-3991)\]
The required should always be provided in `RelSet.getOrCreateSubset()` (Botong Huang)
- \[ [CALCITE-3981](https://issues.apache.org/jira/browse/CALCITE-3981)\]
`Volcano.register` should not return stale subset (Botong Huang)
- \[ [CALCITE-2997](https://issues.apache.org/jira/browse/CALCITE-2997)\]
In `SqlToRelConverter` and `RelBuilder`, add option to avoid pushing down join condition
- \[ [CALCITE-4023](https://issues.apache.org/jira/browse/CALCITE-4023)\]
Deprecate `ProjectSortTransposeRule`
- \[ [CALCITE-4031](https://issues.apache.org/jira/browse/CALCITE-4031)\]
Remove code to be removed before 1.24
- \[ [CALCITE-3993](https://issues.apache.org/jira/browse/CALCITE-3993)\]
Add utility methods to `RelTrait`, `RelTraitSet` and `RelCollation`
- \[ [CALCITE-4011](https://issues.apache.org/jira/browse/CALCITE-4011)\]
Support trait propagation for `EnumerableProject` and `EnumerableFilter` (Rui Wang)
- \[ [CALCITE-4019](https://issues.apache.org/jira/browse/CALCITE-4019)\]
Visit `SqlInsert` with `SqlShuttle` cause `NullPointerException` (Xu ZhaoHui)
- \[ [CALCITE-4004](https://issues.apache.org/jira/browse/CALCITE-4004)\]
Show `RelOptRuleOperand` description in debugger to facilitate debugging
- \[ [CALCITE-4009](https://issues.apache.org/jira/browse/CALCITE-4009)\]
Remove traitset remapping in `ProjectJoinTransposeRule`
- \[ [CALCITE-3999](https://issues.apache.org/jira/browse/CALCITE-3999)\]
Simplify `DialectPool` implementation using Guava cache
- \[ [CALCITE-3910](https://issues.apache.org/jira/browse/CALCITE-3910)\]
Enhance `ProjectJoinTransposeRule` to support `SemiJoin` and `AntiJoin` (Liya Fan)
- \[ [CALCITE-3988](https://issues.apache.org/jira/browse/CALCITE-3988)\]
Intersect in `RelMdRowCount` doesn’t take into account `intersect all` (Xu Zhaohui)
- \[ [CALCITE-3985](https://issues.apache.org/jira/browse/CALCITE-3985)\]
Simplify grouped window function in parser (Rui Wang)
- \[ [CALCITE-4086](https://issues.apache.org/jira/browse/CALCITE-4086)\]
Upgrade Avatica version to 1.17.0

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-24-0 "Permalink")

- \[ [CALCITE-4075](https://issues.apache.org/jira/browse/CALCITE-4075)\]
Mock table ‘EMPNULLABLES’ should allow nulls in all non-pk columns
- \[ [CALCITE-4101](https://issues.apache.org/jira/browse/CALCITE-4101)\]
Calcite PR CI often failed due to `elasticsearch:test`, disable the related tests first (Jiatao Tao)
- \[ [CALCITE-4061](https://issues.apache.org/jira/browse/CALCITE-4061)\]
Build should fail if Calcite code uses deprecated APIs
- \[ [CALCITE-4104](https://issues.apache.org/jira/browse/CALCITE-4104)\]
Add automatically link to GitHub PR and ‘pull-request-available’ label to issues
- \[ [CALCITE-3478](https://issues.apache.org/jira/browse/CALCITE-3478)\]
Restructure tests for materialized views (Jin Xing)

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-24-0 "Permalink")

- \[ [CALCITE-3950](https://issues.apache.org/jira/browse/CALCITE-3950)\]
Doc of `SqlGroupingFunction` contradicts its behavior
- Site: Remove ‘(for Calcite committers)’ suffix from headers in section dedicated to committers
- Site: Add instructions for managing Calcite repos through GitHub
- Site: Add Tencent and TBDS logo in powered-by image

## [1.23.0](https://github.com/apache/calcite/releases/tag/calcite-1.23.0) / 2020-05-23 [Permalink](https://calcite.apache.org/docs/history.html\#v1-23-0 "Permalink")

This release comes two months after 1.22.0. It includes more than 100 resolved
issues, comprising a lot of new features as well as performance improvements
and bug-fixes. For some complex queries, the planning speed can be 50x or more
faster than previous versions with built-in default rule set. It is also worth
highlighting the following.

- `VolcanoPlanner` supports top down trait request and trait enforcement without
abstract converter
( [CALCITE-3896](https://issues.apache.org/jira/browse/CALCITE-3896))
- Improve `VolcanoPlanner` performance by removing rule match and subset importance
( [CALCITE-3753](https://issues.apache.org/jira/browse/CALCITE-3753))
- Improve `VolcanoPlanner` performance when abstract converter is enabled
( [CALCITE-2970](https://issues.apache.org/jira/browse/CALCITE-2970))
- Support ClickHouse dialect
( [CALCITE-2157](https://issues.apache.org/jira/browse/CALCITE-2157))
- Support `SESSION` and `HOP` Table function
( [CALCITE-3780](https://issues.apache.org/jira/browse/CALCITE-3780),
[CALCITE-3737](https://issues.apache.org/jira/browse/CALCITE-3737))

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13, 14 and OpenJDK 8, 9, 10, 11, 12, 13, 14;
Guava versions 19.0 to 28.2-jre; other software versions as specified in
gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-23-0 "Permalink")

- \[ [CALCITE-3877](https://issues.apache.org/jira/browse/CALCITE-3877)\]
In `RexWindow`, make fields `upperBound` and `lowerBound` not-nullable
- \[ [CALCITE-3868](https://issues.apache.org/jira/browse/CALCITE-3868)\]
Remove redundant `ruleSet`(protected）and `ruleNames`(private) in `VolcanoPlanner`
- \[ [CALCITE-3753](https://issues.apache.org/jira/browse/CALCITE-3753)\]
`VolcanoPlanner` flags `impatient` and `ambitious` are removed, alternatively
use `checkCancel()` to achieve `impatient` mode
- \[ [CALCITE-3997](https://issues.apache.org/jira/browse/CALCITE-3997)\]
In `VolcanoPlanner`, transformation rules won’t match with Enumerable physical
operators
- \[ [CALCITE-3825](https://issues.apache.org/jira/browse/CALCITE-3825)\]
Split `AbstractMaterializedViewRule` into multiple classes (addendum)

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-23-0 "Permalink")

- \[ [CALCITE-3896](https://issues.apache.org/jira/browse/CALCITE-3896)\]
`VolcanoPlanner` supports top down trait request and trait enforcement without
abstract converter
- \[ [CALCITE-3780](https://issues.apache.org/jira/browse/CALCITE-3780)\]
Support `SESSION` Table function (Rui Wang)
- \[ [CALCITE-3737](https://issues.apache.org/jira/browse/CALCITE-3737)\]
Support `HOP` Table function (Rui Wang)
- \[ [CALCITE-3789](https://issues.apache.org/jira/browse/CALCITE-3789)\]
Support Presto style `unnest` with items alias (Will Yu)
- \[ [CALCITE-2157](https://issues.apache.org/jira/browse/CALCITE-2157)\]
Support ClickHouse dialect (Chris Baynes)
- \[ [CALCITE-3833](https://issues.apache.org/jira/browse/CALCITE-3833)\]
Support `SemiJoin` in `EnumerableMergeJoin`
- \[ [CALCITE-3684](https://issues.apache.org/jira/browse/CALCITE-3684)\]
Support `CONCAT` for variable arguments (Wenhui Tang)
- \[ [CALCITE-3285](https://issues.apache.org/jira/browse/CALCITE-3285)\]
`EnumerableMergeJoin` support non-equi join conditions
- \[ [CALCITE-3694](https://issues.apache.org/jira/browse/CALCITE-3694)\]
Implement `SINH` function
- \[ [CALCITE-3647](https://issues.apache.org/jira/browse/CALCITE-3647)\]
Support MySQL `COMPRESS` function (ritesh-kapoor)
- \[ [CALCITE-3726](https://issues.apache.org/jira/browse/CALCITE-3726)\]
Allow declaring type objects (ritesh-kapoor)
- \[ [CALCITE-3815](https://issues.apache.org/jira/browse/CALCITE-3815)\]
Support SQL standard aggregate functions: `EVERY`, `SOME`, `INTERSECTION`
- \[ [CALCITE-3704](https://issues.apache.org/jira/browse/CALCITE-3704)\]
Implement `STRCMP` function

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-23-0 "Permalink")

- \[ [CALCITE-3984](https://issues.apache.org/jira/browse/CALCITE-3984)\]
Support `Exchange` operator in `RelFieldTrimmer` (Xu Zhaohui)
- \[ [CALCITE-3971](https://issues.apache.org/jira/browse/CALCITE-3971)\]
Support `Calc` in `RelMdColumnOrigins` (Xu ZhaoHui)
- \[ [CALCITE-3921](https://issues.apache.org/jira/browse/CALCITE-3921)\]
Support `TableModify` json serialization and deserialization (Wang Yanlin)
- \[ [CALCITE-3938](https://issues.apache.org/jira/browse/CALCITE-3938)\]
Support `LogicalCalc` in `RelShuttle` (dz)
- \[ [CALCITE-3880](https://issues.apache.org/jira/browse/CALCITE-3880)\]
Add `SortExchange` support to `RelFieldTrimmer` (Krisztian Kasa)
- \[ [CALCITE-3867](https://issues.apache.org/jira/browse/CALCITE-3867)\]
Support `RelDistribution` json serialization (Krisztian Kasa)
- \[ [CALCITE-3634](https://issues.apache.org/jira/browse/CALCITE-3634)\]
Add `IntersectOnCalcsToIntersectUnifyRule` for materialized view recognition
(dz)
- \[ [CALCITE-3934](https://issues.apache.org/jira/browse/CALCITE-3934)\]
Allow type-coercion in `CONCAT` operator
- \[ [CALCITE-3889](https://issues.apache.org/jira/browse/CALCITE-3889)\]
Add `apply(Mappings.Mapping)` to `RelTrait` and `RelTraitSet`
- \[ [CALCITE-3838](https://issues.apache.org/jira/browse/CALCITE-3838)\]
Support `Calc` in `RelMdSize`, `RelMdSelectivity`, `RelMdMaxRowCount`,
`RelMdMinRowCount`, `RelMdTableReferences`
- \[ [CALCITE-3718](https://issues.apache.org/jira/browse/CALCITE-3718)\]
Support `Intersect` and `Minus` in `Bindables` (xzh)
- \[ [CALCITE-3997](https://issues.apache.org/jira/browse/CALCITE-3997)\]
Logical rules matched with physical operators but failed to handle traits
- \[ [CALCITE-3979](https://issues.apache.org/jira/browse/CALCITE-3979)\]
Simplification might have removed CAST expression(s) incorrectly
- \[ [CALCITE-3968](https://issues.apache.org/jira/browse/CALCITE-3968)\]
TPC-H queries take forever for planning
- \[ [CALCITE-3877](https://issues.apache.org/jira/browse/CALCITE-3877)\]
In `RexWindow`, make fields `upperBound` and `lowerBound` not-nullable
- \[ [CALCITE-3969](https://issues.apache.org/jira/browse/CALCITE-3969)\]
Trait keys remapping may throw exception when some trait key is not mapped
(Roman Kondakov)
- \[ [CALCITE-3982](https://issues.apache.org/jira/browse/CALCITE-3982)\]
Simplify `FilterMergeRule` to rely on `RelBuilder` instead of `RexProgram`
- \[ [CALCITE-3983](https://issues.apache.org/jira/browse/CALCITE-3983)\]
Add utility methods to `RelTraitSet`
- \[ [CALCITE-3980](https://issues.apache.org/jira/browse/CALCITE-3980)\]
Redis-adapter redis connection is not reused when `RedisTable` is created (Xu
Zhang)
- \[ [CALCITE-3961](https://issues.apache.org/jira/browse/CALCITE-3961)\]
`VolcanoPlanner.prunedNodes` info is lost when duplicate `RelNode` is discarded
(Botong Huang)
- \[ [CALCITE-3866](https://issues.apache.org/jira/browse/CALCITE-3866)\]
“numeric field overflow” when running the generated SQL in Postgres (Wenhui
Tang)
- \[ [CALCITE-3926](https://issues.apache.org/jira/browse/CALCITE-3926)\]
`CannotPlanException` when an empty LogicalValues requires a certain collation
- \[ [CALCITE-3973](https://issues.apache.org/jira/browse/CALCITE-3973)\]
Hints should not unparse as enclosed in parentheses (Alex Baden)
- \[ [CALCITE-3887](https://issues.apache.org/jira/browse/CALCITE-3887)\]
`Filter` and `Join` conditions may not need to retain nullability during
simplifications
- \[ [CALCITE-3966](https://issues.apache.org/jira/browse/CALCITE-3966)\]
Trigger rules for existing `RelSubset` when it becomes delivered
- \[ [CALCITE-3928](https://issues.apache.org/jira/browse/CALCITE-3928)\]
Trim unused fields before materialized view matching (dz)
- \[ [CALCITE-3962](https://issues.apache.org/jira/browse/CALCITE-3962)\]
Make `JSON_VALUE` operands varadic
- \[ [CALCITE-3827](https://issues.apache.org/jira/browse/CALCITE-3827)\]
Reduce the time complexity of finding in-edges of a vertex in the graph (Liya
Fan)
- \[ [CALCITE-3878](https://issues.apache.org/jira/browse/CALCITE-3878)\]
Create `ArrayList` with initial capacity when size is known (Xu Zhang)
- \[ [CALCITE-3949](https://issues.apache.org/jira/browse/CALCITE-3949)\]
`RelDistributions.of()` and `RelCollations.of()` should canonize trait instance
- \[ [CALCITE-3954](https://issues.apache.org/jira/browse/CALCITE-3954)\]
Always compare types using equals
- \[ [CALCITE-3955](https://issues.apache.org/jira/browse/CALCITE-3955)\]
Remove the first operand of `RexCall` from `SqlWindowTableFunction`
- \[ [CALCITE-3915](https://issues.apache.org/jira/browse/CALCITE-3915)\]
Add rule listener to report rule attempts and time at `DEBUG` log level
(Xiening Dai)
- \[ [CALCITE-3948](https://issues.apache.org/jira/browse/CALCITE-3948)\]
`RelSubset` matching is not properly handled in `VolcanoRuleCall` (Botong Huang)
- \[ [CALCITE-3758](https://issues.apache.org/jira/browse/CALCITE-3758)\]
`FilterTableScanRule` generate wrong mapping for filter condition when
underlying is `BindableTableScan` (Jin Xing)
- \[ [CALCITE-3942](https://issues.apache.org/jira/browse/CALCITE-3942)\]
Move type-coercion configurations into `SqlValidator.Config`
- \[ [CALCITE-3939](https://issues.apache.org/jira/browse/CALCITE-3939)\]
Change `UnionEliminatorRule` and `ProjectRemoveRule` to auto pruning
`SubstitutionRule` (Botong Huang)
- \[ [CALCITE-3944](https://issues.apache.org/jira/browse/CALCITE-3944)\]
Move `dumpSets` and `dumpGraphviz` out of `VolcanoPlanner`
- \[ [CALCITE-3927](https://issues.apache.org/jira/browse/CALCITE-3927)\]
`RelSubset` is not fired for rule when set gets merged (Botong Huang)
- \[ [CALCITE-3868](https://issues.apache.org/jira/browse/CALCITE-3868)\]
Remove redundant `ruleSet`(protected）and `ruleNames`(private) in VolcanoPlanner
- \[ [CALCITE-3940](https://issues.apache.org/jira/browse/CALCITE-3940)\]
`Hint` item can not parse correctly if the name is right after token /\*+
- \[ [CALCITE-3447](https://issues.apache.org/jira/browse/CALCITE-3447)\]
MutableScans with the same qualified name are not equivalent (Dai Min,Jin Xing)
- \[ [CALCITE-3931](https://issues.apache.org/jira/browse/CALCITE-3931)\]
Add LOOKAHEAD(2) for methods defined in `createStatementParserMethods`
- \[ [CALCITE-3790](https://issues.apache.org/jira/browse/CALCITE-3790)\]
Make the url() of Sources.of(file) available
- \[ [CALCITE-3894](https://issues.apache.org/jira/browse/CALCITE-3894)\]
SET operation between `DATE` and `TIMESTAMP` returns a wrong result
- \[ [CALCITE-3881](https://issues.apache.org/jira/browse/CALCITE-3881)\]
`SqlFunctions#addMonths` yields incorrect results in some corner case
(Zhenghua Gao)
- \[ [CALCITE-3324](https://issues.apache.org/jira/browse/CALCITE-3324)\]
Set `updateCount` when creating `MetaResultSet` (Robert Yokota)
- \[ [CALCITE-3733](https://issues.apache.org/jira/browse/CALCITE-3733)\]
In JDBC adapter, when generating SQL for MySQL, generate `TIMESTAMP` type as
`DATETIME` for `CAST` (Vineet Garg)
- \[ [CALCITE-3909](https://issues.apache.org/jira/browse/CALCITE-3909)\]
`RelMdMinRowCount` doesn’t take into account `UNION``DISTINCT`
- \[ [CALCITE-3576](https://issues.apache.org/jira/browse/CALCITE-3576)\]
Remove enumerable convention check in `FilterIntoJoinRule`
- \[ [CALCITE-2593](https://issues.apache.org/jira/browse/CALCITE-2593)\]
Plan error when transforming multiple collations to single collation
- \[ [CALCITE-2010](https://issues.apache.org/jira/browse/CALCITE-2010)\]
Cannot plan query that is `UNION ALL` applied to `VALUES`
- \[ [CALCITE-3865](https://issues.apache.org/jira/browse/CALCITE-3865)\]
`RelCollationTraitDef.canConvert` should always return true
- \[ [CALCITE-2970](https://issues.apache.org/jira/browse/CALCITE-2970)\]
Improve `VolcanoPlanner` performance when enabling abstract converter
- \[ [CALCITE-3914](https://issues.apache.org/jira/browse/CALCITE-3914)\]
Improve `SubstitutionVisitor` to consider `RexCall` of type `PLUS` and `TIMES`
for canonicalization (Vineet Garg)
- \[ [CALCITE-3912](https://issues.apache.org/jira/browse/CALCITE-3912)\]
Incorrect mapping parsing when properties have same name as reserved keywords
in ElasticSearch
- \[ [CALCITE-3900](https://issues.apache.org/jira/browse/CALCITE-3900)\]
Add `Config` for `SqlValidator`
- \[ [CALCITE-3908](https://issues.apache.org/jira/browse/CALCITE-3908)\]
`JoinCommuteRule` should update all input references in join condition
- \[ [CALCITE-3898](https://issues.apache.org/jira/browse/CALCITE-3898)\]
`RelOptPredicateList` may generate incorrect map of constant values
- \[ [CALCITE-3835](https://issues.apache.org/jira/browse/CALCITE-3835)\]
Overloaded table functions fail with an assertion error if param types differ
- \[ [CALCITE-3851](https://issues.apache.org/jira/browse/CALCITE-3851)\]
Replace the node importance map with a set for pruned nodes
- \[ [CALCITE-3872](https://issues.apache.org/jira/browse/CALCITE-3872)\]
Simplify expressions with unary minus
- \[ [CALCITE-3814](https://issues.apache.org/jira/browse/CALCITE-3814)\]
Support JDK 14 and guava 28.2-jre
- \[ [CALCITE-3876](https://issues.apache.org/jira/browse/CALCITE-3876)\]
`RelToSqlConverter` should not merge a `Project` that contains a window function
that references a window function in input `Project`
- \[ [CALCITE-3891](https://issues.apache.org/jira/browse/CALCITE-3891)\]
Remove use of Pair.zip in `RelTraitSet`
- \[ [CALCITE-3885](https://issues.apache.org/jira/browse/CALCITE-3885)\]
Restore trace logging for rules queue and Volcano planner’s internal state
(Roman Kondakov)
- \[ [CALCITE-3886](https://issues.apache.org/jira/browse/CALCITE-3886)\]
Execute substitution rule according to the order they get matched
- \[ [CALCITE-3882](https://issues.apache.org/jira/browse/CALCITE-3882)\]
Remove duplicated code from `SqlTypeAssignmentRule` (Wenhui Tang)
- \[ [CALCITE-3846](https://issues.apache.org/jira/browse/CALCITE-3846)\]
`EnumerableMergeJoin`: wrong comparison of composite key with null values
- \[ [CALCITE-3829](https://issues.apache.org/jira/browse/CALCITE-3829)\]
`MergeJoinEnumerator` should not use inputs enumerators until it is really
required
- \[ [CALCITE-3840](https://issues.apache.org/jira/browse/CALCITE-3840)\]
Re-aliasing of `VALUES` that has column aliases produces wrong SQL in the JDBC
adapter
- \[ [CALCITE-3810](https://issues.apache.org/jira/browse/CALCITE-3810)\]
Render `ANTI` and `SEMI` join to `NOT EXISTS` and `EXISTS` in the JDBC adapter.
Also add forgotten `IS_DISTINCT_FROM` translation support
- \[ [CALCITE-3852](https://issues.apache.org/jira/browse/CALCITE-3852)\]
`RexSimplify` doesn’t simplify NOT EQUAL predicates
- \[ [CALCITE-3862](https://issues.apache.org/jira/browse/CALCITE-3862)\]
Materialized view rewriting algorithm throws `IndexOutOfBoundsException`
(Vineet Garg)
- \[ [CALCITE-3856](https://issues.apache.org/jira/browse/CALCITE-3856)\]
Remove code to be removed before 1.23
- \[ [CALCITE-3855](https://issues.apache.org/jira/browse/CALCITE-3855)\]
Supports snapshot on table with virtual columns during sql-to-rel conversion
- \[ [CALCITE-3853](https://issues.apache.org/jira/browse/CALCITE-3853)\]
Minor improvements in `SortJoinCopyRule`
- \[ [CALCITE-3848](https://issues.apache.org/jira/browse/CALCITE-3848)\]
Rewriting for materialized view consisting of group by on join keys fails with
`Mappings$NoElementException` (Vineet Garg)
- \[ [CALCITE-3845](https://issues.apache.org/jira/browse/CALCITE-3845)\]
`CASE WHEN` expression with nullability `CAST` is considered as reduced wrongly in
`ReduceExpressionsRule`
- \[ [CALCITE-3847](https://issues.apache.org/jira/browse/CALCITE-3847)\]
Decorrelation for join with lateral table outputs wrong plan if the join
condition contains correlation variables
- \[ [CALCITE-3753](https://issues.apache.org/jira/browse/CALCITE-3753)\]
Boost `VolcanoPlanner` performance by removing rule match and subset importance
- \[ [CALCITE-3823](https://issues.apache.org/jira/browse/CALCITE-3823)\]
Do not use `String.replaceAll`
- \[ [CALCITE-3412](https://issues.apache.org/jira/browse/CALCITE-3412)\]
FLOOR(timestamp TO WEEK) gives wrong result
- \[ [CALCITE-3839](https://issues.apache.org/jira/browse/CALCITE-3839)\]
After calling `RelBuilder.aggregate`, cannot lookup field by name
- \[ [CALCITE-3819](https://issues.apache.org/jira/browse/CALCITE-3819)\]
Prune parent `RelNode` when merging child `RelSet` with parent `RelSet`
- \[ [CALCITE-3809](https://issues.apache.org/jira/browse/CALCITE-3809)\]
`RexSimplify` simplifies nondeterministic function incorrectly
- \[ [CALCITE-3828](https://issues.apache.org/jira/browse/CALCITE-3828)\]
MergeJoin throws NPE in case of null keys
- \[ [CALCITE-3820](https://issues.apache.org/jira/browse/CALCITE-3820)\]
`EnumerableDefaults#orderBy` should be lazily computed + support enumerator
re-initialization
- \[ [CALCITE-3837](https://issues.apache.org/jira/browse/CALCITE-3837)\]
AntiJoin with empty right input can always be transformed as its left input
- \[ [CALCITE-3821](https://issues.apache.org/jira/browse/CALCITE-3821)\]
`RelOptUtil::containsMultisetOrWindowedAgg` doesn’t really check multiset
(Xiening Dai)
- \[ [CALCITE-3825](https://issues.apache.org/jira/browse/CALCITE-3825)\]
Split `AbstractMaterializedViewRule` into multiple classes (addendum)
- \[ [CALCITE-3824](https://issues.apache.org/jira/browse/CALCITE-3824)\]
`JoinProjectTransposeRule` should skip Projects containing windowing expression
(Vineet Garg)
- \[ [CALCITE-3734](https://issues.apache.org/jira/browse/CALCITE-3734)\]
MySQL JDBC rewrite is producing queries with CHAR with range beyond 255 (Vineet
Garg)
- \[ [CALCITE-3817](https://issues.apache.org/jira/browse/CALCITE-3817)\]
`VolcanoPlanner` does not remove the entry in ruleNames when removing a rule
- \[ [CALCITE-2592](https://issues.apache.org/jira/browse/CALCITE-2592)\]
`EnumerableMergeJoin` is never taken

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-23-0 "Permalink")

- \[ [CALCITE-3965](https://issues.apache.org/jira/browse/CALCITE-3965)\]
Avoid `DiffRepository` lock contention
- \[ [CALCITE-3924](https://issues.apache.org/jira/browse/CALCITE-3924)\]
Fix flakey test to handle `TIMESTAMP` and `TIMESTAMP(0)` correctly (neoReMinD)
- \[ [CALCITE-3888](https://issues.apache.org/jira/browse/CALCITE-3888)\]
Switch avatica-server to be test dependency for core
- \[ [CALCITE-3660](https://issues.apache.org/jira/browse/CALCITE-3660)\]
Disable flaky test `PigRelBuilderStyleTest` since it fails too often for no reason
- \[ [CALCITE-3892](https://issues.apache.org/jira/browse/CALCITE-3892)\]
Make junit test classes and methods non-public where possible
- Update release-plugins: 1.65 -> 1.70
- Avoid failures in SourceTest when filesystem does not support unicode paths
- Add AvoidStarImport Checkstyle rule
- The release tag should be ‘calcite-N.N’ not ‘vN.N’

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-23-0 "Permalink")

- \[ [CALCITE-3958](https://issues.apache.org/jira/browse/CALCITE-3958)\]
Revise documentation of gradle.properties in Cassandra/Piglet and
`SubstitutionVisitor` (xzh)
- \[ [CALCITE-3726](https://issues.apache.org/jira/browse/CALCITE-3726)\]
Documentation for Declaring Objects For Types Defined In Schema (ritesh-kapoor)
- Site: Add Ant Financial logo in powered-by image (Wang Yanlin)
- Site: Change affiliation of Stamatis Zampetakis
- Site: Add Forward Xu, Jin Xing, Wang Yanlin, as committers
- Site: Add Vineet Garg as committer
- Site: Add Feng Zhu as committer

## [1.22.0](https://github.com/apache/calcite/releases/tag/calcite-1.22.0) / 2020-03-05 [Permalink](https://calcite.apache.org/docs/history.html\#v1-22-0 "Permalink")

This release comes five months after 1.21.0. It includes more than 250
resolved issues, comprising a large number of new features as well as
general improvements and bug-fixes. Among others, it is worth
highlighting the following.

- Support
[SQL hints](https://issues.apache.org/jira/browse/CALCITE-482)
for different kind of relational expressions
- A new
[Redis adapter](https://issues.apache.org/jira/browse/CALCITE-3510)
- Support Oracle
[XML](https://issues.apache.org/jira/browse/CALCITE-3579) [functions](https://issues.apache.org/jira/browse/CALCITE-3580)
and
[MySQL](https://issues.apache.org/jira/browse/CALCITE-3684) [math](https://issues.apache.org/jira/browse/CALCITE-3695) [functions](https://issues.apache.org/jira/browse/CALCITE-3707)

We have also fixed some important bugs:

- Merging `RelSet` sometimes gave
[inconsistent state](https://issues.apache.org/jira/browse/CALCITE-2018),
- The `GROUP_ID` function gave
[incorrect results](https://issues.apache.org/jira/browse/CALCITE-1824),
- Improve row count estimate for
[Correlate](https://issues.apache.org/jira/browse/CALCITE-3711)
relational expression,
- When applying the
[MOD operation to DECIMAL values](https://issues.apache.org/jira/browse/CALCITE-3435)
the inferred type was incorrrect.

Compatibility: This release is tested on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13 and OpenJDK 8, 9, 10, 11, 12, 13;
Guava versions 19.0 to 27.1-jre; Apache Flink 1.10.0;
other software versions as specified in gradle.properties.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-changes "Permalink")

- Constructors for `Project`, `TableScan`, `Calc`, `Aggregate` and `Join` introduce new parameter named `hints` ( [CALCITE-482](https://issues.apache.org/jira/browse/CALCITE-482))
- Logical `RelNode`’s `create` method need to pass in hints explicitly ( [CALCITE-3723](https://issues.apache.org/jira/browse/CALCITE-3723))
- `Project` names will not represent in `RelNode` digest anymore ( [CALCITE-3713](https://issues.apache.org/jira/browse/CALCITE-3713))
- `RexCall`s are default to be normalized in the `RelNode` digest ( [CALCITE-2450](https://issues.apache.org/jira/browse/CALCITE-2450))
- `RelBuilder.aggregate` now would prune the unused fields from the input, thus the plan may change ( [CALCITE-3763](https://issues.apache.org/jira/browse/CALCITE-3763))
- `RelBuilder.scan` and sql-to-rel conversion always invoke `RelOptTable.toRel` now, so there may be some plan changes for the `TableScan` node if your `RelOptTable.toRel` returns a physical rel before

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-22-0 "Permalink")

- \[ [CALCITE-3771](https://issues.apache.org/jira/browse/CALCITE-3771)\] `TRIM` Support for HIVE/SPARK Dialect (Dhirenda Gautam)
- \[ [CALCITE-3707](https://issues.apache.org/jira/browse/CALCITE-3707)\] Implement `COSH` function
- \[ [CALCITE-3695](https://issues.apache.org/jira/browse/CALCITE-3695)\] Implement `TANH` function
- \[ [CALCITE-3640](https://issues.apache.org/jira/browse/CALCITE-3640)\] Oracle `EXISTSNODE` Function Support (ritesh-kapoor)
- \[ [CALCITE-3382](https://issues.apache.org/jira/browse/CALCITE-3382)\] Support `TUMBLE` as Table Value Function (Rui Wang)
- \[ [CALCITE-3510](https://issues.apache.org/jira/browse/CALCITE-3510)\] Implement Redis adapter
- \[ [CALCITE-3684](https://issues.apache.org/jira/browse/CALCITE-3684)\] Implement `CBRT` function (Qianjin Xu)
- \[ [CALCITE-3663](https://issues.apache.org/jira/browse/CALCITE-3663)\] Support for `TRIM` function in BigQuery Dialect
- \[ [CALCITE-3580](https://issues.apache.org/jira/browse/CALCITE-3580)\] Oracle `EXTRACT(XML)` Function Support (ritesh-kapoor)
- \[ [CALCITE-3579](https://issues.apache.org/jira/browse/CALCITE-3579)\] Oracle `XMLTRANSFORM` Function Support (ritesh-kapoor)
- \[ [CALCITE-3591](https://issues.apache.org/jira/browse/CALCITE-3591)\] Add bit\_xor aggregate operator (wangxlong)
- \[ [CALCITE-3552](https://issues.apache.org/jira/browse/CALCITE-3552)\] Support MySQL `ExtractValue` function
- \[ [CALCITE-3542](https://issues.apache.org/jira/browse/CALCITE-3542)\] Implement `RepeatUnion` All=false
- \[ [CALCITE-482](https://issues.apache.org/jira/browse/CALCITE-482)\] Implement sql and planner hints
- \[ [CALCITE-3781](https://issues.apache.org/jira/browse/CALCITE-3781)\] `HintStrategy` can specify excluded rules for planner
- \[ [CALCITE-3730](https://issues.apache.org/jira/browse/CALCITE-3730)\] Add hints to `RelBuilder`
- \[ [CALCITE-3719](https://issues.apache.org/jira/browse/CALCITE-3719)\] Add hint option checker to customize the option
- \[ [CALCITE-3631](https://issues.apache.org/jira/browse/CALCITE-3631)\] Support SQL hints for `Calc`
- \[ [CALCITE-3590](https://issues.apache.org/jira/browse/CALCITE-3590)\] Support SQL hints for `Aggregate` (Shuo Cheng)
- \[ [CALCITE-3584](https://issues.apache.org/jira/browse/CALCITE-3584)\] Propagate hints when decorrelating a query
- \[ [CALCITE-3736](https://issues.apache.org/jira/browse/CALCITE-3736)\] Add an interface in `RelOptRuleCall` to customize the propagation of hints before registering into planner rule
- \[ [CALCITE-3496](https://issues.apache.org/jira/browse/CALCITE-3496)\] Hive dialect and MS SQL dialect support with cube and with rollup (dz)
- \[ [CALCITE-3465](https://issues.apache.org/jira/browse/CALCITE-3465)\] Add support for missing Cassandra 3.x data types (Alessandro Solimando)
- \[ [CALCITE-3442](https://issues.apache.org/jira/browse/CALCITE-3442)\] In ElasticSearch adapter, set `stored_fields = _none_` to prohibit FetchPhase get involved (Yunfeng,Wu)
- \[ [CALCITE-3437](https://issues.apache.org/jira/browse/CALCITE-3437)\] Support `MatchQuery` in ElasticSearch adapter (Shlok Srivastava)
- \[ [CALCITE-3434](https://issues.apache.org/jira/browse/CALCITE-3434)\] ElasticSearch schema with pathPrefix (Jeffery Zhang)
- \[ [CALCITE-3405](https://issues.apache.org/jira/browse/CALCITE-3405)\] Prune columns for `ProjectableFilterableTable` when `Project` is not simple mapping (Jin Xing)
- \[ [CALCITE-3349](https://issues.apache.org/jira/browse/CALCITE-3349)\] Add `CREATE FUNCTION` and `DROP FUNCTION` ddl (Zhenqiu Huang)
- \[ [CALCITE-3323](https://issues.apache.org/jira/browse/CALCITE-3323)\] Add mode to `SqlValidator` that treats statements as valid if they contain unknown functions (Ryan Fu)
- \[ [CALCITE-3302](https://issues.apache.org/jira/browse/CALCITE-3302)\] Implement `CLASSIFIER` and `LAST` functions for `MATCH_RECOGNIZE`
- \[ [CALCITE-3112](https://issues.apache.org/jira/browse/CALCITE-3112)\] Support `Window` in `RelToSqlConverter` (Wenhui Tang)

#### Bug fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-22-0 "Permalink")

- Following CALCITE-3769: Add BindableTableScanRule into the default ruleset
- \[ [CALCITE-3826](https://issues.apache.org/jira/browse/CALCITE-3826)\] `UPDATE` assigns wrong type to bind variables
- \[ [CALCITE-3830](https://issues.apache.org/jira/browse/CALCITE-3830)\] The ‘approximate’ field should be considered when computing the digest of `AggregateCall`
- \[ [CALCITE-3807](https://issues.apache.org/jira/browse/CALCITE-3807)\] checkForSatisfiedConverters() is unnecessary
- \[ [CALCITE-3803](https://issues.apache.org/jira/browse/CALCITE-3803)\] Enhance `RexSimplify` to simplify ‘a>1 or (a<3 and b)’ to ‘a>1 or b’ if column a is not nullable
- \[ [CALCITE-2707](https://issues.apache.org/jira/browse/CALCITE-2707)\] Information about distinct aggregation is lost in `MATCH_RECOGNIZE`
- \[ [CALCITE-3801](https://issues.apache.org/jira/browse/CALCITE-3801)\] Deprecate `SqlToRelConverter.Config#isConvertTableAccess`
- \[ [CALCITE-3791](https://issues.apache.org/jira/browse/CALCITE-3791)\] `HepPlanner` does not clear metadata cache for the ancestors of discarded node when a transformation happens
- \[ [CALCITE-3794](https://issues.apache.org/jira/browse/CALCITE-3794)\] `RexSimplify` should return early if there is no pulled up predicate when simplifying using predicates
- \[ [CALCITE-3798](https://issues.apache.org/jira/browse/CALCITE-3798)\] Make `RelBuilder` view expander pluggable
- \[ [CALCITE-3769](https://issues.apache.org/jira/browse/CALCITE-3769)\] Deprecate `TableScanRule`
- \[ [CALCITE-3774](https://issues.apache.org/jira/browse/CALCITE-3774)\] In `RelBuilder` and `ProjectMergeRule`, prevent merges when it would increase expression complexity
- \[ [CALCITE-3763](https://issues.apache.org/jira/browse/CALCITE-3763)\] `RelBuilder.aggregate` should prune unused fields from the input, if the input is a `Project`
- Add `RelBuilder.transform`, which allows you to clone a `RelBuilder` with slightly different Config
- \[ [CALCITE-3785](https://issues.apache.org/jira/browse/CALCITE-3785)\] `HepPlanner.belongToDag()` doesn’t have to use mapDigestToVertex (Xiening Dai)
- \[ [CALCITE-3783](https://issues.apache.org/jira/browse/CALCITE-3783)\] `PruneEmptyRules#JOIN_RIGHT_INSTANCE` wrong behavior for `JoinRelType.ANTI`
- \[ [CALCITE-3773](https://issues.apache.org/jira/browse/CALCITE-3773)\] Wrong parameter in `EnumerableMergeJoin::create` \`method
- \[ [CALCITE-3768](https://issues.apache.org/jira/browse/CALCITE-3768)\] `VolcanoPlanner.changeTraitsUsingConverters()` has parameter that’s never used
- \[ [CALCITE-3766](https://issues.apache.org/jira/browse/CALCITE-3766)\] Add a Builder to `RelHint`
- \[ [CALCITE-3765](https://issues.apache.org/jira/browse/CALCITE-3765)\] Returns early when there is an existing operand when assigning operands solve order
- Switch `RelBuilder.Config` to an interface, and deprecate `RelBuilder.ConfigBuilder`
- \[ [CALCITE-3764](https://issues.apache.org/jira/browse/CALCITE-3764)\] `AggregateCaseToFilterRule` handles `NULL` values incorrectly
- \[ [CALCITE-1824](https://issues.apache.org/jira/browse/CALCITE-1824)\] `GROUP_ID` returns wrong result (DonnyZone)
- \[ [CALCITE-3756](https://issues.apache.org/jira/browse/CALCITE-3756)\] `RelSubset` should not match `operand(RelNode.class)`
- \[ [CALCITE-3738](https://issues.apache.org/jira/browse/CALCITE-3738)\] Missing order by logical plan for `INSERT` statement
- \[ [CALCITE-3676](https://issues.apache.org/jira/browse/CALCITE-3676)\] `VolcanoPlanner.dumpGraphviz` should handle exception gracefully (Qianjin Xu)
- \[ [CALCITE-3653](https://issues.apache.org/jira/browse/CALCITE-3653)\] Support `TableModify` in `ToLogicalConverter` (dz)
- \[ [CALCITE-3668](https://issues.apache.org/jira/browse/CALCITE-3668)\] `VolcanoPlanner` does not match all the `RelSubSet` in matchRecursive
- \[ [CALCITE-3744](https://issues.apache.org/jira/browse/CALCITE-3744)\] Duplicate rule matches when `RelSet` gets merged
- \[ [CALCITE-3747](https://issues.apache.org/jira/browse/CALCITE-3747)\] Constructing `BETWEEN` with `RelBuilder` throws class cast exception
- Add HSQLDB data sets (scott, foodmart and chinook) to SQLLine’s path
- \[ [CALCITE-3735](https://issues.apache.org/jira/browse/CALCITE-3735)\] In `ImmutableBeans`, allow interfaces to have default methods
- \[ [CALCITE-3736](https://issues.apache.org/jira/browse/CALCITE-3736)\] Add an interface in `RelOptRuleCall` to customize the propagation of hints before registering into planner rule
- \[ [CALCITE-3721](https://issues.apache.org/jira/browse/CALCITE-3721)\] `Filter` of distinct aggregate call is lost after applying `AggregateExpandDistinctAggregatesRule` (Shuo Cheng)
- \[ [CALCITE-3644](https://issues.apache.org/jira/browse/CALCITE-3644)\] Add `ProjectSetOpTransposeRule` to normalize materialized view (xy2953396112)
- Add method `Pair.forEach(Iterable, Iterable, BiConsumer)`
- Really deprecate `RelBuilder.groupKey(ImmutableBitSet, ImmutableList<ImmutableBitSet>)`
- \[ [CALCITE-3729](https://issues.apache.org/jira/browse/CALCITE-3729)\] Filters failed to be pushed down when it’s identical to join condition (Jin Xing)
- \[ [CALCITE-3725](https://issues.apache.org/jira/browse/CALCITE-3725)\] `RelMetadataTest` fails with NPE due to unsafe `RelMetadataQuery.instance` call (Jin Xing)
- \[ [CALCITE-3675](https://issues.apache.org/jira/browse/CALCITE-3675)\] SQL to Rel conversion is broken for coalesce on nullable field (DonnyZone)
- Refine rules so they produce less no-op matches
- Refine logging dependencies: keep slf4j bridges in runtime classpath only
- Refine `RuleQueue#addMatch`: skip the match if it is not required for the phase
- \[ [CALCITE-3364](https://issues.apache.org/jira/browse/CALCITE-3364)\] `ClassCastException` if group by is used on the result of scalar valued table function (DonnyZone)
- \[ [CALCITE-3722](https://issues.apache.org/jira/browse/CALCITE-3722)\] Add `Hook#PLAN_BEFORE_IMPLEMENTATION` to capture the plan after optimization
- \[ [CALCITE-3713](https://issues.apache.org/jira/browse/CALCITE-3713)\] Remove column names from `Project#digest`
- \[ [CALCITE-2450](https://issues.apache.org/jira/browse/CALCITE-2450)\] Reorder `RexCall` predicates to a canonical form
validation
- \[ [CALCITE-3677](https://issues.apache.org/jira/browse/CALCITE-3677)\] Add assertion to `EnumerableTableScan` constructor to validate if the table is suitable for enumerable scan
- \[ [CALCITE-3715](https://issues.apache.org/jira/browse/CALCITE-3715)\] Add an interface to pass the table hints to `RelOptTable`
- \[ [CALCITE-3714](https://issues.apache.org/jira/browse/CALCITE-3714)\] `BitString.createFromBytes` reverses order of the bits in each byte
- \[ [CALCITE-3712](https://issues.apache.org/jira/browse/CALCITE-3712)\] Optimize lossless casts in `RexSimplify`: CAST(CAST(intExpr as BIGINT) as INT) => intExpr
- \[ [CALCITE-3587](https://issues.apache.org/jira/browse/CALCITE-3587)\] `RexBuilder` may lose decimal fraction for creating literal with `DECIMAL` type (Wang Yanlin)
- \[ [CALCITE-3658](https://issues.apache.org/jira/browse/CALCITE-3658)\] `TableModify` of `Update` contains correlated variable by mistake (Jin Xing)
- \[ [CALCITE-3711](https://issues.apache.org/jira/browse/CALCITE-3711)\] `Correlate` should override `estimateRowCount`
- \[ [CALCITE-3606](https://issues.apache.org/jira/browse/CALCITE-3606)\] Derive target table column list by mistake when convert `TableModify` to Sql string (JinXing)
- \[ [CALCITE-3526](https://issues.apache.org/jira/browse/CALCITE-3526)\] `SqlPrettyWriter` should have options to fold/chop long lines, print leading commas
- \[ [CALCITE-3328](https://issues.apache.org/jira/browse/CALCITE-3328)\] Immutable beans, powered by reflection
- \[ [CALCITE-3672](https://issues.apache.org/jira/browse/CALCITE-3672)\] Support implicit type coercion for insert and update
- \[ [CALCITE-3651](https://issues.apache.org/jira/browse/CALCITE-3651)\] NPE when convert relational algebra that correlates `TableFunctionScan` (Wang Yanlin)
- \[ [CALCITE-3666](https://issues.apache.org/jira/browse/CALCITE-3666)\] Refine `RelMdColumnUniqueness` and `RelMdUniqueKeys` for `Calc`
- \[ [CALCITE-3655](https://issues.apache.org/jira/browse/CALCITE-3655)\] `SortJoinTransposeRule` must not push sort into `Project` that contains `OVER` expressions
- \[ [CALCITE-3649](https://issues.apache.org/jira/browse/CALCITE-3649)\] Hints should be propagated correctly in planner rules if original node is transformed to different kind
- \[ [CALCITE-3563](https://issues.apache.org/jira/browse/CALCITE-3563)\] When resolving method call in calcite runtime, add type check and match mechanism for input arguments (DonnyZone)
- \[ [CALCITE-3621](https://issues.apache.org/jira/browse/CALCITE-3621)\] Push down sort to DB, SQL of `Sort` rel contains explicit field name instead of \* (Lei Jiang)
- \[ [CALCITE-3652](https://issues.apache.org/jira/browse/CALCITE-3652)\] Add org.apiguardian:apiguardian-api to specify API status
- \[ [CALCITE-3632](https://issues.apache.org/jira/browse/CALCITE-3632)\] Add IntersectToIntersectUnify Rule in SubstitutionVisitor (xy2953396112)
- \[ [CALCITE-3643](https://issues.apache.org/jira/browse/CALCITE-3643)\] Prevent matching `JoinCommuteRule` when both inputs are the same
- \[ [CALCITE-3630](https://issues.apache.org/jira/browse/CALCITE-3630)\] Improve `ReduceExpressionsRule`
- \[ [CALCITE-3607](https://issues.apache.org/jira/browse/CALCITE-3607)\] Support `LogicalTableModify` in RelShuttle (xy2953396112)
- \[ [CALCITE-3618](https://issues.apache.org/jira/browse/CALCITE-3618)\] ProjectToWindowRule - correct isDependent checking (lxian2shell)
- \[ [CALCITE-3635](https://issues.apache.org/jira/browse/CALCITE-3635)\] Supports hint option as string or numeric literal
- \[ [CALCITE-3525](https://issues.apache.org/jira/browse/CALCITE-3525)\] `RexSimplify`: eliminate redundant rex calls in OR
- \[ [CALCITE-3620](https://issues.apache.org/jira/browse/CALCITE-3620)\] Remove implicit lateral operator for temporal table join
- \[ [CALCITE-3387](https://issues.apache.org/jira/browse/CALCITE-3387)\] Query with GROUP BY and JOIN … USING wrongly fails with “Column DEPTNO is ambiguous” error
- \[ [CALCITE-3604](https://issues.apache.org/jira/browse/CALCITE-3604)\] Fixing `SqlXmlFunctionsTest` locale (ritesh-kapoor)
- \[ [CALCITE-3608](https://issues.apache.org/jira/browse/CALCITE-3608)\] Promote `RelOptUtil.createCastRel` to not create new projection if the input rel is already a project
- \[ [CALCITE-3603](https://issues.apache.org/jira/browse/CALCITE-3603)\] `SqlLateralOperator`’s unparse add additional keyword `LATERAL` when the inner operator is `SqlSnapshot`
- \[ [CALCITE-3599](https://issues.apache.org/jira/browse/CALCITE-3599)\] Override toString() of `RexRangeRef` to avoid null string
- \[ [CALCITE-3598](https://issues.apache.org/jira/browse/CALCITE-3598)\] `EnumerableTableScan`: wrong `JavaRowFormat` for elementType String
- \[ [CALCITE-3575](https://issues.apache.org/jira/browse/CALCITE-3575)\] IndexOutOfBoundsException when converting sql to rel
- \[ [CALCITE-3462](https://issues.apache.org/jira/browse/CALCITE-3462)\] Add projectExcept method in `RelBuilder` for projecting out expressions
- \[ [CALCITE-3535](https://issues.apache.org/jira/browse/CALCITE-3535)\] `EnumerableJoinRule`: remove unnecessary `Filter` on top of `INNER` Join
- \[ [CALCITE-3520](https://issues.apache.org/jira/browse/CALCITE-3520)\] Type cast from primitive to box is not correct (DonnyZone)
- \[ [CALCITE-3481](https://issues.apache.org/jira/browse/CALCITE-3481)\] Support convert `TableFunctionScan` to `SqlNode` (Wang Yanlin)
- \[ [CALCITE-3565](https://issues.apache.org/jira/browse/CALCITE-3565)\] Explicitly cast assignable operand types to decimal for udf (DonnyZone)
- \[ [CALCITE-3547](https://issues.apache.org/jira/browse/CALCITE-3547)\] SqlValidatorException because Planner cannot find UDFs added to schema (Chenxiao Mao)
- \[ [CALCITE-3246](https://issues.apache.org/jira/browse/CALCITE-3246)\] NullPointerException while deserializing udf operator (Wang Yanlin)
- \[ [CALCITE-3429](https://issues.apache.org/jira/browse/CALCITE-3429)\] AssertionError for user-defined table function with map argument (Wang Yanlin)
- \[ [CALCITE-3560](https://issues.apache.org/jira/browse/CALCITE-3560)\] Additional calcite.util.Source implementation for generic text source (eg. CharSource)
- \[ [CALCITE-3550](https://issues.apache.org/jira/browse/CALCITE-3550)\] Make `SqlTypeAssignmentRules` conversion mapping pluggable
- \[ [CALCITE-3546](https://issues.apache.org/jira/browse/CALCITE-3546)\] Improve `EnumerableDefaults` nested loop join
Provide a new implementation of nested loop join that, unlike the existing one, does not
require to build the complete result as a list before returning it. Instead, it iterates
through the outer and inner enumerables and returns the results step by step.
- \[ [CALCITE-3281](https://issues.apache.org/jira/browse/CALCITE-3281)\] Support mixed Primitive types for `BinaryExpression` evaluate method (Wang Yanlin)
- \[ [CALCITE-3561](https://issues.apache.org/jira/browse/CALCITE-3561)\] Support using unnest in `Interpreter` (Wang Yanlin)
- \[ [CALCITE-3566](https://issues.apache.org/jira/browse/CALCITE-3566)\] `EnumerableIntersect` and `EnumerableMinus` convert to Logical (xzh\_dz)
- \[ [CALCITE-3567](https://issues.apache.org/jira/browse/CALCITE-3567)\] Unnest support Map wrapped with `RecordType` (Wang Yanlin)
- \[ [CALCITE-3569](https://issues.apache.org/jira/browse/CALCITE-3569)\] IndexOutOfBoundsException when pushing simplified filter to view
- \[ [CALCITE-3536](https://issues.apache.org/jira/browse/CALCITE-3536)\] NPE when executing plan with `Coalesce` due to wrong NullAs strategy (Jin Xing)
- \[ [CALCITE-3355](https://issues.apache.org/jira/browse/CALCITE-3355)\] Deduce whether `CASE` and `COALESCE` may produce NULL values
- \[ [CALCITE-3473](https://issues.apache.org/jira/browse/CALCITE-3473)\] Getting unique result for table scan should contain key column(s) (Wang Yanlin)
- \[ [CALCITE-3544](https://issues.apache.org/jira/browse/CALCITE-3544)\] `RexSimplify` does not exploit all known predicates
- \[ [CALCITE-3353](https://issues.apache.org/jira/browse/CALCITE-3353)\] `ProjectJoinTransposeRule` caused AssertionError when creating a new Join (Wenhui Tang)
- \[ [CALCITE-3539](https://issues.apache.org/jira/browse/CALCITE-3539)\] `EnumerableDefaults#nestedLoopJoin` returns duplicates for JoinType.SEMI
- \[ [CALCITE-3521](https://issues.apache.org/jira/browse/CALCITE-3521)\] `CalciteSystemProperty` failed to load config file
- \[ [CALCITE-3512](https://issues.apache.org/jira/browse/CALCITE-3512)\] Query fails when comparing Time/TimeStamp types (DonnyZone)
- \[ [CALCITE-3534](https://issues.apache.org/jira/browse/CALCITE-3534)\] Support parse(unparse) alien system non-standard data type
- \[ [CALCITE-3454](https://issues.apache.org/jira/browse/CALCITE-3454)\] Support `Exchange`, `SetOp` and `TableModify` for builtin metadata query (xy2953396112)
- \[ [CALCITE-3527](https://issues.apache.org/jira/browse/CALCITE-3527)\] Enrich tests for SQL hints in `SqlHintsConverterTest` (Shuo Cheng)
- \[ [CALCITE-3245](https://issues.apache.org/jira/browse/CALCITE-3245)\] `CompileException` in Janino when a query contains a division between a `Double` and a `BigDecimal` (DonnyZone)
- \[ [CALCITE-3492](https://issues.apache.org/jira/browse/CALCITE-3492)\] `RexUtil.simplifyOrs()` throws exception if terms has 1 RexNode
- \[ [CALCITE-3519](https://issues.apache.org/jira/browse/CALCITE-3519)\] Use List instead of `BitSet` to keep inheritPath in RelHint (Shuo Cheng)
- \[ [CALCITE-3491](https://issues.apache.org/jira/browse/CALCITE-3491)\] Remove unused method `VolcanoPlanner.completeConversion()` (Xiening Dai)
- \[ [CALCITE-3498](https://issues.apache.org/jira/browse/CALCITE-3498)\] Unnest operation’s ordinality should be deterministic (DonnyZone)
- \[ [CALCITE-3494](https://issues.apache.org/jira/browse/CALCITE-3494)\] Support decimal type aggregate in Interpreter (Wang Yanlin)
- \[ [CALCITE-3503](https://issues.apache.org/jira/browse/CALCITE-3503)\] NPE at `VolcanoPlanner#isValid` when DEBUG is enabled (Xiening Dai)
- \[ [CALCITE-3448](https://issues.apache.org/jira/browse/CALCITE-3448)\] `AggregateOnCalcToAggUnifyRule` may ignore Project incorrectly (Jin Xing)
- \[ [CALCITE-3476](https://issues.apache.org/jira/browse/CALCITE-3476)\] `ParameterScope` should override resolveColumn interface (Jark Wu)
- \[ [CALCITE-3474](https://issues.apache.org/jira/browse/CALCITE-3474)\] NullPointerException in `SqlSimpleParser` toke.s.equals() (Xiucheng Qu)
- \[ [CALCITE-3469](https://issues.apache.org/jira/browse/CALCITE-3469)\] Wrong rel used in `SubstitutionVisitor#rowTypesAreEquivalent` (Min Dai)
- \[ [CALCITE-3487](https://issues.apache.org/jira/browse/CALCITE-3487)\] Should not hard code `RelMetadataQuery` class in VolcanoPlanner.isValid() (Xiening Dai)
- \[ [CALCITE-3482](https://issues.apache.org/jira/browse/CALCITE-3482)\] Equality of nested `ROW`s returns false for identical literal value
- \[ [CALCITE-3479](https://issues.apache.org/jira/browse/CALCITE-3479)\] Stack overflow error thrown when running join query (Xiening Dai)
- \[ [CALCITE-3435](https://issues.apache.org/jira/browse/CALCITE-3435)\] Enable decimal modulus operation to allow numeric with non-zero scale (DonnyZone)
- \[ [CALCITE-3456](https://issues.apache.org/jira/browse/CALCITE-3456)\] AssertionError throws for aggregation with same digest `IN` subqueries in same scope
- \[ [CALCITE-3408](https://issues.apache.org/jira/browse/CALCITE-3408)\] Add support for enumerable intersect/minus all (Wang Yanlin)
- \[ [CALCITE-3423](https://issues.apache.org/jira/browse/CALCITE-3423)\] Support using `CAST` operation and `BOOLEAN` type value in table macro (Wang Yanlin)
- \[ [CALCITE-3458](https://issues.apache.org/jira/browse/CALCITE-3458)\] Remove desc in `AbstractRelNode`
- \[ [CALCITE-3400](https://issues.apache.org/jira/browse/CALCITE-3400)\] Implement left/right/semi/anti/full join in interpreter (Wang Yanlin)
- \[ [CALCITE-3254](https://issues.apache.org/jira/browse/CALCITE-3254)\] Exception while deserializing with interval type or with empty partition/order key for `RexOver` (Wang Yanlin)
- \[ [CALCITE-3457](https://issues.apache.org/jira/browse/CALCITE-3457)\] `RexSimplify` incorrectly simplifies `IS NOT NULL` operator with `ITEM` call
- \[ [CALCITE-3433](https://issues.apache.org/jira/browse/CALCITE-3433)\] `EQUALS` operator between date/timestamp types returns false if the type is nullable (DonnyZone)
- \[ [CALCITE-3449](https://issues.apache.org/jira/browse/CALCITE-3449)\] Sync the table name logic from `TableScan` into the `TableModify` (dy.Zhuang)
- \[ [CALCITE-3376](https://issues.apache.org/jira/browse/CALCITE-3376)\] `VolcanoPlanner` CannotPlanException: best rel is null
even though there is an option with non-infinite cost Problem
solved via [CALCITE-2018](https://issues.apache.org/jira/browse/CALCITE-2018),
just add a unit test for this specific scenario
- \[ [CALCITE-3454](https://issues.apache.org/jira/browse/CALCITE-3454)\] Support `Exchange` in `RelMdMaxRowCount`,`RelMdMinRowCount`,`RelMdRowCount` (xy2953396112)
- \[ [CALCITE-2018](https://issues.apache.org/jira/browse/CALCITE-2018)\] Queries failed with AssertionError: rel has lower cost than best cost of subset
- \[ [CALCITE-3446](https://issues.apache.org/jira/browse/CALCITE-3446)\] Make `RelMetadataQuery` extensible
- \[ [CALCITE-3390](https://issues.apache.org/jira/browse/CALCITE-3390)\] Add `ITEM` expression to `SqlKind` and include it in the policy map for Strong (Aman Sinha)
- \[ [CALCITE-3334](https://issues.apache.org/jira/browse/CALCITE-3334)\] Refinement for Substitution-Based MV Matching (Jin Xing)
- \[ [CALCITE-3439](https://issues.apache.org/jira/browse/CALCITE-3439)\] Support `Intersect` and `Minus` in `RelMdPredicates` (Jin Xing)
- \[ [CALCITE-3451](https://issues.apache.org/jira/browse/CALCITE-3451)\] Support `TableModify` in `RelMdNodeTypes` (xy2953396113)
- \[ [CALCITE-3444](https://issues.apache.org/jira/browse/CALCITE-3444)\] Upgrade SQLLine to 1.9.0, and solve “Class path contains multiple SLF4J bindings” problem
- \[ [CALCITE-3436](https://issues.apache.org/jira/browse/CALCITE-3436)\] In `CalciteConnectionConfigImpl`, add isSet and unset methods (Ryan Fu)
- \[ [CALCITE-3440](https://issues.apache.org/jira/browse/CALCITE-3440)\] `RelToSqlConverter` does not properly alias ambiguous `ORDER BY`
- \[ [CALCITE-3441](https://issues.apache.org/jira/browse/CALCITE-3441)\] Remove `SqlTypeExplicitPrecedenceList.COMPACT_NUMERIC_TYPES` because the NULL delimiters are useless
- \[ [CALCITE-3428](https://issues.apache.org/jira/browse/CALCITE-3428)\] Refine `RelMdColumnUniqueness` for `Filter` by considering constant columns (Jin Xing)
- Add `RelBuilder.fields(ImmutableBitSet)`
- \[ [CALCITE-3424](https://issues.apache.org/jira/browse/CALCITE-3424)\] AssertionError thrown for user-defined table function with array argument (Igor Guzenko)
- \[ [CALCITE-3414](https://issues.apache.org/jira/browse/CALCITE-3414)\] In calcite-core, use RexToLixTranslator.convert for type conversion code generation uniformly (DonnyZone)
- \[ [CALCITE-3416](https://issues.apache.org/jira/browse/CALCITE-3416)\] SQL Dialects DEFAULTs should be more extensible
- \[ [CALCITE-3393](https://issues.apache.org/jira/browse/CALCITE-3393)\] `RelStructuredTypeFlattener`: improve support for functions with struct input (Igor Guzenko)
- \[ [CALCITE-3318](https://issues.apache.org/jira/browse/CALCITE-3318)\] Preserving `CAST` of `STRING` operand in binary comparison for BigQuery (soma-mondal)
- \[ [CALCITE-2792](https://issues.apache.org/jira/browse/CALCITE-2792)\] Stackoverflow while evaluating filter with large number of OR conditions
- \[ [CALCITE-3407](https://issues.apache.org/jira/browse/CALCITE-3407)\] Implement `MINUS` and `INTERSECT` in interpreter (Wang Yanlin)
- \[ [CALCITE-3420](https://issues.apache.org/jira/browse/CALCITE-3420)\] `NullPointerException` throws for implicit type coercion of nested `SET` operations
- \[ [CALCITE-3403](https://issues.apache.org/jira/browse/CALCITE-3403)\] `RelMetadataQuery` reuse (Jin Xing)
- \[ [CALCITE-3411](https://issues.apache.org/jira/browse/CALCITE-3411)\] Incorrect code generated for BigDecimal ConstantExpression (DonnyZone)
- \[ [CALCITE-3410](https://issues.apache.org/jira/browse/CALCITE-3410)\] Simplify `RelOptRulesTest` and `HepPlannerTest` by making test methods fluent
- \[ [CALCITE-3404](https://issues.apache.org/jira/browse/CALCITE-3404)\] In `AggregateExpandDistinctAggregatesRule`, treat all the agg expressions as distinct
if they have the same arguments
and the non-distinct expressions distinct constraints can be ignored
- \[ [CALCITE-3382](https://issues.apache.org/jira/browse/CALCITE-3382)\] Hard-wire the `TUMBLE` grouping function into SQL parser (Rui Wang)
- \[ [CALCITE-3396](https://issues.apache.org/jira/browse/CALCITE-3396)\] Materialized view matches unexpectedly for `UNION` with different ‘all’ property (Jin Xing)
- \[ [CALCITE-3379](https://issues.apache.org/jira/browse/CALCITE-3379)\] Support expand `STRING` column expression of table during sql-to-rel conversion
- \[ [CALCITE-3397](https://issues.apache.org/jira/browse/CALCITE-3397)\] AssertionError for interpretering multiset value (Wang Yanlin)
- \[ [CALCITE-3383](https://issues.apache.org/jira/browse/CALCITE-3383)\] Plural time units
- Re-format and re-organize config.fmpp files that customize the SQL parser
- \[ [CALCITE-3392](https://issues.apache.org/jira/browse/CALCITE-3392)\] Column expression in DDL should be validated before converting to RexNode
- \[ [CALCITE-3330](https://issues.apache.org/jira/browse/CALCITE-3330)\] Use breadth first approach for propagating cost improvements
- \[ [CALCITE-3386](https://issues.apache.org/jira/browse/CALCITE-3386)\] CyclicMetadataException singleton instance causes confusion when debugging (Zuozhi Wang)
- \[ [CALCITE-3389](https://issues.apache.org/jira/browse/CALCITE-3389)\] Test may fail if HashSet iterates in different order (contextshuffling)
- \[ [CALCITE-3361](https://issues.apache.org/jira/browse/CALCITE-3361)\] Add ‘lenientOperatorLookup’ connection property
- \[ [CALCITE-3347](https://issues.apache.org/jira/browse/CALCITE-3347)\] IndexOutOfBoundsException in `FixNullabilityShuttle` when using `FilterIntoJoinRule` (Wang Yanlin, Shuming Li)
- \[ [CALCITE-3374](https://issues.apache.org/jira/browse/CALCITE-3374)\] Error format check result for explain plan as json (Wang Yanlin)
- \[ [CALCITE-3363](https://issues.apache.org/jira/browse/CALCITE-3363)\] `JoinUnionTransposeRule.RIGHT_UNION` should not match `SEMI`/`ANTI` Join (Jin Xing)
- \[ [CALCITE-3369](https://issues.apache.org/jira/browse/CALCITE-3369)\] In `LatticeSuggester`, recommend lattices based on `UNION` queries
- \[ [CALCITE-3365](https://issues.apache.org/jira/browse/CALCITE-3365)\] Don’t require use of `JdbcSchema` in `QuerySqlStatisticProvider` (Lindsey Meyer)
- \[ [CALCITE-3239](https://issues.apache.org/jira/browse/CALCITE-3239)\] `Calc#accept(RexShuttle shuttle)` does not update rowType. (Jin Xing)
- \[ [CALCITE-3288](https://issues.apache.org/jira/browse/CALCITE-3288)\] In `ConstantExpression` support `SET` literals (xy2953396112)
- \[ [CALCITE-1178](https://issues.apache.org/jira/browse/CALCITE-1178)\] Allow `SqlBetweenOperator` to compare `DATE` and `TIMESTAMP`
- \[ [CALCITE-3348](https://issues.apache.org/jira/browse/CALCITE-3348)\] AssertionError while determining distribution of Calc (Wang Yanlin)
- \[ [CALCITE-3287](https://issues.apache.org/jira/browse/CALCITE-3287)\] `Union` in `RelMdRowCount.java` doesn’t take into account ‘union all’ (Hong Shen)
- \[ [CALCITE-3357](https://issues.apache.org/jira/browse/CALCITE-3357)\] `Trivial` null checking in `RelSet#addAbstractConverters` (Jin Xing)
- \[ [CALCITE-3286](https://issues.apache.org/jira/browse/CALCITE-3286)\] In `LatticeSuggester`, allow join conditions that use expressions
- \[ [CALCITE-3360](https://issues.apache.org/jira/browse/CALCITE-3360)\] `SqlValidator` throws NPE for unregistered function without implicit type coercion
- \[ [CALCITE-3316](https://issues.apache.org/jira/browse/CALCITE-3316)\] Exception while deserializing `LogicalCorrelate` from json string (Wang Yanlin)
- \[ [CALCITE-3317](https://issues.apache.org/jira/browse/CALCITE-3317)\] Add a public constructor for `LogicalCalc` with RelInput type parameter (Wang Yanlin)
- \[ [CALCITE-3319](https://issues.apache.org/jira/browse/CALCITE-3319)\] AssertionError when reducing decimals (Wang Yanlin)
- \[ [CALCITE-3331](https://issues.apache.org/jira/browse/CALCITE-3331)\] Support implicit type cast for operators that use single operand family checker

##### Adapters [Permalink](https://calcite.apache.org/docs/history.html\#adapters-1-22-0 "Permalink")

- \[ [CALCITE-3751](https://issues.apache.org/jira/browse/CALCITE-3751)\] JDBC adapter generates SQL with wrong aliases in `GROUP BY` … `ORDER BY` query
- \[ [CALCITE-3593](https://issues.apache.org/jira/browse/CALCITE-3593)\] JDBC adapter generates incorrect `HAVING` clause for BigQuery (Jin Xing)
- \[ [CALCITE-3466](https://issues.apache.org/jira/browse/CALCITE-3466)\] JDBC adapter incorrectly drops `GROUP BY` clause of sub-query (Wang Weidong)
- \[ [CALCITE-3154](https://issues.apache.org/jira/browse/CALCITE-3154)\] `RelToSqlConverter` generates `NULLS LAST` and `NULLS FIRST` wrongly
when using `MysqlSqlDialect` to convert `RexOver` to sql (Wenhui Tang)
- \[ [CALCITE-2672](https://issues.apache.org/jira/browse/CALCITE-2672)\] Qualifying the common column should not be allowed in Oracle dialect and SQL standard
- \[ [CALCITE-3568](https://issues.apache.org/jira/browse/CALCITE-3568)\] BigQuery, Hive, Spark SQL dialects do not support nested aggregates (Divyanshu Srivastava)
- \[ [CALCITE-3381](https://issues.apache.org/jira/browse/CALCITE-3381)\] In JDBC adapter, when using BigQuery dialect, converts SQL types to BigQuery types correctly(Rui Wang)
- \[ [CALCITE-3381](https://issues.apache.org/jira/browse/CALCITE-3381)\] Unparse to correct BigQuery integral syntax: `INTERVAL` int64 time\_unit.
Range time unit is not supported yet by BigQuery (amaliujia)
- \[ [CALCITE-3486](https://issues.apache.org/jira/browse/CALCITE-3486)\] In JDBC adapter, when generating `ROW`value expression,
generates the `ROW` keyword only if the dialect allows it (quxiucheng)
- Use proper ClassLoader in SparkHandlerImpl
- \[ [CALCITE-3381](https://issues.apache.org/jira/browse/CALCITE-3381)\] When using BigQuery dialect, Rel2SQL converter converts SQL types to BigQuery types (part2) (Rui Wang)
- \[ [CALCITE-3475](https://issues.apache.org/jira/browse/CALCITE-3475)\] JDBC adapter generates invalid SQL for `UNION ALL` on BigQuery (Steven Talbot)
- \[ [CALCITE-3370](https://issues.apache.org/jira/browse/CALCITE-3370)\] In JDBC adapter for Microsoft SQL Server, emulate `NULLS FIRST` using `CASE` expression (Justin Swett)
- \[ [CALCITE-3344](https://issues.apache.org/jira/browse/CALCITE-3344)\] In JDBC adapter, generate `SELECT TOP(n)` for MSSQL 2008 and earlier, and for `Sybase` ASE
- \[ [CALCITE-3300](https://issues.apache.org/jira/browse/CALCITE-3300)\] In JDBC adapter, when generating SQL for count star, generates the star argument of the call (Wang Weidong)
- \[ [CALCITE-3247](https://issues.apache.org/jira/browse/CALCITE-3247)\] In JDBC adapter, when generating SQL for Hive, transform `SUBSTRING` function to correct format (Jacky Woo)
- \[ [CALCITE-3282](https://issues.apache.org/jira/browse/CALCITE-3282)\] In JDBC adapter, when generating SQL for Hive, generate `INTEGER` type as `INT` (huangfeng)
- \[ [CALCITE-3335](https://issues.apache.org/jira/browse/CALCITE-3335)\] In ElasticSearch adapter, introduce configuration parameter “hosts” which deprecates previous “coordinates” (Shikha Somani)

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-22-0 "Permalink")

- Stop building zip archives when building using gradle
- \[ [CALCITE-2442](https://issues.apache.org/jira/browse/CALCITE-2442)\] Remove .toDelete cassandra temp folder on Windows after tests
- Update Gradle test output formatting
- Color test results in Gradle output
- In JDBC adapter tests that check generated SQL, extract SQL from string literals in generated Java
- Refactor MaterializationTest to use a fluent API
- Allow `CREATE TABLE ... AS SELECT ...` in Quidem tests
- Increase test coverage for regular CI jobs: move @Tag(slow) annotations to test methods
- Use concurrent test execution by default
- Add gradle task ‘aggregateJavadocIncludingTests’ that builds javadoc for both main and test
- \[ [CALCITE-3654](https://issues.apache.org/jira/browse/CALCITE-3654)\] Use single Elasticsearch instance for all elasticsearch tests
- \[ [CALCITE-3637](https://issues.apache.org/jira/browse/CALCITE-3637)\] Update linq4j tests upgrade from junit4 to junit5 (Qianjin Xu)
- \[ [CALCITE-3623](https://issues.apache.org/jira/browse/CALCITE-3623)\] Replace Spotless with Autostyle
- \[ [CALCITE-3622](https://issues.apache.org/jira/browse/CALCITE-3622)\] Update geode tests upgrade from junit4 to junit5 (Qianjin Xu)
- \[ [CALCITE-3601](https://issues.apache.org/jira/browse/CALCITE-3601)\] Update elasticsearch tests upgrade from junit4 to junit5 (Qianjin Xu)
- \[ [CALCITE-3625](https://issues.apache.org/jira/browse/CALCITE-3625)\] Update mongo tests upgrade from junit4 to junit5 (Qianjin Xu)
- Move PGP signing to com.github.vlsi.stage-vote-release Gradle plugin
- \[ [CALCITE-3595](https://issues.apache.org/jira/browse/CALCITE-3595)\] Test infrastructure overwrites reference log with wrong results (Wang Yanlin)
- \[ [CALCITE-3559](https://issues.apache.org/jira/browse/CALCITE-3559)\] Drop `HydromaticFileSetCheck`, upgrade Checkstyle 7.8.2 → 8.27
- \[ [CALCITE-3540](https://issues.apache.org/jira/browse/CALCITE-3540)\] FoodmartTest produces many warnings due to incorrect use of CalciteAssert.pooled()
- \[ [CALCITE-3548](https://issues.apache.org/jira/browse/CALCITE-3548)\] unlock ./gradlew :ubenchmark:jmh to run benchmarks
- \[ [CALCITE-3327](https://issues.apache.org/jira/browse/CALCITE-3327)\] Simplify `SqlValidatorTest` and `SqlParserTest` by making test methods fluent
- \[ [CALCITE-2905](https://issues.apache.org/jira/browse/CALCITE-2905)\] Migrate build scripts to Gradle
- \[ [CALCITE-2457](https://issues.apache.org/jira/browse/CALCITE-2457)\] JUnit 4 → 5: trivial renames
- \[ [CALCITE-2457](https://issues.apache.org/jira/browse/CALCITE-2457)\] Configure build to automatically replace common JUnit4 classes with JUnit5
- Build script: instantiate sqllineClasspath only when buildSqllineClasspath is used
- GitHub Actions: actions/checkout@master → v1.1.0 to avoid unexpected failures
- \[ [CALCITE-3141](https://issues.apache.org/jira/browse/CALCITE-3141)\] Slow tests are not run in continuous integration
- \[ [CALCITE-3140](https://issues.apache.org/jira/browse/CALCITE-3140)\] Multiple failures when executing slow tests
- Reduce FoodmartQuery heap consumption by ignoring rows/columns as they are never used in tests
- Add ‘./gradlew style’ task to apply code format and report violations
- \[ [CALCITE-2905](https://issues.apache.org/jira/browse/CALCITE-2905)\] Migrate build scripts to Gradle
- \[ [CALCITE-2905](https://issues.apache.org/jira/browse/CALCITE-2905)\] Add hydromatic-resource as plain source file
- \[ [CALCITE-3457](https://issues.apache.org/jira/browse/CALCITE-3457)\] Ignore fuzzer tests due to known unsolved issue
- Improve folder detection logic in DocumentationTest
- Ignore `TpcdsLatticeSuggesterTest` because it does not work
- Use `Class#getResource` in FileReaderTest instead of hard-coding file name
- Simplify `RexProgramTest#reproducerFor3457` test
- Add shrinker for `RexProgramFuzzy` so the results are simpler to reason about
- Refactor `SqlPrettyWriterTest`, using a fluent API for invoking tests
- \[ [CALCITE-3362](https://issues.apache.org/jira/browse/CALCITE-3362)\] Add some tests for empty Lattice (Wang Yanlin)
- \[ [CALCITE-3421](https://issues.apache.org/jira/browse/CALCITE-3421)\] Reuse `RelMetadataQuery` in test suites

#### Dependency version upgrade [Permalink](https://calcite.apache.org/docs/history.html\#dependency-1-22-0 "Permalink")

- \[ [CALCITE-3818](https://issues.apache.org/jira/browse/CALCITE-3818)\] Upgrade Avatica version to 1.16.0
- Update Gradle: 6.1 → 6.1.1
- \[ [CALCITE-3742](https://issues.apache.org/jira/browse/CALCITE-3742)\] Update Gradle: 6.0.1 → 6.1
- Bump spark-core\_2.10 from 2.2.0 to 2.2.2
- \[ [CALCITE-3516](https://issues.apache.org/jira/browse/CALCITE-3516)\] Bump net.java.dev.jna:jna to 5.5.0
- \[ [CALCITE-2457](https://issues.apache.org/jira/browse/CALCITE-2457)\] Druid: JUnit4 → JUnit5
- Bump geode-core from 1.9.2 to 1.10.0
- \[ [CALCITE-3502](https://issues.apache.org/jira/browse/CALCITE-3502)\] Upgrade Geode dependency 1.6.0 → 1.9.2
- Bump jackson-databind from 2.9.9.3 to 2.9.10.1

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-22-0 "Permalink")

- Site: Update IntelliJ instructions with suggested and problematic versions
- Site: Switch PMC Chair to Stamatis Zampetakis
- Site: Add two links with useful information about Gradle (Rui Wang)
- Site: Update homepage of Stamatis Zampetakis
- Site: Move “Fast federated SQL with Apache Calcite” in talks section and add video link
- Site: Add Haisheng Yuan as PMC
- Site: Append ‘(FirstName LastName)’ to commit message example in contributing section
- Site: Add Danny Chan as PMC
- \[ [CALCITE-3445](https://issues.apache.org/jira/browse/CALCITE-3445)\] In web site, automatically redirect http to https
- \[ [CALCITE-3391](https://issues.apache.org/jira/browse/CALCITE-3391)\] Insecure pages warning on Chrome
- Site: Update upcoming talks section for ApacheCon Europe 2019
- Site: Change GitHub avatar links to https

## [1.21.0](https://github.com/apache/calcite/releases/tag/calcite-1.21.0) / 2019-09-11 [Permalink](https://calcite.apache.org/docs/history.html\#v1-21-0 "Permalink")

This release comes two months after 1.20.0. It includes more than 100 resolved
issues, comprising a large number of new features as well as general improvements
and bug-fixes.

It is worth highlighting that Calcite now:

- supports implicit type coercion in various contexts
( [CALCITE-2302](https://issues.apache.org/jira/browse/CALCITE-2302));
- allows transformations of Pig Latin scripts into algebraic plans
( [CALCITE-3122](https://issues.apache.org/jira/browse/CALCITE-3122));
- provides an implementation for the main features of `MATCH_RECOGNIZE` in the
`Enumerable` convention
( [CALCITE-1935](https://issues.apache.org/jira/browse/CALCITE-1935));
- supports correlated `ANY`/`SOME`/`ALL` sub-queries
( [CALCITE-3031](https://issues.apache.org/jira/browse/CALCITE-3031));
- introduces anonymous types based on `ROW`, `ARRAY`, and nested collection
( [CALCITE-3233](https://issues.apache.org/jira/browse/CALCITE-3233),
[CALCITE-3231](https://issues.apache.org/jira/browse/CALCITE-3231),
[CALCITE-3250](https://issues.apache.org/jira/browse/CALCITE-3250));
- brings new join algorithms for the `Enumerable` convention
( [CALCITE-2979](https://issues.apache.org/jira/browse/CALCITE-2979),
[CALCITE-2973](https://issues.apache.org/jira/browse/CALCITE-2973),
[CALCITE-3284](https://issues.apache.org/jira/browse/CALCITE-3284)).

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13 and OpenJDK 8, 9, 10, 11, 12, 13;
Guava versions 19.0 to 27.1-jre;
Apache Druid version 0.14.0-incubating;
other software versions as specified in `pom.xml`.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-21-0 "Permalink")

- Core parser config.fmpp#dataTypeParserMethods should return `SqlTypeNameSpec`
instead of `SqlIdentifier`.
- The description of converter rules has slightly changed
( [CALCITE-3115](https://issues.apache.org/jira/browse/CALCITE-3115)).
In some rare cases this may lead to a `Rule description ... is not valid`
exception. The exception can easily disappear by changing the name of the
`Convention` which causes the problem.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-21-0 "Permalink")

- \[ [CALCITE-2973](https://issues.apache.org/jira/browse/CALCITE-2973)\]
\[ [CALCITE-3284](https://issues.apache.org/jira/browse/CALCITE-3284)\]
Allow joins (hash, semi, anti) that have equi conditions to be executed using a
hash join algorithm (Lai Zhou)
- \[ [CALCITE-2302](https://issues.apache.org/jira/browse/CALCITE-2302)\]
Implicit type cast support
- \[ [CALCITE-3122](https://issues.apache.org/jira/browse/CALCITE-3122)\]
Convert Pig Latin scripts into Calcite relational algebra and Calcite SQL
(Khai Tran)
- \[ [CALCITE-2979](https://issues.apache.org/jira/browse/CALCITE-2979)\]
Add a block-based nested loop join algorithm (Khawla Mouhoubi)
- \[ [CALCITE-3263](https://issues.apache.org/jira/browse/CALCITE-3263)\]
Add `MD5`, `SHA1` SQL functions (Shuming Li)
- \[ [CALCITE-3204](https://issues.apache.org/jira/browse/CALCITE-3204)\]
Implement `jps` command for OS adapter (Qianjin Xu)
- \[ [CALCITE-3260](https://issues.apache.org/jira/browse/CALCITE-3260)\]
Add Expressions.evaluate(Node), a public API for evaluating linq4j expressions
(Wang Yanlin)
- \[ [CALCITE-3280](https://issues.apache.org/jira/browse/CALCITE-3280)\]
Add `REGEXP_REPLACE` function in Oracle, MySQL libraries (Shuming Li)
- \[ [CALCITE-3111](https://issues.apache.org/jira/browse/CALCITE-3111)\]
Add `RelBuilder.correlate` method, and allow custom implementations of
`Correlate` in `RelDecorrelator` (Juhwan Kim)
- \[ [CALCITE-3252](https://issues.apache.org/jira/browse/CALCITE-3252)\]
Add `CONVERT_TIMEZONE`, `TO_DATE` and `TO_TIMESTAMP` non-standard SQL functions
(Lindsey Meyer)
- \[ [CALCITE-3235](https://issues.apache.org/jira/browse/CALCITE-3235)\]
Add `CONCAT` function for Redshift (Ryan Fu)
- \[ [CALCITE-3250](https://issues.apache.org/jira/browse/CALCITE-3250)\]
Support nested collection type for `SqlDataTypeSpec`
- \[ [CALCITE-1935](https://issues.apache.org/jira/browse/CALCITE-1935)\]
Implement `MATCH_RECOGNIZE` (Julian Feinauer, Zhiqiang-He)
- \[ [CALCITE-2843](https://issues.apache.org/jira/browse/CALCITE-2843)\]
Support Postgres cast operator (`::`) (Muhammad Gelbana)
- \[ [CALCITE-3233](https://issues.apache.org/jira/browse/CALCITE-3233)\]
Support `ROW` type for `SqlDataTypeSpec`
- \[ [CALCITE-3231](https://issues.apache.org/jira/browse/CALCITE-3231)\]
Support `ARRAY` type for `SqlDataTypeSpec`
- \[ [CALCITE-2624](https://issues.apache.org/jira/browse/CALCITE-2624)\]
Add a rule to copy a sort below a join operator (Khawla Mouhoubi)
- \[ [CALCITE-3031](https://issues.apache.org/jira/browse/CALCITE-3031)\]
Support for correlated `ANY`/`SOME`/`ALL` sub-query (Vineet Garg)
- \[ [CALCITE-2510](https://issues.apache.org/jira/browse/CALCITE-2510)\]
Implement `CHR` function (Sergey Tsvetkov, Chunwei Lei)
- \[ [CALCITE-3176](https://issues.apache.org/jira/browse/CALCITE-3176)\]
File adapter for parsing JSON files
- \[ [CALCITE-3144](https://issues.apache.org/jira/browse/CALCITE-3144)\]
Add rule, `AggregateCaseToFilterRule`, that converts `SUM(CASE WHEN b THEN x
END)` to `SUM(x) FILTER (WHERE b)`
- \[ [CALCITE-2995](https://issues.apache.org/jira/browse/CALCITE-2995)\]
Implement `DAYNAME`，`MONTHNAME` functions; add `locale` connection property
(xuqianjin)
- \[ [CALCITE-2460](https://issues.apache.org/jira/browse/CALCITE-2460)\]
\[CALCITE-2459\] Add `TO_BASE64`, `FROM_BASE64` SQL functions (Wenhui Tang)
- \[ [CALCITE-3063](https://issues.apache.org/jira/browse/CALCITE-3063)\]
Parse and process Postgres posix regular expressions

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-21-0 "Permalink")

- \[ [CALCITE-3321](https://issues.apache.org/jira/browse/CALCITE-3321)\]
Set casing rules for BigQuery SQL dialect (Lindsey Meyer)
- \[ [CALCITE-3115](https://issues.apache.org/jira/browse/CALCITE-3115)\]
Cannot add `JdbcRule` instances that have different `JdbcConvention` to same
`VolcanoPlanner`’s `RuleSet` (Wenhui Tang, Igor Guzenko)
- \[ [CALCITE-3309](https://issues.apache.org/jira/browse/CALCITE-3309)\]
Refactor `generatePredicate` method from `EnumerableNestedLoopJoin`,
`EnumerableHashJoin`, and `EnumerableBatchNestedLoopJoin` into a single location
- \[ [CALCITE-3310](https://issues.apache.org/jira/browse/CALCITE-3310)\]
Approximate and exact aggregate calls are recognized as the same during
SQL-to-RelNode conversion
- \[ [CALCITE-3292](https://issues.apache.org/jira/browse/CALCITE-3292)\]
SqlToRelConverter#substituteSubQuery fails with NullPointerException when
converting `SqlUpdate` (Jin Xing)
- \[ [CALCITE-3297](https://issues.apache.org/jira/browse/CALCITE-3297)\]
`PigToSqlAggregateRule` should be applied on multi-set projection to produce an
optimal plan (Igor Guzenko)
- \[ [CALCITE-3295](https://issues.apache.org/jira/browse/CALCITE-3295)\]
Add aggregate call name in serialized json string for `RelNode` (Wang Yanlin)
- \[ [CALCITE-3296](https://issues.apache.org/jira/browse/CALCITE-3296)\]
Decorrelator shouldn’t give empty value when fetch and offset values are null
in `Sort` rel (Juhwan Kim)
- \[ [CALCITE-3283](https://issues.apache.org/jira/browse/CALCITE-3283)\]
`RelSubset` does not contain its best `RelNode` (Xiening Dai)
- \[ [CALCITE-3210](https://issues.apache.org/jira/browse/CALCITE-3210)\]
JDBC adapter should generate `CAST(NULL AS type)` rather than `NULL`
conditionally (Wang Weidong)
- \[ [CALCITE-3220](https://issues.apache.org/jira/browse/CALCITE-3220)\]
JDBC adapter now transforms `TRIM` to `TRIM`, `LTRIM` or `RTRIM` when target
is Hive (Jacky Woo)
- \[ [CALCITE-3228](https://issues.apache.org/jira/browse/CALCITE-3228)\]
Error while applying rule `ProjectScanRule`: interpreter
- \[ [CALCITE-3223](https://issues.apache.org/jira/browse/CALCITE-3223)\]
Materialized view fails to match when there is non-`RexInputRef` in the
projects (Jin Xing)
- \[ [CALCITE-3257](https://issues.apache.org/jira/browse/CALCITE-3257)\]
`RelMetadataQuery` cache is not invalidated when log trace is enabled
(Xiening Dai)
- \[ [CALCITE-3138](https://issues.apache.org/jira/browse/CALCITE-3138)\]
`RelStructuredTypeFlattener` doesn’t restructure `ROW` type fields (Igor Guzenko)
- \[ [CALCITE-3251](https://issues.apache.org/jira/browse/CALCITE-3251)\]
`BinaryExpression` evaluate method support full numeric types in `Primitive`
(xy2953396112)
- \[ [CALCITE-3259](https://issues.apache.org/jira/browse/CALCITE-3259)\]
Align ‘Property’ in the serialized XML string of `RelXmlWriter` (Wang Yanlin)
- \[ [CALCITE-3167](https://issues.apache.org/jira/browse/CALCITE-3167)\]
Make `equals` and `hashCode` methods final in `AbstractRelNode`, and remove
overriding methods in `EnumerableTableScan` (Jin Xing)
- \[ [CALCITE-3089](https://issues.apache.org/jira/browse/CALCITE-3089)\]
Deprecate `EquiJoin`
- \[ [CALCITE-3267](https://issues.apache.org/jira/browse/CALCITE-3267)\]
Remove method `SqlDataTypeSpec#deriveType(RelDataTypefactory)`
- \[ [CALCITE-3214](https://issues.apache.org/jira/browse/CALCITE-3214)\]
Add `UnionToUnionRule` for materialization matching (refine rule name) (Jin Xing)
- \[ [CALCITE-3214](https://issues.apache.org/jira/browse/CALCITE-3214)\]
Add `UnionToUnionRule` for materialization matching (Jin Xing)
- \[ [CALCITE-3249](https://issues.apache.org/jira/browse/CALCITE-3249)\]
\`Substitution#getRexShuttle does not consider RexLiteral (Jin Xing)
- \[ [CALCITE-3229](https://issues.apache.org/jira/browse/CALCITE-3229)\]
`UnsupportedOperationException` for `UPDATE` with `IN` query
- \[ [CALCITE-3236](https://issues.apache.org/jira/browse/CALCITE-3236)\]
Handle issues found in static code analysis (DonnyZone)
- \[ [CALCITE-3238](https://issues.apache.org/jira/browse/CALCITE-3238)\]
Support Time Zone suffix of DateTime types for `SqlDataTypeSpec`
- \[ [CALCITE-3159](https://issues.apache.org/jira/browse/CALCITE-3159)\]
Remove `DISTINCT` flag from calls to `MIN`, `MAX`, `BIT_OR`, `BIT_AND`
aggregate functions (xuqianjin)
- \[ [CALCITE-3237](https://issues.apache.org/jira/browse/CALCITE-3237)\]
`IndexOutOfBoundsException` when generating deeply nested Java code from linq4j
(Sahith Nallapareddy)
- \[ [CALCITE-3234](https://issues.apache.org/jira/browse/CALCITE-3234)\]
For boolean properties, empty string should mean “true”
- \[ [CALCITE-3226](https://issues.apache.org/jira/browse/CALCITE-3226)\]
`RelBuilder` doesn’t keep the alias when `scan` from an expanded view (Jin Xing)
- \[ [CALCITE-3198](https://issues.apache.org/jira/browse/CALCITE-3198)\]
Enhance `RexSimplify` to handle `(x <> a or x <> b)`
- \[ [CALCITE-3101](https://issues.apache.org/jira/browse/CALCITE-3101)\]
Don’t push non-equi join conditions into `Project` below `Join`
- \[ [CALCITE-3227](https://issues.apache.org/jira/browse/CALCITE-3227)\]
`IndexOutOfBoundsException` when checking candidate parent match’s input
ordinal in `VolcanoRuleCall`
- \[ [CALCITE-3177](https://issues.apache.org/jira/browse/CALCITE-3177)\]
Ensure correct deserialization of relational algebra
- \[ [CALCITE-3218](https://issues.apache.org/jira/browse/CALCITE-3218)\]
Syntax error while parsing `DATEADD` function (which is valid on Redshift)
(Lindsey Meyer)
- Deprecate `RexBuilder.constantNull()`, because it produces untyped `NULL`
literals that make planning difficult
- \[ [CALCITE-3191](https://issues.apache.org/jira/browse/CALCITE-3191)\]
In JDBC adapter for MySQL, implement `Values` by generating `SELECT` without
`FROM`
- \[ [CALCITE-3147](https://issues.apache.org/jira/browse/CALCITE-3147)\]
In JDBC adapter, accommodate the idiosyncrasies of how BigQuery (standard SQL)
quotes character literals and identifiers
- \[ [CALCITE-3131](https://issues.apache.org/jira/browse/CALCITE-3131)\]
In `LatticeSuggester`, record whether columns are used as “dimensions” or
“measures”
- \[ [CALCITE-3175](https://issues.apache.org/jira/browse/CALCITE-3175)\]
`AssertionError` while serializing to JSON a `RexLiteral` with `Enum` type
(Wang Yanlin)
- \[ [CALCITE-3225](https://issues.apache.org/jira/browse/CALCITE-3225)\]
`JoinToMultiJoinRule` should not match semi- or anti-LogicalJoin
- \[ [CALCITE-3215](https://issues.apache.org/jira/browse/CALCITE-3215)\]
Simplification may have not fully simplified IS `NOT NULL` expressions
- \[ [CALCITE-3192](https://issues.apache.org/jira/browse/CALCITE-3192)\]
Simplification may weaken OR conditions containing inequalities
- \[ [CALCITE-3211](https://issues.apache.org/jira/browse/CALCITE-3211)\]
List of `MutableRel` may fail to be identified by `SubstitutionVisitor` during
matching (Jin Xing)
- \[ [CALCITE-3207](https://issues.apache.org/jira/browse/CALCITE-3207)\]
Fail to convert `Join` with `LIKE` condition to SQL statement (wojustme)
- \[ [CALCITE-2496](https://issues.apache.org/jira/browse/CALCITE-2496)\]
Return 0 in case of `EXTRACT(MILLI/MICRO/NANOSECOND FROM date)`
(Sergey Nuyanzin, Chunwei Lei)
- \[ [CALCITE-3109](https://issues.apache.org/jira/browse/CALCITE-3109)\]
Improvements on algebraic operators to express recursive queries (`RepeatUnion`
and `TableSpool`)
- \[ [CALCITE-3209](https://issues.apache.org/jira/browse/CALCITE-3209)\]
When calling `MutableMultiRel.setInput`, exception thrown (Jin Xing)
- \[ [CALCITE-3195](https://issues.apache.org/jira/browse/CALCITE-3195)\]
Handle a UDF that throws checked exceptions in the Enumerable code generator
(DonnyZone)
- \[ [CALCITE-3118](https://issues.apache.org/jira/browse/CALCITE-3118)\]
`VolcanoRuleCall` should look at `RelSubset` rather than `RelSet` when checking
child ordinal of a parent operand (Botong Huang)
- \[ [CALCITE-3201](https://issues.apache.org/jira/browse/CALCITE-3201)\]
`SqlValidator` throws exception for SQL insert target table with virtual columns
- \[ [CALCITE-3182](https://issues.apache.org/jira/browse/CALCITE-3182)\]
Trim unused fields for plan of materialized-view before matching (Jin Xing)
- \[ [CALCITE-3174](https://issues.apache.org/jira/browse/CALCITE-3174)\]
`IS NOT DISTINCT FROM` condition pushed from `Filter` to `Join` is not
collapsed (Bohdan Kazydub)
- \[ [CALCITE-3166](https://issues.apache.org/jira/browse/CALCITE-3166)\]
Make `RelBuilder` configurable
- \[ [CALCITE-3113](https://issues.apache.org/jira/browse/CALCITE-3113)\]
Equivalent `MutableAggregate`s with different row types should match with each
other (Jin Xing)
- [CALCITE-3187](https://issues.apache.org/jira/browse/CALCITE-3187):
Make decimal type inference overridable (Praveen Kumar)
- \[ [CALCITE-3145](https://issues.apache.org/jira/browse/CALCITE-3145)\]
`RelBuilder.aggregate` throws `IndexOutOfBoundsException` if `groupKey` is
non-empty and there are duplicate aggregate functions
- Change type of `SqlStdOperatorTable.GROUPING` field to public class
- \[ [CALCITE-3196](https://issues.apache.org/jira/browse/CALCITE-3196)\]
In `Frameworks`, add `interface BasePrepareAction` (a functional interface) and
deprecate `abstract class PrepareAction`
- \[ [CALCITE-3183](https://issues.apache.org/jira/browse/CALCITE-3183)\]
During field trimming, `Filter` is copied with wrong traitSet (Juhwan Kim)
- \[ [CALCITE-3189](https://issues.apache.org/jira/browse/CALCITE-3189)\]
Multiple fixes for Oracle SQL dialect
- \[ [CALCITE-3165](https://issues.apache.org/jira/browse/CALCITE-3165)\]
`Project#accept`(`RexShuttle` shuttle) does not update rowType
- \[ [CALCITE-3188](https://issues.apache.org/jira/browse/CALCITE-3188)\]
`IndexOutOfBoundsException` in `ProjectFilterTransposeRule` when executing
`SELECT COUNT`
- \[ [CALCITE-3160](https://issues.apache.org/jira/browse/CALCITE-3160)\]
Failed to materialize when the aggregate function uses group key (DonnyZone)
- \[ [CALCITE-3170](https://issues.apache.org/jira/browse/CALCITE-3170)\]
ANTI join on conditions push down generates wrong plan
- \[ [CALCITE-3169](https://issues.apache.org/jira/browse/CALCITE-3169)\]
decorrelateRel method should return when meeting `SEMI`/`ANTI` join in
`RelDecorrelator`
- \[ [CALCITE-3171](https://issues.apache.org/jira/browse/CALCITE-3171)\]
`SemiJoin` on conditions push down throws `IndexOutOfBoundsException`
- \[ [CALCITE-3172](https://issues.apache.org/jira/browse/CALCITE-3172)\]
`RelBuilder#empty` does not keep aliases
- \[ [CALCITE-3121](https://issues.apache.org/jira/browse/CALCITE-3121)\]
`VolcanoPlanner` hangs due to sub-query with dynamic star
- \[ [CALCITE-3152](https://issues.apache.org/jira/browse/CALCITE-3152)\]
Unify throws in SQL parser
- \[ [CALCITE-3125](https://issues.apache.org/jira/browse/CALCITE-3125)\]
Remove completely `class CorrelateJoinType`
- \[ [CALCITE-3133](https://issues.apache.org/jira/browse/CALCITE-3133)\]
Remove completely `class SemiJoinType`
- \[ [CALCITE-3126](https://issues.apache.org/jira/browse/CALCITE-3126)\]
Remove deprecated `SemiJoin` usage completely
- \[ [CALCITE-3146](https://issues.apache.org/jira/browse/CALCITE-3146)\]
Support the detection of nested aggregations for `JdbcAggregate` in
`SqlImplementor` (Wenhui Tang)
- \[ [CALCITE-3155](https://issues.apache.org/jira/browse/CALCITE-3155)\]
Empty `LogicalValues` can not be converted to `UNION ALL` without operands which
can not be unparsed (Musbah EL FIL)
- \[ [CALCITE-3151](https://issues.apache.org/jira/browse/CALCITE-3151)\]
RexCall’s Monotonicity is not considered in determining a Calc’s collation
- \[ [CALCITE-2801](https://issues.apache.org/jira/browse/CALCITE-2801)\]
Check input type in `AggregateUnionAggregateRule` when remove the bottom
`Aggregate` (Hequn Cheng)
- \[ [CALCITE-3149](https://issues.apache.org/jira/browse/CALCITE-3149)\]
`RelDataType` CACHE in `RelDataTypeFactoryImpl` can’t be garbage collected
- \[ [CALCITE-3060](https://issues.apache.org/jira/browse/CALCITE-3060)\]
`MutableProject` should be generated based on INVERSE\_SURJECTION mapping
(DonnyZone)
- \[ [CALCITE-3148](https://issues.apache.org/jira/browse/CALCITE-3148)\]
Validator throws `IndexOutOfBoundsException` for `SqlInsert` when source and
sink have non-equal number of fields

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-21-0 "Permalink")

- \[ [CALCITE-3322](https://issues.apache.org/jira/browse/CALCITE-3322)\]
Remove duplicate test case in `RelMetadataTest`
- \[ [CALCITE-3314](https://issues.apache.org/jira/browse/CALCITE-3314)\]
CVSS dependency-check-maven fails for calcite-pig, calcite-piglet,
calcite-spark
- \[ [CALCITE-3315](https://issues.apache.org/jira/browse/CALCITE-3315)\]
Multiple failures in Druid IT tests due to implicit casts
- \[ [CALCITE-3307](https://issues.apache.org/jira/browse/CALCITE-3307)\]
`PigRelExTest`, `PigRelOpTest` and `PigScriptTest` fail on Windows
- In `SqlFunctionsTest`, replace `assertEquals` and `assertNull` with `assertThat`
- \[ [CALCITE-3258](https://issues.apache.org/jira/browse/CALCITE-3258)\]
Upgrade jackson-databind from 2.9.9 to 2.9.9.3, and kafka-clients from 2.0.0
to 2.1.1
- \[ [CALCITE-3222](https://issues.apache.org/jira/browse/CALCITE-3222)\]
Fix code style issues introduced by \[CALCITE-3031\] (Vineet Garg)
- More compiler fixes, and cosmetic changes
- Fix compiler warnings
- Update stale tests in DruidAdapter
- Following
\[ [CALCITE-2804](https://issues.apache.org/jira/browse/CALCITE-2804)\],
fix incorrect expected Druid query in test case
`DruidAdapterIT#testCastToTimestamp` (Justin Szeluga)
- \[ [CALCITE-3153](https://issues.apache.org/jira/browse/CALCITE-3153)\]
Improve testing in `TpcdsTest` using `assertEqual` instead of printing results
- Fix javadoc error
- Fix compilation warnings after Mongo java driver upgrade
- \[ [CALCITE-3179](https://issues.apache.org/jira/browse/CALCITE-3179)\]
Bump Jackson from 2.9.8 to 2.9.9 (Fokko Driesprong)
- \[ [CALCITE-3157](https://issues.apache.org/jira/browse/CALCITE-3157)\]
Mongo java driver upgrade: 3.5.0 → 3.10.2
- \[ [CALCITE-3156](https://issues.apache.org/jira/browse/CALCITE-3156)\]
Mongo adapter. Replace fongo with Mongo Java Server for tests
- \[ [CALCITE-3168](https://issues.apache.org/jira/browse/CALCITE-3168)\]
Add test for invalid literal of SQL parser

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-21-0 "Permalink")

- \[ [CALCITE-3303](https://issues.apache.org/jira/browse/CALCITE-3303)\]
Release Calcite 1.21.0
- \[ [CALCITE-3311](https://issues.apache.org/jira/browse/CALCITE-3311)\]
Add doc to site for implicit type coercion
- \[ [CALCITE-3262](https://issues.apache.org/jira/browse/CALCITE-3262)\]
Refine doc of `SubstitutionVisitor` (Jin Xing)
- \[ [CALCITE-2835](https://issues.apache.org/jira/browse/CALCITE-2835)\]
Markdown errors on the Geode adapter page
- Site: Update Apache links on homepage to HTTPS
- Update favicon for new logo
- \[ [CALCITE-3136](https://issues.apache.org/jira/browse/CALCITE-3136)\]
Fix the default rule description of `ConverterRule` (TANG Wen-hui)
- \[ [CALCITE-3184](https://issues.apache.org/jira/browse/CALCITE-3184)\]
Add the new logo to the website
- Update example announcement
- Add committer names to 1.20.0 release notes
- Add 1.20.0 release date
- Add 1.20.0 release announcement

## [1.20.0](https://github.com/apache/calcite/releases/tag/calcite-1.20.0) / 2019-06-24 [Permalink](https://calcite.apache.org/docs/history.html\#v1-20-0 "Permalink")

This release comes three months after 1.19.0. It includes a large number of bug fixes,
and additional SQL functions. There is now also explicit support for anti-joins.
Several new operators have been added to the algebra to allow support for recursive queries.
An adapter has also been added for [Apache Kafka](https://kafka.apache.org/).

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12, 13 and OpenJDK 8, 9, 10, 11, 12, 13;
Guava versions 19.0 to 27.1-jre;
Apache Druid version 0.14.0-incubating;
other software versions as specified in `pom.xml`.

#### Breaking Changes [Permalink](https://calcite.apache.org/docs/history.html\#breaking-1-20-0 "Permalink")

- Make `EnumerableMergeJoin` extend `Join` instead of `EquiJoin`
- `Correlate` use `JoinRelType` instead of `SemiJoinType`
- Rename `EnumerableThetaJoin` to `EnumerableNestedLoopJoin`
- Rename `EnumerableJoin` to `EnumerableHashJoin`
- Remove `SemiJoinFactory` from `RelBuilder`, method `semiJoin` now returns a `LogicalJoin`
with join type `JoinRelType.SEMI` instead of a `SemiJoin`
- Rules: `SemiJoinFilterTransposeRule`, `SemiJoinJoinTransposeRule`, `SemiJoinProjectTransposeRule`
and `SemiJoinRemoveRule` match `LogicalJoin` with join type `SEMI` instead of `SemiJoin`.
- `SemiJoin`, `EnumerableSemiJoin`, `SemiJoinType` and `CorrelateJoinType`, and methods that use them,
are deprecated for quick removal in 1.21
- The Elasticsearch adapter no longer supports [Elasticsearch types](https://www.elastic.co/guide/en/elasticsearch/reference/7.0/removal-of-types.html).
Calcite table names will reflect index names in Elasticsearch (as opposed to types).
We recommend use of Elasticsearch 6.2 (or later) with Calcite.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-20-0 "Permalink")

- \[ [CALCITE-2822](https://issues.apache.org/jira/browse/CALCITE-2822)\] Allow `MultiJoin` rules with any project/filter (Siddharth Teotia)
- \[ [CALCITE-2968](https://issues.apache.org/jira/browse/CALCITE-2968)\] New `AntiJoin` relational expression
- \[ [CALCITE-2721](https://issues.apache.org/jira/browse/CALCITE-2721)\] Support parsing record-type \[DOT\] member-functions
- \[ [CALCITE-3005](https://issues.apache.org/jira/browse/CALCITE-3005)\] Implement string functions: `LEFT`, `RIGHT` (xuqianjin)
- \[ [CALCITE-2812](https://issues.apache.org/jira/browse/CALCITE-2812)\] Add algebraic operators to allow expressing recursive queries
- \[ [CALCITE-2913](https://issues.apache.org/jira/browse/CALCITE-2913)\] Adapter for Apache Kafka (Mingmin Xu)
- \[ [CALCITE-3084](https://issues.apache.org/jira/browse/CALCITE-3084)\] Implement JDBC string functions: `ASCII`, `REPEAT`, `SPACE`, `SOUNDEX`, `DIFFERENC` (pingle wang)
- \[ [CALCITE-2985](https://issues.apache.org/jira/browse/CALCITE-2985)\] Implement `JSON_STORAGE_SIZE` function (xuqianjin)
- \[ [CALCITE-2601](https://issues.apache.org/jira/browse/CALCITE-2601)\] Add `REVERSE` function (pingle wang)
- \[ [CALCITE-2712](https://issues.apache.org/jira/browse/CALCITE-2712)\] Add rule to remove null-generating side of a Join
- \[ [CALCITE-2965](https://issues.apache.org/jira/browse/CALCITE-2965)\] Implement string functions: `REPEAT`, `SPACE`, `SOUNDEX`, `DIFFERENCE`
- \[ [CALCITE-2975](https://issues.apache.org/jira/browse/CALCITE-2975)\] Implement `JSON_REMOVE` function (xuqianjin)
- \[ [CALCITE-2933](https://issues.apache.org/jira/browse/CALCITE-2933)\] Add timestamp extract for casts from timestamp type to other types
- \[ [CALCITE-3011](https://issues.apache.org/jira/browse/CALCITE-3011)\] Support left and right outer joins with `AggregateJoinTransposeRule` (Vineet Garg)
- \[ [CALCITE-2427](https://issues.apache.org/jira/browse/CALCITE-2427)\] Allow sub-queries in DML statements (Pressenna Sockalingasamy)
- \[ [CALCITE-2914](https://issues.apache.org/jira/browse/CALCITE-2914)\] Add a new statistic provider, to improve how `LatticeSuggester` deduces foreign keys
- \[ [CALCITE-2754](https://issues.apache.org/jira/browse/CALCITE-2754)\] Implement `LISTAGG` function (Sergey Nuyanzin, Chunwei Lei)
- \[ [CALCITE-1172](https://issues.apache.org/jira/browse/CALCITE-1172)\] Add rule to flatten two Aggregate operators into one
- \[ [CALCITE-2892](https://issues.apache.org/jira/browse/CALCITE-2892)\] Add the `JSON_KEYS` function (xuqianjin)
- \[ [CALCITE-883](https://issues.apache.org/jira/browse/CALCITE-883)\] Support `RESPECT NULLS`, `IGNORE NULLS` option for `LEAD`, `LAG`, `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE` functions (Chunwei Lei)
- \[ [CALCITE-2920](https://issues.apache.org/jira/browse/CALCITE-2920)\] In `RelBuilder`, add `antiJoin` method (Ruben Quesada Lopez)
- \[ [CALCITE-1515](https://issues.apache.org/jira/browse/CALCITE-1515)\] In `RelBuilder`, add `functionScan` method to create `TableFunctionScan` (Chunwei Lei)
- \[ [CALCITE-2658](https://issues.apache.org/jira/browse/CALCITE-2658)\] Add `ExchangeRemoveConstantKeysRule` that removes constant keys from `Exchange` or `SortExchange` (Chunwei Lei)
- \[ [CALCITE-2729](https://issues.apache.org/jira/browse/CALCITE-2729)\] Introducing `WindowReduceExpressionsRule` (Chunwei Lei)
- \[ [CALCITE-2808](https://issues.apache.org/jira/browse/CALCITE-2808)\] Add the `JSON_LENGTH` function (xuqianjin)
- \[ [CALCITE-589](https://issues.apache.org/jira/browse/CALCITE-589)\] Extend `unifyAggregates` method to work with Grouping Sets
- \[ [CALCITE-2908](https://issues.apache.org/jira/browse/CALCITE-2908)\] Implement SQL `LAST_DAY` function (Chunwei Lei)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-20-0 "Permalink")

- \[ [CALCITE-3119](https://issues.apache.org/jira/browse/CALCITE-3119)\] Deprecate Linq4j `CorrelateJoinType` (in favor of `JoinType`)
- \[ [CALCITE-3087](https://issues.apache.org/jira/browse/CALCITE-3087)\] `AggregateOnProjectToAggregateUnifyRule` ignores Project incorrectly when its Mapping breaks ordering (DonnyZone)
- \[ [CALCITE-2744](https://issues.apache.org/jira/browse/CALCITE-2744)\] Remove usage of deprecated API in `MockSqlOperatorTable`
- \[ [CALCITE-3123](https://issues.apache.org/jira/browse/CALCITE-3123)\] In `RelBuilder`, eliminate duplicate aggregate calls
- \[ [CALCITE-3116](https://issues.apache.org/jira/browse/CALCITE-3116)\] Upgrade to Avatica 1.15
- \[ [CALCITE-2744](https://issues.apache.org/jira/browse/CALCITE-2744)\] `RelDecorrelator` use wrong output map for `LogicalAggregate` decorrelate (godfreyhe and Danny Chan)
- \[ [CALCITE-2804](https://issues.apache.org/jira/browse/CALCITE-2804)\] Fix casting to timestamps in Druid
- \[ [CALCITE-3107](https://issues.apache.org/jira/browse/CALCITE-3107)\] Upgrade commons-dbcp2 from 2.5.0 to 2.6.0 (Fokko Driesprong)
- \[ [CALCITE-3106](https://issues.apache.org/jira/browse/CALCITE-3106)\] Upgrade commons-pool2 from 2.6.0 to 2.6.2 (Fokko Driesprong)
- \[ [CALCITE-2944](https://issues.apache.org/jira/browse/CALCITE-2944)\] Deprecate Aggregate indicator and remove fields where possible
- \[ [CALCITE-3098](https://issues.apache.org/jira/browse/CALCITE-3098)\] Upgrade SQLLine to 1.8.0
- \[ [CALCITE-2742](https://issues.apache.org/jira/browse/CALCITE-2742)\] Read values of `USER` and `SYSTEM_USER` variables from `DataContext` (Siddharth Teotia, Jacques Nadeau)
- \[ [CALCITE-3082](https://issues.apache.org/jira/browse/CALCITE-3082)\] Fix NPE in `SqlUtil#getSelectListItem`
- \[ [CALCITE-3093](https://issues.apache.org/jira/browse/CALCITE-3093)\] Remove JDBC connection calls from `PlannerImpl`
- \[ [CALCITE-3095](https://issues.apache.org/jira/browse/CALCITE-3095)\] Add several system properties to control enabling/disabling of rules and traits
- \[ [CALCITE-2696](https://issues.apache.org/jira/browse/CALCITE-2696)\] Improve design of join-like relational expressions
- \[ [CALCITE-3097](https://issues.apache.org/jira/browse/CALCITE-3097)\] GROUPING SETS breaks on sets of size > 1 due to precedence issues (Steven Talbot)
- \[ [CALCITE-3022](https://issues.apache.org/jira/browse/CALCITE-3022)\] Babel: Various SQL parsing issues
- \[ [CALCITE-3047](https://issues.apache.org/jira/browse/CALCITE-3047)\] In JDBC adapter, expose multiple schemas of the back-end database
- \[ [CALCITE-3048](https://issues.apache.org/jira/browse/CALCITE-3048)\] Improve how JDBC adapter deduces current schema on Redshift
- Javadoc typos (Wenhui Tang, Muhammad Gelbana)
- \[ [CALCITE-3096](https://issues.apache.org/jira/browse/CALCITE-3096)\] In `RelBuilder`, make alias method idempotent
- \[ [CALCITE-3055](https://issues.apache.org/jira/browse/CALCITE-3055)\] Use pair of `relNode`’s `rowType` and digest as unique key for cache in `RelOptPlanner` (KazydubB)
- \[ [CALCITE-3077](https://issues.apache.org/jira/browse/CALCITE-3077)\] Rewrite `CUBE`&`ROLLUP` queries in `SparkSqlDialect` (DonnyZone)
- \[ [CALCITE-3090](https://issues.apache.org/jira/browse/CALCITE-3090)\] Remove Central configuration
- \[ [CALCITE-2807](https://issues.apache.org/jira/browse/CALCITE-2807)\] Fix `IS NOT DISTINCT FROM` expression identification in `RelOptUtil#pushDownJoinConditions`()
- \[ [CALCITE-3050](https://issues.apache.org/jira/browse/CALCITE-3050)\] Integrate `SqlDialect` and `SqlParser.Config`
- \[ [CALCITE-3023](https://issues.apache.org/jira/browse/CALCITE-3023)\] Upgrade elastic search to 7.x (Takako Shimamoto)
- \[ [CALCITE-3067](https://issues.apache.org/jira/browse/CALCITE-3067)\] Splunk adapter cannot parse right session keys from Splunk 7.2 (Shawn Chen)
- \[ [CALCITE-3076](https://issues.apache.org/jira/browse/CALCITE-3076)\] `AggregateJoinTransposeRule` throws error for unique under aggregate keys when generating merged calls
- \[ [CALCITE-3068](https://issues.apache.org/jira/browse/CALCITE-3068)\] `testSubprogram()` does not test whether subprogram gets re-executed
- \[ [CALCITE-3072](https://issues.apache.org/jira/browse/CALCITE-3072)\] Generate right SQL for `FLOOR&SUBSTRING` functions in `SparkSqlDialect` (DonnyZone)
- \[ [CALCITE-3074](https://issues.apache.org/jira/browse/CALCITE-3074)\] Move MySQL’s JSON operators to `SqlLibraryOperators`
- \[ [CALCITE-3062](https://issues.apache.org/jira/browse/CALCITE-3062)\] Do not populate `provenanceMap` if not debug
- \[ [CALCITE-2282](https://issues.apache.org/jira/browse/CALCITE-2282)\] Remove sql operator table from parser
- \[ [CALCITE-3052](https://issues.apache.org/jira/browse/CALCITE-3052)\] Error while applying rule `MaterializedViewAggregateRule`(Project-Aggregate): `ArrayIndexOutOfBoundsException`
- \[ [CALCITE-3066](https://issues.apache.org/jira/browse/CALCITE-3066)\] `RelToSqlConverter` may incorrectly throw an `AssertionError` for some decimal literals
- \[ [CALCITE-3028](https://issues.apache.org/jira/browse/CALCITE-3028)\] Support FULL OUTER JOIN with `AggregateJoinTransposeRule` (Vineet Garg)
- \[ [CALCITE-3017](https://issues.apache.org/jira/browse/CALCITE-3017)\] Improve null handling of `JsonValueExpressionOperator`
- \[ [CALCITE-2936](https://issues.apache.org/jira/browse/CALCITE-2936)\] Simplify EXISTS or NOT EXISTS sub-query that has “GROUP BY ()”
- \[ [CALCITE-2803](https://issues.apache.org/jira/browse/CALCITE-2803)\] `ProjectTransposeJoinRule` messes INDF expressions
- \[ [CALCITE-3061](https://issues.apache.org/jira/browse/CALCITE-3061)\] Query with WITH clause fails when alias is the same as the table with rolled up column
- \[ [CALCITE-3017](https://issues.apache.org/jira/browse/CALCITE-3017)\] Re-organize how we represent built-in operators that are not in the standard operator table
- \[ [CALCITE-3056](https://issues.apache.org/jira/browse/CALCITE-3056)\] Elasticsearch adapter. Invalid result with cast function on raw queries
- \[ [CALCITE-3046](https://issues.apache.org/jira/browse/CALCITE-3046)\] `CompileException` when inserting casted value of composited user defined type into table
- \[ [CALCITE-3054](https://issues.apache.org/jira/browse/CALCITE-3054)\] Elasticsearch adapter. Avoid scripting for simple projections
- \[ [CALCITE-3039](https://issues.apache.org/jira/browse/CALCITE-3039)\] In Interpreter, min() incorrectly returns maximum double value (dijkspicy)
- \[ [CALCITE-3049](https://issues.apache.org/jira/browse/CALCITE-3049)\] When simplifying “IS NULL” and “IS NOT NULL”, simplify the operand first
- \[ [CALCITE-3003](https://issues.apache.org/jira/browse/CALCITE-3003)\] `AssertionError` when GROUP BY nested field (Will Yu)
- \[ [CALCITE-3012](https://issues.apache.org/jira/browse/CALCITE-3012)\] Column uniqueness metadata provider may return wrong result for `FULL OUTER JOIN` operator (Vineet Garg)
- \[ [CALCITE-3045](https://issues.apache.org/jira/browse/CALCITE-3045)\] `NullPointerException` when casting null literal to composite user defined type
- \[ [CALCITE-3030](https://issues.apache.org/jira/browse/CALCITE-3030)\] `SqlParseException` when using component identifier for setting in merge statements (Danny Chan)
- \[ [CALCITE-3029](https://issues.apache.org/jira/browse/CALCITE-3029)\] Java-oriented field type is wrongly forced to be NOT NULL after being converted to SQL-oriented
- \[ [CALCITE-2292](https://issues.apache.org/jira/browse/CALCITE-2292)\] Query result is wrong when table is implemented with `FilterableTable` and the sql has multiple where conditions
- \[ [CALCITE-2998](https://issues.apache.org/jira/browse/CALCITE-2998)\] `RexCopier` should support all rex types (Chunwei Lei, Alexander Shilov)
- \[ [CALCITE-2982](https://issues.apache.org/jira/browse/CALCITE-2982)\] `SqlItemOperator` should throw understandable exception message for incorrect operand type (pengzhiwei)
- Revert “\[ [CALCITE-3021](https://issues.apache.org/jira/browse/CALCITE-3021)\] `ArrayEqualityComparer` should use `Arrays#deepEquals`/`deepHashCode` instead of `Arrays#equals`/`hashCode` (Ruben Quesada Lopez)
- \[ [CALCITE-3021](https://issues.apache.org/jira/browse/CALCITE-3021)\] `ArrayEqualityComparer` should use `Arrays#deepEquals`/`deepHashCode` instead of `Arrays#equals`/`hashCode`
- \[ [CALCITE-2453](https://issues.apache.org/jira/browse/CALCITE-2453)\] Parse list of SQL statements separated with a semicolon (Chunwei Lei, charbel yazbeck)
- \[ [CALCITE-3004](https://issues.apache.org/jira/browse/CALCITE-3004)\] `RexOver` is incorrectly pushed down in `ProjectSetOpTransposeRule` and `ProjectCorrelateTransposeRule` (Chunwei Lei)
- \[ [CALCITE-3001](https://issues.apache.org/jira/browse/CALCITE-3001)\] Upgrade to Apache Druid 0.14.0-incubating
- Following \[ [CALCITE-3010](https://issues.apache.org/jira/browse/CALCITE-3010)\], remove redundant non-reserved keyword definitions
- \[ [CALCITE-2993](https://issues.apache.org/jira/browse/CALCITE-2993)\] `ParseException` may be thrown for legal SQL queries due to incorrect “LOOKAHEAD(1)” hints
- \[ [CALCITE-3010](https://issues.apache.org/jira/browse/CALCITE-3010)\] In SQL parser, move `JsonValueExpression` into Expression
- \[ [CALCITE-3009](https://issues.apache.org/jira/browse/CALCITE-3009)\] `DiffRepository` should ensure that XML resource file does not contain duplicate test names
- \[ [CALCITE-2986](https://issues.apache.org/jira/browse/CALCITE-2986)\] Wrong results with `= ANY` sub-query (Vineet Garg)
- \[ [CALCITE-2962](https://issues.apache.org/jira/browse/CALCITE-2962)\] `RelStructuredTypeFlattener` generates wrong types for nested column when `flattenProjection` (Will Yu)
- \[ [CALCITE-3007](https://issues.apache.org/jira/browse/CALCITE-3007)\] Type mismatch for `ANY` sub-query in project (Vineet Garg)
- \[ [CALCITE-2865](https://issues.apache.org/jira/browse/CALCITE-2865)\] `FilterProjectTransposeRule` generates wrong `traitSet` when `copyFilter`/`Project` is true (Ruben Quesada Lopez)
- \[ [CALCITE-2343](https://issues.apache.org/jira/browse/CALCITE-2343)\] `PushProjector` with OVER expression causes infinite loop (Chunwei Lei)
- \[ [CALCITE-2994](https://issues.apache.org/jira/browse/CALCITE-2994)\] Least restrictive type among structs does not consider nullability
- \[ [CALCITE-2991](https://issues.apache.org/jira/browse/CALCITE-2991)\] `getMaxRowCount` should return 1 for an Aggregate with constant keys (Vineet Garg)
- \[ [CALCITE-1338](https://issues.apache.org/jira/browse/CALCITE-1338)\] `JoinProjectTransposeRule` should not pull a literal up through the null-generating side of a join (Chunwei Lei)
- \[ [CALCITE-2977](https://issues.apache.org/jira/browse/CALCITE-2977)\] Exception is not thrown when there are ambiguous field in select list
- \[ [CALCITE-2739](https://issues.apache.org/jira/browse/CALCITE-2739)\] NPE is thrown if the DEFINE statement contains IN in `MATCH_RECOGNIZE`
- \[ [CALCITE-896](https://issues.apache.org/jira/browse/CALCITE-896)\] Remove Aggregate if grouping columns are unique and all functions are splittable
- \[ [CALCITE-2456](https://issues.apache.org/jira/browse/CALCITE-2456)\] `VolcanoRuleCall` doesn’t match unordered child operand when the operand is not the first operand. `PruneEmptyRules``UNION` and `MINUS` with empty inputs cause infinite cycle. (Zuozhi Wang)
- \[ [CALCITE-2847](https://issues.apache.org/jira/browse/CALCITE-2847)\] Optimize global LOOKAHEAD for SQL parsers
- \[ [CALCITE-2976](https://issues.apache.org/jira/browse/CALCITE-2976)\] Improve materialized view rewriting coverage with disjunctive predicates
- \[ [CALCITE-2954](https://issues.apache.org/jira/browse/CALCITE-2954)\] `SubQueryJoinRemoveRule` and `SubQueryProjectRemoveRule` passing on empty set instead of set of correlation id (Vineet Garg)
- \[ [CALCITE-2930](https://issues.apache.org/jira/browse/CALCITE-2930)\] `IllegalStateException` when `FilterCorrelateRule` matches a SEMI or ANTI Correlate (Ruben Quesada Lopez)
- \[ [CALCITE-2004](https://issues.apache.org/jira/browse/CALCITE-2004)\] Push join predicate down into inner relation for lateral join
- \[ [CALCITE-2820](https://issues.apache.org/jira/browse/CALCITE-2820)\] Avoid reducing certain aggregate functions when it is not necessary (Siddharth Teotia)
- \[ [CALCITE-2928](https://issues.apache.org/jira/browse/CALCITE-2928)\] When resolving user-defined functions (UDFs), use the case-sensitivity of the current connection (Danny Chan)
- \[ [CALCITE-2900](https://issues.apache.org/jira/browse/CALCITE-2900)\] `RelStructuredTypeFlattener` generates wrong types on nested columns (Will Yu)
- \[ [CALCITE-2941](https://issues.apache.org/jira/browse/CALCITE-2941)\] `EnumerableLimitRule` on Sort with no collation creates `EnumerableLimit` with wrong `traitSet` and `cluster` (Ruben Quesada Lopez)
- \[ [CALCITE-2909](https://issues.apache.org/jira/browse/CALCITE-2909)\] Optimize Enumerable `SemiJoin` with lazy computation of `innerLookup` (Ruben Quesada Lopez)
- \[ [CALCITE-2903](https://issues.apache.org/jira/browse/CALCITE-2903)\] Exception thrown when decorrelating query with `TEMPORAL TABLE`
- \[ [CALCITE-2958](https://issues.apache.org/jira/browse/CALCITE-2958)\] Upgrade SQLLine to 1.7.0
- \[ [CALCITE-2796](https://issues.apache.org/jira/browse/CALCITE-2796)\] JDBC adapter fix for `ROLLUP` on MySQL 5
- In `RelFieldCollation`, add a `withX` copy method
- \[ [CALCITE-2953](https://issues.apache.org/jira/browse/CALCITE-2953)\] `LatticeTest.testTileAlgorithm2` and `LatticeTest.testTileAlgorithm3` fail intermittently
- \[ [CALCITE-574](https://issues.apache.org/jira/browse/CALCITE-574)\] Remove `org.apache.calcite.util.Bug.CALCITE_461_FIXED`
- \[ [CALCITE-2951](https://issues.apache.org/jira/browse/CALCITE-2951)\] Support decorrelating a sub-query that has aggregate with grouping sets (Haisheng Yuan)
- \[ [CALCITE-2946](https://issues.apache.org/jira/browse/CALCITE-2946)\] `RelBuilder` wrongly skips creation of Aggregate that prunes columns if input produces one row at most
- \[ [CALCITE-2943](https://issues.apache.org/jira/browse/CALCITE-2942)\] Materialized view rewriting logic calls `getApplicableMaterializations` each time the rule is triggered
- \[ [CALCITE-2942](https://issues.apache.org/jira/browse/CALCITE-2942)\] Materialized view rewriting logic instantiates `RelMetadataQuery` each time the rule is triggered

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-20-0 "Permalink")

- Fix test exception caused by slightly different error message from regex in JDK 13
- Following \[ [CALCITE-2812](https://issues.apache.org/jira/browse/CALCITE-2812)\] Disable parallel execution of parameterized test to avoid hanging
- \[ [CALCITE-35](https://issues.apache.org/jira/browse/CALCITE-35)\] More test cases to guard against providing a broken fix for parenthesized join (Muhammad Gelbana)
- \[ [CALCITE-3034](https://issues.apache.org/jira/browse/CALCITE-3034)\] CSV test case description does not match it’s code logic (FaxianZhao)
- Mongo adapter. Mongo checker validates only first line of the Bson query in tests
- \[ [CALCITE-3053](https://issues.apache.org/jira/browse/CALCITE-3053)\] Add a test to ensure that all functions are documented in the SQL reference
- \[ [CALCITE-2961](https://issues.apache.org/jira/browse/CALCITE-2961)\] Enable Travis to test against JDK 13

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-20-0 "Permalink")

- \[ [CALCITE-2952](https://issues.apache.org/jira/browse/CALCITE-2952)\] Document JDK 12 support
- Site: Add Danny Chan as committer
- Site: Improve contribution guidelines for JIRA
- \[ [CALCITE-2846](https://issues.apache.org/jira/browse/CALCITE-2846)\] Document Oracle-specific functions, such as `NVL` and `LTRIM`, in the SQL reference
- Site: Add new committers and PMC (Chunwei Lei, Ruben Quesada Lopez, Zhiwei Peng and Stamatis Zampetakis)
- \[ [CALCITE-3006](https://issues.apache.org/jira/browse/CALCITE-3006)\] Example code on site cannot compile (Chunwei Lei)
- Site: Add guidelines for JIRA’s fix version field
- Site: Update content of “Not implemented” since JSON\_LENGH has already been added
- Site: Improve documentation for MySQL-specific JSON operators
- \[ [CALCITE-2927](https://issues.apache.org/jira/browse/CALCITE-2927)\] The Javadoc and implement of `RuleQueue.computeImportance()` is inconsistent (Meng Wang)
- Update instructions for publishing site; we previously used subversion, now we use git
- Site: Add Alibaba MaxCompute to powered-by page
- Site: Add new committers (Haisheng Yuan, Hongze Zhang and Stamatis Zampetakis)
- \[ [CALCITE-2952](https://issues.apache.org/jira/browse/CALCITE-2952)\] Add JDK 12 as tested to 1.19.0 history

## [1.19.0](https://github.com/apache/calcite/releases/tag/calcite-1.19.0) / 2019-03-25 [Permalink](https://calcite.apache.org/docs/history.html\#v1-19-0 "Permalink")

This release comes three months after 1.18.0. It includes more than 80 resolved
issues, comprising of a few new features as well as general improvements
and bug-fixes. Among others, there have been significant improvements in JSON
query support.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11, 12 and OpenJDK 8, 9, 10, 11, 12;
Guava versions 19.0 to 27.1-jre;
Druid version 0.11.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-19-0 "Permalink")

- \[ [CALCITE-1912](https://issues.apache.org/jira/browse/CALCITE-1912)\]
Support `FOR SYSTEM_TIME AS OF` in regular queries
- \[ [CALCITE-2786](https://issues.apache.org/jira/browse/CALCITE-2786)\]
Add order by clause support for `JSON_ARRAYAGG`
- \[ [CALCITE-2791](https://issues.apache.org/jira/browse/CALCITE-2791)\]
Add the `JSON_TYPE` function
- \[ [CALCITE-2864](https://issues.apache.org/jira/browse/CALCITE-2864)\]
Add the `JSON_DEPTH` function
- \[ [CALCITE-2881](https://issues.apache.org/jira/browse/CALCITE-2881)\]
Add the `JSON_PRETTY` function
- \[ [CALCITE-2770](https://issues.apache.org/jira/browse/CALCITE-2770)\]
Add bitwise aggregate functions `BIT_AND`, `BIT_OR`
- \[ [CALCITE-2799](https://issues.apache.org/jira/browse/CALCITE-2799)\]
Allow alias in `HAVING` clause for aggregate functions

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-19-0 "Permalink")

- \[ [CALCITE-1513](https://issues.apache.org/jira/browse/CALCITE-1513)\]
Correlated `NOT IN` query throws `AssertionError`
- \[ [CALCITE-1726](https://issues.apache.org/jira/browse/CALCITE-1726)\]
Sub-query in `FILTER` is left untransformed
- \[ [CALCITE-2249](https://issues.apache.org/jira/browse/CALCITE-2249)\]
`AggregateJoinTransposeRule` generates non-equivalent nodes if `Aggregate`
contains a `DISTINCT` aggregate function
- \[ [CALCITE-2288](https://issues.apache.org/jira/browse/CALCITE-2288)\]
Type assertion error when reducing partially-constant expression
- \[ [CALCITE-2290](https://issues.apache.org/jira/browse/CALCITE-2290)\]
Type mismatch during flattening
- \[ [CALCITE-2301](https://issues.apache.org/jira/browse/CALCITE-2301)\]
JDBC adapter: use query timeout from the top-level statement
- \[ [CALCITE-2338](https://issues.apache.org/jira/browse/CALCITE-2338)\]
Make simplification API more conservative
- \[ [CALCITE-2344](https://issues.apache.org/jira/browse/CALCITE-2344)\]
Avoid inferring `$0 = null` predicate from `$0 IS NULL` when `$0` is not
nullable
- \[ [CALCITE-2375](https://issues.apache.org/jira/browse/CALCITE-2375)\]
`EnumerableDefaults.join_()` leaks connections
- \[ [CALCITE-2437](https://issues.apache.org/jira/browse/CALCITE-2437)\]
`FilterMultiJoinMergeRule` doesn’t combine postFilterCondition
- \[ [CALCITE-2454](https://issues.apache.org/jira/browse/CALCITE-2454)\]
Avoid treating `Project(x=1)` and `Project(x=1)` equal when the type of `1` is
`int` in the first rel and `long` in the second
- \[ [CALCITE-2463](https://issues.apache.org/jira/browse/CALCITE-2463)\]
Silence ERROR logs from `CalciteException`, `SqlValidatorException`
- \[ [CALCITE-2464](https://issues.apache.org/jira/browse/CALCITE-2464)\]
Allow to set nullability for columns of structured types
- \[ [CALCITE-2471](https://issues.apache.org/jira/browse/CALCITE-2471)\]
`RelNode` description includes all tree when recomputed
- \[ [CALCITE-2554](https://issues.apache.org/jira/browse/CALCITE-2554)\]
Enrich enumerable join operators with order-preserving information
- \[ [CALCITE-2582](https://issues.apache.org/jira/browse/CALCITE-2582)\]
`FilterProjectTransposeRule` does not always simplify the new filter condition
- \[ [CALCITE-2599](https://issues.apache.org/jira/browse/CALCITE-2599)\]
Support `ASCII(string)` in `SqlFunctions`
- \[ [CALCITE-2621](https://issues.apache.org/jira/browse/CALCITE-2621)\]
Add rule to execute semi-joins with correlation
- \[ [CALCITE-2623](https://issues.apache.org/jira/browse/CALCITE-2623)\]
Add specific translation for `POSITION`, `MOD` and set operators in BigQuery
and Hive SQL dialects
- \[ [CALCITE-2625](https://issues.apache.org/jira/browse/CALCITE-2625)\]
`ROW_NUMBER`, `RANK` generating invalid SQL
- \[ [CALCITE-2629](https://issues.apache.org/jira/browse/CALCITE-2629)\]
Unnecessary call to `CatalogReader#getAllSchemaObjects` in `CatalogScope`
- \[ [CALCITE-2635](https://issues.apache.org/jira/browse/CALCITE-2635)\]
`getMonotonocity` is slow on wide tables
- \[ [CALCITE-2674](https://issues.apache.org/jira/browse/CALCITE-2674)\]
`SqlIdentifier` same name with built-in function but with escape character
should be still resolved as an identifier
- \[ [CALCITE-2677](https://issues.apache.org/jira/browse/CALCITE-2677)\]
Struct types with one field are not mapped correctly to Java classes
- \[ [CALCITE-2703](https://issues.apache.org/jira/browse/CALCITE-2703)\]
Reduce code generation and class loading overhead when executing queries in
`EnumerableConvention`
- \[ [CALCITE-2722](https://issues.apache.org/jira/browse/CALCITE-2722)\]
`SqlImplementor.createLeftCall` method throws `StackOverflowError`
- \[ [CALCITE-2727](https://issues.apache.org/jira/browse/CALCITE-2727)\]
Materialized view rewriting bails out incorrectly when a view does not contain
any table reference
- \[ [CALCITE-2733](https://issues.apache.org/jira/browse/CALCITE-2733)\]
Use `catalog` and `schema` from JDBC connect string to retrieve tables if specified
- \[ [CALCITE-2750](https://issues.apache.org/jira/browse/CALCITE-2750)\]
`PI` operator is incorrectly identified as dynamic function
- \[ [CALCITE-2755](https://issues.apache.org/jira/browse/CALCITE-2755)\]
Expose document `_id` field when querying ElasticSearch
- \[ [CALCITE-2762](https://issues.apache.org/jira/browse/CALCITE-2762)\]
Quidem env variable is always false if its name is separated by dot(“.”)
- \[ [CALCITE-2778](https://issues.apache.org/jira/browse/CALCITE-2778)\]
Remove `ClosableAllocation`, `ClosableAllocationOwner`,
`CompoundClosableAllocation`
- \[ [CALCITE-2782](https://issues.apache.org/jira/browse/CALCITE-2782)\]
Use server time zone by default if time zone is not specified in the user connection string
- \[ [CALCITE-2783](https://issues.apache.org/jira/browse/CALCITE-2783)\]
“COALESCE(s, TRUE) = TRUE” and “(s OR s IS UNKNOWN) = TRUE” causes
`NullPointerException`
- \[ [CALCITE-2785](https://issues.apache.org/jira/browse/CALCITE-2785)\]
In `EnumerableAggregate`, wrong result produced If there are sorted aggregates
and non-sorted aggregates at the same time
- \[ [CALCITE-2787](https://issues.apache.org/jira/browse/CALCITE-2787)\]
JSON aggregate calls with different null clause get incorrectly merged while
converting from SQL to relational algebra
- \[ [CALCITE-2790](https://issues.apache.org/jira/browse/CALCITE-2790)\]
`AggregateJoinTransposeRule` incorrectly pushes down distinct count into join
- \[ [CALCITE-2797](https://issues.apache.org/jira/browse/CALCITE-2797)\]
Support `APPROX_COUNT_DISTINCT` aggregate function in ElasticSearch
- \[ [CALCITE-2798](https://issues.apache.org/jira/browse/CALCITE-2798)\]
Optimizer should remove `ORDER BY` in sub-query, provided it has no `LIMIT` or
`OFFSET`
- \[ [CALCITE-2802](https://issues.apache.org/jira/browse/CALCITE-2802)\]
In Druid adapter, use of range conditions like `'2010-01-01' < TIMESTAMP` leads
to incorrect results
- \[ [CALCITE-2805](https://issues.apache.org/jira/browse/CALCITE-2805)\]
Can’t specify port with Cassandra adapter in connection string
- \[ [CALCITE-2806](https://issues.apache.org/jira/browse/CALCITE-2806)\]
Cassandra adapter doesn’t allow uppercase characters in table names
- \[ [CALCITE-2811](https://issues.apache.org/jira/browse/CALCITE-2811)\]
Update version of Cassandra driver
- \[ [CALCITE-2814](https://issues.apache.org/jira/browse/CALCITE-2814)\]
In ElasticSearch adapter, fix `GROUP BY` when using raw item access
(e.g. `_MAP*` \[‘a.b.c’\])
- \[ [CALCITE-2817](https://issues.apache.org/jira/browse/CALCITE-2817)\]
Make `CannotPlanException` more informative
- \[ [CALCITE-2827](https://issues.apache.org/jira/browse/CALCITE-2827)\]
Allow `CONVENTION.NONE` planning with `VolcanoPlanner`
- \[ [CALCITE-2838](https://issues.apache.org/jira/browse/CALCITE-2838)\]
Simplification: Remove redundant `IS TRUE` checks
- \[ [CALCITE-2839](https://issues.apache.org/jira/browse/CALCITE-2839)\]
Simplify comparisons against `BOOLEAN` literals
- \[ [CALCITE-2840](https://issues.apache.org/jira/browse/CALCITE-2840)\]
`RexNode` simplification logic should use more specific `UnknownAs` modes
- \[ [CALCITE-2841](https://issues.apache.org/jira/browse/CALCITE-2841)\]
Simplification: push negation into Case expression
- \[ [CALCITE-2842](https://issues.apache.org/jira/browse/CALCITE-2842)\]
Computing `RexCall` digest containing `IN` expressions leads to exceptions
- \[ [CALCITE-2848](https://issues.apache.org/jira/browse/CALCITE-2848)\]
Simplifying a CASE statement's first branch should ignore its safety
- \[ [CALCITE-2850](https://issues.apache.org/jira/browse/CALCITE-2850)\]
Geode adapter: support `BOOLEAN` column as filter operand
- \[ [CALCITE-2852](https://issues.apache.org/jira/browse/CALCITE-2852)\]
RexNode simplification does not traverse unknown functions
- \[ [CALCITE-2856](https://issues.apache.org/jira/browse/CALCITE-2856)\]
Emulating `COMMA JOIN` as `CROSS JOIN` for `SparkSqlDialect`
- \[ [CALCITE-2858](https://issues.apache.org/jira/browse/CALCITE-2858)\]
Improvements in JSON writer and reader for plans
- \[ [CALCITE-2859](https://issues.apache.org/jira/browse/CALCITE-2859)\]
Centralize Calcite system properties
- \[ [CALCITE-2863](https://issues.apache.org/jira/browse/CALCITE-2863)\]
In ElasticSearch adapter, query fails when filtering directly on `_MAP`
- \[ [CALCITE-2887](https://issues.apache.org/jira/browse/CALCITE-2887)\]
Improve performance of `RexLiteral.toJavaString()`
- \[ [CALCITE-2897](https://issues.apache.org/jira/browse/CALCITE-2897)\]
Reduce expensive calls to `Class.getSimpleName()`
- \[ [CALCITE-2899](https://issues.apache.org/jira/browse/CALCITE-2899)\]
Deprecate `RelTraitPropagationVisitor` and remove its usages
- \[ [CALCITE-2890](https://issues.apache.org/jira/browse/CALCITE-2890)\]
In ElasticSearch adapter, combine `any_value` with other aggregation functions
failed
- \[ [CALCITE-2891](https://issues.apache.org/jira/browse/CALCITE-2891)\]
Alias suggester failed to suggest name based on original name incrementally
- \[ [CALCITE-2894](https://issues.apache.org/jira/browse/CALCITE-2894)\]
`RelMdPercentageOriginalRows` throws `NullPointerException` when explaining
plan with all attributes
- \[ [CALCITE-2902](https://issues.apache.org/jira/browse/CALCITE-2902)\]
Improve performance of `AbstractRelNode.computeDigest()`
- \[ [CALCITE-2929](https://issues.apache.org/jira/browse/CALCITE-2929)\]
Simplification of `IS NULL` checks are incorrectly assuming that `CAST`s are
possible
- Improve Graphviz dump in `CannotPlanException`: make boxes shorter, print
composite traits if they were simplified
- Make `SparkHandlerImpl` singleton thread-safe
- Remove usage of `userConfig` attribute in ElasticSearch adapter
- In ElasticSearch adapter, remove dead (or unnecessary) code

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-19-0 "Permalink")

- \[ [CALCITE-2732](https://issues.apache.org/jira/browse/CALCITE-2732)\]
Upgrade Postgres driver version
- \[ [CALCITE-2759](https://issues.apache.org/jira/browse/CALCITE-2759)\]
Update `maven-remote-resources-plugin` to 1.6.0
- \[ [CALCITE-2765](https://issues.apache.org/jira/browse/CALCITE-2765)\]
Bump Janino compiler dependency to 3.0.11
- \[ [CALCITE-2768](https://issues.apache.org/jira/browse/CALCITE-2768)\]
`PlannerTest` ignores top-level `ORDER BY` clause (`RootRel.collation`)
- \[ [CALCITE-2788](https://issues.apache.org/jira/browse/CALCITE-2788)\]
Building error for sub-project of calcite on `maven-checkstyle-plugin`
- \[ [CALCITE-2779](https://issues.apache.org/jira/browse/CALCITE-2779)\]
Remove references to `StringBuffer`
- \[ [CALCITE-2875](https://issues.apache.org/jira/browse/CALCITE-2875)\]
Some misspellings in `RelOptListener`
- \[ [CALCITE-2895](https://issues.apache.org/jira/browse/CALCITE-2895)\]
Some arguments are undocumented in constructor of `LogicalAggregate`
- \[ [CALCITE-2836](https://issues.apache.org/jira/browse/CALCITE-2836)\]
Remove `maven-compiler-plugin` from `calcite-plus` module `pom.xml`
- \[ [CALCITE-2878](https://issues.apache.org/jira/browse/CALCITE-2878)\]
Avoid `throw new RuntimeException(e)` in tests
- \[ [CALCITE-2916](https://issues.apache.org/jira/browse/CALCITE-2916)\]
Upgrade jackson to 2.9.8
- \[ [CALCITE-2925](https://issues.apache.org/jira/browse/CALCITE-2925)\]
Exclude `maven-wrapper.jar` from source distribution
- \[ [CALCITE-2931](https://issues.apache.org/jira/browse/CALCITE-2931)\]
In Mongo adapter, compare Bson (not string) query representation in tests
- \[ [CALCITE-2932](https://issues.apache.org/jira/browse/CALCITE-2932)\]
`DruidAdapterIT` regression after 1.17 release
- Improve messages for tests based on `CalciteAssert`
- Add JUnit category for extremely slow tests, launch them in a separate Travis job
- Fix sqlline by removing redundant slf4j dependency (`log4j-over-slf4j`) from
`cassandra-all`

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-19-0 "Permalink")

- Switch from `maven:alpine` to `maven` image for generating javadoc when
building the site
- Update instructions for pushing to the git site repository
- \[ [CALCITE-2734](https://issues.apache.org/jira/browse/CALCITE-2734)\]
Site: Update mongo documentation to reflect filename changes
- Site: Add commit message guidelines for contributors (Stamatis Zampetakis)
- Site: Add Zoltan Haindrich as committer
- Site: Elastic query example on `_MAP`
- Site: fix JSON syntax error at file adapter page (Marc Prud’hommeaux)
- Site: fix typo at the main page (Marc Prud’hommeaux)
- \[ [CALCITE-2436](https://issues.apache.org/jira/browse/CALCITE-2436)\]
Steps for building site under Windows; fix misprint in SQL Language page
- Site: News item for release 1.18
- Site: Rename MapD to OmniSci, and update logos
- Update site for new repository
- Update git URL
- Site: ElasticAdapter mention supported versions (and support schedule)
- Site: Improve documentation for ElasticSearch Adapter
- Site: Update PMC chair
- Update year in NOTICE

## [1.18.0](https://github.com/apache/calcite/releases/tag/calcite-1.18.0) / 2018-12-21 [Permalink](https://calcite.apache.org/docs/history.html\#v1-18-0 "Permalink")

With over 200 commits from 36 contributors, this is the largest
Calcite release ever. To the SQL dialect, we added
[JSON\\
functions](https://issues.apache.org/jira/browse/CALCITE-2266) and
[linear\\
regression functions](https://issues.apache.org/jira/browse/CALCITE-2402), the
[WITHIN\\
GROUP](https://issues.apache.org/jira/browse/CALCITE-2224) clause for aggregate functions; there is a new
[utility\\
to recommend lattices based on past queries](https://issues.apache.org/jira/browse/CALCITE-1870),
and improvements to expression simplification, the SQL advisor,
and the Elasticsearch and Apache Geode adapters.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10, 11 and OpenJDK 10, 11;
Guava versions 19.0 to 27.0.1-jre;
Druid version 0.11.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-18-0 "Permalink")

- \[ [CALCITE-2662](https://issues.apache.org/jira/browse/CALCITE-2662)\]
In `Planner`, allow parsing a stream (`Reader`) instead of a `String`
(Enrico Olivelli)
- \[ [CALCITE-2699](https://issues.apache.org/jira/browse/CALCITE-2699)\]
`TIMESTAMPADD` function now applies to `DATE` and `TIME` as well as `TIMESTAMP`
(xuqianjin)
- \[ [CALCITE-563](https://issues.apache.org/jira/browse/CALCITE-563)\]
In JDBC adapter, push bindable parameters down to the underlying JDBC data
source (Vladimir Sitnikov, Piotr Bojko)
- \[ [CALCITE-2663](https://issues.apache.org/jira/browse/CALCITE-2663)\]
In DDL parser, add `CREATE` and `DROP FUNCTION` (ambition119)
- \[ [CALCITE-2266](https://issues.apache.org/jira/browse/CALCITE-2266)\]
Implement SQL:2016 JSON functions: `JSON_EXISTS`, `JSON_VALUE`, `JSON_QUERY`,
`JSON_OBJECT`, `JSON_OBJECTAGG`, `JSON_ARRAY`, `JSON_ARRAYAGG`, `x IS JSON`
predicate (Hongze Zhang)
- \[ [CALCITE-2224](https://issues.apache.org/jira/browse/CALCITE-2224)\]
Support `WITHIN GROUP` clause for aggregate functions (Hongze Zhang)
- \[ [CALCITE-2405](https://issues.apache.org/jira/browse/CALCITE-2405)\]
In Babel parser, make 400 reserved keywords including `YEAR`, `SECOND`, `DESC`
non-reserved
- \[ [CALCITE-1870](https://issues.apache.org/jira/browse/CALCITE-1870)\]
Lattice suggester
- \[ [CALCITE-2571](https://issues.apache.org/jira/browse/CALCITE-2571)\]
`TRIM` function now trims more than one character (Andrew Pilloud)
- \[ [CALCITE-2112](https://issues.apache.org/jira/browse/CALCITE-2112)\]
Add Maven wrapper for Calcite (Ratandeep S. Ratti)
- \[ [CALCITE-1026](https://issues.apache.org/jira/browse/CALCITE-1026)\]
Allow models in YAML format
- \[ [CALCITE-2402](https://issues.apache.org/jira/browse/CALCITE-2402)\]
Implement regression functions: `COVAR_POP`, `COVAR_SAMP`, `REGR_COUNT`,
`REGR_SXX`, `REGR_SYY`
- SQL advisor (`SqlAdvisor`):

  - \[ [CALCITE-2479](https://issues.apache.org/jira/browse/CALCITE-2479)\]
    Automatically quote identifiers that look like SQL keywords
  - \[ [CALCITE-2478](https://issues.apache.org/jira/browse/CALCITE-2478)\]
    Purge `from_clause` when `_suggest_` token is located in one of the
    `FROM` sub-queries
  - \[ [CALCITE-2477](https://issues.apache.org/jira/browse/CALCITE-2477)\]
    Scalar sub-queries
  - \[ [CALCITE-2476](https://issues.apache.org/jira/browse/CALCITE-2476)\]
    Produce hints when sub-query with `*` is present in query
  - \[ [CALCITE-2475](https://issues.apache.org/jira/browse/CALCITE-2475)\]
    Support `MINUS`
  - \[ [CALCITE-2473](https://issues.apache.org/jira/browse/CALCITE-2473)\]
    Support `--` comments
  - \[ [CALCITE-2434](https://issues.apache.org/jira/browse/CALCITE-2434)\]
    Hints for nested tables and schemas
  - \[ [CALCITE-2433](https://issues.apache.org/jira/browse/CALCITE-2433)\]
    Configurable quoting characters
- Relational algebra builder (`RelBuilder`):

  - \[ [CALCITE-2661](https://issues.apache.org/jira/browse/CALCITE-2661)\]
    Add methods for creating `Exchange` and `SortExchange`
    relational expressions (Chunwei Lei)
  - \[ [CALCITE-2654](https://issues.apache.org/jira/browse/CALCITE-2654)\]
    Add a fluent API for building complex aggregate calls
  - \[ [CALCITE-2441](https://issues.apache.org/jira/browse/CALCITE-2441)\]
    `RelBuilder.scan` should expand `TranslatableTable` and views
  - \[ [CALCITE-2647](https://issues.apache.org/jira/browse/CALCITE-2647)\]
    Add a `groupKey` method that assumes only one grouping set
  - \[ [CALCITE-2470](https://issues.apache.org/jira/browse/CALCITE-2470)\]
    `project` method should combine expressions if the underlying
    node is a `Project`
- Elasticsearch adapter:
  - \[ [CALCITE-2679](https://issues.apache.org/jira/browse/CALCITE-2679)\]
    Implement `DISTINCT` and `GROUP BY` without aggregate functions (Siyuan Liu)
  - \[ [CALCITE-2689](https://issues.apache.org/jira/browse/CALCITE-2689)\]
    Allow grouping on non-textual fields like `DATE` and `NUMBER`
  - \[ [CALCITE-2651](https://issues.apache.org/jira/browse/CALCITE-2651)\]
    Enable scrolling for basic search queries
  - \[ [CALCITE-2585](https://issues.apache.org/jira/browse/CALCITE-2585)\]
    Support `NOT` operator
  - \[ [CALCITE-2578](https://issues.apache.org/jira/browse/CALCITE-2578)\]
    Support `ANY_VALUE` aggregate function
  - \[ [CALCITE-2528](https://issues.apache.org/jira/browse/CALCITE-2528)\]
    Support `Aggregate` (Andrei Sereda)
- Apache Geode adapter:
  - \[ [CALCITE-2709](https://issues.apache.org/jira/browse/CALCITE-2709)\]
    Allow filtering on `DATE`, `TIME`, `TIMESTAMP` fields (Sandeep Chada)
  - \[ [CALCITE-2671](https://issues.apache.org/jira/browse/CALCITE-2671)\]
    `GeodeFilter` now converts multiple `OR` predicates (on same attribute) into
    a single `IN SET` (Sandeep Chada)
  - \[ [CALCITE-2498](https://issues.apache.org/jira/browse/CALCITE-2498)\]
    Geode adapter wrongly quotes `BOOLEAN` values as strings (Andrei Sereda)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-18-0 "Permalink")

- \[ [CALCITE-2670](https://issues.apache.org/jira/browse/CALCITE-2670)\]
Combine similar JSON aggregate functions in operator table
- \[ [CALCITE-2468](https://issues.apache.org/jira/browse/CALCITE-2468)\]
Validator throws `IndexOutOfBoundsException` when trying to infer operand type
from `STRUCT` return type (Rong Rong)
- \[ [CALCITE-2596](https://issues.apache.org/jira/browse/CALCITE-2596)\]
When translating correlated variables in enumerable convention, convert
not-null boxed primitive values to primitive (Stamatis Zampetakis)
- \[ [CALCITE-2684](https://issues.apache.org/jira/browse/CALCITE-2684)\]
`RexBuilder` gives `AssertionError` when creating integer literal larger than
263 (Ruben Quesada Lopez)
- \[ [CALCITE-2719](https://issues.apache.org/jira/browse/CALCITE-2719)\]
In JDBC adapter for MySQL, fix cast to `INTEGER` and `BIGINT` (Piotr Bojko)
- \[ [CALCITE-2713](https://issues.apache.org/jira/browse/CALCITE-2713)\]
JDBC adapter may generate casts on Postgres for `VARCHAR` type exceeding max
length
- \[ [CALCITE-2529](https://issues.apache.org/jira/browse/CALCITE-2529)\]
All numbers are in the same type family (Andrew Pilloud)
- \[ [CALCITE-2701](https://issues.apache.org/jira/browse/CALCITE-2701)\]
Make generated `Baz` classes immutable (Stamatis Zampetakis)
- \[ [CALCITE-2619](https://issues.apache.org/jira/browse/CALCITE-2619)\]
Reduce string literal creation cost by deferring and caching charset
conversion (Ted Xu)
- \[ [CALCITE-2720](https://issues.apache.org/jira/browse/CALCITE-2720)\]
`RelMetadataQuery.getTableOrigin` throws `IndexOutOfBoundsException` if
`RelNode` has no columns (Zoltan Haindrich)
- \[ [CALCITE-2717](https://issues.apache.org/jira/browse/CALCITE-2717)\]
Use `Interner` instead of `LoadingCache` to cache traits, and so allow traits
to be garbage-collected (Haisheng Yuan)
- \[ [CALCITE-2542](https://issues.apache.org/jira/browse/CALCITE-2542)\]
In SQL parser, allow `.field` to follow any expression, not just tables and
columns (Rong Rong)
- \[ [CALCITE-2637](https://issues.apache.org/jira/browse/CALCITE-2637)\]
In SQL parser, allow prefix ‘-‘ between `BETWEEN` and `AND` (Qi Yu)
- \[ [CALCITE-2632](https://issues.apache.org/jira/browse/CALCITE-2632)\]
Ensure that `RexNode` and its sub-classes implement `hashCode` and `equals`
methods (Zoltan Haindrich)
- \[ [CALCITE-2494](https://issues.apache.org/jira/browse/CALCITE-2494)\]
`RexFieldAccess` should implement `equals` and `hashCode` methods
- \[ [CALCITE-2715](https://issues.apache.org/jira/browse/CALCITE-2715)\]
In JDBC adapter, do not generate character set in data types for MS SQL Server
(Piotr Bojko)
- \[ [CALCITE-2714](https://issues.apache.org/jira/browse/CALCITE-2714)\]
Make `BasicSqlType` immutable, and now `SqlTypeFactory.createWithNullability`
can reuse existing type if possible (Ruben Quesada Lopez)
- \[ [CALCITE-2687](https://issues.apache.org/jira/browse/CALCITE-2687)\]
`IS DISTINCT FROM` could lead to exceptions in `ReduceExpressionsRule`
(Zoltan Haindrich)
- \[ [CALCITE-2673](https://issues.apache.org/jira/browse/CALCITE-2673)\]
`SqlDialect` supports pushing of all functions by default
- \[ [CALCITE-2675](https://issues.apache.org/jira/browse/CALCITE-2675)\]
Type validation error as `ReduceExpressionsRule` fails to preserve type
nullability (Zoltan Haindrich)
- \[ [CALCITE-2669](https://issues.apache.org/jira/browse/CALCITE-2669)\]
`RelMdTableReferences` should check whether references inferred from input are
null for `Union`/`Join` operators
- Following
\[ [CALCITE-2031](https://issues.apache.org/jira/browse/CALCITE-2031)\]
remove incorrect “Not implemented” message
- \[ [CALCITE-2668](https://issues.apache.org/jira/browse/CALCITE-2668)\]
Support for left/right outer join in `RelMdExpressionLineage`
- Fix invocation of deprecated constructor of `SqlAggFunction` (Hongze Zhang)
- \[ [CALCITE-2652](https://issues.apache.org/jira/browse/CALCITE-2652)\]
`SqlNode` to SQL conversion fails if the join condition references a `BOOLEAN`
column (Zoltan Haindrich)
- \[ [CALCITE-2657](https://issues.apache.org/jira/browse/CALCITE-2657)\]
In `RexShuttle`, use `RexCall.clone` instead of `new RexCall` (Chunwei Lei)
- \[ [CALCITE-2605](https://issues.apache.org/jira/browse/CALCITE-2605)\]
Support semi-join via `EnumerableCorrelate` (Ruben Quesada Lopez)
- \[ [CALCITE-2605](https://issues.apache.org/jira/browse/CALCITE-2605)\]
Support left outer join via `EnumerableCorrelate`
- \[ [CALCITE-1174](https://issues.apache.org/jira/browse/CALCITE-1174)\]
When generating SQL, translate `SUM0(x)` to `COALESCE(SUM(x), 0)`
- `RelBuilder.toString()`
- \[ [CALCITE-2617](https://issues.apache.org/jira/browse/CALCITE-2617)\]
Add a variant of `FilterProjectTransposeRule` that can push down a `Filter`
that contains correlated variables (Stamatis Zampetakis)
- \[ [CALCITE-2638](https://issues.apache.org/jira/browse/CALCITE-2638)\]
Constant reducer should not treat as constant an `RexInputRef` that points to a
call to a dynamic or non-deterministic function (Danny Chan)
- \[ [CALCITE-2628](https://issues.apache.org/jira/browse/CALCITE-2628)\]
JDBC adapter throws `NullPointerException` while generating `GROUP BY` query
for MySQL
- \[ [CALCITE-2404](https://issues.apache.org/jira/browse/CALCITE-2404)\]
Implement access to structured-types in enumerable runtime
(Stamatis Zampetakis)
- \[ [CALCITE-2622](https://issues.apache.org/jira/browse/CALCITE-2622)\]
`RexFieldCollation.toString()` method is not deterministic
- \[ [CALCITE-2611](https://issues.apache.org/jira/browse/CALCITE-2611)\]
Linq4j code generation failure if one side of an `OR` contains `UNKNOWN`
(Zoltan Haindrich)
- Canonize simple cases for composite traits in trait factory
- \[ [CALCITE-2591](https://issues.apache.org/jira/browse/CALCITE-2591)\]
`EnumerableDefaults#mergeJoin` should throw error and not return incorrect
results when inputs are not ordered (Enrico Olivelli)
- Test case for
\[ [CALCITE-2592](https://issues.apache.org/jira/browse/CALCITE-2592)\]
`EnumerableMergeJoin` is never taken
- \[ [CALCITE-2526](https://issues.apache.org/jira/browse/CALCITE-2526)\]
Add test for `OR` with nullable comparisons (pengzhiwei)
- \[ [CALCITE-2413](https://issues.apache.org/jira/browse/CALCITE-2413)\]
Use raw signatures for classes with generics when producing Java code
- In Elasticsearch adapter, remove redundant null check in
`CompoundQueryExpression`
- \[ [CALCITE-2562](https://issues.apache.org/jira/browse/CALCITE-2562)\]
Remove dead code in `StandardConvertletTable#convertDatetimeMinus`
- Avoid `NullPointerException` when `FlatList` contains null elements
- \[ [CALCITE-2561](https://issues.apache.org/jira/browse/CALCITE-2561)\]
Remove dead code in `Lattice` constructor
- Apply small refactorings to Calcite codebase (Java 5, Java 7, Java 8)
- \[ [CALCITE-2572](https://issues.apache.org/jira/browse/CALCITE-2572)\]
SQL standard semantics for `SUBSTRING` function (Andrew Pilloud)
- Remove dead code: `Compatible`, `CompatibleGuava11`
- Remove “Now, do something with table” from standard output when implementing
sequences
- \[ [CALCITE-2444](https://issues.apache.org/jira/browse/CALCITE-2444)\]
Handle `IN` expressions when converting `SqlNode` to SQL (Zoltan Haindrich)
- \[ [CALCITE-2537](https://issues.apache.org/jira/browse/CALCITE-2537)\]
Use litmus for `VolcanoPlanner#validate`
- \[ [CALCITE-2546](https://issues.apache.org/jira/browse/CALCITE-2546)\]
Reduce precision of `Profiler`’s `surprise` and `cardinality` attributes to
avoid floating point discrepancies (Alisha Prabhu)
- \[ [CALCITE-2563](https://issues.apache.org/jira/browse/CALCITE-2563)\]
Materialized view rewriting may swap columns in equivalent classes incorrectly
- \[ [CALCITE-2551](https://issues.apache.org/jira/browse/CALCITE-2551)\]
`SqlToRelConverter` gives `ClassCastException` while handling `IN` inside
`WHERE NOT CASE` (pengzhiwei)
- Remove redundant `new` expression in constant array creation
- \[ [CALCITE-2474](https://issues.apache.org/jira/browse/CALCITE-2474)\]
SqlAdvisor: avoid NPE in lookupFromHints where FROM is empty
- \[ [CALCITE-2418](https://issues.apache.org/jira/browse/CALCITE-2418)\]
Remove `matchRecognize` field of `SqlSelect`
- \[ [CALCITE-2514](https://issues.apache.org/jira/browse/CALCITE-2514)\]
Add `SqlIdentifier` conversion to `ITEM` operator for dynamic tables in
`ExtendedExpander` (Arina Ielchiieva)
- \[ [CALCITE-2491](https://issues.apache.org/jira/browse/CALCITE-2491)\]
Refactor `NameSet`, `NameMap`, and `NameMultimap`
- \[ [CALCITE-2520](https://issues.apache.org/jira/browse/CALCITE-2520)\]
Make `SparkHandlerImpl#compile` silent by default, print code in
`calcite.debug=true` mode only
- \[ [CALCITE-1026](https://issues.apache.org/jira/browse/CALCITE-1026)\]
Remove unused import
- \[ [CALCITE-2483](https://issues.apache.org/jira/browse/CALCITE-2483)\]
Druid adapter, when querying Druid segment metadata, throws when row number is
larger than `Integer.MAX_VALUE` (Hongze Zhang)
- Support `AND`, `OR`, `COALESCE`, `IS [NOT] DISTINCT` in `RexUtil#op`
- \[ [CALCITE-2495](https://issues.apache.org/jira/browse/CALCITE-2495)\]
Support encoded URLs in `org.apache.calcite.util.Source`, and use it for URL
→ File conversion in tests
- \[ [CALCITE-2271](https://issues.apache.org/jira/browse/CALCITE-2271)\]
Join of two views with window aggregates produces incorrect results or throws
`NullPointerException`
- \[ [CALCITE-2481](https://issues.apache.org/jira/browse/CALCITE-2481)\]
`NameSet` assumes lower-case characters have greater codes, which does not hold
for certain characters
- \[ [CALCITE-2480](https://issues.apache.org/jira/browse/CALCITE-2480)\]
`NameSet.contains` wrongly returns `false` when element in set is upper-case
and `seek` is lower-case
- \[ [CALCITE-2465](https://issues.apache.org/jira/browse/CALCITE-2465)\]
Enable use of materialized views for any planner
- \[ [CALCITE-2446](https://issues.apache.org/jira/browse/CALCITE-2446)\]
Lateral joins do not work when saved as custom views (Piotr Bojko)
- \[ [CALCITE-2447](https://issues.apache.org/jira/browse/CALCITE-2447)\]
`POWER`, `ATAN2` functions fail with `NoSuchMethodException`
- Typo in `HepPlanner` trace message (Dylan)
- \[ [CALCITE-2416](https://issues.apache.org/jira/browse/CALCITE-2416)\]
`AssertionError` when determining monotonicity (Alina Ipatina)
- Java 8: use `Map.computeIfAbsent` when possible
- \[ [CALCITE-2431](https://issues.apache.org/jira/browse/CALCITE-2431)\]
`SqlUtil.getAncestry` throws `AssertionError` when providing completion hints
for sub-schema
- \[ [CALCITE-2430](https://issues.apache.org/jira/browse/CALCITE-2430)\]
`RelDataTypeImpl.getFieldList` throws `AssertionError` when SQL Advisor inspects
non-struct field
- \[ [CALCITE-2429](https://issues.apache.org/jira/browse/CALCITE-2429)\]
`SqlValidatorImpl.lookupFieldNamespace` throws `NullPointerException` when SQL
Advisor observes non-existing field
- \[ [CALCITE-2422](https://issues.apache.org/jira/browse/CALCITE-2422)\]
Query with unnest of column from nested sub-query fails when dynamic table is
used
- \[ [CALCITE-2417](https://issues.apache.org/jira/browse/CALCITE-2417)\]
`RelToSqlConverter` throws `ClassCastException` with structs (Benoit Hanotte)
- Upgrades:
  - \[ [CALCITE-2716](https://issues.apache.org/jira/browse/CALCITE-2716)\]
    Upgrade to Avatica 1.13.0
  - \[ [CALCITE-2711](https://issues.apache.org/jira/browse/CALCITE-2711)\]
    Upgrade SQLLine to 1.6.0
  - \[ [CALCITE-2570](https://issues.apache.org/jira/browse/CALCITE-2570)\]
    Upgrade `forbiddenapis` to 2.6 for JDK 11 support
  - \[ [CALCITE-2486](https://issues.apache.org/jira/browse/CALCITE-2486)\]
    Upgrade Apache parent POM to version 21
  - \[ [CALCITE-2467](https://issues.apache.org/jira/browse/CALCITE-2467)\]
    Upgrade `owasp-dependency-check` maven plugin to 3.3.1
  - \[ [CALCITE-2559](https://issues.apache.org/jira/browse/CALCITE-2559)\]
    Update Checkstyle to 7.8.2
  - \[ [CALCITE-2497](https://issues.apache.org/jira/browse/CALCITE-2497)\]
    Update Janino version to 3.0.9
- Expression simplification (`RexSimplify`):

  - \[ [CALCITE-2731](https://issues.apache.org/jira/browse/CALCITE-2731)\]
    `RexProgramBuilder` makes unsafe simplifications to `CASE` expressions (Zoltan
    Haindrich)
  - \[ [CALCITE-2730](https://issues.apache.org/jira/browse/CALCITE-2730)\]
    `RelBuilder` incorrectly simplifies a `Filter` with duplicate conjunction to
    empty (Stamatis Zampetakis)
  - \[ [CALCITE-2726](https://issues.apache.org/jira/browse/CALCITE-2726)\]
    `ReduceExpressionRule` may oversimplify filter conditions containing `NULL`
    values
  - \[ [CALCITE-2695](https://issues.apache.org/jira/browse/CALCITE-2695)\]
    Simplify casts that are only widening nullability (Zoltan Haindrich)
  - \[ [CALCITE-2631](https://issues.apache.org/jira/browse/CALCITE-2631)\]
    General improvements in simplifying `CASE`
  - \[ [CALCITE-2639](https://issues.apache.org/jira/browse/CALCITE-2639)\]
    `FilterReduceExpressionsRule` causes `ArithmeticException` at execution time
  - \[ [CALCITE-2620](https://issues.apache.org/jira/browse/CALCITE-2620)\]
    Simplify `COALESCE(NULL, x)` → `x` (pengzhiwei)
  - \[ [CALCITE-1413](https://issues.apache.org/jira/browse/CALCITE-1413)\]
    Enhance boolean case statement simplifications (Zoltan Haindrich)
  - \[ [CALCITE-2615](https://issues.apache.org/jira/browse/CALCITE-2615)\]
    When simplifying `NOT-AND-OR`, `RexSimplify` incorrectly applies predicates
    deduced for operands to the same operands (Zoltan Haindrich)
  - \[ [CALCITE-2604](https://issues.apache.org/jira/browse/CALCITE-2604)\]
    When simplifying an expression, say whether an `UNKNOWN` value will be
    interpreted as is, or as `TRUE` or `FALSE`
  - \[ [CALCITE-2438](https://issues.apache.org/jira/browse/CALCITE-2438)\]
    Fix wrong results for `IS NOT FALSE(FALSE)` (zhiwei.pzw) (Zoltan Haindrich)
  - \[ [CALCITE-2506](https://issues.apache.org/jira/browse/CALCITE-2506)\]
    Simplifying `COALESCE(+ nullInt, +vInt())` results in
    `AssertionError: result mismatch` (pengzhiwei)
  - \[ [CALCITE-2580](https://issues.apache.org/jira/browse/CALCITE-2580)\]
    Simplifying `COALESCE(NULL > NULL, TRUE)` produces wrong result filter
    expressions (pengzhiwei)
  - \[ [CALCITE-2586](https://issues.apache.org/jira/browse/CALCITE-2586)\]
    `CASE` with repeated branches gives `AssertionError`
    (pengzhiwei)
  - \[ [CALCITE-2590](https://issues.apache.org/jira/browse/CALCITE-2590)\]
    Remove redundant `CAST` when operand has exactly the same type as it is casted to
  - Implement fuzzy generator for `CASE` expressions
  - \[ [CALCITE-2556](https://issues.apache.org/jira/browse/CALCITE-2556)\]
    Simplify `NOT TRUE` → `FALSE`, and `NOT FALSE` → `TRUE` (pengzhiwei)
  - \[ [CALCITE-2581](https://issues.apache.org/jira/browse/CALCITE-2581)\]
    Avoid errors in simplifying `UNKNOWN AND NOT (UNKNOWN OR ...)` (pengzhiwei)
  - \[ [CALCITE-2527](https://issues.apache.org/jira/browse/CALCITE-2527)\]
    Simplify `(c IS NULL) OR (c IS ...)` might result in AssertionError: result
    mismatch (pengzhiwei)
  - Display random failure of Rex fuzzer in build logs to inspire further fixes
  - \[ [CALCITE-2567](https://issues.apache.org/jira/browse/CALCITE-2567)\]
    Simplify `IS NULL(NULL)` to `TRUE` (pengzhiwei)
  - \[ [CALCITE-2555](https://issues.apache.org/jira/browse/CALCITE-2555)\]
    RexSimplify: Simplify `x >= NULL` to `UNKNOWN` (pengzhiwei)
  - \[ [CALCITE-2504](https://issues.apache.org/jira/browse/CALCITE-2504)\]
    Add randomized test for better code coverage of rex node create and
    simplification
  - \[ [CALCITE-2469](https://issues.apache.org/jira/browse/CALCITE-2469)\]
    Simplify `(NOT x) IS NULL` → `x IS NULL` (pengzhiwei);
    also, simplify `f(x, y) IS NULL` → `x IS NULL OR y IS NULL` if `f` is a
    strong operator
  - \[ [CALCITE-2327](https://issues.apache.org/jira/browse/CALCITE-2327)\]
    Simplify `AND(x, y, NOT(y))` → `AND(x, null, IS NULL(y))`
  - \[ [CALCITE-2327](https://issues.apache.org/jira/browse/CALCITE-2327)\]
    Avoid simplification of `x AND NOT(x)` to `FALSE` for nullable `x`
  - \[ [CALCITE-2505](https://issues.apache.org/jira/browse/CALCITE-2505)\]
    `AssertionError` when simplifying `IS [NOT] DISTINCT` expressions
    (Haisheng Yuan)

#### Build and test suite [Permalink](https://calcite.apache.org/docs/history.html\#build-1-18-0 "Permalink")

- \[ [CALCITE-2678](https://issues.apache.org/jira/browse/CALCITE-2678)\]
`RelBuilderTest#testRelBuilderToString` fails on Windows (Stamatis Zampetakis)
- \[ [CALCITE-2660](https://issues.apache.org/jira/browse/CALCITE-2660)\]
`OsAdapterTest` now checks whether required commands are available
- \[ [CALCITE-2655](https://issues.apache.org/jira/browse/CALCITE-2655)\]
Enable Travis to test against JDK 12
- Ensure that tests are not calling `checkSimplify3` with `expected`,
`expectedFalse`, `expectedTrue` all the same
- Geode adapter tests: Removed unnecessary `try/final` block in `RefCountPolicy`
- Add license to `TestKtTest` and add `apache-rat:check` to Travis CI
- \[ [CALCITE-2112](https://issues.apache.org/jira/browse/CALCITE-2112)\]
Add Apache license header to `maven-wrapper.properties`
- \[ [CALCITE-2588](https://issues.apache.org/jira/browse/CALCITE-2588)\]
Run Geode adapter tests with an embedded instance
- \[ [CALCITE-2594](https://issues.apache.org/jira/browse/CALCITE-2594)\]
Ensure `forbiddenapis` and `maven-compiler` use the correct JDK version
- \[ [CALCITE-2642](https://issues.apache.org/jira/browse/CALCITE-2642)\]
Checkstyle complains that `maven-wrapper.properties` is missing a header
- `commons:commons-pool2` is used in tests only, so use `scope=test` for it
- Make `findbugs:jsr305` dependency optional
- \[ [CALCITE-2458](https://issues.apache.org/jira/browse/CALCITE-2458)\]
Add Kotlin as a test dependency
- Make build scripts Maven 3.3 compatible
- Fix JavaDoc warnings for Java 9+, and check JavaDoc in Travis CI
- Unwrap invocation target exception from QuidemTest#test
- \[ [CALCITE-2518](https://issues.apache.org/jira/browse/CALCITE-2518)\]
Add `failOnWarnings` to `maven-javadoc-plugin` configuration
- Silence Pig, Spark, and Elasticsearch logs in tests
- \[ [CALCITE-1894](https://issues.apache.org/jira/browse/CALCITE-1894)\]
`CsvTest.testCsvStream` failing often: add `@Ignore` since the test is known to
fail
- \[ [CALCITE-2535](https://issues.apache.org/jira/browse/CALCITE-2535)\]
Enable `SqlTester.checkFails` (previously it was a no-op) (Hongze Zhang)
- \[ [CALCITE-2558](https://issues.apache.org/jira/browse/CALCITE-2558)\]
Improve re-compilation times by skipping `parser.java` update on each build
- Increase timeout for Cassandra daemon startup for `CassandraAdapterTest`
- \[ [CALCITE-2412](https://issues.apache.org/jira/browse/CALCITE-2412)\]
Add Windows CI via AppVeyor (Sergey Nuyanzin)
- Reduce `HepPlannerTest#testRuleApplyCount` complexity
- \[ [CALCITE-2523](https://issues.apache.org/jira/browse/CALCITE-2523)\]
Guard `PartiallyOrderedSetTest#testPosetBitsLarge` with
`CalciteAssert.ENABLE_SLOW`
- \[ [CALCITE-2521](https://issues.apache.org/jira/browse/CALCITE-2521)\]
Guard `RelMetadataTest#testMetadataHandlerCacheLimit` with
`CalciteAssert.ENABLE_SLOW`
- \[ [CALCITE-2484](https://issues.apache.org/jira/browse/CALCITE-2484)\]
Add `SqlValidatorDynamicTest` to `CalciteSuite`
- \[ [CALCITE-2484](https://issues.apache.org/jira/browse/CALCITE-2484)\]
Move dynamic tests to a separate class like `SqlValidatorDynamicTest`, and
avoid reuse of `MockCatalogReaderDynamic`
- \[ [CALCITE-2522](https://issues.apache.org/jira/browse/CALCITE-2522)\]
Remove `e.printStackTrace()` from `CalciteAssert#returns`
- \[ [CALCITE-2512](https://issues.apache.org/jira/browse/CALCITE-2512)\]
Move `StreamTest#ROW_GENERATOR` to `Table.scan().iterator` to make it not
shared between threads (Sergey Nuyanzin)
- Skip second Checkstyle execution during Travis CI build
- \[ [CALCITE-2519](https://issues.apache.org/jira/browse/CALCITE-2519)\]
Silence ERROR logs from `CalciteException`, `SqlValidatorException` during
tests
- \[ [CALCITE-1026](https://issues.apache.org/jira/browse/CALCITE-1026)\]
Fix `ModelTest#testYamlFileDetection` when source folder has spaces
- `MockCatalogReader` is used in testing, so cache should be disabled there to
avoid thread conflicts and/or stale results
- \[ [CALCITE-311](https://issues.apache.org/jira/browse/CALCITE-311)\]
Add a test-case for Filter after Window aggregate
- \[ [CALCITE-2462](https://issues.apache.org/jira/browse/CALCITE-2462)\]
`RexProgramTest`: replace `nullLiteral` → `nullInt`,
`unknownLiteral` → `nullBool` for brevity
- \[ [CALCITE-2462](https://issues.apache.org/jira/browse/CALCITE-2462)\]
`RexProgramTest`: move “rex building” methods to base class
- `SqlTestFactory`: use lazy initialization of objects
- \[ [CALCITE-2435](https://issues.apache.org/jira/browse/CALCITE-2435)\]
Refactor `SqlTestFactory`
- \[ [CALCITE-2428](https://issues.apache.org/jira/browse/CALCITE-2428)\]
Cassandra unit test fails to parse JDK version string (Andrei Sereda)
- \[ [CALCITE-2419](https://issues.apache.org/jira/browse/CALCITE-2419)\]
Use embedded Cassandra for tests

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-18-0 "Permalink")

- Add geospatial category to DOAP file
- \[ [CALCITE-2577](https://issues.apache.org/jira/browse/CALCITE-2577)\]
Update links on download page to HTTPS
- \[ [CALCITE-2574](https://issues.apache.org/jira/browse/CALCITE-2574)\]
Update download page to include instructions for verifying a downloaded
artifact
- Update build status badges in `README.md`
- \[ [CALCITE-2705](https://issues.apache.org/jira/browse/CALCITE-2705)\]
Site: Remove duplicate “selectivity” in list of metadata types (Alan Jin)
- Site: Add Andrei Sereda as committer
- Site: Update Julian Hyde’s affiliation
- Update Michael Mior’s affiliation
- Site: Add instructions for updating PRs based on the discussion in the dev
list (Stamatis Zampetakis)
- Site: Add committer Sergey Nuyanzin
- Site: News item for release 1.17.0

## [1.17.0](https://github.com/apache/calcite/releases/tag/calcite-1.17.0) / 2018-07-16 [Permalink](https://calcite.apache.org/docs/history.html\#v1-17-0 "Permalink")

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10;
Guava versions 19.0 to 23.0;
Druid version 0.11.0;
other software versions as specified in `pom.xml`.

This release comes four months after 1.16.0. It includes more than 90 resolved
issues, comprising a large number of new features as well as general improvements
and bug-fixes. Among others:

Implemented [Babel SQL parser](https://issues.apache.org/jira/browse/CALCITE-2280)
that accepts all SQL dialects.
Allowed [JDK 8 language level](https://issues.apache.org/jira/browse/CALCITE-2261) for core module.
Calcite has been upgraded to use [Avatica 1.12.0](https://issues.apache.org/jira/browse/CALCITE-2365)

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-17-0 "Permalink")

- \[ [CALCITE-873](https://issues.apache.org/jira/browse/CALCITE-873)\]
Add a planner rule, `SortRemoveConstantKeysRule`, that removes constant keys from Sort (Atri Sharma)
- \[ [CALCITE-2045](https://issues.apache.org/jira/browse/CALCITE-2045)\]
`CREATE TYPE` (Shuyi Chen)
- \[ [CALCITE-2216](https://issues.apache.org/jira/browse/CALCITE-2216)\]
Improve extensibility of `AggregateReduceFunctionsRule` (Fabian Hueske)
- \[ [CALCITE-2227](https://issues.apache.org/jira/browse/CALCITE-2227)\]
Standards-compliant column ordering for `NATURAL JOIN` and `JOIN USING`
- \[ [CALCITE-2280](https://issues.apache.org/jira/browse/CALCITE-2280)\]
Babel SQL parser
- \[ [CALCITE-2286](https://issues.apache.org/jira/browse/CALCITE-2286)\]
Support timestamp type for Druid adapter
- \[ [CALCITE-2304](https://issues.apache.org/jira/browse/CALCITE-2304)\]
In Babel parser, allow Hive-style syntax `LEFT SEMI JOIN`
- \[ [CALCITE-2321](https://issues.apache.org/jira/browse/CALCITE-2321)\]
A union of `CHAR` columns of different lengths can now (based on a conformance setting) yield a `VARCHAR` column (Hequn Cheng)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-17-0 "Permalink")

- \[ [CALCITE-531](https://issues.apache.org/jira/browse/CALCITE-531)\]
`LATERAL` combined with window function or table function
- \[ [CALCITE-1167](https://issues.apache.org/jira/browse/CALCITE-1167)\]
`OVERLAPS` should match even if operands are in (high, low) order
- \[ [CALCITE-1436](https://issues.apache.org/jira/browse/CALCITE-1436)\]
Support `MIN`/`MAX` functions (Muhammad Gelbana)
- \[ [CALCITE-1866](https://issues.apache.org/jira/browse/CALCITE-1866)\]
JDBC adapter generates incorrect code when pushing `FLOOR` to MySQL (Kang Wang, Sergey Nuyanzin)
- \[ [CALCITE-1916](https://issues.apache.org/jira/browse/CALCITE-1916)\]
Use Teradata’s TPC-DS generator and run tests against TPC-DS at small scale
- \[ [CALCITE-1949](https://issues.apache.org/jira/browse/CALCITE-1949)\]
`CalciteStatement` should call `AvaticaStatement` close\_(), to avoid memory leak (Kevin Risden)
- \[ [CALCITE-2053](https://issues.apache.org/jira/browse/CALCITE-2053)\]
Resolve Java user-defined functions that have `Double` and `BigDecimal` arguments (余启)
- \[ [CALCITE-2063](https://issues.apache.org/jira/browse/CALCITE-2063)\]
Add JDK 10 to `.travis.yml`
- \[ [CALCITE-2159](https://issues.apache.org/jira/browse/CALCITE-2159)\]
Support dynamic row type in `UNNEST` (Chunhui Shi)
- \[ [CALCITE-2164](https://issues.apache.org/jira/browse/CALCITE-2164)\]
Fix alerts raised by lgtm.com (Malcolm Taylor)
- \[ [CALCITE-2188](https://issues.apache.org/jira/browse/CALCITE-2188)\]
JDBC adapter generates invalid SQL for `DATE`/`INTERVAL` arithmetic (Rahul Raj)
- \[ [CALCITE-2201](https://issues.apache.org/jira/browse/CALCITE-2201)\]
Pass `RelBuilder` into `RelDecorrelator` and `RelStructuredTypeFlattener` (Volodymyr Vysotskyi)
- \[ [CALCITE-2205](https://issues.apache.org/jira/browse/CALCITE-2205)\]
`JoinPushTransitivePredicatesRule` should not create `Filter` on top of equivalent `Filter` (Vitalii Diravka)
- \[ [CALCITE-2206](https://issues.apache.org/jira/browse/CALCITE-2206)\]
JDBC adapter incorrectly pushes windowed aggregates down to HSQLDB (Pavel Gubin)
- \[ [CALCITE-2220](https://issues.apache.org/jira/browse/CALCITE-2220)\]
`SqlToRelConverter` generates incorrect ordinal while flattening a record-valued field (Shuyi Chen)
- \[ [CALCITE-2222](https://issues.apache.org/jira/browse/CALCITE-2222)\]
Add Quarter timeunit as a valid unit to pushdown to Druid
- \[ [CALCITE-2225](https://issues.apache.org/jira/browse/CALCITE-2225)\]
Upgrade Apache parent POM to version 19, and support OpenJDK 10
- \[ [CALCITE-2226](https://issues.apache.org/jira/browse/CALCITE-2226)\]
Druid adapter: Substring operator converter does not handle non-constant literals correctly
- \[ [CALCITE-2229](https://issues.apache.org/jira/browse/CALCITE-2229)\]
Allow sqlsh to be run from path, not just current directory
- \[ [CALCITE-2232](https://issues.apache.org/jira/browse/CALCITE-2232)\]
Assertion error on `AggregatePullUpConstantsRule` while adjusting `Aggregate` indices
- \[ [CALCITE-2236](https://issues.apache.org/jira/browse/CALCITE-2236)\]
Druid adapter: Avoid duplication of fields names during Druid query planing
- \[ [CALCITE-2237](https://issues.apache.org/jira/browse/CALCITE-2237)\]
Upgrade Maven Surefire plugin to 2.21.0 (Kevin Risden)
- \[ [CALCITE-2238](https://issues.apache.org/jira/browse/CALCITE-2238)\]
Fix Pig and Spark adapter failures with JDK 10
- \[ [CALCITE-2240](https://issues.apache.org/jira/browse/CALCITE-2240)\]
Extend rule to push predicates into `CASE` statement (Zoltan Haindrich)
- \[ [CALCITE-2242](https://issues.apache.org/jira/browse/CALCITE-2242)\]
Using custom `RelBuilder` for `FilterRemoveIsNotDistinctFromRule` (Vitalii Diravka)
- \[ [CALCITE-2247](https://issues.apache.org/jira/browse/CALCITE-2247)\]
Simplify `AND` and `OR` conditions using predicates (Zoltan Haindrich)
- \[ [CALCITE-2253](https://issues.apache.org/jira/browse/CALCITE-2253)\]
Fix matching predicate for `JdbcProjectRule` rule
- \[ [CALCITE-2255](https://issues.apache.org/jira/browse/CALCITE-2255)\]
Add JDK 11 to Travis CI
- \[ [CALCITE-2259](https://issues.apache.org/jira/browse/CALCITE-2259)\]
Allow Java 8 syntax
- \[ [CALCITE-2261](https://issues.apache.org/jira/browse/CALCITE-2261)\]
Switch core module to JDK 8 (Enrico Olivelli)
- \[ [CALCITE-2262](https://issues.apache.org/jira/browse/CALCITE-2262)\]
Druid adapter: Allow count(\*) to be pushed when other aggregate functions are present
- \[ [CALCITE-2264](https://issues.apache.org/jira/browse/CALCITE-2264)\]
In JDBC adapter, do not push down a call to a user-defined function (UDF) (Piotr Bojko)
- \[ [CALCITE-2265](https://issues.apache.org/jira/browse/CALCITE-2265)\]
Allow comparison of ROW values (Dylan Adams)
- \[ [CALCITE-2267](https://issues.apache.org/jira/browse/CALCITE-2267)\]
Thread-safe generation of `AbstractRelNode.id` (Zhong Yu)
- \[ [CALCITE-2275](https://issues.apache.org/jira/browse/CALCITE-2275)\]
Do not push down `NOT` condition in `JOIN` (Vitalii Diravka)
- \[ [CALCITE-2276](https://issues.apache.org/jira/browse/CALCITE-2276)\]
Allow explicit `ROW` value constructor in `SELECT` clause and elsewhere (Danny Chan)
- \[ [CALCITE-2277](https://issues.apache.org/jira/browse/CALCITE-2277)\]
Skip `SemiJoin` operator in materialized view-based rewriting algorithm
- \[ [CALCITE-2278](https://issues.apache.org/jira/browse/CALCITE-2278)\]
`AggregateJoinTransposeRule` fails to split aggregate call if input contains an aggregate call and has distinct rows (Haisheng Yuan)
- \[ [CALCITE-2281](https://issues.apache.org/jira/browse/CALCITE-2281)\]
Return type of the `TIMESTAMPADD` function has wrong precision (Sudheesh Katkam)
- \[ [CALCITE-2287](https://issues.apache.org/jira/browse/CALCITE-2287)\]
`FlatList.equals()` throws `StackOverflowError` (Zhen Wang, Zhong Yu)
- \[ [CALCITE-2291](https://issues.apache.org/jira/browse/CALCITE-2291)\]
Support Push Project past Correlate (Chunhui Shi)
- \[ [CALCITE-2293](https://issues.apache.org/jira/browse/CALCITE-2293)\]
Upgrade forbidden-apis to 2.5 (for JDK 10)
- \[ [CALCITE-2299](https://issues.apache.org/jira/browse/CALCITE-2299)\]
`TIMESTAMPADD`(`SQL_TSI_FRAC_SECOND`) should be nanoseconds (Sergey Nuyanzin)
- \[ [CALCITE-2303](https://issues.apache.org/jira/browse/CALCITE-2303)\]
In `EXTRACT` function, support `MICROSECONDS`, `MILLISECONDS`, `EPOCH`, `ISODOW`, `ISOYEAR` and `DECADE` time units (Sergey Nuyanzin)
- \[ [CALCITE-2305](https://issues.apache.org/jira/browse/CALCITE-2305)\]
JDBC adapter generates invalid casts on Postgres, because Postgres does not have `TINYINT` and `DOUBLE` types
- \[ [CALCITE-2306](https://issues.apache.org/jira/browse/CALCITE-2306)\]
AssertionError in `RexLiteral.getValue3` with null literal of type `DECIMAL` (Godfrey He)
- \[ [CALCITE-2309](https://issues.apache.org/jira/browse/CALCITE-2309)\]
Dialects: Hive dialect does not support charsets in constants
- \[ [CALCITE-2314](https://issues.apache.org/jira/browse/CALCITE-2314)\]
Verify RexNode transformations by evaluating before and after expressions against sample values
- \[ [CALCITE-2316](https://issues.apache.org/jira/browse/CALCITE-2316)\]
Elasticsearch adapter should not convert queries to lower-case (Andrei Sereda)
- \[ [CALCITE-2318](https://issues.apache.org/jira/browse/CALCITE-2318)\]
`NumberFormatException` while starting SQLLine
- \[ [CALCITE-2319](https://issues.apache.org/jira/browse/CALCITE-2319)\]
Set correct dimension type for druid expressions with result type boolean (nsihantmonu51)
- \[ [CALCITE-2320](https://issues.apache.org/jira/browse/CALCITE-2320)\]
Filtering UDF when converting `Filter` to `JDBCFilter` (Piotr Bojko)
- \[ [CALCITE-2323](https://issues.apache.org/jira/browse/CALCITE-2323)\]
Apply “`defaultNullCollation`” configuration parameter when translating `ORDER BY` inside `OVER` (John Fang)
- \[ [CALCITE-2324](https://issues.apache.org/jira/browse/CALCITE-2324)\]
`EXTRACT` function: `HOUR`, `MINUTE` and `SECOND` parts of a `DATE` must be zero (Sergey Nuyanzin)
- \[ [CALCITE-2329](https://issues.apache.org/jira/browse/CALCITE-2329)\]
Improve rewrite for “constant IN (sub-query)”
- \[ [CALCITE-2331](https://issues.apache.org/jira/browse/CALCITE-2331)\]
Evaluation of predicate `(A or B) and C` fails for Elasticsearch adapter (Andrei Sereda)
- \[ [CALCITE-2332](https://issues.apache.org/jira/browse/CALCITE-2332)\]
Wrong simplification of `FLOOR(CEIL(x))` to `FLOOR(x)`
- \[ [CALCITE-2333](https://issues.apache.org/jira/browse/CALCITE-2333)\]
Stop releasing zips
- \[ [CALCITE-2334](https://issues.apache.org/jira/browse/CALCITE-2334)\]
Extend simplification of expressions with `CEIL` function over date types
- \[ [CALCITE-2341](https://issues.apache.org/jira/browse/CALCITE-2341)\]
Fix `ImmutableBitSetTest` for jdk11
- \[ [CALCITE-2342](https://issues.apache.org/jira/browse/CALCITE-2342)\]
Fix improper use of assert
- \[ [CALCITE-2345](https://issues.apache.org/jira/browse/CALCITE-2345)\]
Running Unit tests with Fongo and integration tests with real mongo instance (Andrei Sereda)
- \[ [CALCITE-2347](https://issues.apache.org/jira/browse/CALCITE-2347)\]
Running ElasticSearch in embedded mode for unit tests of ES adapter (Andrei Sereda)
- \[ [CALCITE-2353](https://issues.apache.org/jira/browse/CALCITE-2353)\]
Allow user to override `SqlSetOption` (Andrew Pilloud)
- \[ [CALCITE-2355](https://issues.apache.org/jira/browse/CALCITE-2355)\]
Implement multiset operations (Sergey Nuyanzin)
- \[ [CALCITE-2357](https://issues.apache.org/jira/browse/CALCITE-2357)\]
Freemarker dependency override issue in fmpp maven plugin (yanghua)
- \[ [CALCITE-2358](https://issues.apache.org/jira/browse/CALCITE-2358)\]
Use null literal instead of empty string (b-slim)
- \[ [CALCITE-2359](https://issues.apache.org/jira/browse/CALCITE-2359)\]
Inconsistent results casting intervals to integers (James Duong)
- \[ [CALCITE-2364](https://issues.apache.org/jira/browse/CALCITE-2364)\]
Fix timezone issue (in test) between Mongo DB and local JVM (Andrei Sereda)
- \[ [CALCITE-2365](https://issues.apache.org/jira/browse/CALCITE-2365)\]
Upgrade avatica to 1.12
- \[ [CALCITE-2366](https://issues.apache.org/jira/browse/CALCITE-2366)\]
Add support for `ANY_VALUE` aggregate function (Gautam Parai)
- \[ [CALCITE-2368](https://issues.apache.org/jira/browse/CALCITE-2368)\]
Fix `misc.iq` and `scalar.iq` quidem unit tests failures on Windows
- \[ [CALCITE-2369](https://issues.apache.org/jira/browse/CALCITE-2369)\]
Fix `OsAdapterTest` failure on windows (Sergey Nuyanzin)
- \[ [CALCITE-2370](https://issues.apache.org/jira/browse/CALCITE-2370)\]
Fix failing mongo IT tests when explicit order was not specified (Andrei Sereda)
- \[ [CALCITE-2376](https://issues.apache.org/jira/browse/CALCITE-2376)\]
Unify ES2 and ES5 adapters. Migrate to low-level ES rest client as main transport (Andrei Sereda)
- \[ [CALCITE-2379](https://issues.apache.org/jira/browse/CALCITE-2379)\]
CVSS dependency-check-maven fails for calcite-spark and calcite-ubenchmark modules
- \[ [CALCITE-2380](https://issues.apache.org/jira/browse/CALCITE-2380)\]
Javadoc generation failure in Elasticsearch2 adapter (Andrei Sereda)
- \[ [CALCITE-2381](https://issues.apache.org/jira/browse/CALCITE-2381)\]
Add information for authenticating against maven repo, GPG keys and version numbers to HOWTO
- \[ [CALCITE-2382](https://issues.apache.org/jira/browse/CALCITE-2382)\]
Sub-query join lateral table function (pengzhiwei)
- \[ [CALCITE-2383](https://issues.apache.org/jira/browse/CALCITE-2383)\]
`NTH_VALUE` window function (Sergey Nuyanzin)
- \[ [CALCITE-2384](https://issues.apache.org/jira/browse/CALCITE-2384)\]
Performance issue in `getPulledUpPredicates` (Zoltan Haindrich)
- \[ [CALCITE-2387](https://issues.apache.org/jira/browse/CALCITE-2387)\]
Fix for `date`/`timestamp` cast expressions in Druid adapter
- \[ [CALCITE-2388](https://issues.apache.org/jira/browse/CALCITE-2388)\]
Upgrade from `commons-dbcp` to `commons-dbcp2` version 2.4.0
- \[ [CALCITE-2391](https://issues.apache.org/jira/browse/CALCITE-2391)\]
Aggregate query with `UNNEST` or `LATERAL` fails with `ClassCastException`
- \[ [CALCITE-2392](https://issues.apache.org/jira/browse/CALCITE-2392)\]
Prevent columns permutation for `NATURAL JOIN` and `JOIN USING` when dynamic table is used
- \[ [CALCITE-2396](https://issues.apache.org/jira/browse/CALCITE-2396)\]
Allow `NULL` intervals in `TIMESTAMPADD` and `DATETIME_PLUS` functions (James Duong)
- \[ [CALCITE-2398](https://issues.apache.org/jira/browse/CALCITE-2398)\]
`SqlSelect` must call into `SqlDialect` for unparse (James Duong)
- \[ [CALCITE-2403](https://issues.apache.org/jira/browse/CALCITE-2403)\]
Upgrade quidem to 0.9
- \[ [CALCITE-2409](https://issues.apache.org/jira/browse/CALCITE-2409)\]
`SparkAdapterTest` fails on Windows when ‘/tmp’ directory does not exist
(Sergey Nuyanzin)

## [1.16.0](https://github.com/apache/calcite/releases/tag/calcite-1.16.0) / 2018-03-14 [Permalink](https://calcite.apache.org/docs/history.html\#v1-16-0 "Permalink")

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 8, 9, 10;
Guava versions 19.0 to 23.0;
Druid version 0.11.0;
other software versions as specified in `pom.xml`.

This release comes three months after 1.15.0. It includes more than 80 resolved
issues, comprising a large number of new features as well as general improvements
and bug-fixes to Calcite core. Among others:

- Calcite has been upgraded to use
[Avatica 1.11.0](https://issues.apache.org/jira/browse/CALCITE-2182),
which was recently released.
- Moreover, a new adapter to
[read data from Apache Geode](https://issues.apache.org/jira/browse/CALCITE-2059)
was added in this release. In addition, more progress has been made for the existing adapters,
e.g., the Druid adapter can generate
[`SCAN` queries rather than `SELECT` queries](https://issues.apache.org/jira/browse/CALCITE-2077)
for more efficient execution and it can push
[more work to Druid using its new expressions capabilities](https://issues.apache.org/jira/browse/CALCITE-2170),
and the JDBC adapter now [supports the SQL dialect used by Jethro Data](https://issues.apache.org/jira/browse/CALCITE-2128).
- Finally, this release
[drops support for JDK 1.7](https://issues.apache.org/jira/browse/CALCITE-2027) and
support for [Guava versions earlier than 19](https://issues.apache.org/jira/browse/CALCITE-2191).

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-16-0 "Permalink")

- \[ [CALCITE-1265](https://issues.apache.org/jira/browse/CALCITE-1265)\]
In JDBC adapter, push `OFFSET` and `FETCH` to data source
- \[ [CALCITE-2059](https://issues.apache.org/jira/browse/CALCITE-2059)\]
Apache Geode adapter (Christian Tzolov)
- \[ [CALCITE-2077](https://issues.apache.org/jira/browse/CALCITE-2077)\]
Druid adapter: Use `SCAN` query rather than `SELECT` query (Nishant Bangarwa)
- \[ [CALCITE-2128](https://issues.apache.org/jira/browse/CALCITE-2128)\]
In JDBC adapter, add SQL dialect for Jethro Data (Jonathan Doron)
- \[ [CALCITE-2170](https://issues.apache.org/jira/browse/CALCITE-2170)\]
Use Druid Expressions capabilities to improve the amount of work that can be pushed to Druid

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-16-0 "Permalink")

- \[ [CALCITE-1054](https://issues.apache.org/jira/browse/CALCITE-1054)\]
NPE caused by wrong code generation for Timestamp fields
- \[ [CALCITE-1188](https://issues.apache.org/jira/browse/CALCITE-1188)\]
NullPointerException in `EXTRACT` with `WHERE ... IN` clause if field has null value
- \[ [CALCITE-1427](https://issues.apache.org/jira/browse/CALCITE-1427)\]
Code generation incorrect (does not compile) for DATE, TIME and TIMESTAMP fields
- \[ [CALCITE-1658](https://issues.apache.org/jira/browse/CALCITE-1658)\]
DateRangeRules incorrectly rewrites `EXTRACT` calls (Nishant Bangarwa)
- \[ [CALCITE-1697](https://issues.apache.org/jira/browse/CALCITE-1697)\]
Update Mongo driver version to 3.5.0 (Vladimir Dolzhenko)
- \[ [CALCITE-2002](https://issues.apache.org/jira/browse/CALCITE-2002)\]
`DISTINCT` applied to `VALUES` returns wrong result
- \[ [CALCITE-2009](https://issues.apache.org/jira/browse/CALCITE-2009)\]
Possible bug in interpreting `( IN ) OR ( IN )` logic
- \[ [CALCITE-2020](https://issues.apache.org/jira/browse/CALCITE-2020)\]
Upgrade org.incava java-diff
- \[ [CALCITE-2027](https://issues.apache.org/jira/browse/CALCITE-2027)\]
Drop support for Java 7 (JDK 1.7)
- \[ [CALCITE-2034](https://issues.apache.org/jira/browse/CALCITE-2034)\]
`FileReaderTest` fails with path containing spaces
- \[ [CALCITE-2066](https://issues.apache.org/jira/browse/CALCITE-2066)\]
`RelOptUtil.splitJoinCondition()` could not split condition with case after applying `FilterReduceExpressionsRule` (Volodymyr Vysotskyi)
- \[ [CALCITE-2071](https://issues.apache.org/jira/browse/CALCITE-2071)\]
Query with `IN` and `OR` in `WHERE` clause returns wrong result (Vineet Garg)
- \[ [CALCITE-2072](https://issues.apache.org/jira/browse/CALCITE-2072)\]
Enable spatial functions by adding ‘fun=spatial’ to JDBC connect string
- \[ [CALCITE-2075](https://issues.apache.org/jira/browse/CALCITE-2075)\]
SparkAdapterTest UT fails
- \[ [CALCITE-2076](https://issues.apache.org/jira/browse/CALCITE-2076)\]
Upgrade to Druid 0.11.0 (Nishant Bangarwa)
- \[ [CALCITE-2080](https://issues.apache.org/jira/browse/CALCITE-2080)\]
Query with `NOT IN` operator and literal throws `AssertionError`: ‘Cast for just nullability not allowed’ (Volodymyr Vysotskyi)
- \[ [CALCITE-2081](https://issues.apache.org/jira/browse/CALCITE-2081)\]
Query with windowed aggregates under both sides of a `JOIN` throws `NullPointerException` (Zhen Wang)
- \[ [CALCITE-2084](https://issues.apache.org/jira/browse/CALCITE-2084)\]
`SqlValidatorImpl.findTable()` method incorrectly handles table schema with few schema levels (Volodymyr Vysotskyi)
- \[ [CALCITE-2088](https://issues.apache.org/jira/browse/CALCITE-2088)\]
Add more complex end-to-end tests in “plus” module, using Chinook data set (Piotr Bojko)
- \[ [CALCITE-2089](https://issues.apache.org/jira/browse/CALCITE-2089)\]
Druid adapter: Push filter on `floor(time)` to Druid (Nishant Bangarwa)
- \[ [CALCITE-2090](https://issues.apache.org/jira/browse/CALCITE-2090)\]
Extend Druid Range Rules to extract interval from Floor (Nishant Bangarwa)
- \[ [CALCITE-2091](https://issues.apache.org/jira/browse/CALCITE-2091)\]
Improve DruidQuery cost function, to ensure that `EXTRACT` gets pushed as an interval if possible
- \[ [CALCITE-2092](https://issues.apache.org/jira/browse/CALCITE-2092)\]
Allow passing custom `RelBuilder` into `SqlToRelConverter`
- \[ [CALCITE-2093](https://issues.apache.org/jira/browse/CALCITE-2093)\]
`OsAdapterTest` in Calcite Plus does not respect locale (Piotr Bojko)
- \[ [CALCITE-2094](https://issues.apache.org/jira/browse/CALCITE-2094)\]
Druid adapter: `Count(*)` returns null instead of 0 when condition filters all rows
- \[ [CALCITE-2095](https://issues.apache.org/jira/browse/CALCITE-2095)\]
Druid adapter: Push always true and always true expressions as Expression Filters
- \[ [CALCITE-2096](https://issues.apache.org/jira/browse/CALCITE-2096)\]
Druid adapter: Remove extra `dummy_aggregator`
- \[ [CALCITE-2097](https://issues.apache.org/jira/browse/CALCITE-2097)\]
Druid adapter: Push Aggregate and Filter operators containing metric columns to Druid
- \[ [CALCITE-2098](https://issues.apache.org/jira/browse/CALCITE-2098)\]
Push filters to Druid Query Scan when we have `OR` of `AND` clauses
- \[ [CALCITE-2099](https://issues.apache.org/jira/browse/CALCITE-2099)\]
Code generated for `GROUP BY` inside `UNION` does not compile (Zhen Wang)
- \[ [CALCITE-2101](https://issues.apache.org/jira/browse/CALCITE-2101)\]
Druid adapter: Push count(column) using Druid filtered aggregate
- \[ [CALCITE-2102](https://issues.apache.org/jira/browse/CALCITE-2102)\]
Ignore duplicate `ORDER BY` keys, and ensure RelCollation contains no duplicates (John Fang)
- \[ [CALCITE-2104](https://issues.apache.org/jira/browse/CALCITE-2104)\]
Add separate rules for `AggregateUnionAggregateRule` to reduce potential matching cost in `VolcanoPlanner` (lincoln-lil)
- \[ [CALCITE-2105](https://issues.apache.org/jira/browse/CALCITE-2105)\]
`AggregateJoinTransposeRule` fails when process aggregate without group keys (jingzhang)
- \[ [CALCITE-2107](https://issues.apache.org/jira/browse/CALCITE-2107)\]
Timezone not passed as part of granularity when passing `TimeExtractionFunction` to Druid (Nishant Bangarwa)
- \[ [CALCITE-2108](https://issues.apache.org/jira/browse/CALCITE-2108)\]
`AggregateJoinTransposeRule` fails when process aggregateCall above `SqlSumEmptyIsZeroAggFunction` without groupKeys (jingzhang)
- \[ [CALCITE-2110](https://issues.apache.org/jira/browse/CALCITE-2110)\]
`ArrayIndexOutOfBoundsException` in RexSimplify when using `ReduceExpressionsRule.JOIN_INSTANCE`
- \[ [CALCITE-2111](https://issues.apache.org/jira/browse/CALCITE-2111)\]
Make HepPlanner more efficient by applying rules depth-first
- \[ [CALCITE-2113](https://issues.apache.org/jira/browse/CALCITE-2113)\]
Push column pruning to druid when Aggregate cannot be pushed (Nishant Bangarwa)
- \[ [CALCITE-2114](https://issues.apache.org/jira/browse/CALCITE-2114)\]
Re-enable `DruidAggregateFilterTransposeRule`
- \[ [CALCITE-2116](https://issues.apache.org/jira/browse/CALCITE-2116)\]
The digests are not same for the common sub-expressions in HepPlanner (LeoWangLZ)
- \[ [CALCITE-2118](https://issues.apache.org/jira/browse/CALCITE-2118)\]
RelToSqlConverter should only generate “\*” if field names match (Sam Waggoner)
- \[ [CALCITE-2122](https://issues.apache.org/jira/browse/CALCITE-2122)\]
In DateRangeRules, make either `TIMESTAMP` or `DATE` literal, according to target type (Nishant Bangarwa)
- \[ [CALCITE-2124](https://issues.apache.org/jira/browse/CALCITE-2124)\]
`AggregateExpandDistinctAggregatesRule` should make `SUM` nullable if there is no `GROUP BY` (Godfrey He)
- \[ [CALCITE-2127](https://issues.apache.org/jira/browse/CALCITE-2127)\]
In Interpreter, allow a node to have more than one consumer
- \[ [CALCITE-2133](https://issues.apache.org/jira/browse/CALCITE-2133)\]
Allow SqlGroupedWindowFunction to specify returnTypeInference in its constructor (Shuyi Chen)
- \[ [CALCITE-2135](https://issues.apache.org/jira/browse/CALCITE-2135)\]
If there is an aggregate function inside an `OVER` clause, validator should treat query as an aggregate query (Volodymyr Tkach)
- \[ [CALCITE-2137](https://issues.apache.org/jira/browse/CALCITE-2137)\]
Materialized view rewriting not being triggered for some join queries
- \[ [CALCITE-2139](https://issues.apache.org/jira/browse/CALCITE-2139)\]
Upgrade checkstyle
- \[ [CALCITE-2143](https://issues.apache.org/jira/browse/CALCITE-2143)\]
RelToSqlConverter produces incorrect SQL with aggregation (Sam Waggoner)
- \[ [CALCITE-2147](https://issues.apache.org/jira/browse/CALCITE-2147)\]
GroupingSets involving rollup resulting into an incorrect plan (Ravindar Munjam)
- \[ [CALCITE-2154](https://issues.apache.org/jira/browse/CALCITE-2154)\]
Upgrade jackson to 2.9.4
- \[ [CALCITE-2156](https://issues.apache.org/jira/browse/CALCITE-2156)\]
In DateRangeRules, compute `FLOOR` and `CEIL` of `TIMESTAMP WITH LOCAL TIMEZONE` in local time zone (Nishant Bangarwa)
- \[ [CALCITE-2162](https://issues.apache.org/jira/browse/CALCITE-2162)\]
Exception when accessing sub-field of sub-field of composite Array element (Shuyi Chen)
- \[ [CALCITE-2178](https://issues.apache.org/jira/browse/CALCITE-2178)\]
Extend expression simplifier to work on datetime `CEIL`/`FLOOR` functions
- \[ [CALCITE-2179](https://issues.apache.org/jira/browse/CALCITE-2179)\]
General improvements for materialized view rewriting rule
- \[ [CALCITE-2180](https://issues.apache.org/jira/browse/CALCITE-2180)\]
Invalid code generated for negative of byte and short values
- \[ [CALCITE-2183](https://issues.apache.org/jira/browse/CALCITE-2183)\]
Implement `RelSubset.copy` method (Alessandro Solimando)
- \[ [CALCITE-2185](https://issues.apache.org/jira/browse/CALCITE-2185)\]
Additional unit tests for Spark Adapter (Alessandro Solimando)
- \[ [CALCITE-2187](https://issues.apache.org/jira/browse/CALCITE-2187)\]
Fix build issue caused by `CALCITE-2170`
- \[ [CALCITE-2189](https://issues.apache.org/jira/browse/CALCITE-2189)\]
RelMdAllPredicates fast bail out creates mismatch with RelMdTableReferences
- \[ [CALCITE-2190](https://issues.apache.org/jira/browse/CALCITE-2190)\]
Extend SubstitutionVisitor.splitFilter to cover different order of operands
- \[ [CALCITE-2191](https://issues.apache.org/jira/browse/CALCITE-2191)\]
Drop support for Guava versions earlier than 19
- \[ [CALCITE-2192](https://issues.apache.org/jira/browse/CALCITE-2192)\]
RelBuilder wrongly skips creating an Aggregate that prunes columns, if input is unique
- \[ [CALCITE-2195](https://issues.apache.org/jira/browse/CALCITE-2195)\]
`AggregateJoinTransposeRule` fails to aggregate over unique column (Zhong Yu)
- \[ [CALCITE-2196](https://issues.apache.org/jira/browse/CALCITE-2196)\]
Tweak janino code generation to allow debugging (jingzhang)
- \[ [CALCITE-2197](https://issues.apache.org/jira/browse/CALCITE-2197)\]
Test failures on Windows
- \[ [CALCITE-2200](https://issues.apache.org/jira/browse/CALCITE-2200)\]
Infinite loop for JoinPushTransitivePredicatesRule
- \[ [CALCITE-2207](https://issues.apache.org/jira/browse/CALCITE-2207)\]
Enforce Java version via maven-enforcer-plugin (Kevin Risden)
- \[ [CALCITE-2213](https://issues.apache.org/jira/browse/CALCITE-2213)\]
Geode integration tests are failing

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-16-0 "Permalink")

- \[ [CALCITE-2024](https://issues.apache.org/jira/browse/CALCITE-2024)\]
Submit a journal paper on Calcite to VLDB Journal or ACM SIGMOD Record (Edmon Begoli)
- \[ [CALCITE-2203](https://issues.apache.org/jira/browse/CALCITE-2203)\]
Calcite site redirect links to Avatica broken with jekyll-redirect-from 0.12+ (Kevin Risden)

## [1.15.0](https://github.com/apache/calcite/releases/tag/calcite-1.15.0) / 2017-12-11 [Permalink](https://calcite.apache.org/docs/history.html\#v1-15-0 "Permalink")

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 7, 8, 9, 10;
Guava versions 14.0 to 23.0;
Druid version 0.10.0;
other software versions as specified in `pom.xml`.

This release comes three months after 1.14.0. It includes than 44 resolved
issues, mostly modest improvements and bug-fixes, but here are some
features of note:

- \[ [CALCITE-707](https://issues.apache.org/jira/browse/CALCITE-707)\]
adds _DDL commands_ to Calcite for the first time, including _CREATE and DROP_
_commands for schemas, tables, foreign tables, views, and materialized views_.
We know that DDL syntax is a matter of taste, so we added the extensions to a
_new “server” module_, leaving the “core” parser unchanged;
- \[ [CALCITE-2061](https://issues.apache.org/jira/browse/CALCITE-2061)\]
allows _dynamic parameters_ in the `LIMIT` and `OFFSET` and clauses;
- \[ [CALCITE-1913](https://issues.apache.org/jira/browse/CALCITE-1913)\]
refactors the JDBC adapter to make it easier to _plug in a new SQL dialect_;
- \[ [CALCITE-1616](https://issues.apache.org/jira/browse/CALCITE-1616)\]
adds a _data profiler_, an algorithm that efficiently analyzes large data sets
with many columns, estimating the number of distinct values in columns and
groups of columns, and finding functional dependencies. The improved
statistics are used by the algorithm that designs summary tables for a
lattice.

Calcite now supports JDK 10 and Guava 23.0. (It continues to run on
JDK 7, 8 and 9, and on versions of Guava as early as 14.0.1. The default
version of Guava remains 19.0, the latest version compatible with JDK 7
and the Cassandra adapter’s dependencies.)

This is the [last\\
release that will support JDK 1.7](https://issues.apache.org/jira/browse/CALCITE-2027).

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-15-0 "Permalink")

- \[ [CALCITE-1616](https://issues.apache.org/jira/browse/CALCITE-1616)\]
Data profiler
- \[ [CALCITE-2061](https://issues.apache.org/jira/browse/CALCITE-2061)\]
Dynamic parameters in `OFFSET`, `FETCH` and `LIMIT` clauses (Enrico Olivelli)
- \[ [CALCITE-707](https://issues.apache.org/jira/browse/CALCITE-707)\]
Add “server” module, with built-in support for simple DDL statements
- \[ [CALCITE-2041](https://issues.apache.org/jira/browse/CALCITE-2041)\]
When `ReduceExpressionRule` simplifies a nullable expression, allow the result
to change type to `NOT NULL`
- \[ [CALCITE-2058](https://issues.apache.org/jira/browse/CALCITE-2058)\]
Support JDK 10
- \[ [CALCITE-2016](https://issues.apache.org/jira/browse/CALCITE-2016)\]
Make item + dot operators work for array (e.g. `SELECT orders[5].color FROM t`
(Shuyi Chen)
- \[ [CALCITE-2035](https://issues.apache.org/jira/browse/CALCITE-2035)\]
Allow approximate aggregate functions, and add `APPROX_COUNT_DISTINCT`
- \[ [CALCITE-1990](https://issues.apache.org/jira/browse/CALCITE-1990)\]
Make `RelDistribution` extend `RelMultipleTrait` (LeoWangLZ)
- \[ [CALCITE-1867](https://issues.apache.org/jira/browse/CALCITE-1867)\]
Allow user-defined grouped window functions (Timo Walther)
- \[ [CALCITE-2031](https://issues.apache.org/jira/browse/CALCITE-2031)\]
`ST_X` and `ST_Y` GIS functions
- \[ [CALCITE-1913](https://issues.apache.org/jira/browse/CALCITE-1913)\]
Pluggable SQL dialects for JDBC adapter: Replace usages of `DatabaseProduct`
with dialect methods, and introduce a configurable `SqlDialectFactory`
(Christian Beikov)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-15-0 "Permalink")

- \[ [CALCITE-2078](https://issues.apache.org/jira/browse/CALCITE-2078)\]
Aggregate functions in `OVER` clause (Liao Xintao)
- \[ [CALCITE-2070](https://issues.apache.org/jira/browse/CALCITE-2070)\]
Git test fails when run from source distro
- \[ [CALCITE-1808](https://issues.apache.org/jira/browse/CALCITE-1808)\]
`JaninoRelMetadataProvider` loading cache might cause `OutOfMemoryError`
- \[ [CALCITE-2069](https://issues.apache.org/jira/browse/CALCITE-2069)\]
`RexSimplify.removeNullabilityCast()` always removes cast for operand with
`ANY` type (Volodymyr Vysotskyi)
- \[ [CALCITE-2074](https://issues.apache.org/jira/browse/CALCITE-2074)\]
Simplification of point ranges that are open above or below yields wrong
results
- \[ [CALCITE-2005](https://issues.apache.org/jira/browse/CALCITE-2005)\]
Test failures on Windows
- Add `ImmutableBitSet.set(int, boolean)`
- \[ [CALCITE-2054](https://issues.apache.org/jira/browse/CALCITE-2054)\]
Error while validating `UPDATE` with dynamic parameter in `SET` clause (Enrico
Olivelli)
- \[ [CALCITE-2055](https://issues.apache.org/jira/browse/CALCITE-2055)\]
Check year, month, day, hour, minute and second ranges for date and time
literals (Volodymyr Vysotskyi)
- \[ [CALCITE-2051](https://issues.apache.org/jira/browse/CALCITE-2051)\]
Rules using `Aggregate` might check for simple grouping sets incorrectly
- Add parameter to `SqlCallBinding.getOperandLiteralValue(int)` to specify
desired value type
- \[ [CALCITE-2039](https://issues.apache.org/jira/browse/CALCITE-2039)\]
`AssertionError` when pushing project to `ProjectableFilterableTable`
- \[ [CALCITE-2050](https://issues.apache.org/jira/browse/CALCITE-2050)\]
Exception when pushing post-aggregates into Druid
- \[ [CALCITE-2043](https://issues.apache.org/jira/browse/CALCITE-2043)\]
Use custom `RelBuilder` implementation in some rules (Volodymyr Vysotskyi)
- \[ [CALCITE-2044](https://issues.apache.org/jira/browse/CALCITE-2044)\]
Tweak cost of `BindableTableScan` to make sure `Project` is pushed through
`Aggregate` (Luis Fernando Kauer)
- \[ [CALCITE-2012](https://issues.apache.org/jira/browse/CALCITE-2012)\]
Replace `LocalInterval` by `Interval` in Druid adapter
- \[ [CALCITE-1984](https://issues.apache.org/jira/browse/CALCITE-1984)\]
Incorrect rewriting with materialized views using `DISTINCT` in aggregate
functions
- \[ [CALCITE-1876](https://issues.apache.org/jira/browse/CALCITE-1876)\]
In CSV example, tweak cost to ensure that `Project` is pushed through
`Aggregate` (Luis Fernando Kauer)
- \[ [CALCITE-2037](https://issues.apache.org/jira/browse/CALCITE-2037)\]
Modify parser template to allow sub-projects to override `SqlStmt` syntax
(Roman Kulyk)
- \[ [CALCITE-2019](https://issues.apache.org/jira/browse/CALCITE-2019)\]
Druid’s time column is NOT NULL, so push `COUNT(druid_time_column)` as if it
were `COUNT(*)`
- \[ [CALCITE-2034](https://issues.apache.org/jira/browse/CALCITE-2034)\]
`FileReaderTest` fails with path containing spaces (Marc Prud’hommeaux)
- \[ [CALCITE-2028](https://issues.apache.org/jira/browse/CALCITE-2028)\]
`SubQueryRemoveRule` should create `Join`, not `Correlate`, for un-correlated
sub-queries (Liao Xintao)
- \[ [CALCITE-2029](https://issues.apache.org/jira/browse/CALCITE-2029)\]
Query with `IS DISTINCT FROM` condition in `WHERE` or `JOIN` clause fails with
`AssertionError`, “Cast for just nullability not allowed” (Volodymyr Vysotskyi)
- \[ [CALCITE-1998](https://issues.apache.org/jira/browse/CALCITE-1998)\]
Hive `ORDER BY` null values (Abbas Gadhia)
- \[ [CALCITE-2014](https://issues.apache.org/jira/browse/CALCITE-2014)\]
Look for `saffron.properties` file in classpath rather than in working
directory (Arina Ielchiieva)
- \[ [CALCITE-1910](https://issues.apache.org/jira/browse/CALCITE-1910)\]
`NullPointerException` on filtered aggregators using `IN`
- \[ [CALCITE-1762](https://issues.apache.org/jira/browse/CALCITE-1762)\]
Upgrade to Spark 2.X
- \[ [CALCITE-2008](https://issues.apache.org/jira/browse/CALCITE-2008)\]
Fix braces in `TRIM` signature
- \[ [CALCITE-2007](https://issues.apache.org/jira/browse/CALCITE-2007)\]
Fix `RexSimplify` behavior when literals come first
- \[ [CALCITE-2006](https://issues.apache.org/jira/browse/CALCITE-2006)\]
Push `IS NULL` and `IS NOT NULL` predicates to Druid
- \[ [CALCITE-1996](https://issues.apache.org/jira/browse/CALCITE-1996)\]
In JDBC adapter, generate correct `VALUES` syntax
- \[ [CALCITE-2001](https://issues.apache.org/jira/browse/CALCITE-2001)\]
JDBC driver should return “SYSTEM TABLE” rather than “SYSTEM\_TABLE”
- \[ [CALCITE-1995](https://issues.apache.org/jira/browse/CALCITE-1995)\]
Remove terms from `Filter` if predicates indicate they are always true or
false
- \[ [CALCITE-1983](https://issues.apache.org/jira/browse/CALCITE-1983)\]
Push `=`and `<>` operations with numeric cast on dimensions to Druid
- \[ [CALCITE-1960](https://issues.apache.org/jira/browse/CALCITE-1960)\]
`RelMdPredicates.getPredicates` is slow if there are many equivalent columns
(Rheet Wong)
- Make Travis CI builds work (Christian Beikov)
- \[ [CALCITE-1987](https://issues.apache.org/jira/browse/CALCITE-1987)\]
Implement `EXTRACT` for JDBC (Pavel Gubin)
- \[ [CALCITE-1988](https://issues.apache.org/jira/browse/CALCITE-1988)\]
Various code quality issues
- \[ [CALCITE-1986](https://issues.apache.org/jira/browse/CALCITE-1986)\]
Add `RelBuilder.match` and methods for building patterns (Dian Fu)
- \[ [CALCITE-1980](https://issues.apache.org/jira/browse/CALCITE-1980)\]
`RelBuilder.aggregate` should rename underlying fields if `groupKey` contains
an alias
- \[ [CALCITE-1946](https://issues.apache.org/jira/browse/CALCITE-1946)\]
JDBC adapter should generate sub-`SELECT` if dialect does not support nested
aggregate functions (Pawel Ruchaj)
- \[ [CALCITE-1976](https://issues.apache.org/jira/browse/CALCITE-1976)\]
linq4j: support List and Map literals

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-15-0 "Permalink")

- Update PMC Chair
- \[ [CALCITE-2052](https://issues.apache.org/jira/browse/CALCITE-2052)\]
Remove SQL code style from materialized views documentation
- \[ [CALCITE-2036](https://issues.apache.org/jira/browse/CALCITE-2036)\]
Fix “next” link in [powered\_by.html](https://calcite.apache.org/docs/powered_by.html)
- \[ [CALCITE-2038](https://issues.apache.org/jira/browse/CALCITE-2038)\]
Fix incomplete sentence in tutorial
- \[ [CALCITE-2021](https://issues.apache.org/jira/browse/CALCITE-2021)\]
Document the interfaces that you can use to extend Calcite
- Javadoc fixes (Alexey Roytman)
- Add two talks, and committer Christian Beikov
- Fix URL in `FileSchemaFactory` javadoc (Marc Prud’hommeaux)
- \[ [CALCITE-1989](https://issues.apache.org/jira/browse/CALCITE-1989)\]
Check dependencies for vulnerabilities each release

## [1.14.0](https://github.com/apache/calcite/releases/tag/calcite-1.14.0) / 2017-09-06 [Permalink](https://calcite.apache.org/docs/history.html\#v1-14-0 "Permalink")

This release brings some big new features.
The `GEOMETRY` data type was added along with 35 associated functions as the start of support for Simple Feature Access.
There are also two new adapters.
Firstly, the Elasticsearch 5 adapter which now exists in parallel with the previous Elasticsearch 2 adapter.
Additionally there is now an [OS adapter](https://calcite.apache.org/docs/os_adapter.html) which exposes operating system metrics as relational tables.
`ThetaSketch` and `HyperUnique` support has also been added to the Druid adapter.

Several minor improvements are added as well including improved `MATCH_RECOGNIZE` support, quantified comparison predicates, and `ARRAY` and `MULTISET` support for UDFs.
A full list of new features is given below.

There are also a few breaking changes.
The return type of `RANK` and other aggregate functions has been changed.
There also changes to `Aggregate` in order to improve compatibility with Apache Hive.
Finally, the `Schema#snapshot()` interface has been upgraded to allow for more flexible versioning.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 1.7, 1.8, 9;
Guava versions 14.0 to 21.0;
Druid version 0.11.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-14-0 "Permalink")

- \[ [CALCITE-1968](https://issues.apache.org/jira/browse/CALCITE-1968)\] OpenGIS Simple Feature Access SQL 1.2.1: add `GEOMETRY` data type and first 35 functions
Add Spatial page, document GIS functions in SQL reference (indicating
which ones are implemented), and add “countries” data set for testing.
- \[ [CALCITE-1967](https://issues.apache.org/jira/browse/CALCITE-1967)\] Elasticsearch 5 adapter (Christian Beikov)
- \[ [CALCITE-1911](https://issues.apache.org/jira/browse/CALCITE-1911)\] In `MATCH_RECOGNIZE`, support `WITHIN` sub-clause (Dian Fu)
- \[ [CALCITE-1897](https://issues.apache.org/jira/browse/CALCITE-1897)\] Add ‘%’ operator as an alternative to ‘MOD’ (sunjincheng)
- \[ [CALCITE-1787](https://issues.apache.org/jira/browse/CALCITE-1787)\] Add `ThetaSketch` and `HyperUnique` support to Calcite via rolled up columns (Zain Humayun)
- \[ [CALCITE-1896](https://issues.apache.org/jira/browse/CALCITE-1896)\] OS adapter and `sqlsh`
  - Vmstat table function for sqlsh
- \[ [CALCITE-1864](https://issues.apache.org/jira/browse/CALCITE-1864)\] Allow `NULL` literal as argument
- \[ [CALCITE-1834](https://issues.apache.org/jira/browse/CALCITE-1834)\] Allow user-defined functions to have arguments that are `ARRAY` or `MULTISET` (Ankit Singhal)
- \[ [CALCITE-1886](https://issues.apache.org/jira/browse/CALCITE-1886)\] Support `"LIMIT [offset,] row_count"`, per MySQL (Kaiwang Chen)
- \[ [CALCITE-1845](https://issues.apache.org/jira/browse/CALCITE-1845)\] Quantified comparison predicates (SOME, ANY, ALL)
- \[ [CALCITE-1709](https://issues.apache.org/jira/browse/CALCITE-1709)\] Support mixing table columns with extended columns in DML (Rajeshbabu Chintaguntla)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-14-0 "Permalink")

- \[ [CALCITE-1931](https://issues.apache.org/jira/browse/CALCITE-1931)\]
Change the return type of `RANK` and other aggregate functions.
Various aggregate functions that used to return `INTEGER` now return other
types: `RANK`, `DENSE_RANK`, and `NTILE` now return `BIGINT`;
`CUME_DIST` and `PERCENT_RANK` now return `DOUBLE`.
( **This is a breaking change**.)
- \[ [CALCITE-1947](https://issues.apache.org/jira/browse/CALCITE-1947)\] Add `TIME`/`TIMESTAMP` with local time zone types to optimizer
- \[ [CALCITE-1972](https://issues.apache.org/jira/browse/CALCITE-1972)\] Create `.sha512` and `.md5` digests for release artifacts
- \[ [CALCITE-1941](https://issues.apache.org/jira/browse/CALCITE-1941)\] Refine interface `Schema#snapshot()`
( **This is a breaking change**.)
- \[ [CALCITE-1069](https://issues.apache.org/jira/browse/CALCITE-1069)\] In `Aggregate`, deprecate indicators, and allow `GROUPING` to be used as an aggregate function
( **This is a breaking change**.)
- \[ [CALCITE-1969](https://issues.apache.org/jira/browse/CALCITE-1969)\] Annotate user-defined functions as strict and semi-strict
- \[ [CALCITE-1945](https://issues.apache.org/jira/browse/CALCITE-1945)\] Make return types of `AVG`, `VARIANCE`, `STDDEV` and `COVAR` customizable via RelDataTypeSystem
- \[ [CALCITE-1966](https://issues.apache.org/jira/browse/CALCITE-1966)\] Allow normal views to act as materialization table (Christian Beikov)
- \[ [CALCITE-1953](https://issues.apache.org/jira/browse/CALCITE-1953)\] Rewrite `"NOT (x IS FALSE)" to "x IS NOT FALSE"; "x IS TRUE"` would be wrong
- \[ [CALCITE-1943](https://issues.apache.org/jira/browse/CALCITE-1943)\] Add back `NavigationExpander` and `NavigationReplacer` in `SqlValidatorImpl` (Dian Fu)
- \[ [CALCITE-1963](https://issues.apache.org/jira/browse/CALCITE-1963)\] Upgrade checkstyle, and fix code to comply
- \[ [CALCITE-1944](https://issues.apache.org/jira/browse/CALCITE-1944)\] Window function applied to sub-query that returns dynamic star gets wrong plan (Volodymyr Vysotskyi)
- \[ [CALCITE-1954](https://issues.apache.org/jira/browse/CALCITE-1954)\] Column from outer join should be null, whether or not it is aliased
- \[ [CALCITE-1959](https://issues.apache.org/jira/browse/CALCITE-1959)\] Reduce the amount of metadata and `tableName` calls in Druid (Zain Humayun)
- \[ [CALCITE-1930](https://issues.apache.org/jira/browse/CALCITE-1930)\] Fix `AggregateExpandDistinctAggregatesRule` when there are multiple `AggregateCalls` referring to the same input
- \[ [CALCITE-1936](https://issues.apache.org/jira/browse/CALCITE-1936)\] Allow `ROUND()` and `TRUNCATE()` to take one operand, defaulting scale to 0
- \[ [CALCITE-1931](https://issues.apache.org/jira/browse/CALCITE-1931)\] Change the return type of RANK and other aggregate functions
- \[ [CALCITE-1932](https://issues.apache.org/jira/browse/CALCITE-1932)\] `Project.getPermutation()` should return null if not a permutation (e.g. repeated `InputRef`)
- \[ [CALCITE-1925](https://issues.apache.org/jira/browse/CALCITE-1925)\] In `JaninoRelMetadataProvider`, cache null values (Ted Xu)
- \[ [CALCITE-1849](https://issues.apache.org/jira/browse/CALCITE-1849)\] Support `RexSubQuery` in `RelToSqlConverter`
- \[ [CALCITE-1909](https://issues.apache.org/jira/browse/CALCITE-1909)\] Output `rowType` of Match should include `PARTITION BY` and `ORDER BY` columns
- \[ [CALCITE-1929](https://issues.apache.org/jira/browse/CALCITE-1929)\] Deprecate class `RelDataTypeFactory.FieldInfoBuilder`
- \[ [CALCITE-1895](https://issues.apache.org/jira/browse/CALCITE-1895)\] MSSQL’s SUBSTRING operator has different syntax (Chris Baynes)
- \[ [CALCITE-1919](https://issues.apache.org/jira/browse/CALCITE-1919)\] `NullPointerException` when target in `ReflectiveSchema` belongs to root package (Lim Chee Hau)
- \[ [CALCITE-1907](https://issues.apache.org/jira/browse/CALCITE-1907)\] Table function with 1 column gives `ClassCastException`
- \[ [CALCITE-1841](https://issues.apache.org/jira/browse/CALCITE-1841)\] Create handlers for JDBC dialect-specific generated SQL (Chris Baynes)
- \[ [CALCITE-1898](https://issues.apache.org/jira/browse/CALCITE-1898)\] `LIKE` must match ‘.’ (period) literally
- \[ [CALCITE-1900](https://issues.apache.org/jira/browse/CALCITE-1900)\] Detect cyclic views and give useful error message
- \[ [CALCITE-1893](https://issues.apache.org/jira/browse/CALCITE-1893)\] Add MYSQL\_5 conformance
- \[ [CALCITE-1883](https://issues.apache.org/jira/browse/CALCITE-1883)\] `HepPlanner` should force garbage collect whenever a root registered (Ted Xu)
- \[ [CALCITE-1889](https://issues.apache.org/jira/browse/CALCITE-1889)\] Accept compound identifiers in `SqlValidatorUtil.checkIdentifierListForDuplicates()` (Rajeshbabu Chintaguntla)
- \[ [CALCITE-1881](https://issues.apache.org/jira/browse/CALCITE-1881)\] Can’t distinguish overloaded user-defined functions that have DATE and TIMESTAMP arguments (余启)
- \[ [CALCITE-1803](https://issues.apache.org/jira/browse/CALCITE-1803)\] Push Project that follows Aggregate down to Druid (Junxian Wu)
- \[ [CALCITE-1828](https://issues.apache.org/jira/browse/CALCITE-1828)\] Push the FILTER clause into Druid as a Filtered Aggregator (Zain Humayun)
- \[ [CALCITE-1871](https://issues.apache.org/jira/browse/CALCITE-1871)\] Nesting `LAST` within `PREV` is not parsed correctly for `MATCH_RECOGNIZE`
- \[ [CALCITE-1877](https://issues.apache.org/jira/browse/CALCITE-1877)\] Move the Pig test data files into target for the test runtime
- \[ [CALCITE-1815](https://issues.apache.org/jira/browse/CALCITE-1815)\] Switch Pig adapter to depend on avatica-core instead of full avatica
- \[ [CALCITE-1826](https://issues.apache.org/jira/browse/CALCITE-1826)\] Generate dialect-specific SQL for `FLOOR` operator when in a `GROUP BY` (Chris Baynes)
- \[ [CALCITE-1842](https://issues.apache.org/jira/browse/CALCITE-1842)\] `Sort.computeSelfCost()`` calls`makeCost()\`\` with arguments in wrong order (Junxian Wu)
- \[ [CALCITE-1874](https://issues.apache.org/jira/browse/CALCITE-1874)\] In Frameworks, make `SqlToRelConverter` configurable
- \[ [CALCITE-1873](https://issues.apache.org/jira/browse/CALCITE-1873)\] In a “GROUP BY ordinal” query, validator gives invalid “Expression is not being grouped” error if column has alias
- \[ [CALCITE-1833](https://issues.apache.org/jira/browse/CALCITE-1833)\] User-defined aggregate functions with more than one parameter (hzyuemeng1)
- \[ [CALCITE-1860](https://issues.apache.org/jira/browse/CALCITE-1860)\] Duplicate null predicates cause `NullPointerException` in `RexUtil` (Ruidong Li)
- \[ [CALCITE-1859](https://issues.apache.org/jira/browse/CALCITE-1859)\] NPE in validate method of `VolcanoPlanner`
- \[ [CALCITE-1818](https://issues.apache.org/jira/browse/CALCITE-1818)\] Handle `SqlKind.DYNAMIC` (parameters) in `SqlImplementor` (Dylan Adams)
- \[ [CALCITE-1856](https://issues.apache.org/jira/browse/CALCITE-1856)\] Add option `StructKind.PEEK_FIELDS_NO_EXPAND`, similar to `PEEK_FIELDS` but is not expanded in `"SELECT *"` (Shuyi Chen)

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-14-0 "Permalink")

- Add committer Chris Baynes
- Add DataEngConf talk
- \[ [CALCITE-1901](https://issues.apache.org/jira/browse/CALCITE-1901)\] SQL reference should say that “ONLY” is required after “FETCH … ROWS”

## [1.13.0](https://github.com/apache/calcite/releases/tag/calcite-1.13.0) / 2017-06-20 [Permalink](https://calcite.apache.org/docs/history.html\#v1-13-0 "Permalink")

This release comes three months after 1.12.0. It includes more than 75 resolved issues, comprising
a large number of new features as well as general improvements and bug-fixes.

First, Calcite has been upgraded to use
[Avatica 1.10.0](https://issues.apache.org/jira/browse/CALCITE-1807),
which was recently released.

Moreover, Calcite core includes improvements which aim at making it more powerful, stable and robust.
In addition to numerous bux-fixes, we have implemented a
[new materialized view rewriting algorithm](https://issues.apache.org/jira/browse/CALCITE-1731)
and [new metadata providers](https://issues.apache.org/jira/browse/CALCITE-1682) which
should prove useful for data processing systems relying on Calcite.

In this release, we have also completed the work to
[support the `MATCH_RECOGNIZE` clause](https://issues.apache.org/jira/browse/CALCITE-1570)
used in complex-event processing (CEP).

In addition, more progress has been made for the different adapters.
For instance, the Druid adapter now relies on
[Druid 0.10.0](https://issues.apache.org/jira/browse/CALCITE-1771) and
it can generate more efficient plans where most of the computation can be pushed to Druid,
e.g., [using extraction functions](https://issues.apache.org/jira/browse/CALCITE-1707).

There is one minor but potentially breaking API change in
\[ [CALCITE-1788](https://issues.apache.org/jira/browse/CALCITE-1788)\]
(Simplify handling of position in the parser), requiring changes in the parameter
lists of parser extension methods.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 1.7, 1.8, 9;
Guava versions 14.0 to 21.0;
Druid version 0.10.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-13-0 "Permalink")

- \[ [CALCITE-1570](https://issues.apache.org/jira/browse/CALCITE-1570)\]
Add `MATCH_RECOGNIZE` operator, for event pattern-matching

  - \[ [CALCITE-1647](https://issues.apache.org/jira/browse/CALCITE-1647)\]
    Classifier and `match_number` syntax support for `MATCH_RECOGNIZE`
  - \[ [CALCITE-1646](https://issues.apache.org/jira/browse/CALCITE-1646)\]
    Partition by and order by syntax support for `MATCH_RECOGNIZE` (Zhiqiang-He)
  - \[ [CALCITE-1645](https://issues.apache.org/jira/browse/CALCITE-1645)\]
    Row per match syntax support for `MATCH_RECOGNIZE` (Zhiqiang-He)
  - \[ [CALCITE-1644](https://issues.apache.org/jira/browse/CALCITE-1644)\]
    Subset clause syntax support for `MATCH_RECOGNIZE` (Zhiqiang-He)
  - \[ [CALCITE-1643](https://issues.apache.org/jira/browse/CALCITE-1643)\]
    `AFTER MATCH` sub-clause of `MATCH_RECOGNIZE` clause (Zhiqiang-He)
  - \[ [CALCITE-1642](https://issues.apache.org/jira/browse/CALCITE-1642)\]
    Support `MEASURES` clause in `MATCH_RECOGNIZE` (Zhiqiang-He)
- \[ [CALCITE-1853](https://issues.apache.org/jira/browse/CALCITE-1853)\]
Push Count distinct into Druid when approximate results are acceptable (Zain Humayun)
- \[ [CALCITE-1829](https://issues.apache.org/jira/browse/CALCITE-1829)\]
Add `TIME`/`TIMESTAMP`/`DATE` datatype handling to `RexImplicationChecker`
- \[ [CALCITE-1613](https://issues.apache.org/jira/browse/CALCITE-1613)\]
Implement `EXTRACT` for time unit `DOW`, `DOY`; and fix `CENTURY`
- \[ [CALCITE-1807](https://issues.apache.org/jira/browse/CALCITE-1807)\]
Upgrade to Avatica 1.10
- \[ [CALCITE-1802](https://issues.apache.org/jira/browse/CALCITE-1802)\]
Add post-aggregation step for Union in materialized view rewriting
- \[ [CALCITE-1795](https://issues.apache.org/jira/browse/CALCITE-1795)\]
Extend materialized view rewriting to produce rewritings using `Union` operators
- \[ [CALCITE-1797](https://issues.apache.org/jira/browse/CALCITE-1797)\]
Support view partial rewriting in aggregate materialized view rewriting
- \[ [CALCITE-1791](https://issues.apache.org/jira/browse/CALCITE-1791)\]
Support view partial rewriting in join materialized view rewriting
- \[ [CALCITE-1731](https://issues.apache.org/jira/browse/CALCITE-1731)\]
Rewriting of queries using materialized views with joins and aggregates
- \[ [CALCITE-1780](https://issues.apache.org/jira/browse/CALCITE-1780)\]
Add `required Order` and `requiresOver` parameters to the constructor of `SqlUserDefinedAggregate Function` (SunJincheng)
- \[ [CALCITE-1306](https://issues.apache.org/jira/browse/CALCITE-1306)\]
Allow `GROUP BY` and `HAVING` to reference `SELECT` expressions by ordinal and alias (Rajeshbabu Chintaguntla)
- \[ [CALCITE-1781](https://issues.apache.org/jira/browse/CALCITE-1781)\]
Allow expression in `CUBE` and `ROLLUP`
- \[ [CALCITE-1771](https://issues.apache.org/jira/browse/CALCITE-1771)\]
Upgrade to Druid 0.10.0 (Nishant Bangarwa)
- \[ [CALCITE-1772](https://issues.apache.org/jira/browse/CALCITE-1772)\]
Add a hook to allow `RelNode` expressions to be executed by JDBC driver
- \[ [CALCITE-1766](https://issues.apache.org/jira/browse/CALCITE-1766)\]
Support system functions having no args with parenthesis too (Ankit Singhal)
- \[ [CALCITE-1760](https://issues.apache.org/jira/browse/CALCITE-1760)\]
Implement utility method to identify lossless casts
- \[ [CALCITE-1682](https://issues.apache.org/jira/browse/CALCITE-1682)\]
New metadata providers for expression column origin and all predicates in plan
- \[ [CALCITE-1753](https://issues.apache.org/jira/browse/CALCITE-1753)\]
Push expressions into null-generating side of a join if they are “strong” (null-preserving)
- \[ [CALCITE-1759](https://issues.apache.org/jira/browse/CALCITE-1759)\]
Add SQL:2014 reserved words to parser
- \[ [CALCITE-476](https://issues.apache.org/jira/browse/CALCITE-476)\]
Support distinct aggregates in window functions
- \[ [CALCITE-1738](https://issues.apache.org/jira/browse/CALCITE-1738)\]
Support `CAST` of literal values in filters pushed to Druid (Remus Rusanu)
- \[ [CALCITE-1758](https://issues.apache.org/jira/browse/CALCITE-1758)\]
Push to Druid `OrderBy`/`Limit` operation over time dimension and additional columns (Slim Bouguerra)
- \[ [CALCITE-1707](https://issues.apache.org/jira/browse/CALCITE-1707)\]
Push `Extraction` filter on `Year`/`Month`/`Day` to druid (Slim Bouguerra)
- \[ [CALCITE-1725](https://issues.apache.org/jira/browse/CALCITE-1725)\]
Push project aggregate of time extract to druid (Slim Bouguerra)
- \[ [CALCITE-1747](https://issues.apache.org/jira/browse/CALCITE-1747)\]
`RelMdColumnUniqueness` for `HepRelVertex`
- \[ [CALCITE-1749](https://issues.apache.org/jira/browse/CALCITE-1749)\]
Push filter conditions partially into Druid
- \[ [CALCITE-1730](https://issues.apache.org/jira/browse/CALCITE-1730)\]
Upgrade Druid to 0.9.2 (Nishant Bangarwa)
- \[ [CALCITE-1702](https://issues.apache.org/jira/browse/CALCITE-1702)\]
Support extended columns in DML (Kevin Liew)

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-13-0 "Permalink")

- \[ [CALCITE-1855](https://issues.apache.org/jira/browse/CALCITE-1855)\]
Fix float values in Cassandra adapter
- \[ [CALCITE-1848](https://issues.apache.org/jira/browse/CALCITE-1848)\]
Rename MySource to FileSource (Darion Yaphet)
- \[ [CALCITE-1852](https://issues.apache.org/jira/browse/CALCITE-1852)\]
Fix for `UnionMergeRule` to deal correctly with `EXCEPT`
- \[ [CALCITE-1850](https://issues.apache.org/jira/browse/CALCITE-1850)\]
Extend `UnionMergeRule` to deal with more than 2 branches (Pengcheng Xiong)
- \[ [CALCITE-1805](https://issues.apache.org/jira/browse/CALCITE-1805)\]
Druid adapter incorrectly pushes down `COUNT(c)`; Druid only supports `COUNT(*)`
- \[ [CALCITE-1846](https://issues.apache.org/jira/browse/CALCITE-1846)\]
Metadata pulled up predicates should skip non-deterministic calls (Ted Xu)
- \[ [CALCITE-1819](https://issues.apache.org/jira/browse/CALCITE-1819)\]
Druid Adapter does not push the boolean operator `<>` as a filter correctly (Zain Humayun)
- \[ [CALCITE-1798](https://issues.apache.org/jira/browse/CALCITE-1798)\]
In JDBC adapter, generate dialect-specific SQL for `FLOOR` operator (Chris Baynes)
- \[ [CALCITE-1812](https://issues.apache.org/jira/browse/CALCITE-1812)\]
Provide `RelMetadataQuery` from planner to rules and invalidate in `transformTo` (Remus Rusanu)
- \[ [CALCITE-1804](https://issues.apache.org/jira/browse/CALCITE-1804)\]
Cannot assign `NOT NULL` array to `NULLABLE` array (Ankit Singhal)
- \[ [CALCITE-1810](https://issues.apache.org/jira/browse/CALCITE-1810)\]
Allow `NULL` for `ARRAY` constructor (Ankit Singhal)
- \[ [CALCITE-1830](https://issues.apache.org/jira/browse/CALCITE-1830)\]
`ProcessBuilder` is security sensitive; move it to test suite to prevent accidents
- \[ [CALCITE-1816](https://issues.apache.org/jira/browse/CALCITE-1816)\]
`JaninoRelMetadataProvider` generated classes leak ACTIVE nodes on exception (Remus Rusanu)
- \[ [CALCITE-1690](https://issues.apache.org/jira/browse/CALCITE-1690)\]
Calcite timestamp literals cannot express precision above millisecond, `TIMESTAMP(3)`
- \[ [CALCITE-1664](https://issues.apache.org/jira/browse/CALCITE-1664)\]
`CAST(<string> as TIMESTAMP)` adds part of sub-second fraction to the value
- \[ [CALCITE-1742](https://issues.apache.org/jira/browse/CALCITE-1742)\]
Create a read-consistent view of CalciteSchema for each statement compilation
- \[ [CALCITE-1800](https://issues.apache.org/jira/browse/CALCITE-1800)\]
JDBC adapter fails on query with `UNION` in `FROM` clause (Viktor Batytskyi, Minji Kim)
- \[ [CALCITE-1788](https://issues.apache.org/jira/browse/CALCITE-1788)\]
Simplify handling of position in the parser
- \[ [CALCITE-1782](https://issues.apache.org/jira/browse/CALCITE-1782)\]
`AggregateExpandDistinctAggregatesRule` should work on `Aggregate` instead of `LogicalAggregate` (Haohui Mai)
- \[ [CALCITE-1293](https://issues.apache.org/jira/browse/CALCITE-1293)\]
Bad code generated when argument to `COUNT(DISTINCT)` is a `GROUP BY` column
- \[ [CALCITE-1770](https://issues.apache.org/jira/browse/CALCITE-1770)\]
`CAST(NULL AS ...)` gives NPE (Slim Bouguerra)
- \[ [CALCITE-1777](https://issues.apache.org/jira/browse/CALCITE-1777)\]
`WHERE FALSE` causes `AssertionError` (Slim Bouguerra)
- \[ [CALCITE-1778](https://issues.apache.org/jira/browse/CALCITE-1778)\]
Query with `WHERE CASE` throws `AssertionError` “Cast for just nullability not allowed”
- \[ [CALCITE-1773](https://issues.apache.org/jira/browse/CALCITE-1773)\]
Add Test sql validator test for Pattern skip syntax in `MATCH_RECOGNIZE` (Zhiqiang-He)
- \[ [CALCITE-1761](https://issues.apache.org/jira/browse/CALCITE-1761)\]
`TUMBLE`/`HOP`/`SESSION_START`/`END` do not resolve time field correctly
- \[ [CALCITE-1765](https://issues.apache.org/jira/browse/CALCITE-1765)\]
Druid adapter fail when the extract granularity is not supported (Slim Bouguerra)
- \[ [CALCITE-1767](https://issues.apache.org/jira/browse/CALCITE-1767)\]
Fix join/aggregate rewriting rule when same table is referenced more than once
- \[ [CALCITE-1764](https://issues.apache.org/jira/browse/CALCITE-1764)\]
Adding sort ordering type for druid sort json field (Slim Bouguerra)
- \[ [CALCITE-715](https://issues.apache.org/jira/browse/CALCITE-715)\]
Add `PERIOD` type constructor and period operators (`CONTAINS`, `PRECEDES`, etc.)
- \[ [CALCITE-1456](https://issues.apache.org/jira/browse/CALCITE-1456)\]
Change `SubstitutionVisitor` to use generic `RelBuilder` instead of Logical instances of the operators when possible
- \[ [CALCITE-1763](https://issues.apache.org/jira/browse/CALCITE-1763)\]
Recognize lossless casts in join/aggregate materialized view rewriting rule
- \[ [CALCITE-1639](https://issues.apache.org/jira/browse/CALCITE-1639)\]
`TIMESTAMPADD(MONTH, ...)` should return last day of month if the day overflows
- \[ [CALCITE-1754](https://issues.apache.org/jira/browse/CALCITE-1754)\]
In Csv adapter, convert `DATE` and `TIME` values to `int`, and `TIMESTAMP` values to `long` (Hongbin Ma)
- \[ [CALCITE-1751](https://issues.apache.org/jira/browse/CALCITE-1751)\]
`PigRelBuilderStyleTest` test cases are flapping
- \[ [CALCITE-1750](https://issues.apache.org/jira/browse/CALCITE-1750)\]
Fix unit test failures when the path to the repository contains spaces
- \[ [CALCITE-1724](https://issues.apache.org/jira/browse/CALCITE-1724)\]
Wrong comparison for floats/double type in Druid (Slim Bouguerra)
- \[ [CALCITE-1734](https://issues.apache.org/jira/browse/CALCITE-1734)\]
Select query result not parsed correctly with druid 0.9.2 (Nishant Bangarwa)
- \[ [CALCITE-1732](https://issues.apache.org/jira/browse/CALCITE-1732)\]
`IndexOutOfBoundsException` when using `LATERAL TABLE` with more than one field (Godfrey He)
- \[ [CALCITE-1722](https://issues.apache.org/jira/browse/CALCITE-1722)\]
Druid adapter uses un-scaled value of `DECIMAL` literals (Slim Bouguerra)
- \[ [CALCITE-1723](https://issues.apache.org/jira/browse/CALCITE-1723)\]
Match `DruidProjectFilterTransposeRule` against `DruidQuery` (Nishant Bangarwa)
- \[ [CALCITE-1714](https://issues.apache.org/jira/browse/CALCITE-1714)\]
Do not push group by on druid metrics fields (Slim Bouguerra)

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-13-0 "Permalink")

- Michael Mior joins PMC
- Add 3 new committers (Zhiqiang-He, Kevin Liew, Slim Bouguerra)
- \[ [CALCITE-1854](https://issues.apache.org/jira/browse/CALCITE-1854)\]
Fix value range of TINYINT in documentation (James Xu)
- \[ [CALCITE-1827](https://issues.apache.org/jira/browse/CALCITE-1827)\]
Document `TIMESTAMPADD`, `TIMESTAMPDIFF` functions (SunJincheng)
- \[ [CALCITE-1796](https://issues.apache.org/jira/browse/CALCITE-1796)\]
Update materialized views documentation
- \[ [CALCITE-1566](https://issues.apache.org/jira/browse/CALCITE-1566)\]
Better documentation on the use of materialized views

## [1.12.0](https://github.com/apache/calcite/releases/tag/calcite-1.12.0) / 2017-03-24 [Permalink](https://calcite.apache.org/docs/history.html\#v1-12-0 "Permalink")

[Features of note](https://calcite.apache.org/news/2017/03/24/release-1.12.0) this release are
JDK 9 support,
the new file/web and Apache Pig adapters,
general improvements to the Druid adapter,
more helpful error messages if you get a table or column name wrong,
improved the plans for correlated sub-queries,
support for `TUMBLE`, `HOP` and `SESSION` window functions in streaming and regular queries,
experimental support for `MATCH_RECOGNIZE` clause for complex-event processing (CEP),
several new built-in functions to comply with the ODBC/JDBC standard.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 1.7, 1.8, 9;
Guava versions 14.0 to 21.0;
Druid version 0.9.1.1;
other software versions as specified in `pom.xml`.

### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-12-0 "Permalink")

- \[ [CALCITE-1666](https://issues.apache.org/jira/browse/CALCITE-1666)\]
Support for modifiable views with extended columns (Kevin Liew)
- \[ [CALCITE-1655](https://issues.apache.org/jira/browse/CALCITE-1655)\]
Druid adapter: add `IN` filter (Slim Bouguerra)
- \[ [CALCITE-1641](https://issues.apache.org/jira/browse/CALCITE-1641)\]
Add parser and validator support for `MATCH_RECOGNIZE`, a new clause for
complex-event processing (CEP) (Zhiqiang-He)

  - \[ [CALCITE-1686](https://issues.apache.org/jira/browse/CALCITE-1686)\]
    Only allow `FINAL` and other functions inside `MATCH_RECOGNIZE` (Zhiqiang-He)
  - \[ [CALCITE-1689](https://issues.apache.org/jira/browse/CALCITE-1689)\]
    Remove `PATTERN_DEFINE_AS` in SqlStdOperatorTable; `MATCH_RECOGNIZE` now uses
    `AS` (Zhiqiang-He)
- \[ [CALCITE-1668](https://issues.apache.org/jira/browse/CALCITE-1668)\]
Simplify `1 = 1` to `TRUE`, `1 > 2` to `FALSE` (Kevin Risden)
- \[ [CALCITE-1598](https://issues.apache.org/jira/browse/CALCITE-1598)\]
Pig adapter (Eli Levine)
- \[ [CALCITE-1661](https://issues.apache.org/jira/browse/CALCITE-1661)\]
Druid adapter: Support aggregation functions on `DECIMAL` columns
- \[ [CALCITE-1615](https://issues.apache.org/jira/browse/CALCITE-1615)\]
Support `HOP` and `SESSION` functions in the `GROUP BY` clause
(Julian Hyde and Haohui Mai)
- \[ [CALCITE-1494](https://issues.apache.org/jira/browse/CALCITE-1494)\]
More efficient plan for correlated sub-queries, omitting value-generating
scans where possible
- \[ [CALCITE-1638](https://issues.apache.org/jira/browse/CALCITE-1638)\]
Simplify `$x = $x` to `$x is not null`
- \[ [CALCITE-884](https://issues.apache.org/jira/browse/CALCITE-884)\]
File adapter (Henry Olson)

  - \[ [CALCITE-1704](https://issues.apache.org/jira/browse/CALCITE-1704)\]
    Execute queries on CSV files using simple `sqlline` command
  - \[ [CALCITE-1676](https://issues.apache.org/jira/browse/CALCITE-1676)\]
    Scan directory for .csv, .json and .gz files
  - Allow multiple Calcite columns to be derived from one HTML column,
    e.g. Location → Lat, Lon
  - Improved pattern match: added `matchSeq` to allow selection of
    _n_ th match
  - Add replace patterns to cell parsing logic
  - Add handling for tables without `<TH>` elements
  - Unit tests using local files (URL tests are contingent on network
    access)
  - Ability to parse HTML, CSV and JSON from local files
  - Combine the [optiq-web](https://github.com/HenryOlson/optiq-web)
    project with code from the
    [CSV adapter](https://calcite.apache.org/org/apache/calcite/adapter/csv/package-summary.html)
- \[ [CALCITE-1652](https://issues.apache.org/jira/browse/CALCITE-1652)\]
Allow `GROUPING` function to have multiple arguments, like `GROUPING_ID`
- \[ [CALCITE-1634](https://issues.apache.org/jira/browse/CALCITE-1634)\]
Make `RelBuilder.distinct` no-op if input is already distinct; use it in
`RelDecorrelator`
- \[ [CALCITE-1635](https://issues.apache.org/jira/browse/CALCITE-1635)\]
Add `MinRowCount` metadata
- \[ [CALCITE-1628](https://issues.apache.org/jira/browse/CALCITE-1628)\]
Add an alternative match pattern for `SemiJoinRule`
- \[ [CALCITE-1618](https://issues.apache.org/jira/browse/CALCITE-1618)\]
`SortProjectTransposeRule` should check for monotonicity preserving `CAST`
- \[ [CALCITE-1510](https://issues.apache.org/jira/browse/CALCITE-1510)\]
In `INSERT`/`UPSERT` without an explicit target column list, allow fewer source
columns than table (Kevin Liew)

  - Check for default value only when target field is null
    (Rajeshbabu Chintaguntla)
- \[ [CALCITE-1603](https://issues.apache.org/jira/browse/CALCITE-1603)\]
Support `TUMBLE` window function in the `GROUP BY` clause (Julian Hyde and
Haohui Mai)
- \[ [CALCITE-1606](https://issues.apache.org/jira/browse/CALCITE-1606)\]
Add datetime scalar functions (Laurent Goujon)
- \[ [CALCITE-1604](https://issues.apache.org/jira/browse/CALCITE-1604)\]
Add JDBC/ODBC scalar functions `DATABASE`, `IFNULL`, `USER` (Laurent Goujon)
- \[ [CALCITE-1549](https://issues.apache.org/jira/browse/CALCITE-1549)\]
More helpful error message when schema, table or column not found
- \[ [CALCITE-420](https://issues.apache.org/jira/browse/CALCITE-420)\]
Add `REPLACE` function, callable with and without JDBC escape syntax (Riccardo
Tommasini)
- \[ [CALCITE-1557](https://issues.apache.org/jira/browse/CALCITE-1557)\]
Add numeric scalar functions (Laurent Goujon)
- \[ [CALCITE-1258](https://issues.apache.org/jira/browse/CALCITE-1258)\]
JDK9

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-12-0 "Permalink")

- \[ [CALCITE-1716](https://issues.apache.org/jira/browse/CALCITE-1716)\]
Fix Cassandra integration tests
- \[ [CALCITE-1715](https://issues.apache.org/jira/browse/CALCITE-1715)\]
Downgrade to Guava 19.0 to fix Cassandra incompatibility
- \[ [CALCITE-1706](https://issues.apache.org/jira/browse/CALCITE-1706)\]
Disable `DruidAggregateFilterTransposeRule`, because it causes fine-grained
aggregations to be pushed to Druid
- \[ [CALCITE-1695](https://issues.apache.org/jira/browse/CALCITE-1695)\]
Add class `RexSimplify`, providing an explicit `RexExecutor` for methods to
simplify `RexNode`s
- \[ [CALCITE-1694](https://issues.apache.org/jira/browse/CALCITE-1694)\]
Pig adapter: Use the shaded Avatica dependency instead
- \[ [CALCITE-1561](https://issues.apache.org/jira/browse/CALCITE-1561)\]
Make `PigTest` cluster aware of data files; hopefully this will prevent
intermittent test failures (Eli Levine)
- \[ [CALCITE-1696](https://issues.apache.org/jira/browse/CALCITE-1696)\]
Support `RexLocalRef` for `EXPLAIN PLAN AS JSON`
- \[ [CALCITE-1683](https://issues.apache.org/jira/browse/CALCITE-1683)\]
Druid-specific rules to transpose `Filter` with other relations
(Nishant Bangarwa)
- \[ [CALCITE-1684](https://issues.apache.org/jira/browse/CALCITE-1684)\]
Change default precision of `VARCHAR` and `VARBINARY` types from 1 to
“unspecified” (Kevin Liew)
- \[ [CALCITE-1691](https://issues.apache.org/jira/browse/CALCITE-1691)\]
`ClassCastException` in `RelOptUtil.containsNullableFields`, attempting to
convert executor to `RexExecutorImpl`
- \[ [CALCITE-1688](https://issues.apache.org/jira/browse/CALCITE-1688)\]
Infinite loop during materialization substitution if query contains `Union`,
`Minus` or `Intersect`
- \[ [CALCITE-1665](https://issues.apache.org/jira/browse/CALCITE-1665)\]
`HAVING` support in `RelToSqlConverter` (Zhiqiang He)
- \[ [CALCITE-1673](https://issues.apache.org/jira/browse/CALCITE-1673)\]
In CSV adapter, query with `ORDER BY` or `GROUP BY` on `TIMESTAMP` column
throws CompileException (Gangadhar Kairi)
- \[ [CALCITE-1674](https://issues.apache.org/jira/browse/CALCITE-1674)\]
`LIKE` does not match value that contains newline (Mark Payne)
- \[ [CALCITE-1675](https://issues.apache.org/jira/browse/CALCITE-1675)\]
Two-level column name cannot be resolved in `ORDER BY`
- \[ [CALCITE-1667](https://issues.apache.org/jira/browse/CALCITE-1667)\]
Forbid calls to JDK APIs that use the default locale, time zone or character
set
- \[ [CALCITE-1656](https://issues.apache.org/jira/browse/CALCITE-1656)\]
Improve cost function in `DruidQuery` to encourage early column pruning
(Nishant Bangarwa)
- \[ [CALCITE-1664](https://issues.apache.org/jira/browse/CALCITE-1664)\]
`CAST('<string>' as TIMESTAMP)` wrongly adds part of sub-second fraction to the
value
- \[ [CALCITE-1659](https://issues.apache.org/jira/browse/CALCITE-1659)\]
Simplifying `CAST('YYYY-MM-DD hh:mm:ss.SSS' as TIMESTAMP)` should round the
sub-second fraction (Remus Rusanu)
- \[ [CALCITE-1439](https://issues.apache.org/jira/browse/CALCITE-1439)\]
Handle errors during constant reduction
- \[ [CALCITE-1653](https://issues.apache.org/jira/browse/CALCITE-1653)\]
Pass an expression executor to `RexUtil.simplify` for constant reduction (Remus
Rusanu)
- \[ [CALCITE-1601](https://issues.apache.org/jira/browse/CALCITE-1601)\]
`DateRangeRules` loses OR filters
- \[ [CALCITE-1637](https://issues.apache.org/jira/browse/CALCITE-1637)\]
Add mutable equivalents for all relational expressions (e.g. `MutableFilter`)
- \[ [CALCITE-1621](https://issues.apache.org/jira/browse/CALCITE-1621)\]
Add a cast around the NULL literal in aggregate rules (Anton Mushin)

  - Add `RexBuilder.makeNullLiteral(RelDataType)`
- \[ [CALCITE-1649](https://issues.apache.org/jira/browse/CALCITE-1649)\]
Data type mismatch in `EnumerableMergeJoin`
- \[ [CALCITE-1636](https://issues.apache.org/jira/browse/CALCITE-1636)\]
JDBC adapter generates wrong SQL for self join with sub-query (Zhiqiang-He)
- \[ [CALCITE-1633](https://issues.apache.org/jira/browse/CALCITE-1633)\]
In plans, output `Correlate.joinType` attribute in lower-case, same as
`Join.joinType`
- \[ [CALCITE-1632](https://issues.apache.org/jira/browse/CALCITE-1632)\]
Return type of “datetime + interval” expression
- \[ [CALCITE-365](https://issues.apache.org/jira/browse/CALCITE-365)\]
`AssertionError` while translating query with `WITH` and correlated sub-query
- \[ [CALCITE-1623](https://issues.apache.org/jira/browse/CALCITE-1623)\]
Make sure `DATE`, `TIME` and `TIMESTAMP` literals have `Calendar` with GMT
timezone
- \[ [CALCITE-1619](https://issues.apache.org/jira/browse/CALCITE-1619)\]
`CAST` is ignored by rules pushing operators into `DruidQuery`
- \[ [CALCITE-1617](https://issues.apache.org/jira/browse/CALCITE-1617)\]
Druid adapter: Send timestamp literals to Druid as local time, not UTC
- \[ [CALCITE-1500](https://issues.apache.org/jira/browse/CALCITE-1500)\]
Decouple materialization and lattice substitution from `VolcanoPlanner`
- \[ [CALCITE-1589](https://issues.apache.org/jira/browse/CALCITE-1589)\]
Druid adapter: `timeseries` query shows all days, even if no data
- \[ [CALCITE-1572](https://issues.apache.org/jira/browse/CALCITE-1572)\]
`JdbcSchema` throws exception when detecting nullable columns (Wu Xiang)
- \[ [CALCITE-1610](https://issues.apache.org/jira/browse/CALCITE-1610)\]
`RelBuilder` sort-combining optimization treats aliases incorrectly (Jess
Balint)
- \[ [CALCITE-1595](https://issues.apache.org/jira/browse/CALCITE-1595)\]
`RelBuilder.call` throws `NullPointerException` if argument types are invalid
(Jess Balint)
- \[ [CALCITE-1602](https://issues.apache.org/jira/browse/CALCITE-1602)\]
Remove uses of deprecated APIs
- \[ [CALCITE-1569](https://issues.apache.org/jira/browse/CALCITE-1569)\]
Code generation for fields of type `java.sql.Date` (Zhen Wang)
- \[ [CALCITE-1582](https://issues.apache.org/jira/browse/CALCITE-1582)\]
`RelToSqlConverter` doesn’t handle cartesian join (Jess Balint)
- \[ [CALCITE-1597](https://issues.apache.org/jira/browse/CALCITE-1597)\]
Obsolete `Util.newInternal`, `.pre`, `.post`, `.permAssert` and
`Throwables.propagate`
- \[ [CALCITE-1586](https://issues.apache.org/jira/browse/CALCITE-1586)\]
JDBC adapter generates wrong SQL if `UNION` has more than two inputs (Zhiqiang
He)
- \[ [CALCITE-1535](https://issues.apache.org/jira/browse/CALCITE-1535)\]
Give error if column referenced in `ORDER BY` is ambiguous (Zhen Wang)
- \[ [CALCITE-1594](https://issues.apache.org/jira/browse/CALCITE-1594)\]
`ConventionTraitDef.getConversionData()` is not thread-safe
- \[ [CALCITE-1577](https://issues.apache.org/jira/browse/CALCITE-1577)\]
Druid adapter: Incorrect result - limit on timestamp disappears
- \[ [CALCITE-1587](https://issues.apache.org/jira/browse/CALCITE-1587)\]
Druid adapter: `topN` query returns approximate results
- \[ [CALCITE-1578](https://issues.apache.org/jira/browse/CALCITE-1578)\]
Druid adapter: wrong semantics of `topN` query limit with granularity
- Druid adapter: Add `enum Granularity`
- \[ [CALCITE-1592](https://issues.apache.org/jira/browse/CALCITE-1592)\]
`SqlToRelConverter` throws `UnsupportedOperationException` if query has
`NOT ... NOT IN`
- \[ [CALCITE-1590](https://issues.apache.org/jira/browse/CALCITE-1590)\]
Support Guava version 21.0
- \[ [CALCITE-1575](https://issues.apache.org/jira/browse/CALCITE-1575)\]
Literals may lose precision during expression reduction
- \[ [CALCITE-1546](https://issues.apache.org/jira/browse/CALCITE-1546)\]
Wrong plan for `NOT IN` sub-queries with disjunction
- \[ [CALCITE-1574](https://issues.apache.org/jira/browse/CALCITE-1574)\]
Memory leak in maven
- \[ [CALCITE-1571](https://issues.apache.org/jira/browse/CALCITE-1571)\]
Could not resolve view with `SimpleCalciteSchema`
- \[ [CALCITE-1558](https://issues.apache.org/jira/browse/CALCITE-1558)\]
`AggregateExpandDistinctAggregatesRule` gets field mapping wrong if group key
is used in aggregate function (Zhenghua Gao)
- \[ [CALCITE-1562](https://issues.apache.org/jira/browse/CALCITE-1562)\]
Update jsr305 from 1.3.9 to 3.0.1
- \[ [CALCITE-1563](https://issues.apache.org/jira/browse/CALCITE-1563)\]
In case-insensitive connection, non-existent tables use alphabetically
preceding table
- \[ [CALCITE-1544](https://issues.apache.org/jira/browse/CALCITE-1544)\]
`AggregateJoinTransposeRule` fails to preserve row type (Kurt Young)
- \[ [CALCITE-1543](https://issues.apache.org/jira/browse/CALCITE-1543)\]
Correlated scalar sub-query with multiple aggregates gives `AssertionError`
(Kurt Young)

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-12-0 "Permalink")

- Maryann Xue joins PMC
- Add 3 new committers (Gian Merlino, Jess Balint, Laurent Goujon)
- \[ [CALCITE-1657](https://issues.apache.org/jira/browse/CALCITE-1657)\]
Release Calcite 1.12.0
- \[ [CALCITE-1677](https://issues.apache.org/jira/browse/CALCITE-1677)\]
Replace duplicate avatica docs with a redirect
- \[ [CALCITE-1685](https://issues.apache.org/jira/browse/CALCITE-1685)\]
Site: `defaultNullCollation` key listed as `materializationsEnabled`
(Kevin Liew)
- Add MapD to [Powered by\\
Calcite](https://calcite.apache.org/docs/powered_by.html) page (Todd Mostak)
- Diagram of logos of projects and products powered by Calcite
- \[ [CALCITE-1622](https://issues.apache.org/jira/browse/CALCITE-1622)\]
Bugs in website example code (Damjan Jovanovic)

## [1.11.0](https://github.com/apache/calcite/releases/tag/calcite-1.11.0) / 2017-01-09 [Permalink](https://calcite.apache.org/docs/history.html\#v1-11-0 "Permalink")

Nearly three months after the previous release, there is a long list
of improvements and bug-fixes, many of them making planner rules
smarter.

Several adapters have improvements:

- The JDBC adapter can now push down DML (`INSERT`, `UPDATE`, `DELETE`),
windowed aggregates (`OVER`), `IS NULL` and `IS NOT NULL` operators.
- The Cassandra adapter now supports authentication.
- Several key bug-fixes in the Druid adapter.

For correlated and uncorrelated sub-queries, we generate more
efficient plans (for example, in some correlated queries we no longer
require a sub-query to generate the values of the correlating
variable), can now handle multiple correlations, and have also fixed a
few correctness bugs.

New SQL syntax:

- `CROSS APPLY` and `OUTER APPLY`;
- `MINUS` as a synonym for `EXCEPT`;
- an `AS JSON` option for the `EXPLAIN` command;
- compound identifiers in the target list of `INSERT`, allowing you to
insert into individual fields of record-valued columns (or column
families if you are using the Apache Phoenix adapter).

A variety of new and extended built-in functions: `CONVERT`, `LTRIM`,
`RTRIM`, 3-parameter `LOCATE` and `POSITION`, `RAND`, `RAND_INTEGER`,
and `SUBSTRING` applied to binary types.

There are minor but potentially breaking API changes in
\[ [CALCITE-1519](https://issues.apache.org/jira/browse/CALCITE-1519)\]
(interface `SubqueryConverter` becomes `SubQueryConverter` and some
similar changes in the case of classes and methods) and
\[ [CALCITE-1530](https://issues.apache.org/jira/browse/CALCITE-1530)\]
(rename `Shuttle` to `Visitor`, and create a new class `Visitor<R>`).
See the cases for more details.

Compatibility: This release is tested
on Linux, macOS, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
Guava versions 14.0 to 19.0;
Druid version 0.9.1.1;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-11-0 "Permalink")

- \[ [CALCITE-1551](https://issues.apache.org/jira/browse/CALCITE-1551)\]
Preserve alias in `RelBuilder.project` (Jess Balint)
- \[ [CALCITE-1552](https://issues.apache.org/jira/browse/CALCITE-1552)\]
Add `RAND` function, returning `DOUBLE` values in the range 0..1
- \[ [CALCITE-1414](https://issues.apache.org/jira/browse/CALCITE-1414)\]
Add `RAND_INTEGER` function, which returns a random integer modulo N (Julian
Feinauer)
- \[ [CALCITE-1540](https://issues.apache.org/jira/browse/CALCITE-1540)\]
Support multiple columns in `PARTITION BY` clause of window function
(Hongbin Ma)
- \[ [CALCITE-1534](https://issues.apache.org/jira/browse/CALCITE-1534)\]
Allow compound identifiers in `INSERT` target column list
- \[ [CALCITE-1529](https://issues.apache.org/jira/browse/CALCITE-1529)\]
Support `CREATE TABLE` in tests (and only in tests)
- \[ [CALCITE-1527](https://issues.apache.org/jira/browse/CALCITE-1527)\]
Support DML in the JDBC adapter (Christian Tzolov)
- \[ [CALCITE-1523](https://issues.apache.org/jira/browse/CALCITE-1523)\]
In `RelBuilder`, add `field` method to reference input to join by alias (Jess
Balint)
- \[ [CALCITE-1524](https://issues.apache.org/jira/browse/CALCITE-1524)\]
Add a project to the planner root so that rules know which output fields are
used
- \[ [CALCITE-1425](https://issues.apache.org/jira/browse/CALCITE-1425)\]
Support two-level column structure in `INSERT`/`UPDATE`/`MERGE`
- \[ [CALCITE-1472](https://issues.apache.org/jira/browse/CALCITE-1472)\]
Support `CROSS`/`OUTER APPLY` syntax (Jark Wu)
- \[ [CALCITE-1506](https://issues.apache.org/jira/browse/CALCITE-1506)\]
Push `OVER` clause to underlying SQL via JDBC adapter (Christian Tzolov)
- \[ [CALCITE-1509](https://issues.apache.org/jira/browse/CALCITE-1509)\]
Allow overriding the convertlet table in CalcitePrepareImpl (Gian Merlino)
- \[ [CALCITE-1483](https://issues.apache.org/jira/browse/CALCITE-1483)\]
Generate simpler logic for `NOT IN` if we can deduce that the key is never null
- \[ [CALCITE-1497](https://issues.apache.org/jira/browse/CALCITE-1497)\]
Infer `IS NOT NULL`, and project predicates
- \[ [CALCITE-1489](https://issues.apache.org/jira/browse/CALCITE-1489)\]
Add rule, `AggregateValuesRule`, that applies to an `Aggregate` on an empty
relation (Gian Merlino)
- \[ [CALCITE-1447](https://issues.apache.org/jira/browse/CALCITE-1447)\]
Implement `INTERSECT DISTINCT` by rewriting to `UNION ALL` and counting
(Pengcheng Xiong)
- \[ [CALCITE-1389](https://issues.apache.org/jira/browse/CALCITE-1389)\]
Add a rewrite rule to use materialized views with joins
- \[ [CALCITE-1125](https://issues.apache.org/jira/browse/CALCITE-1125)\]
`MINUS` as a synonym for `EXCEPT` (enabled in Oracle10 conformance)
(Chandni Singh)
- \[ [CALCITE-1453](https://issues.apache.org/jira/browse/CALCITE-1453)\]
Support `ANY` type with binary comparison and arithmetic operators
(Jungtaek Lim)
- \[ [CALCITE-1444](https://issues.apache.org/jira/browse/CALCITE-1444)\]
Add `CONVERT` function (Laurent Goujon)
- \[ [CALCITE-1448](https://issues.apache.org/jira/browse/CALCITE-1448)\]
Add rules to flatten and prune `Intersect` and `Minus`;
flatten set-operators if the top is `DISTINCT` and bottom is `ALL`
- \[ [CALCITE-1426](https://issues.apache.org/jira/browse/CALCITE-1426)\]
Support customized star expansion in `Table`
- \[ [CALCITE-1454](https://issues.apache.org/jira/browse/CALCITE-1454)\]
Allow custom implementations of `SqlConformance`
- \[ [CALCITE-1417](https://issues.apache.org/jira/browse/CALCITE-1417)\]
In `RelBuilder`, simplify “CAST(literal TO type)” to a literal when possible
- \[ [CALCITE-1443](https://issues.apache.org/jira/browse/CALCITE-1443)\]
Add authentication support in Cassandra adapter
- \[ [CALCITE-1404](https://issues.apache.org/jira/browse/CALCITE-1404)\]
Implement `FILTER` on aggregate functions in `Interpreter`
- \[ [CALCITE-1418](https://issues.apache.org/jira/browse/CALCITE-1418)\]
Implement `SUBSTRING` function for `BINARY` and `VARBINARY` (Jungtaek Lim)
- \[ [CALCITE-1422](https://issues.apache.org/jira/browse/CALCITE-1422)\]
In JDBC adapter, allow `IS NULL` and `IS NOT NULL` operators in generated SQL
join condition (Viktor Batytskyi)
- \[ [CALCITE-1419](https://issues.apache.org/jira/browse/CALCITE-1419)\]
Implement JDBC functions: `LTRIM`, `RTRIM` and 3-parameter `LOCATE` and
`POSITION` (Jungtaek Lim)
- \[ [CALCITE-917](https://issues.apache.org/jira/browse/CALCITE-917)\]
Add `AS JSON` as output option for `EXPLAIN`

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-11-0 "Permalink")

- \[ [CALCITE-1559](https://issues.apache.org/jira/browse/CALCITE-1559)\]
Convert example models to stricter JSON
- \[ [CALCITE-1560](https://issues.apache.org/jira/browse/CALCITE-1560)\]
Remove `avatica` directory from `sqlline`’s class path
- Remove non-ASCII characters from Java source files
- \[ [CALCITE-1511](https://issues.apache.org/jira/browse/CALCITE-1511)\]
Decorrelation fails if query has more than one `EXISTS` in `WHERE` clause
- \[ [CALCITE-1555](https://issues.apache.org/jira/browse/CALCITE-1555)\]
Improve `RelNode` validation
- \[ [CALCITE-1548](https://issues.apache.org/jira/browse/CALCITE-1548)\]
Instantiate function objects once per query
- Add lock to `JdbcAdapterTest`, to ensure that tests that modify data run in
series
- \[ [CALCITE-1519](https://issues.apache.org/jira/browse/CALCITE-1519)\]
Standardize on “sub-query” rather than “subquery” in class names and comments
- \[ [CALCITE-1493](https://issues.apache.org/jira/browse/CALCITE-1493)\]
Wrong plan for `NOT IN` correlated queries
- \[ [CALCITE-1526](https://issues.apache.org/jira/browse/CALCITE-1526)\]
Use `Strong` to infer whether a predicate’s inputs may be null
- \[ [CALCITE-1530](https://issues.apache.org/jira/browse/CALCITE-1530)\]
Create a visitor to traverse linq4j expressions without mutating them, and
rename `Visitor` to `Shuttle`
- \[ [CALCITE-1507](https://issues.apache.org/jira/browse/CALCITE-1507)\]
`OFFSET` cannot be pushed through a `JOIN` if the non-preserved side of outer
join is not count-preserving
- \[ [CALCITE-1522](https://issues.apache.org/jira/browse/CALCITE-1522)\]
Fix error message for `SetOp` with incompatible args (Jess Balint)
- \[ [CALCITE-1532](https://issues.apache.org/jira/browse/CALCITE-1532)\]
In `HttpUtils`, don’t log HTTP requests; they may contain user name, password
- \[ [CALCITE-1037](https://issues.apache.org/jira/browse/CALCITE-1037)\]
Column uniqueness is calculated incorrectly for `Correlate` (Alexey Makhmutov)
- \[ [CALCITE-1495](https://issues.apache.org/jira/browse/CALCITE-1495)\]
`SemiJoinRule` should not apply to `RIGHT` and `FULL JOIN`, and should strip
`LEFT JOIN`
- \[ [CALCITE-1516](https://issues.apache.org/jira/browse/CALCITE-1516)\]
Upgrade `hydromatic-resource-maven-plugin`, and re-work `SaffronProperties`
- \[ [CALCITE-1498](https://issues.apache.org/jira/browse/CALCITE-1498)\]
Avoid `LIMIT` with trivial `ORDER BY` being pushed through `JOIN` endlessly
- \[ [CALCITE-1501](https://issues.apache.org/jira/browse/CALCITE-1501)\]
`EnumerableUnion` should use array comparator when row format is `ARRAY` (Dayue
Gao)
- \[ [CALCITE-1502](https://issues.apache.org/jira/browse/CALCITE-1502)\]
`AssertionError` in `ReduceExpressionsRule` when `CASE` is used with optional
value and literal (Serhii Harnyk)
- Cosmetic changes, and deprecate some methods
- \[ [CALCITE-1486](https://issues.apache.org/jira/browse/CALCITE-1486)\]
Invalid “Invalid literal” error for complex expression
- \[ [CALCITE-1488](https://issues.apache.org/jira/browse/CALCITE-1488)\]
`ValuesReduceRule` should ignore empty `Values`
- \[ [CALCITE-1384](https://issues.apache.org/jira/browse/CALCITE-1384)\]
Extension point for `ALTER` statements (Gabriel Reid)
- \[ [CALCITE-1484](https://issues.apache.org/jira/browse/CALCITE-1484)\]
Upgrade Apache parent POM to version 18
- \[ [CALCITE-1482](https://issues.apache.org/jira/browse/CALCITE-1482)\]
Fix leak on CassandraSchema creation
- \[ [CALCITE-1479](https://issues.apache.org/jira/browse/CALCITE-1479)\]
`AssertionError` in `ReduceExpressionsRule` on multi-column `IN` sub-query
(Gian Merlino)
- Upgrade `Quidem`
- \[ [CALCITE-1416](https://issues.apache.org/jira/browse/CALCITE-1416)\]
Make classes implement `AutoCloseable` where possible (Chinmay Kolhatkar)
- \[ [CALCITE-1474](https://issues.apache.org/jira/browse/CALCITE-1474)\]
Upgrade `aggdesigner`
- \[ [CALCITE-1270](https://issues.apache.org/jira/browse/CALCITE-1270)\]
Upgrade to `avatica-1.9`, `sqlline-1.2.0`
- \[ [CALCITE-1461](https://issues.apache.org/jira/browse/CALCITE-1461)\]
Hard-coded class name in `JaninoRelMetadataProvider` breaks shading (Jark Wu)
- \[ [CALCITE-1465](https://issues.apache.org/jira/browse/CALCITE-1465)\]
Store constants as a derived field in `RelOptPredicateList`
- \[ [CALCITE-1429](https://issues.apache.org/jira/browse/CALCITE-1429)\]
Druid adapter must send `fromNext` when requesting rows from Druid (Jiarong
Wei)
- \[ [CALCITE-1430](https://issues.apache.org/jira/browse/CALCITE-1430)\]
In Druid adapter, `pagingIdentifiers` might have more than one value (Jiarong
Wei)
- \[ [CALCITE-1442](https://issues.apache.org/jira/browse/CALCITE-1442)\]
Interval fractional second precision returns wrong value (Laurent Goujon)
- \[ [CALCITE-1434](https://issues.apache.org/jira/browse/CALCITE-1434)\]
User-defined aggregate function that uses a generic interface (Arun Mahadevan)
- \[ [CALCITE-1431](https://issues.apache.org/jira/browse/CALCITE-1431)\]
`RelDataTypeFactoryImpl.copyType()` did not copy `StructKind`
- \[ [CALCITE-1424](https://issues.apache.org/jira/browse/CALCITE-1424)\]
Druid type is called `FLOAT`, not `DOUBLE` (Jiarong Wei)
- \[ [CALCITE-1415](https://issues.apache.org/jira/browse/CALCITE-1415)\]
Add sub-query support for RelStructuredTypeFlattener

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-11-0 "Permalink")

- Change PMC chair
- \[ [CALCITE-1459](https://issues.apache.org/jira/browse/CALCITE-1459)\]
Add Apache Apex to “Powered By” page (Chinmay Kolhatkar)

## [1.10.0](https://github.com/apache/calcite/releases/tag/calcite-1.10.0) / 2016-10-12 [Permalink](https://calcite.apache.org/docs/history.html\#v1-10-0 "Permalink")

This release comes shortly after 1.9.0. It includes mainly bug-fixes for the core and
Druid adapter. For the latest, we fixed an
[important issue](https://issues.apache.org/jira/browse/CALCITE-1403) that
prevented us from handling consistently time dimensions in different time zones.

Compatibility: This release is tested
on Linux, Mac OS X, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
Guava versions 14.0 to 19.0;
Druid version 0.9.1.1;
other software versions as specified in `pom.xml`.

#### New feature [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-10-0 "Permalink")

- \[ [CALCITE-1374](https://issues.apache.org/jira/browse/CALCITE-1374)\]
Support operator `!=` as an alternative to `<>`

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-10-0 "Permalink")

- \[ [CALCITE-1378](https://issues.apache.org/jira/browse/CALCITE-1378)\]
`ArrayIndexOutOfBoundsException` in sql-to-rel conversion for two-level columns
- \[ [CALCITE-1379](https://issues.apache.org/jira/browse/CALCITE-1379)\]
When expanding `STAR`, expand sub-fields in `RecordType` columns of `StructKind.PEEK_FIELDS` and `StructKind.PEEK_FIELDS_DEFAULT`
- \[ [CALCITE-1381](https://issues.apache.org/jira/browse/CALCITE-1381)\]
Function quantifier should be retained in a cloned Sql call (zhengdong)
- \[ [CALCITE-1386](https://issues.apache.org/jira/browse/CALCITE-1386)\]
`ITEM` operator ignores the value type of the collection, assigns to Object variable (Jungtaek Lim)
- \[ [CALCITE-1392](https://issues.apache.org/jira/browse/CALCITE-1392)\]
Druid default time column not properly recognized
- \[ [CALCITE-1394](https://issues.apache.org/jira/browse/CALCITE-1394)\]
Using `CoreMatchers.containsString` causes javadoc errors
- \[ [CALCITE-1396](https://issues.apache.org/jira/browse/CALCITE-1396)\]
`isDeterministic` only explores top `RexCall`
- \[ [CALCITE-1397](https://issues.apache.org/jira/browse/CALCITE-1397)\]
`ClassCastException` in `FilterReduceExpressionsRule`
- \[ [CALCITE-1398](https://issues.apache.org/jira/browse/CALCITE-1398)\]
Change visibility of `RelFieldTrimmer` utility methods
- \[ [CALCITE-1400](https://issues.apache.org/jira/browse/CALCITE-1400)\]
`AggregatePullUpConstantsRule` might adjust aggregation function parameters indices wrongly
- \[ [CALCITE-1402](https://issues.apache.org/jira/browse/CALCITE-1402)\]
Druid Filter translation incorrect if input reference is in RHS of comparison
- \[ [CALCITE-1403](https://issues.apache.org/jira/browse/CALCITE-1403)\]
`DruidAdapterIT` broken
- \[ [CALCITE-1420](https://issues.apache.org/jira/browse/CALCITE-1420)\]
Allow Calcite JDBC Driver minor version to be greater than 9

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-10-0 "Permalink")

- \[ [CALCITE-1393](https://issues.apache.org/jira/browse/CALCITE-1393)\]
Exclude packages `org.apache.calcite.benchmarks.generated`, `org.openjdk.jmh` from javadoc

## [1.9.0](https://github.com/apache/calcite/releases/tag/calcite-1.9.0) / 2016-09-22 [Permalink](https://calcite.apache.org/docs/history.html\#v1-9-0 "Permalink")

This release includes extensions and fixes for the Druid adapter. New features were
added, such as the capability to
[recognize and translate Timeseries and TopN Druid queries](https://issues.apache.org/jira/browse/CALCITE-1357).
Moreover, this release contains multiple bug-fixes over the initial implementation of the
adapter. It is worth mentioning that most of these fixes were contributed by Druid developers,
which demonstrates the good reception of the adapter by that community.

We have added new SQL features too, e.g.,
[support for `LATERAL TABLE`](https://issues.apache.org/jira/browse/CALCITE-1309).
There are multiple interesting extensions to the planner rules that should contribute to
obtain better plans, such as
[avoiding doing the same join twice](https://issues.apache.org/jira/browse/CALCITE-1288)
in the presence of `COUNT DISTINCT`, or being able to
[simplify the expressions](https://issues.apache.org/jira/browse/CALCITE-1220)
in the plan further. In addition, we implemented a rule to
[convert predicates on `EXTRACT` function calls into date ranges](https://issues.apache.org/jira/browse/CALCITE-1334).
The rule is not specific to Druid; however, in principle, it will be useful to identify
filter conditions on the time dimension of Druid data sources.

Finally, the release includes more than thirty bug-fixes, minor enhancements and internal
changes to planner rules and APIs.

Compatibility: This release is tested
on Linux, Mac OS X, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
Guava versions 14.0 to 19.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-9-0 "Permalink")

- \[ [CALCITE-1208](https://issues.apache.org/jira/browse/CALCITE-1208)\]
Improve two-level column structure handling
- \[ [CALCITE-1227](https://issues.apache.org/jira/browse/CALCITE-1227)\]
Add streaming CSV table (Zhen Wang)
- \[ [CALCITE-1309](https://issues.apache.org/jira/browse/CALCITE-1309)\]
Support `LATERAL TABLE` (Jark Wu)

#### Druid adapter [Permalink](https://calcite.apache.org/docs/history.html\#druid-adapter-1-9-0 "Permalink")

- \[ [CALCITE-1292](https://issues.apache.org/jira/browse/CALCITE-1292)\]
Druid metadata query is very slow (Michael Spector)
- \[ [CALCITE-1324](https://issues.apache.org/jira/browse/CALCITE-1324)\]
Druid metadata query throws exception if there are non-standard aggregators (Martin Karlsch)
- \[ [CALCITE-1343](https://issues.apache.org/jira/browse/CALCITE-1343)\]
Broken Druid query
- \[ [CALCITE-1348](https://issues.apache.org/jira/browse/CALCITE-1348)\]
In Druid adapter, adjust how `SegmentMetadataQuery` is used to detect types (Gian Merlino)
- \[ [CALCITE-1357](https://issues.apache.org/jira/browse/CALCITE-1357)\]
Recognize Druid `Timeseries` and `TopN` queries in `DruidQuery`
- \[ [CALCITE-1358](https://issues.apache.org/jira/browse/CALCITE-1358)\]
Push filters on time dimension to Druid

#### Planner rules [Permalink](https://calcite.apache.org/docs/history.html\#planner-rules-1-9-0 "Permalink")

- \[ [CALCITE-1220](https://issues.apache.org/jira/browse/CALCITE-1220)\]
Further extend simplify for reducing expressions
- \[ [CALCITE-1288](https://issues.apache.org/jira/browse/CALCITE-1288)\]
Avoid doing the same join twice if count(distinct) exists (Gautam Parai)
- \[ [CALCITE-1289](https://issues.apache.org/jira/browse/CALCITE-1289)\]
`RexUtil.simplifyCase()` should account for nullability
- \[ [CALCITE-1290](https://issues.apache.org/jira/browse/CALCITE-1290)\]
When converting to CNF, fail if the expression size exceeds a threshold
- \[ [CALCITE-1334](https://issues.apache.org/jira/browse/CALCITE-1334)\]
Convert predicates on `EXTRACT` function calls into date ranges
- \[ [CALCITE-1342](https://issues.apache.org/jira/browse/CALCITE-1342)\]
`ProjectPusher` should use rel factories when creating new rels, e.g. project/filter
- \[ [CALCITE-1365](https://issues.apache.org/jira/browse/CALCITE-1365)\]
Introduce `UnionPullUpConstantsRule`

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-9-0 "Permalink")

- \[ [CALCITE-30](https://issues.apache.org/jira/browse/CALCITE-30)\]
Implement `Statement.cancel` method
- \[ [CALCITE-308](https://issues.apache.org/jira/browse/CALCITE-308)\]
Wrong result when using `DATE`+`INTERVAL` arithmetics
- \[ [CALCITE-319](https://issues.apache.org/jira/browse/CALCITE-319)\]
Table aliases should follow case-sensitivity policy
- \[ [CALCITE-528](https://issues.apache.org/jira/browse/CALCITE-528)\]
Creating output row type of a Join does not obey case-sensitivity flags
- \[ [CALCITE-991](https://issues.apache.org/jira/browse/CALCITE-991)\]
Create separate `SqlFunctionCategory` values for table functions and macros (Julien Le Dem)
- \[ [CALCITE-1043](https://issues.apache.org/jira/browse/CALCITE-1043)\]
`RexOptUtil` does not support function table other than `SqlStdOperatorTable`
- \[ [CALCITE-1095](https://issues.apache.org/jira/browse/CALCITE-1095)\]
`NOT` precedence
- \[ [CALCITE-1148](https://issues.apache.org/jira/browse/CALCITE-1148)\]
Trait conversion broken for `RelTraits` other than `Convention`
- \[ [CALCITE-1278](https://issues.apache.org/jira/browse/CALCITE-1278)\]
CalciteSignature’s ColumnMetaData for `DELETE` should be same as `INSERT`
- \[ [CALCITE-1283](https://issues.apache.org/jira/browse/CALCITE-1283)\]
Nullability incorrectly assigned in `SqlTypeFactory.leastRestrictiveSqlType()`
- \[ [CALCITE-1284](https://issues.apache.org/jira/browse/CALCITE-1284)\]
Move `Quidem` tests from `JdbcTest` into their own class
- \[ [CALCITE-1297](https://issues.apache.org/jira/browse/CALCITE-1297)\]
`RelBuilder` should rename fields without creating an identity Project (Jark Wu)
- \[ [CALCITE-1302](https://issues.apache.org/jira/browse/CALCITE-1302)\]
Create `SqlTypeName` values for each interval range, e.g. `YEAR_MONTH`
- \[ [CALCITE-1305](https://issues.apache.org/jira/browse/CALCITE-1305)\]
Case-insensitive table aliases and `GROUP BY`
- \[ [CALCITE-1310](https://issues.apache.org/jira/browse/CALCITE-1310)\]
Infer type of arguments to `BETWEEN` operator (Yiming Liu)
- \[ [CALCITE-1312](https://issues.apache.org/jira/browse/CALCITE-1312)\]
Return type of `TIMESTAMP_ADD` applied to a `DATE` should be `TIMESTAMP` if unit is smaller than `DAY`
- \[ [CALCITE-1313](https://issues.apache.org/jira/browse/CALCITE-1313)\]
Validator should derive type of expression in `ORDER BY`
- \[ [CALCITE-1314](https://issues.apache.org/jira/browse/CALCITE-1314)\]
Intermittent failure in `SqlParserTest.testGenerateKeyWords`
- \[ [CALCITE-1321](https://issues.apache.org/jira/browse/CALCITE-1321)\]
In-list to join optimization should have configurable in-list size (Gautam Parai)
- \[ [CALCITE-1327](https://issues.apache.org/jira/browse/CALCITE-1327)\]
Nested aggregate windowed query fails (Gautam Parai)
- \[ [CALCITE-1330](https://issues.apache.org/jira/browse/CALCITE-1330)\]
DB2 does not support character sets in data type
- \[ [CALCITE-1332](https://issues.apache.org/jira/browse/CALCITE-1332)\]
JDBC adapter for DB2 should always use aliases for tables: `x.y.z AS z`
- \[ [CALCITE-1333](https://issues.apache.org/jira/browse/CALCITE-1333)\]
`AggFunctions` supported by `JdbcAggregate` should depend on `SqlKind`, instead of operator instance
- \[ [CALCITE-1336](https://issues.apache.org/jira/browse/CALCITE-1336)\]
Add view name to the `ViewExpander` (Julien Le Dem)
- \[ [CALCITE-1337](https://issues.apache.org/jira/browse/CALCITE-1337)\]
Lazy evaluate `RexCall` digests (Ted Xu)
- \[ [CALCITE-1340](https://issues.apache.org/jira/browse/CALCITE-1340)\]
Window aggregates invalid error/error messages in some cases (Gautam Parai)
- \[ [CALCITE-1344](https://issues.apache.org/jira/browse/CALCITE-1344)\]
Incorrect inferred precision when `BigDecimal` value is less than 1
- \[ [CALCITE-1346](https://issues.apache.org/jira/browse/CALCITE-1346)\]
Invalid nested window aggregate query with alias (Gautam Parai)
- \[ [CALCITE-1360](https://issues.apache.org/jira/browse/CALCITE-1360)\]
Custom schema in file in current directory gives `NullPointerException`
- \[ [CALCITE-1366](https://issues.apache.org/jira/browse/CALCITE-1366)\]
Metadata provider should not pull predicates up through `GROUP BY`
- \[ [CALCITE-1370](https://issues.apache.org/jira/browse/CALCITE-1370)\]
In `SqlKind`, add `OTHER_DDL` to `DDL` enum set (Rajeshbabu Chintaguntla)
- \[ [CALCITE-1372](https://issues.apache.org/jira/browse/CALCITE-1372)\]
Calcite generate wrong field names in JDBC adapter

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-9-0 "Permalink")

- \[ [CALCITE-1229](https://issues.apache.org/jira/browse/CALCITE-1229)\]
Restore API and Test API links to site
- \[ [CALCITE-1325](https://issues.apache.org/jira/browse/CALCITE-1325)\]
Druid adapter requires Guava 14.0 or higher
- \[ [CALCITE-1329](https://issues.apache.org/jira/browse/CALCITE-1329)\]
As part of release, generate a file containing multiple digests

## [1.8.0](https://github.com/apache/calcite/releases/tag/calcite-1.8.0) / 2016-06-13 [Permalink](https://calcite.apache.org/docs/history.html\#v1-8-0 "Permalink")

This release adds adapters for
[Elasticsearch](https://issues.apache.org/jira/browse/CALCITE-1253) and
[Druid](https://issues.apache.org/jira/browse/CALCITE-1121).
It is also now easier to
[make a JDBC connection based upon a single adapter](https://issues.apache.org/jira/browse/CALCITE-1259).

There are several new SQL features: `UNNEST` with
[multiple arguments](https://issues.apache.org/jira/browse/CALCITE-855),
[MAP arguments](https://issues.apache.org/jira/browse/CALCITE-1250)
and [with a JOIN](https://issues.apache.org/jira/browse/CALCITE-1225);
a [DESCRIBE](https://issues.apache.org/jira/browse/CALCITE-1168) statement;
and a [TRANSLATE](https://issues.apache.org/jira/browse/CALCITE-1115)
function like the one in Oracle and Postgres.
We also added support for
[SELECT without FROM](https://issues.apache.org/jira/browse/CALCITE-1120)
(equivalent to the `VALUES` clause, and widely used in MySQL and Postgres),
and added a
[conformance](https://calcite.apache.org/docs/adapter.html#jdbc-connect-string-parameters)
parameter to allow you to selectively enable this and other SQL features.

And a couple of dozen bug-fixes and enhancements to planner rules and APIs.

Compatibility: This release is tested
on Linux, Mac OS X, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
Guava versions 14.0 to 19.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-8-0 "Permalink")

- \[ [CALCITE-1177](https://issues.apache.org/jira/browse/CALCITE-1177)\]
Extend list of supported time units in `EXTRACT`, `CEIL` and `FLOOR` functions
(Venki Korukanti)
- \[ [CALCITE-1259](https://issues.apache.org/jira/browse/CALCITE-1259)\]
Allow connecting to a single schema without writing a model
- \[ [CALCITE-750](https://issues.apache.org/jira/browse/CALCITE-750)\]
Support aggregates within windowed aggregates (Gautam Parai)
- \[ [CALCITE-1250](https://issues.apache.org/jira/browse/CALCITE-1250)\]
`UNNEST` applied to `MAP` data type (Johannes Schulte)
- \[ [CALCITE-1253](https://issues.apache.org/jira/browse/CALCITE-1253)\]
Elasticsearch adapter (Subhobrata Dey)
- \[ [CALCITE-1228](https://issues.apache.org/jira/browse/CALCITE-1228)\]
Bind parameters in `INSERT`
- \[ [CALCITE-1120](https://issues.apache.org/jira/browse/CALCITE-1120)\]
`SELECT` without `FROM` (Jimmy Xiang)
- \[ [CALCITE-855](https://issues.apache.org/jira/browse/CALCITE-855)\]
`UNNEST` with multiple arguments
- \[ [CALCITE-1225](https://issues.apache.org/jira/browse/CALCITE-1225)\]
`UNNEST` with `JOIN`
- \[ [CALCITE-1115](https://issues.apache.org/jira/browse/CALCITE-1115)\]
Add `TRANSLATE` function with 3 parameters, like the one in Oracle (Javanshir
Yelchiyev)
- \[ [CALCITE-1168](https://issues.apache.org/jira/browse/CALCITE-1168)\]
Add `DESCRIBE` statement (Arina Ielchiieva)
- \[ [CALCITE-1121](https://issues.apache.org/jira/browse/CALCITE-1121)\]
Druid adapter

  - \[ [CALCITE-1276](https://issues.apache.org/jira/browse/CALCITE-1276)\]
    In Druid adapter, deduce tables and columns if not specified
- \[ [CALCITE-1207](https://issues.apache.org/jira/browse/CALCITE-1207)\]
Allow numeric connection properties, and ‘K’, ‘M’, ‘G’ suffixes

#### Planner rules [Permalink](https://calcite.apache.org/docs/history.html\#planner-rules-1-8-0 "Permalink")

- \[ [CALCITE-1235](https://issues.apache.org/jira/browse/CALCITE-1235)\]
Fully push down `LIMIT` \+ `OFFSET` in Cassandra
- \[ [CALCITE-1216](https://issues.apache.org/jira/browse/CALCITE-1216)\]
Rule to convert `Filter`-on-`Scan` to materialized view (Amogh Margoor)
- \[ [CALCITE-1200](https://issues.apache.org/jira/browse/CALCITE-1200)\]
Extend `RelOptUtil.splitJoinCondition` to handle `IS NOT DISTINCT FROM`
(Venki Korukanti)
- \[ [CALCITE-1211](https://issues.apache.org/jira/browse/CALCITE-1211)\]
Allow free use of `CassandraSort` for `LIMIT`
- \[ [CALCITE-1210](https://issues.apache.org/jira/browse/CALCITE-1210)\]
Allow UUID filtering in Cassandra
- \[ [CALCITE-1182](https://issues.apache.org/jira/browse/CALCITE-1182)\]
Add `ProjectRemoveRule` to pre-processing program of materialization
substitution

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-8-0 "Permalink")

- \[ [CALCITE-1281](https://issues.apache.org/jira/browse/CALCITE-1281)\]
Druid adapter wrongly returns all numeric values as `int` or `float`
- \[ [CALCITE-1279](https://issues.apache.org/jira/browse/CALCITE-1279)\]
Druid “select” query gives `ClassCastException`
- \[ [CALCITE-1277](https://issues.apache.org/jira/browse/CALCITE-1277)\]
Rat fails on source distribution due to `git.properties`
- Update KEYS
- \[ [CALCITE-1252](https://issues.apache.org/jira/browse/CALCITE-1252)\]
Handle `ANY` type in `RexBuilder.ensureType` and `TypeFactory.leastRestrictive`
(Mehand Baid, Minji Kim)
- \[ [CALCITE-1151](https://issues.apache.org/jira/browse/CALCITE-1151)\]
Fix `SqlSetOption` to correctly handle `SqlOperator.createCall`
(Sudheesh Katkam, Minji Kim)
- \[ [CALCITE-1106](https://issues.apache.org/jira/browse/CALCITE-1106)\]
Expose constructor for `ProjectJoinTransposeRule` (Minji Kim)
- \[ [CALCITE-1107](https://issues.apache.org/jira/browse/CALCITE-1107)\]
Make `SqlSumEmptyIsZeroAggFunction` constructor public (Minji Kim)
- \[ [CALCITE-1269](https://issues.apache.org/jira/browse/CALCITE-1269)\]
Replace `IntList` with Guava `Ints` class
- \[ [CALCITE-1239](https://issues.apache.org/jira/browse/CALCITE-1239)\]
Upgrade to avatica-1.8.0
- \[ [CALCITE-1266](https://issues.apache.org/jira/browse/CALCITE-1266)\]
`RelBuilder.field` gets offsets wrong
- \[ [CALCITE-1264](https://issues.apache.org/jira/browse/CALCITE-1264)\]
`Litmus` argument interpolation (Chris Baynes)
- \[ [CALCITE-1245](https://issues.apache.org/jira/browse/CALCITE-1245)\]
Allow `RelBuilder.scan` to take qualified table name (Chris Baynes)
- Move code from `Enumerables` to `EnumerableDefaults`
- \[ [CALCITE-1246](https://issues.apache.org/jira/browse/CALCITE-1246)\]
Cleanup duplicate variables in `JoinPushThroughJoinRule` (Yi Xinglu)
- \[ [CALCITE-1241](https://issues.apache.org/jira/browse/CALCITE-1241)\]
Add a Freemarker variable for adding non reserved keyword list to `Parser.jj`
template (Venki Korukanti)

  - Create a table in `SqlParserTest` of reserved keywords from various versions
    of the SQL standard
- \[ [CALCITE-1150](https://issues.apache.org/jira/browse/CALCITE-1150)\]
Add dynamic record type and dynamic star for schema-on-read table
- \[ [CALCITE-1238](https://issues.apache.org/jira/browse/CALCITE-1238)\]
Unparsing a query with `LIMIT` but no `ORDER BY` gives invalid SQL (Emmanuel
Bastien)
- \[ [CALCITE-1230](https://issues.apache.org/jira/browse/CALCITE-1230)\]
Add SQLSTATE reference data as `enum SqlState` in Avatica, and
deprecate `SqlStateCodes` in Calcite
- \[ [CALCITE-1199](https://issues.apache.org/jira/browse/CALCITE-1199)\]
Incorrect trimming of `CHAR` when performing cast to `VARCHAR`
- \[ [CALCITE-1219](https://issues.apache.org/jira/browse/CALCITE-1219)\]
Add method `SqlOperatorBinding.isOperandLiteral()` (Hsuan-Yi Chu)
- \[ [CALCITE-1222](https://issues.apache.org/jira/browse/CALCITE-1222)\]
`DatabaseMetaData.getColumnLabel` returns null when query has `ORDER BY`
- \[ [CALCITE-1215](https://issues.apache.org/jira/browse/CALCITE-1215)\]
Fix missing override in `CassandraTable`
- \[ [CALCITE-1212](https://issues.apache.org/jira/browse/CALCITE-1212)\]
Fix NPE on some Cassandra projects
- Remove trailing spaces from all source files
- Move HTTP utilities from Splunk adapter to core
- Test case for
\[ [PHOENIX-2767](https://issues.apache.org/jira/browse/PHOENIX-2767)\],
non-constant in `IN`
- \[ [CALCITE-1166](https://issues.apache.org/jira/browse/CALCITE-1166)\]
Disallow sub-classes of `RelOptRuleOperand`
- Remove all calls to deprecated methods
- Add class `ConsList`
- More of \[ [CALCITE-999](https://issues.apache.org/jira/browse/CALCITE-999)\]
Clean up maven POM files
- \[ [CALCITE-1204](https://issues.apache.org/jira/browse/CALCITE-1204)\]
Fix invalid Javadoc and suppress checkstyle “errors”
- \[ [CALCITE-1170](https://issues.apache.org/jira/browse/CALCITE-1170)\]
Allow `SqlSetOperator` to be overridden, as a regular `SqlOperator` can
(Hsuan-Yi Chu)
- \[ [CALCITE-746](https://issues.apache.org/jira/browse/CALCITE-746)\]
Allow apache-rat to be run outside of release process

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-8-0 "Permalink")

- \[ [CALCITE-1273](https://issues.apache.org/jira/browse/CALCITE-1273)\]
Following
\[ [CALCITE-306](https://issues.apache.org/jira/browse/CALCITE-306)\],
update references to `EnumerableTableAccessRel` to `EnumerableTableScan`
- Fix typo in SQL (Yi Xinglu)
- Site: add committer, and post slides/video from Polyalgebra talk
- \[ [CALCITE-1203](https://issues.apache.org/jira/browse/CALCITE-1203)\]
Update to github-pages-67
- \[ [CALCITE-1202](https://issues.apache.org/jira/browse/CALCITE-1202)\]
Lock version of Jekyll for bundler
- Site: add upcoming talks, and fix link to Apache phonebook

## [1.7.0](https://github.com/apache/calcite/releases/tag/calcite-1.7.0) / 2016-03-22 [Permalink](https://calcite.apache.org/docs/history.html\#v1-7-0 "Permalink")

This is the first Apache Calcite release since
[Avatica became an independent project](https://calcite.apache.org/avatica/news/2016/03/03/separate-project/).
Calcite now depends on [Avatica](https://calcite.apache.org/avatica/) in the
same way as it does other libraries, via a Maven dependency. To see
Avatica-related changes, see the
[release notes for Avatica 1.7.1](https://calcite.apache.org/avatica/docs/history.html#v1-7-1).

We have [added](https://issues.apache.org/jira/browse/CALCITE-1080)
an [adapter](https://calcite.apache.org/docs/adapter.html) for
[Apache Cassandra](https://cassandra.apache.org/).
You can map a Cassandra keyspace into Calcite as a schema, Cassandra
CQL tables as tables, and execute SQL queries on them, which Calcite
converts into [CQL](https://cassandra.apache.org/doc/cql/CQL.html).
Cassandra can define and maintain materialized views but the adapter
goes further: it can transparently rewrite a query to use a
materialized view even if the view is not mentioned in the query.

This release adds an
[Oracle-compatibility mode](https://issues.apache.org/jira/browse/CALCITE-1066).
If you add `fun=oracle` to your JDBC connect string, you get all of
the standard operators and functions plus Oracle-specific functions
`DECODE`, `NVL`, `LTRIM`, `RTRIM`, `GREATEST` and `LEAST`. We look
forward to adding more functions, and compatibility modes for other
databases, in future releases.

We’ve replaced our use of JUL (`java.util.logging`)
with [SLF4J](https://slf4j.org/). SLF4J provides an API which Calcite can use
independent of the logging implementation. This ultimately provides additional
flexibility to users, allowing them to configure Calcite’s logging within their
own chosen logging framework. This work was done in
\[ [CALCITE-669](https://issues.apache.org/jira/browse/CALCITE-669)\].

For users experienced with configuring JUL in Calcite previously, there are some
differences as some the JUL logging levels do not exist in SLF4J: `FINE`,
`FINER`, and `FINEST`, specifically. To deal with this, `FINE` was mapped
to SLF4J’s `DEBUG` level, while `FINER` and `FINEST` were mapped to SLF4J’s `TRACE`.

Compatibility: This release is tested
on Linux, Mac OS X, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
Guava versions 12.0.1 to 19.0;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-7-0 "Permalink")

- \[ [CALCITE-1124](https://issues.apache.org/jira/browse/CALCITE-1124)\]
Add `TIMESTAMPADD`, `TIMESTAMPDIFF` functions (Arina Ielchiieva)
- \[ [CALCITE-1066](https://issues.apache.org/jira/browse/CALCITE-1066)\]
Add Oracle function table, and functions `DECODE`, `NVL`, `LTRIM`, `RTRIM`,
`GREATEST`, `LEAST`
- \[ [CALCITE-1080](https://issues.apache.org/jira/browse/CALCITE-1080)\]
Cassandra adapter (Michael Mior)
- \[ [CALCITE-1062](https://issues.apache.org/jira/browse/CALCITE-1062)\]
In validation, lookup a (possibly overloaded) operator from an operator
table (Hsuan-Yi Chu)
- \[ [CALCITE-551](https://issues.apache.org/jira/browse/CALCITE-551)\]
Sub-query inside aggregate function

#### Planner rules [Permalink](https://calcite.apache.org/docs/history.html\#planner-rules-1-7-0 "Permalink")

- \[ [CALCITE-1158](https://issues.apache.org/jira/browse/CALCITE-1158)\]
Make `AggregateRemoveRule` extensible
- \[ [CALCITE-1116](https://issues.apache.org/jira/browse/CALCITE-1116)\]
Extend `simplify` for reducing expressions
- \[ [CALCITE-1104](https://issues.apache.org/jira/browse/CALCITE-1104)\]
Materialized views in Cassandra (Michael Mior)
- \[ [CALCITE-1130](https://issues.apache.org/jira/browse/CALCITE-1130)\]
Add support for operators `IS NULL` and `IS NOT NULL` in
`RexImplicationChecker` (Amogh Margoor)
- \[ [CALCITE-1129](https://issues.apache.org/jira/browse/CALCITE-1129)\]
Extend `JoinUnionTransposeRule` to match `Union` instead of `LogicalUnion`
(Vasia Kalavri)
- \[ [CALCITE-1109](https://issues.apache.org/jira/browse/CALCITE-1109)\]
Fix up condition when pushing `Filter` through `Aggregate` (Amogh Margoor)
- \[ [CALCITE-1100](https://issues.apache.org/jira/browse/CALCITE-1100)\]
If constant reduction no-ops, don’t create a new `RelNode` (Hsuan-Yi Chu)
- \[ [CALCITE-1076](https://issues.apache.org/jira/browse/CALCITE-1076)\]
Update `RelMdDistribution` to match other metadata APIs (Ted Xu)
- \[ [CALCITE-1056](https://issues.apache.org/jira/browse/CALCITE-1056)\]
In `RelBuilder`, simplify predicates, and optimize away `WHERE FALSE`
- \[ [CALCITE-1059](https://issues.apache.org/jira/browse/CALCITE-1059)\]
Not valid to convert `Aggregate` on empty to empty if its `GROUP BY` key is empty

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-7-0 "Permalink")

- \[ [CALCITE-1147](https://issues.apache.org/jira/browse/CALCITE-1147)\]
Allow multiple providers for the same kind of metadata
- \[ [CALCITE-1153](https://issues.apache.org/jira/browse/CALCITE-1153)\]
Invalid cast created during SQL Join in Oracle (Chris Atkinson)
- \[ [CALCITE-1146](https://issues.apache.org/jira/browse/CALCITE-1146)\]
Wrong path in CSV example model (wanglan)
- \[ [CALCITE-1156](https://issues.apache.org/jira/browse/CALCITE-1156)\]
Increase Jetty version to 9.2.15.v20160210
- \[ [CALCITE-1064](https://issues.apache.org/jira/browse/CALCITE-1064)\]
Address problematic `maven-remote-resources-plugin`
- In `TimeUnit` add `WEEK`, `QUARTER`, `MICROSECOND` values, and change type of
`multiplier`
- Deprecate `SqlLiteral.SqlSymbol`; `SqlSymbol` can now wrap any enum
- \[ [CALCITE-1078](https://issues.apache.org/jira/browse/CALCITE-1078)\]
Detach avatica from the core calcite Maven project

  - \[ [CALCITE-1077](https://issues.apache.org/jira/browse/CALCITE-1077)\]
    Switch Calcite to the released Avatica 1.7.1
  - Update `groupId` when Calcite POMs reference Avatica modules
  - \[ [CALCITE-1137](https://issues.apache.org/jira/browse/CALCITE-1137)\]
    Exclude Avatica from Calcite source release
- \[ [CALCITE-1111](https://issues.apache.org/jira/browse/CALCITE-1111)\]
Upgrade Guava, and test on a range of Guava versions
- \[ [CALCITE-1054](https://issues.apache.org/jira/browse/CALCITE-1054)\]
Wrong code generation for `TIMESTAMP` values that may be `NULL`
- \[ [CALCITE-604](https://issues.apache.org/jira/browse/CALCITE-604)\]
Tune metadata by generating a dispatcher at runtime
- \[ [CALCITE-1063](https://issues.apache.org/jira/browse/CALCITE-1063)\]
Flat lists for 4, 5, 6 elements
- Add Orinoco schema (streaming retail data), accessible from Quidem scripts
- \[ [CALCITE-1097](https://issues.apache.org/jira/browse/CALCITE-1097)\]
Exception when executing query with too many aggregation columns (chenzhifa)
- Add tests for leap days
- \[ [CALCITE-553](https://issues.apache.org/jira/browse/CALCITE-553)\]
In maven, enable compiler profiles by default
- \[ [CALCITE-1031](https://issues.apache.org/jira/browse/CALCITE-1031)\]
In prepared statement, `CsvScannableTable.scan` is called twice
- \[ [CALCITE-1046](https://issues.apache.org/jira/browse/CALCITE-1046)\]
Matchers for testing SQL query results
- \[ [CALCITE-1083](https://issues.apache.org/jira/browse/CALCITE-1083)\]
`SqlNode.equalsDeep` has O(n ^ 2) performance
- \[ [CALCITE-998](https://issues.apache.org/jira/browse/CALCITE-998)\]
Exception when calling `STDDEV_SAMP`, `STDDEV_POP` (Matthew Shaer)
- \[ [CALCITE-1071](https://issues.apache.org/jira/browse/CALCITE-1071)\]
Improve hash functions
- \[ [CALCITE-1072](https://issues.apache.org/jira/browse/CALCITE-1072)\]
CSV adapter incorrectly parses `TIMESTAMP` values after noon (Chris Albright)
- \[ [CALCITE-669](https://issues.apache.org/jira/browse/CALCITE-669)\]
Mass removal of Java Logging for SLF4J
- \[ [CALCITE-1068](https://issues.apache.org/jira/browse/CALCITE-1068)\]
Deprecate `Stacks`
- \[ [CALCITE-1067](https://issues.apache.org/jira/browse/CALCITE-1067)\]
Test failures due to clashing temporary table names
- \[ [CALCITE-864](https://issues.apache.org/jira/browse/CALCITE-864)\]
Correlation variable has incorrect row type if it is populated by right side
of a Join
- \[ [CALCITE-1021](https://issues.apache.org/jira/browse/CALCITE-1021)\]
Upgrade Jackson
- \[ [CALCITE-999](https://issues.apache.org/jira/browse/CALCITE-999)\]
Clean up maven POM files

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-7-0 "Permalink")

- \[ [CALCITE-1112](https://issues.apache.org/jira/browse/CALCITE-1112)\]
“Powered by Calcite” page
- Add SQL-Gremlin to Adapters page
- \[ [CALCITE-1090](https://issues.apache.org/jira/browse/CALCITE-1090)\]
Revise Streaming SQL specification
- Appoint Josh Elser to PMC
- Add “Streaming SQL” talk
- \[ [CALCITE-623](https://issues.apache.org/jira/browse/CALCITE-623)\]
Add a small blurb to the site about Jenkins for CI
- \[ [CALCITE-1070](https://issues.apache.org/jira/browse/CALCITE-1070)\]
Upgrade to new Apache logo
- Document how to announce a release
- \[ [CALCITE-1074](https://issues.apache.org/jira/browse/CALCITE-1074)\]
Delete old releases from mirroring system

## [1.6.0](https://github.com/apache/calcite/releases/tag/calcite-1.6.0) / 2016-01-22 [Permalink](https://calcite.apache.org/docs/history.html\#v1-6-0 "Permalink")

As usual in this release, there are new SQL features, improvements to
planning rules and Avatica, and lots of bug-fixes. We’ll spotlight a
couple of features make it easier to handle complex queries.

\[ [CALCITE-816](https://issues.apache.org/jira/browse/CALCITE-816)\]
allows you to represent sub-queries (`EXISTS`, `IN` and scalar) as
`RexSubQuery`, a kind of expression in the relational algebra. Until
now, the sql-to-rel converter was burdened with expanding sub-queries,
and people creating relational algebra directly (or via RelBuilder)
could only create ‘flat’ relational expressions. Now we have planner
rules to expand and de-correlate sub-queries.

Metadata is the fuel that powers query planning. It includes
traditional query-planning statistics such as cost and row-count
estimates, but also information such as which columns form unique
keys, unique and what predicates are known to apply to a relational
expression’s output rows. From the predicates we can deduce which
columns are constant, and following
\[ [CALCITE-1023](https://issues.apache.org/jira/browse/CALCITE-1023)\]
we can now remove constant columns from `GROUP BY` keys.

Metadata is often computed recursively, and it is hard to safely and
efficiently calculate metadata on a graph of `RelNode`s that is large,
frequently cyclic, and constantly changing.
\[ [CALCITE-794](https://issues.apache.org/jira/browse/CALCITE-794)\]
introduces a context to each metadata call. That context can detect
cyclic metadata calls and produce a safe answer to the metadata
request. It will also allow us to add finer-grained caching and
further tune the metadata layer.

Compatibility: This release is tested
on Linux, Mac OS X, Microsoft Windows;
using Oracle JDK 1.7, 1.8;
other software versions as specified in `pom.xml`.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-6-0 "Permalink")

- \[ [CALCITE-816](https://issues.apache.org/jira/browse/CALCITE-816)\]
Represent sub-query as a `RexNode`
- \[ [CALCITE-854](https://issues.apache.org/jira/browse/CALCITE-854)\]
Implement `UNNEST ... WITH ORDINALITY`
- \[ [CALCITE-1003](https://issues.apache.org/jira/browse/CALCITE-1003)\]
Utility to convert `RelNode` to SQL (Amogh Margoor)

  - \[ [CALCITE-1010](https://issues.apache.org/jira/browse/CALCITE-1010)\]
    `FETCH/LIMIT` and `OFFSET` in RelToSqlConverter (Amogh Margoor)
  - Move code from `JdbcImplementor` and `JdbcRules` to new class
    `SqlImplementor`
  - Deduce dialect’s null collation from `DatabaseMetaData`
  - Fix `RelToSqlConverterTest` on Windows
- Following
\[ [CALCITE-897](https://issues.apache.org/jira/browse/CALCITE-897)\],
empty string for `boolean` properties means true
- \[ [CALCITE-992](https://issues.apache.org/jira/browse/CALCITE-992)\]
Validate and resolve sequence reference as a `Table` object
- \[ [CALCITE-968](https://issues.apache.org/jira/browse/CALCITE-968)\]
Stream-to-relation and stream-to-stream joins (Milinda Pathirage)
- \[ [CALCITE-1041](https://issues.apache.org/jira/browse/CALCITE-1041)\]
User-defined function that returns `DATE` or `TIMESTAMP` value
- \[ [CALCITE-986](https://issues.apache.org/jira/browse/CALCITE-986)\]
User-defined function with `DATE` or `TIMESTAMP` parameters
- \[ [CALCITE-958](https://issues.apache.org/jira/browse/CALCITE-958)\]
Overloaded Table Functions with named arguments (Julien Le Dem)
- \[ [CALCITE-970](https://issues.apache.org/jira/browse/CALCITE-970)\]
If `NULLS FIRST`/`NULLS LAST` not specified, sort `NULL` values high

#### Avatica features and bug-fixes [Permalink](https://calcite.apache.org/docs/history.html\#avatica-1-6-0 "Permalink")

- \[ [CALCITE-1040](https://issues.apache.org/jira/browse/CALCITE-1040)\]
Differentiate better between arrays and scalars in protobuf
- \[ [CALCITE-934](https://issues.apache.org/jira/browse/CALCITE-934)\]
Use an OS-assigned ephemeral port for `CalciteRemoteDriverTest`
- \[ [CALCITE-767](https://issues.apache.org/jira/browse/CALCITE-767)\]
Create Avatica RPC endpoints for commit and rollback commands
- \[ [CALCITE-983](https://issues.apache.org/jira/browse/CALCITE-983)\]
Handle nulls in `ErrorResponse`’s protobuf representation better
- \[ [CALCITE-989](https://issues.apache.org/jira/browse/CALCITE-989)\]
Add server’s address in each response
- Fix some bugs found by static analysis
- Make all `equals` and `hashCode` methods uniform
- \[ [CALCITE-962](https://issues.apache.org/jira/browse/CALCITE-962)\]
Propagate the cause, not just the cause’s message, from `JdbcMeta`

#### Planner rules [Permalink](https://calcite.apache.org/docs/history.html\#planner-rules-1-6-0 "Permalink")

- \[ [CALCITE-1057](https://issues.apache.org/jira/browse/CALCITE-1057)\]
Add `RelMetadataProvider` parameter to standard planner `Program`s
- \[ [CALCITE-1055](https://issues.apache.org/jira/browse/CALCITE-1055)\]
`SubQueryRemoveRule` should create `Correlate`, not `Join`, for correlated
sub-queries
- \[ [CALCITE-978](https://issues.apache.org/jira/browse/CALCITE-978)\]
Enable customizing constant folding rule behavior when a `Filter` simplifies
to false (Jason Altekruse)
- \[ [CALCITE-977](https://issues.apache.org/jira/browse/CALCITE-977)\]
Make the constant expression `Executor` configurable in `FrameworkConfig`
(Jason Altekruse)
- \[ [CALCITE-1058](https://issues.apache.org/jira/browse/CALCITE-1058)\]
Add method `RelBuilder.empty`, and rewrite LIMIT 0 and WHERE FALSE to it
- \[ [CALCITE-996](https://issues.apache.org/jira/browse/CALCITE-996)\]
Simplify predicate when we create a `Filter` operator
- Simplify `RexProgram`, in particular `(NOT CASE ... END) IS TRUE`, which
occurs in when `NOT IN` is expanded
- Fix variant of
\[ [CALCITE-923](https://issues.apache.org/jira/browse/CALCITE-923)\]
that occurs in `RelOptRulesTest.testPushFilterPastProject`
- \[ [CALCITE-1023](https://issues.apache.org/jira/browse/CALCITE-1023)\]
and
\[ [CALCITE-1038](https://issues.apache.org/jira/browse/CALCITE-1038)\]
Planner rule that removes `Aggregate` keys that are constant
- \[ [CALCITE-1018](https://issues.apache.org/jira/browse/CALCITE-1018)\]
`SortJoinTransposeRule` not firing due to `getMaxRowCount(RelSubset)` returning
null
- \[ [CALCITE-1019](https://issues.apache.org/jira/browse/CALCITE-1019)\]
`RelMdUtil.checkInputForCollationAndLimit()` was wrong with `alreadySorted`
check
- Not safe to use ‘=’ for predicates on constant expressions that might be null
- \[ [CALCITE-993](https://issues.apache.org/jira/browse/CALCITE-993)\]
Pull up all constant expressions, not just literals, as predicates
- \[ [CALCITE-1005](https://issues.apache.org/jira/browse/CALCITE-1005)\]
Handle null in `getMaxRowCount` for `Aggregate` (Mike Hinchey)
- \[ [CALCITE-995](https://issues.apache.org/jira/browse/CALCITE-995)\]
Sort transpose rules might fall in an infinite loop
- \[ [CALCITE-987](https://issues.apache.org/jira/browse/CALCITE-987)\]
Pushing `LIMIT 0` results in an infinite loop (Pengcheng Xiong)
- \[ [CALCITE-988](https://issues.apache.org/jira/browse/CALCITE-988)\]
`FilterToProjectUnifyRule.invert(MutableRel, MutableRel, MutableProject)`
works incorrectly
- \[ [CALCITE-969](https://issues.apache.org/jira/browse/CALCITE-969)\]
Composite `EnumerableSort` with `DESC` wrongly sorts `NULL` values low
- \[ [CALCITE-959](https://issues.apache.org/jira/browse/CALCITE-959)\]
Add description to `SortProjectTransposeRule`’s constructor

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-6-0 "Permalink")

- \[ [CALCITE-1060](https://issues.apache.org/jira/browse/CALCITE-1060)\]
Fix test deadlock by initializing `DriverManager` before registering `AlternatingDriver`
- \[ [CALCITE-1047](https://issues.apache.org/jira/browse/CALCITE-1047)\]
`ChunkList.clear` throws `AssertionError`
- \[ [CALCITE-1053](https://issues.apache.org/jira/browse/CALCITE-1053)\]
CPU spin, `ReflectiveRelMetadataProvider.apply` waiting for `HashMap.get`
- Upgrade toolbox, to fix line length issue on Windows
- \[ [CALCITE-1051](https://issues.apache.org/jira/browse/CALCITE-1051)\]
Underflow exception due to scaling IN clause literals (Frankie Bollaert)
- \[ [CALCITE-975](https://issues.apache.org/jira/browse/CALCITE-975)\]
Allow Planner to return validated row type together with SqlNode
- \[ [CALCITE-1020](https://issues.apache.org/jira/browse/CALCITE-1020)\]
Add `MILLISECOND` in `TimeUnit` (Pengcheng Xiong)
- \[ [CALCITE-794](https://issues.apache.org/jira/browse/CALCITE-794)\]
Detect cycles when computing statistics
( **This is a breaking change**.)
- Tune algorithm that deduces the return type of `AND` expression
- \[ [CALCITE-842](https://issues.apache.org/jira/browse/CALCITE-842)\]
Decorrelator gets field offsets confused if fields have been trimmed
- Fix `NullPointerException` in `SqlJoin.toString()`
- Add `ImmutableBitSet.rebuild()`
- \[ [CALCITE-915](https://issues.apache.org/jira/browse/CALCITE-915)\]
Tests now unset `ThreadLocal` values on exit
- \[ [CALCITE-1036](https://issues.apache.org/jira/browse/CALCITE-1036)\]
`DiffRepository` should not insert new resources at the end of the repository
- \[ [CALCITE-955](https://issues.apache.org/jira/browse/CALCITE-955)\]
`Litmus` (continuation-passing style for methods that check invariants)
- `RelBuilder.project` now does nothing if asked to project the identity with
the same field names
- Deprecate some `Util` methods, and upgrade last Maven modules to JDK 1.7
- Document `RelOptPredicateList`
- Add `ImmutableNullableList.copyOf(Iterable)`
- Fix “endPosTable already set” error from `javac`
- Add benchmark of `Parser.create(sql).parseQuery()`
- \[ [CALCITE-1042](https://issues.apache.org/jira/browse/CALCITE-1042)\]
Ensure that `FILTER` is `BOOLEAN NOT NULL`
- \[ [CALCITE-1039](https://issues.apache.org/jira/browse/CALCITE-1039)\]
Assign a `SqlKind` value for each built-in aggregate function
- \[ [CALCITE-1030](https://issues.apache.org/jira/browse/CALCITE-1030)\]
JSON `ModelHandler` calling `SchemaPlus.setCacheEnabled()` causes
`UnsupportedOperationException` when using `SimpleCalciteSchema`
- \[ [CALCITE-1028](https://issues.apache.org/jira/browse/CALCITE-1028)\]
Move populate materializations after sql-to-rel conversion
- \[ [CALCITE-1034](https://issues.apache.org/jira/browse/CALCITE-1034)\]
Use a custom checker for code style rules that Checkstyle cannot express
- \[ [CALCITE-1032](https://issues.apache.org/jira/browse/CALCITE-1032)\]
Verify javadoc of private methods
- \[ [CALCITE-1015](https://issues.apache.org/jira/browse/CALCITE-1015)\]
`OFFSET 0` causes `AssertionError` (Zhen Wang)
- \[ [CALCITE-1024](https://issues.apache.org/jira/browse/CALCITE-1024)\]
In a planner test, if a rule should have no effect, state that explicitly
- \[ [CALCITE-1016](https://issues.apache.org/jira/browse/CALCITE-1016)\]
`GROUP BY *constant*` on empty relation should return 0 rows
- \[ [CALCITE-1022](https://issues.apache.org/jira/browse/CALCITE-1022)\]
Rename `.oq` Quidem files to `.iq`
- \[ [CALCITE-980](https://issues.apache.org/jira/browse/CALCITE-980)\]
Fix `AND` and `OR` implementation in `Enumerable` convention
- \[ [CALCITE-459](https://issues.apache.org/jira/browse/CALCITE-459)\]
When parsing SQL, allow single line comment on last line (Zhen Wang)
- \[ [CALCITE-1009](https://issues.apache.org/jira/browse/CALCITE-1009)\]
`SelfPopulatingList` is not thread-safe
- \[ [CALCITE-1008](https://issues.apache.org/jira/browse/CALCITE-1008)\]
Replace `Closeable` with `AutoCloseable`
- \[ [CALCITE-1001](https://issues.apache.org/jira/browse/CALCITE-1001)\]
Upgrade to quidem-0.7
- \[ [CALCITE-990](https://issues.apache.org/jira/browse/CALCITE-990)\]
In `VolcanoPlanner`, populate `RelOptRuleCall.nodeInputs` for operands of type
“any”
- \[ [CALCITE-966](https://issues.apache.org/jira/browse/CALCITE-966)\]
`VolcanoPlanner` now clears `ruleNames` in order to avoid rule name
conflicting error
- Factor user-defined function tests from `JdbcTest` to `UdfTest`, and classes
into `Smalls`
- \[ [CALCITE-974](https://issues.apache.org/jira/browse/CALCITE-974)\]
Exception while validating `DELETE` (Yuri Au Yong)
- \[ [CALCITE-964](https://issues.apache.org/jira/browse/CALCITE-964)\]
Rename `timezone` connection property to `timeZone`

#### Web site and documentation [Permalink](https://calcite.apache.org/docs/history.html\#site-1-6-0 "Permalink")

- Avatica
  - \[ [CALCITE-1033](https://issues.apache.org/jira/browse/CALCITE-1033)\]
    Introduce Avatica protobuf documentation
  - \[ [CALCITE-1029](https://issues.apache.org/jira/browse/CALCITE-1029)\]
     Add “purpose” descriptions to Avatica JSON docs
  - \[ [CALCITE-984](https://issues.apache.org/jira/browse/CALCITE-984)\]
    Massive cleanup of Avatica JSON docs
- \[ [CALCITE-861](https://issues.apache.org/jira/browse/CALCITE-861)\]
Be explicit that `mvn test` needs to be invoked
- \[ [CALCITE-997](https://issues.apache.org/jira/browse/CALCITE-997)\]
Document keywords
- \[ [CALCITE-979](https://issues.apache.org/jira/browse/CALCITE-979)\]
Broken links in web site
- \[ [CALCITE-961](https://issues.apache.org/jira/browse/CALCITE-961)\]
Web site: Add downloads and Apache navigation links
- \[ [CALCITE-960](https://issues.apache.org/jira/browse/CALCITE-960)\]
Download links for pgp, md5, `KEYS` files, and direct from mirrors
- Remove embedded date-stamps from javadoc; add javadoc for test classes
- \[ [CALCITE-965](https://issues.apache.org/jira/browse/CALCITE-965)\]
Link to downloads page from each release news item

## [1.5.0](https://github.com/apache/calcite/releases/tag/calcite-1.5.0) / 2015-11-06 [Permalink](https://calcite.apache.org/docs/history.html\#v1-5-0 "Permalink")

Our first release as a top-level Apache project!

Avatica has undergone major improvements,
including a new RPC layer that uses
[protocol buffers](https://developers.google.com/protocol-buffers/),
support for DML statements, better support for bind variables and
unique identifiers for connections and statements.

There are lots of improvements to planner rules, and the logic
that replaces relational expressions with equivalent materializations.

We continue to find more uses for
[RelBuilder](https://calcite.apache.org/docs/algebra.html).
We now recommend that you use `RelBuilder` whenever you create
relational expressions within a planner rule; the rule can then be
re-used to create different sub-classes of relational expression, and
the builder will perform simple optimizations automatically.

Using `RelBuilder` we built Piglet,
a subset of the classic Hadoop language
[Pig](https://pig.apache.org/).
Pig is particularly interesting because it makes heavy use of nested
multi-sets. You can follow this example to implement your own query
language, and immediately taking advantage of Calcite’s back-ends and
optimizer rules. It’s all just algebra, after all!

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-5-0 "Permalink")

- \[ [CALCITE-911](https://issues.apache.org/jira/browse/CALCITE-911)\]
Add a variant of `CalciteSchema` that does not cache sub-objects
- \[ [CALCITE-845](https://issues.apache.org/jira/browse/CALCITE-845)\]
Derive `SUM`’s return type by a customizable policy (Maryann Xue)
- \[ [CALCITE-916](https://issues.apache.org/jira/browse/CALCITE-916)\]
Support table function that implements `ScannableTable`
  - Example table function that generates mazes and their solutions
- \[ [CALCITE-941](https://issues.apache.org/jira/browse/CALCITE-941)\]
Named, optional and `DEFAULT` arguments to function calls;
support named arguments when calling table functions and table macros
- \[ [CALCITE-910](https://issues.apache.org/jira/browse/CALCITE-910)\]
Improve handling of `ARRAY`, `MULTISET`, `STRUCT` types
- \[ [CALCITE-879](https://issues.apache.org/jira/browse/CALCITE-879)\]
`COLLECT` aggregate function
- \[ [CALCITE-546](https://issues.apache.org/jira/browse/CALCITE-546)\]
Allow table, column and field called ‘\*’
- \[ [CALCITE-893](https://issues.apache.org/jira/browse/CALCITE-893)\]
Theta join in JDBC adapter
- Linq4j: Implement `EnumerableDefaults` methods (MiNG)
- \[ [CALCITE-823](https://issues.apache.org/jira/browse/CALCITE-823)\]
Add `ALTER ... RESET` statement (Sudheesh Katkam)
- \[ [CALCITE-881](https://issues.apache.org/jira/browse/CALCITE-881)\]
Allow schema.table.column references in `GROUP BY`
- \[ [CALCITE-852](https://issues.apache.org/jira/browse/CALCITE-852)\]
DDL statements
- \[ [CALCITE-851](https://issues.apache.org/jira/browse/CALCITE-851)\]
Add original SQL string as a field in the parser
- \[ [CALCITE-819](https://issues.apache.org/jira/browse/CALCITE-819)\]
Add `RelRoot`, a contract for the result of a relational expression

#### Avatica features and bug-fixes [Permalink](https://calcite.apache.org/docs/history.html\#avatica-1-5-0 "Permalink")

- \[ [CALCITE-951](https://issues.apache.org/jira/browse/CALCITE-951)\]
Print the server-side stack in the local exception (Josh Elser)
- \[ [CALCITE-936](https://issues.apache.org/jira/browse/CALCITE-936)\]
Make HttpServer configurable (Navis Ryu)
- \[ [CALCITE-903](https://issues.apache.org/jira/browse/CALCITE-903)\]
Enable Avatica client to recover from missing server-side state (Josh Elser)
- \[ [CALCITE-921](https://issues.apache.org/jira/browse/CALCITE-921)\]
Fix incorrectness when calling `getString()` on binary data (Josh Elser)
- \[ [CALCITE-913](https://issues.apache.org/jira/browse/CALCITE-913)\]
Construct proper `ColumnMetaData` for arrays (Josh Elser)
- \[ [CALCITE-871](https://issues.apache.org/jira/browse/CALCITE-871)\]
In `JdbcMeta`, register each statement using an id from a generator (Bruno
Dumon)
- \[ [CALCITE-645](https://issues.apache.org/jira/browse/CALCITE-645)\]
Implement `AvaticaSqlException` to pass server-side exception information to
clients (Josh Elser)
- \[ [CALCITE-912](https://issues.apache.org/jira/browse/CALCITE-912)\]
Add Avatica `OpenConnectionRequest` (Bruno Dumon)
- \[ [CALCITE-919](https://issues.apache.org/jira/browse/CALCITE-919)\]
Avoid `setScale` on `BigDecimal` when scale is 0 (Josh Elser)
- \[ [CALCITE-927](https://issues.apache.org/jira/browse/CALCITE-927)\]
Call finagle for all calls that return ResultSetResponses (Josh Elser)
- \[ [CALCITE-705](https://issues.apache.org/jira/browse/CALCITE-705)\]
DML in Avatica, and split `Execute` out from `Fetch` request (Yeong Wei)
- \[ [CALCITE-914](https://issues.apache.org/jira/browse/CALCITE-914)\]
Add `JsonSubType` for `ExecuteResponse`, and fix JSON docs (Josh Elser)
- \[ [CALCITE-905](https://issues.apache.org/jira/browse/CALCITE-905)\]
`getTables` returns empty result in `JdbcMeta` (Jan Van Besien)
- \[ [CALCITE-906](https://issues.apache.org/jira/browse/CALCITE-906)\]
Avatica `JdbcMeta` statement IDs are not unique
- \[ [CALCITE-866](https://issues.apache.org/jira/browse/CALCITE-866)\]
Break out Avatica documentation and add JSON reference (Josh Elser)
- \[ [CALCITE-843](https://issues.apache.org/jira/browse/CALCITE-843)\]
`AvaticaConnection.getAutoCommit` throws `NullPointerException`
- \[ [CALCITE-840](https://issues.apache.org/jira/browse/CALCITE-840)\]
Protocol buffer serialization over HTTP for Avatica Server (Josh Elser)

#### Materializations [Permalink](https://calcite.apache.org/docs/history.html\#materializations-1-5-0 "Permalink")

- \[ [CALCITE-952](https://issues.apache.org/jira/browse/CALCITE-952)\]
Organize applicable materializations in reversed topological order (Maryann
Xue)
- \[ [CALCITE-890](https://issues.apache.org/jira/browse/CALCITE-890)\]
Register all combinations of materialization substitutions (Maryann Xue)
- \[ [CALCITE-891](https://issues.apache.org/jira/browse/CALCITE-891)\]
When substituting materializations, match `TableScan` without `Project`
(Maryann Xue)
- \[ [CALCITE-890](https://issues.apache.org/jira/browse/CALCITE-890)\]
Register all combinations of materialization substitutions (Maryann Xue)
- \[ [CALCITE-925](https://issues.apache.org/jira/browse/CALCITE-925)\]
Match materialized views when predicates contain strings and ranges (Amogh
Margoor)
- \[ [CALCITE-793](https://issues.apache.org/jira/browse/CALCITE-793)\]
Planner requires unnecessary collation when using materialized view (Maryann
Xue)
- \[ [CALCITE-825](https://issues.apache.org/jira/browse/CALCITE-825)\]
Allow user to specify sort order of an `ArrayTable`

#### Planner rules [Permalink](https://calcite.apache.org/docs/history.html\#planner-rules-1-5-0 "Permalink")

- \[ [CALCITE-953](https://issues.apache.org/jira/browse/CALCITE-953)\]
Improve `RelMdPredicates` to deal with `RexLiteral` (Pengcheng Xiong)
- \[ [CALCITE-939](https://issues.apache.org/jira/browse/CALCITE-939)\]
Variant of `SortUnionTransposeRule` for order-preserving `Union`
(Maryann Xue)
- \[ [CALCITE-931](https://issues.apache.org/jira/browse/CALCITE-931)\]
Wrong collation trait in `SortJoinTransposeRule` for right joins
(Maryann Xue)
- \[ [CALCITE-938](https://issues.apache.org/jira/browse/CALCITE-938)\]
More accurate rowCount for `Aggregate` applied to already unique keys
(Maryann Xue)
- \[ [CALCITE-935](https://issues.apache.org/jira/browse/CALCITE-935)\]
Improve how `ReduceExpressionsRule` handles duplicate constraints (Pengcheng
Xiong)
- \[ [CALCITE-922](https://issues.apache.org/jira/browse/CALCITE-922)\]
Extract value of an `INTERVAL` literal (Hsuan-Yi Chu)
- \[ [CALCITE-889](https://issues.apache.org/jira/browse/CALCITE-889)\]
Implement `SortUnionTransposeRule` (Pengcheng Xiong)
- \[ [CALCITE-909](https://issues.apache.org/jira/browse/CALCITE-909)\]
Make `ReduceExpressionsRule` extensible
- \[ [CALCITE-856](https://issues.apache.org/jira/browse/CALCITE-856)\]
Make more rules extensible
- \[ [CALCITE-902](https://issues.apache.org/jira/browse/CALCITE-902)\]
Match nullability when reducing expressions in a `Project`
- \[ [CALCITE-895](https://issues.apache.org/jira/browse/CALCITE-895)\]
Simplify “(`CASE` … `END`) = constant” inside `AND` or `OR` (Hsuan-Yi Chu)
- \[ [CALCITE-828](https://issues.apache.org/jira/browse/CALCITE-828)\]
Use RelBuilder in rules rather than type-specific RelNode factories
- \[ [CALCITE-892](https://issues.apache.org/jira/browse/CALCITE-892)\]
Implement `SortJoinTransposeRule`
- \[ [CALCITE-876](https://issues.apache.org/jira/browse/CALCITE-876)\]
After pushing `LogicalProject` past `LogicalWindow`, adjust references to
constants properly (Hsuan-Yi Chu)
- \[ [CALCITE-844](https://issues.apache.org/jira/browse/CALCITE-844)\]
Push `Project` through `Window` (Hsuan-Yi Chu)
- \[ [CALCITE-841](https://issues.apache.org/jira/browse/CALCITE-841)\]
Redundant windows when window function arguments are expressions (Hsuan-Yi
Chu)
- \[ [CALCITE-846](https://issues.apache.org/jira/browse/CALCITE-846)\]
Push `Aggregate` with `Filter` through `Union(all)`

#### RelBuilder and Piglet [Permalink](https://calcite.apache.org/docs/history.html\#rel-builder-1-5-0 "Permalink")

- \[ [CALCITE-933](https://issues.apache.org/jira/browse/CALCITE-933)\]
`RelBuilder.scan()` now gives a nice exception if the table does not exist
(Andy Grove)
- Fix Piglet `DUMP` applied to multisets and structs
- Multisets and `COLLECT` in Piglet
- \[ [CALCITE-785](https://issues.apache.org/jira/browse/CALCITE-785)\]
Add “Piglet”, a subset of Pig Latin on top of Calcite algebra
- \[ [CALCITE-869](https://issues.apache.org/jira/browse/CALCITE-869)\]
Add `VALUES` command to Piglet
- \[ [CALCITE-868](https://issues.apache.org/jira/browse/CALCITE-868)\]
Add API to execute queries expressed as `RelNode`
- In RelBuilder, build expressions by table alias

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-5-0 "Permalink")

- \[ [CALCITE-948](https://issues.apache.org/jira/browse/CALCITE-948)\]
Indicator columns not preserved by `RelFieldTrimmer`
- Fix Windows issues (line endings and checkstyle suppressions)
- \[ [CALCITE-937](https://issues.apache.org/jira/browse/CALCITE-937)\]
User-defined function within view
- \[ [CALCITE-926](https://issues.apache.org/jira/browse/CALCITE-926)\]
Rules fail to match because of missing link to parent equivalence set
(Maryann Xue)
- \[ [CALCITE-908](https://issues.apache.org/jira/browse/CALCITE-908)\]
Bump protobuf to 3.0.0-beta-1, fix deprecations and update docs (Josh Elser)
- \[ [CALCITE-932](https://issues.apache.org/jira/browse/CALCITE-932)\]
Fix muddled columns when `RelFieldTrimmer` is applied to `Aggregate`
- \[ [CALCITE-930](https://issues.apache.org/jira/browse/CALCITE-930)\]
Now Calcite is a top-level project, remove references to “incubating”
- \[ [CALCITE-929](https://issues.apache.org/jira/browse/CALCITE-929)\]
Calls to `AbstractRelNode` may result in NPE
- \[ [CALCITE-923](https://issues.apache.org/jira/browse/CALCITE-923)\]
Type mismatch when converting `LEFT JOIN` to `INNER`
- \[ [CALCITE-666](https://issues.apache.org/jira/browse/CALCITE-666)\]
Anti-semi-joins against JDBC adapter give wrong results (Yeong Wei)
- \[ [CALCITE-918](https://issues.apache.org/jira/browse/CALCITE-918)\]
`createProject` in `RelOptUtil` should uniquify field names
- \[ [CALCITE-792](https://issues.apache.org/jira/browse/CALCITE-792)\]
Obsolete `RelNode.isKey` and `isDistinct` methods
- Allow FlatLists of different length to be compared
- \[ [CALCITE-898](https://issues.apache.org/jira/browse/CALCITE-898)\]
Type of ‘Java \\* \`INTEGER\`' should be \`BIGINT\`
- \[ [CALCITE-894](https://issues.apache.org/jira/browse/CALCITE-894)\]
Do not generate redundant column alias for the left relation when
translating `IN` sub-query (Maryann Xue)
- \[ [CALCITE-897](https://issues.apache.org/jira/browse/CALCITE-897)\]
Enable debugging using “-Dcalcite.debug”
- \[ [CALCITE-885](https://issues.apache.org/jira/browse/CALCITE-885)\]
Add Oracle test environment
- \[ [CALCITE-888](https://issues.apache.org/jira/browse/CALCITE-888)\]
Overlay window loses `PARTITION BY` list (Hsuan-Yi Chu)
- \[ [CALCITE-886](https://issues.apache.org/jira/browse/CALCITE-886)\]
System functions in `GROUP BY` clause
- \[ [CALCITE-860](https://issues.apache.org/jira/browse/CALCITE-860)\]
Correct LICENSE file for generated web site
- \[ [CALCITE-882](https://issues.apache.org/jira/browse/CALCITE-882)\]
Allow web site to be deployed not as the root directory of the web server
(Josh Elser)
- Upgrade parent POM to apache-17
- \[ [CALCITE-687](https://issues.apache.org/jira/browse/CALCITE-687)\]
Synchronize HSQLDB at a coarse level using a Lock (Josh Elser)
- \[ [CALCITE-870](https://issues.apache.org/jira/browse/CALCITE-870)\]
Remove copyright content from archers.json
- Replace `Stack` with `ArrayDeque`
- \[ [CALCITE-874](https://issues.apache.org/jira/browse/CALCITE-874)\]
`ReflectiveRelMetadataProvider` is not thread-safe
- Add `LogicalWindow.create()`
- Add `ImmutableBitSet.get(int, int)`
- \[ [CALCITE-865](https://issues.apache.org/jira/browse/CALCITE-865)\]
Unknown table type causes `NullPointerException` in `JdbcSchema`
  - Add table types used by Oracle and DB2
- \[ [CALCITE-862](https://issues.apache.org/jira/browse/CALCITE-862)\]
`JdbcSchema` gives `NullPointerException` on non-standard column type (Marc
Prud’hommeaux)
- \[ [CALCITE-847](https://issues.apache.org/jira/browse/CALCITE-847)\]
`AVG` window function in `GROUP BY` gives `AssertionError` (Hsuan-Yi Chu)
- \[ [CALCITE-827](https://issues.apache.org/jira/browse/CALCITE-827)\]
Calcite incorrectly permutes columns of `OVER` query (Hsuan-Yi Chu)
- \[ [CALCITE-809](https://issues.apache.org/jira/browse/CALCITE-809)\]
`TableScan` does not support large/infinite scans (Jesse Yates)
- Lazily create exception only when it needs to be thrown (Marc Prud’hommeaux)
- \[ [CALCITE-812](https://issues.apache.org/jira/browse/CALCITE-812)\]
Make JSON reader and writer use properly quoted key names (Marc
Prud’hommeaux)
- \[ [CALCITE-820](https://issues.apache.org/jira/browse/CALCITE-820)\]
Validate that window functions have `OVER` clause (Hsuan-Yi Chu)
- \[ [CALCITE-824](https://issues.apache.org/jira/browse/CALCITE-824)\]
Type inference when converting `IN` clause to semijoin (Josh Wills)

## [1.4.0-incubating](https://github.com/apache/calcite/releases/tag/calcite-1.4.0-incubating) / 2015-09-02 [Permalink](https://calcite.apache.org/docs/history.html\#v1-4-0 "Permalink")

In addition to a large number of bug-fixes and minor enhancements,
this release includes improvements to lattices and materialized views,
and adds a builder API so that you can easily create relational
algebra expressions.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-4-0 "Permalink")

- \[ [CALCITE-748](https://issues.apache.org/jira/browse/CALCITE-748)\]
Add `RelBuilder`, builder for expressions in relational algebra
- \[ [CALCITE-758](https://issues.apache.org/jira/browse/CALCITE-758)\]
Use more than one lattice in the same query (Rajat Venkatesh)
- \[ [CALCITE-761](https://issues.apache.org/jira/browse/CALCITE-761)\]
Pre-populated materializations (Maryann Xue)
- \[ [CALCITE-786](https://issues.apache.org/jira/browse/CALCITE-786)\]
Detect if materialized view can be used to rewrite a query in
non-trivial cases (Amogh Margoor)
- \[ [CALCITE-732](https://issues.apache.org/jira/browse/CALCITE-732)\]
Implement multiple distinct-`COUNT` using `GROUPING SETS`
- Add various `BitSet` and `ImmutableBitSet` utilities

#### Web site updates [Permalink](https://calcite.apache.org/docs/history.html\#site-1-4-0 "Permalink")

- \[ [CALCITE-810](https://issues.apache.org/jira/browse/CALCITE-810)\]
Add committers’ organizations to the web site
- Add news item (XLDB best lighting talk), and some talks
- Fix javadoc links
- Add license notice for web site
- Wrap file header in HTML comments
- How to release
- Move disclaimer out of every page’s footer and into home page and downloads
page
- For web site files, add license headers where possible, apache-rat
exclusions otherwise
- Calcite DOAP
- \[ [CALCITE-355](https://issues.apache.org/jira/browse/CALCITE-355)\]
Web site

#### Bug-fixes, API changes and minor enhancements [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-4-0 "Permalink")

- \[ [CALCITE-741](https://issues.apache.org/jira/browse/CALCITE-741)\]
Ensure that the source release’s `DEPENDENCIES` file includes all module
dependencies
- \[ [CALCITE-743](https://issues.apache.org/jira/browse/CALCITE-743)\]
Ensure only a single source assembly is executed
- \[ [CALCITE-850](https://issues.apache.org/jira/browse/CALCITE-850)\]
Remove push down expressions from `FilterJoinRule` and create a new rule
for it
- \[ [CALCITE-834](https://issues.apache.org/jira/browse/CALCITE-834)\]
`StackOverflowError` getting predicates from the metadata provider
- \[ [CALCITE-833](https://issues.apache.org/jira/browse/CALCITE-833)\]
`RelOptUtil.splitJoinCondition` incorrectly splits a join condition
(Hsuan-Yi Chu)
- \[ [CALCITE-822](https://issues.apache.org/jira/browse/CALCITE-822)\]
Add a unit test case to test collation of `LogicalAggregate`
- \[ [CALCITE-822](https://issues.apache.org/jira/browse/CALCITE-822)\]
Revert incorrect `LogicalAggregate` collation inferring logic made in
\[ [CALCITE-783](https://issues.apache.org/jira/browse/CALCITE-783)\]
(Milinda Pathirage)
- \[ [CALCITE-826](https://issues.apache.org/jira/browse/CALCITE-826)\]
Use `ProjectFactory` in `AggregateJoinTranposeRule` and `FilterJoinRule`
- \[ [CALCITE-821](https://issues.apache.org/jira/browse/CALCITE-821)\]
`Frameworks` gives NPE when `FrameworkConfig` has no default schema
- \[ [CALCITE-811](https://issues.apache.org/jira/browse/CALCITE-811)\]
Extend `JoinProjectTransposeRule` with option to support outer joins
- \[ [CALCITE-805](https://issues.apache.org/jira/browse/CALCITE-805)\]
Add support for using an alternative grammar specification for left and
right curly braces. Additionally, add support for including addition token
manager declarations
- \[ [CALCITE-803](https://issues.apache.org/jira/browse/CALCITE-803)\]
Add `MYSQL_ANSI` Lexing policy
- \[ [CALCITE-717](https://issues.apache.org/jira/browse/CALCITE-717)\]
Compare BINARY and VARBINARY on unsigned byte values (Low Chin Wei)
- \[ [CALCITE-814](https://issues.apache.org/jira/browse/CALCITE-814)\]
`RexBuilder` reverses precision and scale of `DECIMAL` literal
- \[ [CALCITE-813](https://issues.apache.org/jira/browse/CALCITE-813)\]
Upgrade `updateCount`, `maxRows` from int to long
- \[ [CALCITE-714](https://issues.apache.org/jira/browse/CALCITE-714)\]
When de-correlating, push join condition into sub-query
- \[ [CALCITE-751](https://issues.apache.org/jira/browse/CALCITE-751)\]
Push aggregate with aggregate functions through join
- Add `RelBuilder.avg`
- \[ [CALCITE-806](https://issues.apache.org/jira/browse/CALCITE-806)\]
`ROW_NUMBER` should emit distinct values
- Document JSON model, making javadoc consistent with the model reference
- \[ [CALCITE-808](https://issues.apache.org/jira/browse/CALCITE-808)\]
Optimize `ProjectMergeRule`
- \[ [CALCITE-791](https://issues.apache.org/jira/browse/CALCITE-791)\]
Optimize `RelOptUtil.pushFilterPastProject`
- \[ [CALCITE-783](https://issues.apache.org/jira/browse/CALCITE-783)\]
Infer collation of `Project` using monotonicity (Milinda Pathirage)
- Change the argument types of `SqlOperator.getMonotonicity` to allow it to be
used for `RexNode` as well as `SqlNode`
- \[ [CALCITE-800](https://issues.apache.org/jira/browse/CALCITE-800)\]
Window function defined within another window function should be invalid
(Hsuan-Yi Chu)
- \[ [CALCITE-787](https://issues.apache.org/jira/browse/CALCITE-787)\]
Star table wrongly assigned to materialized view (Amogh Margoor)
- Remove duplicate resources from XML test reference files
- \[ [CALCITE-795](https://issues.apache.org/jira/browse/CALCITE-795)\]
Loss of precision when sending a decimal number via the remote JSON
service (Lukáš Lalinský)
- \[ [CALCITE-774](https://issues.apache.org/jira/browse/CALCITE-774)\]
When `GROUP BY` is present, ensure that window function operands only
refer to grouping keys (Hsuan-Yi Chu)
- \[ [CALCITE-799](https://issues.apache.org/jira/browse/CALCITE-799)\]
Incorrect result for `HAVING count(*) > 1`
- \[ [CALCITE-801](https://issues.apache.org/jira/browse/CALCITE-801)\]
`NullPointerException` using `USING` on table alias with column aliases
- \[ [CALCITE-390](https://issues.apache.org/jira/browse/CALCITE-390)\]
Infer predicates for semi-join
- \[ [CALCITE-789](https://issues.apache.org/jira/browse/CALCITE-789)\]
`MetaImpl.MetaCatalog` should expose `TABLE_CAT` instead of
`TABLE_CATALOG`
- \[ [CALCITE-752](https://issues.apache.org/jira/browse/CALCITE-752)\]
Add back sqlline as a dependency to csv example
- \[ [CALCITE-780](https://issues.apache.org/jira/browse/CALCITE-780)\]
HTTP error 413 when sending a long string to the Avatica server
- In `RelBuilder`, calling `sort` then `limit` has same effect as calling
`sortLimit`
- Add `Ord.reverse`
- \[ [CALCITE-788](https://issues.apache.org/jira/browse/CALCITE-788)\]
Allow `EnumerableJoin` to be sub-classed (Li Yang)
- \[ [CALCITE-280](https://issues.apache.org/jira/browse/CALCITE-280)\]
`BigDecimal` underflow (Li Yang)
- \[ [CALCITE-763](https://issues.apache.org/jira/browse/CALCITE-763)\]
Missing translation from `Sort` to `MutableSort` (Maryann Xue)
- \[ [CALCITE-770](https://issues.apache.org/jira/browse/CALCITE-770)\]
Ignore window aggregates and ranking functions when finding aggregate
functions
- \[ [CALCITE-765](https://issues.apache.org/jira/browse/CALCITE-765)\]
Set `Content-Type` from the RPC server to `application/json` (Lukáš Lalinský)
- Fix Windows line-endings in `RelBuilderTest`
- \[ [CALCITE-727](https://issues.apache.org/jira/browse/CALCITE-727)\]
Constant folding involving `CASE` and `NULL`
- Related to
\[ [CALCITE-758](https://issues.apache.org/jira/browse/CALCITE-758)\],
speed up matching by not considering tiles separately from other
materialized views
- Test case and workaround for
\[ [CALCITE-760](https://issues.apache.org/jira/browse/CALCITE-760)\]
`Aggregate` recommender blows up if row count estimate is too high
- \[ [CALCITE-753](https://issues.apache.org/jira/browse/CALCITE-753)\]
`Aggregate` operators may derive row types with duplicate column names
- \[ [CALCITE-457](https://issues.apache.org/jira/browse/CALCITE-457)\]
Push condition of non-ansi join into join operator
- Change jsonRequest encoding to UTF-8 (Guitao Ding)
- \[ [CALCITE-757](https://issues.apache.org/jira/browse/CALCITE-757)\]
Fix expansion of view of another view (Venki Korukanti)
- Fix coverity warnings
- Remove deprecated `SqlTypeName` methods
- \[ [CALCITE-754](https://issues.apache.org/jira/browse/CALCITE-754)\]
Validator error when resolving `OVER` clause of `JOIN` query
- \[ [CALCITE-429](https://issues.apache.org/jira/browse/CALCITE-429)\]
Cardinality provider for use by lattice algorithm
- \[ [CALCITE-740](https://issues.apache.org/jira/browse/CALCITE-740)\]
Redundant `WHERE` clause causes wrong result in MongoDB adapter
- \[ [CALCITE-665](https://issues.apache.org/jira/browse/CALCITE-665)\]
`ClassCastException` in MongoDB adapter
- Separate `TableFactory` from suggested table name, so one `TableFactory` can be
used for several tables
- \[ [CALCITE-749](https://issues.apache.org/jira/browse/CALCITE-749)\]
Add `MaterializationService.TableFactory` (Rajat Venkatesh)
- \[ [CALCITE-718](https://issues.apache.org/jira/browse/CALCITE-718)\]
Enable fetch to work for `Statement.execute()` for Avatica (Xavier Leong)
- \[ [CALCITE-712](https://issues.apache.org/jira/browse/CALCITE-712)\]
Obey `setMaxRows` for statement execute (Xavier Leong)
- Add `LoggingLocalJsonService`, to make it easier to test that JDBC requests
cause the right RPCs
- \[ [CALCITE-708](https://issues.apache.org/jira/browse/CALCITE-708)\]
Implement `DatabaseMetaData.getTypeInfo` (Xavier Leong)
- Enable Travis CI on new-master branch and bug-fix branches named
“NNN-description”
- Clean up
- Upgrade tpcds
- Make `JdbcTest.testVersion` more permissive, so that `version.major` and
`version.minor` can be set just before a release, rather than just after as at
present

## [1.3.0-incubating](https://github.com/apache/calcite/releases/tag/calcite-1.3.0-incubating) / 2015-05-30 [Permalink](https://calcite.apache.org/docs/history.html\#v1-3-0 "Permalink")

Mainly bug-fixes, but this release adds support for
[modifiable views](https://issues.apache.org/jira/browse/CALCITE-505)
and
[filtered aggregate functions](https://issues.apache.org/jira/browse/CALCITE-704)
and various improvements to Avatica.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-3-0 "Permalink")

- \[ [CALCITE-505](https://issues.apache.org/jira/browse/CALCITE-505)\]
Support modifiable view
- \[ [CALCITE-704](https://issues.apache.org/jira/browse/CALCITE-704)\]
`FILTER` clause for aggregate functions
- \[ [CALCITE-522](https://issues.apache.org/jira/browse/CALCITE-522)\]
In remote JDBC driver, transmit static database properties as a map
- \[ [CALCITE-661](https://issues.apache.org/jira/browse/CALCITE-661)\]
Remote fetch in Calcite JDBC driver
- Support Date, Time, Timestamp parameters

#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-1-3-0 "Permalink")

- \[ [CALCITE-722](https://issues.apache.org/jira/browse/CALCITE-722)\]
Rename markdown files to lower-case
- \[ [CALCITE-697](https://issues.apache.org/jira/browse/CALCITE-697)\]
Obsolete class `RelOptQuery`
- \[ [CALCITE-693](https://issues.apache.org/jira/browse/CALCITE-693)\]
Allow clients to control creation of `RelOptCluster`
- \[ [CALCITE-691](https://issues.apache.org/jira/browse/CALCITE-691)\]
Allow projects to supply alternate SQL parser
- \[ [CALCITE-675](https://issues.apache.org/jira/browse/CALCITE-675)\]
Enable `AggregateProjectMergeRule` in standard rule set
- \[ [CALCITE-679](https://issues.apache.org/jira/browse/CALCITE-679)\]
Factory method for `SemiJoin`
- \[ [CALCITE-674](https://issues.apache.org/jira/browse/CALCITE-674)\]
Add a `SWAP_OUTER` static instance to `JoinCommuteRule` (Maryann Xue)
- \[ [CALCITE-735](https://issues.apache.org/jira/browse/CALCITE-735)\]
`Primitive.DOUBLE.min` should be large and negative

#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-3-0 "Permalink")

- \[ [CALCITE-688](https://issues.apache.org/jira/browse/CALCITE-688)\]
`splitCondition` does not behave correctly when one side of the condition
references columns from different inputs
- \[ [CALCITE-259](https://issues.apache.org/jira/browse/CALCITE-259)\]
Using sub-queries in `CASE` statement against JDBC tables generates invalid
Oracle SQL (Yeong Wei)
- In sample code in README.md, rename optiq to calcite (Ethan)
- \[ [CALCITE-720](https://issues.apache.org/jira/browse/CALCITE-720)\]
`VolcanoPlanner.ambitious` comment doc is inconsistent (Santiago M. Mola)
- \[ [CALCITE-729](https://issues.apache.org/jira/browse/CALCITE-729)\]
`IndexOutOfBoundsException` in `ROLLUP` query on JDBC data source
- \[ [CALCITE-733](https://issues.apache.org/jira/browse/CALCITE-733)\]
Multiple distinct-`COUNT` query gives wrong results
- \[ [CALCITE-730](https://issues.apache.org/jira/browse/CALCITE-730)\]
`ClassCastException` in table from `CloneSchema`
- \[ [CALCITE-728](https://issues.apache.org/jira/browse/CALCITE-728)\]
Test suite hangs on Windows
- \[ [CALCITE-723](https://issues.apache.org/jira/browse/CALCITE-723)\]
Document lattices
- \[ [CALCITE-515](https://issues.apache.org/jira/browse/CALCITE-515)\]
Add Apache headers to markdown files
- Upgrade quidem
- \[ [CALCITE-716](https://issues.apache.org/jira/browse/CALCITE-716)\]
Scalar sub-query and aggregate function in `SELECT` or `HAVING` clause gives
`AssertionError`
- \[ [CALCITE-694](https://issues.apache.org/jira/browse/CALCITE-694)\]
Scan `HAVING` clause for sub-queries and `IN`-lists (Hsuan-Yi Chu)
- Upgrade hydromatic-resource-maven-plugin
- \[ [CALCITE-710](https://issues.apache.org/jira/browse/CALCITE-710)\]
Identical conditions in the `WHERE` clause cause `AssertionError` (Sean
Hsuan-Yi Chu)
- \[ [CALCITE-695](https://issues.apache.org/jira/browse/CALCITE-695)\]
Do not add `SINGLE_VALUE` aggregate function to a sub-query that will never
return more than one row (Hsuan-Yi Chu)
- Add tests for scalar sub-queries, including test cases for
\[ [CALCITE-709](https://issues.apache.org/jira/browse/CALCITE-709)\]
Errors with `LIMIT` inside scalar sub-query
- \[ [CALCITE-702](https://issues.apache.org/jira/browse/CALCITE-702)\]
Add validator test for monotonic expressions
- \[ [CALCITE-699](https://issues.apache.org/jira/browse/CALCITE-699)\]
In Avatica, synchronize access to Calendar
- \[ [CALCITE-700](https://issues.apache.org/jira/browse/CALCITE-700)\]
Pass time zone into tests
- \[ [CALCITE-698](https://issues.apache.org/jira/browse/CALCITE-698)\]
For `GROUP BY ()`, `areColumnsUnique()` should return true for any key
- Disable tests that fail under JDK 1.7 due to
\[ [CALCITE-687](https://issues.apache.org/jira/browse/CALCITE-687)\]
- Add “getting started” to HOWTO
- \[ [CALCITE-692](https://issues.apache.org/jira/browse/CALCITE-692)\]
Add back sqlline as a dependency
- \[ [CALCITE-677](https://issues.apache.org/jira/browse/CALCITE-677)\]
`RemoteDriverTest.testTypeHandling` fails east of Greenwich
- Disable test for
\[ [CALCITE-687](https://issues.apache.org/jira/browse/CALCITE-687)\]
Make `RemoteDriverTest.testStatementLifecycle` thread-safe
- \[ [CALCITE-686](https://issues.apache.org/jira/browse/CALCITE-686)\]
`SqlNode.unparse` produces invalid SQL
- \[ [CALCITE-507](https://issues.apache.org/jira/browse/CALCITE-507)\]
Update HOWTO.md with running integration tests
- Add H2 integration test
- Add Postgres integration test
- \[ [CALCITE-590](https://issues.apache.org/jira/browse/CALCITE-590)\]
Update MongoDB test suite to calcite-test-dataset
- Add `CalciteAssert.assertArrayEqual` for more user-friendly asserts
- \[ [CALCITE-585](https://issues.apache.org/jira/browse/CALCITE-585)\]
Avatica JDBC methods should throw `SQLFeatureNotSupportedException` (Ng Jiunn
Jye)
- \[ [CALCITE-671](https://issues.apache.org/jira/browse/CALCITE-671)\]
`ByteString` does not deserialize properly as a `FetchRequest` parameter value
- \[ [CALCITE-676](https://issues.apache.org/jira/browse/CALCITE-676)\]
`AssertionError` in `GROUPING SETS` query
- \[ [CALCITE-678](https://issues.apache.org/jira/browse/CALCITE-678)\]
`SemiJoinRule` mixes up fields when `Aggregate.groupSet` is not field #0

## [1.2.0-incubating](https://github.com/apache/calcite/releases/tag/calcite-1.2.0-incubating) / 2015-04-07 [Permalink](https://calcite.apache.org/docs/history.html\#v1-2-0 "Permalink")

A short release, less than a month after 1.1.

There have been many changes to Avatica, hugely improving its coverage of the
JDBC API and overall robustness. A new provider, `JdbcMeta`, allows
you to remote an existing JDBC driver.

\[ [CALCITE-606](https://issues.apache.org/jira/browse/CALCITE-606)\]
improves how the planner propagates traits such as collation and
distribution among relational expressions.

\[ [CALCITE-613](https://issues.apache.org/jira/browse/CALCITE-613)\]
and \[ [CALCITE-307](https://issues.apache.org/jira/browse/CALCITE-307)\]
improve implicit and explicit conversions in SQL.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-2-0 "Permalink")

- \[ [CALCITE-366](https://issues.apache.org/jira/browse/CALCITE-366)\]
Support Aggregate push down in bushy joins (Jesus Camacho Rodriguez)
- \[ [CALCITE-613](https://issues.apache.org/jira/browse/CALCITE-613)\]
Implicitly convert character values in comparisons
- \[ [CALCITE-307](https://issues.apache.org/jira/browse/CALCITE-307)\]
Implement `CAST` between date-time types
- \[ [CALCITE-634](https://issues.apache.org/jira/browse/CALCITE-634)\]
Allow `ORDER BY` aggregate function in `SELECT DISTINCT`, provided that it
occurs in `SELECT` clause (Sean Hsuan-Yi Chu)
- In linq4j, implement `firstOrDefault`, `single`, and `singleOrDefault` methods
(Daniel Cooper)
- JDBC adapter
  - \[ [CALCITE-631](https://issues.apache.org/jira/browse/CALCITE-631)\]
    Push theta joins down to JDBC adapter (Ng Jiunn Jye)
  - \[ [CALCITE-657](https://issues.apache.org/jira/browse/CALCITE-657)\]
    `NullPointerException` when executing `JdbcAggregate.implement`
    method (Yuri Au Yong)
- Metadata
  - \[ [CALCITE-659](https://issues.apache.org/jira/browse/CALCITE-659)\]
    Missing types in `averageTypeValueSize` method in `RelMdSize`
    (Jesus Camacho Rodriguez)
  - \[ [CALCITE-650](https://issues.apache.org/jira/browse/CALCITE-650)\]
    Add metadata for average size of a tuple in `SemiJoin` (Jesus
    Camacho Rodriguez)
  - \[ [CALCITE-649](https://issues.apache.org/jira/browse/CALCITE-649)\]
    Extend `splitCondition` method in `RelOptUtil` to handle multiple
    joins on the same key (Jesus Camacho Rodriguez)

#### Avatica features and bug-fixes [Permalink](https://calcite.apache.org/docs/history.html\#avatica-1-2-0 "Permalink")

- \[ [CALCITE-670](https://issues.apache.org/jira/browse/CALCITE-670)\]
`AvaticaPreparedStatement` should support `execute()` and
`executeUpdate()` (Nick Dimiduk)
- \[ [CALCITE-641](https://issues.apache.org/jira/browse/CALCITE-641)\]
Implement logging throughout Avatica server (Nick Dimiduk)
- \[ [CALCITE-646](https://issues.apache.org/jira/browse/CALCITE-646)\]
`AvaticaStatement.execute` method broken over remote JDBC (Yeong Wei
and Julian Hyde)
- \[ [CALCITE-660](https://issues.apache.org/jira/browse/CALCITE-660)\]
Improve Avatica date support
- \[ [CALCITE-655](https://issues.apache.org/jira/browse/CALCITE-655)\]
Implement `ConnectionSync` RPC (Nick Dimiduk)
- \[ [CALCITE-654](https://issues.apache.org/jira/browse/CALCITE-654)\]
Tighten up `AvaticaStatement.execute` semantics (Nick Dimiduk)
- \[ [CALCITE-658](https://issues.apache.org/jira/browse/CALCITE-658)\]
Cleanup dependency usage (Nick Dimiduk)
- \[ [CALCITE-652](https://issues.apache.org/jira/browse/CALCITE-652)\]
Move server pieces of `avatica` into `avatica-server` (Nick Dimiduk)
- \[ [CALCITE-651](https://issues.apache.org/jira/browse/CALCITE-651)\]
In `JdbcMeta`, convert property definitions to an enum (Nick Dimiduk)
- \[ [CALCITE-640](https://issues.apache.org/jira/browse/CALCITE-640)\]
Avatica server should expire stale connections/statements (Nick Dimiduk)
- \[ [CALCITE-639](https://issues.apache.org/jira/browse/CALCITE-639)\]
Open up permissions on avatica server components (Nick Dimiduk)
- \[ [CALCITE-637](https://issues.apache.org/jira/browse/CALCITE-637)\]
Implement Avatica `CloseConnection` RPC (Nick Dimiduk)
- \[ [CALCITE-636](https://issues.apache.org/jira/browse/CALCITE-636)\]
Connection isolation for Avatica clients (Nick Dimiduk)
- \[ [CALCITE-626](https://issues.apache.org/jira/browse/CALCITE-626)\]
Implement `CloseStatement` RPC (Nick Dimiduk)
- \[ [CALCITE-630](https://issues.apache.org/jira/browse/CALCITE-630)\]
Flesh out `AvaticaParameter.setObject` (Nick Dimiduk)
- \[ [CALCITE-627](https://issues.apache.org/jira/browse/CALCITE-627)\]
Add Avatica support for `getTableTypes`, `getColumns` (Xavier FH Leong)
- \[ [CALCITE-618](https://issues.apache.org/jira/browse/CALCITE-618)\]
Add Avatica support for `getTables` (Julian Hyde and Nick Dimiduk)

#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-1-2-0 "Permalink")

- \[ [CALCITE-617](https://issues.apache.org/jira/browse/CALCITE-617)\]
Check at initialization time in `CachingInvocationHandler` that MD provider
is not null (Jesus Camacho Rodriguez)
- \[ [CALCITE-638](https://issues.apache.org/jira/browse/CALCITE-638)\]
SQL standard `REAL` is 4 bytes, `FLOAT` is 8 bytes

#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-2-0 "Permalink")

- \[ [CALCITE-672](https://issues.apache.org/jira/browse/CALCITE-672)\]
SQL `ANY` type should be nullable (Jinfeng Ni)
- Disable tests, pending
\[ [CALCITE-673](https://issues.apache.org/jira/browse/CALCITE-673)\]
Timeout executing joins against MySQL
- Fix traits in MongoDB adapter, and `NullPointerException` in `JdbcTest`
- \[ [CALCITE-662](https://issues.apache.org/jira/browse/CALCITE-662)\]
Query validation fails when an `ORDER BY` clause is used with `WITH CLAUSE`
- \[ [CALCITE-606](https://issues.apache.org/jira/browse/CALCITE-606)\]
Fix trait propagation and add test case
- Remove checkstyle Eclipse properties from git tracking
- \[ [CALCITE-644](https://issues.apache.org/jira/browse/CALCITE-644)\]
Increase check style line limit to 100 chars (Nick Dimiduk)
- \[ [CALCITE-648](https://issues.apache.org/jira/browse/CALCITE-648)\]
Update `ProjectMergeRule` description for new naming convention (Jinfeng Ni)
- \[ [CALCITE-625](https://issues.apache.org/jira/browse/CALCITE-625)\]
`README.md` linking to the wrong page of `optiq-csv` (hongbin ma)
- \[ [CALCITE-632](https://issues.apache.org/jira/browse/CALCITE-632)\]
Sort order returned by `SUPERCLASS_COMPARATOR` in
`ReflectiveRelMetadataProvider` is inconsistent (Jesus Camacho
Rodriguez)
- \[ [CALCITE-335](https://issues.apache.org/jira/browse/CALCITE-335)\]
Remove uses of linq4j `Functions.adapt`
- \[ [CALCITE-592](https://issues.apache.org/jira/browse/CALCITE-592)\]
Upgrade to Guava 14.0.1
- \[ [CALCITE-596](https://issues.apache.org/jira/browse/CALCITE-596)\]
JDBC adapter incorrectly reads null values as 0 (Ng Jiunn Jye)
- \[ [CALCITE-633](https://issues.apache.org/jira/browse/CALCITE-633)\]
`WITH ... ORDER BY` cannot find table
- \[ [CALCITE-614](https://issues.apache.org/jira/browse/CALCITE-614)\]
`IN` clause in `CASE` in `GROUP BY` gives `AssertionError`
- \[ [CALCITE-619](https://issues.apache.org/jira/browse/CALCITE-619)\]
Slim down dependencies in parent POM

## [1.1.0-incubating](https://github.com/apache/calcite/releases/tag/calcite-1.1.0-incubating) / 2015-03-13 [Permalink](https://calcite.apache.org/docs/history.html\#v1-1-0 "Permalink")

This Calcite release makes it possible to exploit physical properties
of relational expressions to produce more efficient plans, introducing
collation and distribution as traits, `Exchange` relational operator,
and several new forms of metadata.

We add experimental support for streaming SQL.

This release drops support for JDK 1.6; Calcite now requires 1.7 or
later.

We have introduced static `create` methods for many sub-classes of
`RelNode`. We strongly suggest that you use these rather than
calling constructors directly.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-1-0 "Permalink")

- SQL
  - \[ [CALCITE-602](https://issues.apache.org/jira/browse/CALCITE-602)\]
    Streaming queries (experimental)
  - \[ [CALCITE-588](https://issues.apache.org/jira/browse/CALCITE-588)\]
    Allow `TableMacro` to consume maps and collections
  - \[ [CALCITE-583](https://issues.apache.org/jira/browse/CALCITE-583)\]
    Operator `||` mishandles `ANY` type (Sean Hsuan-Yi Chu)
- Planner rule improvements
  - \[ [CALCITE-445](https://issues.apache.org/jira/browse/CALCITE-445)\]
    Pull up filters rejected by a `ProjectableFilterableTable`
  - \[ [CALCITE-600](https://issues.apache.org/jira/browse/CALCITE-600)\]
    Use `SetOpFactory` in rules containing `Union` operator (Jesus
    Camacho Rodriguez)
  - \[ [CALCITE-603](https://issues.apache.org/jira/browse/CALCITE-603)\]
    Metadata providers for size, memory, parallelism

    - \[ [CALCITE-607](https://issues.apache.org/jira/browse/CALCITE-607)\]
      Change visibility of constructor in metadata providers for size,
      memory, parallelism (Jesus Camacho Rodriguez)
    - \[ [CALCITE-608](https://issues.apache.org/jira/browse/CALCITE-608)\]
      Exception is thrown when `RelMdDistribution` for `Project`
      operator is called (Jesus Camacho Rodriguez)
- Collation and distribution as traits
  - \[ [CALCITE-88](https://issues.apache.org/jira/browse/CALCITE-88)\]
    Add collation as a trait and a kind of `RelNode` metadata
  - \[ [CALCITE-569](https://issues.apache.org/jira/browse/CALCITE-569)\]
    `ArrayIndexOutOfBoundsException` when deducing collation (Aman Sinha)
  - \[ [CALCITE-581](https://issues.apache.org/jira/browse/CALCITE-581)\]
    Add `LogicalSort` relational expression, and make `Sort` abstract
  - \[ [CALCITE-526](https://issues.apache.org/jira/browse/CALCITE-526)\]
    Add `EnumerableMergeJoin`, which exploits sorted inputs
  - \[ [CALCITE-71](https://issues.apache.org/jira/browse/CALCITE-71)\]
    Provide a way to declare that tables are sorted
  - \[ [CALCITE-576](https://issues.apache.org/jira/browse/CALCITE-576)\]
    Make `RelCollation` trait and `AbstractRelNode.getCollationList` consistent
  - \[ [CALCITE-254](https://issues.apache.org/jira/browse/CALCITE-254)\]
    Propagate `RelCollation` on aliased columns in `JoinRule`
  - \[ [CALCITE-569](https://issues.apache.org/jira/browse/CALCITE-569)\]
    `ArrayIndexOutOfBoundsException` when deducing collation
  - \[ [CALCITE-594](https://issues.apache.org/jira/browse/CALCITE-594)\]
    Add `RelDistribution` trait and `Exchange` relational expression

#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-1-1-0 "Permalink")

- Many sub-classes of `RelNode` now have a static `create` method
which automatically sets up traits such as collation and
distribution. The constructors are not marked deprecated, but we
strongly suggest that you use the `create` method if it exists.
- \[ [CALCITE-591](https://issues.apache.org/jira/browse/CALCITE-591)\]
Drop support for Java 1.6 (and JDBC 4.0)
- \[ [CALCITE-587](https://issues.apache.org/jira/browse/CALCITE-587)\]
Upgrade `jetty-server` to 9.2.7.v20150116 and port avatica-server `HttpServer`
(Trevor Hartman)
- \[ [CALCITE-577](https://issues.apache.org/jira/browse/CALCITE-577)\]
Revert temporary API changes introduced in
\[ [CALCITE-575](https://issues.apache.org/jira/browse/CALCITE-575)\]
- Add means to create `Context` instances by wrapping objects and by chaining
contexts
- \[ [CALCITE-599](https://issues.apache.org/jira/browse/CALCITE-599)\]
`EquiJoin` in wrong package (Jesus Camacho Rodriguez)
- \[ [CALCITE-573](https://issues.apache.org/jira/browse/CALCITE-573)\]
Use user-given names in `RelOptUtil.createProject` and `createRename`
- \[ [CALCITE-572](https://issues.apache.org/jira/browse/CALCITE-572)\]
Remove `Project.flags` (methods are deprecated, to be removed before 2.0)

#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-1-0 "Permalink")

- Remove the `LICENSE` file of calcite-example-csv (the former
optiq-csv) and move its history into main history
- \[ [CALCITE-615](https://issues.apache.org/jira/browse/CALCITE-615)\]
AvaticaParameter should be Jackson serializable (Nick Dimiduk)
- \[ [CALCITE-612](https://issues.apache.org/jira/browse/CALCITE-612)\]
Update AvaticaStatement to handle cancelled queries (Parth Chandra)
- \[ [CALCITE-605](https://issues.apache.org/jira/browse/CALCITE-605)\]
Reduce dependency on third-party maven repositories
- \[ [CALCITE-611](https://issues.apache.org/jira/browse/CALCITE-611)\]
Method `setAggChildKeys` should take into account indicator columns of
`Aggregate` operator (Jesus Camacho Rodriguez)
- \[ [CALCITE-566](https://issues.apache.org/jira/browse/CALCITE-566)\]
`ReduceExpressionsRule` requires planner to have an `Executor`
- Refactor `TableScanNode.create` method
- \[ [CALCITE-593](https://issues.apache.org/jira/browse/CALCITE-593)\]
Validator in `Frameworks` should expand identifiers (Jinfeng Ni)
- Australian time-zones changed in `tzdata2014f`, Java 1.8.0\_31
- \[ [CALCITE-580](https://issues.apache.org/jira/browse/CALCITE-580)\]
Average aggregation on an `Integer` column throws `ClassCastException`
- In Travis, ask Surefire to print results to screen
- \[ [CALCITE-586](https://issues.apache.org/jira/browse/CALCITE-586)\]
Prevent JSON serialization of `Signature.internalParameters`

## [1.0.0-incubating](https://github.com/apache/calcite/releases/tag/calcite-1.0.0-incubating) / 2015-01-31 [Permalink](https://calcite.apache.org/docs/history.html\#v1-0-0 "Permalink")

Calcite’s first major release.

Since the previous release we have re-organized the into the `org.apache.calcite`
namespace. To make migration of your code easier, we have described the
[mapping from old to new class names](https://issues.apache.org/jira/secure/attachment/12681620/mapping.txt)
as an attachment to
\[ [CALCITE-296](https://issues.apache.org/jira/browse/CALCITE-296)\].

The release adds SQL support for `GROUPING SETS`, `EXTEND`, `UPSERT` and sequences;
a remote JDBC driver;
improvements to the planner engine and built-in planner rules;
improvements to the algorithms that implement the relational algebra,
including an interpreter that can evaluate queries without compilation;
and fixes about 30 bugs.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-1-0-0 "Permalink")

- SQL
  - \[ [CALCITE-494](https://issues.apache.org/jira/browse/CALCITE-494)\]
    Support `NEXT`/`CURRENT VALUE FOR` syntax for using sequences
  - \[ [CALCITE-492](https://issues.apache.org/jira/browse/CALCITE-492)\]
    Support `UPSERT` statement in parser
  - \[ [CALCITE-493](https://issues.apache.org/jira/browse/CALCITE-493)\]
    Add `EXTEND` clause, for defining columns and their types at query/DML time
  - \[ [CALCITE-497](https://issues.apache.org/jira/browse/CALCITE-497)\]
    Support optional qualifier for column name references
  - \[ [CALCITE-356](https://issues.apache.org/jira/browse/CALCITE-356)\]
    Allow column references of the form `schema.table.column`
  - \[ [CALCITE-462](https://issues.apache.org/jira/browse/CALCITE-462)\]
    Allow table functions in `LATERAL` expression
  - \[ [CALCITE-282](https://issues.apache.org/jira/browse/CALCITE-282)\]
    Add `{fn QUARTER(date)}` function (Benoy Antony)
  - Grouping sets
    - \[ [CALCITE-370](https://issues.apache.org/jira/browse/CALCITE-370)\]
      Support `GROUPING SETS`, `CUBE`, `ROLLUP` in SQL and algebra
    - \[ [CALCITE-512](https://issues.apache.org/jira/browse/CALCITE-512)\]
      Add `GROUP_ID`,`GROUPING_ID`, `GROUPING` functions
- Planner rule improvements
  - \[ [CALCITE-92](https://issues.apache.org/jira/browse/CALCITE-92)\]
    Optimize away `Project` that merely renames fields
  - Detect and merge duplicate predicates `AND(x, y, x)` to `AND(x, y)` in more
    circumstances
  - \[ [CALCITE-557](https://issues.apache.org/jira/browse/CALCITE-557)\]
    Speed up planning by never creating `AbstractConverter`
  - \[ [CALCITE-545](https://issues.apache.org/jira/browse/CALCITE-545)\]
    When a projected expression can only have one value, replace with that
    constant
  - Grouping sets
    - \[ [CALCITE-542](https://issues.apache.org/jira/browse/CALCITE-542)\]
      Support for `Aggregate` with grouping sets in `RelMdColumnOrigins` (Jesus
      Camacho Rodriguez)
    - \[ [CALCITE-533](https://issues.apache.org/jira/browse/CALCITE-533)\]
      Support for grouping sets in `FilterAggregateTransposeRule` (Jesus Camacho
      Rodriguez)
    - \[ [CALCITE-532](https://issues.apache.org/jira/browse/CALCITE-532)\]
      Support for grouping sets in `AggregateFilterTransposeRule` (Jesus Camacho
      Rodriguez)
    - \[ [CALCITE-513](https://issues.apache.org/jira/browse/CALCITE-513)\]
      Support for grouping sets in `AggregateProjectMergeRule` (Jesus Camacho
      Rodriguez)
    - \[ [CALCITE-510](https://issues.apache.org/jira/browse/CALCITE-510)\]
      Support for grouping sets in `AggregateExpandDistinctAggregatesRule` (Jesus
      Camacho Rodriguez)
    - \[ [CALCITE-502](https://issues.apache.org/jira/browse/CALCITE-502)\]
      Support for grouping sets in `AggregateUnionTransposeRule` (Jesus Camacho
      Rodriguez)
    - \[ [CALCITE-503](https://issues.apache.org/jira/browse/CALCITE-503)\]
      Tests to check rules on `Aggregate` operator without grouping sets (Jesus
      Camacho Rodriguez)
- Algorithms
  - \[ [CALCITE-451](https://issues.apache.org/jira/browse/CALCITE-451)\]
    Implement theta join, inner and outer, in enumerable convention
  - \[ [CALCITE-489](https://issues.apache.org/jira/browse/CALCITE-489)\]
    Update `Correlate` mechanics and implement `EnumerableCorrelate` (aka nested
    loops join)
  - \[ [CALCITE-544](https://issues.apache.org/jira/browse/CALCITE-544)\]
    Implement `Union` in interpreter
  - \[ [CALCITE-562](https://issues.apache.org/jira/browse/CALCITE-562)\]
    Implement inner `Join` in interpreter and improve handling of scalar expressions
  - \[ [CALCITE-543](https://issues.apache.org/jira/browse/CALCITE-543)\]
    Implement `Aggregate` (including `GROUPING SETS`) in interpreter (Jacques
    Nadeau)
  - In progress towards
    \[ [CALCITE-558](https://issues.apache.org/jira/browse/CALCITE-558)\]
    add `BINDABLE` convention (but `ENUMERABLE` is still the default), and add
    `ArrayBindable` and `Scalar` interfaces
- Remote driver
  - \[ [CALCITE-93](https://issues.apache.org/jira/browse/CALCITE-93)\]
    Calcite RPC server
  - \[ [CALCITE-94](https://issues.apache.org/jira/browse/CALCITE-94)\]
    Remote JDBC driver
  - Make `JsonHandler` and `JsonService` thread-safe

#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-1-0-0 "Permalink")

- The great code re-org
  - \[ [CALCITE-296](https://issues.apache.org/jira/browse/CALCITE-296)\]
    Re-organize package structure
  - \[ [CALCITE-419](https://issues.apache.org/jira/browse/CALCITE-419)\]
    Naming convention for planner rules
  - \[ [CALCITE-306](https://issues.apache.org/jira/browse/CALCITE-306)\]
    Standardize code style for “import package.\*;”
  - \[ [CALCITE-474](https://issues.apache.org/jira/browse/CALCITE-474)\]
    Clean up rule naming in order to support enabling/disabling rules
  - \[ [CALCITE-460](https://issues.apache.org/jira/browse/CALCITE-460)\]
    Add `ImmutableBitSet` and replace uses of `BitSet`
  - \[ [CALCITE-479](https://issues.apache.org/jira/browse/CALCITE-479)\]
    Migrate `RelNode.getChildExps` to `RelNode.accept(RexShuttle)`
  - \[ [CALCITE-527](https://issues.apache.org/jira/browse/CALCITE-527)\]
    Drop `rowType` field and constructor/copy argument of `Calc`
- Add linq4j and example-csv modules
  - Remove unused packages in linq4j, and fix checkstyle issues in linq4j and csv
  - Add calcite-linq4j and calcite-example-csv as POM sub-modules
  - Import ‘optiq-csv’ project as ‘example/csv/’, and add Apache headers
  - Import ‘linq4j’ project, and add Apache headers
  - \[ [CALCITE-478](https://issues.apache.org/jira/browse/CALCITE-478)\]
    Move CSV tutorial (Siva Narayanan)
- \[ [CALCITE-464](https://issues.apache.org/jira/browse/CALCITE-464)\]
Make parser accept configurable max length for SQL identifier
- \[ [CALCITE-465](https://issues.apache.org/jira/browse/CALCITE-465)\]
Remove `OneRow` and `Empty` relational expressions; `Values` will suffice

#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-1-0-0 "Permalink")

- Build improvements
  - \[ [CALCITE-541](https://issues.apache.org/jira/browse/CALCITE-541)\]
    Update maven-source-plugin to 2.4 to get speedup in jdk 1.8
  - \[ [CALCITE-537](https://issues.apache.org/jira/browse/CALCITE-537)\]
    Skip overwrite of `NOTICE`, `DEPENDENCIES`, and `LICENSE` files
  - \[ [CALCITE-538](https://issues.apache.org/jira/browse/CALCITE-538)\]
    Generate `Parser.jj` only at first build
  - \[ [CALCITE-539](https://issues.apache.org/jira/browse/CALCITE-539)\]
    Avoid rewrite of `org-apache-calcite-jdbc.properties`
  - \[ [CALCITE-540](https://issues.apache.org/jira/browse/CALCITE-540)\]
    Create git.properties file only at first build. This saves time in
    development at a cost of stale `git.properties`
  - \[ [CALCITE-536](https://issues.apache.org/jira/browse/CALCITE-536)\]
    Add `@PackageMarker` to `package-info.java` so maven-compiler skips
    compilation when the sources are unchanged
  - \[ [CALCITE-535](https://issues.apache.org/jira/browse/CALCITE-535)\]
    Support skip overwrite in hydromatic-resource
- \[ [CALCITE-582](https://issues.apache.org/jira/browse/CALCITE-582)\]
`EnumerableTableScan` broken when table has single column
- \[ [CALCITE-575](https://issues.apache.org/jira/browse/CALCITE-575)\]
Variant of `ProjectRemoveRule` that considers a project trivial only if its
field names are identical (John Pullokkaran)
- \[ [CALCITE-571](https://issues.apache.org/jira/browse/CALCITE-571)\]
`ReduceExpressionsRule` tries to reduce `SemiJoin` condition to non-equi
condition
- \[ [CALCITE-568](https://issues.apache.org/jira/browse/CALCITE-568)\]
Upgrade to a version of `pentaho-aggdesigner` that does not pull in
`servlet-api`
- \[ [CALCITE-567](https://issues.apache.org/jira/browse/CALCITE-567)\]
Make `quidem` dependency have scope “test”
- \[ [CALCITE-570](https://issues.apache.org/jira/browse/CALCITE-570)\]
`ReduceExpressionsRule` throws “duplicate key” exception
- \[ [CALCITE-561](https://issues.apache.org/jira/browse/CALCITE-561)\]
Upgrade parent POM
- \[ [CALCITE-458](https://issues.apache.org/jira/browse/CALCITE-458)\]
ArrayIndexOutOfBoundsException when using just a single column in interpreter
- Fix spurious extra row from `FULL JOIN`
- \[ [CALCITE-554](https://issues.apache.org/jira/browse/CALCITE-554)\]
Outer join over NULL keys generates wrong result
- \[ [CALCITE-489](https://issues.apache.org/jira/browse/CALCITE-489)\]
Teach `CalciteAssert` to respect multiple settings
- \[ [CALCITE-516](https://issues.apache.org/jira/browse/CALCITE-516)\]
`GROUP BY` on a `CASE` expression containing `IN` predicate fails (Aman Sinha)
- \[ [CALCITE-552](https://issues.apache.org/jira/browse/CALCITE-552)\]
Upgrade tpcds (which depends on an old version of guava)
- Copy identifier when fully-qualifying, so column aliases have the right case
- \[ [CALCITE-548](https://issues.apache.org/jira/browse/CALCITE-548)\]
Extend `induce` method to return `CUBE` and `ROLLUP` (Jesus Camacho Rodriguez)

  - Simplify `Group.induce` by assuming that group sets are sorted
- Test case for
\[ [CALCITE-212](https://issues.apache.org/jira/browse/CALCITE-212)\]
Join condition with `OR`
- \[ [CALCITE-550](https://issues.apache.org/jira/browse/CALCITE-550)\]
Case-insensitive matching of sub-query columns fails

  - Add more unit tests (Jinfeng Ni)
- \[ [CALCITE-448](https://issues.apache.org/jira/browse/CALCITE-448)\]
`FilterIntoJoinRule` creates filters containing invalid `RexInputRef`
- When registering a `RelNode`, be tolerant if it is equivalent to a `RelNode`
with different traits
- \[ [CALCITE-547](https://issues.apache.org/jira/browse/CALCITE-547)\]
Set nullability while inferring return type of `item(any,...)` operator
- In Travis CI, enable containers, and cache `.m2` directory
- \[ [CALCITE-534](https://issues.apache.org/jira/browse/CALCITE-534)\]
Missing implementation of `ResultSetMetaData.getColumnClassName` (Knut
Forkalsrud)
- \[ [CALCITE-506](https://issues.apache.org/jira/browse/CALCITE-506)\]
Update `EnumerableRelImplementor.stash` so it is suitable for all kinds of
classes
- Merge join algorithm for `Enumerable`s
- Efficient `Enumerable` over random-access list
- Add a test that calls all functions with arguments of all types that they
claim to accept
- \[ [CALCITE-511](https://issues.apache.org/jira/browse/CALCITE-511)\]
`copy` method in `LogicalAggregate` not copying the indicator value properly
- Add a model that has lattices and works against HSQLDB
- \[ [CALCITE-509](https://issues.apache.org/jira/browse/CALCITE-509)\]
`RelMdColumnUniqueness` uses `ImmutableBitSet.Builder` twice, gets
`NullPointerException`
- \[ [CALCITE-488](https://issues.apache.org/jira/browse/CALCITE-488)\]
`Enumerable<Holder>` does not work if where `Holder` is a custom class
with a single field; Calcite tries to treat it as `SCALAR` due to premature
`JavaRowFormat.optimize`
- \[ [CALCITE-352](https://issues.apache.org/jira/browse/CALCITE-352)\]
Throw exception if `ResultSet.next()` is called after `close()`
- \[ [CALCITE-403](https://issues.apache.org/jira/browse/CALCITE-403)\]
`Enumerable` gives `NullPointerException` with `NOT` on nullable expression
- \[ [CALCITE-469](https://issues.apache.org/jira/browse/CALCITE-469)\]
Update example/csv README.md instructions
- Document `WITH`, `LATERAL`, `GROUPING SETS`, `CUBE`, `ROLLUP`;
add descriptions for all built-in functions and operators
- \[ [CALCITE-470](https://issues.apache.org/jira/browse/CALCITE-470)\]
Print warning when column type hint is not understood;
Update `EMPS.deptno` column Integer → int
- Fix `Linq4j.product`; the cartesian product of 0 attributes is one row of 0
attributes
- Update link optiq-mat-plugin → mat-calcite-plugin
- \[ [CALCITE-467](https://issues.apache.org/jira/browse/CALCITE-467)\]
Incorrect namespace in `package-info.java`
- Add headers, to appease the RAT
- \[ [CALCITE-446](https://issues.apache.org/jira/browse/CALCITE-446)\]
CSV adapter should read from directory relative to the model file
- Add examples of scannable and filterable tables, matching
\[ [CALCITE-436](https://issues.apache.org/jira/browse/CALCITE-436)\]
Simpler SPI to query Table
- Fix `JdbcTest.testVersion` now that version is 1.0
- Update release HOWTO

## [0.9.2-incubating](https://github.com/apache/calcite/releases/tag/calcite-0.9.2-incubating) / 2014-11-05 [Permalink](https://calcite.apache.org/docs/history.html\#v0-9-2 "Permalink")

A fairly minor release, and last release before we rename all of the
packages and lots of classes, in what we expect to call 1.0. If you
have an existing application, it’s worth upgrading to this first,
before you move on to 1.0.

#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-9-2 "Permalink")

- \[ [CALCITE-436](https://issues.apache.org/jira/browse/CALCITE-436)\]
Simpler SPI to query `Table`

#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-9-2 "Permalink")

- \[ [CALCITE-447](https://issues.apache.org/jira/browse/CALCITE-447)\]
Change semi-join rules to make use of factories
- \[ [CALCITE-442](https://issues.apache.org/jira/browse/CALCITE-442)\
Add `RelOptRuleOperand` constructor that takes a predicate\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-9-2 "Permalink")\
\
- \[ [CALCITE-397](https://issues.apache.org/jira/browse/CALCITE-397)\]\
`SELECT DISTINCT *` on reflective schema gives `ClassCastException` at runtime\
- Various lattice improvements.\
- sqlline: Looking for class-path in inconsistent locations.\
- Re-order test suite, so that fast tests are run first.\
- \[ [CALCITE-444](https://issues.apache.org/jira/browse/CALCITE-444)\]\
Filters wrongly pushed into full outer join\
- Make it more convenient to unit test `RelMetadataQuery`, and add some more\
tests for\
\[ [CALCITE-443](https://issues.apache.org/jira/browse/CALCITE-443)\]\
- \[ [CALCITE-443](https://issues.apache.org/jira/browse/CALCITE-443)\]\
`getPredicates` from a Union is not correct\
- Update references to web sites, git repositories, jira, mailing lists,\
travis CI now that \[INFRA-8413\] is fixed\
- \[ [CALCITE-435](https://issues.apache.org/jira/browse/CALCITE-434)\]\
`FilterAggregateTransposeRule` loses conditions that cannot be pushed\
- \[ [CALCITE-435](https://issues.apache.org/jira/browse/CALCITE-435)\]\
`LoptOptimizeJoinRule` incorrectly re-orders outer joins\
- \[ [CALCITE-439](https://issues.apache.org/jira/browse/CALCITE-439)\]\
`SqlValidatorUtil.uniquify()` may not terminate under some conditions\
- \[ [CALCITE-438](https://issues.apache.org/jira/browse/CALCITE-438)\]\
Push predicates through `SemiJoinRel`\
- Add test case for `LIKE ... ESCAPE`.\
- HOWTO: Modify release instructions.\
- Update `DiffRepository` documentation.\
- Add tests for windowed aggregates without `ORDER BY`. (Works already.)\
\
## [0.9.1-incubating](https://github.com/apache/calcite/releases/tag/calcite-0.9.1-incubating) / 2014-10-02 [Permalink](https://calcite.apache.org/docs/history.html\#v0-9-1 "Permalink")\
\
This is the first release as Calcite. (The project was previously called Optiq.)\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-9-1 "Permalink")\
\
- \[ [CALCITE-430](https://issues.apache.org/jira/browse/CALCITE-430)\]\
Rename project from Optiq to Calcite\
- \[ [CALCITE-426](https://issues.apache.org/jira/browse/CALCITE-426)\]\
Pool JDBC data sources, to make it easier to pool connections\
- \[ [CALCITE-416](https://issues.apache.org/jira/browse/CALCITE-416)\]\
Execute logical `RelNode`s using an interpreter\
- \[ [CALCITE-376](https://issues.apache.org/jira/browse/CALCITE-376)\]\
Move `SqlRun` into its own artifact,\
[Quidem](https://github.com/julianhyde/quidem).\
- \[ [CALCITE-269](https://issues.apache.org/jira/browse/CALCITE-269)\]\
MongoDB result sets larger than 16MB\
- \[ [CALCITE-373](https://issues.apache.org/jira/browse/CALCITE-373)\]\
`NULL` values in `NOT IN` sub-queries\
- SQL functions:\
  - \[ [CALCITE-422](https://issues.apache.org/jira/browse/CALCITE-422)\]\
    Add `REGR_SXX` and `REGR_SYY` regression functions\
  - \[ [CALCITE-421](https://issues.apache.org/jira/browse/CALCITE-421)\]\
    Add `COVAR_POP` and `COVAR_SAMP` aggregate functions\
- Planner rules:\
  - \[ [CALCITE-425](https://issues.apache.org/jira/browse/CALCITE-425)\]\
    Add `FilterAggregateTransposeRule`, that pushes a filter through an\
    aggregate\
  - \[ [CALCITE-399](https://issues.apache.org/jira/browse/CALCITE-399)\]\
    Factorize common `AND` factors out of `OR` predicates\
  - \[ [CALCITE-404](https://issues.apache.org/jira/browse/CALCITE-404)\]\
    `MergeProjectRule` should not construct `RexProgram`s for simple mappings\
  - \[ [CALCITE-394](https://issues.apache.org/jira/browse/CALCITE-394)\]\
    Add `RexUtil.toCnf()`, to convert expressions to conjunctive normal form\
    (CNF)\
  - \[ [CALCITE-389](https://issues.apache.org/jira/browse/CALCITE-389)\]\
    `MergeFilterRule` should flatten `AND` condition\
- Lattices:\
  - \[ [CALCITE-428](https://issues.apache.org/jira/browse/CALCITE-428)\]\
    Use optimization algorithm to suggest which tiles of a lattice to\
    materialize\
  - \[ [CALCITE-410](https://issues.apache.org/jira/browse/CALCITE-410)\]\
    Allow lattice tiles to satisfy a query by rolling up\
  - \[ [CALCITE-406](https://issues.apache.org/jira/browse/CALCITE-406)\]\
    Add tile and measure elements to lattice model element\
  - Now, a lattice can materialize an aggregate-join and use it in a subsequent\
    query.\
  - \[ [CALCITE-402](https://issues.apache.org/jira/browse/CALCITE-402)\]\
    Lattice should create materializations on demand\
  - \[ [CALCITE-344](https://issues.apache.org/jira/browse/CALCITE-344)\]\
    Lattice data structure\
- Field trimmer:\
  - \[ [CALCITE-408](https://issues.apache.org/jira/browse/CALCITE-408)\]\
    Make `FieldTrimmer` work with `RelNode` base classes\
  - \[ [CALCITE-388](https://issues.apache.org/jira/browse/CALCITE-388)\]\
    Handle semi-joins in field trimmer\
  - \[ [CALCITE-395](https://issues.apache.org/jira/browse/CALCITE-395)\]\
    Make `FieldTrimmer.trimFields(SetOp)` generate `ProjectRel` instead of\
    `CalcRel`\
  - \[ [CALCITE-393](https://issues.apache.org/jira/browse/CALCITE-393)\]\
    If no fields are projected from a table, field trimmer should project a\
    dummy expression\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-9-1 "Permalink")\
\
- \[ [CALCITE-413](https://issues.apache.org/jira/browse/CALCITE-413)\]\
Add `RelDataTypeSystem` plugin, allowing different max precision of a\
`DECIMAL`\
- In `Planner`, query de-correlation no longer requires state in a\
`SqlToRelConverter`.\
- Factories:\
  - \[ [CALCITE-392](https://issues.apache.org/jira/browse/CALCITE-392)\]\
    `RelFieldTrimmer` should use factory to create new rel nodes\
  - \[ [CALCITE-382](https://issues.apache.org/jira/browse/CALCITE-382)\]\
    Refactoring rules to use factories\
  - \[ [CALCITE-398](https://issues.apache.org/jira/browse/CALCITE-398)\]\
    Move `CalcRel.createProject` methods to `RelOptUtil`\
  - \[ [CALCITE-396](https://issues.apache.org/jira/browse/CALCITE-396)\]\
    Change return type of `JoinFactory.createJoin()`; add `SemiJoinFactory`\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-9-1 "Permalink")\
\
- \[ [CALCITE-386](https://issues.apache.org/jira/browse/CALCITE-386)\]\
Fix NOTICE\
- Add tests inspired by Derby bugs.\
- Add recent presentation to README.md.\
- \[ [CALCITE-427](https://issues.apache.org/jira/browse/CALCITE-427)\]\
Off-by-one issues in `RemoveDistinctAggregateRule`,\
`AggregateFilterTransposeRule`\
- \[ [CALCITE-414](https://issues.apache.org/jira/browse/CALCITE-414)\]\
Bad class name in `sqlline` shell script\
- Bad package name in `package-info.java` was causing errors in Eclipse.\
- \[ [CALCITE-412](https://issues.apache.org/jira/browse/CALCITE-412)\]\
`RelFieldTrimmer`: when trimming `SortRel`, the collation and trait set don’t\
match\
- Add test case for\
\[ [CALCITE-411](https://issues.apache.org/jira/browse/CALCITE-411)\]\
Duplicate column aliases\
- \[ [CALCITE-407](https://issues.apache.org/jira/browse/CALCITE-407)\]\
`RemoveTrivialProjectRule` drops child node’s traits\
- \[ [CALCITE-409](https://issues.apache.org/jira/browse/CALCITE-409)\]\
`PushFilterPastProjectRule` should not push filters past windowed aggregates\
- Fix tests on Windows.\
- Don’t load `FoodMartQuerySet` unless we have to. It’s big.\
- Enable connection pooling in test suite.\
- \[ [CALCITE-384](https://issues.apache.org/jira/browse/CALCITE-384)\]\
Add `apache-` prefix to tarball and directory within tarball\
- Freeze hive fmpp > freemarker plugin dependency.\
- Upgrade Janino\
- Removed hardcoded foodmart schema information\
- \[ [CALCITE-387](https://issues.apache.org/jira/browse/CALCITE-387)\]\
CompileException when cast TRUE to nullable boolean\
- Temporary fix for\
\[ [CALCITE-390](https://issues.apache.org/jira/browse/CALCITE-390)\]\
Transitive inference (`RelMdPredicates`) doesn’t handle semi-join\
- \[ [CALCITE-385](https://issues.apache.org/jira/browse/CALCITE-385)\]\
Change comment style for Java headers\
- Disable test that is inconistent between JDK 1.7 and 1.8.\
- Fix `git-commit-id-plugin` error when running in Travis-CI.\
- \[ [CALCITE-381](https://issues.apache.org/jira/browse/CALCITE-381)\]\
Remove plugin versions from the `<plugins>` tag in root pom\
- \[ [CALCITE-383](https://issues.apache.org/jira/browse/CALCITE-383)\]\
Each jar should have a `git.properties` file describing its exact version\
- Fix `mvn site` on JDK 1.8 and enable in Travis-CI.\
- Status icon based on master branch, not whichever branch happened to build\
most recently.\
- HOWTO:\
  - Document how to build from git, and how to get jars from maven repo.\
  - Optiq web site\
  - Template emails for Apache votes\
  - Update JIRA cases following release\
  - Instructions for making and verifying a release\
\
## [0.9.0-incubating](https://github.com/apache/calcite/releases/tag/optiq-0.9.0-incubating) / 2014-08-19 [Permalink](https://calcite.apache.org/docs/history.html\#v0-9-0 "Permalink")\
\
This is the first release under the Apache incubator process.\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-9-0 "Permalink")\
\
- \[ [CALCITE-371](https://issues.apache.org/jira/browse/CALCITE-371)\]\
Implement `JOIN` whose `ON` clause contains mixed equi and theta\
- \[ [CALCITE-369](https://issues.apache.org/jira/browse/CALCITE-369)\]\
Add `EnumerableSemiJoinRel`, implementation of semi-join in enumerable\
convention\
- Add class `Strong`, for detecting null-rejecting predicates.\
- \[ [CALCITE-368](https://issues.apache.org/jira/browse/CALCITE-368)\]\
Add SemiJoinRule, planner rule to convert project-join-aggregate into semi-join\
- \[ [CALCITE-367](https://issues.apache.org/jira/browse/CALCITE-367)\]\
`PushFilterPastJoinRule` should strengthen join type\
- Add `EquiJoinRel`, base class for joins known to be equi-joins.\
- Implement `CAST(<string> AS <datetime>)` and\
`<datetime> + <interval>`.\
- \[ [CALCITE-360](https://issues.apache.org/jira/browse/CALCITE-360)\]\
Introduce a rule to infer predicates from equi-join conditions\
- \[ [CALCITE-349](https://issues.apache.org/jira/browse/CALCITE-349)\]\
Add heuristic join-optimizer that can generate bushy joins\
- \[ [CALCITE-346](https://issues.apache.org/jira/browse/CALCITE-346)\]\
Add commutative join rule\
- \[ [CALCITE-347](https://issues.apache.org/jira/browse/CALCITE-347)\]\
In `SqlRun`, add `!plan` command\
- \[ [CALCITE-314](https://issues.apache.org/jira/browse/CALCITE-314)\]\
Allow simple UDFs based on methods\
- \[ [CALCITE-327](https://issues.apache.org/jira/browse/CALCITE-327)\]\
Rules should use base class to find rule match & use factory for object\
creation\
- \[ [CALCITE-316](https://issues.apache.org/jira/browse/CALCITE-316)\]\
In `SqlRun`, match output regardless of order if `ORDER BY` not present\
- \[ [CALCITE-300](https://issues.apache.org/jira/browse/CALCITE-300)\]\
Support multiple parameters in `COUNT(DISTINCT x, y, ...)`\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-9-0 "Permalink")\
\
- \[ [CALCITE-343](https://issues.apache.org/jira/browse/CALCITE-343)\]\
RelDecorrelator should build its own mappings, not inherit from SqlToRelConverter\
- Remove deprecated methods.\
- Convert `Hook` to use Guava `Function` (was linq4j `Function1`).\
- Add fluent method `withHook`, to more easily add hooks in tests.\
- \[ [CALCITE-321](https://issues.apache.org/jira/browse/CALCITE-321)\]\
Add support for overriding implementation of `CompoundIdentifier` in\
`SqlParser`.\
- \[ [CALCITE-322](https://issues.apache.org/jira/browse/CALCITE-322)\]\
Add support for `SqlExplain`, `SqlOrderBy` and `SqlWith` to support\
`SqlShuttle` use.\
- \[ [CALCITE-323](https://issues.apache.org/jira/browse/CALCITE-323)\]\
Override `SqlUnresolvedFunction.inferReturnType()` to return `ANY` type\
so framework implementors can support late bound function implementations.\
- \[ [CALCITE-324](https://issues.apache.org/jira/browse/CALCITE-324)\]\
Add `ViewExpander` for `Planner` in `Frameworks`. Expose additional\
properties of `ViewTable` to allow subclassing.\
- \[ [CALCITE-247](https://issues.apache.org/jira/browse/CALCITE-247)\]\
Add `Context` and `FrameworkConfig`\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-9-0 "Permalink")\
\
- \[ [CALCITE-380](https://issues.apache.org/jira/browse/CALCITE-380)\]\
Downgrade to Guava 11.0.2\
- Move several .md files into new ‘doc’ directory, to keep the root directory simple.\
- Add DISCLAIMER\
- Update history and HOWTO\
- \[ [CALCITE-377](https://issues.apache.org/jira/browse/CALCITE-377)\]\
UnregisteredDriver should catch, log and re-throw NoClassDefFoundError\
- Inherit maven-release-plugin from Apache POM.\
- Test case for\
\[ [CALCITE-373](https://issues.apache.org/jira/browse/CALCITE-373)\]\
NOT IN and NULL values\
- \[ [CALCITE-372](https://issues.apache.org/jira/browse/CALCITE-372)\]\
Change `LoptOptimizeJoinRule` & `PushFilterPast`\\* rules to use factory\
- Upgrade `maven-checkstyle-plugin`.\
- Add class `Holder`, a mutable slot that can contain one object.\
- Remove the 2-minute wait at the top of the hour for tests of\
`CURRENT_TIME`, etc.\
- Tune `ImmutableIntList`’s iterators.\
- \[ [CALCITE-364](https://issues.apache.org/jira/browse/CALCITE-364)\]\
Validator rejects valid `WITH ... ORDER BY` query\
- \[ [CALCITE-363](https://issues.apache.org/jira/browse/CALCITE-363)\]\
Use `dependencyManagement` and `pluginManagement` in POM files\
- Add `FilterFactory`.\
- Add `README` file, incubation disclaimers, and how-to build and running tests.\
- Add `KEYS` and start how-to for making snapshots and releases.\
- Capital case component names; inherit license info from Apache parent POM.\
- Only run `apache-rat` and `git-commit-id-plugin` in “release” maven profile.\
- \[ [CALCITE-348](https://issues.apache.org/jira/browse/CALCITE-348)\]\
Add Apache RAT as maven plugin\
- Change license headers from “Julian Hyde” to “ASF”; add headers where missing.\
- Fix build breakage on JDK 1.6 due to missing method `BitSet.previousClearBit`.\
- Refactor test infrastructure to allow testing against heuristic bushy-join\
optimizer.\
- Add methods and tests for BitSets, and re-organize tests.\
- \[ [CALCITE-354](https://issues.apache.org/jira/browse/CALCITE-354)\]\
Change maven groupId to “org.apache.optiq”\
- Specify return type when calling `RexBuilder.makeCall`, if possible.\
- Eliminate duplicate conditions in `RexProgramBuilder.addCondition`, not\
`RexBuilder.makeCall` as previously.\
- \[ [CALCITE-345](https://issues.apache.org/jira/browse/CALCITE-345)\]\
`AssertionError` in `RexToLixTranslator` comparing to date literal\
- Restore `PushFilterPastJoinRule` to `RelDecorrelator`; interim pending\
\[ [CALCITE-343](https://issues.apache.org/jira/browse/CALCITE-343)\]\
fix.\
- \[ [CALCITE-340](https://issues.apache.org/jira/browse/CALCITE-340)\]\
Fix bug in `SqlToRelConverter` when push expressions in join conditions into\
`ProjectRel`.\
- \[ [CALCITE-313](https://issues.apache.org/jira/browse/CALCITE-313)\]\
Query decorrelation fails\
- While unifying a `RelNode` tree with a materialized view expression,\
switch representation to `MutableRel`s.\
- \[ [CALCITE-305](https://issues.apache.org/jira/browse/CALCITE-305)\]\
Unit test failure on release candidates\
- \[ [CALCITE-325](https://issues.apache.org/jira/browse/CALCITE-325)\]\
Use Java list instead of Guava list to avoid null checks in case of\
`SqlTypeExplicitPrecedenceList`.\
- \[ [CALCITE-326](https://issues.apache.org/jira/browse/CALCITE-326)\]\
Fix `RelOptUtil``ANY` type check.\
- \[ [CALCITE-303](https://issues.apache.org/jira/browse/CALCITE-303)\]\
Migrate issue URLs\
- \[ [CALCITE-331](https://issues.apache.org/jira/browse/CALCITE-331)\]\
Precision/scale compatibility checks should always succeed for `ANY` type\
- In `SqlRun`, allow `!plan` after `!ok` for same SQL statement.\
- \[ [CALCITE-318](https://issues.apache.org/jira/browse/CALCITE-318)\]\
Add unit test for `SqlRun`\
- Fix a bug where composite `SELECT DISTINCT` would return duplicate rows.\
\
## [0.8](https://github.com/apache/calcite/releases/tag/optiq-parent-0.8) / 2014-06-27 [Permalink](https://calcite.apache.org/docs/history.html\#v0-8 "Permalink")\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-8 "Permalink")\
\
- \[ [CALCITE-310](https://issues.apache.org/jira/browse/CALCITE-310)\]\
Implement LEAD, LAG and NTILE windowed aggregates\
- Reduce `COUNT(not-null-expression)` to `COUNT()`\
- \[ [CALCITE-292](https://issues.apache.org/jira/browse/CALCITE-292)\]\
Improve windowed aggregate return types\
- \[ [CALCITE-302](https://issues.apache.org/jira/browse/CALCITE-302)\]\
Use heuristic rule to plan queries with large numbers of joins\
- \[ [CALCITE-283](https://issues.apache.org/jira/browse/CALCITE-283)\]\
Add TPC-DS data generator\
- \[ [CALCITE-294](https://issues.apache.org/jira/browse/CALCITE-294)\]\
Implement DENSE\_RANK windowed aggregate function\
- SqlRun utility\
  - \[ [CALCITE-290](https://issues.apache.org/jira/browse/CALCITE-290)\]\
    Add `SqlRun`, an idempotent utility for running SQL test scripts\
  - Add “!skip” command to SqlRun.\
  - Add MySQL formatting mode to SqlRun.\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-8 "Permalink")\
\
- Re-organize planner initialization,\
to make it easier to use heuristic join order.\
- \[ [CALCITE-301](https://issues.apache.org/jira/browse/CALCITE-301)\]\
Add `Program` interface, a planner phase more general than current `RuleSet`\
- \[ [CALCITE-263](https://issues.apache.org/jira/browse/CALCITE-263)\]\
Add operand type that will cause a rule to fire when a new subset is created\
- Clean up and document SqlKind.\
  - Add `IS_NOT_TRUE` and `IS_NOT_FALSE``SqlKind` enums.\
  - Add `SqlKind.IS_NOT_NULL` enum value, and use where possible,\
    including for `IS_NOT_UNKNOWN` operator.\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-8 "Permalink")\
\
- \[ [CALCITE-312](https://issues.apache.org/jira/browse/CALCITE-312)\]\
Trim non-required fields before `WindowRel`\
- \[ [CALCITE-311](https://issues.apache.org/jira/browse/CALCITE-311)\]\
Wrong results when filtering the results of windowed aggregation\
- More tests for `WITH ... ORDER BY`\
- \[ [CALCITE-309](https://issues.apache.org/jira/browse/CALCITE-309)\]\
`WITH ... ORDER BY` query gives `AssertionError`\
- Enable `MultiJoinRel` and some other planner rule tests.\
- Add `ImmutableNullableList` and `UnmodifiableArrayList`,\
and remove calls to `Arrays.asList`.\
- Add method `IntPair.zip`.\
- Reimplement regular and windowed aggregates\
- Switch from github to Apache JIRA for issues tracking.\
  - In release history, update issue URLs from github to Apache JIRA\
- The Apache mailing list is now the official mailing list. Add presentations.\
- Add test for overloaded UDF.\
- Add tests for `NOT IN` where sub-query returns NULL values.\
- \[ [CALCITE-288](https://issues.apache.org/jira/browse/CALCITE-288)\]\
Add tests for windowed aggregation based on Postgres reference queries\
- \[ [CALCITE-286](https://issues.apache.org/jira/browse/CALCITE-286)\]\
Error casting MongoDB date\
- \[ [CALCITE-284](https://issues.apache.org/jira/browse/CALCITE-284)\]\
Window functions range defaults to `CURRENT ROW`\
- \[ [CALCITE-285](https://issues.apache.org/jira/browse/CALCITE-285)\]\
Window functions throw exception without `ORDER BY`\
- Test case for\
\[<a href=“https://issues.apache.org/jira/browse/CALCITE-285”>CALCITE-285</a>\].\
- \[ [CALCITE-281](https://issues.apache.org/jira/browse/CALCITE-281)\]\
`EXTRACT` function’s SQL return type is `BIGINT` but implemented as Java `int`\
\
## [0.7](https://github.com/apache/calcite/releases/tag/optiq-parent-0.7) / 2014-05-13 [Permalink](https://calcite.apache.org/docs/history.html\#v0-7 "Permalink")\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-7 "Permalink")\
\
- Implement table functions.\
- Arrays and multi-sets:\
  - \[ [CALCITE-267](https://issues.apache.org/jira/browse/CALCITE-267)\]\
    Improve support for ARRAY data type\
  - Better type information for JDBC Array; nested array now possible.\
  - Implement `JOIN LATERAL` and `JOIN UNNEST`.\
  - Implement the `UNNEST` relational operator, and various improvements\
    to `ARRAY` and `MULTISET` data types.\
  - Represent `ARRAY` columns as Java lists.\
  - Implement `CARDINALITY(ARRAY)` SQL operator.\
- Implement scalar sub-query in `SELECT` clause.\
- \[ [CALCITE-273](https://issues.apache.org/jira/browse/CALCITE-273)\]\
Support column alias in WITH queries (common table expressions)\
- Windowed aggregates:\
  - Aggregate over constants, e.g. `SUM(1) OVER (ROWS 10 PRECEDING)`;\
  - `UNBOUNDED PRECEDING` window range;\
  - Windowed aggregates computed over primitive scalars.\
- Fix return type inference for aggregate calls. If the `GROUP BY` clause is\
empty, `SUM` may return null.\
- \[ [CALCITE-37](https://issues.apache.org/jira/browse/CALCITE-37)\]\
Document JSON model file format (as [model.md](https://github.com/apache/calcite/blob/main/site/_docs/model.md)).\
- \[ [CALCITE-238](https://issues.apache.org/jira/browse/CALCITE-238)\]\
Add adapter that generates TPC-H data\
- Improve exception message in `AvaticaConnection`; add\
`ExceptionMessageTest`.\
- Implement micro-benchmarks via\
[JMH](https://openjdk.java.net/projects/code-tools/jmh/).\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-7 "Permalink")\
\
- Provide an option to create root schema without the “metadata” schema.\
- Schema SPI:\
  - \[ [CALCITE-175](https://issues.apache.org/jira/browse/CALCITE-175)\]\
    Modify Schema SPI to allow caching\
  - Get sub-schemas defined by a Schema SPI, and cache their `OptiqSchema`\
    wrappers. (Tobi Vollebregt and Julian Hyde)\
- SqlAdvisor callable from client via JDBC.\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-7 "Permalink")\
\
- Add Apache incubator proposal.\
- Rename RELEASE.md to HISTORY.md.\
- Upgrade maven-release-plugin.\
- Upgrade to linq4j-0.3.\
- Code generation improvements:\
- Move code-generation optimizer to linq4j;\
- Improve translation of strict functions;\
- Mark most methods in `SqlFunctions` as `@Deterministic`;\
- Support `static final` constants generated by linq4j.\
- Avoid excessive box and unbox of primitives when using `Object[]` storage.\
- In JDBC result set, avoid row computation on each accessor call.\
- Test composite join conditions in various flavors of outer join.\
- Use `fromTrait` of the just previously converted `RelNode` instead\
of the original `RelNode`.\
- Disable a MongoDB test, pending\
\[ [CALCITE-270](https://issues.apache.org/jira/browse/CALCITE-270)\].\
- Hush warnings from `SplunkAdapterTest` if Splunk is not available.\
- \[ [CALCITE-252](https://issues.apache.org/jira/browse/CALCITE-252)\]\
Scalar sub-query that returns 0 rows should become NULL value\
- `SplunkAdapterTest` now uses the same Foodmart database as `JdbcTest`.\
- \[ [CALCITE-242](https://issues.apache.org/jira/browse/CALCITE-242)\]\
SplunkAdapterTest fails\
- Remove some obsolete classes.\
- \[ [CALCITE-205](https://issues.apache.org/jira/browse/CALCITE-205)\]\
Suspicious map.get in VolcanoPlanner.reregister\
\
## [0.6](https://github.com/apache/calcite/releases/tag/optiq-parent-0.6) / 2014-04-11 [Permalink](https://calcite.apache.org/docs/history.html\#v0-6 "Permalink")\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-6 "Permalink")\
\
- \[ [CALCITE-214](https://issues.apache.org/jira/browse/CALCITE-214)\]\
Modify Frameworks to allow Schema to be re-used\
Obsoletes `name` field of `ReflectiveSchema`.\
- \[ [CALCITE-237](https://issues.apache.org/jira/browse/CALCITE-237)\]\
Allow user-defined aggregate functions (UDAs) to be defined in a model\
- \[ [CALCITE-227](https://issues.apache.org/jira/browse/CALCITE-227)\]\
Extend `EXTRACT` function to support `DATE`, `TIME` and `TIMESTAMP` values\
- \[ [CALCITE-222](https://issues.apache.org/jira/browse/CALCITE-222)\]\
User-defined table macros\
- \[ [CALCITE-179](https://issues.apache.org/jira/browse/CALCITE-179)\]\
Optiq on Windows\
\
  - Add `sqlline.bat` and fix issues running `sqlline` under Cygwin.\
- \[ [CALCITE-195](https://issues.apache.org/jira/browse/CALCITE-195)\]\
Push aggregation into MongoDB adapter\
- \[ [CALCITE-193](https://issues.apache.org/jira/browse/CALCITE-193)\]\
Implement OFFSET and LIMIT in MongoDB adapter\
- \[ [CALCITE-164](https://issues.apache.org/jira/browse/CALCITE-164)\]\
Improve query performance of optiq over MongoDB\
- Add Phoenix (HBase) SQL dialect (Bruno Dumon)\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-6 "Permalink")\
\
- Obsolete `RexImpTable.AggregateImplementor` and rename `AggImplementor2`.\
( **This is a breaking change**.)\
- Convert `CombinedParser.jj` into freemarker template to allow\
custom parser implementations. (Venki Korukanti)\
- Extend `Planner` to pass a custom `ConvertletTable` and custom SQL parser.\
- In `Frameworks`, add a way to specify list of `TraitDef`s that will be used\
by planner. (Jinfeng Ni)\
- \[ [CALCITE-198](https://issues.apache.org/jira/browse/CALCITE-198)\]\
Use `RexExecutor` to evaluate projections and filters\
- \[ [CALCITE-219](https://issues.apache.org/jira/browse/CALCITE-219)\]\
Parse `ALTER scope SET option = value` statement\
- \[ [CALCITE-215](https://issues.apache.org/jira/browse/CALCITE-215)\]\
A Schema should not have to remember its name and parent\
( **This is a breaking change**.)\
- \[ [CALCITE-180](https://issues.apache.org/jira/browse/CALCITE-180)\]\
Common base class for TableFunction, ScalarFunction\
( **This is a breaking change**.)\
- Add methods for dealing with symbols; deprecate\
`SqlLiteral.booleanValue(SqlNode)`, `SqlLiteral.symbolValue(SqlNode)`.\
- Add `RelOptPlanner.clear()`; now it is safe to call `transform` twice.\
(Jinfeng Ni)\
- Remove APIs deprecated for 0.5.\
- Move around some operator classes and singletons.\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-6 "Permalink")\
\
- Upgrade to linq4j-0.2.\
- `FETCH` and `LIMIT` are ignored during SQL-to-RelNode translation.\
(Venki Korukanti)\
- \[ [CALCITE-245](https://issues.apache.org/jira/browse/CALCITE-245)\]\
Off-by-one translation of ON clause of JOIN\
- \[ [CALCITE-191](https://issues.apache.org/jira/browse/CALCITE-191)\]\
Rotate time/date/timestamp vals to local timezone\
- \[ [CALCITE-244](https://issues.apache.org/jira/browse/CALCITE-244)\]\
`RelOptTableImpl.create` always expects `QueryableTable` type in\
`OptiqSchema.TableEntry`\
- \[ [CALCITE-225](https://issues.apache.org/jira/browse/CALCITE-225)\]\
Optiq doesn’t correctly decorrelate queries\
- Clean up package-info. Remove duplicates in test packages so they\
don’t conflict with those in non-test packages.\
- Add `Pair.adjacents(Iterable)`.\
- \[ [CALCITE-199](https://issues.apache.org/jira/browse/CALCITE-199)\]\
Various `ANY` type conditions aren’t correctly being considered\
(Jacques Nadeau)\
- Add files to `.gitignore` that shouldn’t be checked in when using\
Eclipse. (Jacques Nadeau)\
- Add class `ControlFlowException`, and make it base class of\
existing control-flow exception classes.\
- \[ [CALCITE-232](https://issues.apache.org/jira/browse/CALCITE-232)\]\
Sum and avg of empty set should be null as per SQL specification\
- Add `SqlUnresolvedFunction`, to improve how return type of\
user-defined functions is resolved. (Vladimir Sitnikov)\
- \[ [CALCITE-228](https://issues.apache.org/jira/browse/CALCITE-228)\]\
Error while compiling generated Java code when using UDF in expression\
- \[ [CALCITE-226](https://issues.apache.org/jira/browse/CALCITE-226)\]\
User-defined functions should work without explicit schema prefix\
- \[ [CALCITE-229](https://issues.apache.org/jira/browse/CALCITE-229)\]\
Join between different JDBC schemas not implementable\
- \[ [CALCITE-230](https://issues.apache.org/jira/browse/CALCITE-230)\]\
RemoveSortRule derives trait set from sort, should derive it from sort’s child\
- Test view and sub-query with `ORDER BY` and `LIMIT`.\
- \[ [CALCITE-223](https://issues.apache.org/jira/browse/CALCITE-223)\]\
Add `NOTICE` and `LICENSE` files in all generated JAR files\
- \[ [CALCITE-209](https://issues.apache.org/jira/browse/CALCITE-209)\]\
Consistent strategy for line-endings in tests\
Convert uses of `NL` in tests to Linux newline “\\n”.\
This makes string constants simpler.\
- \[ [CALCITE-218](https://issues.apache.org/jira/browse/CALCITE-218)\]\
Functions case sensitive when using `Lex.MYSQL`\
- Add tests that a query with aggregate expressions in the `SELECT`\
clause is considered an aggregate query, even if there is no `GROUP BY`.\
- \[ [CALCITE-216](https://issues.apache.org/jira/browse/CALCITE-216)\]\
Inconsistent use of provided operator table causes inability to\
add aggregate functions\
- \[ [CALCITE-200](https://issues.apache.org/jira/browse/CALCITE-200)\]\
Javadoc generation fails under JDK 1.8\
- Add class `XmlOutput` (based on `org.eigenbase.xom.XMLOutput`) and remove\
dependency on eigenbase-xom.\
- Performance: Don’t create stack-trace for exceptions used for control-flow.\
(Vladimir Sitnikov)\
- Performance: Tune `RexProgramBuilder` by using `Pair` rather than `String` as\
expression key. (Vladimir Sitnikov)\
- Fix NPE using TRIM function with JDBC. (Bruno Dumon)\
- Add dependency on\
[hydromatic-resource-maven-plugin](https://github.com/julianhyde/hydromatic-resource)\
and obsolete our copy of the resource framework.\
- Fix race condition in `SpaceList`.\
- In planner, use `RelTrait.subsumes` rather than `equals` in an assert.\
(Jinfeng Ni)\
\
## [0.5](https://github.com/apache/calcite/releases/tag/optiq-parent-0.5) / 2014-03-14 [Permalink](https://calcite.apache.org/docs/history.html\#v0-5 "Permalink")\
\
#### New features [Permalink](https://calcite.apache.org/docs/history.html\#new-features-0-5 "Permalink")\
\
- Allow `quoting`, `quotedCasing`, `unquotedCasing`, and `caseSensitive`\
properties to be specified explicitly (Vladimir Sitnikov)\
- Recognize more kinds of materializations, including filter-on-project (where\
project contains expressions) and some kinds of aggregation.\
- \[ [CALCITE-128](https://issues.apache.org/jira/browse/CALCITE-128)\]\
Support `WITH` queries (common table expressions)\
- \[ [CALCITE-53](https://issues.apache.org/jira/browse/CALCITE-53)\]\
Allow `WHEN` clause in simple `CASE` expression to have multiple values\
- \[ [CALCITE-156](https://issues.apache.org/jira/browse/CALCITE-156)\]\
Optiq should recognize ‘SYSTEM TABLE’, ‘JOIN’, ‘INDEX’ as table types\
- Support querying ARRAY columns from JDBC source. (Gabriel Reid)\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-5 "Permalink")\
\
- Add\
`ProjectRelBase.copy(RelTraitSet, RelNode, List<RexNode>, RelDataType)`\
and make `ProjectRelBase.copy(RelTraitSet, RelNode)` final.\
( **This is a breaking change** for sub-classes of `ProjectRelBase`.)\
- Change `RexBuilder.makeRangeReference` parameter type.\
- `RexBuilder.makeInputRef` replaces `RelOptUtil.createInputRef`.\
- \[ [CALCITE-160](https://issues.apache.org/jira/browse/CALCITE-160)\]\
Allow comments in schema definitions\
- \[ [CALCITE-147](https://issues.apache.org/jira/browse/CALCITE-147)\]\
Create a new kind of `SqlCall` that keeps operands in fields, not an operands\
array\
\
  - Very widely used parse tree nodes with complex operands, including\
    `SqlSelect`, `SqlJoin`, `SqlInsert`, and a new node type `SqlOrderBy`, are\
    now sub-classes of `SqlCall` but not `SqlBasicCall`.\
  - ( **This is a breaking change** to code that assumes that, say,\
    `SqlSelect` has an `operands` field.)\
- Convert all enum constants to upper-case.\
( **This is a breaking change**.)\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-5 "Permalink")\
\
- Generate optiq-core-VERSION-tests.jar not parent-VERSION-tests.jar.\
- \[ [CALCITE-176](https://issues.apache.org/jira/browse/CALCITE-176)\]\
ORDER BY expression doesn’t work with SELECT \*\
- Fix VARCHAR casts sent to hsqldb source (Bruno Dumon)\
- \[ [CALCITE-143](https://issues.apache.org/jira/browse/CALCITE-143)\]\
Remove dependency on eigenbase-resgen\
- \[ [CALCITE-173](https://issues.apache.org/jira/browse/CALCITE-173)\]\
Case-insensitive table names are not supported for `Casing.UNCHANGED`\
- `DATE.getLimit` now returns `Calendar` in GMT time zone (Vladimir Sitnikov)\
- Set `en_US` locale in tests that match against error numbers, dates\
(Vladimir Sitnikov)\
- Use 1 test thread per CPU to avoid thread starvation on dual core CPUs\
(Vladimir Sitnikov)\
- \[ [CALCITE-174](https://issues.apache.org/jira/browse/CALCITE-174)\]\
Move hsqldb to test scope\
- Add unit tests for `RexExecutorImpl`.\
- Correct JSON model examples in Javadoc comments. (Karel Vervaeke)\
- Move test reference logs from `src/test/java` to `src/test/resources`\
(reduces the number of ‘untracked files’ reported by git)\
- Tune `Util.SpaceList`, fix race condition, and move into new utility class\
`Spaces`.\
- \[ [CALCITE-163](https://issues.apache.org/jira/browse/CALCITE-163)\]\
Equi-join warning\
- \[ [CALCITE-157](https://issues.apache.org/jira/browse/CALCITE-157)\]\
Handle `SQLFeatureNotSupported` when calling `setQueryTimeout`\
(Karel Vervaeke)\
- Fix Optiq on Windows. (All tests and checkstyle checks pass.)\
- In checkstyle, support Windows-style file separator, otherwise build fails in\
Windows due to suppressions not used. (Vladimir Sitnikov)\
- Enable MongoDB tests when `-Dcalcite.test.mongodb=true`.\
- Cleanup cache exception-handling and an assert.\
- \[ [CALCITE-153](https://issues.apache.org/jira/browse/CALCITE-153)\]\
Error using MongoDB adapter: Failed to set setXIncludeAware(true)\
- Disable spark engine unless Spark libraries are on the class path and\
`spark=true` is specified in the connect string.\
- Fix path to `mongo-zips-model.json` in HOWTO. (Mariano Luna)\
- Fix bug deriving the type of a join-key.\
- Fix the value of `ONE_MINUS_EPSILON`.\
- \[ [CALCITE-158](https://issues.apache.org/jira/browse/CALCITE-158)\]\
Optiq fails when call `Planner.transform()` multiple times, each with\
different ruleset\
- \[ [CALCITE-148](https://issues.apache.org/jira/browse/CALCITE-148)\]\
Less verbose description of collation. Also, optimize `RelTraitSet` creation\
and amortize `RelTraitSet.toString()`.\
- Add generics to SQL parser.\
- \[ [CALCITE-145](https://issues.apache.org/jira/browse/CALCITE-145)\]\
Unexpected upper-casing of keywords when using java lexer\
- Remove duplicate `maven-source-plugin`.\
- \[ [CALCITE-141](https://issues.apache.org/jira/browse/CALCITE-141)\]\
Downgrade to guava-11.0.2. (This is necessary for Hadoop compatibility.\
Later versions of Guava can also be used.)\
- Upgrade to spark-0.9.0. (Because this version of spark is available from\
maven-central, we can make optiq-spark part of the regular build, and remove\
the spark profile.)\
\
## [0.4.18](https://github.com/apache/calcite/releases/tag/optiq-parent-0.4.18) / 2014-02-14 [Permalink](https://calcite.apache.org/docs/history.html\#v0-4-18 "Permalink")\
\
#### API and functionality changes [Permalink](https://calcite.apache.org/docs/history.html\#api-0-4-18 "Permalink")\
\
- Configurable lexical policy\
  - \[ [CALCITE-33](https://issues.apache.org/jira/browse/CALCITE-33)\]\
    SQL parser should allow different identifier quoting\
  - \[ [CALCITE-34](https://issues.apache.org/jira/browse/CALCITE-34)\]\
    Policy for case-sensitivity of identifiers should be configurable\
  - New connect-string parameter “lex”, with allowable values\
    “ORACLE”, “MYSQL”, “SQL\_SERVER”, “JAVA” sets policy to be like those\
    databases, in terms of quote string, whether quoted and unquoted\
    identifiers are converted to upper/lower case, and whether\
    identifiers are matched case-sensitively. “JAVA” is case-sensitive,\
    even for unquoted identifiers. It should be possible\
    for each connection to have its own settings for these. Objects\
    shared between sessions (views, materialized views) might\
    require more work.\
  - Added various internals to make it easy for developers to do the\
    right thing. When you need to look up a schema, table or\
    column/field name, you should use a catalog reader, and it will\
    apply the right case-sensitivity policy.\
  - Enable optiq consumer to utilize different lexical settings in\
    Frameworks/Planner. (Jacques Nadeau)\
- \[ [CALCITE-115](https://issues.apache.org/jira/browse/CALCITE-135)\]\
Add a PARSE\_TREE hook point with SqlNode parameter\
- Change planner rules to use `ProjectFactory` for creating\
projects. (John Pullokkaran)\
- \[ [CALCITE-131](https://issues.apache.org/jira/browse/CALCITE-131)\]\
Add interfaces for metadata (statistics)\
( **This is a breaking change**.)\
- Update Avatica to allow `Cursor` & `Accessor` implementations to throw\
`SQLException`. (Jacques Nadeau)\
- Separate cost model (`RelOptCostFactory`) from planner. Allow\
`VolcanoPlanner` to be sub-classed with different cost factory.\
\
  - Remove references to VolcanoCost from RelSubset, so clients can\
    use a different `RelOptCost`. (Harish Butani)\
  - Make `VolcanoCost` immutable.\
- Break `SqlTypeStrategies` into `OperandTypes`, `ReturnTypes` and\
`InferTypes`, and rename its static members to upper-case, per\
checkstyle. ( **This is a breaking change**.)\
- Add a mechanism for defining configuration parameters and have them\
appear in the responses to `AvaticaDatabaseMetaData` methods.\
- \[ [CALCITE-113](https://issues.apache.org/jira/browse/CALCITE-113)\]\
User-defined scalar functions\
- Add rules to short-cut a query if `LIMIT 0` is present. Also remove\
sort, aggregation, join if their inputs are known to be empty, and\
propagate the fact that the relational expressions are known to be\
empty up the tree. (We already do this for union, filter, project.)\
- `RexNode` and its sub-classes are now immutable.\
\
#### Bug-fixes and internal changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-4-18 "Permalink")\
\
- \[ [CALCITE-16](https://issues.apache.org/jira/browse/CALCITE-61)\]\
Upgrade to janino-2.7\
- Upgrade to guava-15.0 (guava-14.0.1 still allowed), sqlline-1.1.7,\
maven-surefire-plugin-2.16, linq4j-0.1.13.\
- \[ [CALCITE-136](https://issues.apache.org/jira/browse/CALCITE-136)\]\
Support Hive dialect\
- \[ [CALCITE-138](https://issues.apache.org/jira/browse/CALCITE-138)\]\
SqlDataTypeSpec.clone handles collection types wrong\
- \[ [CALCITE-137](https://issues.apache.org/jira/browse/CALCITE-137)\]\
If a subset is created that is subsumed by an existing subset, its\
‘best’ is not assigned\
\
  - If best rel in a Volcano subset doesn’t have metadata, see if\
    other rels have metadata.\
- \[ [CALCITE-127](https://issues.apache.org/jira/browse/CALCITE-127)\]\
EnumerableCalcRel can’t support 3+ AND conditions (Harish Butani)\
- Fix push-down of datetime literals to JDBC data sources.\
- Add `Util.startsWith(List, List)` and `Util.hashCode(double)`.\
- Add maven-checkstyle-plugin, enable in “verify” phase, and fix exceptions.\
- Fix `SqlValidator` to rely on `RelDataType` to do field name matching. Fix\
`RelDataTypeImpl` to correctly use the case sensitive flag rather than\
ignoring it.\
- \[ [CALCITE-119](https://issues.apache.org/jira/browse/CALCITE-119)\]\
Comparing Java type long with SQL type INTEGER gives wrong answer\
- Enable multi-threaded testing, and fix race conditions.\
  - Two of the race conditions involved involving trait caches. The\
    other was indeterminacy in type system when precision was not\
    specified but had a default; now we canonize TIME to TIME(0), for\
    instance.\
- Convert files to `us-ascii`.\
- Work around\
\[ [JANINO-169](https://jira.codehaus.org/browse/JANINO-169)\].\
- Refactor SQL validator testing infrastructure so SQL parser is\
configurable.\
- Add `optiq-mat-plugin` to README.\
- Fix the check for duplicate subsets in a rule match.\
- \[ [CALCITE-112](https://issues.apache.org/jira/browse/CALCITE-112)\]\
Java boolean column should be treated as SQL boolean\
- Fix escaped unicode characters above 0x8000. Add tests for unicode\
strings.\
\
## [0.4.17](https://github.com/apache/calcite/releases/tag/optiq-parent-0.4.17) / 2014-01-13 [Permalink](https://calcite.apache.org/docs/history.html\#v0-4-17 "Permalink")\
\
#### API changes [Permalink](https://calcite.apache.org/docs/history.html\#fixes-0-4-17 "Permalink")\
\
- \[ [CALCITE-106](https://issues.apache.org/jira/browse/CALCITE-106)\]\
Make `Schema` and `Table` SPIs simpler to implement, and make them\
re-usable across connections\
( **This is a breaking change**.)\
- Make it easier to define sub-classes of rule operands. The new class\
`RelOptRuleOperandChildren` contains the children of an operand and\
the policy for dealing with them. Existing rules now use the new\
methods to construct operands: `operand()`, `leaf()`, `any()`, `none()`,\
`unordered()`. The previous methods are now deprecated and will be\
removed before 0.4.18. ( **This is a breaking change**.)\
- \[ [CALCITE-101](https://issues.apache.org/jira/browse/CALCITE-101)\]\
Enable phased access to the Optiq engine\
- List-handling methods in `Util`: add methods `skipLast`, `last`, `skip`;\
remove `subList`, `butLast`.\
- Convert `SqlIdentifier.names` from `String[]` to `ImmutableList<String>`.\
- Rename `OptiqAssert.assertThat()` to `that()`, to avoid clash with junit’s\
`Assert.assertThat()`.\
- Usability improvements for `RelDataTypeFactory.FieldInfoBuilder`. It\
now has a type-factory, so you can just call `build()`.\
- Rework `HepProgramBuilder` into a fluent API.\
- \[ [CALCITE-105](https://issues.apache.org/jira/browse/CALCITE-105)\]\
Externalize RelNode to and from JSON\
\
#### Tuning [Permalink](https://calcite.apache.org/docs/history.html\#tuning-0-4-17 "Permalink")\
\
- If `EnumerableAggregateRel` has no aggregate functions, generate a\
call to `Enumerable.distinct()`, thereby saving the effort of\
building trivial accumulators.\
- Default rule set now does not introduce `CalcRel` until a later phase\
of planning. This reduces the number of trivial projects and calcs\
created, merged, and elimated.\
- Reduce the amount of time spent creating record types that\
already exist.\
- More efficient implementation of `Util.isDistinct` for small lists.\
- When an internal record has 0 fields, rather than generating a\
synthetic class and lots of instances that are all the same, use the\
new `Unit` class, which is a singleton.\
- To take advantage of asymmetric hash join added recently in linq4j,\
tweak cost of `EnumerableJoinRel` so that join is cheaper if the\
larger input is on the left, and more expensive if it is a cartesian\
product.\
- \[ [CALCITE-70](https://issues.apache.org/jira/browse/CALCITE-70)\]\
Joins seem to be very expensive in memory\
- Make planning process more efficient by not sorting the list of\
matched rules each cycle. It is sorted if tracing is enabled;\
otherwise we scan to find the most important element. For this list,\
replace `LinkedList` with `ChunkList`, which has an O(1) remove and add,\
a fast O(n) get, and fast scan.\
\
#### Other [Permalink](https://calcite.apache.org/docs/history.html\#other-0-4-17 "Permalink")\
\
- \[ [CALCITE-87](https://issues.apache.org/jira/browse/CALCITE-87)\]\
Constant folding\
\
  - Rules for constant-expression reduction, and to simplify/eliminate\
    `VALUES` operator.\
- Graph algorithms: Implement breadth-first iterator and cycle-detector.\
- Fix bug in planner which occurred when two `RelNode`s have identical\
digest but different row-type.\
- Fix link to optiq-csv tutorial.\
- Fix bugs in `RemoveTrivialProjectRule.strip`, `JdbcProjectRel.implement`\
and `SortRel.computeSelfCost`.\
- Reformat code, and remove `@author` tags.\
- Upgrade to eigenbase-xom-1.3.4, eigenbase-properties-1.1.4,\
eigenbase-resgen-1.3.6.\
- Upgrade to linq4j-0.1.12.\
- \[ [CALCITE-97](https://issues.apache.org/jira/browse/CALCITE-97)\]\
Correlated EXISTS\
- Fix a bug in `VolcanoCost`.\
- Add class `FoodMartQuerySet`, that contains the 6,700 foodmart queries.\
- Fix factory class names in `UnregisteredDriver`\
- \[ [CALCITE-96](https://issues.apache.org/jira/browse/CALCITE-96)\]\
LIMIT against a table in a clone schema causes UnsupportedOperationException\
- Disable spark module by default.\
- Allow `CloneSchema` to be specified in terms of url, driver, user,\
password; not just dataSource.\
- Wrap internal error in `SQLException`.\
\
## [0.4.16](https://github.com/apache/calcite/releases/tag/optiq-parent-0.4.16) / 2013-11-24 [Permalink](https://calcite.apache.org/docs/history.html\#v0-4-16 "Permalink")\
\
- \[ [CALCITE-69](https://issues.apache.org/jira/browse/CALCITE-69)\]\
Can’t join on string columns and other problems with expressions in the join\
condition\
- \[ [CALCITE-74](https://issues.apache.org/jira/browse/CALCITE-74)\]\
JOIN … USING fails in 3-way join with UnsupportedOperationException.\
- \[ [CALCITE-65](https://issues.apache.org/jira/browse/CALCITE-65)\]\
Fix issues in the JDBC driver, and in particular to DatabaseMetaData methods,\
to make Squirrel-SQL run better.\
- Fix JDBC column, table, schema names for when the table is not in a schema of\
depth 1.\
- \[ [CALCITE-85](https://issues.apache.org/jira/browse/CALCITE-85)\]\
Adding a table to the root schema causes breakage in OptiqPrepareImpl\
- \[ [CALCITE-84](https://issues.apache.org/jira/browse/CALCITE-84)\]\
Extract Optiq’s JDBC driver as a new JDBC driver framework, Avatica.\
Other projects can use this to implement a JDBC driver by implementing\
just a few methods. If you wish to use Optiq’s JDBC driver, you will\
now need to include optiq-avatica.jar in addition to optiq-core.jar.\
Avatica does not depend on anything besides the standard Java library.\
- Support for parameters in PreparedStatement.\
- First steps in recognizing complex materializations. Internally we introduce a\
concept called a “star table”, virtual table composed of real tables joined\
together via many-to-one relationships. The queries that define\
materializations and end-user queries are canonized in terms of star tables.\
Matching (not done yet) will then be a matter of looking for sort, groupBy,\
project. It is not yet possible to define a star in an Optiq model file.\
- Add section to [HOWTO](https://github.com/apache/calcite/blob/main/site/_docs/howto.md)\
on implementing adapters.\
- Fix data type conversions when creating a clone table in memory.\
- Fix how strings are escaped in JsonBuilder.\
- Test suite now depends on an embedded hsqldb database, so you can run\
`mvn test` right after pulling from git. You can instead use a\
MySQL database if you specify ‘-Dcalcite.test.db=mysql’, but you need to\
manually populate it.\
- Fix a planner issue which occurs when the left and right children of join are\
the same relational expression, caused by a self-join query.\
- \[ [CALCITE-76](https://issues.apache.org/jira/browse/CALCITE-76)\]\
Precedence of the item operator, `map[index]`; remove the space\
before ‘\[’ when converting parse tree to string.\
- Allow `CAST(expression AS ANY)`, and fix an issue with the ANY type\
and NULL values.\
- Handle null timestamps and dates coming out of JDBC adapter.\
- Add `jdbcDriver` attribute to JDBC schema in model, for drivers\
that do not auto-register.\
- Allow join rules to match any subclass of JoinRelBase.\
- Push projects, filters and sorts down to MongoDB. (Fixes\
\[ [CALCITE-57](https://issues.apache.org/jira/browse/CALCITE-57)\],\
\[ [CALCITE-60](https://issues.apache.org/jira/browse/CALCITE-60)\] and\
\[ [CALCITE-72](https://issues.apache.org/jira/browse/CALCITE-72)\].)\
- Add instructions for loading FoodMart data set into MongoDB, and how to enable\
tracing.\
- Now runs on JDK 1.8 (still runs on JDK 1.6 and JDK 1.7).\
- Upgrade to junit-4.11 (avoiding the dodgy junit-4.1.12).\
- Upgrade to linq4j-0.1.11.\
\
## [0.4.15](https://github.com/apache/calcite/releases/tag/optiq-parent-0.4.15) / 2013-10-14 [Permalink](https://calcite.apache.org/docs/history.html\#v0-4-15 "Permalink")\
\
- Lots of good stuff that this margin is too small to contain. See\
[SQL language reference](https://github.com/apache/calcite/blob/main/site/_docs/reference.md) and\
[JSON model reference](https://github.com/apache/calcite/blob/main/site/_docs/model.md).\
\
# Optiq-csv release history [Permalink](https://calcite.apache.org/docs/history.html\#optiq-csv-release-history "Permalink")\
\
Optiq-csv-0.3 was the last independent release of optiq-csv. From\
calcite-0.9.2 onwards, the code was included as the\
calcite-example-csv module.\
\
- Upgrade to calcite-0.9.1\
- Support gzip-compressed CSV and JSON files (recognized by ‘.gz’ suffix)\
- Cleanup, and fix minor timezone issue in a test\
- Support for date types (date, time, timestamp) (Martijn van den Broek)\
- Upgrade to optiq-0.8, optiq-avatica-0.8, linq4j-0.4\
- Add support for JSON files (recognized by ‘.json’ suffix)\
- Upgrade maven-release-plugin to version 2.4.2\
- Upgrade to optiq-0.6, linq4j-0.2\
- Add NOTICE and LICENSE files in generated JAR file\
\
## [0.3](https://github.com/julianhyde/optiq-csv/releases/tag/optiq-csv-0.3) / 2014-03-21 [Permalink](https://calcite.apache.org/docs/history.html\#csv-v0-3 "Permalink")\
\
- Upgrade to optiq-0.5\
- Add workaround to\
\[ [JLINE2-62](https://github.com/jline/jline2/issues/62)\]\
to `sqlline.bat` (windows) and `sqlline` (windows using cygwin)\
- Fix classpath construction: `sqlline.bat` copies dependencies to\
`target/dependencies`; `sqlline` constructs `target/classpath.txt`\
- Build, checkstyle and tests now succeed on windows (both native and cygwin)\
- Models can now contain comments\
- \[ [OPTIQ-CSV-2](https://github.com/julianhyde/optiq-csv/issues/2)\]\
Update tutorial to reflect changes to Optiq’s JDBC adapter\
\
## [0.2](https://github.com/julianhyde/optiq-csv/releases/tag/optiq-csv-0.2) / 2014-02-18 [Permalink](https://calcite.apache.org/docs/history.html\#csv-v0-2 "Permalink")\
\
- Add test case for\
\[ [CALCITE-112](https://issues.apache.org/jira/browse/CALCITE-112)\]\
- Add `sqlline.bat`, Windows SQL shell (based on fix for\
\[ [DRILL-338](https://issues.apache.org/jira/browse/DRILL-338)\])\
- Upgrade to optiq-0.4.18, sqlline-1.1.7\
- Return a single object for single-col enumerator (Gabriel Reid)\
- Enable maven-checkstyle-plugin; fix checkstyle exceptions\
\
## [0.1](https://github.com/julianhyde/optiq-csv/releases/tag/optiq-csv-0.1) / 2014-01-13 [Permalink](https://calcite.apache.org/docs/history.html\#csv-v0-1 "Permalink")\
\
- Add release notes and history\
- Enable maven-release-plugin\
- Upgrade to optiq-0.4.17, linq4j-0.1.12, sqlline-1.1.6\
- Upgrade tutorial for new Schema and Table SPIs\
- Fixes for optiq SPI changes in\
\[ [CALCITE-106](https://issues.apache.org/jira/browse/CALCITE-106)\]\
- Enable oraclejdk8 in Travis CI\
- Fix bug where non-existent directory would give NPE; instead print warning\
- Add an example of a planner rule\
- Add `CsvTableFactory`, an example of a custom table\
- Add a view to tutorial\
- Split into scenario with a “simple” schema that generates tables\
(`CsvTable`) that just execute and a “smart” schema that generates\
tables (`CsvSmartTable`) that undergo optimization\
- Make `CsvEnumerator` a top-level class\
- Implement the algorithms to sniff names and types from the first\
row, and to return an enumerator of all rows\
- Read column types from header of CSV file\
\
# Linq4j release history [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-release-history "Permalink")\
\
Linq4j-0.4 was the last independent release of linq4j. From\
calcite-0.9.2 onwards, the code was included as calcite-linq4j, and\
features added to linq4j in a particular calcite release are described\
with the other changes in that release.\
\
## [0.4](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.4) / 2014-05-28 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-4 "Permalink")\
\
- Fix [#27](https://github.com/julianhyde/linq4j/issues/27),\
“Incorrectly inlines non-final variable”.\
- Maven build process now deploys web site.\
- Implement `Enumerable` methods: `any`, `all`,\
`contains` with `EqualityComparer`, `first`, `first` with predicate.\
\
## [0.3](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.3) / 2014-04-21 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-3 "Permalink")\
\
- Move optimizer visitor from optiq to linq4j; add\
`ExpressionType.modifiesLvalue` to avoid invalid inlining.\
- Fix [#17](https://github.com/julianhyde/linq4j/issues/17),\
“Assign constant expressions to ‘static final’ members”;\
add `@Deterministic` annotation to help deduce which expressions are\
constant.\
- Multi-pass optimization: some of the variables might be avoided and\
inlined after the first pass.\
- Various other peephole optimizations: `Boolean.valueOf(const)`,\
‘not’ expressions (`!const`, `!!a`, `!(a==b)`, `!(a!=b)`, `!(a>b)`,\
etc.),\
‘?’ expressions coming from `CASE` (`a ? booleanConstant : b` and `a\
? b : booleanConstant`).\
- Implement left, right and full outer join.\
- Clean build on cygwin/Windows.\
\
## [0.2](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.2) / 2014-04-11 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-2 "Permalink")\
\
- Fix [#8](https://github.com/julianhyde/linq4j/issues/8),\
“Javadoc generation fails under JDK 1.8”.\
- Fix [#15](https://github.com/julianhyde/linq4j/issues/15),\
“`Expressions.ifThenElse` does not work”.\
- Use `HashMap` for searching of declarations to reuse; consider both\
`optimizing` and `optimize` flags when reusing.\
- Implement `equals` and `hashCode` for expressions. Hash codes for\
complex expressions are cached into a field of the expression.\
- Add example, `com.example.Linq4jExample`.\
- Fix optimizing away parameter declarations in assignment target.\
- Support Windows path names in checkstyle-suppresions.\
- Support `Statement.toString` via `ExpressionWriter`.\
- Use `AtomicInteger` for naming of `ParameterExpression`s to avoid\
conflicts in multithreaded usage\
- Cleanup: use `Functions.adapt` rather than `new AbstractList`\
- Add `NOTICE` and `LICENSE` files in generated JAR file.\
- Optimize `select()` if selector is identity.\
- Enable checkstyle.\
\
## [0.1.13](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.1.13) / 2014-01-20 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-1-13 "Permalink")\
\
- Remove spurious “null” generated when converting expression to string.\
- Allow a field declaration to not have an initializer.\
- Add `Primitive.defaultValue`.\
- Enable `oraclejdk8` in [Travis CI](https://travis-ci.org/julianhyde/linq4j).\
\
## [0.1.12](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.1.12) / 2013-12-07 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-1-12 "Permalink")\
\
- Add release notes.\
- Fix implementation of `Enumerable.asEnumerable` in\
`DefaultQueryable` (inherited by most classes that implement\
`Queryable`).\
\
## [0.1.11](https://github.com/julianhyde/linq4j/releases/tag/linq4j-0.1.11) / 2013-11-06 [Permalink](https://calcite.apache.org/docs/history.html\#linq4j-v0-1-11 "Permalink")\
\
- Initial commit\
\
[Previous](https://calcite.apache.org/docs/howto.html)\
\
[Next](https://calcite.apache.org/docs/powered_by.html)