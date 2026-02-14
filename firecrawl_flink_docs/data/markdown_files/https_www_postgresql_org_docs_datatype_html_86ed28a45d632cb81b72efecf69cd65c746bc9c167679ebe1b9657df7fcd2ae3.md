November 13, 2025: [PostgreSQL 18.1, 17.7, 16.11, 15.15, 14.20, and 13.23 Released!](https://www.postgresql.org/about/news/postgresql-181-177-1611-1515-1420-and-1323-released-3171/)

[Documentation](https://www.postgresql.org/docs/ "Documentation") → [PostgreSQL 12](https://www.postgresql.org/docs/12/index.html)

Supported Versions:



[Current](https://www.postgresql.org/docs/current/datatype.html "PostgreSQL 18 - Chapter 8. Data Types")
( [18](https://www.postgresql.org/docs/18/datatype.html "PostgreSQL 18 - Chapter 8. Data Types"))


/

[17](https://www.postgresql.org/docs/17/datatype.html "PostgreSQL 17 - Chapter 8. Data Types")


/

[16](https://www.postgresql.org/docs/16/datatype.html "PostgreSQL 16 - Chapter 8. Data Types")


/

[15](https://www.postgresql.org/docs/15/datatype.html "PostgreSQL 15 - Chapter 8. Data Types")


/

[14](https://www.postgresql.org/docs/14/datatype.html "PostgreSQL 14 - Chapter 8. Data Types")

Development Versions:


[devel](https://www.postgresql.org/docs/devel/datatype.html "PostgreSQL devel - Chapter 8. Data Types")

Unsupported versions:


[13](https://www.postgresql.org/docs/13/datatype.html "PostgreSQL 13 - Chapter 8. Data Types")

/
[12](https://www.postgresql.org/docs/12/datatype.html "PostgreSQL 12 - Chapter 8. Data Types")

/
[11](https://www.postgresql.org/docs/11/datatype.html "PostgreSQL 11 - Chapter 8. Data Types")

/
[10](https://www.postgresql.org/docs/10/datatype.html "PostgreSQL 10 - Chapter 8. Data Types")

/
[9.6](https://www.postgresql.org/docs/9.6/datatype.html "PostgreSQL 9.6 - Chapter 8. Data Types")

/
[9.5](https://www.postgresql.org/docs/9.5/datatype.html "PostgreSQL 9.5 - Chapter 8. Data Types")

/
[9.4](https://www.postgresql.org/docs/9.4/datatype.html "PostgreSQL 9.4 - Chapter 8. Data Types")

/
[9.3](https://www.postgresql.org/docs/9.3/datatype.html "PostgreSQL 9.3 - Chapter 8. Data Types")

/
[9.2](https://www.postgresql.org/docs/9.2/datatype.html "PostgreSQL 9.2 - Chapter 8. Data Types")

/
[9.1](https://www.postgresql.org/docs/9.1/datatype.html "PostgreSQL 9.1 - Chapter 8. Data Types")

/
[9.0](https://www.postgresql.org/docs/9.0/datatype.html "PostgreSQL 9.0 - Chapter 8. Data Types")

/
[8.4](https://www.postgresql.org/docs/8.4/datatype.html "PostgreSQL 8.4 - Chapter 8. Data Types")

/
[8.3](https://www.postgresql.org/docs/8.3/datatype.html "PostgreSQL 8.3 - Chapter 8. Data Types")

/
[8.2](https://www.postgresql.org/docs/8.2/datatype.html "PostgreSQL 8.2 - Chapter 8. Data Types")

/
[8.1](https://www.postgresql.org/docs/8.1/datatype.html "PostgreSQL 8.1 - Chapter 8. Data Types")

/
[8.0](https://www.postgresql.org/docs/8.0/datatype.html "PostgreSQL 8.0 - Chapter 8. Data Types")

/
[7.4](https://www.postgresql.org/docs/7.4/datatype.html "PostgreSQL 7.4 - Chapter 8. Data Types")

/
[7.3](https://www.postgresql.org/docs/7.3/datatype.html "PostgreSQL 7.3 - Chapter 8. Data Types")

/
[7.2](https://www.postgresql.org/docs/7.2/datatype.html "PostgreSQL 7.2 - Chapter 8. Data Types")

/
[7.1](https://www.postgresql.org/docs/7.1/datatype.html "PostgreSQL 7.1 - Chapter 8. Data Types")

This documentation is for an unsupported version of PostgreSQL.

You may want to view the same page for the
[current](https://www.postgresql.org/docs/current/datatype.html "PostgreSQL  - Chapter 8. Data Types")
version, or one of the other supported versions listed above instead.


| Chapter 8. Data Types |
| :-: |
| [Prev](https://www.postgresql.org/docs/12/queries-with.html "7.8. WITH Queries (Common Table Expressions)") | [Up](https://www.postgresql.org/docs/12/sql.html "Part II. The SQL Language") | Part II. The SQL Language | [Home](https://www.postgresql.org/docs/12/index.html "PostgreSQL 12.22 Documentation") | [Next](https://www.postgresql.org/docs/12/datatype-numeric.html "8.1. Numeric Types") |

* * *

## Chapter 8. Data Types

**Table of Contents**

[8.1. Numeric Types](https://www.postgresql.org/docs/12/datatype-numeric.html)[8.1.1. Integer Types](https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-INT)[8.1.2. Arbitrary Precision Numbers](https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL)[8.1.3. Floating-Point Types](https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-FLOAT)[8.1.4. Serial Types](https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-SERIAL)[8.2. Monetary Types](https://www.postgresql.org/docs/12/datatype-money.html)[8.3. Character Types](https://www.postgresql.org/docs/12/datatype-character.html)[8.4. Binary Data Types](https://www.postgresql.org/docs/12/datatype-binary.html)[8.4.1. `bytea` Hex Format](https://www.postgresql.org/docs/12/datatype-binary.html#id-1.5.7.12.9)[8.4.2. `bytea` Escape Format](https://www.postgresql.org/docs/12/datatype-binary.html#id-1.5.7.12.10)[8.5. Date/Time Types](https://www.postgresql.org/docs/12/datatype-datetime.html)[8.5.1. Date/Time Input](https://www.postgresql.org/docs/12/datatype-datetime.html#DATATYPE-DATETIME-INPUT)[8.5.2. Date/Time Output](https://www.postgresql.org/docs/12/datatype-datetime.html#DATATYPE-DATETIME-OUTPUT)[8.5.3. Time Zones](https://www.postgresql.org/docs/12/datatype-datetime.html#DATATYPE-TIMEZONES)[8.5.4. Interval Input](https://www.postgresql.org/docs/12/datatype-datetime.html#DATATYPE-INTERVAL-INPUT)[8.5.5. Interval Output](https://www.postgresql.org/docs/12/datatype-datetime.html#DATATYPE-INTERVAL-OUTPUT)[8.6. Boolean Type](https://www.postgresql.org/docs/12/datatype-boolean.html)[8.7. Enumerated Types](https://www.postgresql.org/docs/12/datatype-enum.html)[8.7.1. Declaration of Enumerated Types](https://www.postgresql.org/docs/12/datatype-enum.html#id-1.5.7.15.5)[8.7.2. Ordering](https://www.postgresql.org/docs/12/datatype-enum.html#id-1.5.7.15.6)[8.7.3. Type Safety](https://www.postgresql.org/docs/12/datatype-enum.html#id-1.5.7.15.7)[8.7.4. Implementation Details](https://www.postgresql.org/docs/12/datatype-enum.html#id-1.5.7.15.8)[8.8. Geometric Types](https://www.postgresql.org/docs/12/datatype-geometric.html)[8.8.1. Points](https://www.postgresql.org/docs/12/datatype-geometric.html#id-1.5.7.16.6)[8.8.2. Lines](https://www.postgresql.org/docs/12/datatype-geometric.html#DATATYPE-LINE)[8.8.3. Line Segments](https://www.postgresql.org/docs/12/datatype-geometric.html#DATATYPE-LSEG)[8.8.4. Boxes](https://www.postgresql.org/docs/12/datatype-geometric.html#id-1.5.7.16.9)[8.8.5. Paths](https://www.postgresql.org/docs/12/datatype-geometric.html#id-1.5.7.16.10)[8.8.6. Polygons](https://www.postgresql.org/docs/12/datatype-geometric.html#DATATYPE-POLYGON)[8.8.7. Circles](https://www.postgresql.org/docs/12/datatype-geometric.html#DATATYPE-CIRCLE)[8.9. Network Address Types](https://www.postgresql.org/docs/12/datatype-net-types.html)[8.9.1. `inet`](https://www.postgresql.org/docs/12/datatype-net-types.html#DATATYPE-INET)[8.9.2. `cidr`](https://www.postgresql.org/docs/12/datatype-net-types.html#DATATYPE-CIDR)[8.9.3. `inet` vs. `cidr`](https://www.postgresql.org/docs/12/datatype-net-types.html#DATATYPE-INET-VS-CIDR)[8.9.4. `macaddr`](https://www.postgresql.org/docs/12/datatype-net-types.html#DATATYPE-MACADDR)[8.9.5. `macaddr8`](https://www.postgresql.org/docs/12/datatype-net-types.html#DATATYPE-MACADDR8)[8.10. Bit String Types](https://www.postgresql.org/docs/12/datatype-bit.html)[8.11. Text Search Types](https://www.postgresql.org/docs/12/datatype-textsearch.html)[8.11.1. `tsvector`](https://www.postgresql.org/docs/12/datatype-textsearch.html#DATATYPE-TSVECTOR)[8.11.2. `tsquery`](https://www.postgresql.org/docs/12/datatype-textsearch.html#DATATYPE-TSQUERY)[8.12. UUID Type](https://www.postgresql.org/docs/12/datatype-uuid.html)[8.13. XML Type](https://www.postgresql.org/docs/12/datatype-xml.html)[8.13.1. Creating XML Values](https://www.postgresql.org/docs/12/datatype-xml.html#id-1.5.7.21.6)[8.13.2. Encoding Handling](https://www.postgresql.org/docs/12/datatype-xml.html#id-1.5.7.21.7)[8.13.3. Accessing XML Values](https://www.postgresql.org/docs/12/datatype-xml.html#id-1.5.7.21.8)[8.14. JSON Types](https://www.postgresql.org/docs/12/datatype-json.html)[8.14.1. JSON Input and Output Syntax](https://www.postgresql.org/docs/12/datatype-json.html#JSON-KEYS-ELEMENTS)[8.14.2. Designing JSON Documents](https://www.postgresql.org/docs/12/datatype-json.html#JSON-DOC-DESIGN)[8.14.3. `jsonb` Containment and Existence](https://www.postgresql.org/docs/12/datatype-json.html#JSON-CONTAINMENT)[8.14.4. `jsonb` Indexing](https://www.postgresql.org/docs/12/datatype-json.html#JSON-INDEXING)[8.14.5. Transforms](https://www.postgresql.org/docs/12/datatype-json.html#id-1.5.7.22.19)[8.14.6. jsonpath Type](https://www.postgresql.org/docs/12/datatype-json.html#DATATYPE-JSONPATH)[8.15. Arrays](https://www.postgresql.org/docs/12/arrays.html)[8.15.1. Declaration of Array Types](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-DECLARATION)[8.15.2. Array Value Input](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-INPUT)[8.15.3. Accessing Arrays](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-ACCESSING)[8.15.4. Modifying Arrays](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-MODIFYING)[8.15.5. Searching in Arrays](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-SEARCHING)[8.15.6. Array Input and Output Syntax](https://www.postgresql.org/docs/12/arrays.html#ARRAYS-IO)[8.16. Composite Types](https://www.postgresql.org/docs/12/rowtypes.html)[8.16.1. Declaration of Composite Types](https://www.postgresql.org/docs/12/rowtypes.html#ROWTYPES-DECLARING)[8.16.2. Constructing Composite Values](https://www.postgresql.org/docs/12/rowtypes.html#id-1.5.7.24.6)[8.16.3. Accessing Composite Types](https://www.postgresql.org/docs/12/rowtypes.html#ROWTYPES-ACCESSING)[8.16.4. Modifying Composite Types](https://www.postgresql.org/docs/12/rowtypes.html#id-1.5.7.24.8)[8.16.5. Using Composite Types in Queries](https://www.postgresql.org/docs/12/rowtypes.html#ROWTYPES-USAGE)[8.16.6. Composite Type Input and Output Syntax](https://www.postgresql.org/docs/12/rowtypes.html#ROWTYPES-IO-SYNTAX)[8.17. Range Types](https://www.postgresql.org/docs/12/rangetypes.html)[8.17.1. Built-in Range Types](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-BUILTIN)[8.17.2. Examples](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-EXAMPLES)[8.17.3. Inclusive and Exclusive Bounds](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-INCLUSIVITY)[8.17.4. Infinite (Unbounded) Ranges](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-INFINITE)[8.17.5. Range Input/Output](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-IO)[8.17.6. Constructing Ranges](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-CONSTRUCT)[8.17.7. Discrete Range Types](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-DISCRETE)[8.17.8. Defining New Range Types](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-DEFINING)[8.17.9. Indexing](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-INDEXING)[8.17.10. Constraints on Ranges](https://www.postgresql.org/docs/12/rangetypes.html#RANGETYPES-CONSTRAINT)[8.18. Domain Types](https://www.postgresql.org/docs/12/domains.html)[8.19. Object Identifier Types](https://www.postgresql.org/docs/12/datatype-oid.html)[8.20. pg\_lsn Type](https://www.postgresql.org/docs/12/datatype-pg-lsn.html)[8.21. Pseudo-Types](https://www.postgresql.org/docs/12/datatype-pseudo.html)

PostgreSQL has a rich set of native data types available to users. Users can add new types to PostgreSQL using the [CREATE TYPE](https://www.postgresql.org/docs/12/sql-createtype.html "CREATE TYPE") command.

[Table 8.1](https://www.postgresql.org/docs/12/datatype.html#DATATYPE-TABLE "Table 8.1. Data Types") shows all the built-in general-purpose data types. Most of the alternative names listed in the “Aliases” column are the names used internally by PostgreSQL for historical reasons. In addition, some internally used or deprecated types are available, but are not listed here.

**Table 8.1. Data Types**

| Name | Aliases | Description |
| --- | --- | --- |
| `bigint` | `int8` | signed eight-byte integer |
| `bigserial` | `serial8` | autoincrementing eight-byte integer |
| `bit [ (n) ]` |  | fixed-length bit string |
| `bit varying [ (n) ]` | `varbit [ (n) ]` | variable-length bit string |
| `boolean` | `bool` | logical Boolean (true/false) |
| `box` |  | rectangular box on a plane |
| `bytea` |  | binary data (“byte array”) |
| `character [ (n) ]` | `char [ (n) ]` | fixed-length character string |
| `character varying [ (n) ]` | `varchar [ (n) ]` | variable-length character string |
| `cidr` |  | IPv4 or IPv6 network address |
| `circle` |  | circle on a plane |
| `date` |  | calendar date (year, month, day) |
| `double precision` | `float8` | double precision floating-point number (8 bytes) |
| `inet` |  | IPv4 or IPv6 host address |
| `integer` | `int`, `int4` | signed four-byte integer |
| `interval [ fields ] [ (p) ]` |  | time span |
| `json` |  | textual JSON data |
| `jsonb` |  | binary JSON data, decomposed |
| `line` |  | infinite line on a plane |
| `lseg` |  | line segment on a plane |
| `macaddr` |  | MAC (Media Access Control) address |
| `macaddr8` |  | MAC (Media Access Control) address (EUI-64 format) |
| `money` |  | currency amount |
| `numeric [ (p, s) ]` | `decimal [ (p, s) ]` | exact numeric of selectable precision |
| `path` |  | geometric path on a plane |
| `pg_lsn` |  | PostgreSQL Log Sequence Number |
| `point` |  | geometric point on a plane |
| `polygon` |  | closed geometric path on a plane |
| `real` | `float4` | single precision floating-point number (4 bytes) |
| `smallint` | `int2` | signed two-byte integer |
| `smallserial` | `serial2` | autoincrementing two-byte integer |
| `serial` | `serial4` | autoincrementing four-byte integer |
| `text` |  | variable-length character string |
| `time [ (p) ] [ without time zone ]` |  | time of day (no time zone) |
| `time [ (p) ] with time zone` | `timetz` | time of day, including time zone |
| `timestamp [ (p) ] [ without time zone ]` |  | date and time (no time zone) |
| `timestamp [ (p) ] with time zone` | `timestamptz` | date and time, including time zone |
| `tsquery` |  | text search query |
| `tsvector` |  | text search document |
| `txid_snapshot` |  | user-level transaction ID snapshot |
| `uuid` |  | universally unique identifier |
| `xml` |  | XML data |

### Compatibility

The following types (or spellings thereof) are specified by SQL: `bigint`, `bit`, `bit varying`, `boolean`, `char`, `character varying`, `character`, `varchar`, `date`, `double precision`, `integer`, `interval`, `numeric`, `decimal`, `real`, `smallint`, `time` (with or without time zone), `timestamp` (with or without time zone), `xml`.

Each data type has an external representation determined by its input and output functions. Many of the built-in types have obvious external formats. However, several types are either unique to PostgreSQL, such as geometric paths, or have several possible formats, such as the date and time types. Some of the input and output functions are not invertible, i.e., the result of an output function might lose accuracy when compared to the original input.

* * *

|     |     |     |
| --- | --- | --- |
| [Prev](https://www.postgresql.org/docs/12/queries-with.html "7.8. WITH Queries (Common Table Expressions)") | [Up](https://www.postgresql.org/docs/12/sql.html "Part II. The SQL Language") | [Next](https://www.postgresql.org/docs/12/datatype-numeric.html "8.1. Numeric Types") |
| 7.8. `WITH` Queries (Common Table Expressions) | [Home](https://www.postgresql.org/docs/12/index.html "PostgreSQL 12.22 Documentation") | 8.1. Numeric Types |