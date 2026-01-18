Navigate the docs…

# SQL language

The page describes the SQL dialect recognized by Calcite’s default SQL parser.

## Grammar [Permalink](https://calcite.apache.org/docs/reference.html\#grammar "Permalink")

SQL grammar in [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)-like
form.

```sql
statement:
      setStatement
  |   resetStatement
  |   explain
  |   describe
  |   insert
  |   update
  |   merge
  |   delete
  |   query

statementList:
      statement [ ';' statement ]* [ ';' ]

setStatement:
      [ ALTER { SYSTEM | SESSION } ] SET identifier '=' expression

resetStatement:
      [ ALTER { SYSTEM | SESSION } ] RESET identifier
  |   [ ALTER { SYSTEM | SESSION } ] RESET ALL

explain:
      EXPLAIN PLAN
      [ WITH TYPE | WITH IMPLEMENTATION | WITHOUT IMPLEMENTATION ]
      [ EXCLUDING ATTRIBUTES | INCLUDING [ ALL ] ATTRIBUTES ]
      [ AS JSON | AS XML | AS DOT ]
      FOR { query | insert | update | merge | delete }

describe:
      DESCRIBE DATABASE databaseName
  |   DESCRIBE CATALOG [ databaseName . ] catalogName
  |   DESCRIBE SCHEMA [ [ databaseName . ] catalogName ] . schemaName
  |   DESCRIBE [ TABLE ] [ [ [ databaseName . ] catalogName . ] schemaName . ] tableName [ columnName ]
  |   DESCRIBE [ STATEMENT ] { query | insert | update | merge | delete }

insert:
      { INSERT | UPSERT } INTO tablePrimary
      [ '(' column [, column ]* ')' ]
      query

update:
      UPDATE tablePrimary
      SET assign [, assign ]*
      [ WHERE booleanExpression ]

assign:
      identifier '=' expression

merge:
      MERGE INTO tablePrimary [ [ AS ] alias ]
      USING tablePrimary
      ON booleanExpression
      [ WHEN MATCHED THEN UPDATE SET assign [, assign ]* ]
      [ WHEN NOT MATCHED THEN INSERT VALUES '(' value [ , value ]* ')' ]

delete:
      DELETE FROM tablePrimary [ [ AS ] alias ]
      [ WHERE booleanExpression ]

query:
      values
  |   WITH [ RECURSIVE ] withItem [ , withItem ]* query
  |   {
          select
      |   selectWithoutFrom
      |   query UNION [ ALL | DISTINCT ] query
      |   query EXCEPT [ ALL | DISTINCT ] query
      |   query MINUS [ ALL | DISTINCT ] query
      |   query INTERSECT [ ALL | DISTINCT ] query
      }
      [ ORDER BY orderItem [, orderItem ]* ]
      [ LIMIT [ start, ] { count | ALL } ]
      [ OFFSET start { ROW | ROWS } ]
      [ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } ONLY ]

withItem:
      name
      [ '(' column [, column ]* ')' ]
      AS '(' query ')'

orderItem:
      expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ]

select:
      SELECT [ hintComment ] [ STREAM ] [ ALL | DISTINCT ]
          { * | projectItem [, projectItem ]* }
      FROM tableExpression
      [ WHERE booleanExpression ]
      [ GROUP BY [ ALL | DISTINCT ] { groupItem [, groupItem ]* } ]
      [ HAVING booleanExpression ]
      [ WINDOW windowName AS windowSpec [, windowName AS windowSpec ]* ]
      [ QUALIFY booleanExpression ]

selectWithoutFrom:
      SELECT [ ALL | DISTINCT ]
          { * | projectItem [, projectItem ]* }

projectItem:
      expression [ [ AS ] columnAlias ]
  |   tableAlias . *

tableExpression:
      tableReference [, tableReference ]*
  |   tableExpression [ NATURAL ] [ { LEFT | RIGHT | FULL } [ OUTER ] ] [ ASOF ] JOIN tableExpression [ joinCondition ]
  |   tableExpression CROSS JOIN tableExpression
  |   tableExpression [ CROSS | OUTER ] APPLY tableExpression

joinCondition:
      ON booleanExpression
  |   MATCH_CONDITION booleanExpression ON booleanExpression
  |   USING '(' column [, column ]* ')'

tableReference:
      tablePrimary
      [ FOR SYSTEM_TIME AS OF expression ]
      [ pivot ]
      [ unpivot ]
      [ matchRecognize ]
      [ [ AS ] alias [ '(' columnAlias [, columnAlias ]* ')' ] ]

tablePrimary:
      [ [ catalogName . ] schemaName . ] tableName
      '(' TABLE [ [ catalogName . ] schemaName . ] tableName ')'
  |   tablePrimary [ hintComment ] [ EXTEND ] '(' columnDecl [, columnDecl ]* ')'
  |   [ LATERAL ] '(' query ')'
  |   UNNEST '(' expression ')' [ WITH ORDINALITY ]
  |   [ LATERAL ] TABLE '(' [ SPECIFIC ] functionName '(' expression [, expression ]* ')' ')'

columnDecl:
      column type [ NOT NULL ]

hint:
      hintName
  |   hintName '(' hintOptions ')'

hintOptions:
      hintKVOption [, hintKVOption ]*
  |   optionName [, optionName ]*
  |   optionValue [, optionValue ]*

hintKVOption:
      optionName '=' stringLiteral
  |   stringLiteral '=' stringLiteral

optionValue:
      stringLiteral
  |   numericLiteral

columnOrList:
      column
  |   '(' column [, column ]* ')'

exprOrList:
      expr
  |   '(' expr [, expr ]* ')'

pivot:
      PIVOT '('
      pivotAgg [, pivotAgg ]*
      FOR pivotList
      IN '(' pivotExpr [, pivotExpr ]* ')'
      ')'

pivotAgg:
      agg '(' [ ALL | DISTINCT ] value [, value ]* ')'
      [ [ AS ] alias ]

pivotList:
      columnOrList

pivotExpr:
      exprOrList [ [ AS ] alias ]

unpivot:
      UNPIVOT [ INCLUDING NULLS | EXCLUDING NULLS ] '('
      unpivotMeasureList
      FOR unpivotAxisList
      IN '(' unpivotValue [, unpivotValue ]* ')'
      ')'

unpivotMeasureList:
      columnOrList

unpivotAxisList:
      columnOrList

unpivotValue:
      column [ AS literal ]
  |   '(' column [, column ]* ')' [ AS '(' literal [, literal ]* ')' ]

values:
      { VALUES | VALUE } expression [, expression ]*

groupItem:
      expression
  |   '(' ')'
  |   '(' expression [, expression ]* ')'
  |   CUBE '(' expression [, expression ]* ')'
  |   ROLLUP '(' expression [, expression ]* ')'
  |   GROUPING SETS '(' groupItem [, groupItem ]* ')'

window:
      windowName
  |   windowSpec

windowSpec:
      '('
      [ windowName ]
      [ ORDER BY orderItem [, orderItem ]* ]
      [ PARTITION BY expression [, expression ]* ]
      [\
          RANGE numericOrIntervalExpression { PRECEDING | FOLLOWING [exclude]}\
      |   ROWS numericExpression { PRECEDING | FOLLOWING [exclude] }\
      ]
      ')'

exclude:
      EXCLUDE NO OTHERS
  |   EXCLUDE CURRENT ROW
  |   EXCLUDE GROUP
  |   EXCLUDE TIES
```

In _insert_, if the INSERT or UPSERT statement does not specify a
list of target columns, the query must have the same number of
columns as the target table, except in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isInsertSubsetColumnsAllowed--).

In _merge_, at least one of the WHEN MATCHED and WHEN NOT MATCHED clauses must
be present.

_tablePrimary_ may only contain an EXTEND clause in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#allowExtend--);
in those same conformance levels, any _column_ in _insert_ may be replaced by
_columnDecl_, which has a similar effect to including it in an EXTEND clause.

In _orderItem_, if _expression_ is a positive integer _n_, it denotes
the _n_ th item in the SELECT clause.

In _query_, _count_ and _start_ may each be either an unsigned integer literal
or a dynamic parameter whose value is an integer.

An aggregate query is a query that contains a GROUP BY or a HAVING
clause, or aggregate functions in the SELECT clause. In the SELECT,
HAVING and ORDER BY clauses of an aggregate query, all expressions
must be constant within the current group (that is, grouping constants
as defined by the GROUP BY clause, or constants), or aggregate
functions, or a combination of constants and aggregate
functions. Aggregate and grouping functions may only appear in an
aggregate query, and only in a SELECT, HAVING or ORDER BY clause.

A scalar sub-query is a sub-query used as an expression.
If the sub-query returns no rows, the value is NULL; if it
returns more than one row, it is an error.

IN, EXISTS, UNIQUE and scalar sub-queries can occur
in any place where an expression can occur (such as the SELECT clause,
WHERE clause, ON clause of a JOIN, or as an argument to an aggregate
function).

An IN, EXISTS, UNIQUE or scalar sub-query may be correlated; that is, it
may refer to tables in the FROM clause of an enclosing query.

GROUP BY DISTINCT removes duplicate grouping sets (for example,
“GROUP BY DISTINCT GROUPING SETS ((a), (a, b), (a))” is equivalent to
“GROUP BY GROUPING SETS ((a), (a, b))”);
GROUP BY ALL is equivalent to GROUP BY.

_selectWithoutFrom_ is equivalent to VALUES,
but is not standard SQL and is only allowed in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isFromRequired--).

MINUS is equivalent to EXCEPT,
but is not standard SQL and is only allowed in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isMinusAllowed--).

CROSS APPLY and OUTER APPLY are only allowed in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isApplyAllowed--).

“LIMIT start, count” is equivalent to “LIMIT count OFFSET start”
but is only allowed in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isLimitStartCountAllowed--).

“OFFSET start” may occur before “LIMIT count” in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isOffsetLimitAllowed--).

VALUE is equivalent to VALUES,
but is not standard SQL and is only allowed in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isValueAllowed--).

An “ASOF JOIN” operation combines rows from two tables based on
comparable timestamp values. For each row in the left table, the join
finds at most a single row in the right table that has the “closest”
timestamp value. The matched row on the right side is the closest
match whose timestamp column is compared using one of the operations
<, ≤, >, or ≥, as specified by the comparison operator in
the MATCH\_CONDITION clause. The comparison is performed using SQL
semantics, which returns ‘false’ when comparing ‘NULL’ values with any
other values. Thus a ‘NULL’ timestamp in the left table will not
match any timestamps in the right table.

ASOF JOIN can be used in an OUTER JOIN form as LEFT ASOF JOIN. In this case,
when there is no match for a row in the left table, the columns from
the right table are null-padded. There are no RIGHT ASOF joins.

Example:

```sql
SELECT *
FROM left_table LEFT ASOF JOIN right_table
MATCH_CONDITION left_table.timecol <= right_table.timecol
ON left_table.col = right_table.col
```

## Keywords [Permalink](https://calcite.apache.org/docs/reference.html\#keywords "Permalink")

The following is a list of SQL keywords.
Reserved keywords are **bold**.

A,
**ABS**,
ABSENT,
ABSOLUTE,
ACTION,
ADA,
ADD,
ADMIN,
AFTER,
**ALL**,
**ALLOCATE**,
**ALLOW**,
**ALTER**,
ALWAYS,
**AND**,
**ANY**,
APPLY,
**ARE**,
**ARRAY**,
ARRAY\_AGG,
ARRAY\_CONCAT\_AGG,
**ARRAY\_MAX\_CARDINALITY**,
**AS**,
ASC,
**ASENSITIVE**,
**ASOF**,
ASSERTION,
ASSIGNMENT,
**ASYMMETRIC**,
**AT**,
**ATOMIC**,
ATTRIBUTE,
ATTRIBUTES,
**AUTHORIZATION**,
**AVG**,
BEFORE,
**BEGIN**,
**BEGIN\_FRAME**,
**BEGIN\_PARTITION**,
BERNOULLI,
**BETWEEN**,
**BIGINT**,
**BINARY**,
**BIT**,
**BLOB**,
**BOOLEAN**,
**BOTH**,
BREADTH,
**BY**,
C,
**CALL**,
**CALLED**,
**CARDINALITY**,
CASCADE,
**CASCADED**,
**CASE**,
**CAST**,
CATALOG,
CATALOG\_NAME,
**CEIL**,
**CEILING**,
CENTURY,
CHAIN,
**CHAR**,
**CHARACTER**,
CHARACTERISTICS,
CHARACTERS,
**CHARACTER\_LENGTH**,
CHARACTER\_SET\_CATALOG,
CHARACTER\_SET\_NAME,
CHARACTER\_SET\_SCHEMA,
**CHAR\_LENGTH**,
**CHECK**,
**CLASSIFIER**,
CLASS\_ORIGIN,
**CLOB**,
**CLOSE**,
**COALESCE**,
COBOL,
**COLLATE**,
COLLATION,
COLLATION\_CATALOG,
COLLATION\_NAME,
COLLATION\_SCHEMA,
**COLLECT**,
**COLUMN**,
COLUMN\_NAME,
COMMAND\_FUNCTION,
COMMAND\_FUNCTION\_CODE,
**COMMIT**,
COMMITTED,
**CONDITION**,
CONDITIONAL,
CONDITION\_NUMBER,
**CONNECT**,
CONNECTION,
CONNECTION\_NAME,
**CONSTRAINT**,
CONSTRAINTS,
CONSTRAINT\_CATALOG,
CONSTRAINT\_NAME,
CONSTRAINT\_SCHEMA,
CONSTRUCTOR,
**CONTAINS**,
CONTAINS\_SUBSTR,
CONTINUE,
**CONVERT**,
**CORR**,
**CORRESPONDING**,
**COUNT**,
**COVAR\_POP**,
**COVAR\_SAMP**,
**CREATE**,
**CROSS**,
**CUBE**,
**CUME\_DIST**,
**CURRENT**,
**CURRENT\_CATALOG**,
**CURRENT\_DATE**,
**CURRENT\_DEFAULT\_TRANSFORM\_GROUP**,
**CURRENT\_PATH**,
**CURRENT\_ROLE**,
**CURRENT\_ROW**,
**CURRENT\_SCHEMA**,
**CURRENT\_TIME**,
**CURRENT\_TIMESTAMP**,
**CURRENT\_TRANSFORM\_GROUP\_FOR\_TYPE**,
**CURRENT\_USER**,
**CURSOR**,
CURSOR\_NAME,
**CYCLE**,
DATA,
DATABASE,
**DATE**,
**DATETIME**,
DATETIME\_DIFF,
DATETIME\_INTERVAL\_CODE,
DATETIME\_INTERVAL\_PRECISION,
DATETIME\_TRUNC,
DATE\_DIFF,
DATE\_TRUNC,
**DAY**,
DAYOFWEEK,
DAYOFYEAR,
DAYS,
**DEALLOCATE**,
**DEC**,
DECADE,
**DECIMAL**,
**DECLARE**,
**DEFAULT**,
DEFAULTS,
DEFERRABLE,
DEFERRED,
**DEFINE**,
DEFINED,
DEFINER,
DEGREE,
**DELETE**,
**DENSE\_RANK**,
DEPTH,
**DEREF**,
DERIVED,
DESC,
**DESCRIBE**,
DESCRIPTION,
DESCRIPTOR,
**DETERMINISTIC**,
DIAGNOSTICS,
**DISALLOW**,
**DISCONNECT**,
DISPATCH,
**DISTINCT**,
DOMAIN,
DOT,
**DOUBLE**,
DOW,
DOY,
**DROP**,
**DYNAMIC**,
DYNAMIC\_FUNCTION,
DYNAMIC\_FUNCTION\_CODE,
**EACH**,
**ELEMENT**,
**ELSE**,
**EMPTY**,
ENCODING,
**END**,
**END-EXEC**,
**END\_FRAME**,
**END\_PARTITION**,
EPOCH,
**EQUALS**,
ERROR,
**ESCAPE**,
**EVERY**,
**EXCEPT**,
EXCEPTION,
EXCLUDE,
EXCLUDING,
**EXEC**,
**EXECUTE**,
**EXISTS**,
**EXP**,
**EXPLAIN**,
**EXTEND**,
**EXTERNAL**,
**EXTRACT**,
**FALSE**,
**FETCH**,
**FILTER**,
FINAL,
FIRST,
**FIRST\_VALUE**,
**FLOAT**,
**FLOOR**,
FOLLOWING,
**FOR**,
**FOREIGN**,
FORMAT,
FORTRAN,
FOUND,
FRAC\_SECOND,
**FRAME\_ROW**,
**FREE**,
**FRIDAY**,
**FROM**,
**FULL**,
**FUNCTION**,
**FUSION**,
G,
GENERAL,
GENERATED,
GEOMETRY,
**GET**,
**GLOBAL**,
GO,
GOTO,
**GRANT**,
GRANTED,
**GROUP**,
**GROUPING**,
**GROUPS**,
GROUP\_CONCAT,
**HAVING**,
HIERARCHY,
**HOLD**,
HOP,
**HOUR**,
HOURS,
**IDENTITY**,
IGNORE,
ILIKE,
IMMEDIATE,
IMMEDIATELY,
IMPLEMENTATION,
**IMPORT**,
**IN**,
INCLUDE,
INCLUDING,
INCREMENT,
**INDICATOR**,
**INITIAL**,
INITIALLY,
**INNER**,
**INOUT**,
INPUT,
**INSENSITIVE**,
**INSERT**,
INSTANCE,
INSTANTIABLE,
**INT**,
**INTEGER**,
**INTERSECT**,
**INTERSECTION**,
**INTERVAL**,
**INTO**,
INVOKER,
**IS**,
ISODOW,
ISOLATION,
ISOYEAR,
JAVA,
**JOIN**,
JSON,
**JSON\_ARRAY**,
**JSON\_ARRAYAGG**,
**JSON\_EXISTS**,
**JSON\_OBJECT**,
**JSON\_OBJECTAGG**,
**JSON\_QUERY**,
**JSON\_SCOPE**,
**JSON\_VALUE**,
K,
KEY,
KEY\_MEMBER,
KEY\_TYPE,
LABEL,
**LAG**,
**LANGUAGE**,
**LARGE**,
LAST,
**LAST\_VALUE**,
**LATERAL**,
**LEAD**,
**LEADING**,
**LEFT**,
LENGTH,
LEVEL,
LIBRARY,
**LIKE**,
**LIKE\_REGEX**,
**LIMIT**,
**LN**,
**LOCAL**,
**LOCALTIME**,
**LOCALTIMESTAMP**,
LOCATOR,
**LOWER**,
M,
MAP,
**MATCH**,
MATCHED,
**MATCHES**,
**MATCH\_CONDITION**,
**MATCH\_NUMBER**,
**MATCH\_RECOGNIZE**,
**MAX**,
MAXVALUE,
**MEASURE**,
**MEASURES**,
**MEMBER**,
**MERGE**,
MESSAGE\_LENGTH,
MESSAGE\_OCTET\_LENGTH,
MESSAGE\_TEXT,
**METHOD**,
MICROSECOND,
MILLENNIUM,
MILLISECOND,
**MIN**,
**MINUS**,
**MINUTE**,
MINUTES,
MINVALUE,
**MOD**,
**MODIFIES**,
**MODULE**,
**MONDAY**,
**MONTH**,
MONTHS,
MORE,
**MULTISET**,
MUMPS,
NAME,
NAMES,
NANOSECOND,
**NATIONAL**,
**NATURAL**,
**NCHAR**,
**NCLOB**,
NESTING,
**NEW**,
**NEXT**,
**NO**,
**NONE**,
**NORMALIZE**,
NORMALIZED,
**NOT**,
**NTH\_VALUE**,
**NTILE**,
**NULL**,
NULLABLE,
**NULLIF**,
NULLS,
NUMBER,
**NUMERIC**,
OBJECT,
**OCCURRENCES\_REGEX**,
OCTETS,
**OCTET\_LENGTH**,
**OF**,
**OFFSET**,
**OLD**,
**OMIT**,
**ON**,
**ONE**,
**ONLY**,
**OPEN**,
OPTION,
OPTIONS,
**OR**,
**ORDER**,
ORDERING,
**ORDINAL**,
ORDINALITY,
OTHERS,
**OUT**,
**OUTER**,
OUTPUT,
**OVER**,
**OVERLAPS**,
**OVERLAY**,
OVERRIDING,
PAD,
**PARAMETER**,
PARAMETER\_MODE,
PARAMETER\_NAME,
PARAMETER\_ORDINAL\_POSITION,
PARAMETER\_SPECIFIC\_CATALOG,
PARAMETER\_SPECIFIC\_NAME,
PARAMETER\_SPECIFIC\_SCHEMA,
PARTIAL,
**PARTITION**,
PASCAL,
PASSING,
PASSTHROUGH,
PAST,
PATH,
**PATTERN**,
**PER**,
**PERCENT**,
**PERCENTILE\_CONT**,
**PERCENTILE\_DISC**,
**PERCENT\_RANK**,
**PERIOD**,
**PERMUTE**,
PIVOT,
PLACING,
PLAN,
PLI,
**PORTION**,
**POSITION**,
**POSITION\_REGEX**,
**POWER**,
**PRECEDES**,
PRECEDING,
**PRECISION**,
**PREPARE**,
PRESERVE,
**PREV**,
**PRIMARY**,
PRIOR,
PRIVILEGES,
**PROCEDURE**,
PUBLIC,
**QUALIFY**,
QUARTER,
QUARTERS,
**RANGE**,
**RANK**,
READ,
**READS**,
**REAL**,
**RECURSIVE**,
**REF**,
**REFERENCES**,
**REFERENCING**,
**REGR\_AVGX**,
**REGR\_AVGY**,
**REGR\_COUNT**,
**REGR\_INTERCEPT**,
**REGR\_R2**,
**REGR\_SLOPE**,
**REGR\_SXX**,
**REGR\_SXY**,
**REGR\_SYY**,
RELATIVE,
**RELEASE**,
REPEATABLE,
REPLACE,
**RESET**,
RESPECT,
RESTART,
RESTRICT,
**RESULT**,
**RETURN**,
RETURNED\_CARDINALITY,
RETURNED\_LENGTH,
RETURNED\_OCTET\_LENGTH,
RETURNED\_SQLSTATE,
RETURNING,
**RETURNS**,
**REVOKE**,
**RIGHT**,
RLIKE,
ROLE,
**ROLLBACK**,
**ROLLUP**,
ROUTINE,
ROUTINE\_CATALOG,
ROUTINE\_NAME,
ROUTINE\_SCHEMA,
**ROW**,
**ROWS**,
ROW\_COUNT,
**ROW\_NUMBER**,
**RUNNING**,
**SAFE\_CAST**,
**SAFE\_OFFSET**,
**SAFE\_ORDINAL**,
**SATURDAY**,
**SAVEPOINT**,
SCALAR,
SCALE,
SCHEMA,
SCHEMA\_NAME,
**SCOPE**,
SCOPE\_CATALOGS,
SCOPE\_NAME,
SCOPE\_SCHEMA,
**SCROLL**,
**SEARCH**,
**SECOND**,
SECONDS,
SECTION,
SECURITY,
**SEEK**,
**SELECT**,
SELF,
**SENSITIVE**,
SEPARATOR,
SEQUENCE,
SERIALIZABLE,
SERVER,
SERVER\_NAME,
SESSION,
**SESSION\_USER**,
**SET**,
SETS,
**SHOW**,
**SIMILAR**,
SIMPLE,
SIZE,
**SKIP**,
**SMALLINT**,
**SOME**,
SOURCE,
SPACE,
**SPECIFIC**,
**SPECIFICTYPE**,
SPECIFIC\_NAME,
**SQL**,
**SQLEXCEPTION**,
**SQLSTATE**,
**SQLWARNING**,
SQL\_BIGINT,
SQL\_BINARY,
SQL\_BIT,
SQL\_BLOB,
SQL\_BOOLEAN,
SQL\_CHAR,
SQL\_CLOB,
SQL\_DATE,
SQL\_DECIMAL,
SQL\_DOUBLE,
SQL\_FLOAT,
SQL\_INTEGER,
SQL\_INTERVAL\_DAY,
SQL\_INTERVAL\_DAY\_TO\_HOUR,
SQL\_INTERVAL\_DAY\_TO\_MINUTE,
SQL\_INTERVAL\_DAY\_TO\_SECOND,
SQL\_INTERVAL\_HOUR,
SQL\_INTERVAL\_HOUR\_TO\_MINUTE,
SQL\_INTERVAL\_HOUR\_TO\_SECOND,
SQL\_INTERVAL\_MINUTE,
SQL\_INTERVAL\_MINUTE\_TO\_SECOND,
SQL\_INTERVAL\_MONTH,
SQL\_INTERVAL\_SECOND,
SQL\_INTERVAL\_YEAR,
SQL\_INTERVAL\_YEAR\_TO\_MONTH,
SQL\_LONGVARBINARY,
SQL\_LONGVARCHAR,
SQL\_LONGVARNCHAR,
SQL\_NCHAR,
SQL\_NCLOB,
SQL\_NUMERIC,
SQL\_NVARCHAR,
SQL\_REAL,
SQL\_SMALLINT,
SQL\_TIME,
SQL\_TIMESTAMP,
SQL\_TINYINT,
SQL\_TSI\_DAY,
SQL\_TSI\_FRAC\_SECOND,
SQL\_TSI\_HOUR,
SQL\_TSI\_MICROSECOND,
SQL\_TSI\_MINUTE,
SQL\_TSI\_MONTH,
SQL\_TSI\_QUARTER,
SQL\_TSI\_SECOND,
SQL\_TSI\_WEEK,
SQL\_TSI\_YEAR,
SQL\_VARBINARY,
SQL\_VARCHAR,
**SQRT**,
**START**,
STATE,
STATEMENT,
**STATIC**,
**STDDEV\_POP**,
**STDDEV\_SAMP**,
**STREAM**,
STRING\_AGG,
STRUCTURE,
STYLE,
SUBCLASS\_ORIGIN,
**SUBMULTISET**,
**SUBSET**,
SUBSTITUTE,
**SUBSTRING**,
**SUBSTRING\_REGEX**,
**SUCCEEDS**,
**SUM**,
**SUNDAY**,
**SYMMETRIC**,
**SYSTEM**,
**SYSTEM\_TIME**,
**SYSTEM\_USER**,
**TABLE**,
**TABLESAMPLE**,
TABLE\_NAME,
TEMPORARY,
**THEN**,
**THURSDAY**,
TIES,
**TIME**,
**TIMESTAMP**,
TIMESTAMPADD,
TIMESTAMPDIFF,
TIMESTAMP\_DIFF,
TIMESTAMP\_TRUNC,
**TIMEZONE\_HOUR**,
**TIMEZONE\_MINUTE**,
TIME\_DIFF,
TIME\_TRUNC,
**TINYINT**,
**TO**,
TOP\_LEVEL\_COUNT,
**TRAILING**,
TRANSACTION,
TRANSACTIONS\_ACTIVE,
TRANSACTIONS\_COMMITTED,
TRANSACTIONS\_ROLLED\_BACK,
TRANSFORM,
TRANSFORMS,
**TRANSLATE**,
**TRANSLATE\_REGEX**,
**TRANSLATION**,
**TREAT**,
**TRIGGER**,
TRIGGER\_CATALOG,
TRIGGER\_NAME,
TRIGGER\_SCHEMA,
**TRIM**,
**TRIM\_ARRAY**,
**TRUE**,
**TRUNCATE**,
**TRY\_CAST**,
**TUESDAY**,
TUMBLE,
TYPE,
**UESCAPE**,
UNBOUNDED,
UNCOMMITTED,
UNCONDITIONAL,
UNDER,
**UNION**,
**UNIQUE**,
**UNKNOWN**,
UNNAMED,
**UNNEST**,
UNPIVOT,
**UNSIGNED**,
**UPDATE**,
**UPPER**,
**UPSERT**,
USAGE,
**USER**,
USER\_DEFINED\_TYPE\_CATALOG,
USER\_DEFINED\_TYPE\_CODE,
USER\_DEFINED\_TYPE\_NAME,
USER\_DEFINED\_TYPE\_SCHEMA,
**USING**,
UTF16,
UTF32,
UTF8,
**UUID**,
**VALUE**,
**VALUES**,
**VALUE\_OF**,
**VARBINARY**,
**VARCHAR**,
**VARIANT**,
**VARYING**,
**VAR\_POP**,
**VAR\_SAMP**,
VERSION,
**VERSIONING**,
VIEW,
**WEDNESDAY**,
WEEK,
WEEKS,
**WHEN**,
**WHENEVER**,
**WHERE**,
**WIDTH\_BUCKET**,
**WINDOW**,
**WITH**,
**WITHIN**,
**WITHOUT**,
WORK,
WRAPPER,
WRITE,
XML,
**YEAR**,
YEARS,
ZONE.

