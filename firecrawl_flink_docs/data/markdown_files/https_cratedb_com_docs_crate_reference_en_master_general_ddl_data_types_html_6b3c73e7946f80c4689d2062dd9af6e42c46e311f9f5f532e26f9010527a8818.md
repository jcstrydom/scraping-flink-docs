ContentsMenuExpandLight modeDark mode[Skip to content](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#main-content)

Download the latest version of the CrateDB Architecture Guide

[Download Now](https://cratedb.com/resources/white-papers/lp-wp-architecture-guide)

# Data types [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#data-types "Link to this heading")

Data can be stored in different formats. CrateDB has different types that can
be specified if a table is created using the [CREATE TABLE](https://cratedb.com/docs/crate/reference/en/master/sql/statements/create-table.html#sql-create-table) statement.

Data types play a central role as they limit what kind of data can be inserted
and how it is stored. They also influence the behaviour when the records are
queried.

Data type names are reserved words and need to be escaped when used as column
names.

Table of contents

## [Overview](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id16) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#overview "Link to this heading")

### [Supported types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id17) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#supported-types "Link to this heading")

CrateDB supports the following data types. Scroll down for more details.

| Type | Description | Example |
| --- | --- | --- |
| `BOOLEAN` | A boolean value | `true` or `false` |
| `VARCHAR(n)` and `TEXT` | A string of Unicode characters | `'foobar'` |
| `CHARACTER(n)` and `CHAR(n)` | A fixed-length, blank padded string of Unicode characters | `'foobar'` |
| `SMALLINT`, `INTEGER` and `BIGINT` | A signed integer value | `12345` or `-12345` |
| `REAL` | An inexact [single-precision floating-point](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) value. | `3.4028235e+38` |
| `DOUBLE PRECISION` | An inexact [double-precision floating-point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) value. | `1.7976931348623157e+308` |
| `NUMERIC(precision, scale)` | An exact [fixed-point fractional number](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) with an arbitrary, user-specified precision. | `123.45` |
| `TIMESTAMP WITH TIME ZONE` | Time and date with time zone | `'1970-01-02T00:00:00+01:00'` |
| `TIMESTAMP WITHOUT TIME ZONE` | Time and date without time zone | `'1970-01-02T00:00:00'` |
| `DATE` | A specific year, month and a day in UTC. | `'2021-03-09'` |
| `TIME` | A specific time as the number of milliseconds since midnight<br>along with an optional time zone offset | `'13:00:00'` or `'13:00:00+01:00'` |
| `BIT(n)` | A bit sequence | `B'00010010'` |
| `IP` | An IP address (IPv4 or IPv6) | `'127.0.0.1'` or `'0:0:0:0:0:ffff:c0a8:64'` |
| `OBJECT` | Express an object | ```<br>{<br>    "foo" = 'bar',<br>    "baz" = 'qux'<br>}<br>```<br>Copy to clipboard |
| `ARRAY` | Express an array | ```<br>[<br>    {"name" = 'Alice', "age" = 33},<br>    {"name" = 'Bob', "age" = 45}<br>]<br>```<br>Copy to clipboard |
| `GEO_POINT` | A geographic data type comprised of a pair of coordinates (latitude and longitude) | `[13.46738, 52.50463]` or `POINT( 13.46738 52.50463 )` |
| `GEO_SHAPE` | Express arbitrary [GeoJSON geometry objects](https://datatracker.ietf.org/doc/html/rfc7946) | `[13.46738, 52.50463]` or `POINT( 13.46738 52.50463 )`<br>```<br>{<br>    type = 'Polygon',<br>    coordinates = [<br>        [<br>            [100.0, 0.0],<br>            [101.0, 0.0],<br>            [101.0, 1.0],<br>            [100.0, 1.0],<br>            [100.0, 0.0]<br>        ]<br>    ]<br>}<br>```<br>Copy to clipboard<br>or:<br>```<br>'POLYGON ((5 5, 10 5, 10 10, 5 10, 5 5))'<br>```<br>Copy to clipboard |
| `float_vector(n)` | A fixed length vector of floating point numbers | `[3.14, 42.21]` |
| `ROW` | A composite type made up of a number of inner types/fields. Similar to a<br>`tuple` in other languages. | No literal support yet. Result format depends on the used protocol. HTTP<br>uses a list. PostgreSQL serializes it via the `record` type (`oid`<br>2249). |
| `UUID` | A unique identifier | No dedicated literal support. Use string casts:<br>`'65ace7f6-ac84-4920-a0ff-3c40bfd89478'::uuid` |

### [Ranges and widths](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id18) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#ranges-and-widths "Link to this heading")

This section lists all data types supported by CrateDB at a glance in tabular
form, including some facts about their byte widths, value ranges and
properties.

Please note that the byte widths do not equal the total storage sizes, which
are likely to be larger due to additional metadata.

| Type | Width | Range | Description |
| --- | --- | --- | --- |
| `BOOLEAN` | 1 byte | `true` or `false` | Boolean type |
| `VARCHAR(n)` | variable | Minimum length: 1. Maximum length: 2^31-1 (upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range). [\[1\]](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#f1) | Strings of variable length. All Unicode characters are allowed. |
| `TEXT` | variable | Minimum length: 1. Maximum length: 2^31-1 (upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range). [\[1\]](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#f1) | Strings of variable length. All Unicode characters are allowed. |
| `CHARACTER(n)`, `CHAR(n)` | variable | Minimum length: 1. Maximum length: 2^31-1 (upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range). [\[1\]](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#f1) | Strings of fixed length, blank padded. All Unicode characters are allowed. |
| `SMALLINT` | 2 bytes | -32,768 to 32,767 | Small-range integer |
| `INTEGER` | 4 bytes | -2^31 to 2^31-1 | Typical choice for integer |
| `BIGINT` | 8 bytes | -2^63 to 2^63-1 | Large-range integer |
| `NUMERIC` | variable | Up to 131072 digits before, and<br>up to 16383 digits after the decimal point | user-specified precision, exact |
| `REAL` | 4 bytes | 6 decimal digits precision | Inexact, variable-precision |
| `DOUBLE PRECISION` | 8 bytes | 15 decimal digits precision | Inexact, variable-precision |
| `TIMESTAMP WITH TIME ZONE` | 8 bytes | 292275054BC to 292278993AD | Time and date with time zone |
| `TIMESTAMP WITHOUT TIME ZONE` | 8 bytes | 292275054BC to 292278993AD | Time and date without time zone |
| `DATE` | 8 bytes | 292275054BC to 292278993AD | Date in UTC. Internally stored as `BIGINT`. |
| `TIME WITH TIME ZONE` | 12 bytes | 292275054BC to 292278993AD | 00:00:00.000000 to 23:59:59.999999<br>zone: -18:00 to 18:00 |
| `BIT(n)` | variable | A sequence of `0` or `1` digits.<br>Minimum length: 1. Maximum length: 2^31-1 (upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range). | A string representation of a bit sequence. |
| `IP` | 8 bytes | IP addresses are stored as `BIGINT` values. | A string representation of an IP address (IPv4 or IPv6). |
| `OBJECT` | variable | The theoretical maximum length (number of key/value pairs) is slightly below Java’s `Integer.MAX_VALUE`. | An object is structured as a collection of key-values, containing any other type,<br>including further child objects. |
| `ARRAY` | variable | The theoretical maximum length (number of elements) is slightly below Java’s `Integer.MAX_VALUE`. | An array is structured as a sequence of any other type. |
| `GEO_POINT` | 16 bytes | Each coordinate is stored as a `DOUBLE PRECISION` type. | A `GEO_POINT` is a geographic data type used to store latitude and longitude coordinates. |
| `GEO_SHAPE` | variable | Each coordinate is stored as a `DOUBLE PRECISION` type. | A `GEO_SHAPE` column can store different kinds of [GeoJSON geometry objects](https://datatracker.ietf.org/doc/html/rfc7946). |
| `FLOAT_VECTOR(n)` | `n` | Vector Minimum length: 1. Maximum length: 2048. | A vector of floating point numbers. |
| `UUID` | 16 bytes | Any valid UUID. | A universally unique identifier as a 128-bit number |

Footnotes

### [Precedence and type conversion](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id19) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#precedence-and-type-conversion "Link to this heading")

When expressions of different data types are combined by operators or scalars,
the data type with the lower precedence is converted to the data type
with the higher precedence. If an implicit conversion between the types isn’t
supported, an error is returned.

The following precedence order is used for data types (highest to lowest):

01. Custom (complex) types (currently: [bitstring](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-bit-strings),
    [float\_vector](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-float-vector)) (highest)

02. [GEO\_SHAPE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo-shape)

03. [JSON](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-type-json)

04. [OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-objects)

05. [GEO\_POINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo-point)

06. `Record` (internal type, return type of
    [table functions](https://cratedb.com/docs/crate/reference/en/master/general/builtins/table-functions.html#table-functions))

07. [Array](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-arrays)

08. [Numeric](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-numeric)

09. [Double precision](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-double-precision)

10. [Real](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-real)

11. [IP](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-ip-addresses)

12. [Bigint](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-bigint)

13. [UUID](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-uuid)

14. [Timestamp without time zone](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz)

15. [Timestamp with time zone](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-with-tz)

16. [Date](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-date)

17. [Interval](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-interval)

18. [Regclass](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-regclass)

19. [Regproc](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-regproc)

20. [Integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer)

21. [Time with time zone](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-time)

22. [Smallint](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-smallint)

23. [Boolean](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-boolean)

24. [“Char”](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-char)

25. [Text](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text)

26. [Character](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-type-character)

27. [NULL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-null) (lowest)


## [Primitive types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id20) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#primitive-types "Link to this heading")

Primitive types are types with [scalar](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-scalar) values:

### [Null values](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id43) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#null-values "Link to this heading")

#### [`NULL`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id44) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#null "Link to this heading")

A `NULL` represents a missing value.

Note

`NULL` values are not the same as `0`, an empty string (`''`), an
empty object (`{}`), an empty array (`[]`), or any other kind of empty
or zeroed data type.

You can use `NULL` values when inserting records to indicate the absence of a
data point when the value for a specific column is not known.

Similarly, CrateDB will produce `NULL` values when, for example, data is
missing from an [outer left-join](https://cratedb.com/docs/crate/reference/en/master/concepts/joins.html#join-types-outer) operation. This
happens when a row from one relation has no corresponding row in the joined
relation.

If you insert a record without specifying the value for a particular column,
CrateDB will insert a `NULL` value for that column.

For example:

```
cr> CREATE TABLE users (
...     first_name TEXT,
...     surname TEXT
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

Insert a record without specifying `surname`:

```
cr> INSERT INTO users (
...     first_name
... ) VALUES (
...     'Alice'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

The resulting row will have a `NULL` value for `surname`:

```
cr> SELECT
...     first_name,
...     surname
... FROM users
... WHERE first_name = 'Alice';
+------------+---------+
| first_name | surname |
+------------+---------+
| Alice      | NULL    |
+------------+---------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can prevent `NULL` values being inserted altogether with a [NOT NULL\\
constraint](https://cratedb.com/docs/crate/reference/en/master/sql/general/constraints.html#not-null-constraint), like so:

```
cr> CREATE TABLE users_with_surnames (
...     first_name TEXT,
...     surname TEXT NOT NULL
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

Now, when you try to insert a user without a surname, it will produce an
error:

```
cr> INSERT INTO users_with_surnames (
...     first_name
... ) VALUES (
...     'Alice'
... );
SQLParseException["surname" must not be null]
```

Copy to clipboard

### [Boolean values](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id45) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#boolean-values "Link to this heading")

#### [`BOOLEAN`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id46) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#boolean "Link to this heading")

A basic boolean type accepting `true` and `false` as values.

Example:

```
cr> CREATE TABLE my_table (
...     first_column BOOLEAN
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     first_column
... ) VALUES (
...     true
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT * FROM my_table;
+--------------+
| first_column |
+--------------+
| TRUE         |
+--------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

### [Character data](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id47) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#character-data "Link to this heading")

Character types are general purpose strings of character data.

CrateDB supports the following character types:

Note

Only character data types without specified length can be [analyzed\\
for full text search](https://cratedb.com/docs/crate/reference/en/master/general/ddl/fulltext-indices.html#sql-ddl-index-fulltext).

By default, the [plain](https://cratedb.com/docs/crate/reference/en/master/general/ddl/analyzers.html#plain-analyzer) analyzer is used.

#### [`VARCHAR(n)`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id69) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#varchar-n "Link to this heading")

The `VARCHAR(n)` (or `CHARACTER VARYING(n)`) type represents variable
length strings. All Unicode characters are allowed.

The optional length specification `n` is a positive [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) that defines the maximum length, in characters, of the
values that have to be stored or cast. The minimum length is `1`. The maximum
length is defined by the upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range.

An attempt to store a string literal that exceeds the specified length
of the character data type results in an error.

```
cr> CREATE TABLE users (
...     id VARCHAR,
...     name VARCHAR(3)
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Alice Smith'
... );
SQLParseException['Alice Smith' is too long for the text type of length: 3]
```

Copy to clipboard

If the excess characters are all spaces, the string literal will be truncated
to the specified length.

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Bob     '
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...    id,
...    name,
...    char_length(name) AS name_length
... FROM users;
+----+------+-------------+
| id | name | name_length |
+----+------+-------------+
| 1  | Bob  |           3 |
+----+------+-------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

If a value is explicitly cast to `VARCHAR(n)`, then an over-length value
will be truncated to `n` characters without raising an error.

```
cr> SELECT 'Alice Smith'::VARCHAR(5) AS name;
+-------+
| name  |
+-------+
| Alice |
+-------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

`CHARACTER VARYING` and `VARCHAR` without the length specifier are
aliases for the [text](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text) data type,
see also [type aliases](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-postgres-aliases).

#### [`CHARACTER(n)`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id70) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#character-n "Link to this heading")

The `CHARACTER(n)` (or `CHAR(n)`) type represents fixed-length, blank padded
strings. All Unicode characters are allowed.

The optional length specification `n` is a positive [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) that defines the maximum length, in characters, of the
values that have to be stored or cast. The minimum length is `1`. The maximum
length is defined by the upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range.
If the type is used without the length parameter, a length of `1` is used.

An attempt to store a string literal that exceeds the specified length
of the character data type results in an error.

```
cr> CREATE TABLE users (
...     id CHARACTER,
...     name CHAR(3)
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Alice Smith'
... );
SQLParseException['Alice Smith' is too long for the character type of length: 3]
```

Copy to clipboard

If the excess characters are all spaces, the string literal will be truncated
to the specified length.

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Bob     '
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...    id,
...    name,
...    char_length(name) AS name_length
... FROM users;
+----+------+-------------+
| id | name | name_length |
+----+------+-------------+
| 1  | Bob  |           3 |
+----+------+-------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Bob     '
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

If a value is inserted with a length lower than the defined one, the value will
be right padded with whitespaces.

```
cr> INSERT INTO users (
...     id,
...     name
... ) VALUES (
...     '1',
...     'Bo'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...    id,
...    name,
...    char_length(name) AS name_length
... FROM users;
+----+------+-------------+
| id | name | name_length |
+----+------+-------------+
| 1  | Bo   |           3 |
+----+------+-------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

If a value is explicitly cast to `CHARACTER(n)`, then an over-length value
will be truncated to `n` characters without raising an error.

```
cr> SELECT 'Alice Smith'::CHARACTER(5) AS name;
+-------+
| name  |
+-------+
| Alice |
+-------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`TEXT`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id71) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#text "Link to this heading")

A text-based basic type containing one or more characters. All Unicode
characters are allowed.

Create table:

```
cr> CREATE TABLE users (
...     name TEXT
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

Insert data:

```
cr> INSERT INTO users (
...     name
... ) VALUES (
...     '🌻 Alice 🌻'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Query data:

```
cr> SELECT * FROM users;
+-------------+
| name        |
+-------------+
| 🌻 Alice 🌻 |
+-------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Note

The maximum indexed string length is restricted to 32766 bytes when encoded
with UTF-8 unless the string is analyzed using full text or indexing and the
usage of the [Column store](https://cratedb.com/docs/crate/reference/en/master/general/ddl/storage.html#ddl-storage-columnstore) is disabled.

There is no difference in storage costs among all character data types.

#### [`json`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id72) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#json "Link to this heading")

A type representing a JSON string.

This type only exists for compatibility and interoperability with PostgreSQL. It cannot to be
used in data definition statements and it is not possible to use it to store data.
To store JSON data use the existing [OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-objects) type. It is a more powerful
alternative that offers more flexibility but delivers the same benefits.

The primary use of the JSON type is in [type casting](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting) for
interoperability with PostgreSQL clients which may use the `JSON` type.
The following type casts are example of supported usage of the `JSON` data type:

Casting from `STRING` to `JSON`:

```
cr> SELECT '{"x": 10}'::json;
+---------------------------+
| CAST('{"x": 10}' AS json) |
+---------------------------+
| {"x": 10}                 |
+---------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Casting from `JSON` to `OBJECT`:

```
cr> SELECT ('{"x": 10}'::json)::object;
+-------------------------------------------+
| CAST(CAST('{"x": 10}' AS json) AS object) |
+-------------------------------------------+
| {"x": 10}                                 |
+-------------------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Casting from `OBJECT` to `JSON`:

```
cr> SELECT {x=10}::json;
+-------------------------+
| CAST({"x"= 10} AS json) |
+-------------------------+
| {"x":10}                |
+-------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

### [Numeric data](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id52) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#numeric-data "Link to this heading")

CrateDB supports the following numeric types:

Note

The [REAL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-real) and [DOUBLE PRECISION](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-double-precision) data types are inexact, variable-precision
floating-point types, meaning that these types are stored as an
approximation.

Accordingly, storage, calculation, and retrieval of the value will not
always result in an exact representation of the actual floating-point
value. For instance, the result of applying [SUM](https://cratedb.com/docs/crate/reference/en/master/general/builtins/aggregation.html#aggregation-sum)
or [AVG](https://cratedb.com/docs/crate/reference/en/master/general/builtins/aggregation.html#aggregation-avg) aggregate functions may slightly vary
between query executions or comparing floating-point values for equality
might not always match.

CrateDB conforms to the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) standard concerning special values for
floating-point data types, meaning that `NaN`, `Infinity`,
`-Infinity` (negative infinity), and `-0` (signed zero) are all
supported:

```
cr> SELECT
...     0.0 / 0.0 AS a,
...     1.0 / 0.0 AS B,
...     1.0 / -0.0 AS c;
+-----+----------+-----------+
| a   | b        | c         |
+-----+----------+-----------+
| NaN | Infinity | -Infinity |
+-----+----------+-----------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

These special numeric values can also be inserted into a column of type
`REAL` or `DOUBLE PRECISION` using a [TEXT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text) literal.

For instance:

```
cr> CREATE TABLE my_table (
...     column_1 INTEGER,
...     column_2 BIGINT,
...     column_3 SMALLINT,
...     column_4 DOUBLE PRECISION,
...     column_5 REAL,
...     column_6 "CHAR"
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     column_4,
...     column_5
... ) VALUES (
...     'NaN',
...     'Infinity'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...     column_4,
...     column_5
... FROM my_table;
+----------+----------+
| column_4 | column_5 |
+----------+----------+
| NaN      | Infinity |
+----------+----------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`SMALLINT`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id73) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#smallint "Link to this heading")

A small integer.

Limited to two bytes, with a range from -32,768 to 32,767.

Example:

```
cr> CREATE TABLE my_table (
...     number SMALLINT
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     32767
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT number FROM my_table;
+--------+
| number |
+--------+
| 32767  |
+--------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`INTEGER`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id74) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#integer "Link to this heading")

An integer.

Limited to four bytes, with a range from -2^31 to 2^31-1.

Example:

```
cr> CREATE TABLE my_table (
...     number INTEGER
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     2147483647
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT number FROM my_table;
+------------+
| number     |
+------------+
| 2147483647 |
+------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`BIGINT`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id75) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#bigint "Link to this heading")

A large integer.

Limited to eight bytes, with a range from -2^63 + 1 to 2^63-2.

Example:

```
cr> CREATE TABLE my_table (
...     number BIGINT
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     9223372036854775806
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT number FROM my_table;
+---------------------+
| number              |
+---------------------+
| 9223372036854775806 |
+---------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`NUMERIC(precision, scale)`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id76) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#numeric-precision-scale "Link to this heading")

An exact [fixed-point fractional number](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) with an arbitrary, user-specified
precision.

Variable size, with up to 38 digits for storage.

If using `NUMERIC` only for type casts up to 131072 digits before the decimal
point and up to 16383 digits after the decimal point are supported.

For example, using a [cast from a string literal](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-str):

```
cr> SELECT NUMERIC(5, 2) '123.45' AS number;
+--------+
| number |
+--------+
| 123.45 |
+--------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

This type is usually used when it is important to preserve exact precision
or handle values that exceed the range of the numeric types of the fixed
length. The aggregations and arithmetic operations on numeric values are
much slower compared to operations on the integer or floating-point types.

The `NUMERIC` type can be configured with the `precision` and
`scale`. The `precision` value of a numeric is the total count of
significant digits in the unscaled numeric value. The `scale` value of a
numeric is the count of decimal digits in the fractional part, to the right of
the decimal point. For example, the number 123.45 has a precision of `5` and
a scale of `2`. Integers have a scale of zero.
The scale must be less than or equal to the precision and greater or equal to zero.

To declare the `NUMERIC` type with the precision and scale, use the syntax:

```
NUMERIC(precision, scale)
```

Copy to clipboard

Alternatively, only the precision can be specified, the scale will be zero
or positive integer in this case:

```
NUMERIC(precision)
```

Copy to clipboard

Without configuring the precision and scale the `NUMERIC` type value will be
represented by an unscaled value of the unlimited precision:

```
NUMERIC
```

Copy to clipboard

Note

`NUMERIC` without precision and scale cannot be used in CREATE TABLE
statements. To store values of type NUMERIC it is required to define the
precision and scale.

Note

`NUMERIC` values returned as results of an SQL query might loose precision

when using the [HTTP interface](https://cratedb.com/docs/crate/reference/en/master/interfaces/http.html#interface-http), because of limitation
of [JSON Data Types](https://en.wikipedia.org/wiki/JSON#Data_types) for numbers with higher than 53-bits precision.

Caution

`NUMERIC` operations, for example [scalar function](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-functions)
and [aggregations](https://cratedb.com/docs/crate/reference/en/master/general/builtins/aggregation.html#aggregation) may consume more memory and have worse
performance compared to their [REAL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-real) and
[DOUBLE PRECISION](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-double-precision), so consider using those types, unless the
increased precision, offered by `NUMERIC`, is desired.

The `NUMERIC` type is internally backed by the Java `BigDecimal` class. For
more detailed information about its behaviour, see [BigDecimal documentation](https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/math/BigDecimal.html).

#### [`UUID`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id77) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#uuid "Link to this heading")

A [universally unique identifier](https://en.wikipedia.org/wiki/Uuid) stored as a 128-bit number.

Example:

```
cr> CREATE TABLE tbl (
...   id uuid
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO tbl (id) VALUES ('55d07626-4927-47c5-ba43-a015c23632ef');
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT id FROM tbl
+--------------------------------------+
| id                                   |
+--------------------------------------+
| 55d07626-4927-47c5-ba43-a015c23632ef |
+--------------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`REAL`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id78) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#real "Link to this heading")

An inexact [single-precision floating-point](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) value.

Limited to four bytes, six decimal digits precision.

Example:

```
cr> CREATE TABLE my_table (
...     number REAL
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     3.4028235e+38
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Tip

`3.4028235+38` represents the value 3.4028235 × 1038

```
cr> SELECT number FROM my_table;
+---------------+
| number        |
+---------------+
| 3.4028235e+38 |
+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can insert values which exceed the maximum precision, like so:

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     3.4028234664e+38
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

However, the recorded value will be an approximation of the original (i.e., the
additional precision is lost):

```
cr> SELECT number FROM my_table;
+---------------+
| number        |
+---------------+
| 3.4028235e+38 |
+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

See also

[CrateDB floating-point values](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-floating-point)

#### [`DOUBLE PRECISION`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id79) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#double-precision "Link to this heading")

An inexact number with variable precision supporting [double-precision\\
floating-point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) values.

Limited to eight bytes, with 15 decimal digits precision.

Example:

```
cr> CREATE TABLE my_table (
...     number DOUBLE PRECISION
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     1.7976931348623157e+308
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Tip

`1.7976931348623157e+308` represents the value 1.7976931348623157 × 10308

```
cr> SELECT number FROM my_table;
+-------------------------+
| number                  |
+-------------------------+
| 1.7976931348623157e+308 |
+-------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can insert values which exceed the maximum precision, like so:

```
cr> INSERT INTO my_table (
...     number
... ) VALUES (
...     1.79769313486231572014e+308
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

However, the recorded value will be an approximation of the original (i.e., the
additional precision is lost):

```
cr> SELECT number FROM my_table;
+-------------------------+
| number                  |
+-------------------------+
| 1.7976931348623157e+308 |
+-------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

See also

[CrateDB floating-point values](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-floating-point)

### [Dates and times](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id60) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#dates-and-times "Link to this heading")

CrateDB supports the following types for dates and times:

With a few exceptions (noted below), the `+` and `-` [operators](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-operator) can be used to create [arithmetic expressions](https://cratedb.com/docs/crate/reference/en/master/general/builtins/arithmetic.html#arithmetic) with temporal operands:

| Operand | Operator | Operand |
| --- | --- | --- |
| `TIMESTAMP` | `-` | `TIMESTAMP` |
| `INTERVAL` | `+` | `TIMESTAMP` |
| `TIMESTAMP` | `+` or `-` | `INTERVAL` |
| `INTERVAL` | `+` or `-` | `INTERVAL` |

Note

If an object column is [dynamically created](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic), the type detection will not recognize date
and time types, meaning that date and time type columns must always be
declared beforehand.

#### [`TIMESTAMP`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id80) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#timestamp "Link to this heading")

A timestamp expresses a specific date and time as the number of milliseconds
since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time) (i.e., `1970-01-01T00:00:00Z`).

`TIMESTAMP` has two variants:

- [TIMESTAMP WITHOUT TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz) which

presents all values in UTC.

- [TIMESTAMP WITH TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-with-tz) which presents
all values in UTC in respect to the `TIME ZONE` related offset.


By default a `TIMESTAMP` is an alias for [TIMESTAMP WITHOUT TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz).

Timestamps can be expressed as string literals (e.g.,
`'1970-01-02T00:00:00'`) with the following syntax:

```
date-element [time-separator [time-element [offset]]]

date-element:   yyyy-MM-dd
time-separator: 'T' | ' '
time-element:   HH:mm:ss [fraction]
fraction:       '.' digit+
offset:         {+ | -} HH [:mm] | 'Z'
```

Copy to clipboard

See also

For more information about date and time formatting, see [Java 15:\\
Patterns for Formatting and Parsing](https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/time/format/DateTimeFormatter.html#patterns).

Time zone syntax as defined by [ISO 8601 time zone designators](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators).

Internally, CrateDB stores timestamps as [BIGINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-bigint)
values, which are limited to eight bytes.

If you cast a [BIGINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-bigint) to a `TIMEZONE`, the integer value
will be interpreted as the number of milliseconds since the Unix epoch.

Using the [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) function, for readability:

```
cr> SELECT
...     date_format(0::TIMESTAMP) AS ts_0,
...     date_format(1000::TIMESTAMP) AS ts_1;
+-----------------------------+-----------------------------+
| ts_0                        | ts_1                        |
+-----------------------------+-----------------------------+
| 1970-01-01T00:00:00.000000Z | 1970-01-01T00:00:01.000000Z |
+-----------------------------+-----------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

If you cast a [REAL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-real) or a [DOUBLE PRECISION](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-double-precision) to a `TIMESTAMP`, the numeric value will be
interpreted as the number of seconds since the Unix epoch, with fractional
values approximated to the nearest millisecond:

```
cr> SELECT
...     date_format(0::TIMESTAMP) AS ts_0,
...     date_format(1.5::TIMESTAMP) AS ts_1;
+-----------------------------+-----------------------------+
| ts_0                        | ts_1                        |
+-----------------------------+-----------------------------+
| 1970-01-01T00:00:00.000000Z | 1970-01-01T00:00:01.500000Z |
+-----------------------------+-----------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

If you cast a literal to a `TIMESTAMP`, years outside the range 0000 to 9999
must be prefixed by the plus or minus symbol. See also [Year.parse Javadoc](https://docs.oracle.com/javase/8/docs/api/java/time/Year.html#parse-java.lang.CharSequence-):

```
cr> SELECT '+292278993-12-31T23:59:59.999Z'::TIMESTAMP as tmstp;
+---------------------+
|               tmstp |
+---------------------+
| 9223372017129599999 |
+---------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Caution

Due to internal date parsing, the full `BIGINT` range is not supported
for timestamp values. The valid range of dates is from `292275054BC` to
`292278993AD`.

When inserting timestamps smaller than `-999999999999999` (equal to
`-29719-04-05T22:13:20.001Z`) or bigger than `999999999999999` (equal
to `33658-09-27T01:46:39.999Z`) rounding issues may occur.

A `TIMESTAMP` can be further defined as:

##### [`WITH TIME ZONE`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id87) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#with-time-zone "Link to this heading")

If you define a timestamp as `TIMESTAMP WITH TIME ZONE`, CrateDB will convert
string literals to [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC) using the `offset`
value (e.g., `+01:00` for plus one hour or `Z` for UTC).

Example:

```
cr> CREATE TABLE my_table (
...     ts_tz_1 TIMESTAMP WITH TIME ZONE,
...     ts_tz_2 TIMESTAMP WITH TIME ZONE
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     ts_tz_1,
...     ts_tz_2
... ) VALUES (
...     '1970-01-02T00:00:00',
...     '1970-01-02T00:00:00+01:00'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...     ts_tz_1,
...     ts_tz_2
... FROM my_table;
+----------+----------+
|  ts_tz_1 |  ts_tz_2 |
+----------+----------+
| 86400000 | 82800000 |
+----------+----------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can use [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) to make the output
easier to read:

```
cr> SELECT
...     date_format('%Y-%m-%dT%H:%i', ts_tz_1) AS ts_tz_1,
...     date_format('%Y-%m-%dT%H:%i', ts_tz_2) AS ts_tz_2
... FROM my_table;
+------------------+------------------+
| ts_tz_1          | ts_tz_2          |
+------------------+------------------+
| 1970-01-02T00:00 | 1970-01-01T23:00 |
+------------------+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Notice that `ts_tz_2` is smaller than `ts_tz_1` by one hour. CrateDB used
the `+01:00` offset (i.e., _ahead of UTC by one hour_) to convert the second
timestamp into UTC prior to insertion. Contrast this with the behavior of
[WITHOUT TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz).

Note

`TIMESTAMPTZ` is an alias for `TIMESTAMP WITH TIME ZONE`.

##### [`WITHOUT TIME ZONE`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id88) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#without-time-zone "Link to this heading")

If you define a timestamp as `TIMESTAMP WITHOUT TIME ZONE`, CrateDB will
convert string literals to [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC) without using
the `offset` value (i.e., any time zone information present is stripped prior
to insertion).

Example:

```
cr> CREATE TABLE my_table (
...     ts_1 TIMESTAMP WITHOUT TIME ZONE,
...     ts_2 TIMESTAMP WITHOUT TIME ZONE
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     ts_1,
...     ts_2
... ) VALUES (
...     '1970-01-02T00:00:00',
...     '1970-01-02T00:00:00+01:00'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Using the [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) function, for readability:

```
cr> SELECT
...     date_format('%Y-%m-%dT%H:%i', ts_1) AS ts_1,
...     date_format('%Y-%m-%dT%H:%i', ts_2) AS ts_2
... FROM my_table;
+------------------+------------------+
| ts_1             | ts_2             |
+------------------+------------------+
| 1970-01-02T00:00 | 1970-01-02T00:00 |
+------------------+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Notice that `ts_1` and `ts_2` are identical. CrateDB ignored the `+01:00`
offset (i.e., _ahead of UTC by one hour_) when processing the second string
literal. Contrast this with the behavior of [WITH TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-with-tz).

##### [`AT TIME ZONE`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id89) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#at-time-zone "Link to this heading")

You can use the `AT TIME ZONE` clause to modify a timestamp in two different
ways. It converts a timestamp without time zone to a timestamp with time zone
and vice versa.

Note

The `AT TIME ZONE` type is only supported as a type literal (i.e., for
use in SQL [expressions](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression), like a [type cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-exp), as below).

You cannot create table columns of type `AT TIME ZONE`.

###### [Convert a timestamp time zone](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id90) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#convert-a-timestamp-time-zone "Link to this heading")

If you use `AT TIME ZONE tz` with a `TIMESTAMP WITH TIME ZONE`, CrateDB
will convert the timestamp to time zone `tz` and cast the return value as a
[TIMESTAMP WITHOUT TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz) (which discards
the time zone information). This process effectively allows you to correct
the offset used to calculate UTC.

Example:

```
cr> CREATE TABLE my_table (
...     ts_tz TIMESTAMP WITH TIME ZONE
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     ts_tz
... ) VALUES (
...     '1970-01-02T00:00:00'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Using the [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) function, for readability:

```
cr> SELECT date_format(
...     '%Y-%m-%dT%H:%i', ts_tz AT TIME ZONE '+01:00'
... ) AS ts
... FROM my_table;
+------------------+
| ts               |
+------------------+
| 1970-01-02T01:00 |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Tip

The `AT TIME ZONE` clause does the same as the [timezone()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-timezone) function:

```
cr> SELECT
...     date_format('%Y-%m-%dT%H:%i', ts_tz AT TIME ZONE '+01:00') AS ts_1,
...     date_format('%Y-%m-%dT%H:%i', timezone('+01:00', ts_tz)) AS ts_2
... FROM my_table;
+------------------+------------------+
| ts_1             | ts_2             |
+------------------+------------------+
| 1970-01-02T01:00 | 1970-01-02T01:00 |
+------------------+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

###### [Add a timestamp time zone](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id91) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#add-a-timestamp-time-zone "Link to this heading")

If you use `AT TIME ZONE` with a [TIMESTAMP WITHOUT TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-with-tz), CrateDB will add the missing time zone information,
recalculate the timestamp in UTC, and cast the return value as a
[TIMESTAMP WITH TIME ZONE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp-without-tz).

Example:

```
cr> CREATE TABLE my_table (
...     ts TIMESTAMP WITHOUT TIME ZONE
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     ts
... ) VALUES (
...     '1970-01-02T00:00:00'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Using the [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) function, for readability:

```
cr> SELECT date_format(
...     '%Y-%m-%dT%H:%i', ts AT TIME ZONE '+01:00'
... ) AS ts_tz
... FROM my_table;
+------------------+
| ts_tz            |
+------------------+
| 1970-01-01T23:00 |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Tip

The `AT TIME ZONE` clause does the same as the [timezone()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-timezone) function:

```
cr> SELECT date_format(
...     '%Y-%m-%dT%H:%i', timezone('+01:00', ts)
... ) AS ts_tz
... FROM my_table;
+------------------+
| ts_tz            |
+------------------+
| 1970-01-01T23:00 |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`TIME`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id84) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#time "Link to this heading")

A `TIME` expresses a specific time as the number of milliseconds
since midnight along with a time zone offset.

Limited to 12 bytes, with a time range from `00:00:00.000000` to
`23:59:59.999999` and a time zone range from `-18:00` to `18:00`.

Caution

CrateDB does not support `TIME` by itself or `TIME WITHOUT TIME ZONE`.
You must always specify `TIME WITH TIME ZONE` or its alias `TIMETZ`.

This behaviour does not comply with standard SQL and is incompatible with
PostgreSQL. This behavior may change in a future version of CrateDB (see
[tracking issue #11491](https://github.com/crate/crate/issues/11491)).

Note

The `TIME` type is only supported as a type literal (i.e., for use in
SQL [expressions](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression), like a [type cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-exp), as below).

You cannot create table columns of type `TIME`.

Times can be expressed as string literals (e.g., `'13:00:00'`) with the
following syntax:

```
time-element [offset]

time-element: time-only [fraction]
time-only:    HH[[:][mm[:]ss]]
fraction:     '.' digit+
offset:       {+ | -} time-only | geo-region
geo-region:   As defined by ISO 8601.
```

Copy to clipboard

Above, `fraction` accepts up to six digits, with a precision in microseconds.

See also

For more information about time formatting, see [Java 15: Patterns for\\
Formatting and Parsing](https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/time/format/DateTimeFormatter.html#patterns).

Time zone syntax as defined by [ISO 8601 time zone designators](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators).

For example:

```
cr> SELECT '13:00:00'::TIMETZ AS t_tz;
+------------------+
| t_tz             |
+------------------+
| [46800000000, 0] |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

The value of first element is the number of milliseconds since midnight. The
value of the second element is the number of seconds corresponding to the time
zone offset (zero in this instance, as no time zone was specified).

For example, with a `+01:00` time zone:

```
cr> SELECT '13:00:00+01:00'::TIMETZ AS t_tz;
+---------------------+
| t_tz                |
+---------------------+
| [46800000000, 3600] |
+---------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

The time zone offset is calculated as 3600 seconds, which is equivalent to an
hour.

Negative time zone offsets will return negative seconds:

```
cr> SELECT '13:00:00-01:00'::TIMETZ AS t_tz;
+----------------------+
| t_tz                 |
+----------------------+
| [46800000000, -3600] |
+----------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Here’s an example that uses fractional seconds:

```
cr> SELECT '13:59:59.999999'::TIMETZ as t_tz;
+------------------+
| t_tz             |
+------------------+
| [50399999999, 0] |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Caution

The current implementation of the `TIME` type has the following
limitations:

- `TIME` types cannot be [cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-exp) to any
other types (including [TEXT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text))

- `TIME` types cannot be used in [arithmetic expressions](https://cratedb.com/docs/crate/reference/en/master/general/builtins/arithmetic.html#arithmetic) (e.g., with `TIME`, `DATE`, and
`INTERVAL` types)

- `TIME` types cannot be used with time and date scalar functions (e.g.,
[date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) and [extract()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-extract))


This behaviour does not comply with standard SQL and is incompatible with
PostgreSQL. This behavior may change in a future version of CrateDB (see
[tracking issue #11528](https://github.com/crate/crate/issues/11528)).

#### [`DATE`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id85) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#date "Link to this heading")

A `DATE` expresses a specific year, month and a day in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

Internally, CrateDB stores dates as [BIGINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-bigint) values, which
are limited to eight bytes.

If you cast a [BIGINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-bigint) to a `DATE`, the integer value will
be interpreted as the number of milliseconds since the Unix epoch. If you cast
a [REAL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-real) or a [DOUBLE PRECISION](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-double-precision)
to a `DATE`, the numeric value will be interpreted as the number of seconds
since the Unix epoch.

If you cast a literal to a `DATE`, years outside the range 0000 to 9999
must be prefixed by the plus or minus symbol. See also [Year.parse Javadoc](https://docs.oracle.com/javase/8/docs/api/java/time/Year.html#parse-java.lang.CharSequence-):

```
cr> SELECT '+10000-03-09'::DATE as date;
+-----------------+
|            date |
+-----------------+
| 253408176000000 |
+-----------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Caution

Due to internal date parsing, the full `BIGINT` range is not supported
for timestamp values. The valid range of dates is from `292275054BC` to
`292278993AD`.

When inserting dates smaller than `-999999999999999` (equal to
`-29719-04-05`) or bigger than `999999999999999` (equal
to `33658-09-27`) rounding issues may occur.

Warning

The `DATE` type was not designed to allow time-of-day information (i.e.,
it is supposed to have a resolution of one day).

However, CrateDB allows you violate that constraint by casting any number
of milliseconds within limits to a `DATE` type. The result is then
returned as a [TIMESTAMP](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-timestamp). When used in conjunction
with [arithmetic expressions](https://cratedb.com/docs/crate/reference/en/master/general/builtins/arithmetic.html#arithmetic), these `TIMESTAMP` values
may produce unexpected results.

This behaviour does not comply with standard SQL and is incompatible with
PostgreSQL. This behavior may change in a future version of CrateDB (see
[tracking issue #11528](https://github.com/crate/crate/issues/11528)).

Caution

The current implementation of the `DATE` type has the following
limitations:

- `DATE` types cannot be added or subtracted to or from other `DATE`
types as expected (i.e., to calculate the difference between the two in
a number of days).

Doing so will convert both `DATE` values into `TIMESTAMP` values
before performing the operation, resulting in a `TIMESTAMP` value
corresponding to a full date and time (see [WARNING](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-date-warning) above).

- [Numeric data types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-numeric) cannot be added to or
subtracted from `DATE` types as expected (e.g., to increase the date by
`n` days).

Doing so will, for example, convert the `DATE` into a `TIMESTAMP` and
increase the value by `n` milliseconds (see [WARNING](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-date-warning) above).

- [TIME](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-time) types cannot be added to or subtracted from
`DATE` types.

- [INTERVAL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-interval) types cannot be added to or subtracted
from `DATE` types.


This behaviour does not comply with standard SQL and is incompatible with
PostgreSQL. This behavior may change in a future version of CrateDB (see
[tracking issue #11528](https://github.com/crate/crate/issues/11528)).

Note

The `DATE` type is only supported as a type literal (i.e., for use in
SQL [expressions](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression), like a [type cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-exp), as below).

You cannot create table columns of type `DATE`.

Dates can be expressed as string literals (e.g., `'2021-03-09'`) with the
following syntax:

```
yyyy-MM-dd
```

Copy to clipboard

See also

For more information about date and time formatting, see [Java 15:\\
Patterns for Formatting and Parsing](https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/time/format/DateTimeFormatter.html#patterns).

For example, using the [date\_format()](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-date-format) function, for
readability:

```
cr> SELECT
...    date_format(
...        '%Y-%m-%d',
...        '2021-03-09'::DATE
...    ) AS date;
+------------+
| date       |
+------------+
| 2021-03-09 |
+------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### [`INTERVAL`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id86) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#interval "Link to this heading")

An `INTERVAL` represents a span of time.

Note

The `INTERVAL` type is only supported as a type literal (i.e., for use in
SQL [expressions](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression), like a [type cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-exp), as above).

You cannot create table columns of type `INTERVAL`.

The basic syntax is:

```
INTERVAL <quantity> <unit>
```

Copy to clipboard

Where `unit` can be any of the following:

- `YEAR`

- `MONTH`

- `DAY`

- `HOUR`

- `MINUTE`

- `SECOND`

- `MILLISECOND`


For example:

```
cr> SELECT INTERVAL '1' DAY AS result;
+----------------+
| result         |
+----------------+
| 1 day 00:00:00 |
+----------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Intervals can be positive or negative:

```
cr> SELECT INTERVAL -'1' DAY AS result;
+------------------+
| result           |
+------------------+
| -1 days 00:00:00 |
+------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

When using `SECOND`, you can define fractions of a seconds (with a precision
of zero to six digits):

```
cr> SELECT INTERVAL '1.5' SECOND AS result;
+--------------+
| result       |
+--------------+
| 00:00:01.500 |
+--------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Caution

The `INTERVAL` data type does not currently support the input units
`MILLENNIUM`, `CENTURY`, `DECADE`, or
`MICROSECOND`.

This behaviour does not comply with standard SQL and is incompatible with
PostgreSQL. This behavior may change in a future version of CrateDB (see
[tracking issue #11490](https://github.com/crate/crate/issues/11490)).

You can also use the following syntax to express an interval:

```
INTERVAL <string>
```

Copy to clipboard

Where `string` describes the interval using one of the recognized formats:

| Description | Example | Equivalent |
| --- | --- | --- |
| Standard SQL format<br>(year-month) | `1-2` | 1 year 2 months |
| Standard SQL format | `1-2 3 4:05:06` | 1 year 2 months<br>3 days 4 hours<br>5 minutes 6 seconds |
| Standard SQL format<br>(day-time) | `3 4:05:06` | 3 days 4 hours<br>5 minutes 6 seconds |
| [PostgreSQL interval\<br>format](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-INTERVAL-INPUT) | `1 year 2 months<br>3 days 4 hours<br>5 minutes 6 seconds` | 1 year 2 months<br>3 days 4 hours<br>5 minutes 6 seconds |
| [ISO 8601 duration\<br>format](https://en.wikipedia.org/wiki/ISO_8601#Durations) | `P1Y2M3DT4H5M6S` | 1 year 2 months<br>3 days 4 hours<br>5 minutes 6 seconds |

For example:

```
cr> SELECT INTERVAL '1-2 3 4:05:06' AS result;
+-------------------------------+
| result                        |
+-------------------------------+
| 1 year 2 mons 3 days 04:05:06 |
+-------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can limit the precision of an interval by specifying `<unit> TO
<unit>` after the interval `string`.

For example, you can use `YEAR TO MONTH` to limit an interval to a day-month
value:

```
cr> SELECT INTERVAL '1-2 3 4:05:06' YEAR TO MONTH AS result;
+------------------------+
| result                 |
+------------------------+
| 1 year 2 mons 00:00:00 |
+------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can use `DAY TO HOUR`, as another example, to limit a day-time interval
to days and hours:

```
cr> SELECT INTERVAL '3 4:05:06' DAY TO HOUR AS result;
+-----------------+
| result          |
+-----------------+
| 3 days 04:00:00 |
+-----------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

You can multiply an interval by an integer:

```
cr> SELECT 2 * INTERVAL '2 years 1 month 10 days' AS result;
+---------------------------------+
| result                          |
+---------------------------------+
| 4 years 2 mons 20 days 00:00:00 |
+---------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Tip

You can use intervals in combination with [CURRENT\_TIMESTAMP](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-current-timestamp) to calculate values that are offset relative to the
current date and time.

For example, to calculate a timestamp corresponding to exactly one day ago,
use:

```
cr> SELECT CURRENT_TIMESTAMP - INTERVAL '1' DAY AS result;
+---------------+
| result        |
+---------------+
| ...           |
+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

### [Bit strings](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id65) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#bit-strings "Link to this heading")

#### [`BIT(n)`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id66) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#bit-n "Link to this heading")

A string representation of a bit sequence, useful for visualizing a [bit\\
mask](https://en.wikipedia.org/wiki/Mask_(computing)).

Values of this type can be created using the bit string literal syntax. A bit
string starts with the `B` prefix, followed by a sequence of `0` or `1`
digits quoted within single quotes `'`.

An example:

```
B'00010010'
```

Copy to clipboard

The optional length specification `n` is a positive [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) that defines the maximum length, in characters, of the
values that have to be stored or cast. The minimum length is `1`. The maximum
length is defined by the upper [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-integer) range.

For example:

```
cr> CREATE TABLE my_table (
...     bit_mask BIT(4)
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     bit_mask
... ) VALUES (
...     B'0110'
... );
INSERT OK, 1 row affected  (... sec)
```

Copy to clipboard

```
cr> SELECT bit_mask FROM my_table;
+----------+
| bit_mask |
+----------+
| B'0110'  |
+----------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Inserting values that are either too short or too long results in an error:

```
cr> INSERT INTO my_table (
...     bit_mask
... ) VALUES (
...    B'00101'
... );
SQLParseException[bit string length 5 does not match type bit(4)]
```

Copy to clipboard

### [IP addresses](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id67) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#ip-addresses "Link to this heading")

#### [`IP`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id68) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#ip "Link to this heading")

An `IP` is a string representation of an [IP address](https://en.wikipedia.org/wiki/IP_address) (IPv4 or IPv6).

Internally IP addresses are stored as `BIGINT` values, allowing expected
sorting, filtering, and aggregation.

For example:

```
cr> CREATE TABLE my_table (
...     fqdn TEXT,
...     ip_addr IP
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     fqdn,
...     ip_addr
... ) VALUES (
...     'localhost',
...     '127.0.0.1'
... ), (
...     'router.local',
...     'ff:0:ff:ff:0:ffff:c0a8:64'
... );
INSERT OK, 2 rows affected (... sec)
```

Copy to clipboard

```
cr> SELECT fqdn, ip_addr FROM my_table ORDER BY fqdn;
+--------------+---------------------------+
| fqdn         | ip_addr                   |
+--------------+---------------------------+
| localhost    | 127.0.0.1                 |
| router.local | ff:0:ff:ff:0:ffff:c0a8:64 |
+--------------+---------------------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

The `fqdn` column (see [Fully Qualified Domain Name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name)) will accept any value
because it was specified as [TEXT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text). However, trying to insert
`fake.ip` won’t work, because it is not a correctly formatted `IP`
address:

```
cr> INSERT INTO my_table (
...     fqdn,
...     ip_addr
... ) VALUES (
...     'localhost',
...     'fake.ip'
... );
SQLParseException[Cannot cast `'fake.ip'` of type `text` to type `ip`]
```

Copy to clipboard

IP addresses support the `<<` [operator](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-operator), which checks
for subnet inclusion using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_blocks). The left-hand [operand](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-operand) must an [IP type](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-ip) and the right-hand must be
[TEXT type](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text) (e.g., `'192.168.1.5' << '192.168.1/24'`).

## [Container types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id28) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#container-types "Link to this heading")

Container types are types with [nonscalar](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-nonscalar) values that
may contain other values:

### [Objects](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id92) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#objects "Link to this heading")

#### [`OBJECT`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id93) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#object "Link to this heading")

An object is structured as a collection of key-values.

An object can contain any other type, including further child objects. An
`OBJECT` column can be schemaless or can have a defined (i.e., enforced)
schema.

Objects are not the same as JSON objects, although they share a lot of
similarities. However, objects can be [inserted as JSON strings](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-object-json).

Syntax:

```
<columnName> OBJECT
    [ ({DYNAMIC|STRICT|IGNORED}) ]
    [ AS ( <columnDefinition>* ) ]
```

Copy to clipboard

The only required syntax is `OBJECT`.

The column policy (`DYNAMIC`, `STRICT`, or `IGNORED`) is optional and
defaults to [DYNAMIC](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic).

If the optional list of subcolumns (`columnDefinition`) is omitted, the
object will have no schema. CrateDB will create a schema for [DYNAMIC](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic) objects upon first insert.

Example:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     quotation OBJECT,
...     protagonist OBJECT(STRICT) AS (
...         age INTEGER,
...         first_name TEXT,
...         details OBJECT AS (
...             birthday TIMESTAMP WITH TIME ZONE
...         )
...     )
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     title,
...     quotation,
...     protagonist
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "words" = 'Curiouser and curiouser!',
...         "length" = 3
...     },
...     {
...         "age" = '10',
...         "first_name" = 'Alice',
...         "details" = {
...             "birthday" = '1852-05-04T00:00Z'::TIMESTAMPTZ
...         }
...     }
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT
...     protagonist['first_name'] AS name,
...     date_format(
...         '%D %b %Y',
...         'GMT',
...         protagonist['details']['birthday']
...      ) AS born,
...     protagonist['age'] AS age
... FROM my_table;
+-------+--------------+-----+
| name  | born         | age |
+-------+--------------+-----+
| Alice | 4th May 1852 |  10 |
+-------+--------------+-----+
SELECT 1 row in set (... sec)
```

Copy to clipboard

New sub-columns can be added to the `columnDefinition` at any time.
See [Adding columns](https://cratedb.com/docs/crate/reference/en/master/general/ddl/alter-table.html#alter-table-add-column) for details.

##### [Object column policy](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id94) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#object-column-policy "Link to this heading")

###### `STRICT` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#strict "Link to this heading")

If the column policy is configured as `STRICT`, CrateDB will reject any
subcolumn that is not defined upfront by `columnDefinition`.

Example:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     protagonist OBJECT(STRICT) AS (
...         name TEXT
...     )
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     title,
...     protagonist
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "age" = '10'
...     }
... );
SQLParseException[Cannot add column `age` to strict object `protagonist`]
```

Copy to clipboard

The insert above failed because the `age` sub-column is not defined.

Note

Objects with a `STRICT` column policy and no `columnDefinition` will
have one unusable column that will always be `NULL`.

###### `DYNAMIC` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#dynamic "Link to this heading")

If the column policy is configured as `DYNAMIC` (the default), inserts may
dynamically add new subcolumns to the object definition.

Example:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     quotation OBJECT
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

The following statement is equivalent to the above:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     quotation OBJECT(DYNAMIC)
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

The following statement is also equivalent to the above:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     quotation OBJECT(DYNAMIC) AS (
...         words TEXT,
...         length SMALLINT
...     )
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

You can insert using the existing columns:

```
cr> INSERT INTO my_table (
...     title,
...     quotation
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "words" = 'Curiouser and curiouser!',
...         "length" = 3
...     }
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Or you can add new columns:

```
cr> INSERT INTO my_table (
...     title,
...     quotation
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "words" = 'DRINK ME',
...         "length" = 2,
...         "chapter" = 1
...     }
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

All rows have the same columns (including newly added columns), but missing
records will be returned as [NULL](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-null) values:

```
cr> SELECT
...     quotation['chapter'] as chapter,
...     quotation['words'] as quote
... FROM my_table
... ORDER BY chapter ASC;
+---------+--------------------------+
| chapter | quote                    |
+---------+--------------------------+
|       1 | DRINK ME                 |
|    NULL | Curiouser and curiouser! |
+---------+--------------------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

New columns are usable like any other subcolumn. You can retrieve them, sort by
them, and use them in where clauses.

Note

Adding new columns to an object with a `DYNAMIC` policy will affect the
schema of the table.

Once a column is added, it shows up in the `information_schema.columns`
table and its type and attributes are fixed. If a new column `a` was
added with type `INTEGER`, adding strings to the column will result in an
error.

Dynamically added columns will always be analyzed as-is with the
[plain analyzer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/analyzers.html#plain-analyzer), which means the column will be
indexed but not tokenized in the case of `TEXT` columns.

###### `IGNORED` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#ignored "Link to this heading")

If the column policy is configured as `IGNORED`, inserts may dynamically add
new subcolumns to the object definition. However, dynamically added subcolumns
do not cause a schema update and the values contained will not be indexed.

Because dynamically created columns are not recorded in the schema, you can
insert mixed types into them. For example, one row may insert an integer and
the next row may insert an object. Objects with a [STRICT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-strict) or [DYNAMIC](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic)
column policy do not allow this.

Example:

```
cr> CREATE TABLE my_table (
...     title TEXT,
...     protagonist OBJECT(IGNORED) AS (
...         name TEXT,
...         chapter SMALLINT
...     )
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     title,
...     protagonist
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "name" = 'Alice',
...         "chapter" = 1,
...         "size" = {
...             "value" = 10,
...             "units" = 'inches'
...         }
...     }
... );
INSERT OK, 1 row affected  (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table (
...     title,
...     protagonist
... ) VALUES (
...     'Alice in Wonderland',
...     {
...         "name" = 'Alice',
...         "chapter" = 2,
...         "size" = 'As big as a room'
...     }
... );
INSERT OK, 1 row affected  (... sec)
```

Copy to clipboard

```
cr> SELECT
...     protagonist['name'] as name,
...     protagonist['chapter'] as chapter,
...     protagonist['size'] as size
... FROM my_table
... ORDER BY protagonist['chapter'] ASC;
+-------+---------+----------------------------------+
| name  | chapter | size                             |
+-------+---------+----------------------------------+
| Alice |       1 | {"units": "inches", "value": 10} |
| Alice |       2 | As big as a room                 |
+-------+---------+----------------------------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

Reflecting the types of the columns:

```
cr> SELECT
...     pg_typeof(protagonist['name']) as name_type,
...     pg_typeof(protagonist['chapter']) as chapter_type,
...     pg_typeof(protagonist['size']) as size_type
... FROM my_table
... ORDER BY protagonist['chapter'] ASC;
+-----------+--------------+-----------+
| name_type | chapter_type | size_type |
+-----------+--------------+-----------+
| text      | smallint     | undefined |
| text      | smallint     | undefined |
+-----------+--------------+-----------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

Note

Given that dynamically added sub-columns of an `IGNORED` object are not
indexed, filter operations on these columns cannot utilize the index and
instead a value lookup is performed for each matching row. This can be
mitigated by combining a filter using the `AND` clause with other
predicates on indexed columns.

Furthermore, values for dynamically added sub-columns of an `IGNORED`
objects aren’t stored in a column store, which means that ordering on these
columns or using them with aggregates is also slower than using the same
operations on regular columns. For some operations it may also be necessary
to add an explicit type cast because there is no type information available
in the schema.

An example:

```
cr> SELECT
...     protagonist['name'] as name,
...     protagonist['chapter'] as chapter,
...     protagonist['size'] as size
... FROM my_table
... ORDER BY protagonist['size']::TEXT ASC;
+-------+---------+----------------------------------+
| name  | chapter | size                             |
+-------+---------+----------------------------------+
| Alice |       2 | As big as a room                 |
| Alice |       1 | {"units": "inches", "value": 10} |
+-------+---------+----------------------------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

Given that it is possible have values of different types within the same
sub-column of an ignored objects, aggregations may fail at runtime:

```
cr> SELECT protagonist['size']::BIGINT FROM my_table ORDER BY protagonist['chapter'] LIMIT 1;
SQLParseException[Cannot cast value `{value=10, units=inches}` to type `bigint`]
```

Copy to clipboard

##### [Object literals](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id95) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#object-literals "Link to this heading")

You can insert objects using object literals. Object literals are delimited
using curly brackets and key-value pairs are connected via `=`.

Synopsis:

```
{ [ ident = expr [ , ... ] ] }
```

Copy to clipboard

Here, `ident` is the key and `expr` is the value. The key must be a
lowercase column identifier or a quoted mixed-case column identifier. The value
must be a value literal (object literals are permitted and can be nested in
this way).

Empty object literal:

```
{}
```

Copy to clipboard

Boolean type:

```
{ my_bool_column = true }
```

Copy to clipboard

Text type:

```
{ my_str_col = 'this is a text value' }
```

Copy to clipboard

Number types:

```
{ my_int_col = 1234, my_float_col = 5.6 }
```

Copy to clipboard

Array type:

```
{ my_array_column = ['v', 'a', 'l', 'u', 'e'] }
```

Copy to clipboard

Camel case keys must be quoted:

```
{ "CamelCaseColumn" = 'this is a text value' }
```

Copy to clipboard

Nested object:

```
{ nested_obj_colmn = { int_col = 1234, str_col = 'text value' } }
```

Copy to clipboard

You can even specify a [placeholder parameter](https://cratedb.com/docs/crate/reference/en/master/sql/general/value-expressions.html#sql-parameter-reference)
for a value:

```
{ my_other_column = ? }
```

Copy to clipboard

Combined:

```
{ id = 1, name = 'foo', tags = ['apple'], size = 3.1415, valid = ? }
```

Copy to clipboard

Note

Even though they look like JSON, object literals are not JSON. If you want
to use JSON, skip to the next subsection.

See also

[Selecting values from inner objects and nested objects](https://cratedb.com/docs/crate/reference/en/master/general/dql/selects.html#sql-dql-objects)

##### [Inserting objects as JSON](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id96) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#inserting-objects-as-json "Link to this heading")

You can insert objects using JSON strings. To do this, you must [type cast](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-fn) the string to an object with an implicit cast (i.e.,
passing a string into an object column) or an explicit cast (i.e., using the
`::OBJECT` syntax).

Tip

Explicit casts can improve query readability.

Below you will find examples from the previous subsection rewritten to use JSON
strings with explicit casts.

Empty object literal:

```
'{}'::object
```

Copy to clipboard

Boolean type:

```
'{ "my_bool_column": true }'::object
```

Copy to clipboard

Text type:

```
'{ "my_str_col": "this is a text value" }'::object
```

Copy to clipboard

Number types:

```
'{ "my_int_col": 1234, "my_float_col": 5.6 }'::object
```

Copy to clipboard

Array type:

```
'{ "my_array_column": ["v", "a", "l", "u", "e"] }'::object
```

Copy to clipboard

Camel case keys:

```
'{ "CamelCaseColumn": "this is a text value" }'::object
```

Copy to clipboard

Nested object:

```
'{ "nested_obj_col": { "int_col": 1234, "str_col": "foo" } }'::object
```

Copy to clipboard

Note

You cannot use [placeholder parameters](https://cratedb.com/docs/crate/reference/en/master/sql/general/value-expressions.html#sql-parameter-reference)
inside a JSON string.

### [Arrays](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id97) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#arrays "Link to this heading")

#### [`ARRAY`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id98) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#array "Link to this heading")

An array is structured as a collection of other data types.

Arrays can contain the following:

- [Primitive types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-primitive)

- [Objects](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object)

- [Geographic types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo)


Array types are defined as follows:

```
cr> CREATE TABLE my_table_arrays (
...     tags ARRAY(TEXT),
...     objects ARRAY(OBJECT AS (age INTEGER, name TEXT))
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table_arrays (
...     tags,
...     objects
... ) VALUES (
...     ['foo', 'bar'],
...     [{"name" = 'Alice', "age" = 33}, {"name" = 'Bob', "age" = 45}]
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT * FROM my_table_arrays;
+----------------+------------------------------------------------------------+
| tags           | objects                                                    |
+----------------+------------------------------------------------------------+
| ["foo", "bar"] | [{"age": 33, "name": "Alice"}, {"age": 45, "name": "Bob"}] |
+----------------+------------------------------------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

An alternative is the following syntax to refer to arrays:

```
<typeName>[]
```

Copy to clipboard

This means `TEXT[]` is equivalent to `ARRAY(text)`.

Arrays are always represented as zero or more literal elements inside square
brackets (`[]`), for example:

```
[1, 2, 3]
['Zaphod', 'Ford', 'Arthur']
```

Copy to clipboard

##### [Array literals](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id99) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#array-literals "Link to this heading")

Arrays can be written using the array constructor `ARRAY[]` or short `[]`.
The array constructor is an [expression](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression) that accepts
both literals and expressions as its parameters. Parameters may contain zero or
more elements.

Synopsis:

```
[ ARRAY ] '[' element [ , ... ] ']'
```

Copy to clipboard

All array elements must have the same data type, which determines the inner
type of the array. If an array contains no elements, its element type will be
inferred by the context in which it occurs, if possible.

Some valid arrays are:

```
[]
[null]
[1, 2, 3, 4, 5, 6, 7, 8]
['Zaphod', 'Ford', 'Arthur']
[?]
ARRAY[true, false]
ARRAY[column_a, column_b]
ARRAY[ARRAY[1, 2, 1 + 2], ARRAY[3, 4, 3 + 4]]
```

Copy to clipboard

An alternative way to define arrays is to use string literals and casts to
arrays. This requires a string literal that contains the elements separated by
comma and enclosed with curly braces:

```
'{ val1, val2, val3 }'
```

Copy to clipboard

```
cr> SELECT '{ab, CD, "CD", null, "null"}'::ARRAY(TEXT) AS arr;
+----------------------------------+
| arr                              |
+----------------------------------+
| ["ab", "CD", "CD", null, "null"] |
+----------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

`null` elements are interpreted as `null` (none, absent), if you want the
literal `null` string, it has to be enclosed in double quotes.

This variant primarily exists for compatibility with PostgreSQL. The array
constructor syntax explained further above is the preferred way to define
constant array values.

##### [Nested arrays](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id100) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#nested-arrays "Link to this heading")

You can directly define nested arrays in column definitions:

```
CREATE TABLE SensorData (sensorID char(10), readings ARRAY(ARRAY(DOUBLE)));
```

Copy to clipboard

Nested arrays can also be used directly in input and output to UDFs:

```
CREATE FUNCTION sort_nested_array("data" ARRAY(ARRAY(DOUBLE)), sort_dimension SMALLINT)
RETURNS ARRAY(ARRAY(DOUBLE))
LANGUAGE JAVASCRIPT
AS 'function sort_nested_array(data, sort_dimension) {
    data = data.sort(function compareFn(a, b) {
        if (a[sort_dimension] < b[sort_dimension]){return -1;}
        if (a[sort_dimension] > b[sort_dimension]){return 1;}
        return 0;
    });
    return data;
}';
```

Copy to clipboard

Nested arrays can be constructed using `ARRAY_AGG` and accessing them
requires an intermediate cast:

```
CREATE TABLE metrics (ts TIMESTAMP, reading DOUBLE);
INSERT INTO metrics SELECT '2022-11-01',2;
INSERT INTO metrics SELECT '2022-10-01',1;

WITH sorteddata AS (
    SELECT sort_nested_array(ARRAY_AGG([ts,reading]),0) AS nestedarray
    FROM metrics
)
SELECT (nestedarray[generate_series]::ARRAY(DOUBLE))[2] AS "ReadingsSortedByTimestamp"
FROM generate_series(1, 2), sorteddata;

+---------------------------+
| ReadingsSortedByTimestamp |
+---------------------------+
|                       1.0 |
|                       2.0 |
+---------------------------+
```

Copy to clipboard

Note

Accessing nested arrays will generally require loading
sources directly from disk, and will not be very efficient. If you find
yourself using nested arrays frequently, you may want to consider splitting
the data up into multiple tables instead.

Note

Nested arrays cannot be created dynamically, either as a
[top level column](https://cratedb.com/docs/crate/reference/en/master/general/ddl/column-policy.html#column-policy)
or as part of a [dynamic object](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic)

## [`ROW`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id31) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#row "Link to this heading")

A row type is a composite type made up of an arbitrary number of other types,
similar to a `tuple` in programming languages like `python`.

There is currently no type literal to create values of such a type, but the type
is used for the result of table functions used in the select list of a statement
if the table function returns more than one column.

```
cr> SELECT unnest([1, 2], ['Arthur', 'Trillian']);
+-----------------+
| unnest          |
+-----------------+
| [1, "Arthur"]   |
| [2, "Trillian"] |
+-----------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

## [`FLOAT_VECTOR`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id32) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#float-vector "Link to this heading")

A `float_vector` type allows to store dense vectors of float values of fixed
length.

It support [KNN\_MATCH](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-knn-match) for k-nearest neighbour search.
This allows you to find vectors in a dataset which are similar to a query
vector.

The type can’t be used as an element type of a regular array. `float_vector`
values are defined like float arrays.

An example:

```
cr> CREATE TABLE my_vectors (
...     xs FLOAT_VECTOR(2)
... );
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_vectors (xs) VALUES ([3.14, 27.34]);
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Inserting a value with a different dimension than declared in `CREATE TABLE`
results in an error.

```
cr> INSERT INTO my_vectors (xs) VALUES ([3.14, 27.34, 38.4]);
SQLParseException[The number of vector dimensions does not match the field type]
```

Copy to clipboard

```
cr> SELECT * FROM my_vectors;
+---------------+
| xs            |
+---------------+
| [3.14, 27.34] |
+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

## [Geographic types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id33) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geographic-types "Link to this heading")

[Geographic types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo) are types with [nonscalar](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-nonscalar) values representing points or shapes in a 2D world:

### [Geometric points](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id101) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geometric-points "Link to this heading")

#### [`GEO_POINT`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id102) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-point "Link to this heading")

A `GEO_POINT` is a [geographic data type](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo) used to store
latitude and longitude coordinates.

To define a `GEO_POINT` column, use:

```
<columnName> GEO_POINT
```

Copy to clipboard

Values for columns with the `GEO_POINT` type are represented and inserted
using an array of doubles in the following format:

```
[<lon_value>, <lat_value>]
```

Copy to clipboard

Alternatively, a [WKT](https://en.wikipedia.org/wiki/Well-known_text) string can also be used to declare geo points:

```
'POINT ( <lon_value> <lat_value> )'
```

Copy to clipboard

Note

Empty geo points are not supported.

Additionally, if a column is dynamically created, the type detection won’t
recognize neither WKT strings nor double arrays. That means columns of type
`GEO_POINT` must always be declared beforehand.

An example:

```
cr> CREATE TABLE my_table_geo (
...   id INTEGER PRIMARY KEY,
...   pin GEO_POINT
... ) WITH (number_of_replicas = 0)
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

Insert using ARRAY syntax:

```
cr> INSERT INTO my_table_geo (
...     id, pin
... ) VALUES (
...     1, [13.46738, 52.50463]
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Insert using WKT syntax:

```
cr> INSERT INTO my_table_geo (
...     id, pin
... ) VALUES (
...     2, 'POINT (9.7417 47.4108)'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

Query data:

```
cr> SELECT * FROM my_table_geo;
+----+-----------------------------------------+
| id | pin                                     |
+----+-----------------------------------------+
|  1 | [13.467379929497838, 52.50462996773422] |
|  2 | [9.741699993610382, 47.410799972712994] |
+----+-----------------------------------------+
SELECT 2 rows in set (... sec)
```

Copy to clipboard

### [Geometric shapes](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id103) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geometric-shapes "Link to this heading")

#### [`GEO_SHAPE`](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id104) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-shape "Link to this heading")

A `geo_shape` is a [geographic data type](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-geo) used to store
2D shapes defined as [GeoJSON geometry objects](https://datatracker.ietf.org/doc/html/rfc7946).

A `GEO_SHAPE` column can store different kinds of [GeoJSON geometry\\
objects](https://datatracker.ietf.org/doc/html/rfc7946):

- “Point”

- “MultiPoint”

- “LineString”

- “MultiLineString”,

- “Polygon”

- “MultiPolygon”

- “GeometryCollection”


Caution

- 3D coordinates are not supported.

- Empty `Polygon` and `LineString` geo shapes are not supported.


An example:

```
cr> CREATE TABLE my_table_geo (
...   id INTEGER PRIMARY KEY,
...   area GEO_SHAPE
... ) WITH (number_of_replicas = 0)
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table_geo (
...     id, area
... ) VALUES (
...     1, 'POLYGON ((5 5, 10 5, 10 10, 5 10, 5 5))'
... );
INSERT OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> SELECT * FROM my_table_geo;
+----+--------------------------------------------------------------------------------------------------------+
| id | area                                                                                                   |
+----+--------------------------------------------------------------------------------------------------------+
|  1 | {"coordinates": [[[5.0, 5.0], [5.0, 10.0], [10.0, 10.0], [10.0, 5.0], [5.0, 5.0]]], "type": "Polygon"} |
+----+--------------------------------------------------------------------------------------------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

##### [Geo shape column definition](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id105) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-shape-column-definition "Link to this heading")

To define a `GEO_SHAPE` column, use:

```
<columnName> GEO_SHAPE
```

Copy to clipboard

A geographical index with default parameters is created implicitly to allow for
geographical queries. Its default parameters are:

```
<columnName> GEO_SHAPE INDEX USING geohash
    WITH (precision='50m', distance_error_pct=0.025)
```

Copy to clipboard

There are three geographic index types: `geohash` (default), `quadtree` and
`bkdtree`. These indices are only allowed on `geo_shape` columns. For more
information, see [Geo shape index structure](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-geo-shape-index).

Both `geohash` and `quadtree` index types accept the following parameters:

`precision`

(Default: `50m`) Define the maximum precision of the used index and
thus for all indexed shapes. Given as string containing a number and
an optional distance unit (defaults to `m`).

Supported units are `inch` (`in`), `yard` (`yd`), `miles`
(`mi`), `kilometers` (`km`), `meters` (`m`), `centimeters`
(`cm`), `millimeters` (`mm`).

`distance_error_pct`

(Default: `0.025` (2,5%)) The measure of acceptable error for shapes
stored in this column expressed as a percentage value of the shape
size The allowed maximum is `0.5` (50%).

The percentage will be taken from the diagonal distance from the
center of the bounding box enclosing the shape to the closest corner
of the enclosing box. In effect bigger shapes will be indexed with
lower precision than smaller shapes. The ratio of precision loss is
determined by this setting, that means the higher the
`distance_error_pct` the smaller the indexing precision.

This will have the effect of increasing the indexed shape internally,
so e.g. points that are not exactly inside this shape will end up
inside it when it comes to querying as the shape has grown when
indexed.

`tree_levels`

Maximum number of layers to be used by the `PrefixTree` defined by
the index type (either `geohash` or `quadtree`. See
[Geo shape index structure](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-geo-shape-index)).

This can be used to control the precision of the used index. Since
this parameter requires a certain level of understanding of the
underlying implementation, users may use the `precision` parameter
instead. CrateDB uses the `tree_levels` parameter internally and
this is what is returned via the `SHOW CREATE TABLE` statement even
if you use the precision parameter. Defaults to the value which is
`50m` converted to `precision` depending on the index type.

##### [Geo shape index structure](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id106) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-shape-index-structure "Link to this heading")

Computations on very complex polygons and geometry collections are exact but
very expensive. To provide fast queries even on complex shapes, CrateDB uses a
different approach to store, analyze and query geo shapes. The available geo
shape indexing strategies are based on two primary data structures: Prefix and
BKD trees, which are described below.

Prefix Tree

The surface of the earth is represented as a number of grid layers each with
higher precision. While the upper layer has one grid cell, the layer below
contains many cells for the equivalent space.

Each grid cell on each layer is addressed in 2d space either by a [Geohash](https://en.wikipedia.org/wiki/Geohash)
for `geohash` trees or by tightly packed coordinates in a [Quadtree](https://en.wikipedia.org/wiki/Quadtree). Those
addresses conveniently share the same address-prefix between lower layers and
upper layers. So we are able to use a [Trie](https://en.wikipedia.org/wiki/Trie) to represent the grids, and
[Tries](https://en.wikipedia.org/wiki/Trie) can be queried efficiently as their complexity is determined by the
tree depth only.

A geo shape is transformed into these grid cells. Think of this transformation
process as dissecting a vector image into its pixelated counterpart, reasonably
accurately. We end up with multiple images each with a better resolution, up to
the configured precision.

Every grid cell that processed up to the configured precision is stored in an
inverted index, creating a mapping from a grid cell to all shapes that touch
it. This mapping is our geographic index.

The main difference is that the `geohash` supports higher precision than the
`quadtree` tree. Both tree implementations support precision in order of
fractions of millimeters.

BKD-tree

In the BKD-tree-based (`bkdtree`) approach, a geo shape is decomposed into a
collection of triangles. Each triangle is represented as a 7-dimensional point
and stored in this format within a BKD-tree.

To improve the storage efficiency of triangles within an index, the initial four
dimensions are used to represent the bounding box of each triangle. These
bounding boxes are stored in the internal nodes of the BKD-tree, while the
remaining three dimensions are stored in the leaves to enable the reconstruction
of the original triangles.

The BKD-tree-based indexing strategy maintains the original shapes with an
accuracy of 1 cm. Its primary advantage over the Prefix tree approach lies in
its better performance in searching and indexing, coupled with a more efficient
use of storage.

##### [Geo shape literals](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id107) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-shape-literals "Link to this heading")

Columns with the `GEO_SHAPE` type are represented and inserted as an object
containing a valid [GeoJSON](https://geojson.org/) geometry object:

```
{
    type = 'Polygon',
    coordinates = [\
        [\
            [100.0, 0.0],\
            [101.0, 0.0],\
            [101.0, 1.0],\
            [100.0, 1.0],\
            [100.0, 0.0]\
        ]\
    ]
}
```

Copy to clipboard

Alternatively a [WKT](https://en.wikipedia.org/wiki/Well-known_text) string can be used to represent a `GEO_SHAPE` as
well:

```
'POLYGON ((5 5, 10 5, 10 10, 5 10, 5 5))'
```

Copy to clipboard

Note

It is not possible to detect a `GEO_SHAPE` type for a dynamically created
column. Like with [GEO\_POINT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-geo-point) type, `GEO_SHAPE` columns need to
be created explicitly using either [CREATE TABLE](https://cratedb.com/docs/crate/reference/en/master/sql/statements/create-table.html#sql-create-table) or
[ALTER TABLE](https://cratedb.com/docs/crate/reference/en/master/sql/statements/alter-table.html#sql-alter-table).

##### [Geo shape GeoJSON examples](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id108) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#geo-shape-geojson-examples "Link to this heading")

Those are examples showing how to insert all possible kinds of GeoJSON types
using [WKT](https://en.wikipedia.org/wiki/Well-known_text) syntax.

```
cr> CREATE TABLE my_table_geo (
...   id INTEGER PRIMARY KEY,
...   area GEO_SHAPE
... ) WITH (number_of_replicas = 0)
CREATE OK, 1 row affected (... sec)
```

Copy to clipboard

```
cr> INSERT INTO my_table_geo (
...     id, area
... ) VALUES
...     (1, 'POINT (9.7417 47.4108)'),
...     (2, 'MULTIPOINT (47.4108 9.7417, 9.7483 47.4106)'),
...     (3, 'LINESTRING (47.4108 9.7417, 9.7483 47.4106)'),
...     (4, 'MULTILINESTRING ((47.4108 9.7417, 9.7483 47.4106), (52.50463 13.46738, 52.51000 13.47000))'),
...     (5, 'POLYGON ((47.4108 9.7417, 9.7483 47.4106, 9.7426 47.4142, 47.4108 9.7417))'),
...     (6, 'MULTIPOLYGON (((5 5, 10 5, 10 10, 5 5)), ((6 6, 10 5, 10 10, 6 6)))'),
...     (7, 'GEOMETRYCOLLECTION (POINT (9.7417 47.4108), MULTIPOINT (47.4108 9.7417, 9.7483 47.4106))')
... ;
INSERT OK, 7 rows affected (... sec)
```

Copy to clipboard

```
cr> SELECT * FROM my_table_geo ORDER BY id;
+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id | area                                                                                                                                                                               |
+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  1 | {"coordinates": [9.7417, 47.4108], "type": "Point"}                                                                                                                                |
|  2 | {"coordinates": [[47.4108, 9.7417], [9.7483, 47.4106]], "type": "MultiPoint"}                                                                                                      |
|  3 | {"coordinates": [[47.4108, 9.7417], [9.7483, 47.4106]], "type": "LineString"}                                                                                                      |
|  4 | {"coordinates": [[[47.4108, 9.7417], [9.7483, 47.4106]], [[52.50463, 13.46738], [52.51, 13.47]]], "type": "MultiLineString"}                                                       |
|  5 | {"coordinates": [[[47.4108, 9.7417], [9.7483, 47.4106], [9.7426, 47.4142], [47.4108, 9.7417]]], "type": "Polygon"}                                                                 |
|  6 | {"coordinates": [[[[5.0, 5.0], [10.0, 5.0], [10.0, 10.0], [5.0, 5.0]]], [[[6.0, 6.0], [10.0, 5.0], [10.0, 10.0], [6.0, 6.0]]]], "type": "MultiPolygon"}                            |
|  7 | {"geometries": [{"coordinates": [9.7417, 47.4108], "type": "Point"}, {"coordinates": [[47.4108, 9.7417], [9.7483, 47.4106]], "type": "MultiPoint"}], "type": "GeometryCollection"} |
+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
SELECT 7 rows in set (... sec)
```

Copy to clipboard

## [Type casting](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id36) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#type-casting "Link to this heading")

A type `CAST` specifies a conversion from one data type to another. It will
only succeed if the value of the [expression](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression) is
convertible to the desired data type, otherwise an error is returned.

CrateDB supports two equivalent syntaxes for type casts:

```
CAST(expression AS TYPE)
expression::TYPE
```

Copy to clipboard

### [Cast expressions](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id109) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast-expressions "Link to this heading")

```
CAST(expression AS TYPE)
expression::TYPE
```

Copy to clipboard

### [Cast functions](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id110) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast-functions "Link to this heading")

#### `CAST` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast "Link to this heading")

Example usages:

```
cr> SELECT CAST(port['http'] AS BOOLEAN) AS col FROM sys.nodes LIMIT 1;
+------+
| col  |
+------+
| TRUE |
+------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

```
cr> SELECT (2+10)/2::TEXT AS col;
+-----+
| col |
+-----+
|   6 |
+-----+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### `CAST to ARRAY` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast-to-array "Link to this heading")

It is possible to convert array structures to different data types, e.g.
converting an array of integer values to a boolean array.

```
cr> SELECT CAST([0,1,5] AS ARRAY(BOOLEAN)) AS active_threads ;
+---------------------+
| active_threads      |
+---------------------+
| [false, true, true] |
+---------------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

#### `CAST to OBJECT` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast-to-object "Link to this heading")

The following data types can be converted to an [OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object) type:

- any [CHARACTER](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-character-data) type if it is a valid
[JSON](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-type-json) string.

- [GEO\_SHAPE](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-geo-shape)

- [OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object)


When casting from an object to an object (or array of objects), the resulting
object type will contain all inner types from both types if the target
[column policy](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-column-policy) is not set to
[STRICT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-strict). If both types contain the same inner key,
the target inner type definition will be used. Additionally, the resulting
[column policy](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-column-policy) is taken from the target type.

The availability of the inner types in the resulting object type is important
when trying to access the keys of an object. The following examples will
demonstrate how the object type merges and policy will affect a subscript
expression on the resulting object type.

By default, the target type policy is set to [DYNAMIC](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-dynamic),
such selecting any type not contained in the source expression type will lead
to an error if [error\_on\_unknown\_object\_key](https://cratedb.com/docs/crate/reference/en/master/config/session.html#conf-session-error-on-unknown-object-key) is true.

```
cr> SELECT person['name'], person['age'] FROM (SELECT {name = 'Alice'}::OBJECT AS person) t;
ColumnUnknownException[Column person['age'] unknown]
```

Copy to clipboard

When defining additional inner types in the target object type, these keys can
be queried even that they do not exist in the source object type or value.

```
cr> SELECT person['name'], person['age'] FROM (SELECT {name = 'Alice'}::OBJECT AS(age INT) AS person) t;
+----------------+---------------+
| person['name'] | person['age'] |
+----------------+---------------+
| Alice          | NULL          |
+----------------+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

If the the target type policy is changed to [STRICT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-strict),
selecting any key not defined at the target type will lead to an error.

```
cr> SELECT person['name'], person['age'] FROM (SELECT {name = 'Alice'}::OBJECT(STRICT) AS(age INT) AS person) t;
ColumnUnknownException[Column person['name'] unknown]
```

Copy to clipboard

In contrast, changing the target type policy to
[IGNORED](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object-columns-ignored) will allow selecting any key from the object,
even if it is not defined in the target type.

```
cr> SELECT person['name'], person['age'] FROM (SELECT {name = 'Alice'}::OBJECT(IGNORED) AS person) t;
+----------------+---------------+
| person['name'] | person['age'] |
+----------------+---------------+
| Alice          | NULL          |
+----------------+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Note

When the source type is not an [OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object) type, or it does
not contain any inner type definition and the target
[OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object) type does not as well, the resulting
[OBJECT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-object) is always untyped and a query on any object
property will return an `UNDEFINED` type as the value type is not known
until the expression gets evaluated. This is important when using the
resulting symbol as an argument to any other expression.

#### `TRY_CAST` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#try-cast "Link to this heading")

While [CAST](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#fn-cast) throws an error for incompatible type casts,
`TRY_CAST` returns `null` in this case. Otherwise the result and behaviour
is the same as with [CAST](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#fn-cast).

```
TRY_CAST(expression AS TYPE)
```

Copy to clipboard

Example usages:

```
cr> SELECT TRY_CAST('true' AS BOOLEAN) AS col;
+------+
| col  |
+------+
| TRUE |
+------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Trying to cast a `TEXT` to `INTEGER`, will fail with `CAST` if
`TEXT` is no valid integer but return `null` with `TRY_CAST`:

```
cr> SELECT TRY_CAST(name AS INTEGER) AS name_as_int FROM sys.nodes LIMIT 1;
+-------------+
| name_as_int |
+-------------+
|        NULL |
+-------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

### [Cast from string literals](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id111) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#cast-from-string-literals "Link to this heading")

This cast operation is applied to a string literal and it effectively
initializes a constant of an arbitrary type.

Example usages, initializing an `INTEGER` and a `TIMESTAMP` constant:

```
cr> SELECT INTEGER '25' AS int;
+-----+
| int |
+-----+
|  25 |
+-----+
SELECT 1 row in set (... sec)
```

Copy to clipboard

```
cr> SELECT TIMESTAMP WITH TIME ZONE '2029-12-12T11:44:00.24446' AS ts;
+---------------+
| ts            |
+---------------+
| 1891770240244 |
+---------------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

Note

This cast operation is limited to [primitive data types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-primitive) only. For complex types such as `ARRAY` or
`OBJECT`, use the [Cast functions](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting-fn) syntax.

## [PostgreSQL compatibility](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id40) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#postgresql-compatibility "Link to this heading")

### [Type aliases](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id112) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#type-aliases "Link to this heading")

For compatibility with PostgreSQL we include some type aliases which can be
used instead of the CrateDB specific type names.

For example, in a type cast:

```
cr> SELECT 10::INT2 AS INT2;
+------+
| int2 |
+------+
|   10 |
+------+
SELECT 1 row in set (... sec)
```

Copy to clipboard

See the table below for a full list of aliases:

| Alias | CrateDB Type |
| --- | --- |
| `SHORT` | `SMALLINT` |
| `INT` | `INTEGER` |
| `INT2` | `SMALLINT` |
| `INT4` | `INTEGER` |
| `INT8` | `BIGINT` |
| `LONG` | `BIGINT` |
| `STRING` | `TEXT` |
| `VARCHAR` | `TEXT` |
| `CHARACTER VARYING` | `TEXT` |
| `NAME` | `TEXT` |
| `REGPROC` | `TEXT` |
| `"CHAR"` | `BYTE` |
| `FLOAT` | `REAL` |
| `FLOAT4` | `REAL` |
| `FLOAT8` | `DOUBLE PRECISION` |
| `DOUBLE` | `DOUBLE PRECISION` |
| `DECIMAL` | `NUMERIC` |
| `TIMESTAMP` | `TIMESTAMP WITHOUT TIME ZONE` |
| `TIMESTAMPTZ` | `TIMESTAMP WITH TIME ZONE` |

Note

The [PG\_TYPEOF](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-pg-typeof) system [function](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-function) can be used to resolve the data type of any
[expression](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression).

### [Internal-use types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#id113) [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#internal-use-types "Link to this heading")

#### `"CHAR"` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#char "Link to this heading")

A one-byte character used internally for enumeration items in the
[PostgreSQL system catalogs](https://cratedb.com/docs/crate/reference/en/master/interfaces/postgres.html#postgres-pg-catalog).

Specified as a signed integer in the range -128 to 127.

#### `OID` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#oid "Link to this heading")

An _Object Identifier_ (OID). OIDS are used internally as primary keys in the
[PostgreSQL system catalogs](https://cratedb.com/docs/crate/reference/en/master/interfaces/postgres.html#postgres-pg-catalog).

The `OID` type is mapped to the [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) data type.

#### `REGPROC` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#regproc "Link to this heading")

An alias for the [oid](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-oid) type.

The `REGPROC` type is used by tables in the [pg\_catalog](https://cratedb.com/docs/crate/reference/en/master/interfaces/postgres.html#postgres-pg-catalog)
schema to reference functions in the [pg\_proc](https://www.postgresql.org/docs/14/catalog-pg-proc.html) table.

[Casting](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting) a `REGPROC` type to a [TEXT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text) or
[integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) type will result in the corresponding
function name or `oid` value, respectively.

#### `REGCLASS` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#regclass "Link to this heading")

An alias for the [oid](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-oid) type.

The `REGCLASS` type is used by tables in the [pg\_catalog](https://cratedb.com/docs/crate/reference/en/master/interfaces/postgres.html#postgres-pg-catalog)
schema to reference relations in the [pg\_class](https://www.postgresql.org/docs/14/catalog-pg-class.html) table.

[Casting](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-casting) a `REGCLASS` type to a
[TEXT](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-text) or [integer](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-numeric) type will result
in the corresponding relation name or `oid` value, respectively.

Note

String values casted to the `REGCLASS` type must match a valid relation
name identifier, see also
[identifier naming restrictions](https://cratedb.com/docs/crate/reference/en/master/general/ddl/create-table.html#ddl-create-table-naming).
The given relation name won’t be validated against existing relations.

#### `OIDVECTOR` [¶](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html\#oidvector "Link to this heading")

The `OIDVECTOR` type is used to represent one or more [oid](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-oid)
values.

This type is similar to an [array](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#data-types-arrays) of integers.
However, you cannot use it with any [scalar functions](https://cratedb.com/docs/crate/reference/en/master/general/builtins/scalar-functions.html#scalar-functions) or [expressions](https://cratedb.com/docs/crate/reference/en/master/appendices/glossary.html#gloss-expression).

See also

[PostgreSQL: Object Identifier (OID) types](https://cratedb.com/docs/crate/reference/en/master/general/ddl/data-types.html#type-oid)