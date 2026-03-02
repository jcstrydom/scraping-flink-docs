[Skip to content](https://trino.io/docs/current/language/types.html#language/types)

# Data types [\#](https://trino.io/docs/current/language/types.html\#language-types--page-root "Link to this heading")

Trino has a set of built-in data types, described below. Additional types can be
[provided by plugins](https://trino.io/docs/current/develop/types.html).

## Trino type support and mapping [\#](https://trino.io/docs/current/language/types.html\#trino-type-support-and-mapping "Link to this heading")

Connectors to data sources are not required to support all Trino data types
described on this page. If there are data types similar to Trino’s that are used
on the data source, the connector may map the Trino and remote data types to
each other as needed.

Depending on the connector and the data source, type mapping may apply
in either direction as follows:

- **Data source to Trino** mapping applies to any operation where columns in the
data source are read by Trino, such as a [SELECT](https://trino.io/docs/current/sql/select.html) statement, and the
underlying source data type needs to be represented by a Trino data type.

- **Trino to data source** mapping applies to any operation where the columns
or expressions in Trino need to be translated into data types or expressions
compatible with the underlying data source. For example,
[CREATE TABLE AS](https://trino.io/docs/current/sql/create-table-as.html) statements specify Trino types that are then
mapped to types on the remote data source. Predicates like `WHERE` also use
these mappings in order to ensure that the predicate is translated to valid
syntax on the remote data source.


Data type support and mappings vary depending on the connector. Refer to the
[connector documentation](https://trino.io/docs/current/connector.html) for more information.

## Boolean [\#](https://trino.io/docs/current/language/types.html\#boolean "Link to this heading")

### `BOOLEAN` [\#](https://trino.io/docs/current/language/types.html\#id1 "Link to this heading")

This type captures boolean values `true` and `false`.

## Integer [\#](https://trino.io/docs/current/language/types.html\#integer "Link to this heading")

Integer numbers can be expressed as numeric literals in the following formats:

- Decimal integer. Examples are `-7`, `0`, or `3`.

- Hexadecimal integer composed of `0X` or `0x` and the value. Examples are
`0x0A` for decimal `10` or `0x11` for decimal `17`.

- Octal integer composed of `0O` or `0o` and the value. Examples are `0o40` for
decimal `32` or `0o11` for decimal `9`.

- Binary integer composed of `0B` or `0b` and the value. Examples are `0b1001`
for decimal `9` or `0b101010` for decimal \`42\`\`.


Underscore characters are ignored within literal values, and can be used to
increase readability. For example, decimal integer `123_456` is equivalent to
`123456`. Preceding underscores, trailing underscores, and consecutive underscores
are not permitted.

Integers are supported by the following data types.

### `TINYINT` [\#](https://trino.io/docs/current/language/types.html\#tinyint "Link to this heading")

A 8-bit signed two’s complement integer with a minimum value of
`-2^7` or `-0x80` and a maximum value of `2^7 - 1` or `0x7F`.

### `SMALLINT` [\#](https://trino.io/docs/current/language/types.html\#smallint "Link to this heading")

A 16-bit signed two’s complement integer with a minimum value of
`-2^15` or `-0x8000` and a maximum value of `2^15 - 1` or `0x7FFF`.

### `INTEGER` or `INT` [\#](https://trino.io/docs/current/language/types.html\#integer-or-int "Link to this heading")

A 32-bit signed two’s complement integer with a minimum value of `-2^31` or
`-0x80000000` and a maximum value of `2^31 - 1` or `0x7FFFFFFF`. The names
`INTEGER` and `INT` can both be used for this type.

### `BIGINT` [\#](https://trino.io/docs/current/language/types.html\#bigint "Link to this heading")

A 64-bit signed two’s complement integer with a minimum value of `-2^63` or
`-0x8000000000000000` and a maximum value of `2^63 - 1` or `0x7FFFFFFFFFFFFFFF`.

## Floating-point [\#](https://trino.io/docs/current/language/types.html\#floating-point "Link to this heading")

Floating-point, fixed-precision numbers can be expressed as numeric literal
using scientific notation such as `1.03e1` and are cast as `DOUBLE` data type.
Underscore characters are ignored within literal values, and can be used to
increase readability. For example, value `123_456.789e4` is equivalent to
`123456.789e4`. Preceding underscores, trailing underscores, consecutive
underscores, and underscores beside the comma (`.`) are not permitted.

### `REAL` [\#](https://trino.io/docs/current/language/types.html\#real "Link to this heading")

A real is a 32-bit inexact, variable-precision implementing the
IEEE Standard 754 for Binary Floating-Point Arithmetic.

Example literals: `REAL '10.3'`, `REAL '10.3e0'`, `REAL '1.03e1'`

### `DOUBLE` [\#](https://trino.io/docs/current/language/types.html\#double "Link to this heading")

A double is a 64-bit inexact, variable-precision implementing the
IEEE Standard 754 for Binary Floating-Point Arithmetic.

Example literals: `DOUBLE '10.3'`, `DOUBLE '1.03e1'`, `10.3e0`, `1.03e1`

## Exact numeric [\#](https://trino.io/docs/current/language/types.html\#exact-numeric "Link to this heading")

Exact numeric values can be expressed as numeric literals such as `1.1`, and
are supported by the `DECIMAL` data type.

Underscore characters are ignored within literal values, and can be used to
increase readability. For example, decimal `123_456.789_123` is equivalent to
`123456.789123`. Preceding underscores, trailing underscores, consecutive
underscores, and underscores beside the comma (`.`) are not permitted.

Leading zeros in literal values are permitted and ignored. For example,
`000123.456` is equivalent to `123.456`.

### `DECIMAL` [\#](https://trino.io/docs/current/language/types.html\#decimal "Link to this heading")

A exact decimal number. Precision up to 38 digits is supported but performance
is best up to 18 digits.

The decimal type takes two literal parameters:

- **precision** \- total number of digits

- **scale** \- number of digits in fractional part. Scale is optional and defaults to 0.


Example type definitions: `DECIMAL(10,3)`, `DECIMAL(20)`

Example literals: `DECIMAL '10.3'`, `DECIMAL '1234567890'`, `1.1`

## String [\#](https://trino.io/docs/current/language/types.html\#string "Link to this heading")

### `VARCHAR` [\#](https://trino.io/docs/current/language/types.html\#varchar "Link to this heading")

Variable length character data with an optional maximum length.

Example type definitions: `varchar`, `varchar(20)`

SQL statements support simple literal, as well as Unicode usage:

- literal string : `'Hello winter !'`

- Unicode string with default escape character: `U&'Hello winter \2603 !'`

- Unicode string with custom escape character: `U&'Hello winter #2603 !' UESCAPE '#'`


A Unicode string is prefixed with `U&` and requires an escape character
before any Unicode character usage with 4 digits. In the examples above
`\2603` and `#2603` represent a snowman character. Long Unicode codes
with 6 digits require usage of the plus symbol before the code. For example,
you need to use `\+01F600` for a grinning face emoji.

Single quotes in string literals can be escaped by using another single quote:
`'I am big, it''s the pictures that got small!'`

### `CHAR` [\#](https://trino.io/docs/current/language/types.html\#char "Link to this heading")

Fixed length character data. A `CHAR` type without length specified has a
default length of 1. A `CHAR(x)` value always has a fixed length of `x`
characters. For example, casting `dog` to `CHAR(7)` adds four implicit trailing
spaces.

As with `VARCHAR`, a single quote in a `CHAR` literal can be escaped with
another single quote:

```
SELECT CHAR 'All right, Mr. DeMille, I''m ready for my close-up.'
```

Copy to clipboard

Example type definitions: `char`, `char(20)`

### `VARBINARY` [\#](https://trino.io/docs/current/language/types.html\#varbinary "Link to this heading")

Variable length binary data.

SQL statements support usage of binary literal data with the prefix `X` or `x`.
The binary data has to use hexadecimal format. For example, the binary form of
`eh?` is `X'65683F'` as you can confirm with the following statement:

```
SELECT from_utf8(x'65683F');
```

Copy to clipboard

Binary literals ignore any whitespace characters. For example, the literal
`X'FFFF 0FFF  3FFF FFFF'` is equivalent to `X'FFFF0FFF3FFFFFFF'`.

Note

Binary strings with length are not yet supported: `varbinary(n)`

### `JSON` [\#](https://trino.io/docs/current/language/types.html\#json "Link to this heading")

JSON value type, which can be a JSON object, a JSON array, a JSON number, a JSON string,
`true`, `false` or `null`.

## Date and time [\#](https://trino.io/docs/current/language/types.html\#date-and-time "Link to this heading")

See also [Date and time functions and operators](https://trino.io/docs/current/functions/datetime.html)

### `DATE` [\#](https://trino.io/docs/current/language/types.html\#date "Link to this heading")

Calendar date (year, month, day).

Example: `DATE '2001-08-22'`

### `TIME` [\#](https://trino.io/docs/current/language/types.html\#time "Link to this heading")

`TIME` is an alias for `TIME(3)` (millisecond precision).

### `TIME(P)` [\#](https://trino.io/docs/current/language/types.html\#time-p "Link to this heading")

Time of day (hour, minute, second) without a time zone with `P` digits of precision
for the fraction of seconds. A precision of up to 12 (picoseconds) is supported.

Example: `TIME '01:02:03.456'`

### `TIME WITH TIME ZONE` [\#](https://trino.io/docs/current/language/types.html\#time-with-time-zone "Link to this heading")

Time of day (hour, minute, second, millisecond) with a time zone.
Values of this type are rendered using the time zone from the value.
Time zones are expressed as the numeric UTC offset value:

```
SELECT TIME '01:02:03.456 -08:00';
-- 1:02:03.456-08:00
```

Copy to clipboard

### `TIMESTAMP` [\#](https://trino.io/docs/current/language/types.html\#timestamp "Link to this heading")

`TIMESTAMP` is an alias for `TIMESTAMP(3)` (millisecond precision).

### `TIMESTAMP(P)` [\#](https://trino.io/docs/current/language/types.html\#timestamp-p "Link to this heading")

Calendar date and time of day without a time zone with `P` digits of precision
for the fraction of seconds. A precision of up to 12 (picoseconds) is supported.
This type is effectively a combination of the `DATE` and `TIME(P)` types.

`TIMESTAMP(P) WITHOUT TIME ZONE` is an equivalent name.

Timestamp values can be constructed with the `TIMESTAMP` literal
expression. Alternatively, language constructs such as
`localtimestamp(p)`, or a number of [date and time functions and operators](https://trino.io/docs/current/functions/datetime.html) can return timestamp values.

Casting to lower precision causes the value to be rounded, and not
truncated. Casting to higher precision appends zeros for the additional
digits.

The following examples illustrate the behavior:

```
SELECT TIMESTAMP '2020-06-10 15:55:23';
-- 2020-06-10 15:55:23

SELECT TIMESTAMP '2020-06-10 15:55:23.383345';
-- 2020-06-10 15:55:23.383345

SELECT typeof(TIMESTAMP '2020-06-10 15:55:23.383345');
-- timestamp(6)

SELECT cast(TIMESTAMP '2020-06-10 15:55:23.383345' as TIMESTAMP(1));
 -- 2020-06-10 15:55:23.4

SELECT cast(TIMESTAMP '2020-06-10 15:55:23.383345' as TIMESTAMP(12));
-- 2020-06-10 15:55:23.383345000000
```

Copy to clipboard

### `TIMESTAMP WITH TIME ZONE` [\#](https://trino.io/docs/current/language/types.html\#timestamp-with-time-zone "Link to this heading")

`TIMESTAMP WITH TIME ZONE` is an alias for `TIMESTAMP(3) WITH TIME ZONE`
(millisecond precision).

### `TIMESTAMP(P) WITH TIME ZONE` [\#](https://trino.io/docs/current/language/types.html\#timestamp-p-with-time-zone "Link to this heading")

Instant in time that includes the date and time of day with `P` digits of
precision for the fraction of seconds and with a time zone. Values of this type
are rendered using the time zone from the value. Time zones can be expressed in
the following ways:

- `UTC`, with `GMT`, `Z`, or `UT` usable as aliases for UTC.

- `+hh:mm` or `-hh:mm` with `hh:mm` as an hour and minute offset from UTC.
Can be written with or without `UTC`, `GMT`, or `UT` as an alias for
UTC.

- An [IANA time zone name](https://www.iana.org/time-zones).


The following examples demonstrate some of these syntax options:

```
SELECT TIMESTAMP '2001-08-22 03:04:05.321 UTC';
-- 2001-08-22 03:04:05.321 UTC

SELECT TIMESTAMP '2001-08-22 03:04:05.321 -08:30';
-- 2001-08-22 03:04:05.321 -08:30

SELECT TIMESTAMP '2001-08-22 03:04:05.321 GMT-08:30';
-- 2001-08-22 03:04:05.321 -08:30

SELECT TIMESTAMP '2001-08-22 03:04:05.321 America/New_York';
-- 2001-08-22 03:04:05.321 America/New_York
```

Copy to clipboard

### `INTERVAL YEAR TO MONTH` [\#](https://trino.io/docs/current/language/types.html\#interval-year-to-month "Link to this heading")

Span of years and months.

Example: `INTERVAL '3' MONTH`

### `INTERVAL DAY TO SECOND` [\#](https://trino.io/docs/current/language/types.html\#interval-day-to-second "Link to this heading")

Span of days, hours, minutes, seconds and milliseconds.

Example: `INTERVAL '2' DAY`

## Structural [\#](https://trino.io/docs/current/language/types.html\#structural "Link to this heading")

### `ARRAY` [\#](https://trino.io/docs/current/language/types.html\#array "Link to this heading")

An array of the given component type.

Example: `ARRAY[1, 2, 3]`

More information in [Array functions and operators](https://trino.io/docs/current/functions/array.html).

### `MAP` [\#](https://trino.io/docs/current/language/types.html\#map "Link to this heading")

A map between the given component types. A map is a collection of key-value
pairs, where each key is associated with a single value. Map keys are required,
while map values can be null.

Example: `MAP(ARRAY['foo', 'bar'], ARRAY[1, 2])`

More information in [Map functions and operators](https://trino.io/docs/current/functions/map.html).

### `ROW` [\#](https://trino.io/docs/current/language/types.html\#row "Link to this heading")

A structure made up of fields that allows mixed types.
The fields may be of any SQL type.

By default, row fields are not named, but names can be assigned.

Example: `CAST(ROW(1, 2e0) AS ROW(x BIGINT, y DOUBLE))`

Named row fields are accessed with field reference operator (`.`).

Example: `CAST(ROW(1, 2.0) AS ROW(x BIGINT, y DOUBLE)).x`

Named or unnamed row fields are accessed by position with the subscript
operator (`[]`). The position starts at `1` and must be a constant.

Example: `ROW(1, 2.0)[1]`

## Network address [\#](https://trino.io/docs/current/language/types.html\#network-address "Link to this heading")

### `IPADDRESS` [\#](https://trino.io/docs/current/language/types.html\#ipaddress "Link to this heading")

An IP address that can represent either an IPv4 or IPv6 address. Internally,
the type is a pure IPv6 address. Support for IPv4 is handled using the
_IPv4-mapped IPv6 address_ range ( [**RFC 4291#section-2.5.5.2**](https://datatracker.ietf.org/doc/html/rfc4291.html#section-2.5.5.2)).
When creating an `IPADDRESS`, IPv4 addresses will be mapped into that range.
When formatting an `IPADDRESS`, any address within the mapped range will
be formatted as an IPv4 address. Other addresses will be formatted as IPv6
using the canonical format defined in [**RFC 5952**](https://datatracker.ietf.org/doc/html/rfc5952.html).

Examples: `IPADDRESS '10.0.0.1'`, `IPADDRESS '2001:db8::1'`

## UUID [\#](https://trino.io/docs/current/language/types.html\#uuid "Link to this heading")

### `UUID` [\#](https://trino.io/docs/current/language/types.html\#uuid-type "Link to this heading")

This type represents a UUID (Universally Unique IDentifier), also known as a
GUID (Globally Unique IDentifier), using the format defined in [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html).

Example: `UUID '12151fd2-7586-11e9-8f9e-2a86e4085a59'`

## HyperLogLog [\#](https://trino.io/docs/current/language/types.html\#hyperloglog "Link to this heading")

Calculating the approximate distinct count can be done much more cheaply than an exact count using the
[HyperLogLog](https://wikipedia.org/wiki/HyperLogLog) data sketch. See [HyperLogLog functions](https://trino.io/docs/current/functions/hyperloglog.html).

### `HyperLogLog` [\#](https://trino.io/docs/current/language/types.html\#hyperloglog-type "Link to this heading")

A HyperLogLog sketch allows efficient computation of [`approx_distinct()`](https://trino.io/docs/current/functions/aggregate.html#approx_distinct "approx_distinct"). It starts as a
sparse representation, switching to a dense representation when it becomes more efficient.

### `P4HyperLogLog` [\#](https://trino.io/docs/current/language/types.html\#p4hyperloglog "Link to this heading")

A P4HyperLogLog sketch is similar to [HyperLogLog](https://trino.io/docs/current/language/types.html#hyperloglog-type), but it starts (and remains)
in the dense representation.

## SetDigest [\#](https://trino.io/docs/current/language/types.html\#setdigest "Link to this heading")

### `SetDigest` [\#](https://trino.io/docs/current/language/types.html\#setdigest-type "Link to this heading")

A SetDigest (setdigest) is a data sketch structure used
in calculating [Jaccard similarity coefficient](https://wikipedia.org/wiki/Jaccard_index)
between two sets.

SetDigest encapsulates the following components:

- [HyperLogLog](https://wikipedia.org/wiki/HyperLogLog)

- [MinHash with a single hash function](https://wikipedia.org/wiki/MinHash#Variant_with_a_single_hash_function)


The HyperLogLog structure is used for the approximation of the distinct elements
in the original set.

The MinHash structure is used to store a low memory footprint signature of the original set.
The similarity of any two sets is estimated by comparing their signatures.

SetDigests are additive, meaning they can be merged together.

## Quantile digest [\#](https://trino.io/docs/current/language/types.html\#quantile-digest "Link to this heading")

### `QDigest` [\#](https://trino.io/docs/current/language/types.html\#qdigest "Link to this heading")

A quantile digest (qdigest) is a summary structure which captures the approximate
distribution of data for a given input set, and can be queried to retrieve approximate
quantile values from the distribution. The level of accuracy for a qdigest
is tunable, allowing for more precise results at the expense of space.

A qdigest can be used to give approximate answer to queries asking for what value
belongs at a certain quantile. A useful property of qdigests is that they are
additive, meaning they can be merged together without losing precision.

A qdigest may be helpful whenever the partial results of `approx_percentile`
can be reused. For example, one may be interested in a daily reading of the 99th
percentile values that are read over the course of a week. Instead of calculating
the past week of data with `approx_percentile`, `qdigest`s could be stored
daily, and quickly merged to retrieve the 99th percentile value.

## T-Digest [\#](https://trino.io/docs/current/language/types.html\#t-digest "Link to this heading")

### `TDigest` [\#](https://trino.io/docs/current/language/types.html\#tdigest "Link to this heading")

A T-digest (tdigest) is a summary structure which, similarly to qdigest, captures the
approximate distribution of data for a given input set. It can be queried to retrieve
approximate quantile values from the distribution.

TDigest has the following advantages compared to QDigest:

- higher performance

- lower memory usage

- higher accuracy at high and low percentiles


T-digests are additive, meaning they can be merged together.