## Identifiers [Permalink](https://calcite.apache.org/docs/reference.html\#identifiers "Permalink")

Identifiers are the names of tables, columns and other metadata
elements used in a SQL query.

Unquoted identifiers, such as emp, must start with a letter and can
only contain letters, digits, and underscores. They are implicitly
converted to upper case.

Quoted identifiers, such as `"Employee Name"`, start and end with
double quotes. They may contain virtually any character, including
spaces and other punctuation. If you wish to include a double quote
in an identifier, use another double quote to escape it, like this:
`"An employee called ""Fred""."`.

In Calcite, matching identifiers to the name of the referenced object is
case-sensitive. But remember that unquoted identifiers are implicitly
converted to upper case before matching, and if the object it refers
to was created using an unquoted identifier for its name, then its
name will have been converted to upper case also.

## Data types [Permalink](https://calcite.apache.org/docs/reference.html\#data-types "Permalink")

### Scalar types [Permalink](https://calcite.apache.org/docs/reference.html\#scalar-types "Permalink")

| Data type | Description | Range and example literals |
| --- | --- | --- |
| BOOLEAN | Logical values | Values: TRUE, FALSE, UNKNOWN |
| TINYINT | 1 byte signed integer | Range is -128 to 127 |
| SMALLINT | 2 byte signed integer | Range is -32768 to 32767 |
| INTEGER, INT | 4 byte signed integer | Range is -2147483648 to 2147483647 |
| BIGINT | 8 byte signed integer | Range is -9223372036854775808 to 9223372036854775807 |
| TINYINT UNSIGNED | 1 byte unsigned integer | Range is 0 to 255 |
| SMALLINT UNSIGNED | 2 byte unsigned integer | Range is 0 to 65535 |
| INTEGER UNSIGNED, INT UNSIGNED | 4 byte unsigned integer | Range is 0 to 4294967295 |
| BIGINT UNSIGNED | 8 byte unsigned integer | Range is 0 to 18446744073709551615 |
| DECIMAL(p, s) | Fixed point | Example: 123.45 and DECIMAL ‘123.45’ are identical values, and have type DECIMAL(5, 2) |
| NUMERIC(p, s) | Fixed point | A synonym for DECIMAL |
| REAL | 4 byte floating point | 6 decimal digits precision; examples: CAST(1.2 AS REAL), CAST(‘Infinity’ AS REAL) |
| DOUBLE | 8 byte floating point | 15 decimal digits precision; examples: 1.4E2, CAST(‘-Infinity’ AS DOUBLE), CAST(‘NaN’ AS DOUBLE) |
| FLOAT | 8 byte floating point | A synonym for DOUBLE |
| CHAR(n), CHARACTER(n) | Fixed-width character string | ‘Hello’, ‘’ (empty string), \_latin1’Hello’, n’Hello’, \_UTF16’Hello’, ‘Hello’ ‘there’ (literal split into multiple parts), e’Hello\\nthere’ (literal containing C-style escapes) |
| VARCHAR(n), CHARACTER VARYING(n) | Variable-length character string | As CHAR(n) |
| BINARY(n) | Fixed-width binary string | x’45F0AB’, x’’ (empty binary string), x’AB’ ‘CD’ (multi-part binary string literal) |
| VARBINARY(n), BINARY VARYING(n) | Variable-length binary string | As BINARY(n) |
| DATE | Date | Example: DATE ‘1969-07-20’ |
| TIME | Time of day | Example: TIME ‘20:17:40’ |
| TIME WITH LOCAL TIME ZONE | Time of day with local time zone | Example: TIME WITH LOCAL TIME ZONE ‘20:17:40’ |
| TIME WITH TIME ZONE | Time of day with time zone | Example: TIME ‘20:17:40 GMT+08’ |
| TIMESTAMP \[ WITHOUT TIME ZONE \] | Date and time | Example: TIMESTAMP ‘1969-07-20 20:17:40’ |
| TIMESTAMP WITH LOCAL TIME ZONE | Date and time with local time zone | Example: TIMESTAMP WITH LOCAL TIME ZONE ‘1969-07-20 20:17:40’ |
| TIMESTAMP WITH TIME ZONE | Date and time with time zone | Example: TIMESTAMP WITH TIME ZONE ‘1969-07-20 20:17:40 America/Los Angeles’ |
| UUID | An 128-bit UUID | Example: UUID ‘123e4567-e89b-12d3-a456-426655440000’ |
| INTERVAL timeUnit \[ TO timeUnit \] | Date time interval | Examples: INTERVAL ‘1-5’ YEAR TO MONTH, INTERVAL ‘45’ DAY, INTERVAL ‘1 2:34:56.789’ DAY TO SECOND |
| GEOMETRY | Geometry | Examples: ST\_GeomFromText(‘POINT (30 10)’) |

Where:

```sql
timeUnit:
  MILLENNIUM | CENTURY | DECADE | YEAR | QUARTER | MONTH | WEEK | DOY | DOW | DAY | HOUR | MINUTE | SECOND | EPOCH
```

Note:

- DATE, TIME and TIMESTAMP have no time zone. For those types, there is not
even an implicit time zone, such as UTC (as in Java) or the local time zone.
It is left to the user or application to supply a time zone. In turn,
TIMESTAMP WITH LOCAL TIME ZONE does not store the time zone internally, but
it will rely on the supplied time zone to provide correct semantics.
- GEOMETRY is allowed only in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#allowGeometry--).
- Interval literals may only use time units
YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE and SECOND. In certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#allowPluralTimeUnits--),
we also allow their plurals, YEARS, QUARTERS, MONTHS, WEEKS, DAYS, HOURS, MINUTES and SECONDS.

### Non-scalar types [Permalink](https://calcite.apache.org/docs/reference.html\#non-scalar-types "Permalink")

| Type | Description | Example type |
| --- | --- | --- |
| ANY | The union of all types |  |
| UNKNOWN | A value of an unknown type; used as a placeholder |  |
| ROW | Row with 1 or more columns | Example: row(f0 int null, f1 varchar) |
| MAP | Collection of keys mapped to values | Example: map < int, varchar > |
| MULTISET | Unordered collection that may contain duplicates | Example: int multiset |
| ARRAY | Ordered, contiguous collection that may contain duplicates | Example: varchar(10) array |
| CURSOR | Cursor over the result of executing a query |  |
| FUNCTION | A function definition that is not bound to an identifier, it is not fully supported in CAST or DDL | Example FUNCTION(INTEGER, VARCHAR(30)) -> INTEGER |
| VARIANT | Dynamically-typed value that can have at runtime a value of any other type | VARIANT |

Note:

- Every `ROW` column type can have an optional \[ NULL \| NOT NULL \] suffix
to indicate if this column type is nullable, default is not nullable.

### The `VARIANT` type [Permalink](https://calcite.apache.org/docs/reference.html\#the-variant-type "Permalink")

Values of `VARIANT` type are dynamically-typed.
Any such value holds at runtime two pieces of information:

- the data type
- the data value

Values of `VARIANT` type can be created by casting any other value to a `VARIANT`: e.g.
`SELECT CAST(x AS VARIANT)`. Conversely, values of type `VARIANT` can be cast to any other data type
`SELECT CAST(variant AS INT)`. A cast of a value of type `VARIANT` to target type T
will compare the runtime type with T. If the types are identical or the types are
numeric and there is a natural conversion between the two types, the
original value is converted to the target type and returned. Otherwise the `CAST` returns `NULL`.

Values of type `ARRAY`, `MAP`, and `ROW` type can be cast to `VARIANT`. `VARIANT` values
also offer the following operations:

- indexing using array indexing notation `variant[index]`. If the `VARIANT` is
obtained from an `ARRAY` value, the indexing operation returns a `VARIANT` whose value element
is the element at the specified index. Otherwise, this operation returns `NULL`
- indexing using map element access notation `variant[key]`, where `key` can have
any legal `MAP` key type. If the `VARIANT` is obtained from a `MAP` value
that has en element with this key, a `VARIANT` value holding the associated value in
the `MAP` is returned. Otherwise `NULL` is returned. If the `VARIANT` is obtained from `ROW` value
which has a field with the name `key`, this operation returns a `VARIANT` value holding
the corresponding field value. Otherwise `NULL` is returned.
- field access using the dot notation: `variant.field`. This operation is interpreted
as equivalent to `variant['field']`. Note, however, that the field notation
is subject to the capitalization rules of the SQL dialect, so for correct
operation the field may need to be quoted: `variant."field"`

The runtime types do not need to match exactly the compile-time types.
As a compiler front-end, Calcite does not mandate exactly how the runtime types
are represented. Calcite does include one particular implementation in
Java runtime, which is used for testing. In this representation
the runtime types are represented as follows:

- The scalar types do not include information about precision and scale. Thus all `DECIMAL`
compile-time types are represented by a single run-time type.
- `CHAR(N)` and `VARCHAR` are both represented by a single runtime `VARCHAR` type.
- `BINARY(N)` and `VARBINARY` are both represented by a single runtime `VARBINARY` type.
- `FLOAT` and `DOUBLE` are both represented by the same runtime type.
- All “short interval” types (from days to seconds) are represented by a single type.
- All “long interval” types (from years to months) are represented by a single type.
- Generic types such as `INT ARRAY`, `MULTISET`, and `MAP` convert all their elements to VARIANT values

The function VARIANTNULL() can be used to create an instance
of the `VARIANT``null` value.

### Spatial types [Permalink](https://calcite.apache.org/docs/reference.html\#spatial-types "Permalink")

