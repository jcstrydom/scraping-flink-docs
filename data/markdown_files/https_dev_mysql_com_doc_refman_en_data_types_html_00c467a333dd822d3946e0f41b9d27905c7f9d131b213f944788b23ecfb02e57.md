[Skip to Main Content](https://dev.mysql.com/doc/refman/8.0/en/data-types.html#main)

[Hide Sidebar](https://dev.mysql.com/doc/refman/8.0/en/data-types.html "Hide Sidebar")

[Previous: MySQL Server Locale Support](https://dev.mysql.com/doc/refman/8.0/en/locale-support.html "Previous: MySQL Server Locale Support")[Start](https://dev.mysql.com/doc/refman/8.0/en/index.html "Start")[Up](https://dev.mysql.com/doc/refman/8.0/en/index.html "Up")[Next: Numeric Data Types](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html "Next: Numeric Data Types")

[Documentation Home](https://dev.mysql.com/doc/)

* * *

MySQL 8.0 Reference Manual

[Related Documentation](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/)

[MySQL 8.0 Source Code Documentation](https://dev.mysql.com/doc/dev/mysql-server/latest/)

[Download\\
this Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-8.0-en.pdf)
\- 43.3Mb

[PDF (A4)](https://downloads.mysql.com/docs/refman-8.0-en.a4.pdf)
\- 43.4Mb

[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-8.0-en.man-gpl.tar.gz)
\- 297.2Kb

[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-8.0-en.man-gpl.zip)
\- 402.4Kb

[Info (Gzip)](https://downloads.mysql.com/docs/mysql-8.0.info.gz)
\- 4.3Mb

[Info (Zip)](https://downloads.mysql.com/docs/mysql-8.0.info.zip)
\- 4.3Mb

[Excerpts from this Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[MySQL Backup and Recovery](https://dev.mysql.com/doc/mysql-backup-excerpt/8.0/en/)

[MySQL Globalization](https://dev.mysql.com/doc/mysql-g11n-excerpt/8.0/en/)

[MySQL Information Schema](https://dev.mysql.com/doc/mysql-infoschema-excerpt/8.0/en/)

[MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)

[Security in MySQL](https://dev.mysql.com/doc/mysql-security-excerpt/8.0/en/)

[Starting and Stopping MySQL](https://dev.mysql.com/doc/mysql-startstop-excerpt/8.0/en/)

[MySQL and Linux/Unix](https://dev.mysql.com/doc/mysql-linuxunix-excerpt/8.0/en/)

[MySQL and Windows](https://dev.mysql.com/doc/mysql-windows-excerpt/8.0/en/)

[MySQL and macOS](https://dev.mysql.com/doc/mysql-macos-excerpt/8.0/en/)

[MySQL and Solaris](https://dev.mysql.com/doc/mysql-solaris-excerpt/8.0/en/)

[Building MySQL from Source](https://dev.mysql.com/doc/mysql-sourcebuild-excerpt/8.0/en/)

[MySQL Restrictions and Limitations](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/)

[MySQL Partitioning](https://dev.mysql.com/doc/mysql-partitioning-excerpt/8.0/en/)

[MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)

[MySQL Performance Schema](https://dev.mysql.com/doc/mysql-perfschema-excerpt/8.0/en/)

[MySQL Replication](https://dev.mysql.com/doc/mysql-replication-excerpt/8.0/en/)

[Using the MySQL Yum Repository](https://dev.mysql.com/doc/mysql-repo-excerpt/8.0/en/)

[MySQL NDB Cluster 8.0](https://dev.mysql.com/doc/mysql-cluster-excerpt/8.0/en/)

[version 8.0](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[9.5](https://dev.mysql.com/doc/refman/9.5/en/data-types.html)

[9.4](https://dev.mysql.com/doc/refman/9.4/en/data-types.html)

[9.3](https://dev.mysql.com/doc/refman/9.3/en/data-types.html)

[9.2](https://dev.mysql.com/doc/refman/9.2/en/data-types.html)

[9.1](https://dev.mysql.com/doc/refman/9.1/en/data-types.html)

[9.0](https://dev.mysql.com/doc/refman/9.0/en/data-types.html)

[8.4\\
current](https://dev.mysql.com/doc/refman/8.4/en/data-types.html)

[5.7](https://dev.mysql.com/doc/refman/5.7/en/data-types.html)

[8.0 \\
Japanese](https://dev.mysql.com/doc/refman/8.0/ja/data-types.html)

[Show Sidebar](https://dev.mysql.com/doc/refman/8.0/en/data-types.html "Show Sidebar")

[MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)  /
Data Types


# Chapter 13 Data Types

**Table of Contents**

[13.1 Numeric Data Types](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html)[13.1.1 Numeric Data Type Syntax](https://dev.mysql.com/doc/refman/8.0/en/numeric-type-syntax.html)[13.1.2 Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT,\\
MEDIUMINT, BIGINT](https://dev.mysql.com/doc/refman/8.0/en/integer-types.html)[13.1.3 Fixed-Point Types (Exact Value) - DECIMAL, NUMERIC](https://dev.mysql.com/doc/refman/8.0/en/fixed-point-types.html)[13.1.4 Floating-Point Types (Approximate Value) - FLOAT, DOUBLE](https://dev.mysql.com/doc/refman/8.0/en/floating-point-types.html)[13.1.5 Bit-Value Type - BIT](https://dev.mysql.com/doc/refman/8.0/en/bit-type.html)[13.1.6 Numeric Type Attributes](https://dev.mysql.com/doc/refman/8.0/en/numeric-type-attributes.html)[13.1.7 Out-of-Range and Overflow Handling](https://dev.mysql.com/doc/refman/8.0/en/out-of-range-and-overflow.html)[13.2 Date and Time Data Types](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html)[13.2.1 Date and Time Data Type Syntax](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-type-syntax.html)[13.2.2 The DATE, DATETIME, and TIMESTAMP Types](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)[13.2.3 The TIME Type](https://dev.mysql.com/doc/refman/8.0/en/time.html)[13.2.4 The YEAR Type](https://dev.mysql.com/doc/refman/8.0/en/year.html)[13.2.5 Automatic Initialization and Updating for TIMESTAMP and DATETIME](https://dev.mysql.com/doc/refman/8.0/en/timestamp-initialization.html)[13.2.6 Fractional Seconds in Time Values](https://dev.mysql.com/doc/refman/8.0/en/fractional-seconds.html)[13.2.7 What Calendar Is Used By MySQL?](https://dev.mysql.com/doc/refman/8.0/en/mysql-calendar.html)[13.2.8 Conversion Between Date and Time Types](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-type-conversion.html)[13.2.9 2-Digit Years in Dates](https://dev.mysql.com/doc/refman/8.0/en/two-digit-years.html)[13.3 String Data Types](https://dev.mysql.com/doc/refman/8.0/en/string-types.html)[13.3.1 String Data Type Syntax](https://dev.mysql.com/doc/refman/8.0/en/string-type-syntax.html)[13.3.2 The CHAR and VARCHAR Types](https://dev.mysql.com/doc/refman/8.0/en/char.html)[13.3.3 The BINARY and VARBINARY Types](https://dev.mysql.com/doc/refman/8.0/en/binary-varbinary.html)[13.3.4 The BLOB and TEXT Types](https://dev.mysql.com/doc/refman/8.0/en/blob.html)[13.3.5 The ENUM Type](https://dev.mysql.com/doc/refman/8.0/en/enum.html)[13.3.6 The SET Type](https://dev.mysql.com/doc/refman/8.0/en/set.html)[13.4 Spatial Data Types](https://dev.mysql.com/doc/refman/8.0/en/spatial-types.html)[13.4.1 Spatial Data Types](https://dev.mysql.com/doc/refman/8.0/en/spatial-type-overview.html)[13.4.2 The OpenGIS Geometry Model](https://dev.mysql.com/doc/refman/8.0/en/opengis-geometry-model.html)[13.4.3 Supported Spatial Data Formats](https://dev.mysql.com/doc/refman/8.0/en/gis-data-formats.html)[13.4.4 Geometry Well-Formedness and Validity](https://dev.mysql.com/doc/refman/8.0/en/geometry-well-formedness-validity.html)[13.4.5 Spatial Reference System Support](https://dev.mysql.com/doc/refman/8.0/en/spatial-reference-systems.html)[13.4.6 Creating Spatial Columns](https://dev.mysql.com/doc/refman/8.0/en/creating-spatial-columns.html)[13.4.7 Populating Spatial Columns](https://dev.mysql.com/doc/refman/8.0/en/populating-spatial-columns.html)[13.4.8 Fetching Spatial Data](https://dev.mysql.com/doc/refman/8.0/en/fetching-spatial-data.html)[13.4.9 Optimizing Spatial Analysis](https://dev.mysql.com/doc/refman/8.0/en/optimizing-spatial-analysis.html)[13.4.10 Creating Spatial Indexes](https://dev.mysql.com/doc/refman/8.0/en/creating-spatial-indexes.html)[13.4.11 Using Spatial Indexes](https://dev.mysql.com/doc/refman/8.0/en/using-spatial-indexes.html)[13.5 The JSON Data Type](https://dev.mysql.com/doc/refman/8.0/en/json.html)[13.6 Data Type Default Values](https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html)[13.7 Data Type Storage Requirements](https://dev.mysql.com/doc/refman/8.0/en/storage-requirements.html)[13.8 Choosing the Right Type for a Column](https://dev.mysql.com/doc/refman/8.0/en/choosing-types.html)[13.9 Using Data Types from Other Database Engines](https://dev.mysql.com/doc/refman/8.0/en/other-vendor-data-types.html)

MySQL supports [SQL](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_sql "SQL") data types in
several categories: numeric types, date and time types, string
(character and byte) types, spatial types, and the
[`JSON`](https://dev.mysql.com/doc/refman/8.0/en/json.html "13.5 The JSON Data Type") data type. This chapter provides
an overview and more detailed description of the properties of the
types in each category, and a summary of the data type storage
requirements. The initial overviews are intentionally brief. Consult
the more detailed descriptions for additional information about
particular data types, such as the permissible formats in which you
can specify values.


Data type descriptions use these conventions:

- For integer types, _`M`_ indicates the
maximum display width. For floating-point and fixed-point types,
_`M`_ is the total number of digits that
can be stored (the precision). For string types,
_`M`_ is the maximum length. The maximum
permissible value of _`M`_ depends on the
data type.


- _`D`_ applies to floating-point and
fixed-point types and indicates the number of digits following
the decimal point (the scale). The maximum possible value is 30,
but should be no greater than
_`M`_ −2.


- _`fsp`_ applies to the
[`TIME`](https://dev.mysql.com/doc/refman/8.0/en/time.html "13.2.3 The TIME Type"),
[`DATETIME`](https://dev.mysql.com/doc/refman/8.0/en/datetime.html "13.2.2 The DATE, DATETIME, and TIMESTAMP Types"), and
[`TIMESTAMP`](https://dev.mysql.com/doc/refman/8.0/en/datetime.html "13.2.2 The DATE, DATETIME, and TIMESTAMP Types") types and represents
fractional seconds precision; that is, the number of digits
following the decimal point for fractional parts of seconds. The
_`fsp`_ value, if given, must be in the
range 0 to 6. A value of 0 signifies that there is no fractional
part. If omitted, the default precision is 0. (This differs from
the standard SQL default of 6, for compatibility with previous
MySQL versions.)


- Square brackets (`[` and `]`)
indicate optional parts of type definitions.


[PREV](https://dev.mysql.com/doc/refman/8.0/en/locale-support.html "Previous: MySQL Server Locale Support") [HOME](https://dev.mysql.com/doc/refman/8.0/en/index.html "Start") [UP](https://dev.mysql.com/doc/refman/8.0/en/index.html "Up") [NEXT](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html "Next: Numeric Data Types")

[Related Documentation](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/)

[MySQL 8.0 Source Code Documentation](https://dev.mysql.com/doc/dev/mysql-server/latest/)

[Download\\
this Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-8.0-en.pdf)
\- 43.3Mb

[PDF (A4)](https://downloads.mysql.com/docs/refman-8.0-en.a4.pdf)
\- 43.4Mb

[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-8.0-en.man-gpl.tar.gz)
\- 297.2Kb

[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-8.0-en.man-gpl.zip)
\- 402.4Kb

[Info (Gzip)](https://downloads.mysql.com/docs/mysql-8.0.info.gz)
\- 4.3Mb

[Info (Zip)](https://downloads.mysql.com/docs/mysql-8.0.info.zip)
\- 4.3Mb

[Excerpts from this Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

[MySQL Backup and Recovery](https://dev.mysql.com/doc/mysql-backup-excerpt/8.0/en/)

[MySQL Globalization](https://dev.mysql.com/doc/mysql-g11n-excerpt/8.0/en/)

[MySQL Information Schema](https://dev.mysql.com/doc/mysql-infoschema-excerpt/8.0/en/)

[MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)

[Security in MySQL](https://dev.mysql.com/doc/mysql-security-excerpt/8.0/en/)

[Starting and Stopping MySQL](https://dev.mysql.com/doc/mysql-startstop-excerpt/8.0/en/)

[MySQL and Linux/Unix](https://dev.mysql.com/doc/mysql-linuxunix-excerpt/8.0/en/)

[MySQL and Windows](https://dev.mysql.com/doc/mysql-windows-excerpt/8.0/en/)

[MySQL and macOS](https://dev.mysql.com/doc/mysql-macos-excerpt/8.0/en/)

[MySQL and Solaris](https://dev.mysql.com/doc/mysql-solaris-excerpt/8.0/en/)

[Building MySQL from Source](https://dev.mysql.com/doc/mysql-sourcebuild-excerpt/8.0/en/)

[MySQL Restrictions and Limitations](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/)

[MySQL Partitioning](https://dev.mysql.com/doc/mysql-partitioning-excerpt/8.0/en/)

[MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)

[MySQL Performance Schema](https://dev.mysql.com/doc/mysql-perfschema-excerpt/8.0/en/)

[MySQL Replication](https://dev.mysql.com/doc/mysql-replication-excerpt/8.0/en/)

[Using the MySQL Yum Repository](https://dev.mysql.com/doc/mysql-repo-excerpt/8.0/en/)

[MySQL NDB Cluster 8.0](https://dev.mysql.com/doc/mysql-cluster-excerpt/8.0/en/)