Spatial data is represented as character strings encoded as
[well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text)
or binary strings encoded as
[well-known binary (WKB)](https://en.wikipedia.org/wiki/Well-known_binary).

Where you would use a literal, apply the `ST_GeomFromText` function,
for example `ST_GeomFromText('POINT (30 10)')`.

| Data type | Type code | Examples in WKT |
| --- | --- | --- |
| GEOMETRY | 0 | generalization of Point, Curve, Surface, GEOMETRYCOLLECTION |
| POINT | 1 | `ST_GeomFromText(​'POINT (30 10)')` is a point in 2D space; `ST_GeomFromText(​'POINT Z(30 10 2)')` is point in 3D space |
| CURVE | 13 | generalization of LINESTRING |
| LINESTRING | 2 | `ST_GeomFromText(​'LINESTRING (30 10, 10 30, 40 40)')` |
| SURFACE | 14 | generalization of Polygon, PolyhedralSurface |
| POLYGON | 3 | `ST_GeomFromText(​'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))')` is a pentagon; `ST_GeomFromText(​'POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10), (20 30, 35 35, 30 20, 20 30))')` is a pentagon with a quadrilateral hole |
| POLYHEDRALSURFACE | 15 |  |
| GEOMETRYCOLLECTION | 7 | a collection of zero or more GEOMETRY instances; a generalization of MULTIPOINT, MULTILINESTRING, MULTIPOLYGON |
| MULTIPOINT | 4 | `ST_GeomFromText(​'MULTIPOINT ((10 40), (40 30), (20 20), (30 10))')` is equivalent to `ST_GeomFromText(​'MULTIPOINT (10 40, 40 30, 20 20, 30 10)')` |
| MULTICURVE | - | generalization of MULTILINESTRING |
| MULTILINESTRING | 5 | `ST_GeomFromText(​'MULTILINESTRING ((10 10, 20 20, 10 40), (40 40, 30 30, 40 20, 30 10))')` |
| MULTISURFACE | - | generalization of MULTIPOLYGON |
| MULTIPOLYGON | 6 | `ST_GeomFromText(​'MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)), ((15 5, 40 10, 10 20, 5 10, 15 5)))')` |

## Operators and functions [Permalink](https://calcite.apache.org/docs/reference.html\#operators-and-functions "Permalink")

### Operator precedence [Permalink](https://calcite.apache.org/docs/reference.html\#operator-precedence "Permalink")

The operator precedence and associativity, highest to lowest.

| Operator | Associativity |
| --- | --- |
| . | left |
| :: | left |
| \[ \] (collection element) | left |
| \+ \- (unary plus, minus) | right |
| \\* / % \|\| | left |
| \+ - | left |
| BETWEEN, IN, LIKE, SIMILAR, OVERLAPS, CONTAINS etc. | - |
| < > = <= >= <\> != <=> | left |
| IS NULL, IS FALSE, IS NOT TRUE etc. | - |
| NOT | right |
| AND | left |
| OR | left |

Note that `::`,`<=>` is dialect-specific, but is shown in this table for
completeness.

### Comparison operators [Permalink](https://calcite.apache.org/docs/reference.html\#comparison-operators "Permalink")

| Operator syntax | Description |
| --- | --- |
| value1 = value2 | Equals |
| value1 <> value2 | Not equal |
| value1 != value2 | Not equal (only in certain [conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isBangEqualAllowed--)) |
| value1 > value2 | Greater than |
| value1 >= value2 | Greater than or equal |
| value1 < value2 | Less than |
| value1 <= value2 | Less than or equal |
| value1 <=> value2 | Whether two values are equal, treating null values as the same |
| value IS NULL | Whether _value_ is null |
| value IS NOT NULL | Whether _value_ is not null |
| value1 IS DISTINCT FROM value2 | Whether two values are not equal, treating null values as the same |
| value1 IS NOT DISTINCT FROM value2 | Whether two values are equal, treating null values as the same |
| value1 BETWEEN value2 AND value3 | Whether _value1_ is greater than or equal to _value2_ and less than or equal to _value3_ |
| value1 NOT BETWEEN value2 AND value3 | Whether _value1_ is less than _value2_ or greater than _value3_ |
| string1 LIKE string2 \[ ESCAPE string3 \] | Whether _string1_ matches pattern _string2_ |
| string1 NOT LIKE string2 \[ ESCAPE string3 \] | Whether _string1_ does not match pattern _string2_ |
| string1 SIMILAR TO string2 \[ ESCAPE string3 \] | Whether _string1_ matches regular expression _string2_ |
| string1 NOT SIMILAR TO string2 \[ ESCAPE string3 \] | Whether _string1_ does not match regular expression _string2_ |
| value IN (value \[, value \]\*) | Whether _value_ is equal to a value in a list |
| value NOT IN (value \[, value \]\*) | Whether _value_ is not equal to every value in a list |
| value IN (sub-query) | Whether _value_ is equal to a row returned by _sub-query_ |
| value NOT IN (sub-query) | Whether _value_ is not equal to every row returned by _sub-query_ |
| value comparison SOME (sub-query or collection) | Whether _value_ _comparison_ at least one row returned by _sub-query_ or _collection_ |
| value comparison ANY (sub-query or collection) | Synonym for `SOME` |
| value comparison ALL (sub-query or collection) | Whether _value_ _comparison_ every row returned by _sub-query_ or _collection_ |
| EXISTS (sub-query) | Whether _sub-query_ returns at least one row |
| UNIQUE (sub-query) | Whether the rows returned by _sub-query_ are unique (ignoring null values) |

```sql
comp:
      =
  |   <>
  |   >
  |   >=
  |   <
  |   <=
  |   <=>
```

### Logical operators [Permalink](https://calcite.apache.org/docs/reference.html\#logical-operators "Permalink")

| Operator syntax | Description |
| --- | --- |
| boolean1 OR boolean2 | Whether _boolean1_ is TRUE or _boolean2_ is TRUE |
| boolean1 AND boolean2 | Whether _boolean1_ and _boolean2_ are both TRUE |
| NOT boolean | Whether _boolean_ is not TRUE; returns UNKNOWN if _boolean_ is UNKNOWN |
| boolean IS FALSE | Whether _boolean_ is FALSE; returns FALSE if _boolean_ is UNKNOWN |
| boolean IS NOT FALSE | Whether _boolean_ is not FALSE; returns TRUE if _boolean_ is UNKNOWN |
| boolean IS TRUE | Whether _boolean_ is TRUE; returns FALSE if _boolean_ is UNKNOWN |
| boolean IS NOT TRUE | Whether _boolean_ is not TRUE; returns TRUE if _boolean_ is UNKNOWN |
| boolean IS UNKNOWN | Whether _boolean_ is UNKNOWN |
| boolean IS NOT UNKNOWN | Whether _boolean_ is not UNKNOWN |

### Arithmetic operators and functions [Permalink](https://calcite.apache.org/docs/reference.html\#arithmetic-operators-and-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| \+ numeric | Returns _numeric_ |
| \- numeric | Returns negative _numeric_ |
| numeric1 + numeric2 | Returns _numeric1_ plus _numeric2_ |
| numeric1 - numeric2 | Returns _numeric1_ minus _numeric2_ |
| numeric1 \* numeric2 | Returns _numeric1_ multiplied by _numeric2_ |
| numeric1 / numeric2 | Returns _numeric1_ divided by _numeric2_ |
| numeric1 % numeric2 | As _MOD(numeric1, numeric2)_ (only in certain [conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#isPercentRemainderAllowed--)) |
| POWER(numeric1, numeric2) | Returns _numeric1_ raised to the power of _numeric2_ |
| ABS(numeric) | Returns the absolute value of _numeric_ |
| MOD(numeric1, numeric2) | Returns the remainder (modulus) of _numeric1_ divided by _numeric2_. The result is negative only if _numeric1_ is negative |
| SQRT(numeric) | Returns the square root of _numeric_ |
| LN(numeric) | Returns the natural logarithm (base _e_) of _numeric_ |
| LOG10(numeric) | Returns the base 10 logarithm of _numeric_ |
| EXP(numeric) | Returns _e_ raised to the power of _numeric_ |
| CEIL(numeric) | Rounds _numeric_ up, returning the smallest integer that is greater than or equal to _numeric_ |
| FLOOR(numeric) | Rounds _numeric_ down, returning the largest integer that is less than or equal to _numeric_ |
| RAND(\[seed\]) | Generates a random double between 0 and 1 inclusive, optionally initializing the random number generator with _seed_ |
| RAND\_INTEGER(\[seed, \] numeric) | Generates a random integer between 0 and _numeric_ \- 1 inclusive, optionally initializing the random number generator with _seed_ |
| ACOS(numeric) | Returns the arc cosine of _numeric_ |
| ASIN(numeric) | Returns the arc sine of _numeric_ |
| ATAN(numeric) | Returns the arc tangent of _numeric_ |
| ATAN2(numeric, numeric) | Returns the arc tangent of the _numeric_ coordinates |
| CBRT(numeric) | Returns the cube root of _numeric_ |
| COS(numeric) | Returns the cosine of _numeric_ |
| COT(numeric) | Returns the cotangent of _numeric_ |
| DEGREES(numeric) | Converts _numeric_ from radians to degrees |
| PI() | Returns a value that is closer than any other value to _pi_ |
| RADIANS(numeric) | Converts _numeric_ from degrees to radians |
| ROUND(numeric1 \[, integer2\]) | Rounds _numeric1_ to optionally _integer2_ (if not specified 0) places right to the decimal point |
| SIGN(numeric) | Returns the signum of _numeric_ |
| SIN(numeric) | Returns the sine of _numeric_ |
| TAN(numeric) | Returns the tangent of _numeric_ |
| TRUNCATE(numeric1 \[, integer2\]) | Truncates _numeric1_ to optionally _integer2_ (if not specified 0) places right to the decimal point |

### Character string operators and functions [Permalink](https://calcite.apache.org/docs/reference.html\#character-string-operators-and-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| string \|\| string | Concatenates two character strings |
| CHAR\_LENGTH(string) | Returns the number of characters in a character string |
| CHARACTER\_LENGTH(string) | As CHAR\_LENGTH( _string_) |
| UPPER(string) | Returns a character string converted to upper case |
| LOWER(string) | Returns a character string converted to lower case |
| POSITION(substring IN string) | Returns the position of the first occurrence of _substring_ in _string_ |
| POSITION(substring IN string FROM integer) | Returns the position of the first occurrence of _substring_ in _string_ starting at a given point (not standard SQL) |
| TRIM( { BOTH \| LEADING \| TRAILING } \[\[ string1 \] FROM \] string2) | Removes the longest string containing only the characters in _string1_ from the start/end/both ends of _string2_. If _string1_ is missing a single space is used. |
| OVERLAY(string1 PLACING string2 FROM integer \[ FOR integer2 \]) | Replaces a substring of _string1_ with _string2_, starting at the specified position _integer_ in _string1_ and optionally for a specified length _integer2_ |
| SUBSTRING(string FROM integer) | Returns a substring of a character string starting at a given point. If starting point is less than 1, the returned expression will begin at the first character that is specified in expression |
| SUBSTRING(string FROM integer FOR integer) | Returns a substring of a character string starting at a given point with a given length. If start point is less than 1 in this case, the number of characters that are returned is the largest value of either the start + length - 1 or 0 |
| INITCAP(string) | Returns _string_ with the first letter of each word converter to upper case and the rest to lower case. Words are sequences of alphanumeric characters separated by non-alphanumeric characters. |

Not implemented:

- SUBSTRING(string FROM regexp FOR regexp)

### Binary string operators and functions [Permalink](https://calcite.apache.org/docs/reference.html\#binary-string-operators-and-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| binary \|\| binary | Concatenates two binary strings |
| OCTET\_LENGTH(binary) | Returns the number of bytes in _binary_ |
| POSITION(binary1 IN binary2) | Returns the position of the first occurrence of _binary1_ in _binary2_ |
| POSITION(binary1 IN binary2 FROM integer) | Returns the position of the first occurrence of _binary1_ in _binary2_ starting at a given point (not standard SQL) |
| OVERLAY(binary1 PLACING binary2 FROM integer \[ FOR integer2 \]) | Replaces a substring of _binary1_ with _binary2_, starting at the specified position _integer_ in _binary1_ and optionally for a specified length _integer2_ |
| SUBSTRING(binary FROM integer) | Returns a substring of _binary_ starting at a given point |
| SUBSTRING(binary FROM integer FOR integer) | Returns a substring of _binary_ starting at a given point with a given length |

### Date/time functions [Permalink](https://calcite.apache.org/docs/reference.html\#datetime-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| LOCALTIME | Returns the current date and time in the session time zone in a value of datatype TIME |
| LOCALTIME(precision) | Returns the current date and time in the session time zone in a value of datatype TIME, with _precision_ digits of precision |
| LOCALTIMESTAMP | Returns the current date and time in the session time zone in a value of datatype TIMESTAMP |
| LOCALTIMESTAMP(precision) | Returns the current date and time in the session time zone in a value of datatype TIMESTAMP, with _precision_ digits of precision |
| CURRENT\_TIME | Returns the current time in the session time zone, in a value of datatype TIMESTAMP WITH TIME ZONE |
| CURRENT\_DATE | Returns the current date in the session time zone, in a value of datatype DATE |
| CURRENT\_TIMESTAMP | Returns the current date and time in the session time zone, in a value of datatype TIMESTAMP WITH TIME ZONE |
| EXTRACT(timeUnit FROM datetime) | Extracts and returns the value of a specified datetime field from a datetime value expression |
| FLOOR(datetime TO timeUnit) | Rounds _datetime_ down to _timeUnit_ |
| CEIL(datetime TO timeUnit) | Rounds _datetime_ up to _timeUnit_ |
| YEAR(date) | Equivalent to `EXTRACT(YEAR FROM date)`. Returns an integer. |
| QUARTER(date) | Equivalent to `EXTRACT(QUARTER FROM date)`. Returns an integer between 1 and 4. |
| MONTH(date) | Equivalent to `EXTRACT(MONTH FROM date)`. Returns an integer between 1 and 12. |
| WEEK(date) | Equivalent to `EXTRACT(WEEK FROM date)`. Returns an integer between 1 and 53. |
| DAYOFYEAR(date) | Equivalent to `EXTRACT(DOY FROM date)`. Returns an integer between 1 and 366. |
| DAYOFMONTH(date) | Equivalent to `EXTRACT(DAY FROM date)`. Returns an integer between 1 and 31. |
| DAYOFWEEK(date) | Equivalent to `EXTRACT(DOW FROM date)`. Returns an integer between 1 and 7. |
| HOUR(date) | Equivalent to `EXTRACT(HOUR FROM date)`. Returns an integer between 0 and 23. |
| MINUTE(date) | Equivalent to `EXTRACT(MINUTE FROM date)`. Returns an integer between 0 and 59. |
| SECOND(date) | Equivalent to `EXTRACT(SECOND FROM date)`. Returns an integer between 0 and 59. |
| TIMESTAMPADD(timeUnit, integer, datetime) | Returns _datetime_ with an interval of (signed) _integer_ _timeUnit_ s added. Equivalent to `datetime + INTERVAL 'integer' timeUnit` |
| TIMESTAMPDIFF(timeUnit, datetime, datetime2) | Returns the (signed) number of _timeUnit_ intervals between _datetime_ and _datetime2_. Equivalent to `(datetime2 - datetime) timeUnit` |
| LAST\_DAY(date) | Returns the date of the last day of the month in a value of datatype DATE; For example, it returns DATE’2020-02-29’ for both DATE’2020-02-10’ and TIMESTAMP’2020-02-10 10:10:10’ |

Calls to niladic functions such as `CURRENT_DATE` do not accept parentheses in
standard SQL. Calls with parentheses, such as `CURRENT_DATE()` are accepted in certain
[conformance levels](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/validate/SqlConformance.html#allowNiladicParentheses--).

Not implemented:

- CEIL(interval)
- FLOOR(interval)
- \+ interval
- \- interval
- interval + interval
- interval - interval
- interval / interval

### System functions [Permalink](https://calcite.apache.org/docs/reference.html\#system-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| USER | Equivalent to CURRENT\_USER |
| CURRENT\_USER | User name of current execution context |
| SESSION\_USER | Session user name |
| SYSTEM\_USER | Returns the name of the current data store user as identified by the operating system |
| CURRENT\_PATH | Returns a character string representing the current lookup scope for references to user-defined routines and types |
| CURRENT\_ROLE | Returns the current active role |
| CURRENT\_SCHEMA | Returns the current schema |

### Conditional functions and operators [Permalink](https://calcite.apache.org/docs/reference.html\#conditional-functions-and-operators "Permalink")

| Operator syntax | Description |
| --- | --- |
| CASE value<br>WHEN value1 \[, value11 \]\* THEN result1<br>\[ WHEN valueN \[, valueN1 \]\* THEN resultN \]\*<br>\[ ELSE resultZ \]<br> END | Simple case |
| CASE<br>WHEN condition1 THEN result1<br>\[ WHEN conditionN THEN resultN \]\*<br>\[ ELSE resultZ \]<br>END | Searched case |
| NULLIF(value, value) | Returns NULL if the values are the same.<br>For example, `NULLIF(5, 5)` returns NULL; `NULLIF(5, 0)` returns 5. |
| COALESCE(value, value \[, value \]\*) | Provides a value if the first value is null.<br>For example, `COALESCE(NULL, 5)` returns 5. |

### Type conversion [Permalink](https://calcite.apache.org/docs/reference.html\#type-conversion "Permalink")

Generally an expression cannot contain values of different datatypes. For example, an expression cannot multiply 5 by 10 and then add ‘JULIAN’.
However, Calcite supports both implicit and explicit conversion of values from one datatype to another.

#### Implicit and Explicit Type Conversion [Permalink](https://calcite.apache.org/docs/reference.html\#implicit-and-explicit-type-conversion "Permalink")

Calcite recommends that you specify explicit conversions, rather than rely on implicit or automatic conversions, for these reasons:

- SQL statements are easier to understand when you use explicit datatype conversion functions.
- Implicit datatype conversion can have a negative impact on performance, especially if the datatype of a column value is converted to that of a constant rather than the other way around.
- Implicit conversion depends on the context in which it occurs and may not work the same way in every case. For example, implicit conversion from a datetime value to a VARCHAR value may return an unexpected format.

Algorithms for implicit conversion are subject to change across Calcite releases. Behavior of explicit conversions is more predictable.

#### Explicit Type Conversion [Permalink](https://calcite.apache.org/docs/reference.html\#explicit-type-conversion "Permalink")

| Operator syntax | Description |
| --- | --- |
| CAST(value AS type) | Converts a value to a given type. Casts between integer types truncate towards 0 |
| CONVERT(string, charSet1, charSet2) | Converts _string_ from _charSet1_ to _charSet2_ |
| CONVERT(value USING transcodingName) | Alter _value_ from one base character set to _transcodingName_ |
| TRANSLATE(value USING transcodingName) | Alter _value_ from one base character set to _transcodingName_ |
| TYPEOF(variant) | Returns a string that describes the runtime type of _variant_, where variant has a `VARIANT` type |
| VARIANTNULL() | Returns an instance of the `VARIANT` null value (constructor) |

Converting a string to a **BINARY** or **VARBINARY** type produces the
list of bytes of the string’s encoding in the strings’ charset. A
runtime error is produced if the string’s characters cannot be
represented using its charset.

Supported data types syntax:

```sql
type:
      typeName
      [ collectionsTypeName ]*

typeName:
      sqlTypeName
  |   rowTypeName
  |   mapTypeName
  |   compoundIdentifier

mapTypeName:
  MAP '<' type ',' type '>'

sqlTypeName:
      char [ precision ] [ charSet ]
  |   varchar [ precision ] [ charSet ]
  |   DATE
  |   time
  |   timestamp
  |   GEOMETRY
  |   decimal [ precision [, scale] ]
  |   BOOLEAN
  |   integer
  |   BINARY [ precision ]
  |   varbinary [ precision ]
  |   TINYINT [ UNSIGNED ]
  |   SMALLINT [ UNSIGNED ]
  |   BIGINT [ UNSIGNED ]
  |   REAL
  |   double
  |   FLOAT
  |   ANY [ precision [, scale] ]

collectionsTypeName:
      ARRAY | MULTISET

rowTypeName:
      ROW '('
      fieldName1 fieldType1 [ NULL | NOT NULL ]
      [ , fieldName2 fieldType2 [ NULL | NOT NULL ] ]*
      ')'

char:
      CHARACTER | CHAR

varchar:
      char VARYING | VARCHAR

decimal:
      DECIMAL | DEC | NUMERIC

integer:
      INTEGER [ UNSIGNED ] | INT [ UNSIGNED ] | UNSIGNED

varbinary:
      BINARY VARYING | VARBINARY

double:
      DOUBLE [ PRECISION ]

time:
      TIME [ precision ] [ timeZone ]

timestamp:
      TIMESTAMP [ precision ] [ timeZone ]

charSet:
      CHARACTER SET charSetName

timeZone:
      WITHOUT TIME ZONE
  |   WITH LOCAL TIME ZONE
```

#### Implicit Type Conversion [Permalink](https://calcite.apache.org/docs/reference.html\#implicit-type-conversion "Permalink")

Calcite automatically converts a value from one datatype to another
when such a conversion makes sense. The table below is a matrix of
Calcite type conversions. The table shows all possible conversions,
without regard to the context in which it is made. The rules governing
these details follow the table.

| FROM - TO | NULL | BOOLEAN | TINYINT | SMALLINT | INT | BIGINT | TINYINT UNSIGNED | SMALLINT UNSIGNED | INT UNSIGNED | BIGINT UNSIGNED | DECIMAL | FLOAT or REAL | DOUBLE | INTERVAL | DATE | TIME | TIMESTAMP | CHAR or VARCHAR | BINARY or VARBINARY | GEOMETRY | ARRAY | MAP | MULTISET | ROW | UUID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NULL | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | x | x | x | x | i |
| BOOLEAN | x | i | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | x | x | x | x | x | x |
| TINYINT | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| SMALLINT | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| INT | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| BIGINT | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| TINYINT UNSIGNED | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| SMALLINT UNSIGNED | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| INT UNSIGNED | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| BIGINT UNSIGNED | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| DECIMAL | x | e | i | i | i | i | i | i | i | i | i | i | i | e | x | x | e | i | x | x | x | x | x | x | x |
| FLOAT/REAL | x | e | i | i | i | i | i | i | i | i | i | i | i | x | x | x | e | i | x | x | x | x | x | x | x |
| DOUBLE | x | e | i | i | i | i | i | i | i | i | i | i | i | x | x | x | e | i | x | x | x | x | x | x | x |
| INTERVAL | x | x | e | e | e | e | e | e | e | e | e | x | x | i | x | x | x | e | x | x | x | x | x | x | x |
| DATE | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | i | i | x | x | x | x | x | x | x |
| TIME | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | e | i | x | x | x | x | x | x | x |
| TIMESTAMP | x | x | e | e | e | e | e | e | e | e | e | e | e | x | i | e | i | i | x | x | x | x | x | x | x |
| CHAR or VARCHAR | x | e | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i | i |
| BINARY or VARBINARY | x | x | x | x | x | x | x | x | x | x | x | x | x | x | e | e | e | i | i | x | x | x | x | x | i |
| GEOMETRY | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | i | x | x | x | x | x |
| ARRAY | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | x | x | x |
| MAP | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | x | x |
| MULTISET | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x | x |
| ROW | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i | x |
| UUID | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x | i |

i: implicit cast / e: explicit cast / x: not allowed

##### Conversion Contexts and Strategies [Permalink](https://calcite.apache.org/docs/reference.html\#conversion-contexts-and-strategies "Permalink")

- Set operation (`UNION`, `EXCEPT`, `INTERSECT`): compare every branch
row data type and find the common type of each fields pair;
- Arithmetic operations combining signed and unsigned values will
produce a result with the wider type; if both types have the same width,
the result is unsigned;
- Binary arithmetic expression (`+`, `-`, `&`, `^`, `/`, `%`): promote
string operand to data type of the other numeric operand;
- Binary comparison (`=`, `<`, `<=`, `<>`, `>`, `>=`):
if operands are `STRING` and `TIMESTAMP`, promote to `TIMESTAMP`;
make `1 = true` and `0 = false` always evaluate to `TRUE`;
if there is numeric type operand, find common type for both operands.
- `IN` sub-query: compare type of LHS and RHS, and find the common type;
if it is struct type, find wider type for every field;
- `IN` expression list: compare every expression to find the common type;
- `CASE WHEN` expression or `COALESCE`: find the common wider type of the `THEN`
and `ELSE` operands;
- Character + `INTERVAL` or character - `INTERVAL`: promote character to
`TIMESTAMP`;
- Built-in function: look up the type families registered in the checker,
find the family default type if checker rules allow it;
- User-defined function (UDF): coerce based on the declared argument types
of the `eval()` method;
- `INSERT` and `UPDATE`: coerce a source field to counterpart target table
field’s type if the two fields differ with type name or precision(scale).

Note:

Implicit type coercion of following cases are ignored:

- One of the type is `ANY`;
- Type coercion within `CHARACTER` types are always ignored,
i.e. from `CHAR(20)` to `VARCHAR(30)`;
- Type coercion from a numeric to another with higher precedence is ignored,
i.e. from `INT` to `LONG`.

##### Strategies for Finding Common Type [Permalink](https://calcite.apache.org/docs/reference.html\#strategies-for-finding-common-type "Permalink")

- If the operator has expected data types, just take them as the
desired one. (e.g. the UDF would have `eval()` method which has
reflection argument types);
- If there is no expected data type but the data type families are
registered, try to coerce the arguments to the family’s default data
type, i.e. the String family will have a `VARCHAR` type;
- If neither expected data type nor families are specified, try to
find the tightest common type of the node types, i.e. `INTEGER` and
`DOUBLE` will return `DOUBLE`, the numeric precision does not lose
for this case;
- If no tightest common type is found, try to find a wider type,
i.e. `VARCHAR` and `INTEGER` will return `INTEGER`,
we allow some precision loss when widening decimal to fractional,
or promote to `VARCHAR` type.

### Value constructors [Permalink](https://calcite.apache.org/docs/reference.html\#value-constructors "Permalink")

| Operator syntax | Description |
| --- | --- |
| ROW (value \[, value \]\*) | Creates a row from a list of values. |
| (value \[, value \]\* ) | Creates a row from a list of values. |
| row ‘\[’ index ‘\]’ | Returns the element at a particular location in a row (1-based index). |
| row ‘\[’ name ‘\]’ | Returns the element of a row with a particular name. |
| map ‘\[’ key ‘\]’ | Returns the element of a map with a particular key. |
| array ‘\[’ index ‘\]’ | Returns the element at a particular location in an array (1-based index). |
| ARRAY ‘\[’ value \[, value \]\* ‘\]’ | Creates an array from a list of values. |
| MAP ‘\[’ key, value \[, key, value \]\* ‘\]’ | Creates a map from a list of key-value pairs. |

### Value constructors by query [Permalink](https://calcite.apache.org/docs/reference.html\#value-constructors-by-query "Permalink")

| Operator syntax | Description |
| --- | --- |
| ARRAY (sub-query) | Creates an array from the result of a sub-query. Example: `ARRAY(SELECT empno FROM emp ORDER BY empno)` |
| MAP (sub-query) | Creates a map from the result of a key-value pair sub-query. Example: `MAP(SELECT empno, deptno FROM emp)` |
| MULTISET (sub-query) | Creates a multiset from the result of a sub-query. Example: `MULTISET(SELECT empno FROM emp)` |

### Collection functions [Permalink](https://calcite.apache.org/docs/reference.html\#collection-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| ELEMENT(value) | Returns the sole element of an array or multiset; null if the collection is empty; throws if it has more than one element. |
| CARDINALITY(value) | Returns the number of elements in an array or multiset. |
| value MEMBER OF multiset | Returns whether the _value_ is a member of _multiset_. |
| multiset IS A SET | Whether _multiset_ is a set (has no duplicates). |
| multiset IS NOT A SET | Whether _multiset_ is not a set (has duplicates). |
| multiset IS EMPTY | Whether _multiset_ contains zero elements. |
| multiset IS NOT EMPTY | Whether _multiset_ contains one or more elements. |
| multiset SUBMULTISET OF multiset2 | Whether _multiset_ is a submultiset of _multiset2_. |
| multiset NOT SUBMULTISET OF multiset2 | Whether _multiset_ is not a submultiset of _multiset2_. |
| multiset MULTISET UNION \[ ALL \| DISTINCT \] multiset2 | Returns the union _multiset_ and _multiset2_, eliminating duplicates if DISTINCT is specified (ALL is the default). |
| multiset MULTISET INTERSECT \[ ALL \| DISTINCT \] multiset2 | Returns the intersection of _multiset_ and _multiset2_, eliminating duplicates if DISTINCT is specified (ALL is the default). |
| multiset MULTISET EXCEPT \[ ALL \| DISTINCT \] multiset2 | Returns the difference of _multiset_ and _multiset2_, eliminating duplicates if DISTINCT is specified (ALL is the default). |

See also: the UNNEST relational operator converts a collection to a relation.

### Period predicates [Permalink](https://calcite.apache.org/docs/reference.html\#period-predicates "Permalink")

| Operator syntax | Description |
| --- | --- |
| period1 CONTAINS datetime |  |
| period1 CONTAINS period2 |  |
| period1 OVERLAPS period2 |  |
| period1 EQUALS period2 |  |
| period1 PRECEDES period2 |  |
| period1 IMMEDIATELY PRECEDES period2 |  |
| period1 SUCCEEDS period2 |  |
| period1 IMMEDIATELY SUCCEEDS period2 |  |

Where _period1_ and _period2_ are period expressions:

```sql
period:
      (datetime, datetime)
  |   (datetime, interval)
  |   PERIOD (datetime, datetime)
  |   PERIOD (datetime, interval)
```

### JDBC function escape [Permalink](https://calcite.apache.org/docs/reference.html\#jdbc-function-escape "Permalink")

#### Numeric [Permalink](https://calcite.apache.org/docs/reference.html\#numeric "Permalink")

| Operator syntax | Description |
| --- | --- |
| {fn ABS(numeric)} | Returns the absolute value of _numeric_ |
| {fn ACOS(numeric)} | Returns the arc cosine of _numeric_ |
| {fn ASIN(numeric)} | Returns the arc sine of _numeric_ |
| {fn ATAN(numeric)} | Returns the arc tangent of _numeric_ |
| {fn ATAN2(numeric, numeric)} | Returns the arc tangent of the _numeric_ coordinates |
| {fn CBRT(numeric)} | Returns the cube root of _numeric_ |
| {fn CEILING(numeric)} | Rounds _numeric_ up, and returns the smallest number that is greater than or equal to _numeric_ |
| {fn COS(numeric)} | Returns the cosine of _numeric_ |
| {fn COT(numeric)} | Returns the cotangent of _numeric_ |
| {fn DEGREES(numeric)} | Converts _numeric_ from radians to degrees |
| {fn EXP(numeric)} | Returns _e_ raised to the power of _numeric_ |
| {fn FLOOR(numeric)} | Rounds _numeric_ down, and returns the largest number that is less than or equal to _numeric_ |
| {fn LOG(numeric)} | Returns the natural logarithm (base _e_) of _numeric_ |
| {fn LOG10(numeric)} | Returns the base-10 logarithm of _numeric_ |
| {fn MOD(numeric1, numeric2)} | Returns the remainder (modulus) of _numeric1_ divided by _numeric2_. The result is negative only if _numeric1_ is negative |
| {fn PI()} | Returns a value that is closer than any other value to _pi_ |
| {fn POWER(numeric1, numeric2)} | Returns _numeric1_ raised to the power of _numeric2_ |
| {fn RADIANS(numeric)} | Converts _numeric_ from degrees to radians |
| {fn RAND(numeric)} | Returns a random double using _numeric_ as the seed value |
| {fn ROUND(numeric1, integer2)} | Rounds _numeric1_ to _integer2_ places right to the decimal point |
| {fn SIGN(numeric)} | Returns the signum of _numeric_ |
| {fn SIN(numeric)} | Returns the sine of _numeric_ |
| {fn SQRT(numeric)} | Returns the square root of _numeric_ |
| {fn TAN(numeric)} | Returns the tangent of _numeric_ |
| {fn TRUNCATE(numeric1, integer2)} | Truncates _numeric1_ to _integer2_ places right to the decimal point |

#### String [Permalink](https://calcite.apache.org/docs/reference.html\#string "Permalink")

| Operator syntax | Description |
| --- | --- |
| {fn ASCII(string)} | Returns the ASCII code of the first character of _string_; if the first character is a non-ASCII character, returns its Unicode code point; returns 0 if _string_ is empty |
| {fn CHAR(integer)} | Returns the character whose ASCII code is _integer_ % 256, or null if _integer_ < 0 |
| {fn CONCAT(character, character)} | Returns the concatenation of character strings |
| {fn INSERT(string1, start, length, string2)} | Inserts _string2_ into a slot in _string1_ |
| {fn LCASE(string)} | Returns a string in which all alphabetic characters in _string_ have been converted to lower case |
| {fn LENGTH(string)} | Returns the number of characters in a string |
| {fn LOCATE(string1, string2 \[, integer\])} | Returns the position in _string2_ of the first occurrence of _string1_. Searches from the beginning of _string2_, unless _integer_ is specified. |
| {fn LEFT(string, length)} | Returns the leftmost _length_ characters from _string_ |
| {fn LTRIM(string)} | Returns _string_ with leading space characters removed |
| {fn REPLACE(string, search, replacement)} | Returns a string in which all the occurrences of _search_ in _string_ are replaced with _replacement_; returns unchanged _string_ if _search_ is an empty string(‘’); if _replacement_ is the empty string, the occurrences of _search_ are removed. Matching between _search_ and _string_ is case-insensitive under SQL Server semantics |
| {fn REVERSE(string)} | Returns _string_ with the order of the characters reversed |
| {fn RIGHT(string, length)} | Returns the rightmost _length_ characters from _string_ |
| {fn RTRIM(string)} | Returns _string_ with trailing space characters removed |
| {fn SUBSTRING(string, offset, length)} | Returns a character string that consists of _length_ characters from _string_ starting at the _offset_ position |
| {fn UCASE(string)} | Returns a string in which all alphabetic characters in _string_ have been converted to upper case |

#### Date/time [Permalink](https://calcite.apache.org/docs/reference.html\#datetime "Permalink")

| Operator syntax | Description |
| --- | --- |
| {fn CURDATE()} | Equivalent to `CURRENT_DATE` |
| {fn CURTIME()} | Equivalent to `LOCALTIME` |
| {fn NOW()} | Equivalent to `LOCALTIMESTAMP` |
| {fn YEAR(date)} | Equivalent to `EXTRACT(YEAR FROM date)`. Returns an integer. |
| {fn QUARTER(date)} | Equivalent to `EXTRACT(QUARTER FROM date)`. Returns an integer between 1 and 4. |
| {fn MONTH(date)} | Equivalent to `EXTRACT(MONTH FROM date)`. Returns an integer between 1 and 12. |
| {fn WEEK(date)} | Equivalent to `EXTRACT(WEEK FROM date)`. Returns an integer between 1 and 53. |
| {fn DAYOFYEAR(date)} | Equivalent to `EXTRACT(DOY FROM date)`. Returns an integer between 1 and 366. |
| {fn DAYOFMONTH(date)} | Equivalent to `EXTRACT(DAY FROM date)`. Returns an integer between 1 and 31. |
| {fn DAYOFWEEK(date)} | Equivalent to `EXTRACT(DOW FROM date)`. Returns an integer between 1 and 7. |
| {fn HOUR(date)} | Equivalent to `EXTRACT(HOUR FROM date)`. Returns an integer between 0 and 23. |
| {fn MINUTE(date)} | Equivalent to `EXTRACT(MINUTE FROM date)`. Returns an integer between 0 and 59. |
| {fn SECOND(date)} | Equivalent to `EXTRACT(SECOND FROM date)`. Returns an integer between 0 and 59. |
| {fn TIMESTAMPADD(timeUnit, count, datetime)} | Adds an interval of _count_ _timeUnit_ s to a datetime |
| {fn TIMESTAMPDIFF(timeUnit, timestamp1, timestamp2)} | Subtracts _timestamp1_ from _timestamp2_ and returns the result in _timeUnit_ s |

#### System [Permalink](https://calcite.apache.org/docs/reference.html\#system "Permalink")

| Operator syntax | Description |
| --- | --- |
| {fn DATABASE()} | Equivalent to `CURRENT_CATALOG` |
| {fn IFNULL(value1, value2)} | Returns value2 if value1 is null |
| {fn USER()} | Equivalent to `CURRENT_USER` |

#### Conversion [Permalink](https://calcite.apache.org/docs/reference.html\#conversion "Permalink")

| Operator syntax | Description |
| --- | --- |
| {fn CONVERT(value, type)} | Cast _value_ into _type_ |

### Aggregate functions [Permalink](https://calcite.apache.org/docs/reference.html\#aggregate-functions "Permalink")

Syntax:

```sql
aggregateCall:
      agg '(' [ ALL | DISTINCT ] value [, value ]* ')'
      [ WITHIN DISTINCT '(' expression [, expression ]* ')' ]
      [ WITHIN GROUP '(' ORDER BY orderItem [, orderItem ]* ')' ]
      [ FILTER '(' WHERE condition ')' ]
  |   agg '(' '*' ')' [ FILTER (WHERE condition) ]
```

where _agg_ is one of the operators in the following table, or a user-defined
aggregate function.

If `FILTER` is present, the aggregate function only considers rows for which
_condition_ evaluates to TRUE.

If `DISTINCT` is present, duplicate argument values are eliminated before being
passed to the aggregate function.

If `WITHIN DISTINCT` is present, argument values are made distinct within
each value of specified keys before being passed to the aggregate function.

If `WITHIN GROUP` is present, the aggregate function sorts the input rows
according to the `ORDER BY` clause inside `WITHIN GROUP` before aggregating
values. `WITHIN GROUP` is only allowed for hypothetical set functions (`RANK`,
`DENSE_RANK`, `PERCENT_RANK` and `CUME_DIST`), inverse distribution functions
(`PERCENTILE_CONT` and `PERCENTILE_DISC`) and collection functions (`COLLECT`
and `LISTAGG`).

| Operator syntax | Description |
| --- | --- |
| ANY\_VALUE( \[ ALL \| DISTINCT \] value) | Returns one of the values of _value_ across all input values; this is NOT specified in the SQL standard |
| ARG\_MAX(value, comp) | Returns _value_ for the maximum value of _comp_ in the group |
| ARG\_MIN(value, comp) | Returns _value_ for the minimum value of _comp_ in the group |
| APPROX\_COUNT\_DISTINCT(value \[, value \]\*) | Returns the approximate number of distinct values of _value_; the database is allowed to use an approximation but is not required to |
| AVG( \[ ALL \| DISTINCT \] numeric) | Returns the average (arithmetic mean) of _numeric_ across all input values |
| BIT\_AND( \[ ALL \| DISTINCT \] value) | Returns the bitwise AND of all non-null input values, or null if none; integer and binary types are supported |
| BIT\_OR( \[ ALL \| DISTINCT \] value) | Returns the bitwise OR of all non-null input values, or null if none; integer and binary types are supported |
| BIT\_XOR( \[ ALL \| DISTINCT \] value) | Returns the bitwise XOR of all non-null input values, or null if none; integer and binary types are supported |
| COLLECT( \[ ALL \| DISTINCT \] value) | Returns a multiset of the values |
| COUNT(\*) | Returns the number of input rows |
| COUNT( \[ ALL \| DISTINCT \] value \[, value \]\*) | Returns the number of input rows for which _value_ is not null (wholly not null if _value_ is composite) |
| COVAR\_POP(numeric1, numeric2) | Returns the population covariance of the pair ( _numeric1_, _numeric2_) across all input values |
| COVAR\_SAMP(numeric1, numeric2) | Returns the sample covariance of the pair ( _numeric1_, _numeric2_) across all input values |
| EVERY(condition) | Returns TRUE if all of the values of _condition_ are TRUE |
| FUSION(multiset) | Returns the multiset union of _multiset_ across all input values |
| INTERSECTION(multiset) | Returns the multiset intersection of _multiset_ across all input values |
| LISTAGG( \[ ALL \| DISTINCT \] value \[, separator\]) | Returns values concatenated into a string, delimited by separator (default ‘,’) |
| MAX( \[ ALL \| DISTINCT \] value) | Returns the maximum value of _value_ across all input values |
| MIN( \[ ALL \| DISTINCT \] value) | Returns the minimum value of _value_ across all input values |
| MODE(value) | Returns the most frequent value of _value_ across all input values |
| REGR\_COUNT(numeric1, numeric2) | Returns the number of rows where both dependent and independent expressions are not null |
| REGR\_SXX(numeric1, numeric2) | Returns the sum of squares of the dependent expression in a linear regression model |
| REGR\_SYY(numeric1, numeric2) | Returns the sum of squares of the independent expression in a linear regression model |
| SOME(condition) | Returns TRUE if one or more of the values of _condition_ is TRUE |
| STDDEV( \[ ALL \| DISTINCT \] numeric) | Synonym for `STDDEV_SAMP` |
| STDDEV\_POP( \[ ALL \| DISTINCT \] numeric) | Returns the population standard deviation of _numeric_ across all input values |
| STDDEV\_SAMP( \[ ALL \| DISTINCT \] numeric) | Returns the sample standard deviation of _numeric_ across all input values |
| SUM( \[ ALL \| DISTINCT \] numeric) | Returns the sum of _numeric_ across all input values |
| VAR\_POP( \[ ALL \| DISTINCT \] value) | Returns the population variance (square of the population standard deviation) of _numeric_ across all input values |
| VAR\_SAMP( \[ ALL \| DISTINCT \] numeric) | Returns the sample variance (square of the sample standard deviation) of _numeric_ across all input values |

Not implemented:

- REGR\_AVGX(numeric1, numeric2)
- REGR\_AVGY(numeric1, numeric2)
- REGR\_INTERCEPT(numeric1, numeric2)
- REGR\_R2(numeric1, numeric2)
- REGR\_SLOPE(numeric1, numeric2)
- REGR\_SXY(numeric1, numeric2)

#### Ordered-Set Aggregate Functions [Permalink](https://calcite.apache.org/docs/reference.html\#ordered-set-aggregate-functions "Permalink")

The syntax is as for _aggregateCall_, except that `WITHIN GROUP` is
required.

In the following:

- _fraction_ is a numeric literal between 0 and 1, inclusive, and
represents a percentage

| Operator syntax | Description |
| --- | --- |
| PERCENTILE\_CONT(fraction) WITHIN GROUP (ORDER BY orderItem) | Returns a percentile based on a continuous distribution of the column values, interpolating between adjacent input items if needed |
| PERCENTILE\_DISC(fraction) WITHIN GROUP (ORDER BY orderItem \[, orderItem \]\*) | Returns a percentile based on a discrete distribution of the column values returning the first input value whose position in the ordering equals or exceeds the specified fraction |

### Window functions [Permalink](https://calcite.apache.org/docs/reference.html\#window-functions "Permalink")

Syntax:

```sql
windowedAggregateCall:
      agg '(' [ ALL | DISTINCT ] value [, value ]* ')'
      [ RESPECT NULLS | IGNORE NULLS ]
      [ WITHIN GROUP '(' ORDER BY orderItem [, orderItem ]* ')' ]
      OVER window
  |   agg '(' '*' ')'
      OVER window
```

where _agg_ is one of the operators in the following table, or a user-defined
aggregate function.

The _exclude_ clause can be one of:

- EXCLUDE NO OTHER: Does not exclude any row from the frame. This is the default.
- EXCLUDE CURRENT ROW: Exclude the current row from the frame.
- EXCLUDE GROUP: Exclude the current row and its ordering peers from the frame.
- EXCLUDE TIES: Exclude all the ordering peers of the current row, but not the current row itself.

`DISTINCT`, `FILTER` and `WITHIN GROUP` are as described for aggregate
functions.

| Operator syntax | Description |
| --- | --- |
| COUNT(value \[, value \]\*) OVER window | Returns the number of rows in _window_ for which _value_ is not null (wholly not null if _value_ is composite) |
| COUNT(\*) OVER window | Returns the number of rows in _window_ |
| AVG(numeric) OVER window | Returns the average (arithmetic mean) of _numeric_ across all values in _window_ |
| SUM(numeric) OVER window | Returns the sum of _numeric_ across all values in _window_ |
| MAX(value) OVER window | Returns the maximum value of _value_ across all values in _window_ |
| MIN(value) OVER window | Returns the minimum value of _value_ across all values in _window_ |
| RANK() OVER window | Returns the rank of the current row with gaps; same as ROW\_NUMBER of its first peer |
| DENSE\_RANK() OVER window | Returns the rank of the current row without gaps; this function counts peer groups |
| ROW\_NUMBER() OVER window | Returns the number of the current row within its partition, counting from 1 |
| FIRST\_VALUE(value) OVER window | Returns _value_ evaluated at the row that is the first row of the window frame |
| LAST\_VALUE(value) OVER window | Returns _value_ evaluated at the row that is the last row of the window frame |
| LEAD(value, offset, default) OVER window | Returns _value_ evaluated at the row that is _offset_ rows after the current row within the partition; if there is no such row, instead returns _default_. Both _offset_ and _default_ are evaluated with respect to the current row. If omitted, _offset_ defaults to 1 and _default_ to NULL |
| LAG(value, offset, default) OVER window | Returns _value_ evaluated at the row that is _offset_ rows before the current row within the partition; if there is no such row, instead returns _default_. Both _offset_ and _default_ are evaluated with respect to the current row. If omitted, _offset_ defaults to 1 and _default_ to NULL |
| NTH\_VALUE(value, nth) OVER window | Returns _value_ evaluated at the row that is the _n_ th row of the window frame |
| NTILE(value) OVER window | Returns an integer ranging from 1 to _value_, dividing the partition as equally as possible |

Note:

- You may specify null treatment (`IGNORE NULLS`, `RESPECT NULLS`) for
`FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE`, `LEAD` and `LAG` functions. The
syntax handled by the parser, but only `RESPECT NULLS` is implemented at
runtime.

Not implemented:

- COUNT(DISTINCT value \[, value \]\*) OVER window
- APPROX\_COUNT\_DISTINCT(value \[, value \]\*) OVER window
- PERCENT\_RANK(value) OVER window
- CUME\_DIST(value) OVER window

### Grouping functions [Permalink](https://calcite.apache.org/docs/reference.html\#grouping-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| GROUPING(expression \[, expression \]\*) | Returns a bit vector of the given grouping expressions |
| GROUP\_ID() | Returns an integer that uniquely identifies the combination of grouping keys |
| GROUPING\_ID(expression \[, expression \]\*) | Synonym for `GROUPING` |

### DESCRIPTOR [Permalink](https://calcite.apache.org/docs/reference.html\#descriptor "Permalink")

| Operator syntax | Description |
| --- | --- |
| DESCRIPTOR(name \[, name \]\*) | DESCRIPTOR appears as an argument in a function to indicate a list of names. The interpretation of names is left to the function. |

### Table functions [Permalink](https://calcite.apache.org/docs/reference.html\#table-functions "Permalink")

Table functions occur in the `FROM` clause.

Table functions may have generic table parameters (i.e., no row type is
declared when the table function is created), and the row type of the result
might depend on the row type(s) of the input tables.
Besides, input tables are classified by three characteristics.
The first characteristic is semantics. Input tables have either row semantics
or set semantics, as follows:

- Row semantics means that the result of the table function depends on a
row-by-row basis.
- Set semantics means that the outcome of the function depends on how the
data is partitioned.

The second characteristic, which applies only to input tables with
set semantics, is whether the table function can generate a result row
even if the input table is empty.

- If the table function can generate a result row on empty input,
the table is said to be “keep when empty”.
- The alternative is called “prune when empty”, meaning that
the result would be pruned out if the input table is empty.

The third characteristic is whether the input table supports
pass-through columns or not. Pass-through columns is a mechanism
enabling the table function to copy every column of an input row
into columns of an output row.

The input tables with set semantics may be partitioned on one or more columns.
The input tables with set semantics may be ordered on one or more columns.

Note:

- The input tables with row semantics may not be partitioned or ordered.
- A polymorphic table function may have multiple input tables. However,
at most one input table could have row semantics.

#### TUMBLE [Permalink](https://calcite.apache.org/docs/reference.html\#tumble "Permalink")

In streaming queries, TUMBLE assigns a window for each row of a relation based
on a timestamp column. An assigned window is specified by its beginning and
ending. All assigned windows have the same length, and that’s why tumbling
sometimes is named as “fixed windowing”.
The first parameter of the TUMBLE table function is a generic table parameter.
The input table has row semantics and supports pass-through columns.

| Operator syntax | Description |
| --- | --- |
| TUMBLE(data, DESCRIPTOR(timecol), size \[, offset \]) | Indicates a tumbling window of _size_ interval for _timecol_, optionally aligned at _offset_. |

Here is an example:

```sql
SELECT * FROM TABLE(
  TUMBLE(
    TABLE orders,
    DESCRIPTOR(rowtime),
    INTERVAL '1' MINUTE));

-- or with the named params
-- note: the DATA param must be the first
SELECT * FROM TABLE(
  TUMBLE(
    DATA => TABLE orders,
    TIMECOL => DESCRIPTOR(rowtime),
    SIZE => INTERVAL '1' MINUTE));
```

applies a tumbling window with a one minute range to rows from the `orders`
table. `rowtime` is the watermarked column of the `orders` table that informs
whether data is complete.

#### HOP [Permalink](https://calcite.apache.org/docs/reference.html\#hop "Permalink")

In streaming queries, HOP assigns windows that cover rows within the interval of _size_ and shifting every _slide_ based
on a timestamp column. Windows assigned could have overlapping so hopping sometime is named as “sliding windowing”.
The first parameter of the HOP table function is a generic table parameter.
The input table has row semantics and supports pass-through columns.

| Operator syntax | Description |
| --- | --- |
| HOP(data, DESCRIPTOR(timecol), slide, size \[, offset \]) | Indicates a hopping window for _timecol_, covering rows within the interval of _size_, shifting every _slide_ and optionally aligned at _offset_. |

Here is an example:

```sql
SELECT * FROM TABLE(
  HOP(
    TABLE orders,
    DESCRIPTOR(rowtime),
    INTERVAL '2' MINUTE,
    INTERVAL '5' MINUTE));

-- or with the named params
-- note: the DATA param must be the first
SELECT * FROM TABLE(
  HOP(
    DATA => TABLE orders,
    TIMECOL => DESCRIPTOR(rowtime),
    SLIDE => INTERVAL '2' MINUTE,
    SIZE => INTERVAL '5' MINUTE));
```

applies hopping with 5-minute interval size on rows from table `orders`
and shifting every 2 minutes. `rowtime` is the watermarked column of table
orders that tells data completeness.

#### SESSION [Permalink](https://calcite.apache.org/docs/reference.html\#session "Permalink")

In streaming queries, SESSION assigns windows that cover rows based on _datetime_. Within a session window, distances
of rows are less than _interval_. Session window is applied per _key_.
The first parameter of the SESSION table function is a generic table parameter.
The input table has set semantics and supports pass-through columns.
Besides, the SESSION table function would not generate a result row
if the input table is empty.

| Operator syntax | Description |
| --- | --- |
| session(data, DESCRIPTOR(timecol), DESCRIPTOR(key), size) | Indicates a session window of _size_ interval for _timecol_. Session window is applied per _key_. |

Here is an example:

```sql
SELECT * FROM TABLE(
  SESSION(
    TABLE orders PARTITION BY product,
    DESCRIPTOR(rowtime),
    INTERVAL '20' MINUTE));

-- or with the named params
-- note: the DATA param must be the first
SELECT * FROM TABLE(
  SESSION(
    DATA => TABLE orders PARTITION BY product,
    TIMECOL => DESCRIPTOR(rowtime),
    SIZE => INTERVAL '20' MINUTE));
```

applies a session with 20-minute inactive gap on rows from table `orders`.
`rowtime` is the watermarked column of table orders that tells data
completeness. Session is applied per product.

**Note**: The `Tumble`, `Hop` and `Session` window table functions assign
each row in the original table to a window. The output table has all
the same columns as the original table plus two additional columns `window_start`
and `window_end`, which represent the start and end of the window interval, respectively.

### Grouped window functions [Permalink](https://calcite.apache.org/docs/reference.html\#grouped-window-functions "Permalink")

**warning**: grouped window functions are deprecated.

Grouped window functions occur in the `GROUP BY` clause and define a key value
that represents a window containing several rows.

In some window functions, a row may belong to more than one window.
For example, if a query is grouped using
`HOP(t, INTERVAL '2' HOUR, INTERVAL '1' HOUR)`, a row with timestamp ‘10:15:00’
will occur in both the 10:00 - 11:00 and 11:00 - 12:00 totals.

| Operator syntax | Description |
| --- | --- |
| HOP(datetime, slide, size \[, time \]) | Indicates a hopping window for _datetime_, covering rows within the interval of _size_, shifting every _slide_, and optionally aligned at _time_ |
| SESSION(datetime, interval \[, time \]) | Indicates a session window of _interval_ for _datetime_, optionally aligned at _time_ |
| TUMBLE(datetime, interval \[, time \]) | Indicates a tumbling window of _interval_ for _datetime_, optionally aligned at _time_ |

### Grouped auxiliary functions [Permalink](https://calcite.apache.org/docs/reference.html\#grouped-auxiliary-functions "Permalink")

Grouped auxiliary functions allow you to access properties of a window defined
by a grouped window function.

| Operator syntax | Description |
| --- | --- |
| HOP\_END(expression, slide, size \[, time \]) | Returns the value of _expression_ at the end of the window defined by a `HOP` function call |
| HOP\_START(expression, slide, size \[, time \]) | Returns the value of _expression_ at the beginning of the window defined by a `HOP` function call |
| SESSION\_END(expression, interval \[, time\]) | Returns the value of _expression_ at the end of the window defined by a `SESSION` function call |
| SESSION\_START(expression, interval \[, time\]) | Returns the value of _expression_ at the beginning of the window defined by a `SESSION` function call |
| TUMBLE\_END(expression, interval \[, time \]) | Returns the value of _expression_ at the end of the window defined by a `TUMBLE` function call |
| TUMBLE\_START(expression, interval \[, time \]) | Returns the value of _expression_ at the beginning of the window defined by a `TUMBLE` function call |

### Spatial functions [Permalink](https://calcite.apache.org/docs/reference.html\#spatial-functions "Permalink")

In the following:

- _geom_ is a GEOMETRY;
- _geomCollection_ is a GEOMETRYCOLLECTION;
- _point_ is a POINT;
- _lineString_ is a LINESTRING;
- _iMatrix_ is a [DE-9IM intersection matrix](https://en.wikipedia.org/wiki/DE-9IM);
- _distance_, _tolerance_, _segmentLengthFraction_, _offsetDistance_ are of type double;
- _dimension_, _quadSegs_, _srid_, _zoom_ are of type integer;
- _layerType_ is a character string;
- _gml_ is a character string containing [Geography Markup Language (GML)](https://en.wikipedia.org/wiki/Geography_Markup_Language);
- _wkt_ is a character string containing [well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text);
- _wkb_ is a binary string containing [well-known binary (WKB)](https://en.wikipedia.org/wiki/Well-known_binary).

In the “C” (for “compatibility”) column, “o” indicates that the function
implements the OpenGIS Simple Features Implementation Specification for SQL,
[version 1.2.1](https://www.opengeospatial.org/standards/sfs);
“p” indicates that the function is a
[PostGIS](https://www.postgis.net/docs/reference.html) extension to OpenGIS;
“h” indicates that the function is an
[H2GIS](http://www.h2gis.org/docs/dev/functions/) extension.

#### Geometry conversion functions (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-conversion-functions-2d "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| p | ST\_AsBinary(geom) | Synonym for `ST_AsWKB` |
| p | ST\_AsEWKB(geom) | Synonym for `ST_AsWKB` |
| p | ST\_AsEWKT(geom) | Converts GEOMETRY → EWKT |
| p | ST\_AsGeoJSON(geom) | Converts GEOMETRY → GeoJSON |
| p | ST\_AsGML(geom) | Converts GEOMETRY → GML |
| p | ST\_AsText(geom) | Synonym for `ST_AsWKT` |
| o | ST\_AsWKB(geom) | Converts GEOMETRY → WKB |
| o | ST\_AsWKT(geom) | Converts GEOMETRY → WKT |
| o | ST\_Force2D(geom) | 3D GEOMETRY → 2D GEOMETRY |
| o | ST\_GeomFromEWKB(wkb \[, srid \]) | Synonym for `ST_GeomFromWKB` |
| o | ST\_GeomFromEWKT(wkb \[, srid \]) | Converts EWKT → GEOMETRY |
| o | ST\_GeomFromGeoJSON(json) | Converts GeoJSON → GEOMETRY |
| o | ST\_GeomFromGML(wkb \[, srid \]) | Converts GML → GEOMETRY |
| o | ST\_GeomFromText(wkt \[, srid \]) | Synonym for `ST_GeomFromWKT` |
| o | ST\_GeomFromWKB(wkb \[, srid \]) | Converts WKB → GEOMETRY |
| o | ST\_GeomFromWKT(wkb \[, srid \]) | Converts WKT → GEOMETRY |
| o | ST\_LineFromText(wkt \[, srid \]) | Converts WKT → LINESTRING |
| o | ST\_LineFromWKB(wkt \[, srid \]) | Converts WKT → LINESTRING |
| o | ST\_MLineFromText(wkt \[, srid \]) | Converts WKT → MULTILINESTRING |
| o | ST\_MPointFromText(wkt \[, srid \]) | Converts WKT → MULTIPOINT |
| o | ST\_MPolyFromText(wkt \[, srid \]) Converts WKT → MULTIPOLYGON |  |
| o | ST\_PointFromText(wkt \[, srid \]) | Converts WKT → POINT |
| o | ST\_PointFromWKB(wkt \[, srid \]) | Converts WKB → POINT |
| o | ST\_PolyFromText(wkt \[, srid \]) | Converts WKT → POLYGON |
| o | ST\_PolyFromWKB(wkt \[, srid \]) | Converts WKB → POLYGON |
| p | ST\_ReducePrecision(geom, gridSize) | Reduces the precision of a _geom_ to the provided _gridSize_ |
| h | ST\_ToMultiPoint(geom) | Converts the coordinates of _geom_ (which may be a GEOMETRYCOLLECTION) into a MULTIPOINT |
| h | ST\_ToMultiLine(geom) | Converts the coordinates of _geom_ (which may be a GEOMETRYCOLLECTION) into a MULTILINESTRING |
| h | ST\_ToMultiSegments(geom) | Converts _geom_ (which may be a GEOMETRYCOLLECTION) into a set of distinct segments stored in a MULTILINESTRING |

Not implemented:

- ST\_GoogleMapLink(geom \[, layerType \[, zoom \]\]) GEOMETRY → Google map link
- ST\_OSMMapLink(geom \[, marker \]) GEOMETRY → OSM map link

#### Geometry conversion functions (3D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-conversion-functions-3d "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_Force3D(geom) | 2D GEOMETRY → 3D GEOMETRY |

#### Geometry creation functions (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-creation-functions-2d "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| h | ST\_BoundingCircle(geom) | Returns the minimum bounding circle of _geom_ |
| h | ST\_Expand(geom, distance) | Expands _geom_’s envelope |
| h | ST\_Expand(geom, deltaX, deltaY) | Expands _geom_’s envelope |
| h | ST\_MakeEllipse(point, width, height) | Constructs an ellipse |
| p | ST\_MakeEnvelope(xMin, yMin, xMax, yMax \[, srid \]) | Creates a rectangular POLYGON |
| h | ST\_MakeGrid(geom, deltaX, deltaY) | Calculates a regular grid of POLYGONs based on _geom_ |
| h | ST\_MakeGridPoints(geom, deltaX, deltaY) | Calculates a regular grid of points based on _geom_ |
| o | ST\_MakeLine(point1 \[, point \]\*) | Creates a line-string from the given POINTs (or MULTIPOINTs) |
| p | ST\_MakePoint(x, y \[, z \]) | Synonym for `ST_Point` |
| p | ST\_MakePolygon(lineString \[, hole \]\*) | Creates a POLYGON from _lineString_ with the given holes (which are required to be closed LINESTRINGs) |
| h | ST\_MinimumDiameter(geom) | Returns the minimum diameter of _geom_ |
| h | ST\_MinimumRectangle(geom) | Returns the minimum rectangle enclosing _geom_ |
| h | ST\_OctogonalEnvelope(geom) | Returns the octogonal envelope of _geom_ |
| o | ST\_Point(x, y \[, z \]) | Constructs a point from two or three coordinates |

Not implemented:

- ST\_RingBuffer(geom, distance, bufferCount \[, endCapStyle \[, doDifference\]\]) Returns a MULTIPOLYGON of buffers centered at _geom_ and of increasing buffer size

### Geometry creation functions (3D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-creation-functions-3d "Permalink")

Not implemented:

- ST\_Extrude(geom, height \[, flag\]) Extrudes a GEOMETRY
- ST\_GeometryShadow(geom, point, height) Computes the shadow footprint of _geom_
- ST\_GeometryShadow(geom, azimuth, altitude, height \[, unify \]) Computes the shadow footprint of _geom_

#### Geometry properties (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-properties-2d "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_Boundary(geom \[, srid \]) | Returns the boundary of _geom_ |
| o | ST\_Centroid(geom) | Returns the centroid of _geom_ |
| o | ST\_CoordDim(geom) | Returns the dimension of the coordinates of _geom_ |
| o | ST\_Dimension(geom) | Returns the dimension of _geom_ |
| o | ST\_Distance(geom1, geom2) | Returns the distance between _geom1_ and _geom2_ |
| h | ST\_ExteriorRing(geom) | Returns the exterior ring of _geom_, or null if _geom_ is not a polygon |
| o | ST\_GeometryType(geom) | Returns the type of _geom_ |
| o | ST\_GeometryTypeCode(geom) | Returns the OGC SFS type code of _geom_ |
| p | ST\_EndPoint(lineString) | Returns the last coordinate of _geom_ |
| o | ST\_Envelope(geom \[, srid \]) | Returns the envelope of _geom_ (which may be a GEOMETRYCOLLECTION) as a GEOMETRY |
| o | ST\_Extent(geom) | Returns the minimum bounding box of _geom_ (which may be a GEOMETRYCOLLECTION) |
| h | ST\_GeometryN(geomCollection, n) | Returns the _n_ th GEOMETRY of _geomCollection_ |
| h | ST\_InteriorRingN(geom) | Returns the nth interior ring of _geom_, or null if _geom_ is not a polygon |
| h | ST\_IsClosed(geom) | Returns whether _geom_ is a closed LINESTRING or MULTILINESTRING |
| o | ST\_IsEmpty(geom) | Returns whether _geom_ is empty |
| o | ST\_IsRectangle(geom) | Returns whether _geom_ is a rectangle |
| h | ST\_IsRing(geom) | Returns whether _geom_ is a closed and simple line-string or MULTILINESTRING |
| o | ST\_IsSimple(geom) | Returns whether _geom_ is simple |
| o | ST\_IsValid(geom) | Returns whether _geom_ is valid |
| h | ST\_NPoints(geom) | Returns the number of points in _geom_ |
| h | ST\_NumGeometries(geom) | Returns the number of geometries in _geom_ (1 if it is not a GEOMETRYCOLLECTION) |
| h | ST\_NumInteriorRing(geom) | Synonym for `ST_NumInteriorRings` |
| h | ST\_NumInteriorRings(geom) | Returns the number of interior rings of _geom_ |
| h | ST\_NumPoints(geom) | Returns the number of points in _geom_ |
| p | ST\_PointN(geom, n) | Returns the _n_ th point of a _geom_ |
| p | ST\_PointOnSurface(geom) | Returns an interior or boundary point of _geom_ |
| o | ST\_SRID(geom) | Returns SRID value of _geom_ or 0 if it does not have one |
| p | ST\_StartPoint(geom) | Returns the first point of _geom_ |
| o | ST\_X(geom) | Returns the x-value of the first coordinate of _geom_ |
| o | ST\_XMax(geom) | Returns the maximum x-value of _geom_ |
| o | ST\_XMin(geom) | Returns the minimum x-value of _geom_ |
| o | ST\_Y(geom) | Returns the y-value of the first coordinate of _geom_ |
| o | ST\_YMax(geom) | Returns the maximum y-value of _geom_ |
| o | ST\_YMin(geom) | Returns the minimum y-value of _geom_ |

Not implemented:

- ST\_CompactnessRatio(polygon) Returns the square root of _polygon_’s area divided by the area of the circle with circumference equal to its perimeter
- ST\_Explode(query \[, fieldName\]) Explodes the GEOMETRYCOLLECTIONs in the _fieldName_ column of a query into multiple geometries
- ST\_IsValidDetail(geom \[, selfTouchValid \]) Returns a valid detail as an array of objects
- ST\_IsValidReason(geom \[, selfTouchValid \]) Returns text stating whether _geom_ is valid, and if not valid, a reason why

#### Geometry properties (3D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-properties-3d "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| p | ST\_Is3D(s) | Returns whether _geom_ has at least one z-coordinate |
| o | ST\_Z(geom) | Returns the z-value of the first coordinate of _geom_ |
| o | ST\_ZMax(geom) | Returns the maximum z-value of _geom_ |
| o | ST\_ZMin(geom) | Returns the minimum z-value of _geom_ |

### Geometry predicates [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-predicates "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_Contains(geom1, geom2) | Returns whether _geom1_ contains _geom2_ |
| p | ST\_ContainsProperly(geom1, geom2) | Returns whether _geom1_ contains _geom2_ but does not intersect its boundary |
| p | ST\_CoveredBy(geom1, geom2) | Returns whether no point in _geom1_ is outside _geom2_. |
| p | ST\_Covers(geom1, geom2) | Returns whether no point in _geom2_ is outside _geom1_ |
| o | ST\_Crosses(geom1, geom2) | Returns whether _geom1_ crosses _geom2_ |
| o | ST\_Disjoint(geom1, geom2) | Returns whether _geom1_ and _geom2_ are disjoint |
| p | ST\_DWithin(geom1, geom2, distance) | Returns whether _geom1_ and _geom_ are within _distance_ of one another |
| o | ST\_EnvelopesIntersect(geom1, geom2) | Returns whether the envelope of _geom1_ intersects the envelope of _geom2_ |
| o | ST\_Equals(geom1, geom2) | Returns whether _geom1_ equals _geom2_ |
| o | ST\_Intersects(geom1, geom2) | Returns whether _geom1_ intersects _geom2_ |
| o | ST\_Overlaps(geom1, geom2) | Returns whether _geom1_ overlaps _geom2_ |
| o | ST\_Relate(geom1, geom2) | Returns the DE-9IM intersection matrix of _geom1_ and _geom2_ |
| o | ST\_Relate(geom1, geom2, iMatrix) | Returns whether _geom1_ and _geom2_ are related by the given intersection matrix _iMatrix_ |
| o | ST\_Touches(geom1, geom2) | Returns whether _geom1_ touches _geom2_ |
| o | ST\_Within(geom1, geom2) | Returns whether _geom1_ is within _geom2_ |

Not implemented:

- ST\_OrderingEquals(geom1, geom2) Returns whether _geom1_ equals _geom2_ and their coordinates and component Geometries are listed in the same order

#### Geometry operators (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-operators-2d "Permalink")

The following functions combine 2D geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| p | ST\_Buffer(geom, distance \[, quadSegs, endCapStyle \]) | Computes a buffer around _geom_ |
| p | ST\_Buffer(geom, distance \[, bufferStyle \]) | Computes a buffer around _geom_ |
| o | ST\_ConvexHull(geom) | Computes the smallest convex polygon that contains all the points in _geom_ |
| o | ST\_Difference(geom1, geom2) | Computes the difference between two geometries |
| o | ST\_SymDifference(geom1, geom2) | Computes the symmetric difference between two geometries |
| o | ST\_Intersection(geom1, geom2) | Computes the intersection of _geom1_ and _geom2_ |
| p | ST\_OffsetCurve(geom, distance, bufferStyle) | Computes an offset line for _linestring_ |
| o | ST\_Union(geom1, geom2) | Computes the union of _geom1_ and _geom2_ |
| o | ST\_Union(geomCollection) | Computes the union of the geometries in _geomCollection_ |

See also: the `ST_Union` aggregate function.

#### Affine transformation functions (3D and 2D) [Permalink](https://calcite.apache.org/docs/reference.html\#affine-transformation-functions-3d-and-2d "Permalink")

The following functions transform 2D geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_Rotate(geom, angle \[, origin \| x, y\]) | Rotates a _geom_ counter-clockwise by _angle_ (in radians) about _origin_ (or the point ( _x_, _y_)) |
| o | ST\_Scale(geom, xFactor, yFactor) | Scales _geom_ by multiplying the ordinates by the indicated scale factors |
| o | ST\_Translate(geom, x, y) | Translates _geom_ by the vector (x, y) |

Not implemented:

- ST\_Scale(geom, xFactor, yFactor \[, zFactor \]) Scales _geom_ by multiplying the ordinates by the indicated scale factors
- ST\_Translate(geom, x, y, \[, z\]) Translates _geom_

#### Geometry editing functions (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-editing-functions-2d "Permalink")

The following functions modify 2D geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| p | ST\_AddPoint(linestring, point \[, index\]) | Adds _point_ to _linestring_ at a given _index_ (or at the end if _index_ is not specified) |
| h | ST\_Densify(geom, tolerance) | Densifies a _geom_ by inserting extra vertices along the line segments |
| h | ST\_FlipCoordinates(geom) | Flips the X and Y coordinates of the _geom_ |
| h | ST\_Holes(geom) | Returns the holes in the _geom_ (which may be a GEOMETRYCOLLECTION) |
| h | ST\_Normalize(geom) | Converts the _geom_ to normal form |
| p | ST\_RemoveRepeatedPoints(geom \[, tolerance\]) | Removes duplicated coordinates from the _geom_ |
| h | ST\_RemoveHoles(geom) | Removes the holes of the _geom_ |
| p | ST\_RemovePoint(linestring, index) | Remove _point_ at given _index_ in _linestring_ |
| h | ST\_Reverse(geom) | Reverses the order of the coordinates of the _geom_ |

Not implemented:

- ST\_CollectionExtract(geom, dimension) Filters _geom_, returning a multi-geometry of those members with a given _dimension_ (1 = point, 2 = line-string, 3 = polygon)

#### Geometry editing functions (3D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-editing-functions-3d "Permalink")

The following functions modify 3D geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| h | ST\_AddZ(geom, zToAdd) | Adds _zToAdd_ to the z-coordinate of _geom_ |

Not implemented:

- ST\_Interpolate3DLine(geom) Returns _geom_ with an interpolation of z values, or null if it is not a line-string or MULTILINESTRING
- ST\_MultiplyZ(geom, zFactor) Returns _geom_ with its z-values multiplied by _zFactor_
- ST\_Reverse3DLine(geom \[, sortOrder \]) Potentially reverses _geom_ according to the z-values of its first and last coordinates
- ST\_UpdateZ(geom, newZ \[, updateCondition \]) Updates the z-values of _geom_
- ST\_ZUpdateLineExtremities(geom, startZ, endZ \[, interpolate \]) Updates the start and end z-values of _geom_

#### Geometry measurement functions (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-measurement-functions-2d "Permalink")

The following functions measure geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_Area(geom) | Returns the area of _geom_ (which may be a GEOMETRYCOLLECTION) |
| h | ST\_ClosestCoordinate(point, geom) | Returns the coordinate(s) of _geom_ closest to _point_ |
| h | ST\_ClosestPoint(geom1, geom2) | Returns the point of _geom1_ closest to _geom2_ |
| h | ST\_FurthestCoordinate(geom, point) | Returns the coordinate(s) of _geom_ that are furthest from _point_ |
| h | ST\_Length(geom) | Returns the length of _geom_ |
| h | ST\_LocateAlong(geom, segmentLengthFraction, offsetDistance) | Returns a MULTIPOINT containing points along the line segments of _geom_ at _segmentLengthFraction_ and _offsetDistance_ |
| h | ST\_LongestLine(geom1, geom2) | Returns the 2-dimensional longest line-string between the points of _geom1_ and _geom2_ |
| h | ST\_MaxDistance(geom1, geom2) | Computes the maximum distance between _geom1_ and _geom2_ |
| h | ST\_Perimeter(polygon) | Returns the length of the perimeter of _polygon_ (which may be a MULTIPOLYGON) |
| h | ST\_ProjectPoint(point, lineString) | Projects _point_ onto a _lineString_ (which may be a MULTILINESTRING) |

#### Geometry measurement functions (3D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-measurement-functions-3d "Permalink")

Not implemented:

- ST\_3DArea(geom) Return a polygon’s 3D area
- ST\_3DLength(geom) Returns the 3D length of a line-string
- ST\_3DPerimeter(geom) Returns the 3D perimeter of a polygon or MULTIPOLYGON
- ST\_SunPosition(point \[, timestamp \]) Computes the sun position at _point_ and _timestamp_ (now by default)

#### Geometry processing functions (2D) [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-processing-functions-2d "Permalink")

The following functions process geometries.

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_LineMerge(geom) | Merges a collection of linear components to form a line-string of maximal length |
| o | ST\_MakeValid(geom) | Makes a valid geometry of a given invalid geometry |
| o | ST\_Polygonize(geom) | Creates a MULTIPOLYGON from edges of _geom_ |
| o | ST\_PrecisionReducer(geom, n) | Reduces _geom_’s precision to _n_ decimal places |
| o | ST\_Simplify(geom, distance) | Simplifies _geom_ using the [Douglas-Peuker algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) with a _distance_ tolerance |
| o | ST\_SimplifyPreserveTopology(geom, distance) | Simplifies _geom_, preserving its topology |
| o | ST\_Snap(geom1, geom2, tolerance) | Snaps _geom1_ and _geom2_ together |
| p | ST\_Split(geom, blade) | Splits _geom_ by _blade_ |

Not implemented:

- ST\_LineIntersector(geom1, geom2) Splits _geom1_ (a line-string) with _geom2_
- ST\_LineMerge(geom) Merges a collection of linear components to form a line-string of maximal length
- ST\_MakeValid(geom \[, preserveGeomDim \[, preserveDuplicateCoord \[, preserveCoordDim\]\]\]) Makes _geom_ valid
- ST\_RingSideBuffer(geom, distance, bufferCount \[, endCapStyle \[, doDifference\]\]) Computes a ring buffer on one side
- ST\_SideBuffer(geom, distance \[, bufferStyle \]) Compute a single buffer on one side

#### Geometry projection functions [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-projection-functions "Permalink")

The EPSG dataset is released separately from Proj4J due
to its restrictive [terms of use](https://epsg.org/terms-of-use.html).
In order to use the projection functions in Apache Calcite,
users must include the EPSG dataset in their dependencies.

| C | Operator syntax | Description |
| --- | --- | --- |
| o | ST\_SetSRID(geom, srid) | Returns a copy of _geom_ with a new SRID |
| o | ST\_Transform(geom, srid) | Transforms _geom_ from one coordinate reference system (CRS) to the CRS specified by _srid_ |

#### Trigonometry functions [Permalink](https://calcite.apache.org/docs/reference.html\#trigonometry-functions "Permalink")

Not implemented:

- ST\_Azimuth(point1, point2) Return the azimuth of the segment from _point1_ to _point2_

#### Topography functions [Permalink](https://calcite.apache.org/docs/reference.html\#topography-functions "Permalink")

Not implemented:

- ST\_TriangleAspect(geom) Returns the aspect of a triangle
- ST\_TriangleContouring(query \[, z1, z2, z3 \]\[, varArgs \]\*) Splits triangles into smaller triangles according to classes
- ST\_TriangleDirection(geom) Computes the direction of steepest ascent of a triangle and returns it as a line-string
- ST\_TriangleSlope(geom) Computes the slope of a triangle as a percentage
- ST\_Voronoi(geom \[, outDimension \[, envelopePolygon \]\]) Creates a Voronoi diagram

#### Triangulation functions [Permalink](https://calcite.apache.org/docs/reference.html\#triangulation-functions "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| h | ST\_ConstrainedDelaunay(geom \[, flag\]) | Computes a constrained Delaunay triangulation based on _geom_ |
| h | ST\_Delaunay(geom \[, flag\]) | Computes a Delaunay triangulation based on points in _geom_ |

Not implemented:

- ST\_Tessellate(polygon) Tessellates _polygon_ (may be MULTIPOLYGON) with adaptive triangles

#### Geometry aggregate functions [Permalink](https://calcite.apache.org/docs/reference.html\#geometry-aggregate-functions "Permalink")

| C | Operator syntax | Description |
| --- | --- | --- |
| h | ST\_Accum(geom) | Accumulates _geom_ into an array |
| h | ST\_Collect(geom) | Collects _geom_ into a GeometryCollection |
| h | ST\_Union(geom) | Computes the union of the geometries in _geom_ |

### JSON Functions [Permalink](https://calcite.apache.org/docs/reference.html\#json-functions "Permalink")

In the following:

- _jsonValue_ is a character string containing a JSON value;
- _path_ is a character string containing a JSON path expression; mode flag `strict` or `lax` should be specified in the beginning of _path_.

#### Query Functions [Permalink](https://calcite.apache.org/docs/reference.html\#query-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| JSON\_EXISTS(jsonValue, path \[ { TRUE \| FALSE \| UNKNOWN \| ERROR } ON ERROR \] ) | Whether a _jsonValue_ satisfies a search criterion described using JSON path expression _path_ |
| JSON\_VALUE(jsonValue, path \[ RETURNING type \] \[ { ERROR \| NULL \| DEFAULT expr } ON EMPTY \] \[ { ERROR \| NULL \| DEFAULT expr } ON ERROR \] ) | Extract an SQL scalar from a _jsonValue_ using JSON path expression _path_ |
| JSON\_QUERY(jsonValue, path \[ { WITHOUT \[ ARRAY \] \| WITH \[ CONDITIONAL \| UNCONDITIONAL \] \[ ARRAY \] } WRAPPER \] \[ { ERROR \| NULL \| EMPTY ARRAY \| EMPTY OBJECT } ON EMPTY \] \[ { ERROR \| NULL \| EMPTY ARRAY \| EMPTY OBJECT } ON ERROR \] ) | Extract a JSON object or JSON array from _jsonValue_ using the _path_ JSON path expression |

Note:

- The `ON ERROR` and `ON EMPTY` clauses define the fallback
behavior of the function when an error is thrown or a null value
is about to be returned.
- The `ARRAY WRAPPER` clause defines how to represent a JSON array result
in `JSON_QUERY` function. The following examples compare the wrapper
behaviors.

Example Data:

```json
{"a": "[1,2]", "b": [1,2], "c": "hi"}
```

Comparison:

| Operator | $.a | $.b | $.c |
| --- | --- | --- | --- |
| JSON\_VALUE | \[1, 2\] | error | hi |
| JSON QUERY WITHOUT ARRAY WRAPPER | error | \[1, 2\] | error |
| JSON QUERY WITH UNCONDITIONAL ARRAY WRAPPER | \[ “\[1,2\]” \] | \[ \[1,2\] \] | \[ “hi” \] |
| JSON QUERY WITH CONDITIONAL ARRAY WRAPPER | \[ “\[1,2\]” \] | \[1,2\] | \[ “hi” \] |

Not implemented:

- JSON\_TABLE

#### Constructor Functions [Permalink](https://calcite.apache.org/docs/reference.html\#constructor-functions "Permalink")

| Operator syntax | Description |
| --- | --- |
| JSON\_OBJECT( jsonKeyVal \[, jsonKeyVal \]\* \[ nullBehavior \] ) | Construct JSON object using a series of key-value pairs |
| JSON\_OBJECTAGG( jsonKeyVal \[ nullBehavior \] ) | Aggregate function to construct a JSON object using a key-value pair |
| JSON\_ARRAY( \[ jsonVal \[, jsonVal \]\* \] \[ nullBehavior \] ) | Construct a JSON array using a series of values |
| JSON\_ARRAYAGG( jsonVal \[ ORDER BY orderItem \[, orderItem \]\* \] \[ nullBehavior \] ) | Aggregate function to construct a JSON array using a value |

```sql
jsonKeyVal:
      [ KEY ] name VALUE value [ FORMAT JSON ]
  |   name : value [ FORMAT JSON ]

jsonVal:
      value [ FORMAT JSON ]

nullBehavior:
      NULL ON NULL
  |   ABSENT ON NULL
```

Note:

- The flag `FORMAT JSON` indicates the value is formatted as JSON
character string. When `FORMAT JSON` is used, the value should be
de-parse from JSON character string to a SQL structured value.
- `ON NULL` clause defines how the JSON output represents null
values. The default null behavior of `JSON_OBJECT` and
`JSON_OBJECTAGG` is `NULL ON NULL`, and for `JSON_ARRAY` and
`JSON_ARRAYAGG` it is `ABSENT ON NULL`.
- If `ORDER BY` clause is provided, `JSON_ARRAYAGG` sorts the
input rows into the specified order before performing aggregation.

#### Comparison Operators [Permalink](https://calcite.apache.org/docs/reference.html\#comparison-operators-1 "Permalink")

| Operator syntax | Description |
| --- | --- |
| jsonValue IS JSON \[ VALUE \] | Whether _jsonValue_ is a JSON value |
| jsonValue IS NOT JSON \[ VALUE \] | Whether _jsonValue_ is not a JSON value |
| jsonValue IS JSON SCALAR | Whether _jsonValue_ is a JSON scalar value |
| jsonValue IS NOT JSON SCALAR | Whether _jsonValue_ is not a JSON scalar value |
| jsonValue IS JSON OBJECT | Whether _jsonValue_ is a JSON object |
| jsonValue IS NOT JSON OBJECT | Whether _jsonValue_ is not a JSON object |
| jsonValue IS JSON ARRAY | Whether _jsonValue_ is a JSON array |
| jsonValue IS NOT JSON ARRAY | Whether _jsonValue_ is not a JSON array |

Note:

- If the _jsonValue_ is `NULL`, the function will return `NULL`.

### Dialect-specific Operators [Permalink](https://calcite.apache.org/docs/reference.html\#dialect-specific-operators "Permalink")

The following operators are not in the SQL standard, and are not enabled in
Calcite’s default operator table. They are only available for use in queries
if your session has enabled an extra operator table.

To enable an operator table, set the
[fun](https://calcite.apache.org/docs/adapter.html#jdbc-connect-string-parameters)
connect string parameter.

The ‘C’ (compatibility) column contains value:

- ‘\*’ for all libraries,
- ‘b’ for Google BigQuery (‘fun=bigquery’ in the connect string),
- ‘c’ for Apache Calcite (‘fun=calcite’ in the connect string),
- ‘f’ for Snowflake (‘fun=snowflake’ in the connect string),
- ‘h’ for Apache Hive (‘fun=hive’ in the connect string),
- ‘m’ for MySQL (‘fun=mysql’ in the connect string),
- ‘q’ for Microsoft SQL Server (‘fun=mssql’ in the connect string),
- ‘o’ for Oracle (‘fun=oracle’ in the connect string),
- ‘p’ for PostgreSQL (‘fun=postgresql’ in the connect string),
- ‘r’ for Amazon RedShift (‘fun=redshift’ in the connect string),
- ’s’ for Apache Spark (‘fun=spark’ in the connect string).
- ‘i’ for ClickHouse(‘fun=clickhouse’ in the connect string).

One operator name may correspond to multiple SQL dialects, but with different
semantics.

BigQuery’s type system uses confusingly different names for types and functions:

- BigQuery’s `DATETIME` type represents a local date time, and corresponds to
Calcite’s `TIMESTAMP` type;
- BigQuery’s `TIMESTAMP` type represents an instant, and corresponds to
Calcite’s `TIMESTAMP WITH LOCAL TIME ZONE` type;
- The _timestampLtz_ parameter, for instance in `DATE(timestampLtz)`, has
Calcite type `TIMESTAMP WITH LOCAL TIME ZONE`;
- The `TIMESTAMP(string)` function, designed to be compatible the BigQuery
function, return a Calcite `TIMESTAMP WITH LOCAL TIME ZONE`;
- Similarly, `DATETIME(string)` returns a Calcite `TIMESTAMP`.

In the following:

- _func_ is a lambda argument.

| C | Operator syntax | Description |
| --- | --- | --- |
| p | expr :: type | Casts _expr_ to _type_ |
| m | expr1 <=> expr2 | Whether two values are equal, treating null values as the same, and it’s similar to `IS NOT DISTINCT FROM` |
| p | ACOSD(numeric) | Returns the inverse cosine of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. Fails if _numeric_ is less than -1.0 or greater than 1.0. |
| \* | ACOSH(numeric) | Returns the inverse hyperbolic cosine of _numeric_ |
| o s | ADD\_MONTHS(date, numMonths) | Returns the date that is _numMonths_ after _date_ |
| h s | ARRAY(\[expr \[, expr \]\*\]) | Construct an array in Apache Spark. The function allows users to use `ARRAY()` to create an empty array |
| s | ARRAY\_APPEND(array, element) | Appends an _element_ to the end of the _array_ and returns the result. Type of _element_ should be similar to type of the elements of the _array_. If the _array_ is null, the function will return null. If an _element_ that is null, the null _element_ will be added to the end of the _array_ |
| s | ARRAY\_COMPACT(array) | Removes null values from the _array_ |
| b | ARRAY\_CONCAT(array \[, array \]\*) | Concatenates one or more arrays. If any input argument is `NULL` the function returns `NULL` |
| s | ARRAY\_CONTAINS(array, element) | Returns true if the _array_ contains the _element_ |
| h s | ARRAY\_DISTINCT(array) | Removes duplicate values from the _array_ that keeps ordering of elements |
| h s | ARRAY\_EXCEPT(array1, array2) | Returns an array of the elements in _array1_ but not in _array2_, without duplicates |
| s | ARRAY\_INSERT(array, pos, element) | Places _element_ into index _pos_ of _array_. Array index start at 1, or start from the end if index is negative. Index above array size appends the array, or prepends the array if index is negative, with `NULL` elements. |
| h s | ARRAY\_INTERSECT(array1, array2) | Returns an array of the elements in the intersection of _array1_ and _array2_, without duplicates |
| h s | ARRAY\_JOIN(array, delimiter \[, nullText \]) | Synonym for `ARRAY_TO_STRING` |
| b | ARRAY\_LENGTH(array) | Synonym for `CARDINALITY` |
| h s | ARRAY\_MAX(array) | Returns the maximum value in the _array_ |
| h s | ARRAY\_MIN(array) | Returns the minimum value in the _array_ |
| s | ARRAY\_POSITION(array, element) | Returns the (1-based) index of the first _element_ of the _array_ as long |
| h s | ARRAY\_REMOVE(array, element) | Remove all elements that equal to _element_ from the _array_ |
| s | ARRAY\_PREPEND(array, element) | Appends an _element_ to the beginning of the _array_ and returns the result. Type of _element_ should be similar to type of the elements of the _array_. If the _array_ is null, the function will return null. If an _element_ that is null, the null _element_ will be added to the beginning of the _array_ |
| s | ARRAY\_REPEAT(element, count) | Returns the array containing element count times. |
| b | ARRAY\_REVERSE(array) | Reverses elements of _array_ |
| s | ARRAY\_SIZE(array) | Synonym for `CARDINALITY` |
| h | ARRAY\_SLICE(array, start, length) | Returns the subset or range of elements. |
| b | ARRAY\_TO\_STRING(array, delimiter \[, nullText \]) | Returns a concatenation of the elements in _array_ as a STRING and take _delimiter_ as the delimiter. If the _nullText_ parameter is used, the function replaces any `NULL` values in the array with the value of _nullText_. If the _nullText_ parameter is not used, the function omits the `NULL` value and its preceding delimiter. Returns `NULL` if any argument is `NULL` |
| h s | ARRAY\_UNION(array1, array2) | Returns an array of the elements in the union of _array1_ and _array2_, without duplicates |
| s | ARRAYS\_OVERLAP(array1, array2) | Returns true if _array1 contains at least a non-null element present also in \*array2_. If the arrays have no common element and they are both non-empty and either of them contains a null element null is returned, false otherwise |
| s | ARRAYS\_ZIP(array \[, array \]\*) | Returns a merged _array_ of structs in which the N-th struct contains all N-th values of input arrays |
| s | SORT\_ARRAY(array \[, ascendingOrder\]) | Sorts the _array_ in ascending or descending order according to the natural ordering of the array elements. The default order is ascending if _ascendingOrder_ is not specified. Null elements will be placed at the beginning of the returned array in ascending order or at the end of the returned array in descending order |
| p | ASIND(numeric) | Returns the inverse sine of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. Fails if _numeric_ is less than -1.0 or greater than 1.0. |
| \* | ASINH(numeric) | Returns the inverse hyperbolic sine of _numeric_ |
| p | ATAND(numeric) | Returns the inverse tangent of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. |
| \* | ATANH(numeric) | Returns the inverse hyperbolic tangent of _numeric_ |
| \* | BITAND(value1, value2) | Returns the bitwise AND of _value1_ and _value2_. _value1_ and _value2_ must both be integer or binary values. Binary values must be of the same length. |
| \* | BITOR(value1, value2) | Returns the bitwise OR of _value1_ and _value2_. _value1_ and _value2_ must both be integer or binary values. Binary values must be of the same length. |
| \* | BITXOR(value1, value2) | Returns the bitwise XOR of _value1_ and _value2_. _value1_ and _value2_ must both be integer or binary values. Binary values must be of the same length. |
| \* | LEFTSHIFT(value1, value2) | Returns the result of left-shifting _value1_ by _value2_ bits. _value1_ can be integer, unsigned integer, or binary. For binary, the result has the same length as _value1_. The shift amount _value2_ is normalized using modulo arithmetic based on the bit width of _value1_. For integers, this uses modulo 32; for binary types, it uses modulo (8 × byte\_length). Negative shift amounts are converted to equivalent positive shifts through this modulo operation. For example, `LEFTSHIFT(1, -2)` returns `1073741824` (equivalent to `1 << 30`), and `LEFTSHIFT(8, -1)` returns `0` due to overflow. |
| \* | BITNOT(value) | Returns the bitwise NOT of _value_. _value_ must be either an integer type or a binary value. |
| f | BITAND\_AGG(value) | Equivalent to `BIT_AND(value)` |
| f | BITOR\_AGG(value) | Equivalent to `BIT_OR(value)` |
| \* | BITCOUNT(value) | Returns the bitwise COUNT of _value_ or NULL if _value_ is NULL. _value_ must be and integer or binary value. |
| b s | BIT\_COUNT(integer) | Returns the bitwise COUNT of _integer_ or NULL if _integer_ is NULL |
| m | BIT\_COUNT(numeric) | Returns the bitwise COUNT of the integer portion of _numeric_ or NULL if _numeric_ is NULL |
| b m s | BIT\_COUNT(binary) | Returns the bitwise COUNT of _binary_ or NULL if _binary_ is NULL |
| s | BIT\_LENGTH(binary) | Returns the bit length of _binary_ |
| s | BIT\_LENGTH(string) | Returns the bit length of _string_ |
| s | BIT\_GET(value, position) | Returns the bit (0 or 1) value at the specified _position_ of numeric _value_. The positions are numbered from right to left, starting at zero. The _position_ argument cannot be negative |
| b | CEIL(value) | Similar to standard `CEIL(value)` except if _value_ is an integer type, the return type is a double |
| m s | CHAR(integer) | Returns the character whose ASCII code is _integer_ % 256, or null if _integer_ < 0 |
| b o p r | CHR(integer) | Returns the character whose UTF-8 code is _integer_ |
| b | CODE\_POINTS\_TO\_BYTES(integers) | Converts _integers_, an array of integers between 0 and 255 inclusive, into bytes; throws error if any element is out of range |
| b | CODE\_POINTS\_TO\_STRING(integers) | Converts _integers_, an array of integers between 0 and 0xD7FF or between 0xE000 and 0x10FFFF inclusive, into string; throws error if any element is out of range |
| o r | CONCAT(string, string) | Concatenates two strings, returns null only when both string arguments are null, otherwise treats null as empty string |
| b m | CONCAT(string \[, string \]\*) | Concatenates one or more strings, returns null if any of the arguments is null |
| p q | CONCAT(string \[, string \]\*) | Concatenates one or more strings, null is treated as empty string |
| m | CONCAT\_WS(separator, str1 \[, string \]\*) | Concatenates one or more strings, returns null only when separator is null, otherwise treats null arguments as empty strings |
| p | CONCAT\_WS(separator, any \[, any \]\*) | Concatenates all but the first argument, returns null only when separator is null, otherwise treats null arguments as empty strings |
| q | CONCAT\_WS(separator, str1, str2 \[, string \]\*) | Concatenates two or more strings, requires at least 3 arguments (up to 254), treats null arguments as empty strings |
| s | CONCAT\_WS(separator \[, string \| array(string)\]\*) | Concatenates one or more strings or arrays. Besides the separator, other arguments can include strings or string arrays. returns null only when separator is null, treats other null arguments as empty strings |
| m | COMPRESS(string) | Compresses a string using zlib compression and returns the result as a binary string |
| b | CONTAINS\_SUBSTR(expression, string \[ , json\_scope => json\_scope\_value \]) | Returns whether _string_ exists as a substring in _expression_. Optional _json\_scope_ argument specifies what scope to search if _expression_ is in JSON format. Returns NULL if a NULL exists in _expression_ that does not result in a match |
| q | CONVERT(type, expression \[ , style \]) | Equivalent to `CAST(expression AS type)`; ignores the _style_ operand |
| o | CONVERT(string, destCharSet\[, srcCharSet\]) | Converts _string_ from _srcCharSet_ to _destCharSet_. If the _srcCharSet_ parameter is not specified, then it uses the default CharSet |
| r | CONVERT\_TIMEZONE(tz1, tz2, datetime) | Converts the timezone of _datetime_ from _tz1_ to _tz2_ |
| p | COSD(numeric) | Returns the cosine of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. Fails if _numeric_ is greater than the maximum double value. |
| \* | COSH(numeric) | Returns the hyperbolic cosine of _numeric_ |
| \* | COTH(numeric) | Returns the hyperbolic cotangent of _numeric_ |
| s h | CRC32(string) | Calculates a cyclic redundancy check value for string or binary argument and returns bigint value |
| \* | CSC(numeric) | Returns the cosecant of _numeric_ in radians |
| \* | CSCH(numeric) | Returns the hyperbolic cosecant of _numeric_ |
| b | CURRENT\_DATETIME(\[ timeZone \]) | Returns the current time as a TIMESTAMP from _timezone_ |
| m | DAYNAME(datetime) | Returns the name, in the connection’s locale, of the weekday in _datetime_; for example, for a locale of en, it will return ‘Sunday’ for both DATE ‘2020-02-10’ and TIMESTAMP ‘2020-02-10 10:10:10’, and for a locale of zh, it will return ‘星期日’ |
| b | DATE(timestamp) | Extracts the DATE from a _timestamp_ |
| b | DATE(timestampLtz) | Extracts the DATE from _timestampLtz_ (an instant; BigQuery’s TIMESTAMP type), assuming UTC |
| b | DATE(timestampLtz, timeZone) | Extracts the DATE from _timestampLtz_ (an instant; BigQuery’s TIMESTAMP type) in _timeZone_ |
| b | DATE(string) | Equivalent to `CAST(string AS DATE)` |
| b | DATE(year, month, day) | Returns a DATE value for _year_, _month_, and _day_ (all of type INTEGER) |
| q r f | DATEADD(timeUnit, integer, datetime) | Equivalent to `TIMESTAMPADD(timeUnit, integer, datetime)` |
| q r f | DATEDIFF(timeUnit, datetime, datetime2) | Equivalent to `TIMESTAMPDIFF(timeUnit, datetime, datetime2)` |
| q | DATEPART(timeUnit, datetime) | Equivalent to `EXTRACT(timeUnit FROM  datetime)` |
| b | DATETIME(date, time) | Converts _date_ and _time_ to a TIMESTAMP |
| b | DATETIME(date) | Converts _date_ to a TIMESTAMP value (at midnight) |
| b | DATETIME(date, timeZone) | Converts _date_ to a TIMESTAMP value (at midnight), in _timeZone_ |
| b | DATETIME(year, month, day, hour, minute, second) | Creates a TIMESTAMP for _year_, _month_, _day_, _hour_, _minute_, _second_ (all of type INTEGER) |
| b | DATETIME\_ADD(timestamp, interval) | Returns the TIMESTAMP value that occurs _interval_ after _timestamp_ |
| b | DATETIME\_DIFF(timestamp, timestamp2, timeUnit) | Returns the whole number of _timeUnit_ between _timestamp_ and _timestamp2_ |
| b | DATETIME\_SUB(timestamp, interval) | Returns the TIMESTAMP that occurs _interval_ before _timestamp_ |
| b | DATETIME\_TRUNC(timestamp, timeUnit) | Truncates _timestamp_ to the granularity of _timeUnit_, rounding to the beginning of the unit |
| b s | DATE\_FROM\_UNIX\_DATE(integer) | Returns the DATE that is _integer_ days after 1970-01-01 |
| p r | DATE\_PART(timeUnit, datetime) | Equivalent to `EXTRACT(timeUnit FROM  datetime)` |
| b | DATE\_ADD(date, interval) | Returns the DATE value that occurs _interval_ after _date_ |
| s h | DATE\_ADD(date, numDays) | Returns the DATE that is _numDays_ after _date_ |
| b | DATE\_DIFF(date, date2, timeUnit) | Returns the whole number of _timeUnit_ between _date_ and _date2_ |
| b | DATE\_SUB(date, interval) | Returns the DATE value that occurs _interval_ before _date_ |
| s h | DATE\_SUB(date, numDays) | Returns the DATE that is _numDays_ before _date_ |
| b | DATE\_TRUNC(date, timeUnit) | Truncates _date_ to the granularity of _timeUnit_, rounding to the beginning of the unit |
| o r s h | DECODE(value, value1, result1 \[, valueN, resultN \]\* \[, default \]) | Compares _value_ to each _valueN_ value one by one; if _value_ is equal to a _valueN_, returns the corresponding _resultN_, else returns _default_, or NULL if _default_ is not specified |
| p r | DIFFERENCE(string, string) | Returns a measure of the similarity of two strings, namely the number of character positions that their `SOUNDEX` values have in common: 4 if the `SOUNDEX` values are same and 0 if the `SOUNDEX` values are totally different |
| f s | ENDSWITH(string1, string2) | Returns whether _string2_ is a suffix of _string1_ |
| b | ENDS\_WITH(string1, string2) | Equivalent to `ENDSWITH(string1, string2)` |
| s | EXISTS(array, func) | Returns whether a predicate _func_ holds for one or more elements in the _array_ |
| o | EXISTSNODE(xml, xpath, \[, namespaces \]) | Determines whether traversal of a XML document using a specified xpath results in any nodes. Returns 0 if no nodes remain after applying the XPath traversal on the document fragment of the element or elements matched by the XPath expression. Returns 1 if any nodes remain. The optional namespace value that specifies a default mapping or namespace mapping for prefixes, which is used when evaluating the XPath expression. |
| o | EXTRACT(xml, xpath, \[, namespaces \]) | Returns the XML fragment of the element or elements matched by the XPath expression. The optional namespace value that specifies a default mapping or namespace mapping for prefixes, which is used when evaluating the XPath expression |
| m | EXTRACTVALUE(xml, xpathExpr)) | Returns the text of the first text node which is a child of the element or elements matched by the XPath expression. |
| h s | FACTORIAL(integer) | Returns the factorial of _integer_, the range of _integer_ is \[0, 20\]. Otherwise, returns NULL |
| h s | FIND\_IN\_SET(matchStr, textStr) | Returns the index (1-based) of the given _matchStr_ in the comma-delimited _textStr_. Returns 0, if the given _matchStr_ is not found or if the _matchStr_ contains a comma. For example, FIND\_IN\_SET(‘bc’, ‘a,bc,def’) returns 2 |
| b | FLOOR(value) | Similar to standard `FLOOR(value)` except if _value_ is an integer type, the return type is a double |
| b | FORMAT\_DATE(string, date) | Formats _date_ according to the specified format _string_ |
| b | FORMAT\_DATETIME(string, timestamp) | Formats _timestamp_ according to the specified format _string_ |
| h s | FORMAT\_NUMBER(value, decimalVal) | Formats the number _value_ like ‘#,###,###.##’, rounded to decimal places _decimalVal_. If _decimalVal_ is 0, the result has no decimal point or fractional part |
| h s | FORMAT\_NUMBER(value, format) | Formats the number _value_ to MySQL’s FORMAT _format_, like ‘#,###,###.##0.00’ |
| b | FORMAT\_TIME(string, time) | Formats _time_ according to the specified format _string_ |
| b | FORMAT\_TIMESTAMP(string timestamp) | Formats _timestamp_ according to the specified format _string_ |
| s | GETBIT(value, position) | Equivalent to `BIT_GET(value, position)` |
| b o p r s h | GREATEST(expr \[, expr \]\*) | Returns the greatest of the expressions |
| b h s | IF(condition, value1, value2) | Returns _value1_ if _condition_ is TRUE, _value2_ otherwise |
| b s | IFNULL(value1, value2) | Equivalent to `NVL(value1, value2)` |
| p | string1 ILIKE string2 \[ ESCAPE string3 \] | Whether _string1_ matches pattern _string2_, ignoring case (similar to `LIKE`) |
| p | string1 NOT ILIKE string2 \[ ESCAPE string3 \] | Whether _string1_ does not match pattern _string2_, ignoring case (similar to `NOT LIKE`) |
| b h o | INSTR(string, substring \[, from \[, occurrence \] \]) | Returns the position of _substring_ in _string_, searching starting at _from_ (default 1), and until locating the nth _occurrence_ (default 1) of _substring_ |
| b h m o | INSTR(string, substring) | Equivalent to `POSITION(substring IN string)` |
| b | IS\_INF(value) | Returns whether _value_ is infinite |
| b | IS\_NAN(value) | Returns whether _value_ is NaN |
| m | JSON\_TYPE(jsonValue) | Returns a string value indicating the type of _jsonValue_ |
| m | JSON\_DEPTH(jsonValue) | Returns an integer value indicating the depth of _jsonValue_ |
| m | JSON\_PRETTY(jsonValue) | Returns a pretty-printing of _jsonValue_ |
| m | JSON\_LENGTH(jsonValue \[, path \]) | Returns a integer indicating the length of _jsonValue_ |
| m | JSON\_INSERT(jsonValue, path, val \[, path, val \]\*) | Returns a JSON document insert a data of _jsonValue_, _path_, _val_ |
| m | JSON\_KEYS(jsonValue \[, path \]) | Returns a string indicating the keys of a JSON _jsonValue_ |
| m | JSON\_REMOVE(jsonValue, path \[, path \]) | Removes data from _jsonValue_ using a series of _path_ expressions and returns the result |
| m | JSON\_REPLACE(jsonValue, path, val \[, path, val \]\*) | Returns a JSON document replace a data of _jsonValue_, _path_, _val_ |
| m | JSON\_SET(jsonValue, path, val \[, path, val \]\*) | Returns a JSON document set a data of _jsonValue_, _path_, _val_ |
| m | JSON\_STORAGE\_SIZE(jsonValue) | Returns the number of bytes used to store the binary representation of _jsonValue_ |
| b o p r s h | LEAST(expr \[, expr \]\* ) | Returns the least of the expressions |
| b m p r s | LEFT(string, length) | Returns the leftmost _length_ characters from the _string_ |
| f r s | LEN(string) | Equivalent to `CHAR_LENGTH(string)` |
| b f h p r s | LENGTH(string) | Equivalent to `CHAR_LENGTH(string)` |
| h s | LEVENSHTEIN(string1, string2) | Returns the Levenshtein distance between _string1_ and _string2_ |
| b | LOG(numeric1 \[, base \]) | Returns the logarithm of _numeric1_ to base _base_, or base e if _base_ is not present, or error if _numeric1_ is 0 or negative |
| m s h | LOG(\[, base \], numeric1) | Returns the logarithm of _numeric1_ to base _base_, or base e if _base_ is not present, or null if _numeric1_ is 0 or negative |
| p | LOG(\[, base \], numeric1 ) | Returns the logarithm of _numeric1_ to base _base_, or base 10 if _numeric1_ is not present, or error if _numeric1_ is 0 or negative |
| m s | LOG2(numeric) | Returns the base 2 logarithm of _numeric_ |
| s | LOG1P(numeric) | Returns the natural logarithm of 1 plus _numeric_ |
| b o p r s h | LPAD(string, length \[, pattern \]) | Returns a string or bytes value that consists of _string_ prepended to _length_ with _pattern_ |
| b | TO\_BASE32(string) | Converts the _string_ to base-32 encoded form and returns an encoded string |
| b | FROM\_BASE32(string) | Returns the decoded result of a base-32 _string_ as a string |
| m | TO\_BASE64(string) | Converts the _string_ to base-64 encoded form and returns a encoded string |
| b m | FROM\_BASE64(string) | Returns the decoded result of a base-64 _string_ as a string. If the input argument is an invalid base-64 _string_ the function returns `NULL` |
| h | BASE64(string) | Converts the _string_ to base-64 encoded form and returns a encoded string |
| h | UNBASE64(string) | Returns the decoded result of a base-64 _string_ as a string. If the input argument is an invalid base-64 _string_ the function returns `NULL` |
| h s | HEX(string) | Converts _string_ into a hexadecimal varchar |
| b | TO\_HEX(binary) | Converts _binary_ into a hexadecimal varchar |
| b | FROM\_HEX(varchar) | Converts a hexadecimal-encoded _varchar_ into bytes |
| s h | BIN(BIGINT) | Converts a _bigint_ into bytes string |
| b o p r s h | LTRIM(string) | Returns _string_ with all blanks removed from the start |
| s | MAP() | Returns an empty map |
| s | MAP(key, value \[, key, value\]\*) | Returns a map with the given _key_/ _value_ pairs |
| s | MAP\_CONCAT(map \[, map\]\*) | Concatenates one or more maps. If any input argument is `NULL` the function returns `NULL`. Note that calcite is using the LAST\_WIN strategy |
| s | MAP\_CONTAINS\_KEY(map, key) | Returns whether _map_ contains _key_ |
| s | MAP\_ENTRIES(map) | Returns the entries of the _map_ as an array, the order of the entries is not defined |
| s | MAP\_KEYS(map) | Returns the keys of the _map_ as an array, the order of the entries is not defined |
| s | MAP\_VALUES(map) | Returns the values of the _map_ as an array, the order of the entries is not defined |
| s | MAP\_FROM\_ARRAYS(array1, array2) | Returns a map created from an _array1_ and _array2_. Note that the lengths of two arrays should be the same and calcite is using the LAST\_WIN strategy |
| s | MAP\_FROM\_ENTRIES(arrayOfRows) | Returns a map created from an arrays of row with two fields. Note that the number of fields in a row must be 2. Note that calcite is using the LAST\_WIN strategy |
| s | STR\_TO\_MAP(string \[, stringDelimiter \[, keyValueDelimiter\]\]) | Returns a map after splitting the _string_ into key/value pairs using delimiters. Default delimiters are ‘,’ for _stringDelimiter_ and ‘:’ for _keyValueDelimiter_. Note that calcite is using the LAST\_WIN strategy |
| s | SUBSTRING\_INDEX(string, delim, count) | Returns the substring from _string_ before _count_ occurrences of the delimiter _delim_. If _count_ is positive, everything to the left of the final delimiter (counting from the left) is returned. If _count_ is negative, everything to the right of the final delimiter (counting from the right) is returned. The function substring\_index performs a case-sensitive match when searching for _delim_. |
| p r | STRING\_TO\_ARRAY(string, delimiter \[, nullString \]) | Returns a one-dimensional string\[\] array by splitting the input string value into subvalues using the specified string value as the “delimiter”. Optionally, allows a specified string value to be interpreted as NULL. |
| b m p r s h | MD5(string) | Calculates an MD5 128-bit checksum of _string_ and returns it as a hex string |
| m | MONTHNAME(date) | Returns the name, in the connection’s locale, of the month in _datetime_; for example, for a locale of en, it will return ‘February’ for both DATE ‘2020-02-10’ and TIMESTAMP ‘2020-02-10 10:10:10’, and for a locale of zh, it will return ‘二月’ |
| o r s | NVL(value1, value2) | Returns _value1_ if _value1_ is not null, otherwise _value2_ |
| o r s | NVL2(value1, value2, value3) | Returns _value2_ if _value1_ is not null, otherwise _value3_ |
| b | OFFSET(index) | When indexing an array, wrapping _index_ in `OFFSET` returns the value at the 0-based _index_; throws error if _index_ is out of bounds |
| b | ORDINAL(index) | Similar to `OFFSET` except _index_ begins at 1 |
| b | PARSE\_DATE(format, string) | Uses format specified by _format_ to convert _string_ representation of date to a DATE value |
| b | PARSE\_DATETIME(format, string) | Uses format specified by _format_ to convert _string_ representation of datetime to a TIMESTAMP value |
| b | PARSE\_TIME(format, string) | Uses format specified by _format_ to convert _string_ representation of time to a TIME value |
| b | PARSE\_TIMESTAMP(format, string\[, timeZone\]) | Uses format specified by _format_ to convert _string_ representation of timestamp to a TIMESTAMP WITH LOCAL TIME ZONE value in _timeZone_ |
| h s | PARSE\_URL(urlString, partToExtract \[, keyToExtract\] ) | Returns the specified _partToExtract_ from the _urlString_. Valid values for _partToExtract_ include HOST, PATH, QUERY, REF, PROTOCOL, AUTHORITY, FILE, and USERINFO. _keyToExtract_ specifies which query to extract. If the first argument is an invalid url _string_ the function returns `NULL` |
| b s | POW(numeric1, numeric2) | Returns _numeric1_ raised to the power _numeric2_ |
| b c h q m o f s p r | POWER(numeric1, numeric2) | Returns _numeric1_ raised to the power of _numeric2_ |
| p r | RANDOM() | Generates a random double between 0 and 1 inclusive |
| s | REGEXP(string, regexp) | Equivalent to `string1 RLIKE string2` |
| b | REGEXP\_CONTAINS(string, regexp) | Returns whether _string_ is a partial match for the _regexp_ |
| b | REGEXP\_EXTRACT(string, regexp \[, position \[, occurrence\]\]) | Returns the substring in _string_ that matches the _regexp_, starting search at _position_ (default 1), and until locating the nth _occurrence_ (default 1). Returns NULL if there is no match |
| b | REGEXP\_EXTRACT\_ALL(string, regexp) | Returns an array of all substrings in _string_ that matches the _regexp_. Returns an empty array if there is no match |
| b | REGEXP\_INSTR(string, regexp \[, position \[, occurrence \[, occurrence\_position\]\]\]) | Returns the lowest 1-based position of the substring in _string_ that matches the _regexp_, starting search at _position_ (default 1), and until locating the nth _occurrence_ (default 1). Setting occurrence\_position (default 0) to 1 returns the end position of substring + 1. Returns 0 if there is no match |
| m o p r s | REGEXP\_LIKE(string, regexp \[, flags\]) | Equivalent to `string1 RLIKE string2` with an optional parameter for search flags. Supported flags are: <ul><li>i: case-insensitive matching</li><li>c: case-sensitive matching</li><li>n: newline-sensitive matching</li><li>s: non-newline-sensitive matching</li><li>m: multi-line</li></ul> |
| r | REGEXP\_REPLACE(string, regexp) | Replaces all substrings of _string_ that match _regexp_ with the empty string |
| b m o r h | REGEXP\_REPLACE(string, regexp, rep \[, pos \[, occurrence \[, matchType\]\]\]) | Replaces all substrings of _string_ that match _regexp_ with _rep_ at the starting _pos_ in expr (if omitted, the default is 1), _occurrence_ specifies which occurrence of a match to search for (if omitted, the default is 1), _matchType_ specifies how to perform matching |
| p | REGEXP\_REPLACE(string, regexp, rep \[, matchType\]) | Replaces substrings of _string_ that match _regexp_ with _rep_ at the starting _pos_ in expr, _matchType_ specifies how to perform matching and whether to only replace first match or all |
| b | REGEXP\_SUBSTR(string, regexp \[, position \[, occurrence\]\]) | Synonym for REGEXP\_EXTRACT |
| b m p r s h | REPEAT(string, integer) | Returns a string consisting of _string_ repeated of _integer_ times; returns an empty string if _integer_ is less than 1 |
| b m | REVERSE(string) | Returns _string_ with the order of the characters reversed |
| s | REVERSE(string \| array) | Returns _string_ with the characters in reverse order or array with elements in reverse order |
| b m p r s | RIGHT(string, length) | Returns the rightmost _length_ characters from the _string_ |
| h m s | string1 RLIKE string2 | Whether _string1_ matches regex pattern _string2_ (similar to `LIKE`, but uses Java regex) |
| h m s | string1 NOT RLIKE string2 | Whether _string1_ does not match regex pattern _string2_ (similar to `NOT LIKE`, but uses Java regex) |
| b o p r s h | RPAD(string, length\[, pattern \]) | Returns a string or bytes value that consists of _string_ appended to _length_ with _pattern_ |
| b o p r s h | RTRIM(string) | Returns _string_ with all blanks removed from the end |
| b | SAFE\_ADD(numeric1, numeric2) | Returns _numeric1_ \+ _numeric2_, or NULL on overflow. Arguments are implicitly cast to one of the types BIGINT, DOUBLE, or DECIMAL |
| b | SAFE\_CAST(value AS type) | Converts _value_ to _type_, returning NULL if conversion fails |
| b | SAFE\_DIVIDE(numeric1, numeric2) | Returns _numeric1_ / _numeric2_, or NULL on overflow or if _numeric2_ is zero. Arguments implicitly are cast to one of the types BIGINT, DOUBLE, or DECIMAL |
| b | SAFE\_MULTIPLY(numeric1, numeric2) | Returns _numeric1_ \\* _numeric2_, or NULL on overflow. Arguments are implicitly cast to one of the types BIGINT, DOUBLE, or DECIMAL |
| b | SAFE\_NEGATE(numeric) | Returns _numeric_ \\* -1, or NULL on overflow. Arguments are implicitly cast to one of the types BIGINT, DOUBLE, or DECIMAL |
| b | SAFE\_OFFSET(index) | Similar to `OFFSET` except null is returned if _index_ is out of bounds |
| b | SAFE\_ORDINAL(index) | Similar to `OFFSET` except _index_ begins at 1 and null is returned if _index_ is out of bounds |
| b | SAFE\_SUBTRACT(numeric1, numeric2) | Returns _numeric1_ \- _numeric2_, or NULL on overflow. Arguments are implicitly cast to one of the types BIGINT, DOUBLE, or DECIMAL |
| \* | SEC(numeric) | Returns the secant of _numeric_ in radians |
| \* | SECH(numeric) | Returns the hyperbolic secant of _numeric_ |
| b m p r s h | SHA1(string) | Calculates a SHA-1 hash value of _string_ and returns it as a hex string |
| b p | SHA256(string) | Calculates a SHA-256 hash value of _string_ and returns it as a hex string |
| b p | SHA512(string) | Calculates a SHA-512 hash value of _string_ and returns it as a hex string |
| p | SIND(numeric) | Returns the sine of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. Fails if _numeric_ is greater than the maximum double value. |
| \* | SINH(numeric) | Returns the hyperbolic sine of _numeric_ |
| b m o p r h | SOUNDEX(string) | Returns the phonetic representation of _string_; throws if _string_ is encoded with multi-byte encoding such as UTF-8 |
| s | SOUNDEX(string) | Returns the phonetic representation of _string_; return original _string_ if _string_ is encoded with multi-byte encoding such as UTF-8 |
| m s h | SPACE(integer) | Returns a string of _integer_ spaces; returns an empty string if _integer_ is less than 1 |
| b | SPLIT(string \[, delimiter \]) | Returns the string array of _string_ split at _delimiter_ (if omitted, default is comma). If the _string_ is empty it returns an empty array, otherwise, if the _delimiter_ is empty, it returns an array containing the original _string_. |
| p | SPLIT\_PART(string, delimiter, n) | Returns the _n_ th field in _string_ using _delimiter_; returns empty string if _n_ is less than 1 or greater than the number of fields, and the n can be negative to count from the end. |
| f s | STARTSWITH(string1, string2) | Returns whether _string2_ is a prefix of _string1_ |
| b p | STARTS\_WITH(string1, string2) | Equivalent to `STARTSWITH(string1, string2)` |
| m | STRCMP(string, string) | Returns 0 if both of the strings are same and returns -1 when the first argument is smaller than the second and 1 when the second one is smaller than the first one |
| b r p | STRPOS(string, substring) | Equivalent to `POSITION(substring IN string)` |
| b m o p r | SUBSTR(string, position \[, substringLength \]) | Returns a portion of _string_, beginning at character _position_, _substringLength_ characters long. SUBSTR calculates lengths using characters as defined by the input character set |
| o | SYSDATE | Returns the current date in the operating system time zone of the database server, in a value of datatype DATE. |
| o | SYSTIMESTAMP | Returns the current date and time in the operating system time zone of the database server, in a value of datatype TIMESTAMP WITH TIME ZONE. |
| p | TAND(numeric) | Returns the tangent of _numeric_ in degrees as a double. Returns NaN if _numeric_ is NaN. Fails if \*numeric is greater than the maximum double value. |
| \* | TANH(numeric) | Returns the hyperbolic tangent of _numeric_ |
| b | TIME(hour, minute, second) | Returns a TIME value _hour_, _minute_, _second_ (all of type INTEGER) |
| b | TIME(timestamp) | Extracts the TIME from _timestamp_ (a local time; BigQuery’s DATETIME type) |
| b | TIME(instant) | Extracts the TIME from _timestampLtz_ (an instant; BigQuery’s TIMESTAMP type), assuming UTC |
| b | TIME(instant, timeZone) | Extracts the time from _timestampLtz_ (an instant; BigQuery’s TIMESTAMP type), in _timeZone_ |
| b | TIMESTAMP(string) | Equivalent to `CAST(string AS TIMESTAMP WITH LOCAL TIME ZONE)` |
| b | TIMESTAMP(string, timeZone) | Equivalent to `CAST(string AS TIMESTAMP WITH LOCAL TIME ZONE)`, converted to _timeZone_ |
| b | TIMESTAMP(date) | Converts _date_ to a TIMESTAMP WITH LOCAL TIME ZONE value (at midnight) |
| b | TIMESTAMP(date, timeZone) | Converts _date_ to a TIMESTAMP WITH LOCAL TIME ZONE value (at midnight), in _timeZone_ |
| b | TIMESTAMP(timestamp) | Converts _timestamp_ to a TIMESTAMP WITH LOCAL TIME ZONE, assuming a UTC |
| b | TIMESTAMP(timestamp, timeZone) | Converts _timestamp_ to a TIMESTAMP WITH LOCAL TIME ZONE, in _timeZone_ |
| b | TIMESTAMP\_ADD(timestamp, interval) | Returns the TIMESTAMP value that occurs _interval_ after _timestamp_ |
| b | TIMESTAMP\_DIFF(timestamp, timestamp2, timeUnit) | Returns the whole number of _timeUnit_ between _timestamp_ and _timestamp2_. Equivalent to `TIMESTAMPDIFF(timeUnit, timestamp2, timestamp)` and `(timestamp - timestamp2) timeUnit` |
| b s | TIMESTAMP\_MICROS(integer) | Returns the TIMESTAMP that is _integer_ microseconds after 1970-01-01 00:00:00 |
| b s | TIMESTAMP\_MILLIS(integer) | Returns the TIMESTAMP that is _integer_ milliseconds after 1970-01-01 00:00:00 |
| b s | TIMESTAMP\_SECONDS(integer) | Returns the TIMESTAMP that is _integer_ seconds after 1970-01-01 00:00:00 |
| b | TIMESTAMP\_SUB(timestamp, interval) | Returns the TIMESTAMP value that is _interval_ before _timestamp_ |
| b | TIMESTAMP\_TRUNC(timestamp, timeUnit) | Truncates _timestamp_ to the granularity of _timeUnit_, rounding to the beginning of the unit |
| b | TIME\_ADD(time, interval) | Adds _interval_ to _time_, independent of any time zone |
| b | TIME\_DIFF(time, time2, timeUnit) | Returns the whole number of _timeUnit_ between _time_ and _time2_ |
| b | TIME\_SUB(time, interval) | Returns the TIME value that is _interval_ before _time_ |
| b | TIME\_TRUNC(time, timeUnit) | Truncates _time_ to the granularity of _timeUnit_, rounding to the beginning of the unit |
| m o p r | TO\_CHAR(timestamp, format) | Converts _timestamp_ to a string using the format _format_ |
| b | TO\_CODE\_POINTS(string) | Converts _string_ to an array of integers that represent code points or extended ASCII character values |
| o p r h | TO\_DATE(string, format) | Converts _string_ to a date using the format _format_ |
| o p r | TO\_TIMESTAMP(string, format) | Converts _string_ to a timestamp using the format _format_ |
| b o p r s | TRANSLATE(expr, fromString, toString) | Returns _expr_ with all occurrences of each character in _fromString_ replaced by its corresponding character in _toString_. Characters in _expr_ that are not in _fromString_ are not replaced |
| b | TRUNC(numeric1 \[, integer2 \]) | Truncates _numeric1_ to optionally _integer2_ (if not specified 0) places right to the decimal point |
| q | TRY\_CAST(value AS type) | Converts _value_ to _type_, returning NULL if conversion fails |
| b s | UNIX\_MICROS(timestamp) | Returns the number of microseconds since 1970-01-01 00:00:00 |
| b s | UNIX\_MILLIS(timestamp) | Returns the number of milliseconds since 1970-01-01 00:00:00 |
| b s | UNIX\_SECONDS(timestamp) | Returns the number of seconds since 1970-01-01 00:00:00 |
| b s | UNIX\_DATE(date) | Returns the number of days since 1970-01-01 |
| s | URL\_DECODE(string) | Decodes a _string_ in ‘application/x-www-form-urlencoded’ format using a specific encoding scheme, returns original _string_ when decoded error |
| s | URL\_ENCODE(string) | Translates a _string_ into ‘application/x-www-form-urlencoded’ format using a specific encoding scheme |
| o | XMLTRANSFORM(xml, xslt) | Applies XSLT transform _xslt_ to XML string _xml_ and returns the result |

Note:

- Functions `DATEADD`, `DATEDIFF`, `DATE_PART` require the Babel parser
- `JSON_TYPE` / `JSON_DEPTH` / `JSON_PRETTY` / `JSON_STORAGE_SIZE` return null if the argument is null
- `JSON_LENGTH` / `JSON_KEYS` / `JSON_REMOVE` return null if the first argument is null
- `JSON_TYPE`generally returns an upper-case string flag indicating the type of the JSON input. Currently supported supported type flags are:
  - INTEGER
  - STRING
  - FLOAT
  - DOUBLE
  - LONG
  - BOOLEAN
  - DATE
  - OBJECT
  - ARRAY
  - NULL
- `JSON_DEPTH`defines a JSON value’s depth as follows:
  - An empty array, empty object, or scalar value has depth 1;
  - A non-empty array containing only elements of depth 1 or non-empty object containing only member values of depth 1 has depth 2;
  - Otherwise, a JSON document has depth greater than 2.
- `JSON_LENGTH`defines a JSON value’s length as follows:
  - A scalar value has length 1;
  - The length of array or object is the number of elements is contains.

Dialect-specific aggregate functions.

| C | Operator syntax | Description |
| --- | --- | --- |
| c | AGGREGATE(m) | Computes measure _m_ in the context of the current GROUP BY key |
| b p | ARRAY\_AGG( \[ ALL \| DISTINCT \] value \[ RESPECT NULLS \| IGNORE NULLS \] \[ ORDER BY orderItem \[, orderItem \]\* \] ) | Gathers values into arrays |
| b p | ARRAY\_CONCAT\_AGG( \[ ALL \| DISTINCT \] value \[ ORDER BY orderItem \[, orderItem \]\* \] ) | Concatenates arrays into arrays |
| p r s | BOOL\_AND(condition) | Synonym for `EVERY` |
| p r s | BOOL\_OR(condition) | Synonym for `SOME` |
| f | BOOLAND\_AGG(condition) | Synonym for `EVERY` |
| f | BOOLOR\_AGG(condition) | Synonym for `SOME` |
| b | COUNTIF(condition) | Returns the number of rows for which _condition_ is TRUE; equivalent to `COUNT(*) FILTER (WHERE condition)` |
| m | GROUP\_CONCAT( \[ ALL \| DISTINCT \] value \[, value \]\* \[ ORDER BY orderItem \[, orderItem \]\* \] \[ SEPARATOR separator \] ) | MySQL-specific variant of `LISTAGG` |
| b | LOGICAL\_AND(condition) | Synonym for `EVERY` |
| b | LOGICAL\_OR(condition) | Synonym for `SOME` |
| s | MAX\_BY(value, comp) | Synonym for `ARG_MAX` |
| s | MIN\_BY(value, comp) | Synonym for `ARG_MIN` |
| b | PERCENTILE\_CONT(value, fraction \[ RESPECT NULLS \| IGNORE NULLS \] ) OVER windowSpec | Synonym for standard `PERCENTILE_CONT` where `PERCENTILE_CONT(value, fraction) OVER (ORDER BY value)` is equivalent to standard `PERCENTILE_CONT(fraction) WITHIN GROUP (ORDER BY value)` |
| b | PERCENTILE\_DISC(value, fraction \[ RESPECT NULLS \| IGNORE NULLS \] ) OVER windowSpec | Synonym for standard `PERCENTILE_DISC` where `PERCENTILE_DISC(value, fraction) OVER (ORDER BY value)` is equivalent to standard `PERCENTILE_DISC(fraction) WITHIN GROUP (ORDER BY value)` |
| b p | STRING\_AGG( \[ ALL \| DISTINCT \] value \[, separator\] \[ ORDER BY orderItem \[, orderItem \]\* \] ) | Synonym for `LISTAGG` |

Usage Examples:

##### JSON\_TYPE example [Permalink](https://calcite.apache.org/docs/reference.html\#json_type-example "Permalink")

SQL

```sql
SELECT JSON_TYPE(v) AS c1,
  JSON_TYPE(JSON_VALUE(v, 'lax $.b' ERROR ON ERROR)) AS c2,
  JSON_TYPE(JSON_VALUE(v, 'strict $.a[0]' ERROR ON ERROR)) AS c3,
  JSON_TYPE(JSON_VALUE(v, 'strict $.a[1]' ERROR ON ERROR)) AS c4
FROM (VALUES ('{"a": [10, true],"b": "[10, true]"}')) AS t(v)
LIMIT 10;
```

Result

| c1 | c2 | c3 | c4 |
| --- | --- | --- | --- |
| OBJECT | ARRAY | INTEGER | BOOLEAN |

##### JSON\_DEPTH example [Permalink](https://calcite.apache.org/docs/reference.html\#json_depth-example "Permalink")

SQL

```sql
SELECT JSON_DEPTH(v) AS c1,
  JSON_DEPTH(JSON_VALUE(v, 'lax $.b' ERROR ON ERROR)) AS c2,
  JSON_DEPTH(JSON_VALUE(v, 'strict $.a[0]' ERROR ON ERROR)) AS c3,
  JSON_DEPTH(JSON_VALUE(v, 'strict $.a[1]' ERROR ON ERROR)) AS c4
FROM (VALUES ('{"a": [10, true],"b": "[10, true]"}')) AS t(v)
LIMIT 10;
```

Result

| c1 | c2 | c3 | c4 |
| --- | --- | --- | --- |
| 3 | 2 | 1 | 1 |

##### JSON\_LENGTH example [Permalink](https://calcite.apache.org/docs/reference.html\#json_length-example "Permalink")

SQL

```sql
SELECT JSON_LENGTH(v) AS c1,
  JSON_LENGTH(v, 'lax $.a') AS c2,
  JSON_LENGTH(v, 'strict $.a[0]') AS c3,
  JSON_LENGTH(v, 'strict $.a[1]') AS c4
FROM (VALUES ('{"a": [10, true]}')) AS t(v)
LIMIT 10;
```

Result

| c1 | c2 | c3 | c4 |
| --- | --- | --- | --- |
| 1 | 2 | 1 | 1 |

##### JSON\_INSERT example [Permalink](https://calcite.apache.org/docs/reference.html\#json_insert-example "Permalink")

SQL

```sql
SELECT JSON_INSERT(v, '$.a', 10, '$.c', '[1]') AS c1,
  JSON_INSERT(v, '$', 10, '$.c', '[1]') AS c2
FROM (VALUES ('{"a": [10, true]}')) AS t(v)
LIMIT 10;
```

Result

| c1 | c2 |
| --- | --- |
| {“a”:1 , “b”:\[2\] , “c”:”\[1\]”} | {“a”:1 , “b”:\[2\] , “c”:”\[1\]”} |

##### JSON\_KEYS example [Permalink](https://calcite.apache.org/docs/reference.html\#json_keys-example "Permalink")

SQL

```sql
SELECT JSON_KEYS(v) AS c1,
  JSON_KEYS(v, 'lax $.a') AS c2,
  JSON_KEYS(v, 'lax $.b') AS c2,
  JSON_KEYS(v, 'strict $.a[0]') AS c3,
  JSON_KEYS(v, 'strict $.a[1]') AS c4
FROM (VALUES ('{"a": [10, true],"b": {"c": 30}}')) AS t(v)
LIMIT 10;
```

Result

| c1 | c2 | c3 | c4 | c5 |
| --- | --- | --- | --- | --- |
| \[“a”, “b”\] | NULL | \[“c”\] | NULL | NULL |

##### JSON\_REMOVE example [Permalink](https://calcite.apache.org/docs/reference.html\#json_remove-example "Permalink")

SQL

```sql
SELECT JSON_REMOVE(v, '$[1]') AS c1
FROM (VALUES ('["a", ["b", "c"], "d"]')) AS t(v)
LIMIT 10;
```

Result

| c1 |
| --- |
| \[“a”, “d”\] |

##### JSON\_REPLACE example [Permalink](https://calcite.apache.org/docs/reference.html\#json_replace-example "Permalink")

SQL

```sql
SELECT
JSON_REPLACE(v, '$.a', 10, '$.c', '[1]') AS c1,
JSON_REPLACE(v, '$', 10, '$.c', '[1]') AS c2
FROM (VALUES ('{\"a\": 1,\"b\":[2]}')) AS t(v)
limit 10;
```

Result

| c1 | c2 |
| --- | --- |
| {“a”:1 , “b”:\[2\] , “c”:”\[1\]”} | {“a”:1 , “b”:\[2\] , “c”:”\[1\]”}”) |

##### JSON\_SET example [Permalink](https://calcite.apache.org/docs/reference.html\#json_set-example "Permalink")

SQL

```sql
SELECT
JSON_SET(v, '$.a', 10, '$.c', '[1]') AS c1,
JSON_SET(v, '$', 10, '$.c', '[1]') AS c2
FROM (VALUES ('{\"a\": 1,\"b\":[2]}')) AS t(v)
limit 10;
```

Result

| c1 | c2 |
| --- | --- |
| {“a”:10, “b”:\[2\]} | 10 |

##### JSON\_STORAGE\_SIZE example [Permalink](https://calcite.apache.org/docs/reference.html\#json_storage_size-example "Permalink")

SQL

```sql
SELECT
JSON_STORAGE_SIZE('[100, \"sakila\", [1, 3, 5], 425.05]') AS c1,
JSON_STORAGE_SIZE('{\"a\": 10, \"b\": \"a\", \"c\": \"[1, 3, 5, 7]\"}') AS c2,
JSON_STORAGE_SIZE('{\"a\": 10, \"b\": \"xyz\", \"c\": \"[1, 3, 5, 7]\"}') AS c3,
JSON_STORAGE_SIZE('[100, \"json\", [[10, 20, 30], 3, 5], 425.05]') AS c4
limit 10;
```

Result

| c1 | c2 | c3 | c4 |
| --- | --- | --- | --- |
| 29 | 35 | 37 | 36 |

#### DECODE example [Permalink](https://calcite.apache.org/docs/reference.html\#decode-example "Permalink")

SQL

```sql
SELECT DECODE(f1, 1, 'aa', 2, 'bb', 3, 'cc', 4, 'dd', 'ee') as c1,
  DECODE(f2, 1, 'aa', 2, 'bb', 3, 'cc', 4, 'dd', 'ee') as c2,
  DECODE(f3, 1, 'aa', 2, 'bb', 3, 'cc', 4, 'dd', 'ee') as c3,
  DECODE(f4, 1, 'aa', 2, 'bb', 3, 'cc', 4, 'dd', 'ee') as c4,
  DECODE(f5, 1, 'aa', 2, 'bb', 3, 'cc', 4, 'dd', 'ee') as c5
FROM (VALUES (1, 2, 3, 4, 5)) AS t(f1, f2, f3, f4, f5);
```

Result

| c1 | c2 | c3 | c4 | c5 |
| --- | --- | --- | --- | --- |
| aa | bb | cc | dd | ee |

#### TRANSLATE example [Permalink](https://calcite.apache.org/docs/reference.html\#translate-example "Permalink")

SQL

```sql
SELECT TRANSLATE('Aa*Bb*Cc''D*d', ' */''%', '_') as c1,
  TRANSLATE('Aa/Bb/Cc''D/d', ' */''%', '_') as c2,
  TRANSLATE('Aa Bb Cc''D d', ' */''%', '_') as c3,
  TRANSLATE('Aa%Bb%Cc''D%d', ' */''%', '_') as c4
FROM (VALUES (true)) AS t(f0);
```

Result

| c1 | c2 | c3 | c4 |
| --- | --- | --- | --- |
| Aa\_Bb\_CcD\_d | Aa\_Bb\_CcD\_d | Aa\_Bb\_CcD\_d | Aa\_Bb\_CcD\_d |

### Higher-order Functions [Permalink](https://calcite.apache.org/docs/reference.html\#higher-order-functions "Permalink")

A higher-order function takes one or more lambda expressions as arguments.

Lambda Expression Syntax:

```sql
lambdaExpression:
      parameters '->' expression

parameters:
      '(' [ identifier [, identifier ] ] ')'
  |   identifier
```

Higher-order functions are not included in the SQL standard, so all the functions will be listed in the
[Dialect-specific OperatorsPermalink](https://calcite.apache.org/docs/reference.html#dialect-specific-operators)
as well.

Examples of functions with a lambda argument are _EXISTS_.

## User-defined functions [Permalink](https://calcite.apache.org/docs/reference.html\#user-defined-functions "Permalink")

Calcite is extensible. You can define each kind of function using user code.
For each kind of function there are often several ways to define a function,
varying from convenient to efficient.

To implement a _scalar function_, there are 3 options:

- Create a class with a public static `eval` method,
and register the class;
- Create a class with a public non-static `eval` method,
and a public constructor with no arguments,
and register the class;
- Create a class with one or more public static methods,
and register each class/method combination.

To implement an _aggregate function_, there are 2 options:

- Create a class with public static `init`, `add` and `result` methods,
and register the class;
- Create a class with public non-static `init`, `add` and `result` methods,
and a public constructor with no arguments,
and register the class.

Optionally, add a public `merge` method to the class; this allows Calcite to
generate code that merges sub-totals.

Optionally, make your class implement the
[SqlSplittableAggFunction](https://calcite.apache.org/javadocAggregate/org/apache/calcite/sql/SqlSplittableAggFunction.html)
interface; this allows Calcite to decompose the function across several stages
of aggregation, roll up from summary tables, and push it through joins.

To implement a _table function_, there are 3 options:

- Create a class with a static `eval` method that returns
[ScannableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/ScannableTable.html)
or
[QueryableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/QueryableTable.html),
and register the class;
- Create a class with a non-static `eval` method that returns
[ScannableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/ScannableTable.html)
or
[QueryableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/QueryableTable.html),
and register the class;
- Create a class with one or more public static methods that return
[ScannableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/ScannableTable.html)
or
[QueryableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/QueryableTable.html),
and register each class/method combination.

To implement a _table macro_, there are 3 options:

- Create a class with a static `eval` method that returns
[TranslatableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TranslatableTable.html),
and register the class;
- Create a class with a non-static `eval` method that returns
[TranslatableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TranslatableTable.html),
and register the class;
- Create a class with one or more public static methods that return
[TranslatableTable](https://calcite.apache.org/javadocAggregate/org/apache/calcite/schema/TranslatableTable.html),
and register each class/method combination.

Calcite deduces the parameter types and result type of a function from the
parameter and return types of the Java method that implements it. Further, you
can specify the name and optionality of each parameter using the
[Parameter](https://calcite.apache.org/javadocAggregate/org/apache/calcite/linq4j/function/Parameter.html)
annotation.

### Calling functions with named and optional parameters [Permalink](https://calcite.apache.org/docs/reference.html\#calling-functions-with-named-and-optional-parameters "Permalink")

Usually when you call a function, you need to specify all of its parameters,
in order. But that can be a problem if a function has a lot of parameters,
and especially if you want to add more parameters over time.

To solve this problem, the SQL standard allows you to pass parameters by name,
and to define parameters which are optional (that is, have a default value
that is used if they are not specified).

Suppose you have a function `f`, declared as in the following pseudo syntax:

```sql
FUNCTION f(
  INTEGER a,
  INTEGER b DEFAULT NULL,
  INTEGER c,
  INTEGER d DEFAULT NULL,
  INTEGER e DEFAULT NULL) RETURNS INTEGER
```

All of the function’s parameters have names, and parameters `b`, `d` and `e`
have a default value of `NULL` and are therefore optional.
(In Calcite, `NULL` is the only allowable default value for optional parameters;
this may change
[in future](https://issues.apache.org/jira/browse/CALCITE-947).)

When calling a function with optional parameters,
you can omit optional arguments at the end of the list, or use the `DEFAULT`
keyword for any optional arguments.
Here are some examples:

- `f(1, 2, 3, 4, 5)` provides a value to each parameter, in order;
- `f(1, 2, 3, 4)` omits `e`, which gets its default value, `NULL`;
- `f(1, DEFAULT, 3)` omits `d` and `e`,
and specifies to use the default value of `b`;
- `f(1, DEFAULT, 3, DEFAULT, DEFAULT)` has the same effect as the previous
example;
- `f(1, 2)` is not legal, because `c` is not optional;
- `f(1, 2, DEFAULT, 4)` is not legal, because `c` is not optional.

You can specify arguments by name using the `=>` syntax.
If one argument is named, they all must be.
Arguments may be in any other, but must not specify any argument more than once,
and you need to provide a value for every parameter which is not optional.
Here are some examples:

- `f(c => 3, d => 1, a => 0)` is equivalent to `f(0, NULL, 3, 1, NULL)`;
- `f(c => 3, d => 1)` is not legal, because you have not specified a value for
`a` and `a` is not optional.

### SQL Hints [Permalink](https://calcite.apache.org/docs/reference.html\#sql-hints "Permalink")

A hint is an instruction to the optimizer. When writing SQL, you may know information about
the data unknown to the optimizer. Hints enable you to make decisions normally made by the optimizer.

- Planner enforcers: there’s no perfect planner, so it makes sense to implement hints to
allow user better control the execution. For instance: “never merge this subquery with others” (`/*+ no_merge */`);
“treat those tables as leading ones” (`/*+ leading */`) to affect join ordering, etc;
- Append meta data/statistics: some statistics like “table index for scan” or “skew info of some shuffle keys”
are somehow dynamic for the query, it would be very convenient to config them with hints because
our planning metadata from the planner is very often not very accurate;
- Operator resource constraints: for many cases, we would give a default resource configuration
for the execution operators,
i.e. min parallelism, memory (resource consuming UDF), special resource requirement (GPU or SSD disk) …
It would be very flexible to profile the resource with hints per query (not the Job).

#### Syntax [Permalink](https://calcite.apache.org/docs/reference.html\#syntax "Permalink")

Calcite supports hints in two locations:

- Query Hint: right after the `SELECT` keyword;
- Table Hint: right after the referenced table name.

For example:

```sql
SELECT /*+ hint1, hint2(a=1, b=2) */
...
FROM
  tableName /*+ hint3(5, 'x') */
JOIN
  tableName /*+ hint4(c=id), hint5 */
...
```

The syntax is as follows:

```sql
hintComment:
      '/*+' hint [, hint ]* '*/'

hint:
      hintName
  |   hintName '(' optionKey '=' optionVal [, optionKey '=' optionVal ]* ')'
  |   hintName '(' hintOption [, hintOption ]* ')'

optionKey:
      simpleIdentifier
  |   stringLiteral

optionVal:
      stringLiteral

hintOption:
      simpleIdentifier
   |  numericLiteral
   |  stringLiteral
```

It is experimental in Calcite, and yet not fully implemented, what we have implemented are:

- The parser support for the syntax above;
- `RelHint` to represent a hint item;
- Mechanism to propagate the hints, during sql-to-rel conversion and planner planning.

We do not add any builtin hint items yet, would introduce more if we think the hints is stable enough.

### MATCH\_RECOGNIZE [Permalink](https://calcite.apache.org/docs/reference.html\#match_recognize "Permalink")

`MATCH_RECOGNIZE` is a SQL extension for recognizing sequences of
events in complex event processing (CEP).

It is experimental in Calcite, and yet not fully implemented.

#### Syntax [Permalink](https://calcite.apache.org/docs/reference.html\#syntax-1 "Permalink")

```sql
matchRecognize:
      MATCH_RECOGNIZE '('
      [ PARTITION BY expression [, expression ]* ]
      [ ORDER BY orderItem [, orderItem ]* ]
      [ MEASURES measureColumn [, measureColumn ]* ]
      [ ONE ROW PER MATCH | ALL ROWS PER MATCH ]
      [ AFTER MATCH skip ]
      PATTERN '(' pattern ')'
      [ WITHIN intervalLiteral ]
      [ SUBSET subsetItem [, subsetItem ]* ]
      DEFINE variable AS condition [, variable AS condition ]*
      ')'

skip:
      SKIP TO NEXT ROW
  |   SKIP PAST LAST ROW
  |   SKIP TO FIRST variable
  |   SKIP TO LAST variable
  |   SKIP TO variable

subsetItem:
      variable = '(' variable [, variable ]* ')'

measureColumn:
      expression AS alias

pattern:
      patternTerm [ '|' patternTerm ]*

patternTerm:
      patternFactor [ patternFactor ]*

patternFactor:
      patternPrimary [ patternQuantifier ]

patternPrimary:
      variable
  |   '$'
  |   '^'
  |   '(' [ pattern ] ')'
  |   '{-' pattern '-}'
  |   PERMUTE '(' pattern [, pattern ]* ')'

patternQuantifier:
      '*'
  |   '*?'
  |   '+'
  |   '+?'
  |   '?'
  |   '??'
  |   '{' { [ minRepeat ], [ maxRepeat ] } '}' ['?']
  |   '{' repeat '}'

intervalLiteral:
      INTERVAL 'string' timeUnit [ TO timeUnit ]
```

In _patternQuantifier_, _repeat_ is a positive integer,
and _minRepeat_ and _maxRepeat_ are non-negative integers.

### DDL Extensions [Permalink](https://calcite.apache.org/docs/reference.html\#ddl-extensions "Permalink")

DDL extensions are only available in the calcite-server module.
To enable, include `calcite-server.jar` in your class path, and add
`parserFactory=org.apache.calcite.server.ServerDdlExecutor#PARSER_FACTORY`
to the JDBC connect string (see connect string property
[parserFactory](https://calcite.apache.org/javadocAggregate/org/apache/calcite/config/CalciteConnectionProperty.html#PARSER_FACTORY)).

```sql
ddlStatement:
      createSchemaStatement
  |   createForeignSchemaStatement
  |   createTableStatement
  |   createTableLikeStatement
  |   createViewStatement
  |   createMaterializedViewStatement
  |   createTypeStatement
  |   createFunctionStatement
  |   dropSchemaStatement
  |   dropForeignSchemaStatement
  |   dropTableStatement
  |   dropViewStatement
  |   dropMaterializedViewStatement
  |   dropTypeStatement
  |   dropFunctionStatement

createSchemaStatement:
      CREATE [ OR REPLACE ] SCHEMA [ IF NOT EXISTS ] name

createForeignSchemaStatement:
      CREATE [ OR REPLACE ] FOREIGN SCHEMA [ IF NOT EXISTS ] name
      (
          TYPE 'type'
      |   LIBRARY 'com.example.calcite.ExampleSchemaFactory'
      )
      [ OPTIONS '(' option [, option ]* ')' ]

option:
      name literal

createTableStatement:
      CREATE TABLE [ IF NOT EXISTS ] name
      [ '(' tableElement [, tableElement ]* ')' ]
      [ AS query ]

createTableLikeStatement:
      CREATE TABLE [ IF NOT EXISTS ] name LIKE sourceTable
      [ likeOption [, likeOption ]* ]

likeOption:
      { INCLUDING | EXCLUDING } { DEFAULTS | GENERATED | ALL }

createTypeStatement:
      CREATE [ OR REPLACE ] TYPE name AS
      {
          baseType
      |   '(' attributeDef [, attributeDef ]* ')'
      }

attributeDef:
      attributeName type
      [ COLLATE collation ]
      [ NULL | NOT NULL ]
      [ DEFAULT expression ]

tableElement:
      columnName type [ columnGenerator ] [ columnConstraint ]
  |   columnName
  |   tableConstraint

columnGenerator:
      DEFAULT expression
  |   [ GENERATED ALWAYS ] AS '(' expression ')'
      { VIRTUAL | STORED }

columnConstraint:
      [ CONSTRAINT name ]
      [ NOT ] NULL

tableConstraint:
      [ CONSTRAINT name ]
      {
          CHECK '(' expression ')'
      |   PRIMARY KEY '(' columnName [, columnName ]* ')'
      |   UNIQUE '(' columnName [, columnName ]* ')'
      }

createViewStatement:
      CREATE [ OR REPLACE ] VIEW name
      [ '(' columnName [, columnName ]* ')' ]
      AS query

createMaterializedViewStatement:
      CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] name
      [ '(' columnName [, columnName ]* ')' ]
      AS query

createFunctionStatement:
      CREATE [ OR REPLACE ] FUNCTION [ IF NOT EXISTS ] name
      AS classNameLiteral
      [ USING  usingFile [, usingFile ]* ]

usingFile:
      { JAR | FILE | ARCHIVE } filePathLiteral

dropSchemaStatement:
      DROP SCHEMA [ IF EXISTS ] name

dropForeignSchemaStatement:
      DROP FOREIGN SCHEMA [ IF EXISTS ] name

dropTableStatement:
      DROP TABLE [ IF EXISTS ] name

dropViewStatement:
      DROP VIEW [ IF EXISTS ] name

dropMaterializedViewStatement:
      DROP MATERIALIZED VIEW [ IF EXISTS ] name

dropTypeStatement:
      DROP TYPE [ IF EXISTS ] name

dropFunctionStatement:
      DROP FUNCTION [ IF EXISTS ] name

truncateTableStatement:
      TRUNCATE TABLE name
      [ CONTINUE IDENTITY | RESTART IDENTITY ]
```

In _createTableStatement_, if you specify _AS query_, you may omit the list of
_tableElement_ s, or you can omit the data type of any _tableElement_, in which
case it just renames the underlying column.

In _columnGenerator_, if you do not specify `VIRTUAL` or `STORED` for a
generated column, `VIRTUAL` is the default.

In _createFunctionStatement_ and _usingFile_, _classNameLiteral_
and _filePathLiteral_ are character literals.

#### Declaring objects for user-defined types [Permalink](https://calcite.apache.org/docs/reference.html\#declaring-objects-for-user-defined-types "Permalink")

After an object type is defined and installed in the schema, you can use it to
declare objects in any SQL block. For example, you can use the object type to
specify the datatype of an attribute, column, variable, bind variable, record
field, table element, formal parameter, or function result. At run time,
instances of the object type are created; that is, objects of that type are
instantiated. Each object can hold different values.

For example, we can declare types `address_typ` and `employee_typ`:

```sql
CREATE TYPE address_typ AS (
   street          VARCHAR(30),
   city            VARCHAR(20),
   state           CHAR(2),
   postal_code     VARCHAR(6));

CREATE TYPE employee_typ AS (
  employee_id       DECIMAL(6),
  first_name        VARCHAR(20),
  last_name         VARCHAR(25),
  email             VARCHAR(25),
  phone_number      VARCHAR(20),
  hire_date         DATE,
  job_id            VARCHAR(10),
  salary            DECIMAL(8,2),
  commission_pct    DECIMAL(2,2),
  manager_id        DECIMAL(6),
  department_id     DECIMAL(4),
  address           address_typ);
```

Using these types, you can instantiate objects as follows:

```sql
employee_typ(315, 'Francis', 'Logan', 'FLOGAN',
    '555.777.2222', DATE '2004-05-01', 'SA_MAN', 11000, .15, 101, 110,
     address_typ('376 Mission', 'San Francisco', 'CA', '94222'))
```

[Previous](https://calcite.apache.org/docs/avatica_protobuf_reference.html)

[Next](https://calcite.apache.org/docs/model.html)