[Go to main content](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BEGIN)

You are viewing an older release.

View latestClose this notice

[Home](https://docs.oracle.com/) / [Database](https://docs.oracle.com/en/database/) / [Oracle Database Online Documentation 12c Release 1 (12.1)](https://docs.oracle.com/database/121/index.html) / [Database Administration](https://docs.oracle.com/database/121/nav/portal_4.htm)

Database SQL Language Reference

[![Contents](https://docs.oracle.com/database/121/dcommon/img/hidetools.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)

[![Previous](https://docs.oracle.com/database/121/dcommon/img/prev.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements.htm)[![Next](https://docs.oracle.com/database/121/dcommon/img/next.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm)[![](https://docs.oracle.com/database/121/dcommon/img/home.gif)](https://docs.oracle.com/database/121/index.htm)

Page 12 of 555

Search

This Book This Release

Table of Contents

- [![open](https://docs.oracle.com/database/121/dcommon/img/minus.png)](https://docs.oracle.com/database/121/SQLRF/toc.htm)[Oracle Database SQL Language Reference](https://docs.oracle.com/database/121/SQLRF/toc.htm)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Preface](https://docs.oracle.com/database/121/SQLRF/preface.htm#SQLRF50918)
    - [Audience](https://docs.oracle.com/database/121/SQLRF/preface.htm#SQLRF50919)
    - [Documentation Accessibility](https://docs.oracle.com/database/121/SQLRF/preface.htm#SQLRF55579)
    - [Related Documents](https://docs.oracle.com/database/121/SQLRF/preface.htm#SQLRF50924)
    - [Conventions](https://docs.oracle.com/database/121/SQLRF/preface.htm#SQLRF50925)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Changes in This Release for Oracle Database SQL Language Reference](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56314)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Changes in Oracle Database 12c Release 1 (12.1.0.2)](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56677)
      - [New Features](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56716)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Changes in Oracle Database 12c Release 1 (12.1.0.1)](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56315)
      - [New Features](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56316)
      - [Deprecated Features](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56317)
      - [Desupported Features](https://docs.oracle.com/database/121/SQLRF/release_changes.htm#SQLRF56318)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Introduction to Oracle SQL](https://docs.oracle.com/database/121/SQLRF/intro.htm#SQLRF001)
    - [History of SQL](https://docs.oracle.com/database/121/SQLRF/intro001.htm#SQLRF50932)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Standards](https://docs.oracle.com/database/121/SQLRF/intro002.htm#SQLRF50933)
      - [How SQL Works](https://docs.oracle.com/database/121/SQLRF/intro002.htm#SQLRF50934)
      - [Common Language for All Relational Databases](https://docs.oracle.com/database/121/SQLRF/intro002.htm#SQLRF50935)
    - [Using Enterprise Manager](https://docs.oracle.com/database/121/SQLRF/intro003.htm#SQLRF50936)
    - [Lexical Conventions](https://docs.oracle.com/database/121/SQLRF/intro004.htm#SQLRF50937)
    - [Tools Support](https://docs.oracle.com/database/121/SQLRF/intro005.htm#SQLRF50938)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Basic Elements of Oracle SQL](https://docs.oracle.com/database/121/SQLRF/sql_elements.htm#SQLRF002)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF0021)
      - [Oracle Built-in Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30020)
      - [Extended Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF55623)
      - [Rowid Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF50998)
      - [ANSI, DB2, and SQL/DS Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF00213)
      - [User-Defined Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30021)
      - [Oracle-Supplied Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30022)
      - [Any Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30023)
      - [XML Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30024)
      - [Spatial Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30025)
      - [Media Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30026)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Data Type Comparison Rules](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF30027)
      - [Numeric Values](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51036)
      - [Date Values](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51037)
      - [Character Values](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51038)
      - [Object Values](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51043)
      - [Varrays and Nested Tables](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51044)
      - [Data Type Precedence](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51045)
      - [Data Conversion](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF00214)
      - [Security Considerations for Data Conversion](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#SQLRF51056)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Literals](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#SQLRF00217)
      - [Text Literals](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#SQLRF00218)
      - [Numeric Literals](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#SQLRF00220)
      - [Datetime Literals](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#SQLRF51062)
      - [Interval Literals](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#SQLRF00221)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Format Models](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF00210)
      - [Number Format Models](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF00211)
      - [Datetime Format Models](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF00212)
      - [Format Model Modifiers](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF00216)
      - [String-to-Date Conversion Rules](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF51090)
      - [XML Format Model](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#SQLRF51092)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Nulls](https://docs.oracle.com/database/121/SQLRF/sql_elements005.htm#SQLRF30037)
      - [Nulls in SQL Functions](https://docs.oracle.com/database/121/SQLRF/sql_elements005.htm#SQLRF51094)
      - [Nulls with Comparison Conditions](https://docs.oracle.com/database/121/SQLRF/sql_elements005.htm#SQLRF51095)
      - [Nulls in Conditions](https://docs.oracle.com/database/121/SQLRF/sql_elements005.htm#SQLRF51096)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Comments](https://docs.oracle.com/database/121/SQLRF/sql_elements006.htm#SQLRF51098)
      - [Comments Within SQL Statements](https://docs.oracle.com/database/121/SQLRF/sql_elements006.htm#SQLRF51099)
      - [Comments on Schema and Nonschema Objects](https://docs.oracle.com/database/121/SQLRF/sql_elements006.htm#SQLRF51101)
      - [Hints](https://docs.oracle.com/database/121/SQLRF/sql_elements006.htm#SQLRF00219)
      - [Alphabetical Listing of Hints](https://docs.oracle.com/database/121/SQLRF/sql_elements006.htm#SQLRF51108)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Database Objects](https://docs.oracle.com/database/121/SQLRF/sql_elements007.htm#SQLRF20003)
      - [Schema Objects](https://docs.oracle.com/database/121/SQLRF/sql_elements007.htm#SQLRF51127)
      - [Nonschema Objects](https://docs.oracle.com/database/121/SQLRF/sql_elements007.htm#SQLRF51128)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Database Object Names and Qualifiers](https://docs.oracle.com/database/121/SQLRF/sql_elements008.htm#SQLRF00223)
      - [Database Object Naming Rules](https://docs.oracle.com/database/121/SQLRF/sql_elements008.htm#SQLRF51129)
      - [Schema Object Naming Examples](https://docs.oracle.com/database/121/SQLRF/sql_elements008.htm#SQLRF51130)
      - [Schema Object Naming Guidelines](https://docs.oracle.com/database/121/SQLRF/sql_elements008.htm#SQLRF51131)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Syntax for Schema Objects and Parts in SQL Statements](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51132)
      - [How Oracle Database Resolves Schema Object References](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51134)
      - [References to Objects in Other Schemas](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51135)
      - [References to Objects in Remote Databases](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51136)
      - [References to Partitioned Tables and Indexes](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51143)
      - [References to Object Type Attributes and Methods](https://docs.oracle.com/database/121/SQLRF/sql_elements009.htm#SQLRF51150)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Pseudocolumns](https://docs.oracle.com/database/121/SQLRF/pseudocolumns.htm#SQLRF0025)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Hierarchical Query Pseudocolumns](https://docs.oracle.com/database/121/SQLRF/pseudocolumns001.htm#SQLRF00251)
      - [CONNECT\_BY\_ISCYCLE Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns001.htm#SQLRF50939)
      - [CONNECT\_BY\_ISLEAF Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns001.htm#SQLRF50940)
      - [LEVEL Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns001.htm#SQLRF50942)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Sequence Pseudocolumns](https://docs.oracle.com/database/121/SQLRF/pseudocolumns002.htm#SQLRF00253)
      - [Where to Use Sequence Values](https://docs.oracle.com/database/121/SQLRF/pseudocolumns002.htm#SQLRF50944)
      - [How to Use Sequence Values](https://docs.oracle.com/database/121/SQLRF/pseudocolumns002.htm#SQLRF50946)
    - [Version Query Pseudocolumns](https://docs.oracle.com/database/121/SQLRF/pseudocolumns003.htm#SQLRF00252)
    - [COLUMN\_VALUE Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns004.htm#SQLRF50950)
    - [OBJECT\_ID Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns005.htm#SQLRF50951)
    - [OBJECT\_VALUE Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns006.htm#SQLRF50952)
    - [ORA\_ROWSCN Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns007.htm#SQLRF50953)
    - [ROWID Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns008.htm#SQLRF00254)
    - [ROWNUM Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns009.htm#SQLRF00255)
    - [XMLDATA Pseudocolumn](https://docs.oracle.com/database/121/SQLRF/pseudocolumns010.htm#SQLRF00256)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Operators](https://docs.oracle.com/database/121/SQLRF/operators.htm#SQLRF003)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[About SQL Operators](https://docs.oracle.com/database/121/SQLRF/operators001.htm#SQLRF51151)
      - [Unary and Binary Operators](https://docs.oracle.com/database/121/SQLRF/operators001.htm#SQLRF51152)
      - [Operator Precedence](https://docs.oracle.com/database/121/SQLRF/operators001.htm#SQLRF51153)
    - [Arithmetic Operators](https://docs.oracle.com/database/121/SQLRF/operators002.htm#SQLRF51156)
    - [Concatenation Operator](https://docs.oracle.com/database/121/SQLRF/operators003.htm#SQLRF51158)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Hierarchical Query Operators](https://docs.oracle.com/database/121/SQLRF/operators004.htm#SQLRF51161)
      - [PRIOR](https://docs.oracle.com/database/121/SQLRF/operators004.htm#SQLRF51162)
      - [CONNECT\_BY\_ROOT](https://docs.oracle.com/database/121/SQLRF/operators004.htm#SQLRF0031)
    - [Set Operators](https://docs.oracle.com/database/121/SQLRF/operators005.htm#SQLRF51164)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Multiset Operators](https://docs.oracle.com/database/121/SQLRF/operators006.htm#SQLRF0032)
      - [MULTISET EXCEPT](https://docs.oracle.com/database/121/SQLRF/operators006.htm#SQLRF51166)
      - [MULTISET INTERSECT](https://docs.oracle.com/database/121/SQLRF/operators006.htm#SQLRF51168)
      - [MULTISET UNION](https://docs.oracle.com/database/121/SQLRF/operators006.htm#SQLRF51170)
    - [User-Defined Operators](https://docs.oracle.com/database/121/SQLRF/operators007.htm#SQLRF51172)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Expressions](https://docs.oracle.com/database/121/SQLRF/expressions.htm#SQLRF004)
    - [About SQL Expressions](https://docs.oracle.com/database/121/SQLRF/expressions001.htm#SQLRF52066)
    - [Simple Expressions](https://docs.oracle.com/database/121/SQLRF/expressions002.htm#SQLRF52068)
    - [Compound Expressions](https://docs.oracle.com/database/121/SQLRF/expressions003.htm#SQLRF52070)
    - [CASE Expressions](https://docs.oracle.com/database/121/SQLRF/expressions004.htm#SQLRF20037)
    - [Column Expressions](https://docs.oracle.com/database/121/SQLRF/expressions005.htm#SQLRF20043)
    - [CURSOR Expressions](https://docs.oracle.com/database/121/SQLRF/expressions006.htm#SQLRF52077)
    - [Datetime Expressions](https://docs.oracle.com/database/121/SQLRF/expressions007.htm#SQLRF00401)
    - [Function Expressions](https://docs.oracle.com/database/121/SQLRF/expressions008.htm#SQLRF52082)
    - [Interval Expressions](https://docs.oracle.com/database/121/SQLRF/expressions009.htm#SQLRF52084)
    - [JSON Object Access Expressions](https://docs.oracle.com/database/121/SQLRF/expressions010.htm#SQLRF57024)
    - [Model Expressions](https://docs.oracle.com/database/121/SQLRF/expressions011.htm#SQLRF52086)
    - [Object Access Expressions](https://docs.oracle.com/database/121/SQLRF/expressions012.htm#SQLRF52088)
    - [Placeholder Expressions](https://docs.oracle.com/database/121/SQLRF/expressions013.htm#SQLRF52091)
    - [Scalar Subquery Expressions](https://docs.oracle.com/database/121/SQLRF/expressions014.htm#SQLRF52093)
    - [Type Constructor Expressions](https://docs.oracle.com/database/121/SQLRF/expressions015.htm#SQLRF52094)
    - [Expression Lists](https://docs.oracle.com/database/121/SQLRF/expressions016.htm#SQLRF52099)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Conditions](https://docs.oracle.com/database/121/SQLRF/conditions.htm#SQLRF005)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[About SQL Conditions](https://docs.oracle.com/database/121/SQLRF/conditions001.htm#SQLRF52101)
      - [Condition Precedence](https://docs.oracle.com/database/121/SQLRF/conditions001.htm#SQLRF52103)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Comparison Conditions](https://docs.oracle.com/database/121/SQLRF/conditions002.htm#SQLRF52105)
      - [Simple Comparison Conditions](https://docs.oracle.com/database/121/SQLRF/conditions002.htm#SQLRF52107)
      - [Group Comparison Conditions](https://docs.oracle.com/database/121/SQLRF/conditions002.htm#SQLRF52110)
    - [Floating-Point Conditions](https://docs.oracle.com/database/121/SQLRF/conditions003.htm#SQLRF52113)
    - [Logical Conditions](https://docs.oracle.com/database/121/SQLRF/conditions004.htm#SQLRF52116)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Model Conditions](https://docs.oracle.com/database/121/SQLRF/conditions005.htm#SQLRF52121)
      - [IS ANY Condition](https://docs.oracle.com/database/121/SQLRF/conditions005.htm#SQLRF52122)
      - [IS PRESENT Condition](https://docs.oracle.com/database/121/SQLRF/conditions005.htm#SQLRF52125)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Multiset Conditions](https://docs.oracle.com/database/121/SQLRF/conditions006.htm#SQLRF52128)
      - [IS A SET Condition](https://docs.oracle.com/database/121/SQLRF/conditions006.htm#SQLRF52129)
      - [IS EMPTY Condition](https://docs.oracle.com/database/121/SQLRF/conditions006.htm#SQLRF52132)
      - [MEMBER Condition](https://docs.oracle.com/database/121/SQLRF/conditions006.htm#SQLRF52135)
      - [SUBMULTISET Condition](https://docs.oracle.com/database/121/SQLRF/conditions006.htm#SQLRF52138)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Pattern-matching Conditions](https://docs.oracle.com/database/121/SQLRF/conditions007.htm#SQLRF52141)
      - [LIKE Condition](https://docs.oracle.com/database/121/SQLRF/conditions007.htm#SQLRF52142)
      - [REGEXP\_LIKE Condition](https://docs.oracle.com/database/121/SQLRF/conditions007.htm#SQLRF00501)
    - [Null Conditions](https://docs.oracle.com/database/121/SQLRF/conditions008.htm#SQLRF52152)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[XML Conditions](https://docs.oracle.com/database/121/SQLRF/conditions009.htm#SQLRF52155)
      - [EQUALS\_PATH Condition](https://docs.oracle.com/database/121/SQLRF/conditions009.htm#SQLRF52156)
      - [UNDER\_PATH Condition](https://docs.oracle.com/database/121/SQLRF/conditions009.htm#SQLRF52159)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[JSON Conditions](https://docs.oracle.com/database/121/SQLRF/conditions010.htm#SQLRF56660)
      - [IS JSON Condition](https://docs.oracle.com/database/121/SQLRF/conditions010.htm#SQLRF56661)
      - [JSON\_EXISTS Condition](https://docs.oracle.com/database/121/SQLRF/conditions010.htm#SQLRF56664)
      - [JSON\_TEXTCONTAINS Condition](https://docs.oracle.com/database/121/SQLRF/conditions010.htm#SQLRF56963)
    - [Compound Conditions](https://docs.oracle.com/database/121/SQLRF/conditions011.htm#SQLRF52162)
    - [BETWEEN Condition](https://docs.oracle.com/database/121/SQLRF/conditions012.htm#SQLRF52164)
    - [EXISTS Condition](https://docs.oracle.com/database/121/SQLRF/conditions013.htm#SQLRF52167)
    - [IN Condition](https://docs.oracle.com/database/121/SQLRF/conditions014.htm#SQLRF52169)
    - [IS OF type Condition](https://docs.oracle.com/database/121/SQLRF/conditions015.htm#SQLRF52174)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Functions](https://docs.oracle.com/database/121/SQLRF/functions.htm#SQLRF006)
    - [About SQL Functions](https://docs.oracle.com/database/121/SQLRF/functions001.htm#SQLRF51173)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Single-Row Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51178)
      - [Numeric Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF20031)
      - [Character Functions Returning Character Values](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF20032)
      - [Character Functions Returning Number Values](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51180)
      - [Character Set Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51179)
      - [Datetime Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF20033)
      - [General Comparison Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51181)
      - [Conversion Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF20034)
      - [Large Object Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51182)
      - [Collection Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51183)
      - [Hierarchical Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51184)
      - [Data Mining Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF20030)
      - [XML Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51185)
      - [JSON Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF56667)
      - [Encoding and Decoding Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51186)
      - [NULL-Related Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF30049)
      - [Environment and Identifier Functions](https://docs.oracle.com/database/121/SQLRF/functions002.htm#SQLRF51187)
    - [Aggregate Functions](https://docs.oracle.com/database/121/SQLRF/functions003.htm#SQLRF20035)
    - [Analytic Functions](https://docs.oracle.com/database/121/SQLRF/functions004.htm#SQLRF06174)
    - [Object Reference Functions](https://docs.oracle.com/database/121/SQLRF/functions005.htm#SQLRF51209)
    - [Model Functions](https://docs.oracle.com/database/121/SQLRF/functions006.htm#SQLRF51210)
    - [OLAP Functions](https://docs.oracle.com/database/121/SQLRF/functions007.htm#SQLRF55592)
    - [Data Cartridge Functions](https://docs.oracle.com/database/121/SQLRF/functions008.htm#SQLRF55593)
    - [ABS](https://docs.oracle.com/database/121/SQLRF/functions009.htm#SQLRF00601)
    - [ACOS](https://docs.oracle.com/database/121/SQLRF/functions010.htm#SQLRF00602)
    - [ADD\_MONTHS](https://docs.oracle.com/database/121/SQLRF/functions011.htm#SQLRF00603)
    - [APPENDCHILDXML](https://docs.oracle.com/database/121/SQLRF/functions012.htm#SQLRF06201)
    - [APPROX\_COUNT\_DISTINCT](https://docs.oracle.com/database/121/SQLRF/functions013.htm#SQLRF56900)
    - [ASCII](https://docs.oracle.com/database/121/SQLRF/functions014.htm#SQLRF00604)
    - [ASCIISTR](https://docs.oracle.com/database/121/SQLRF/functions015.htm#SQLRF00605)
    - [ASIN](https://docs.oracle.com/database/121/SQLRF/functions016.htm#SQLRF00606)
    - [ATAN](https://docs.oracle.com/database/121/SQLRF/functions017.htm#SQLRF00607)
    - [ATAN2](https://docs.oracle.com/database/121/SQLRF/functions018.htm#SQLRF00608)
    - [AVG](https://docs.oracle.com/database/121/SQLRF/functions019.htm#SQLRF00609)
    - [BFILENAME](https://docs.oracle.com/database/121/SQLRF/functions020.htm#SQLRF00610)
    - [BIN\_TO\_NUM](https://docs.oracle.com/database/121/SQLRF/functions021.htm#SQLRF00611)
    - [BITAND](https://docs.oracle.com/database/121/SQLRF/functions022.htm#SQLRF00612)
    - [CARDINALITY](https://docs.oracle.com/database/121/SQLRF/functions023.htm#SQLRF06305)
    - [CAST](https://docs.oracle.com/database/121/SQLRF/functions024.htm#SQLRF00613)
    - [CEIL](https://docs.oracle.com/database/121/SQLRF/functions025.htm#SQLRF00614)
    - [CHARTOROWID](https://docs.oracle.com/database/121/SQLRF/functions026.htm#SQLRF00615)
    - [CHR](https://docs.oracle.com/database/121/SQLRF/functions027.htm#SQLRF00616)
    - [CLUSTER\_DETAILS](https://docs.oracle.com/database/121/SQLRF/functions028.htm#SQLRF55703)
    - [CLUSTER\_DISTANCE](https://docs.oracle.com/database/121/SQLRF/functions029.htm#SQLRF55712)
    - [CLUSTER\_ID](https://docs.oracle.com/database/121/SQLRF/functions030.htm#SQLRF06213)
    - [CLUSTER\_PROBABILITY](https://docs.oracle.com/database/121/SQLRF/functions031.htm#SQLRF06214)
    - [CLUSTER\_SET](https://docs.oracle.com/database/121/SQLRF/functions032.htm#SQLRF06215)
    - [COALESCE](https://docs.oracle.com/database/121/SQLRF/functions033.htm#SQLRF00617)
    - [COLLECT](https://docs.oracle.com/database/121/SQLRF/functions034.htm#SQLRF06304)
    - [COMPOSE](https://docs.oracle.com/database/121/SQLRF/functions035.htm#SQLRF00618)
    - [CON\_DBID\_TO\_ID](https://docs.oracle.com/database/121/SQLRF/functions036.htm#SQLRF56629)
    - [CON\_GUID\_TO\_ID](https://docs.oracle.com/database/121/SQLRF/functions037.htm#SQLRF56633)
    - [CON\_NAME\_TO\_ID](https://docs.oracle.com/database/121/SQLRF/functions038.htm#SQLRF56637)
    - [CON\_UID\_TO\_ID](https://docs.oracle.com/database/121/SQLRF/functions039.htm#SQLRF56641)
    - [CONCAT](https://docs.oracle.com/database/121/SQLRF/functions040.htm#SQLRF00619)
    - [CONVERT](https://docs.oracle.com/database/121/SQLRF/functions041.htm#SQLRF00620)
    - [CORR](https://docs.oracle.com/database/121/SQLRF/functions042.htm#SQLRF00621)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[CORR\_\*](https://docs.oracle.com/database/121/SQLRF/functions043.htm#SQLRF06314)
      - [CORR\_S](https://docs.oracle.com/database/121/SQLRF/functions043.htm#SQLRF51305)
      - [CORR\_K](https://docs.oracle.com/database/121/SQLRF/functions043.htm#SQLRF51307)
    - [COS](https://docs.oracle.com/database/121/SQLRF/functions044.htm#SQLRF00622)
    - [COSH](https://docs.oracle.com/database/121/SQLRF/functions045.htm#SQLRF00623)
    - [COUNT](https://docs.oracle.com/database/121/SQLRF/functions046.htm#SQLRF00624)
    - [COVAR\_POP](https://docs.oracle.com/database/121/SQLRF/functions047.htm#SQLRF00625)
    - [COVAR\_SAMP](https://docs.oracle.com/database/121/SQLRF/functions048.htm#SQLRF00626)
    - [CUBE\_TABLE](https://docs.oracle.com/database/121/SQLRF/functions049.htm#SQLRF20027)
    - [CUME\_DIST](https://docs.oracle.com/database/121/SQLRF/functions050.htm#SQLRF00627)
    - [CURRENT\_DATE](https://docs.oracle.com/database/121/SQLRF/functions051.htm#SQLRF00628)
    - [CURRENT\_TIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions052.htm#SQLRF00629)
    - [CV](https://docs.oracle.com/database/121/SQLRF/functions053.htm#SQLRF06175)
    - [DATAOBJ\_TO\_MAT\_PARTITION](https://docs.oracle.com/database/121/SQLRF/functions054.htm#SQLRF57050)
    - [DATAOBJ\_TO\_PARTITION](https://docs.oracle.com/database/121/SQLRF/functions055.htm#SQLRF20028)
    - [DBTIMEZONE](https://docs.oracle.com/database/121/SQLRF/functions056.htm#SQLRF00630)
    - [DECODE](https://docs.oracle.com/database/121/SQLRF/functions057.htm#SQLRF00631)
    - [DECOMPOSE](https://docs.oracle.com/database/121/SQLRF/functions058.htm#SQLRF00632)
    - [DELETEXML](https://docs.oracle.com/database/121/SQLRF/functions059.htm#SQLRF06202)
    - [DENSE\_RANK](https://docs.oracle.com/database/121/SQLRF/functions060.htm#SQLRF00633)
    - [DEPTH](https://docs.oracle.com/database/121/SQLRF/functions061.htm#SQLRF06176)
    - [DEREF](https://docs.oracle.com/database/121/SQLRF/functions062.htm#SQLRF00634)
    - [DUMP](https://docs.oracle.com/database/121/SQLRF/functions063.htm#SQLRF00635)
    - [EMPTY\_BLOB, EMPTY\_CLOB](https://docs.oracle.com/database/121/SQLRF/functions064.htm#SQLRF00636)
    - [EXISTSNODE](https://docs.oracle.com/database/121/SQLRF/functions065.htm#SQLRF00637)
    - [EXP](https://docs.oracle.com/database/121/SQLRF/functions066.htm#SQLRF00638)
    - [EXTRACT (datetime)](https://docs.oracle.com/database/121/SQLRF/functions067.htm#SQLRF00639)
    - [EXTRACT (XML)](https://docs.oracle.com/database/121/SQLRF/functions068.htm#SQLRF00640)
    - [EXTRACTVALUE](https://docs.oracle.com/database/121/SQLRF/functions069.htm#SQLRF06173)
    - [FEATURE\_DETAILS](https://docs.oracle.com/database/121/SQLRF/functions070.htm#SQLRF55734)
    - [FEATURE\_ID](https://docs.oracle.com/database/121/SQLRF/functions071.htm#SQLRF06216)
    - [FEATURE\_SET](https://docs.oracle.com/database/121/SQLRF/functions072.htm#SQLRF06217)
    - [FEATURE\_VALUE](https://docs.oracle.com/database/121/SQLRF/functions073.htm#SQLRF06218)
    - [FIRST](https://docs.oracle.com/database/121/SQLRF/functions074.htm#SQLRF00641)
    - [FIRST\_VALUE](https://docs.oracle.com/database/121/SQLRF/functions075.htm#SQLRF00642)
    - [FLOOR](https://docs.oracle.com/database/121/SQLRF/functions076.htm#SQLRF00643)
    - [FROM\_TZ](https://docs.oracle.com/database/121/SQLRF/functions077.htm#SQLRF00644)
    - [GREATEST](https://docs.oracle.com/database/121/SQLRF/functions078.htm#SQLRF00645)
    - [GROUP\_ID](https://docs.oracle.com/database/121/SQLRF/functions079.htm#SQLRF00646)
    - [GROUPING](https://docs.oracle.com/database/121/SQLRF/functions080.htm#SQLRF00647)
    - [GROUPING\_ID](https://docs.oracle.com/database/121/SQLRF/functions081.htm#SQLRF00648)
    - [HEXTORAW](https://docs.oracle.com/database/121/SQLRF/functions082.htm#SQLRF00649)
    - [INITCAP](https://docs.oracle.com/database/121/SQLRF/functions083.htm#SQLRF00650)
    - [INSERTCHILDXML](https://docs.oracle.com/database/121/SQLRF/functions084.htm#SQLRF06203)
    - [INSERTCHILDXMLAFTER](https://docs.oracle.com/database/121/SQLRF/functions085.htm#SQLRF30008)
    - [INSERTCHILDXMLBEFORE](https://docs.oracle.com/database/121/SQLRF/functions086.htm#SQLRF30006)
    - [INSERTXMLAFTER](https://docs.oracle.com/database/121/SQLRF/functions087.htm#SQLRF30010)
    - [INSERTXMLBEFORE](https://docs.oracle.com/database/121/SQLRF/functions088.htm#SQLRF06204)
    - [INSTR](https://docs.oracle.com/database/121/SQLRF/functions089.htm#SQLRF00651)
    - [ITERATION\_NUMBER](https://docs.oracle.com/database/121/SQLRF/functions090.htm#SQLRF06328)
    - [JSON\_QUERY](https://docs.oracle.com/database/121/SQLRF/functions091.htm#SQLRF56718)
    - [JSON\_TABLE](https://docs.oracle.com/database/121/SQLRF/functions092.htm#SQLRF56973)
    - [JSON\_VALUE](https://docs.oracle.com/database/121/SQLRF/functions093.htm#SQLRF56668)
    - [LAG](https://docs.oracle.com/database/121/SQLRF/functions094.htm#SQLRF00652)
    - [LAST](https://docs.oracle.com/database/121/SQLRF/functions095.htm#SQLRF00653)
    - [LAST\_DAY](https://docs.oracle.com/database/121/SQLRF/functions096.htm#SQLRF00654)
    - [LAST\_VALUE](https://docs.oracle.com/database/121/SQLRF/functions097.htm#SQLRF00655)
    - [LEAD](https://docs.oracle.com/database/121/SQLRF/functions098.htm#SQLRF00656)
    - [LEAST](https://docs.oracle.com/database/121/SQLRF/functions099.htm#SQLRF00657)
    - [LENGTH](https://docs.oracle.com/database/121/SQLRF/functions100.htm#SQLRF00658)
    - [LISTAGG](https://docs.oracle.com/database/121/SQLRF/functions101.htm#SQLRF30030)
    - [LN](https://docs.oracle.com/database/121/SQLRF/functions102.htm#SQLRF00659)
    - [LNNVL](https://docs.oracle.com/database/121/SQLRF/functions103.htm#SQLRF06327)
    - [LOCALTIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions104.htm#SQLRF00660)
    - [LOG](https://docs.oracle.com/database/121/SQLRF/functions105.htm#SQLRF00661)
    - [LOWER](https://docs.oracle.com/database/121/SQLRF/functions106.htm#SQLRF00662)
    - [LPAD](https://docs.oracle.com/database/121/SQLRF/functions107.htm#SQLRF00663)
    - [LTRIM](https://docs.oracle.com/database/121/SQLRF/functions108.htm#SQLRF00664)
    - [MAKE\_REF](https://docs.oracle.com/database/121/SQLRF/functions109.htm#SQLRF00665)
    - [MAX](https://docs.oracle.com/database/121/SQLRF/functions110.htm#SQLRF00666)
    - [MEDIAN](https://docs.oracle.com/database/121/SQLRF/functions111.htm#SQLRF06315)
    - [MIN](https://docs.oracle.com/database/121/SQLRF/functions112.htm#SQLRF00667)
    - [MOD](https://docs.oracle.com/database/121/SQLRF/functions113.htm#SQLRF00668)
    - [MONTHS\_BETWEEN](https://docs.oracle.com/database/121/SQLRF/functions114.htm#SQLRF00669)
    - [NANVL](https://docs.oracle.com/database/121/SQLRF/functions115.htm#SQLRF06311)
    - [NCHR](https://docs.oracle.com/database/121/SQLRF/functions116.htm#SQLRF00670)
    - [NEW\_TIME](https://docs.oracle.com/database/121/SQLRF/functions117.htm#SQLRF00671)
    - [NEXT\_DAY](https://docs.oracle.com/database/121/SQLRF/functions118.htm#SQLRF00672)
    - [NLS\_CHARSET\_DECL\_LEN](https://docs.oracle.com/database/121/SQLRF/functions119.htm#SQLRF00673)
    - [NLS\_CHARSET\_ID](https://docs.oracle.com/database/121/SQLRF/functions120.htm#SQLRF00674)
    - [NLS\_CHARSET\_NAME](https://docs.oracle.com/database/121/SQLRF/functions121.htm#SQLRF00675)
    - [NLS\_INITCAP](https://docs.oracle.com/database/121/SQLRF/functions122.htm#SQLRF00676)
    - [NLS\_LOWER](https://docs.oracle.com/database/121/SQLRF/functions123.htm#SQLRF00677)
    - [NLS\_UPPER](https://docs.oracle.com/database/121/SQLRF/functions124.htm#SQLRF00679)
    - [NLSSORT](https://docs.oracle.com/database/121/SQLRF/functions125.htm#SQLRF00678)
    - [NTH\_VALUE](https://docs.oracle.com/database/121/SQLRF/functions126.htm#SQLRF30031)
    - [NTILE](https://docs.oracle.com/database/121/SQLRF/functions127.htm#SQLRF00680)
    - [NULLIF](https://docs.oracle.com/database/121/SQLRF/functions128.htm#SQLRF00681)
    - [NUMTODSINTERVAL](https://docs.oracle.com/database/121/SQLRF/functions129.htm#SQLRF00682)
    - [NUMTOYMINTERVAL](https://docs.oracle.com/database/121/SQLRF/functions130.htm#SQLRF00683)
    - [NVL](https://docs.oracle.com/database/121/SQLRF/functions131.htm#SQLRF00684)
    - [NVL2](https://docs.oracle.com/database/121/SQLRF/functions132.htm#SQLRF00685)
    - [ORA\_DST\_AFFECTED](https://docs.oracle.com/database/121/SQLRF/functions133.htm#SQLRF30032)
    - [ORA\_DST\_CONVERT](https://docs.oracle.com/database/121/SQLRF/functions134.htm#SQLRF30034)
    - [ORA\_DST\_ERROR](https://docs.oracle.com/database/121/SQLRF/functions135.htm#SQLRF30033)
    - [ORA\_HASH](https://docs.oracle.com/database/121/SQLRF/functions136.htm#SQLRF06313)
    - [ORA\_INVOKING\_USER](https://docs.oracle.com/database/121/SQLRF/functions137.htm#SQLRF55902)
    - [ORA\_INVOKING\_USERID](https://docs.oracle.com/database/121/SQLRF/functions138.htm#SQLRF55906)
    - [PATH](https://docs.oracle.com/database/121/SQLRF/functions139.htm#SQLRF06177)
    - [PERCENT\_RANK](https://docs.oracle.com/database/121/SQLRF/functions140.htm#SQLRF00686)
    - [PERCENTILE\_CONT](https://docs.oracle.com/database/121/SQLRF/functions141.htm#SQLRF00687)
    - [PERCENTILE\_DISC](https://docs.oracle.com/database/121/SQLRF/functions142.htm#SQLRF00688)
    - [POWER](https://docs.oracle.com/database/121/SQLRF/functions143.htm#SQLRF00689)
    - [POWERMULTISET](https://docs.oracle.com/database/121/SQLRF/functions144.htm#SQLRF06306)
    - [POWERMULTISET\_BY\_CARDINALITY](https://docs.oracle.com/database/121/SQLRF/functions145.htm#SQLRF06307)
    - [PREDICTION](https://docs.oracle.com/database/121/SQLRF/functions146.htm#SQLRF06219)
    - [PREDICTION\_BOUNDS](https://docs.oracle.com/database/121/SQLRF/functions147.htm#SQLRF20020)
    - [PREDICTION\_COST](https://docs.oracle.com/database/121/SQLRF/functions148.htm#SQLRF06210)
    - [PREDICTION\_DETAILS](https://docs.oracle.com/database/121/SQLRF/functions149.htm#SQLRF06211)
    - [PREDICTION\_PROBABILITY](https://docs.oracle.com/database/121/SQLRF/functions150.htm#SQLRF06212)
    - [PREDICTION\_SET](https://docs.oracle.com/database/121/SQLRF/functions151.htm#SQLRF06233)
    - [PRESENTNNV](https://docs.oracle.com/database/121/SQLRF/functions152.htm#SQLRF06178)
    - [PRESENTV](https://docs.oracle.com/database/121/SQLRF/functions153.htm#SQLRF06179)
    - [PREVIOUS](https://docs.oracle.com/database/121/SQLRF/functions154.htm#SQLRF06180)
    - [RANK](https://docs.oracle.com/database/121/SQLRF/functions155.htm#SQLRF00690)
    - [RATIO\_TO\_REPORT](https://docs.oracle.com/database/121/SQLRF/functions156.htm#SQLRF00691)
    - [RAWTOHEX](https://docs.oracle.com/database/121/SQLRF/functions157.htm#SQLRF00692)
    - [RAWTONHEX](https://docs.oracle.com/database/121/SQLRF/functions158.htm#SQLRF00693)
    - [REF](https://docs.oracle.com/database/121/SQLRF/functions159.htm#SQLRF00694)
    - [REFTOHEX](https://docs.oracle.com/database/121/SQLRF/functions160.htm#SQLRF00695)
    - [REGEXP\_COUNT](https://docs.oracle.com/database/121/SQLRF/functions161.htm#SQLRF20014)
    - [REGEXP\_INSTR](https://docs.oracle.com/database/121/SQLRF/functions162.htm#SQLRF06300)
    - [REGEXP\_REPLACE](https://docs.oracle.com/database/121/SQLRF/functions163.htm#SQLRF06302)
    - [REGEXP\_SUBSTR](https://docs.oracle.com/database/121/SQLRF/functions164.htm#SQLRF06303)
    - [REGR\_ (Linear Regression) Functions](https://docs.oracle.com/database/121/SQLRF/functions165.htm#SQLRF00696)
    - [REMAINDER](https://docs.oracle.com/database/121/SQLRF/functions166.htm#SQLRF06312)
    - [REPLACE](https://docs.oracle.com/database/121/SQLRF/functions167.htm#SQLRF00697)
    - [ROUND (date)](https://docs.oracle.com/database/121/SQLRF/functions168.htm#SQLRF00699)
    - [ROUND (number)](https://docs.oracle.com/database/121/SQLRF/functions169.htm#SQLRF00698)
    - [ROW\_NUMBER](https://docs.oracle.com/database/121/SQLRF/functions170.htm#SQLRF06100)
    - [ROWIDTOCHAR](https://docs.oracle.com/database/121/SQLRF/functions171.htm#SQLRF06101)
    - [ROWIDTONCHAR](https://docs.oracle.com/database/121/SQLRF/functions172.htm#SQLRF06102)
    - [RPAD](https://docs.oracle.com/database/121/SQLRF/functions173.htm#SQLRF06103)
    - [RTRIM](https://docs.oracle.com/database/121/SQLRF/functions174.htm#SQLRF06104)
    - [SCN\_TO\_TIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions175.htm#SQLRF06325)
    - [SESSIONTIMEZONE](https://docs.oracle.com/database/121/SQLRF/functions176.htm#SQLRF06105)
    - [SET](https://docs.oracle.com/database/121/SQLRF/functions177.htm#SQLRF06308)
    - [SIGN](https://docs.oracle.com/database/121/SQLRF/functions178.htm#SQLRF06106)
    - [SIN](https://docs.oracle.com/database/121/SQLRF/functions179.htm#SQLRF06107)
    - [SINH](https://docs.oracle.com/database/121/SQLRF/functions180.htm#SQLRF06108)
    - [SOUNDEX](https://docs.oracle.com/database/121/SQLRF/functions181.htm#SQLRF06109)
    - [SQRT](https://docs.oracle.com/database/121/SQLRF/functions182.htm#SQLRF06110)
    - [STANDARD\_HASH](https://docs.oracle.com/database/121/SQLRF/functions183.htm#SQLRF55647)
    - [STATS\_BINOMIAL\_TEST](https://docs.oracle.com/database/121/SQLRF/functions184.htm#SQLRF06316)
    - [STATS\_CROSSTAB](https://docs.oracle.com/database/121/SQLRF/functions185.htm#SQLRF06317)
    - [STATS\_F\_TEST](https://docs.oracle.com/database/121/SQLRF/functions186.htm#SQLRF06318)
    - [STATS\_KS\_TEST](https://docs.oracle.com/database/121/SQLRF/functions187.htm#SQLRF06319)
    - [STATS\_MODE](https://docs.oracle.com/database/121/SQLRF/functions188.htm#SQLRF06320)
    - [STATS\_MW\_TEST](https://docs.oracle.com/database/121/SQLRF/functions189.htm#SQLRF06321)
    - [STATS\_ONE\_WAY\_ANOVA](https://docs.oracle.com/database/121/SQLRF/functions190.htm#SQLRF06322)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[STATS\_T\_TEST\_\*](https://docs.oracle.com/database/121/SQLRF/functions191.htm#SQLRF06323)
      - [STATS\_T\_TEST\_ONE](https://docs.oracle.com/database/121/SQLRF/functions191.htm#SQLRF51788)
      - [STATS\_T\_TEST\_PAIRED](https://docs.oracle.com/database/121/SQLRF/functions191.htm#SQLRF51790)
      - [STATS\_T\_TEST\_INDEP and STATS\_T\_TEST\_INDEPU](https://docs.oracle.com/database/121/SQLRF/functions191.htm#SQLRF51792)
    - [STATS\_WSR\_TEST](https://docs.oracle.com/database/121/SQLRF/functions192.htm#SQLRF06324)
    - [STDDEV](https://docs.oracle.com/database/121/SQLRF/functions193.htm#SQLRF06111)
    - [STDDEV\_POP](https://docs.oracle.com/database/121/SQLRF/functions194.htm#SQLRF06112)
    - [STDDEV\_SAMP](https://docs.oracle.com/database/121/SQLRF/functions195.htm#SQLRF06113)
    - [SUBSTR](https://docs.oracle.com/database/121/SQLRF/functions196.htm#SQLRF06114)
    - [SUM](https://docs.oracle.com/database/121/SQLRF/functions197.htm#SQLRF06115)
    - [SYS\_CONNECT\_BY\_PATH](https://docs.oracle.com/database/121/SQLRF/functions198.htm#SQLRF06116)
    - [SYS\_CONTEXT](https://docs.oracle.com/database/121/SQLRF/functions199.htm#SQLRF06117)
    - [SYS\_DBURIGEN](https://docs.oracle.com/database/121/SQLRF/functions200.htm#SQLRF06118)
    - [SYS\_EXTRACT\_UTC](https://docs.oracle.com/database/121/SQLRF/functions201.htm#SQLRF06119)
    - [SYS\_GUID](https://docs.oracle.com/database/121/SQLRF/functions202.htm#SQLRF06120)
    - [SYS\_OP\_ZONE\_ID](https://docs.oracle.com/database/121/SQLRF/functions203.htm#SQLRF56848)
    - [SYS\_TYPEID](https://docs.oracle.com/database/121/SQLRF/functions204.htm#SQLRF06121)
    - [SYS\_XMLAGG](https://docs.oracle.com/database/121/SQLRF/functions205.htm#SQLRF06122)
    - [SYS\_XMLGEN](https://docs.oracle.com/database/121/SQLRF/functions206.htm#SQLRF06123)
    - [SYSDATE](https://docs.oracle.com/database/121/SQLRF/functions207.htm#SQLRF06124)
    - [SYSTIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions208.htm#SQLRF06125)
    - [TAN](https://docs.oracle.com/database/121/SQLRF/functions209.htm#SQLRF06126)
    - [TANH](https://docs.oracle.com/database/121/SQLRF/functions210.htm#SQLRF06127)
    - [TIMESTAMP\_TO\_SCN](https://docs.oracle.com/database/121/SQLRF/functions211.htm#SQLRF06326)
    - [TO\_BINARY\_DOUBLE](https://docs.oracle.com/database/121/SQLRF/functions212.htm#SQLRF06309)
    - [TO\_BINARY\_FLOAT](https://docs.oracle.com/database/121/SQLRF/functions213.htm#SQLRF06310)
    - [TO\_BLOB](https://docs.oracle.com/database/121/SQLRF/functions214.htm#SQLRF30029)
    - [TO\_CHAR (character)](https://docs.oracle.com/database/121/SQLRF/functions215.htm#SQLRF06128)
    - [TO\_CHAR (datetime)](https://docs.oracle.com/database/121/SQLRF/functions216.htm#SQLRF06129)
    - [TO\_CHAR (number)](https://docs.oracle.com/database/121/SQLRF/functions217.htm#SQLRF06130)
    - [TO\_CLOB](https://docs.oracle.com/database/121/SQLRF/functions218.htm#SQLRF06131)
    - [TO\_DATE](https://docs.oracle.com/database/121/SQLRF/functions219.htm#SQLRF06132)
    - [TO\_DSINTERVAL](https://docs.oracle.com/database/121/SQLRF/functions220.htm#SQLRF06133)
    - [TO\_LOB](https://docs.oracle.com/database/121/SQLRF/functions221.htm#SQLRF06134)
    - [TO\_MULTI\_BYTE](https://docs.oracle.com/database/121/SQLRF/functions222.htm#SQLRF06135)
    - [TO\_NCHAR (character)](https://docs.oracle.com/database/121/SQLRF/functions223.htm#SQLRF06136)
    - [TO\_NCHAR (datetime)](https://docs.oracle.com/database/121/SQLRF/functions224.htm#SQLRF06137)
    - [TO\_NCHAR (number)](https://docs.oracle.com/database/121/SQLRF/functions225.htm#SQLRF06138)
    - [TO\_NCLOB](https://docs.oracle.com/database/121/SQLRF/functions226.htm#SQLRF06139)
    - [TO\_NUMBER](https://docs.oracle.com/database/121/SQLRF/functions227.htm#SQLRF06140)
    - [TO\_SINGLE\_BYTE](https://docs.oracle.com/database/121/SQLRF/functions228.htm#SQLRF06141)
    - [TO\_TIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions229.htm#SQLRF06142)
    - [TO\_TIMESTAMP\_TZ](https://docs.oracle.com/database/121/SQLRF/functions230.htm#SQLRF06143)
    - [TO\_YMINTERVAL](https://docs.oracle.com/database/121/SQLRF/functions231.htm#SQLRF06144)
    - [TRANSLATE](https://docs.oracle.com/database/121/SQLRF/functions232.htm#SQLRF06145)
    - [TRANSLATE ... USING](https://docs.oracle.com/database/121/SQLRF/functions233.htm#SQLRF06146)
    - [TREAT](https://docs.oracle.com/database/121/SQLRF/functions234.htm#SQLRF06148)
    - [TRIM](https://docs.oracle.com/database/121/SQLRF/functions235.htm#SQLRF06149)
    - [TRUNC (date)](https://docs.oracle.com/database/121/SQLRF/functions236.htm#SQLRF06151)
    - [TRUNC (number)](https://docs.oracle.com/database/121/SQLRF/functions237.htm#SQLRF06150)
    - [TZ\_OFFSET](https://docs.oracle.com/database/121/SQLRF/functions238.htm#SQLRF06152)
    - [UID](https://docs.oracle.com/database/121/SQLRF/functions239.htm#SQLRF06153)
    - [UNISTR](https://docs.oracle.com/database/121/SQLRF/functions240.htm#SQLRF06154)
    - [UPDATEXML](https://docs.oracle.com/database/121/SQLRF/functions241.htm#SQLRF06172)
    - [UPPER](https://docs.oracle.com/database/121/SQLRF/functions242.htm#SQLRF06155)
    - [USER](https://docs.oracle.com/database/121/SQLRF/functions243.htm#SQLRF06156)
    - [USERENV](https://docs.oracle.com/database/121/SQLRF/functions244.htm#SQLRF06157)
    - [VALUE](https://docs.oracle.com/database/121/SQLRF/functions245.htm#SQLRF06158)
    - [VAR\_POP](https://docs.oracle.com/database/121/SQLRF/functions246.htm#SQLRF06159)
    - [VAR\_SAMP](https://docs.oracle.com/database/121/SQLRF/functions247.htm#SQLRF06160)
    - [VARIANCE](https://docs.oracle.com/database/121/SQLRF/functions248.htm#SQLRF06161)
    - [VSIZE](https://docs.oracle.com/database/121/SQLRF/functions249.htm#SQLRF06162)
    - [WIDTH\_BUCKET](https://docs.oracle.com/database/121/SQLRF/functions250.htm#SQLRF06163)
    - [XMLAGG](https://docs.oracle.com/database/121/SQLRF/functions251.htm#SQLRF06165)
    - [XMLCAST](https://docs.oracle.com/database/121/SQLRF/functions252.htm#SQLRF20012)
    - [XMLCDATA](https://docs.oracle.com/database/121/SQLRF/functions253.htm#SQLRF06205)
    - [XMLCOLATTVAL](https://docs.oracle.com/database/121/SQLRF/functions254.htm#SQLRF06166)
    - [XMLCOMMENT](https://docs.oracle.com/database/121/SQLRF/functions255.htm#SQLRF06206)
    - [XMLCONCAT](https://docs.oracle.com/database/121/SQLRF/functions256.htm#SQLRF06167)
    - [XMLDIFF](https://docs.oracle.com/database/121/SQLRF/functions257.htm#SQLRF20025)
    - [XMLELEMENT](https://docs.oracle.com/database/121/SQLRF/functions258.htm#SQLRF06168)
    - [XMLEXISTS](https://docs.oracle.com/database/121/SQLRF/functions259.htm#SQLRF20013)
    - [XMLFOREST](https://docs.oracle.com/database/121/SQLRF/functions260.htm#SQLRF06169)
    - [XMLISVALID](https://docs.oracle.com/database/121/SQLRF/functions261.htm#SQLRF06147)
    - [XMLPARSE](https://docs.oracle.com/database/121/SQLRF/functions262.htm#SQLRF06207)
    - [XMLPATCH](https://docs.oracle.com/database/121/SQLRF/functions263.htm#SQLRF20026)
    - [XMLPI](https://docs.oracle.com/database/121/SQLRF/functions264.htm#SQLRF06208)
    - [XMLQUERY](https://docs.oracle.com/database/121/SQLRF/functions265.htm#SQLRF06209)
    - [XMLROOT](https://docs.oracle.com/database/121/SQLRF/functions266.htm#SQLRF06230)
    - [XMLSEQUENCE](https://docs.oracle.com/database/121/SQLRF/functions267.htm#SQLRF06170)
    - [XMLSERIALIZE](https://docs.oracle.com/database/121/SQLRF/functions268.htm#SQLRF06231)
    - [XMLTABLE](https://docs.oracle.com/database/121/SQLRF/functions269.htm#SQLRF06232)
    - [XMLTRANSFORM](https://docs.oracle.com/database/121/SQLRF/functions270.htm#SQLRF06171)
    - [ROUND and TRUNC Date Functions](https://docs.oracle.com/database/121/SQLRF/functions271.htm#SQLRF52058)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[About User-Defined Functions](https://docs.oracle.com/database/121/SQLRF/functions272.htm#SQLRF06181)
      - [Prerequisites](https://docs.oracle.com/database/121/SQLRF/functions272.htm#SQLRF52062)
      - [Name Precedence](https://docs.oracle.com/database/121/SQLRF/functions272.htm#SQLRF52063)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Common SQL DDL Clauses](https://docs.oracle.com/database/121/SQLRF/clauses.htm#SQLRF021)
    - [allocate\_extent\_clause](https://docs.oracle.com/database/121/SQLRF/clauses001.htm#SQLRF30005)
    - [constraint](https://docs.oracle.com/database/121/SQLRF/clauses002.htm#SQLRF52180)
    - [deallocate\_unused\_clause](https://docs.oracle.com/database/121/SQLRF/clauses003.htm#SQLRF30007)
    - [file\_specification](https://docs.oracle.com/database/121/SQLRF/clauses004.htm#SQLRF01602)
    - [logging\_clause](https://docs.oracle.com/database/121/SQLRF/clauses005.htm#SQLRF30009)
    - [parallel\_clause](https://docs.oracle.com/database/121/SQLRF/clauses006.htm#SQLRF20024)
    - [physical\_attributes\_clause](https://docs.oracle.com/database/121/SQLRF/clauses007.htm#SQLRF30011)
    - [size\_clause](https://docs.oracle.com/database/121/SQLRF/clauses008.htm#SQLRF30012)
    - [storage\_clause](https://docs.oracle.com/database/121/SQLRF/clauses009.htm#SQLRF30013)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Queries and Subqueries](https://docs.oracle.com/database/121/SQLRF/queries.htm#SQLRF007)
    - [About Queries and Subqueries](https://docs.oracle.com/database/121/SQLRF/queries001.htm#SQLRF52327)
    - [Creating Simple Queries](https://docs.oracle.com/database/121/SQLRF/queries002.htm#SQLRF52331)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Hierarchical Queries](https://docs.oracle.com/database/121/SQLRF/queries003.htm#SQLRF52332)
      - [Hierarchical Query Examples](https://docs.oracle.com/database/121/SQLRF/queries003.htm#SQLRF52335)
    - [The UNION \[ALL\], INTERSECT, MINUS Operators](https://docs.oracle.com/database/121/SQLRF/queries004.htm#SQLRF52341)
    - [Sorting Query Results](https://docs.oracle.com/database/121/SQLRF/queries005.htm#SQLRF52348)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Joins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF30046)
      - [Join Conditions](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52349)
      - [Equijoins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52350)
      - [Self Joins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52351)
      - [Cartesian Products](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52352)
      - [Inner Joins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52353)
      - [Outer Joins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52354)
      - [Antijoins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52355)
      - [Semijoins](https://docs.oracle.com/database/121/SQLRF/queries006.htm#SQLRF52356)
    - [Using Subqueries](https://docs.oracle.com/database/121/SQLRF/queries007.htm#SQLRF52357)
    - [Unnesting of Nested Subqueries](https://docs.oracle.com/database/121/SQLRF/queries008.htm#SQLRF52358)
    - [Selecting from the DUAL Table](https://docs.oracle.com/database/121/SQLRF/queries009.htm#SQLRF20036)
    - [Distributed Queries](https://docs.oracle.com/database/121/SQLRF/queries010.htm#SQLRF52359)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: ADMINISTER KEY MANAGEMENT to ALTER JAVA](https://docs.oracle.com/database/121/SQLRF/statements_1.htm#SQLRF008)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Types of SQL Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30001)
      - [Data Definition Language (DDL) Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30041)
      - [Data Manipulation Language (DML) Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30042)
      - [Transaction Control Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30043)
      - [Session Control Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30044)
      - [System Control Statement](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF30045)
      - [Embedded SQL Statements](https://docs.oracle.com/database/121/SQLRF/statements_1001.htm#SQLRF52361)
    - [How the SQL Statement Chapters are Organized](https://docs.oracle.com/database/121/SQLRF/statements_1002.htm#SQLRF52362)
    - [ADMINISTER KEY MANAGEMENT](https://docs.oracle.com/database/121/SQLRF/statements_1003.htm#SQLRF55976)
    - [ALTER AUDIT POLICY (Unified Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_1004.htm#SQLRF56045)
    - [ALTER CLUSTER](https://docs.oracle.com/database/121/SQLRF/statements_1005.htm#SQLRF00801)
    - [ALTER DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_1006.htm#SQLRF00802)
    - [ALTER DATABASE LINK](https://docs.oracle.com/database/121/SQLRF/statements_1007.htm#SQLRF30050)
    - [ALTER DIMENSION](https://docs.oracle.com/database/121/SQLRF/statements_1008.htm#SQLRF00803)
    - [ALTER DISKGROUP](https://docs.oracle.com/database/121/SQLRF/statements_1009.htm#SQLRF01113)
    - [ALTER FLASHBACK ARCHIVE](https://docs.oracle.com/database/121/SQLRF/statements_1010.htm#SQLRF20009)
    - [ALTER FUNCTION](https://docs.oracle.com/database/121/SQLRF/statements_1011.htm#SQLRF00804)
    - [ALTER INDEX](https://docs.oracle.com/database/121/SQLRF/statements_1012.htm#SQLRF00805)
    - [ALTER INDEXTYPE](https://docs.oracle.com/database/121/SQLRF/statements_1013.htm#SQLRF00806)
    - [ALTER JAVA](https://docs.oracle.com/database/121/SQLRF/statements_1014.htm#SQLRF00807)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: ALTER LIBRARY to ALTER SYSTEM](https://docs.oracle.com/database/121/SQLRF/statements_2.htm#SQLRF009)
    - [ALTER LIBRARY](https://docs.oracle.com/database/121/SQLRF/statements_2001.htm#SQLRF00818)
    - [ALTER MATERIALIZED VIEW](https://docs.oracle.com/database/121/SQLRF/statements_2002.htm#SQLRF00808)
    - [ALTER MATERIALIZED VIEW LOG](https://docs.oracle.com/database/121/SQLRF/statements_2003.htm#SQLRF00809)
    - [ALTER MATERIALIZED ZONEMAP](https://docs.oracle.com/database/121/SQLRF/statements_2004.htm#SQLRF56854)
    - [ALTER OPERATOR](https://docs.oracle.com/database/121/SQLRF/statements_2005.htm#SQLRF01112)
    - [ALTER OUTLINE](https://docs.oracle.com/database/121/SQLRF/statements_2006.htm#SQLRF00810)
    - [ALTER PACKAGE](https://docs.oracle.com/database/121/SQLRF/statements_2007.htm#SQLRF00811)
    - [ALTER PLUGGABLE DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_2008.htm#SQLRF55667)
    - [ALTER PROCEDURE](https://docs.oracle.com/database/121/SQLRF/statements_2009.htm#SQLRF00812)
    - [ALTER PROFILE](https://docs.oracle.com/database/121/SQLRF/statements_2010.htm#SQLRF00813)
    - [ALTER RESOURCE COST](https://docs.oracle.com/database/121/SQLRF/statements_2011.htm#SQLRF00814)
    - [ALTER ROLE](https://docs.oracle.com/database/121/SQLRF/statements_2012.htm#SQLRF00815)
    - [ALTER ROLLBACK SEGMENT](https://docs.oracle.com/database/121/SQLRF/statements_2013.htm#SQLRF00816)
    - [ALTER SEQUENCE](https://docs.oracle.com/database/121/SQLRF/statements_2014.htm#SQLRF00817)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[ALTER SESSION](https://docs.oracle.com/database/121/SQLRF/statements_2015.htm#SQLRF00901)
      - [Initialization Parameters and ALTER SESSION](https://docs.oracle.com/database/121/SQLRF/statements_2015.htm#SQLRF53046)
      - [Session Parameters and ALTER SESSION](https://docs.oracle.com/database/121/SQLRF/statements_2015.htm#SQLRF53047)
    - [ALTER SYNONYM](https://docs.oracle.com/database/121/SQLRF/statements_2016.htm#SQLRF56347)
    - [ALTER SYSTEM](https://docs.oracle.com/database/121/SQLRF/statements_2017.htm#SQLRF00902)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: ALTER TABLE to ALTER TABLESPACE](https://docs.oracle.com/database/121/SQLRF/statements_3.htm#SQLRF010)
    - [ALTER TABLE](https://docs.oracle.com/database/121/SQLRF/statements_3001.htm#SQLRF01001)
    - [ALTER TABLESPACE](https://docs.oracle.com/database/121/SQLRF/statements_3002.htm#SQLRF01002)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: ALTER TRIGGER to COMMIT](https://docs.oracle.com/database/121/SQLRF/statements_4.htm#SQLRF011)
    - [ALTER TRIGGER](https://docs.oracle.com/database/121/SQLRF/statements_4001.htm#SQLRF01101)
    - [ALTER TYPE](https://docs.oracle.com/database/121/SQLRF/statements_4002.htm#SQLRF01102)
    - [ALTER USER](https://docs.oracle.com/database/121/SQLRF/statements_4003.htm#SQLRF01103)
    - [ALTER VIEW](https://docs.oracle.com/database/121/SQLRF/statements_4004.htm#SQLRF01104)
    - [ANALYZE](https://docs.oracle.com/database/121/SQLRF/statements_4005.htm#SQLRF01105)
    - [ASSOCIATE STATISTICS](https://docs.oracle.com/database/121/SQLRF/statements_4006.htm#SQLRF01106)
    - [AUDIT (Traditional Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_4007.htm#SQLRF01107)
    - [AUDIT (Unified Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_4008.htm#SQLRF56110)
    - [CALL](https://docs.oracle.com/database/121/SQLRF/statements_4009.htm#SQLRF01108)
    - [COMMENT](https://docs.oracle.com/database/121/SQLRF/statements_4010.htm#SQLRF01109)
    - [COMMIT](https://docs.oracle.com/database/121/SQLRF/statements_4011.htm#SQLRF01110)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: CREATE AUDIT POLICY to CREATE JAVA](https://docs.oracle.com/database/121/SQLRF/statements_5.htm#SQLRF012)
    - [CREATE AUDIT POLICY (Unified Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_5001.htm#SQLRF56055)
    - [CREATE CLUSTER](https://docs.oracle.com/database/121/SQLRF/statements_5002.htm#SQLRF01201)
    - [CREATE CONTEXT](https://docs.oracle.com/database/121/SQLRF/statements_5003.htm#SQLRF01202)
    - [CREATE CONTROLFILE](https://docs.oracle.com/database/121/SQLRF/statements_5004.htm#SQLRF01203)
    - [CREATE DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_5005.htm#SQLRF01204)
    - [CREATE DATABASE LINK](https://docs.oracle.com/database/121/SQLRF/statements_5006.htm#SQLRF01205)
    - [CREATE DIMENSION](https://docs.oracle.com/database/121/SQLRF/statements_5007.htm#SQLRF01206)
    - [CREATE DIRECTORY](https://docs.oracle.com/database/121/SQLRF/statements_5008.htm#SQLRF01207)
    - [CREATE DISKGROUP](https://docs.oracle.com/database/121/SQLRF/statements_5009.htm#SQLRF01114)
    - [CREATE EDITION](https://docs.oracle.com/database/121/SQLRF/statements_5010.htm#SQLRF20017)
    - [CREATE FLASHBACK ARCHIVE](https://docs.oracle.com/database/121/SQLRF/statements_5011.htm#SQLRF20008)
    - [CREATE FUNCTION](https://docs.oracle.com/database/121/SQLRF/statements_5012.htm#SQLRF01208)
    - [CREATE INDEX](https://docs.oracle.com/database/121/SQLRF/statements_5013.htm#SQLRF01209)
    - [CREATE INDEXTYPE](https://docs.oracle.com/database/121/SQLRF/statements_5014.htm#SQLRF01210)
    - [CREATE JAVA](https://docs.oracle.com/database/121/SQLRF/statements_5015.htm#SQLRF01211)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: CREATE LIBRARY to CREATE SPFILE](https://docs.oracle.com/database/121/SQLRF/statements_6.htm#SQLRF013)
    - [CREATE LIBRARY](https://docs.oracle.com/database/121/SQLRF/statements_6001.htm#SQLRF01301)
    - [CREATE MATERIALIZED VIEW](https://docs.oracle.com/database/121/SQLRF/statements_6002.htm#SQLRF01302)
    - [CREATE MATERIALIZED VIEW LOG](https://docs.oracle.com/database/121/SQLRF/statements_6003.htm#SQLRF01303)
    - [CREATE MATERIALIZED ZONEMAP](https://docs.oracle.com/database/121/SQLRF/statements_6004.htm#SQLRF56867)
    - [CREATE OPERATOR](https://docs.oracle.com/database/121/SQLRF/statements_6005.htm#SQLRF01304)
    - [CREATE OUTLINE](https://docs.oracle.com/database/121/SQLRF/statements_6006.htm#SQLRF01305)
    - [CREATE PACKAGE](https://docs.oracle.com/database/121/SQLRF/statements_6007.htm#SQLRF01306)
    - [CREATE PACKAGE BODY](https://docs.oracle.com/database/121/SQLRF/statements_6008.htm#SQLRF01307)
    - [CREATE PFILE](https://docs.oracle.com/database/121/SQLRF/statements_6009.htm#SQLRF01308)
    - [CREATE PLUGGABLE DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_6010.htm#SQLRF55686)
    - [CREATE PROCEDURE](https://docs.oracle.com/database/121/SQLRF/statements_6011.htm#SQLRF01309)
    - [CREATE PROFILE](https://docs.oracle.com/database/121/SQLRF/statements_6012.htm#SQLRF01310)
    - [CREATE RESTORE POINT](https://docs.oracle.com/database/121/SQLRF/statements_6013.htm#SQLRF20001)
    - [CREATE ROLE](https://docs.oracle.com/database/121/SQLRF/statements_6014.htm#SQLRF01311)
    - [CREATE ROLLBACK SEGMENT](https://docs.oracle.com/database/121/SQLRF/statements_6015.htm#SQLRF01312)
    - [CREATE SCHEMA](https://docs.oracle.com/database/121/SQLRF/statements_6016.htm#SQLRF01313)
    - [CREATE SEQUENCE](https://docs.oracle.com/database/121/SQLRF/statements_6017.htm#SQLRF01314)
    - [CREATE SPFILE](https://docs.oracle.com/database/121/SQLRF/statements_6018.htm#SQLRF01315)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: CREATE SYNONYM to CREATE TRIGGER](https://docs.oracle.com/database/121/SQLRF/statements_7.htm#SQLRF014)
    - [CREATE SYNONYM](https://docs.oracle.com/database/121/SQLRF/statements_7001.htm#SQLRF01401)
    - [CREATE TABLE](https://docs.oracle.com/database/121/SQLRF/statements_7002.htm#SQLRF01402)
    - [CREATE TABLESPACE](https://docs.oracle.com/database/121/SQLRF/statements_7003.htm#SQLRF01403)
    - [CREATE TRIGGER](https://docs.oracle.com/database/121/SQLRF/statements_7004.htm#SQLRF01405)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: CREATE TYPE to DROP ROLLBACK SEGMENT](https://docs.oracle.com/database/121/SQLRF/statements_8.htm#SQLRF54727)
    - [CREATE TYPE](https://docs.oracle.com/database/121/SQLRF/statements_8001.htm#SQLRF01506)
    - [CREATE TYPE BODY](https://docs.oracle.com/database/121/SQLRF/statements_8002.htm#SQLRF01502)
    - [CREATE USER](https://docs.oracle.com/database/121/SQLRF/statements_8003.htm#SQLRF01503)
    - [CREATE VIEW](https://docs.oracle.com/database/121/SQLRF/statements_8004.htm#SQLRF01504)
    - [DELETE](https://docs.oracle.com/database/121/SQLRF/statements_8005.htm#SQLRF01505)
    - [DISASSOCIATE STATISTICS](https://docs.oracle.com/database/121/SQLRF/statements_8006.htm#SQLRF01507)
    - [DROP AUDIT POLICY (Unified Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_8007.htm#SQLRF56067)
    - [DROP CLUSTER](https://docs.oracle.com/database/121/SQLRF/statements_8008.htm#SQLRF01511)
    - [DROP CONTEXT](https://docs.oracle.com/database/121/SQLRF/statements_8009.htm#SQLRF01512)
    - [DROP DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_8010.htm#SQLRF01513)
    - [DROP DATABASE LINK](https://docs.oracle.com/database/121/SQLRF/statements_8011.htm#SQLRF01514)
    - [DROP DIMENSION](https://docs.oracle.com/database/121/SQLRF/statements_8012.htm#SQLRF01515)
    - [DROP DIRECTORY](https://docs.oracle.com/database/121/SQLRF/statements_8013.htm#SQLRF01516)
    - [DROP DISKGROUP](https://docs.oracle.com/database/121/SQLRF/statements_8014.htm#SQLRF01517)
    - [DROP EDITION](https://docs.oracle.com/database/121/SQLRF/statements_8015.htm#SQLRF20019)
    - [DROP FLASHBACK ARCHIVE](https://docs.oracle.com/database/121/SQLRF/statements_8016.htm#SQLRF20010)
    - [DROP FUNCTION](https://docs.oracle.com/database/121/SQLRF/statements_8017.htm#SQLRF01518)
    - [DROP INDEX](https://docs.oracle.com/database/121/SQLRF/statements_8018.htm#SQLRF01510)
    - [DROP INDEXTYPE](https://docs.oracle.com/database/121/SQLRF/statements_8019.htm#SQLRF01520)
    - [DROP JAVA](https://docs.oracle.com/database/121/SQLRF/statements_8020.htm#SQLRF01521)
    - [DROP LIBRARY](https://docs.oracle.com/database/121/SQLRF/statements_8021.htm#SQLRF01522)
    - [DROP MATERIALIZED VIEW](https://docs.oracle.com/database/121/SQLRF/statements_8022.htm#SQLRF01523)
    - [DROP MATERIALIZED VIEW LOG](https://docs.oracle.com/database/121/SQLRF/statements_8023.htm#SQLRF01524)
    - [DROP MATERIALIZED ZONEMAP](https://docs.oracle.com/database/121/SQLRF/statements_8024.htm#SQLRF56892)
    - [DROP OPERATOR](https://docs.oracle.com/database/121/SQLRF/statements_8025.htm#SQLRF01525)
    - [DROP OUTLINE](https://docs.oracle.com/database/121/SQLRF/statements_8026.htm#SQLRF01526)
    - [DROP PACKAGE](https://docs.oracle.com/database/121/SQLRF/statements_8027.htm#SQLRF01527)
    - [DROP PLUGGABLE DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_8028.htm#SQLRF55699)
    - [DROP PROCEDURE](https://docs.oracle.com/database/121/SQLRF/statements_8029.htm#SQLRF01528)
    - [DROP PROFILE](https://docs.oracle.com/database/121/SQLRF/statements_8030.htm#SQLRF01529)
    - [DROP RESTORE POINT](https://docs.oracle.com/database/121/SQLRF/statements_8031.htm#SQLRF20002)
    - [DROP ROLE](https://docs.oracle.com/database/121/SQLRF/statements_8032.htm#SQLRF01530)
    - [DROP ROLLBACK SEGMENT](https://docs.oracle.com/database/121/SQLRF/statements_8033.htm#SQLRF01531)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: DROP SEQUENCE to ROLLBACK](https://docs.oracle.com/database/121/SQLRF/statements_9.htm#SQLRF016)
    - [DROP SEQUENCE](https://docs.oracle.com/database/121/SQLRF/statements_9001.htm#SQLRF01804)
    - [DROP SYNONYM](https://docs.oracle.com/database/121/SQLRF/statements_9002.htm#SQLRF01805)
    - [DROP TABLE](https://docs.oracle.com/database/121/SQLRF/statements_9003.htm#SQLRF01806)
    - [DROP TABLESPACE](https://docs.oracle.com/database/121/SQLRF/statements_9004.htm#SQLRF01807)
    - [DROP TRIGGER](https://docs.oracle.com/database/121/SQLRF/statements_9005.htm#SQLRF01808)
    - [DROP TYPE](https://docs.oracle.com/database/121/SQLRF/statements_9006.htm#SQLRF01809)
    - [DROP TYPE BODY](https://docs.oracle.com/database/121/SQLRF/statements_9007.htm#SQLRF01810)
    - [DROP USER](https://docs.oracle.com/database/121/SQLRF/statements_9008.htm#SQLRF01811)
    - [DROP VIEW](https://docs.oracle.com/database/121/SQLRF/statements_9009.htm#SQLRF01812)
    - [EXPLAIN PLAN](https://docs.oracle.com/database/121/SQLRF/statements_9010.htm#SQLRF01601)
    - [EXPLAIN WORK](https://docs.oracle.com/database/121/SQLRF/statements_9011.htm#SQLRF57086)
    - [FLASHBACK DATABASE](https://docs.oracle.com/database/121/SQLRF/statements_9012.htm#SQLRF01801)
    - [FLASHBACK TABLE](https://docs.oracle.com/database/121/SQLRF/statements_9013.htm#SQLRF01802)
    - [GRANT](https://docs.oracle.com/database/121/SQLRF/statements_9014.htm#SQLRF01603)
    - [INSERT](https://docs.oracle.com/database/121/SQLRF/statements_9015.htm#SQLRF01604)
    - [LOCK TABLE](https://docs.oracle.com/database/121/SQLRF/statements_9016.htm#SQLRF01605)
    - [MERGE](https://docs.oracle.com/database/121/SQLRF/statements_9017.htm#SQLRF01606)
    - [NOAUDIT (Traditional Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_9018.htm#SQLRF01607)
    - [NOAUDIT (Unified Auditing)](https://docs.oracle.com/database/121/SQLRF/statements_9019.htm#SQLRF56112)
    - [PURGE](https://docs.oracle.com/database/121/SQLRF/statements_9020.htm#SQLRF01803)
    - [RENAME](https://docs.oracle.com/database/121/SQLRF/statements_9021.htm#SQLRF01608)
    - [REVOKE](https://docs.oracle.com/database/121/SQLRF/statements_9022.htm#SQLRF01609)
    - [ROLLBACK](https://docs.oracle.com/database/121/SQLRF/statements_9023.htm#SQLRF01610)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[SQL Statements: SAVEPOINT to UPDATE](https://docs.oracle.com/database/121/SQLRF/statements_10.htm#SQLRF017)
    - [SAVEPOINT](https://docs.oracle.com/database/121/SQLRF/statements_10001.htm#SQLRF01701)
    - [SELECT](https://docs.oracle.com/database/121/SQLRF/statements_10002.htm#SQLRF01702)
    - [SET CONSTRAINT\[S\]](https://docs.oracle.com/database/121/SQLRF/statements_10003.htm#SQLRF01703)
    - [SET ROLE](https://docs.oracle.com/database/121/SQLRF/statements_10004.htm#SQLRF01704)
    - [SET TRANSACTION](https://docs.oracle.com/database/121/SQLRF/statements_10005.htm#SQLRF01705)
    - [TRUNCATE CLUSTER](https://docs.oracle.com/database/121/SQLRF/statements_10006.htm#SQLRF20029)
    - [TRUNCATE TABLE](https://docs.oracle.com/database/121/SQLRF/statements_10007.htm#SQLRF01707)
    - [UPDATE](https://docs.oracle.com/database/121/SQLRF/statements_10008.htm#SQLRF01708)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[How to Read Syntax Diagrams](https://docs.oracle.com/database/121/SQLRF/ap_syntx.htm#SQLRF018)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Graphic Syntax Diagrams](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55485)
      - [Required Keywords and Parameters](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55489)
      - [Optional Keywords and Parameters](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55492)
      - [Syntax Loops](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55495)
      - [Multipart Diagrams](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55497)
      - [Database Objects](https://docs.oracle.com/database/121/SQLRF/ap_syntx001.htm#SQLRF55499)
    - [Backus-Naur Form Syntax](https://docs.oracle.com/database/121/SQLRF/ap_syntx002.htm#SQLRF55500)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Automatic and Manual Locking Mechanisms During SQL Operations](https://docs.oracle.com/database/121/SQLRF/ap_locks.htm#SQLRF55501)
    - [Automatic Locks in DML Operations](https://docs.oracle.com/database/121/SQLRF/ap_locks001.htm#SQLRF55502)
    - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Automatic Locks in DDL Operations](https://docs.oracle.com/database/121/SQLRF/ap_locks002.htm#SQLRF55509)
      - [Exclusive DDL Locks](https://docs.oracle.com/database/121/SQLRF/ap_locks002.htm#SQLRF55510)
      - [Share DDL Locks](https://docs.oracle.com/database/121/SQLRF/ap_locks002.htm#SQLRF55511)
      - [Breakable Parse Locks](https://docs.oracle.com/database/121/SQLRF/ap_locks002.htm#SQLRF55512)
    - [Manual Data Locking](https://docs.oracle.com/database/121/SQLRF/ap_locks003.htm#SQLRF55513)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Oracle and Standard SQL](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql.htm#SQLRF019)
    - [ANSI Standards](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql001.htm#SQLRF55514)
    - [ISO Standards](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql002.htm#SQLRF55515)
    - [Oracle Compliance To Core SQL:2011](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql003.htm#SQLRF55516)
    - [Oracle Support for Optional Features of SQL/Foundation:2011](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql004.htm#SQLRF55521)
    - [Oracle Compliance with SQL/CLI:2008](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql005.htm#SQLRF55525)
    - [Oracle Compliance with SQL/PSM:2011](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql006.htm#SQLRF55526)
    - [Oracle Compliance with SQL/MED:2008](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql007.htm#SQLRF55527)
    - [Oracle Compliance with SQL/OLB:2008](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql008.htm#SQLRF55528)
    - [Oracle Compliance with SQL/JRT:2008](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql009.htm#SQLRF55578)
    - [Oracle Compliance with SQL/XML:2011](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql010.htm#SQLRF55529)
    - [Oracle Compliance with SQL/RPR:2012](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql011.htm#SQLRF56375)
    - [Oracle Compliance with FIPS 127-2](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql012.htm#SQLRF55535)
    - [Oracle Extensions to Standard SQL](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql013.htm#SQLRF55537)
    - [Oracle Compliance with Older Standards](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql014.htm#SQLRF55538)
    - [Character Set Support](https://docs.oracle.com/database/121/SQLRF/ap_standard_sql015.htm#SQLRF55539)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Oracle Regular Expression Support](https://docs.oracle.com/database/121/SQLRF/ap_posix.htm#SQLRF020)
    - [Multilingual Regular Expression Syntax](https://docs.oracle.com/database/121/SQLRF/ap_posix001.htm#SQLRF55540)
    - [Regular Expression Operator Multilingual Enhancements](https://docs.oracle.com/database/121/SQLRF/ap_posix002.htm#SQLRF55542)
    - [Perl-influenced Extensions in Oracle Regular Expressions](https://docs.oracle.com/database/121/SQLRF/ap_posix003.htm#SQLRF55544)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Oracle SQL Reserved Words and Keywords](https://docs.oracle.com/database/121/SQLRF/ap_keywd.htm#SQLRF022)
    - [Oracle SQL Reserved Words](https://docs.oracle.com/database/121/SQLRF/ap_keywd001.htm#SQLRF55621)
    - [Oracle SQL Keywords](https://docs.oracle.com/database/121/SQLRF/ap_keywd002.htm#SQLRF55622)
  - [![open](https://docs.oracle.com/database/121/dcommon/img/plus.png)](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#)[Extended Examples](https://docs.oracle.com/database/121/SQLRF/ap_examples.htm#SQLRF55546)
    - [Using Extensible Indexing](https://docs.oracle.com/database/121/SQLRF/ap_examples001.htm#SQLRF55547)
    - [Using XML in SQL Statements](https://docs.oracle.com/database/121/SQLRF/ap_examples002.htm#SQLRF55548)
  - [Index](https://docs.oracle.com/database/121/SQLRF/index.htm)

Feedback

×

Subject

From

Anonymous (or [Sign In](http://www.oracle.com/webapps/redirect/signon?nexturl=https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm))

Comments, corrections, and suggestions are forwarded to authors every week. By submitting, you confirm you agree to the [terms and conditions](http://docs.oracle.com/cd/E23003_01/html/en/comment_disclaimer.htm). Use the [OTN forums](https://community.oracle.com/) for product questions. For support or consulting, file a service request through [My Oracle Support](https://support.oracle.com/).

![Submitting..](https://docs.oracle.com/database/121/dcommon/img/ajax-loader.gif)Thank you for your feedback!

Download

×

[PDF](https://docs.oracle.com/database/121/SQLRF/E41329-25.pdf) \- best for offline viewing and printing

Categories

- [Home](https://docs.oracle.com/database/121/index.htm)
- [Master Index](https://docs.oracle.com/database/121/nav/mindx.htm)
- [Error Messages](https://docs.oracle.com/database/121/nav/lookup.htm?id=ERRMG)

12/555

# Data Types

Each value manipulated by Oracle Database has a data type. The data type of a value associates a fixed set of properties with the value. These properties cause Oracle to treat values of one data type differently from values of another. For example, you can add values of `NUMBER` data type, but not values of `RAW` data type.

When you create a table or cluster, you must specify a data type for each of its columns. When you create a procedure or stored function, you must specify a data type for each of its arguments. These data types define the domain of values that each column can contain or each argument can have. For example, `DATE` columns cannot accept the value February 29 (except for a leap year) or the values 2 or 'SHOE'. Each value subsequently placed in a column assumes the data type of the column. For example, if you insert `'01-JAN-98'` into a `DATE` column, then Oracle treats the `'01-JAN-98'` character string as a `DATE` value after verifying that it translates to a valid date.

Oracle Database provides a number of built-in data types as well as several categories for user-defined types that can be used as data types. The syntax of Oracle data types appears in the diagrams that follow. The text of this section is divided into the following sections:

- [Oracle Built-in Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54330)

- [ANSI, DB2, and SQL/DS Data Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54335)

- [User-Defined Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i46376)

- [Oracle-Supplied Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54873)

- [Data Type Comparison Rules](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#i55214)

- [Data Conversion](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#i46862)


A data type is either scalar or nonscalar. A scalar type contains an atomic value, whereas a nonscalar (sometimes called a "collection") contains a set of values. A large object (LOB) is a special form of scalar data type representing a large scalar value of binary or character data. LOBs are subject to some restrictions that do not affect other scalar types because of their size. Those restrictions are documented in the context of the relevant SQL syntax.

See Also:

["Restrictions on LOB Columns"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABHIJHI)

The Oracle precompilers recognize other data types in embedded SQL programs. These data types are called external data types and are associated with host variables. Do not confuse built-in data types and user-defined types with external data types. For information on external data types, including how Oracle converts between them and built-in data types or user-defined types, see [Pro\*COBOL Programmer's Guide](https://docs.oracle.com/database/121/LNPCB/toc.htm), and [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/database/121/LNPCC/toc.htm).

datatypes::=

![Description of datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/datatypes.gif)

[Description of the illustration ''datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/datatypes.htm)

The Oracle built-in data types appear in the figures that follows. For descriptions, refer to ["Oracle Built-in Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54330).

Oracle\_built\_in\_datatypes::=

![Description of oracle_built_in_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/oracle_built_in_datatypes.gif)

[Description of the illustration ''oracle\_built\_in\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/oracle_built_in_datatypes.htm)

character\_datatypes::=

![Description of character_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/character_datatypes.gif)

[Description of the illustration ''character\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/character_datatypes.htm)

number\_datatypes::=

![Description of number_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/number_datatypes.gif)

[Description of the illustration ''number\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/number_datatypes.htm)

long\_and\_raw\_datatypes::=

![Description of long_and_raw_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/long_and_raw_datatypes.gif)

[Description of the illustration ''long\_and\_raw\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/long_and_raw_datatypes.htm)

datetime\_datatypes::=

![Description of datetime_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/datetime_datatypes.gif)

[Description of the illustration ''datetime\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/datetime_datatypes.htm)

large\_object\_datatypes::=

![Description of large_object_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/large_object_datatypes.gif)

[Description of the illustration ''large\_object\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/large_object_datatypes.htm)

rowid\_datatypes::=

![Description of rowid_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/rowid_datatypes.gif)

[Description of the illustration ''rowid\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/rowid_datatypes.htm)

The ANSI-supported data types appear in the figure that follows. ["ANSI, DB2, and SQL/DS Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54335) discusses the mapping of ANSI-supported data types to Oracle built-in data types.

ANSI\_supported\_datatypes::=

![Description of ansi_supported_datatypes.gif follows](https://docs.oracle.com/database/121/SQLRF/img/ansi_supported_datatypes.gif)

[Description of the illustration ''ansi\_supported\_datatypes.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/ansi_supported_datatypes.htm)

For descriptions of user-defined types, refer to ["User-Defined Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i46376).

The Oracle-supplied data types appear in the figures that follows. For descriptions, refer to ["Oracle-Supplied Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i54873).

Oracle\_supplied\_types::=

![Description of oracle_supplied_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/oracle_supplied_types.gif)

[Description of the illustration ''oracle\_supplied\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/oracle_supplied_types.htm)

any\_types::=

![Description of any_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/any_types.gif)

[Description of the illustration ''any\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/any_types.htm)

For descriptions of the `Any` types, refer to ["Any Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i107578).

XML\_types::=

![Description of xml_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/xml_types.gif)

[Description of the illustration ''xml\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/xml_types.htm)

For descriptions of the XML types, refer to ["XML Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i160550).

spatial\_types::=

![Description of spatial_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/spatial_types.gif)

[Description of the illustration ''spatial\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/spatial_types.htm)

For descriptions of the spatial types, refer to ["Spatial Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i107588).

media\_types::=

![Description of media_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/media_types.gif)

[Description of the illustration ''media\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/media_types.htm)

still\_image\_object\_types::=

![Description of still_image_object_types.gif follows](https://docs.oracle.com/database/121/SQLRF/img/still_image_object_types.gif)

[Description of the illustration ''still\_image\_object\_types.gif''](https://docs.oracle.com/database/121/SQLRF/img_text/still_image_object_types.htm)

For descriptions of the media types, refer to ["Media Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i121058).

## Oracle Built-in Data Types

The table that follows summarizes Oracle built-in data types. Refer to the syntax in the preceding sections for the syntactic elements. The codes listed for the data types are used internally by Oracle Database. The data type code of a column or object attribute is returned by the `DUMP` function.

Table 2-1 Built-in Data Type Summary

| Code | Data Type | Description |
| --- | --- | --- |
| 1 | `VARCHAR2`(`size` \[`BYTE` \| `CHAR`\]) | Variable-length character string having maximum length `size` bytes or characters. You must specify `size` for `VARCHAR2`. Minimum `size` is 1 byte or 1 character. Maximum size is:<br>- 32767 bytes or characters if `MAX_STRING_SIZE``=``EXTENDED`<br>  <br>- 4000 bytes or characters if `MAX_STRING_SIZE``=``STANDARD`<br>  <br>Refer to ["Extended Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABCIGGA) for more information on the `MAX_STRING_SIZE` initialization parameter.<br>`BYTE` indicates that the column will have byte length semantics. `CHAR` indicates that the column will have character semantics. |
| 1 | `NVARCHAR2`(`size`) | Variable-length Unicode character string having maximum length `size` characters. You must specify `size` for `NVARCHAR2`. The number of bytes can be up to two times `size` for `AL16UTF16` encoding and three times `size` for `UTF8` encoding. Maximum `size` is determined by the national character set definition, with an upper limit of:<br>- 32767 bytes if `MAX_STRING_SIZE``=``EXTENDED`<br>  <br>- 4000 bytes if `MAX_STRING_SIZE``=``STANDARD`<br>  <br>Refer to ["Extended Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABCIGGA) for more information on the `MAX_STRING_SIZE` initialization parameter. |
| 2 | `NUMBER` \[ (`p` \[, `s`\]) \] | Number having precision `p` and scale `s`. The precision `p` can range from 1 to 38. The scale `s` can range from -84 to 127. Both precision and scale are in decimal digits. A `NUMBER` value requires from 1 to 22 bytes. |
| 2 | `FLOAT` \[(`p`)\] | A subtype of the `NUMBER` data type having precision `p`. A `FLOAT` value is represented internally as `NUMBER`. The precision `p` can range from 1 to 126 binary digits. A `FLOAT` value requires from 1 to 22 bytes. |
| 8 | `LONG` | Character data of variable length up to 2 gigabytes, or 231 -1 bytes. Provided for backward compatibility. |
| 12 | `DATE` | Valid date range from January 1, 4712 BC, to December 31, 9999 AD. The default format is determined explicitly by the `NLS_DATE_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is fixed at 7 bytes. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, and `SECOND`. It does not have fractional seconds or a time zone. |
| 100 | `BINARY_FLOAT` | 32-bit floating point number. This data type requires 4 bytes. |
| 101 | `BINARY_DOUBLE` | 64-bit floating point number. This data type requires 8 bytes. |
| 180 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] | Year, month, and day values of date, as well as hour, minute, and second values of time, where `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` datetime field. Accepted values of `fractional_seconds_precision` are 0 to 9. The default is 6. The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is 7 or 11 bytes, depending on the precision. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, and `SECOND`. It contains fractional seconds but does not have a time zone. |
| 181 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] `WITH``TIME``ZONE` | All values of `TIMESTAMP` as well as time zone displacement value, where `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` datetime field. Accepted values are 0 to 9. The default is 6. The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is fixed at 13 bytes. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `TIMEZONE_HOUR`, and `TIMEZONE_MINUTE`. It has fractional seconds and an explicit time zone. |
| 231 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] `WITH``LOCAL``TIME``ZONE` | All values of `TIMESTAMP``WITH``TIME``ZONE`, with the following exceptions:<br>- Data is normalized to the database time zone when it is stored in the database.<br>  <br>- When the data is retrieved, users see the data in the session time zone.<br>  <br>The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is 7 or 11 bytes, depending on the precision. |
| 182 | `INTERVAL``YEAR` \[(`year_precision`)\] `TO``MONTH` | Stores a period of time in years and months, where `year_precision` is the number of digits in the `YEAR` datetime field. Accepted values are 0 to 9. The default is 2. The size is fixed at 5 bytes. |
| 183 | `INTERVAL``DAY` \[(`day_precision`)\] `TO``SECOND` \[(`fractional_seconds_precision`)\] | Stores a period of time in days, hours, minutes, and seconds, where<br>- `day_precision` is the maximum number of digits in the `DAY` datetime field. Accepted values are 0 to 9. The default is 2.<br>  <br>- `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` field. Accepted values are 0 to 9. The default is 6.<br>  <br>The size is fixed at 11 bytes. |
| 23 | `RAW`(`size`) | Raw binary data of length `size` bytes. You must specify `size` for a `RAW` value. Maximum `size` is:<br>- 32767 bytes if `MAX_STRING_SIZE``=``EXTENDED`<br>  <br>- 2000 bytes if `MAX_STRING_SIZE``=``STANDARD`<br>  <br>Refer to ["Extended Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABCIGGA) for more information on the `MAX_STRING_SIZE` initialization parameter. |
| 24 | `LONG RAW` | Raw binary data of variable length up to 2 gigabytes. |
| 69 | `ROWID` | Base 64 string representing the unique address of a row in its table. This data type is primarily for values returned by the `ROWID` pseudocolumn. |
| 208 | `UROWID` \[(`size`)\] | Base 64 string representing the logical address of a row of an index-organized table. The optional `size` is the size of a column of type `UROWID`. The maximum size and default is 4000 bytes. |
| 96 | `CHAR` \[(`size` \[`BYTE` \| `CHAR`\])\] | Fixed-length character data of length `size` bytes or characters. Maximum `size` is 2000 bytes or characters. Default and minimum `size` is 1 byte.<br>`BYTE` and `CHAR` have the same semantics as for `VARCHAR2`. |
| 96 | `NCHAR`\[(`size`)\] | Fixed-length character data of length `size` characters. The number of bytes can be up to two times `size` for `AL16UTF16` encoding and three times `size` for `UTF8` encoding. Maximum `size` is determined by the national character set definition, with an upper limit of 2000 bytes. Default and minimum `size` is 1 character. |
| 112 | `CLOB` | A character large object containing single-byte or multibyte characters. Both fixed-width and variable-width character sets are supported, both using the database character set. Maximum size is (4 gigabytes - 1) \* (database block size). |
| 112 | `NCLOB` | A character large object containing Unicode characters. Both fixed-width and variable-width character sets are supported, both using the database national character set. Maximum size is (4 gigabytes - 1) \* (database block size). Stores national character set data. |
| 113 | `BLOB` | A binary large object. Maximum size is (4 gigabytes - 1) \* (database block size). |
| 114 | `BFILE` | Contains a locator to a large binary file stored outside the database. Enables byte stream I/O access to external LOBs residing on the database server. Maximum size is 4 gigabytes. |

The sections that follow describe the Oracle data types as they are stored in Oracle Database. For information on specifying these data types as literals, refer to ["Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i11223).

Character Data Types

Character data types store character (alphanumeric) data, which are words and free-form text, in the database character set or national character set. They are less restrictive than other data types and consequently have fewer properties. For example, character columns can store all alphanumeric values, but `NUMBER` columns can store only numeric values.

Character data is stored in strings with byte values corresponding to one of the character sets, such as 7-bit ASCII or EBCDIC, specified when the database was created. Oracle Database supports both single-byte and multibyte character sets.

These data types are used for character data:

- [CHAR Data Type](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i45647)

- [NCHAR Data Type](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i45672)

- [VARCHAR2 Data Type](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i45694)

- [NVARCHAR2 Data Type](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i45685)


For information on specifying character data types as literals, refer to ["Text Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i42617).

### CHAR Data Type

The `CHAR` data type specifies a fixed-length character string in the database character set. You specify the database character set when you create your database.

When you create a table with a `CHAR` column, you specify the column length as `size` optionally followed by a length qualifier. The qualifier `BYTE` denotes byte length semantics while the qualifier `CHAR` denotes character length semantics. In the byte length semantics, `size` is the number of bytes to store in the column. In the character length semantics, `size` is the number of code points in the database character set to store in the column. A code point may have from 1 to 4 bytes depending on the database character set and the particular character encoded by the code point. Oracle recommends that you specify one of the length qualifiers to explicitly document the desired length semantics of the column. If you do not specify a qualifier, the value of the `NLS_LENGTH_SEMANTICS` parameter of the session creating the column defines the length semantics, unless the table belongs to the schema `SYS`, in which case the default semantics is `BYTE`.

Oracle ensures that all values stored in a `CHAR` column have the length specified by `size` in the selected length semantics. If you insert a value that is shorter than the column length, then Oracle blank-pads the value to column length. If you try to insert a value that is too long for the column, then Oracle returns an error. Note that if the column length is expressed in characters (code points), blank-padding does not guarantee that all column values have the same byte length.

You can omit `size` from the column definition. The default value is 1.

The maximum value of `size` is 2000, which means 2000 bytes or characters (code points), depending on the selected length semantics. However, independently, the absolute maximum length of any character value that can be stored into a `CHAR` column is 2000 bytes. For example, even if you define the column length to be 2000 characters, Oracle returns an error if you try to insert a 2000-character value in which one or more code points are wider than 1 byte. The value of `size` in characters is a length constraint, not guaranteed capacity. If you want a `CHAR` column to be always able to store `size` characters in any database character set, use a value of `size` that is less than or equal to 500.

To ensure proper data conversion between databases and clients with different character sets, you must ensure that `CHAR` data consists of well-formed strings.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch2charset.htm#NLSPG002) for more information on character set support and ["Data Type Comparison Rules"](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#i55214) for information on comparison semantics

### NCHAR Data Type

The `NCHAR` data type specifies a fixed-length character string in the national character set. You specify the national character set as either AL16UTF16 or UTF8 when you create your database. AL16UTF16 and UTF8 are two encoding forms of the Unicode character set (UTF-16 and CESU-8, correspondingly) and hence `NCHAR` is a Unicode-only data type.

When you create a table with an `NCHAR` column, you specify the column length as `size` characters, or more precisely, code points in the national character set. One code point has always 2 bytes in AL16UTF16 and from 1 to 3 bytes in UTF8, depending on the particular character encoded by the code point.

Oracle ensures that all values stored in an `NCHAR` column have the length of `size` characters. If you insert a value that is shorter than the column length, then Oracle blank-pads the value to the column length. If you try to insert a value that is too long for the column, then Oracle returns an error. Note that if the national character set is UTF8, blank-padding does not guarantee that all column values have the same byte length.

You can omit `size` from the column definition. The default value is 1.

The maximum value of `size` is 1000 characters when the national character set is AL16UTF16, and 2000 characters when the national character set is UTF8. However, independently, the absolute maximum length of any character value that can be stored into an `NCHAR` column is 2000 bytes. For example, even if you define the column length to be 1000 characters, Oracle returns an error if you try to insert a 1000-character value but the national character set is UTF8 and all code points are 3 bytes wide. The value of `size` is a length constraint, not guaranteed capacity. If you want an `NCHAR` column to be always able to store `size` characters in both national character sets, use a value of `size` that is less than or equal to 666.

To ensure proper data conversion between databases and clients with different character sets, you must ensure that `NCHAR` data consists of well-formed strings.

If you assign a `CHAR` value to an `NCHAR` column, the value is implicitly converted from the database character set to the national character set. If you assign an `NCHAR` value to a `CHAR` column, the value is implicitly converted from the national character set to the database character set. If some of the characters from the `NCHAR` value cannot be represented in the database character set, then if the value of the session parameter `NLS_NCHAR_CONV_EXCP` is `TRUE`, then Oracle reports an error. If the value of the parameter is `FALSE`, non-representable characters are replaced with the default replacement character of the database character set, which is usually the question mark '?' or the inverted question mark '¿'.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch6unicode.htm#NLSPG006) for information on Unicode data type support

### VARCHAR2 Data Type

The `VARCHAR2` data type specifies a variable-length character string in the database character set. You specify the database character set when you create your database.

When you create a table with a `VARCHAR2` column, you must specify the column length as `size` optionally followed by a length qualifier. The qualifier `BYTE` denotes byte length semantics while the qualifier `CHAR` denotes character length semantics. In the byte length semantics, `size` is the maximum number of bytes that can be stored in the column. In the character length semantics, `size` is the maximum number of code points in the database character set that can be stored in the column. A code point may have from 1 to 4 bytes depending on the database character set and the particular character encoded by the code point. Oracle recommends that you specify one of the length qualifiers to explicitly document the desired length semantics of the column. If you do not specify a qualifier, the value of the `NLS_LENGTH_SEMANTICS` parameter of the session creating the column defines the length semantics, unless the table belongs to the schema `SYS`, in which case the default semantics is `BYTE`.

Oracle stores a character value in a `VARCHAR2` column exactly as you specify it, without any blank-padding, provided the value does not exceed the length of the column. If you try to insert a value that exceeds the specified length, then Oracle returns an error.

The minimum value of `size` is 1. The maximum value is:

- 32767 if `MAX_STRING_SIZE``=``EXTENDED`

- 4000 if `MAX_STRING_SIZE``=``STANDARD`


Refer to ["Extended Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABCIGGA) for more information on the `MAX_STRING_SIZE` initialization parameter and the internal storage mechanisms for extended data types.

While `size` may be expressed in bytes or characters (code points) the independent absolute maximum length of any character value that can be stored into a `VARCHAR2` column is 32767 or 4000 bytes, depending on `MAX_STRING_SIZE`. For example, even if you define the column length to be 32767 characters, Oracle returns an error if you try to insert a 32767-character value in which one or more code points are wider than 1 byte. The value of `size` in characters is a length constraint, not guaranteed capacity. If you want a `VARCHAR2` column to be always able to store `size` characters in any database character set, use a value of `size` that is less than or equal to 8191, if `MAX_STRING_SIZE` = `EXTENDED`, or 1000, if `MAX_STRING_SIZE` = `STANDARD`.

Oracle compares `VARCHAR2` values using non-padded comparison semantics.

To ensure proper data conversion between databases with different character sets, you must ensure that `VARCHAR2` data consists of well-formed strings. See [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch2charset.htm#NLSPG002) for more information on character set support.

See Also:

["Data Type Comparison Rules"](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#i55214) for information on comparison semantics

### VARCHAR Data Type

Do not use the `VARCHAR` data type. Use the `VARCHAR2` data type instead. Although the `VARCHAR` data type is currently synonymous with `VARCHAR2`, the `VARCHAR` data type is scheduled to be redefined as a separate data type used for variable-length character strings compared with different comparison semantics.

### NVARCHAR2 Data Type

The `NVARCHAR2` data type specifies a variable-length character string in the national character set. You specify the national character set as either AL16UTF16 or UTF8 when you create your database. AL16UTF16 and UTF8 are two encoding forms of the Unicode character set (UTF-16 and CESU-8, correspondingly) and hence `NVARCHAR2` is a Unicode-only data type.

When you create a table with an `NVARCHAR2` column, you must specify the column length as `size` characters, or more precisely, code points in the national character set. One code point has always 2 bytes in AL16UTF16 and from 1 to 3 bytes in UTF8, depending on the particular character encoded by the code point.

Oracle stores a character value in an `NVARCHAR2` column exactly as you specify it, without any blank-padding, provided the value does not exceed the length of the column. If you try to insert a value that exceeds the specified length, then Oracle returns an error.

The minimum value of `size` is 1. The maximum value is:

- 16383 if `MAX_STRING_SIZE``=``EXTENDED` and the national character set is AL16UTF16

- 32767 if `MAX_STRING_SIZE``=``EXTENDED` and the national character set is UTF8

- 2000 if `MAX_STRING_SIZE``=``STANDARD` and the national character set is AL16UTF16

- 4000 if `MAX_STRING_SIZE``=``STANDARD` and the national character set is UTF8


Refer to ["Extended Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABCIGGA) for more information on the `MAX_STRING_SIZE` initialization parameter and the internal storage mechanisms for extended data types.

Independently of the maximum column length in characters, the absolute maximum length of any value that can be stored into an `NVARCHAR2` column is 32767 or 4000 bytes, depending on `MAX_STRING_SIZE`. For example, even if you define the column length to be 16383 characters, Oracle returns an error if you try to insert a 16383-character value but the national character set is UTF8 and all code points are 3 bytes wide. The value of `size` is a length constraint, not guaranteed capacity. If you want an `NVARCHAR2` column to be always able to store `size` characters in both national character sets, use a value of `size` that is less than or equal to 10922, if `MAX_STRING_SIZE` = `EXTENDED`, or 1333, if `MAX_STRING_SIZE` = `STANDARD`.

Oracle compares `NVARCHAR2` values using non-padded comparison semantics.

To ensure proper data conversion between databases and clients with different character sets, you must ensure that `NVARCHAR2` data consists of well-formed strings.

If you assign a `VARCHAR2` value to an `NVARCHAR2` column, the value is implicitly converted from the database character set to the national character set. If you assign an `NVARCHAR2` value to a `VARCHAR2` column, the value is implicitly converted from the national character set to the database character set. If some of the characters from the `NVARCHAR2` value cannot be represented in the database character set, then if the value of the session parameter `NLS_NCHAR_CONV_EXCP` is `TRUE`, then Oracle reports an error. If the value of the parameter is `FALSE`, non-representable characters are replaced with the default replacement character of the database character set, which is usually the question mark '?' or the inverted question mark '¿'.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch6unicode.htm#NLSPG006) for information on Unicode data type support and ["Data Type Comparison Rules"](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#i55214) for information on comparison semantics

Numeric Data Types

The Oracle Database numeric data types store positive and negative fixed and floating-point numbers, zero, infinity, and values that are the undefined result of an operation—"not a number" or `NAN`. For information on specifying numeric data types as literals, refer to ["Numeric Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i139891).

### NUMBER Data Type

The `NUMBER` data type stores zero as well as positive and negative fixed numbers with absolute values from 1.0 x 10-130 to but not including 1.0 x 10126. If you specify an arithmetic expression whose value has an absolute value greater than or equal to 1.0 x 10126, then Oracle returns an error. Each `NUMBER` value requires from 1 to 22 bytes.

Specify a fixed-point number using the following form:

```
NUMBER(p,s)
```

where:

- `p` is the precision, or the maximum number of significant decimal digits, where the most significant digit is the left-most nonzero digit, and the least significant digit is the right-most known digit. Oracle guarantees the portability of numbers with precision of up to 20 base-100 digits, which is equivalent to 39 or 40 decimal digits depending on the position of the decimal point.

- `s` is the scale, or the number of digits from the decimal point to the least significant digit. The scale can range from -84 to 127.
  - Positive scale is the number of significant digits to the right of the decimal point to and including the least significant digit.

  - Negative scale is the number of significant digits to the left of the decimal point, to but not including the least significant digit. For negative scale the least significant digit is on the left side of the decimal point, because the actual data is rounded to the specified number of places to the left of the decimal point. For example, a specification of (10,-2) means to round to hundreds.

Scale can be greater than precision, most commonly when `e` notation is used. When scale is greater than precision, the precision specifies the maximum number of significant digits to the right of the decimal point. For example, a column defined as `NUMBER(4,5)` requires a zero for the first digit after the decimal point and rounds all values past the fifth digit after the decimal point.

It is good practice to specify the scale and precision of a fixed-point number column for extra integrity checking on input. Specifying scale and precision does not force all values to a fixed length. If a value exceeds the precision, then Oracle returns an error. If a value exceeds the scale, then Oracle rounds it.

Specify an integer using the following form:

```
NUMBER(p)
```

This represents a fixed-point number with precision `p` and scale 0 and is equivalent to `NUMBER(p,0)`.

Specify a floating-point number using the following form:

```
NUMBER
```

The absence of precision and scale designators specifies the maximum range and precision for an Oracle number.

See Also:

["Floating-Point Numbers"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i140176)

[Table 2-2](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#g196646) show how Oracle stores data using different precisions and scales.

Table 2-2 Storage of Scale and Precision

| Actual Data | Specified As | Stored As |
| --- | --- | --- |
| 123.89 | `NUMBER` | 123.89 |
| 123.89 | `NUMBER(3)` | 124 |
| 123.89 | `NUMBER(3,2)` | exceeds precision |
| 123.89 | `NUMBER(4,2)` | exceeds precision |
| 123.89 | `NUMBER(5,2)` | 123.89 |
| 123.89 | `NUMBER(6,1)` | 123.9 |
| 123.89 | `NUMBER(6,-2)` | 100 |
| .01234 | `NUMBER(4,5)` | .01234 |
| .00012 | `NUMBER(4,5)` | .00012 |
| .000127 | `NUMBER(4,5)` | .00013 |
| .0000012 | `NUMBER(2,7)` | .0000012 |
| .00000123 | `NUMBER(2,7)` | .0000012 |
| 1.2e-4 | `NUMBER(2,5)` | 0.00012 |
| 1.2e-5 | `NUMBER(2,5)` | 0.00001 |

### FLOAT Data Type

The `FLOAT` data type is a subtype of `NUMBER`. It can be specified with or without precision, which has the same definition it has for `NUMBER` and can range from 1 to 126. Scale cannot be specified, but is interpreted from the data. Each `FLOAT` value requires from 1 to 22 bytes.

To convert from binary to decimal precision, multiply `n` by 0.30103. To convert from decimal to binary precision, multiply the decimal precision by 3.32193. The maximum of 126 digits of binary precision is roughly equivalent to 38 digits of decimal precision.

The difference between `NUMBER` and `FLOAT` is best illustrated by example. In the following example the same values are inserted into `NUMBER` and `FLOAT` columns:

```
CREATE TABLE test (col1 NUMBER(5,2), col2 FLOAT(5));

INSERT INTO test VALUES (1.23, 1.23);
INSERT INTO test VALUES (7.89, 7.89);
INSERT INTO test VALUES (12.79, 12.79);
INSERT INTO test VALUES (123.45, 123.45);

SELECT * FROM test;

      COL1       COL2
---------- ----------
      1.23        1.2
      7.89        7.9
     12.79         13
    123.45        120
```

In this example, the `FLOAT` value returned cannot exceed 5 binary digits. The largest decimal number that can be represented by 5 binary digits is 31. The last row contains decimal values that exceed 31. Therefore, the `FLOAT` value must be truncated so that its significant digits do not require more than 5 binary digits. Thus 123.45 is rounded to 120, which has only two significant decimal digits, requiring only 4 binary digits.

Oracle Database uses the Oracle `FLOAT` data type internally when converting ANSI `FLOAT` data. Oracle `FLOAT` is available for you to use, but Oracle recommends that you use the `BINARY_FLOAT` and `BINARY_DOUBLE` data types instead, as they are more robust. Refer to ["Floating-Point Numbers"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i140176) for more information.

### Floating-Point Numbers

Floating-point numbers can have a decimal point anywhere from the first to the last digit or can have no decimal point at all. An exponent may optionally be used following the number to increase the range, for example, 1.777 e-20. A scale value is not applicable to floating-point numbers, because the number of digits that can appear after the decimal point is not restricted.

Binary floating-point numbers differ from `NUMBER` in the way the values are stored internally by Oracle Database. Values are stored using decimal precision for `NUMBER`. All literals that are within the range and precision supported by `NUMBER` are stored exactly as `NUMBER`. Literals are stored exactly because literals are expressed using decimal precision (the digits 0 through 9). Binary floating-point numbers are stored using binary precision (the digits 0 and 1). Such a storage scheme cannot represent all values using decimal precision exactly. Frequently, the error that occurs when converting a value from decimal to binary precision is undone when the value is converted back from binary to decimal precision. The literal 0.1 is such an example.

Oracle Database provides two numeric data types exclusively for floating-point numbers:

#### BINARY\_FLOAT

`BINARY_FLOAT` is a 32-bit, single-precision floating-point number data type. Each `BINARY_FLOAT` value requires 4 bytes.

#### BINARY\_DOUBLE

`BINARY_DOUBLE` is a 64-bit, double-precision floating-point number data type. Each `BINARY_DOUBLE` value requires 8 bytes.

In a `NUMBER` column, floating point numbers have decimal precision. In a `BINARY_FLOAT` or `BINARY_DOUBLE` column, floating-point numbers have binary precision. The binary floating-point numbers support the special values infinity and `NaN` (not a number).

You can specify floating-point numbers within the limits listed in [Table 2-3](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#g195556). The format for specifying floating-point numbers is defined in ["Numeric Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i139891).

Table 2-3 Floating Point Number Limits

| Value | BINARY\_FLOAT | BINARY\_DOUBLE |
| --- | --- | --- |
| Maximum positive finite value | 3.40282E+38F | 1.79769313486231E+308 |
| Minimum positive finite value | 1.17549E-38F | 2.22507485850720E-308 |

IEEE754 Conformance The Oracle implementation of floating-point data types conforms substantially with the Institute of Electrical and Electronics Engineers (IEEE) Standard for Binary Floating-Point Arithmetic, IEEE Standard 754-1985 (IEEE754). The floating-point data types conform to IEEE754 in the following areas:

- The SQL function `SQRT` implements square root. See [SQRT](https://docs.oracle.com/database/121/SQLRF/functions182.htm#i1009289).

- The SQL function `REMAINDER` implements remainder. See [REMAINDER](https://docs.oracle.com/database/121/SQLRF/functions166.htm#i1300767).

- Arithmetic operators conform. See ["Arithmetic Operators"](https://docs.oracle.com/database/121/SQLRF/operators002.htm#i1028549).

- Comparison operators conform, except for comparisons with `NaN`. Oracle orders `NaN` greatest with respect to all other values, and evaluates `NaN` equal to `NaN`. See ["Floating-Point Conditions"](https://docs.oracle.com/database/121/SQLRF/conditions003.htm#i1052323).

- Conversion operators conform. See ["Conversion Functions"](https://docs.oracle.com/database/121/SQLRF/functions002.htm#i88892).

- The default rounding mode is supported.

- The default exception handling mode is supported.

- The special values `INF`, -`INF`, and `NaN` are supported. See ["Floating-Point Conditions"](https://docs.oracle.com/database/121/SQLRF/conditions003.htm#i1052323).

- Rounding of `BINARY_FLOAT` and `BINARY_DOUBLE` values to integer-valued `BINARY_FLOAT` and `BINARY_DOUBLE` values is provided by the SQL functions `ROUND`, `TRUNC`, `CEIL`, and `FLOOR`.

- Rounding of `BINARY_FLOAT`/`BINARY_DOUBLE` to decimal and decimal to `BINARY_FLOAT`/`BINARY_DOUBLE` is provided by the SQL functions `TO_CHAR`, `TO_NUMBER`, `TO_NCHAR`, `TO_BINARY_FLOAT`, `TO_BINARY_DOUBLE`, and `CAST`.


The floating-point data types do not conform to IEEE754 in the following areas:

- -0 is coerced to +0.

- Comparison with `NaN` is not supported.

- All `NaN` values are coerced to either `BINARY_FLOAT_NAN` or `BINARY_DOUBLE_NAN`.

- Non-default rounding modes are not supported.

- Non-default exception handling mode are not supported.


### Numeric Precedence

Numeric precedence determines, for operations that support numeric data types, the data type Oracle uses if the arguments to the operation have different data types. `BINARY_DOUBLE` has the highest numeric precedence, followed by `BINARY_FLOAT`, and finally by `NUMBER`. Therefore, in any operation on multiple numeric values:

- If any of the operands is `BINARY_DOUBLE`, then Oracle attempts to convert all the operands implicitly to `BINARY_DOUBLE` before performing the operation.

- If none of the operands is `BINARY_DOUBLE` but any of the operands is `BINARY_FLOAT`, then Oracle attempts to convert all the operands implicitly to `BINARY_FLOAT` before performing the operation.

- Otherwise, Oracle attempts to convert all the operands to `NUMBER` before performing the operation.


If any implicit conversion is needed and fails, then the operation fails. Refer to [Table 2-10, "Implicit Type Conversion Matrix"](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm#g195937) for more information on implicit conversion.

In the context of other data types, numeric data types have lower precedence than the datetime/interval data types and higher precedence than character and all other data types.

LONG Data Type

Do not create tables with `LONG` columns. Use LOB columns (`CLOB`, `NCLOB`, `BLOB`) instead. `LONG` columns are supported only for backward compatibility.

`LONG` columns store variable-length character strings containing up to 2 gigabytes -1, or 231-1 bytes. `LONG` columns have many of the characteristics of `VARCHAR2` columns. You can use `LONG` columns to store long text strings. The length of `LONG` values may be limited by the memory available on your computer. `LONG` literals are formed as described for ["Text Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i42617).

Oracle also recommends that you convert existing `LONG` columns to LOB columns. LOB columns are subject to far fewer restrictions than `LONG` columns. Further, LOB functionality is enhanced in every release, whereas `LONG` functionality has been static for several releases. See the `modify_col_properties` clause of [ALTER TABLE](https://docs.oracle.com/database/121/SQLRF/statements_3001.htm#CJAHHIBI) and [TO\_LOB](https://docs.oracle.com/database/121/SQLRF/functions221.htm#i79464) for more information on converting `LONG` columns to LOB.

You can reference `LONG` columns in SQL statements in these places:

- `SELECT` lists

- `SET` clauses of `UPDATE` statements

- `VALUES` clauses of `INSERT` statements


The use of `LONG` values is subject to these restrictions:

- A table can contain only one `LONG` column.

- You cannot create an object type with a `LONG` attribute.

- `LONG` columns cannot appear in `WHERE` clauses or in integrity constraints (except that they can appear in `NULL` and `NOT``NULL` constraints).

- `LONG` columns cannot be indexed.

- `LONG` data cannot be specified in regular expressions.

- A stored function cannot return a `LONG` value.

- You can declare a variable or argument of a PL/SQL program unit using the `LONG` data type. However, you cannot then call the program unit from SQL.

- Within a single SQL statement, all `LONG` columns, updated tables, and locked tables must be located on the same database.

- `LONG` and `LONG``RAW` columns cannot be used in distributed SQL statements and cannot be replicated.

- If a table has both `LONG` and LOB columns, then you cannot bind more than 4000 bytes of data to both the `LONG` and LOB columns in the same SQL statement. However, you can bind more than 4000 bytes of data to either the `LONG` or the LOB column.


In addition, `LONG` columns cannot appear in these parts of SQL statements:

- `GROUP``BY` clauses, `ORDER``BY` clauses, or `CONNECT``BY` clauses or with the `DISTINCT` operator in `SELECT` statements

- The `UNIQUE` operator of a `SELECT` statement

- The column list of a `CREATE``CLUSTER` statement

- The `CLUSTER` clause of a `CREATE``MATERIALIZED``VIEW` statement

- SQL built-in functions, expressions, or conditions

- `SELECT` lists of queries containing `GROUP``BY` clauses

- `SELECT` lists of subqueries or queries combined by the `UNION`, `INTERSECT`, or `MINUS` set operators

- `SELECT` lists of `CREATE``TABLE` ... `AS``SELECT` statements

- `ALTER``TABLE` ... `MOVE` statements

- `SELECT` lists in subqueries in `INSERT` statements


Triggers can use the `LONG` data type in the following manner:

- A SQL statement within a trigger can insert data into a `LONG` column.

- If data from a `LONG` column can be converted to a constrained data type (such as `CHAR` and `VARCHAR2`), then a `LONG` column can be referenced in a SQL statement within a trigger.

- Variables in triggers cannot be declared using the `LONG` data type.

- :`NEW` and :`OLD` cannot be used with `LONG` columns.


You can use Oracle Call Interface functions to retrieve a portion of a `LONG` value from the database.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/database/121/LNOCI/oci03typ.htm#LNOCI16272)

Datetime and Interval Data Types

The datetime data types are `DATE`, `TIMESTAMP`, `TIMESTAMP``WITH``TIME``ZONE`, and `TIMESTAMP``WITH``LOCAL``TIME``ZONE`. Values of datetime data types are sometimes called datetimes. The interval data types are `INTERVAL``YEAR``TO``MONTH` and `INTERVAL``DAY``TO``SECOND`. Values of interval data types are sometimes called intervals. For information on expressing datetime and interval values as literals, refer to ["Datetime Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#BABGIGCJ) and ["Interval Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i38598).

Both datetimes and intervals are made up of fields. The values of these fields determine the value of the data type. [Table 2-4](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABFDAEI) lists the datetime fields and their possible values for datetimes and intervals.

To avoid unexpected results in your DML operations on datetime data, you can verify the database and session time zones by querying the built-in SQL functions `DBTIMEZONE` and `SESSIONTIMEZONE`. If the time zones have not been set manually, then Oracle Database uses the operating system time zone by default. If the operating system time zone is not a valid Oracle time zone, then Oracle uses UTC as the default value.

Table 2-4 Datetime Fields and Values

| Datetime Field | Valid Values for Datetime | Valid Values for INTERVAL |
| --- | --- | --- |
| `YEAR` | -4712 to 9999 (excluding year 0) | Any positive or negative integer |
| `MONTH` | 01 to 12 | 0 to 11 |
| `DAY` | 01 to 31 (limited by the values of `MONTH` and `YEAR`, according to the rules of the current NLS calendar parameter) | Any positive or negative integer |
| `HOUR` | 00 to 23 | 0 to 23 |
| `MINUTE` | 00 to 59 | 0 to 59 |
| `SECOND` | 00 to 59.9(n), where 9(n) is the precision of time fractional seconds. The 9(n) portion is not applicable for `DATE`. | 0 to 59.9(n), where 9(n) is the precision of interval fractional seconds |
| `TIMEZONE_HOUR` | -12 to 14 (This range accommodates daylight saving time changes.) Not applicable for `DATE` or `TIMESTAMP`. | Not applicable |
| `TIMEZONE_MINUTE`<br>(See note at end of table) | 00 to 59. Not applicable for `DATE` or `TIMESTAMP`. | Not applicable |
| `TIMEZONE_REGION` | Query the `TZNAME` column of the `V$TIMEZONE_NAMES` data dictionary view. Not applicable for `DATE` or `TIMESTAMP`. For a complete listing of all time zone region names, refer to [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch4datetime.htm#NLSPG004). | Not applicable |
| `TIMEZONE_ABBR` | Query the `TZABBREV` column of the `V$TIMEZONE_NAMES` data dictionary view. Not applicable for `DATE` or `TIMESTAMP`. | Not applicable |

Note:

`TIMEZONE_HOUR` and `TIMEZONE_MINUTE` are specified together and interpreted as an entity in the format `+`\|`-``hh``:``mi`, with values ranging from -12:59 to +14:00. Refer to [Oracle Data Provider for .NET Developer's Guide for Microsoft Windows](https://docs.oracle.com/database/121/ODPNT/OracleTimeStampStructure.htm#ODPNT0002) for information on specifying time zone values for that API.

### DATE Data Type

The `DATE` data type stores date and time information. Although date and time information can be represented in both character and number data types, the `DATE` data type has special associated properties. For each `DATE` value, Oracle stores the following information: year, month, day, hour, minute, and second.

You can specify a `DATE` value as a literal, or you can convert a character or numeric value to a date value with the `TO_DATE` function. For examples of expressing `DATE` values in both these ways, refer to ["Datetime Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#BABGIGCJ).

#### Using Julian Days

A Julian day number is the number of days since January 1, 4712 BC. Julian days allow continuous dating from a common reference. You can use the date format model "J" with date functions `TO_DATE` and `TO_CHAR` to convert between Oracle `DATE` values and their Julian equivalents.

Note:

Oracle Database uses the astronomical system of calculating Julian days, in which the year 4713 BC is specified as -4712. The historical system of calculating Julian days, in contrast, specifies 4713 BC as -4713. If you are comparing Oracle Julian days with values calculated using the historical system, then take care to allow for the 365-day difference in BC dates. For more information, see `http://aa.usno.navy.mil/faq/docs/millennium.php`.

The default date values are determined as follows:

- The year is the current year, as returned by `SYSDATE`.

- The month is the current month, as returned by `SYSDATE`.

- The day is 01 (the first day of the month).

- The hour, minute, and second are all 0.


These default values are used in a query that requests date values where the date itself is not specified, as in the following example, which is issued in the month of May:

```
SELECT TO_DATE('2009', 'YYYY')
  FROM DUAL;

TO_DATE('
---------
01-MAY-09
```

Example This statement returns the Julian equivalent of January 1, 2009:

```
SELECT TO_CHAR(TO_DATE('01-01-2009', 'MM-DD-YYYY'),'J')
    FROM DUAL;

TO_CHAR
-------
2454833
```

See Also:

["Selecting from the DUAL Table"](https://docs.oracle.com/database/121/SQLRF/queries009.htm#i2054159) for a description of the `DUAL` table

### TIMESTAMP Data Type

The `TIMESTAMP` data type is an extension of the `DATE` data type. It stores the year, month, and day of the `DATE` data type, plus hour, minute, and second values. This data type is useful for storing precise time values and for collecting and evaluating date information across geographic regions. Specify the `TIMESTAMP` data type as follows:

```
TIMESTAMP [(fractional_seconds_precision)]
```

where `fractional_seconds_precision` optionally specifies the number of digits Oracle stores in the fractional part of the `SECOND` datetime field. When you create a column of this data type, the value can be a number in the range 0 to 9. The default is 6.

See Also:

[TO\_TIMESTAMP](https://docs.oracle.com/database/121/SQLRF/functions229.htm#i999843) for information on converting character data to `TIMESTAMP` data

### TIMESTAMP WITH TIME ZONE Data Type

`TIMESTAMP``WITH``TIME``ZONE` is a variant of `TIMESTAMP` that includes a time zone region name or a time zone offset in its value. The time zone offset is the difference (in hours and minutes) between local time and UTC (Coordinated Universal Time—formerly Greenwich Mean Time). This data type is useful for preserving local time zone information.

Specify the `TIMESTAMP``WITH``TIME``ZONE` data type as follows:

```
TIMESTAMP [(fractional_seconds_precision)] WITH TIME ZONE
```

where `fractional_seconds_precision` optionally specifies the number of digits Oracle stores in the fractional part of the `SECOND` datetime field. When you create a column of this data type, the value can be a number in the range 0 to 9. The default is 6.

Oracle time zone data is derived from the public domain information available at `http://www.iana.org/time-zones/`. Oracle time zone data may not reflect the most recent data available at this site.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch4datetime.htm#NLSPG004) for more information on Oracle time zone data

- ["Support for Daylight Saving Times"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i51607) and [Table 2-17, "Matching Character Data and Format Models with the FX Format Model Modifier"](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#g195443) for information on daylight saving support

- [TO\_TIMESTAMP\_TZ](https://docs.oracle.com/database/121/SQLRF/functions230.htm#i999847) for information on converting character data to `TIMESTAMP``WITH``TIME``ZONE` data

- [ALTER SESSION](https://docs.oracle.com/database/121/SQLRF/statements_2015.htm#i2231814) for information on the `ERROR_ON_OVERLAP_TIME` session parameter


### TIMESTAMP WITH LOCAL TIME ZONE Data Type

`TIMESTAMP``WITH``LOCAL``TIME``ZONE` is another variant of `TIMESTAMP` that is sensitive to time zone information. It differs from `TIMESTAMP``WITH``TIME``ZONE` in that data stored in the database is normalized to the database time zone, and the time zone information is not stored as part of the column data. When a user retrieves the data, Oracle returns it in the user's local session time zone. This data type is useful for date information that is always to be displayed in the time zone of the client system in a two-tier application.

Specify the `TIMESTAMP``WITH``LOCAL``TIME``ZONE` data type as follows:

```
TIMESTAMP [(fractional_seconds_precision)] WITH LOCAL TIME ZONE
```

where `fractional_seconds_precision` optionally specifies the number of digits Oracle stores in the fractional part of the `SECOND` datetime field. When you create a column of this data type, the value can be a number in the range 0 to 9. The default is 6.

Oracle time zone data is derived from the public domain information available at `http://www.iana.org/time-zones/`. Oracle time zone data may not reflect the most recent data available at this site.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch4datetime.htm#NLSPG004) for more information on Oracle time zone data

- [Oracle Database Development Guide](https://docs.oracle.com/database/121/ADFNS/adfns_sqltypes.htm#ADFNS00304) for examples of using this data type and [CAST](https://docs.oracle.com/database/121/SQLRF/functions024.htm#i1269136) for information on converting character data to `TIMESTAMP``WITH``LOCAL``TIME``ZONE`


### INTERVAL YEAR TO MONTH Data Type

`INTERVAL``YEAR``TO``MONTH` stores a period of time using the `YEAR` and `MONTH` datetime fields. This data type is useful for representing the difference between two datetime values when only the year and month values are significant.

Specify `INTERVAL``YEAR``TO``MONTH` as follows:

```
INTERVAL YEAR [(year_precision)] TO MONTH
```

where `year_precision` is the number of digits in the `YEAR` datetime field. The default value of `year_precision` is 2.

You have a great deal of flexibility when specifying interval values as literals. Refer to ["Interval Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i38598) for detailed information on specifying interval values as literals. Also see ["Datetime and Interval Examples"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABBICGH) for an example using intervals.

### INTERVAL DAY TO SECOND Data Type

`INTERVAL``DAY``TO``SECOND` stores a period of time in terms of days, hours, minutes, and seconds. This data type is useful for representing the precise difference between two datetime values.

Specify this data type as follows:

```
INTERVAL DAY [(day_precision)]
   TO SECOND [(fractional_seconds_precision)]
```

where

- `day_precision` is the number of digits in the `DAY` datetime field. Accepted values are 0 to 9. The default is 2.

- `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` datetime field. Accepted values are 0 to 9. The default is 6.


You have a great deal of flexibility when specifying interval values as literals. Refer to ["Interval Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i38598) for detailed information on specify interval values as literals. Also see ["Datetime and Interval Examples"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABBICGH) for an example using intervals.

### Datetime/Interval Arithmetic

You can perform a number of arithmetic operations on date (`DATE`), timestamp (`TIMESTAMP`, `TIMESTAMP``WITH``TIME``ZONE`, and `TIMESTAMP``WITH``LOCAL``TIME``ZONE`) and interval (`INTERVAL``DAY``TO``SECOND` and `INTERVAL``YEAR``TO``MONTH`) data. Oracle calculates the results based on the following rules:

- You can use `NUMBER` constants in arithmetic operations on date and timestamp values, but not interval values. Oracle internally converts timestamp values to date values and interprets `NUMBER` constants in arithmetic datetime and interval expressions as numbers of days. For example, `SYSDATE` \+ 1 is tomorrow. `SYSDATE` \- 7 is one week ago. `SYSDATE` \+ (10/1440) is ten minutes from now. Subtracting the `hire_date` column of the sample table `employees` from `SYSDATE` returns the number of days since each employee was hired. You cannot multiply or divide date or timestamp values.

- Oracle implicitly converts `BINARY_FLOAT` and `BINARY_DOUBLE` operands to `NUMBER`.

- Each `DATE` value contains a time component, and the result of many date operations include a fraction. This fraction means a portion of one day. For example, 1.5 days is 36 hours. These fractions are also returned by Oracle built-in functions for common operations on `DATE` data. For example, the `MONTHS_BETWEEN` function returns the number of months between two dates. The fractional portion of the result represents that portion of a 31-day month.

- If one operand is a `DATE` value or a numeric value, neither of which contains time zone or fractional seconds components, then:
  - Oracle implicitly converts the other operand to `DATE` data. The exception is multiplication of a numeric value times an interval, which returns an interval.

  - If the other operand has a time zone value, then Oracle uses the session time zone in the returned value.

  - If the other operand has a fractional seconds value, then the fractional seconds value is lost.
- When you pass a timestamp, interval, or numeric value to a built-in function that was designed only for the `DATE` data type, Oracle implicitly converts the non-`DATE` value to a `DATE` value. Refer to ["Datetime Functions"](https://docs.oracle.com/database/121/SQLRF/functions002.htm#i88891) for information on which functions cause implicit conversion to `DATE`.

- When interval calculations return a datetime value, the result must be an actual datetime value or the database returns an error. For example, the next two statements return errors:


```
SELECT TO_DATE('31-AUG-2004','DD-MON-YYYY') + TO_YMINTERVAL('0-1')
    FROM DUAL;

SELECT TO_DATE('29-FEB-2004','DD-MON-YYYY') + TO_YMINTERVAL('1-0')
    FROM DUAL;
```


The first fails because adding one month to a 31-day month would result in September 31, which is not a valid date. The second fails because adding one year to a date that exists only every four years is not valid. However, the next statement succeeds, because adding four years to a February 29 date is valid:


```
SELECT TO_DATE('29-FEB-2004', 'DD-MON-YYYY') + TO_YMINTERVAL('4-0')
    FROM DUAL;

TO_DATE('
  ---------
29-FEB-08
```

- Oracle performs all timestamp arithmetic in UTC time. For `TIMESTAMP``WITH``LOCAL``TIME``ZONE`, Oracle converts the datetime value from the database time zone to UTC and converts back to the database time zone after performing the arithmetic. For `TIMESTAMP``WITH``TIME``ZONE`, the datetime value is always in UTC, so no conversion is necessary.


[Table 2-5](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#g196492) is a matrix of datetime arithmetic operations. Dashes represent operations that are not supported.

Table 2-5 Matrix of Datetime Arithmetic

| Operand & Operator | DATE | TIMESTAMP | INTERVAL | Numeric |
| --- | --- | --- | --- | --- |
| DATE |  |  |  |  |
| + | `—` | `—` | `DATE` | `DATE` |
| - | `NUMBER` | `INTERVAL` | `DATE` | `DATE` |
| \* | `—` | `—` | `—` | `—` |
| / | `—` | `—` | `—` | `—` |
| TIMESTAMP |  |  |  |  |
| + | `—` | `—` | `TIMESTAMP` | `DATE` |
| - | `INTERVAL` | `INTERVAL` | `TIMESTAMP` | `DATE` |
| \* | `—` | `—` | `—` | `—` |
| / | `—` | `—` | `—` | `—` |
| INTERVAL |  |  |  |  |
| + | `DATE` | `TIMESTAMP` | `INTERVAL` | `—` |
| - | `—` | `—` | `INTERVAL` | `—` |
| \* | `—` | `—` | `—` | `INTERVAL` |
| / | `—` | `—` | `—` | `INTERVAL` |
| Numeric |  |  |  |  |
| + | `DATE` | `DATE` | `—` | `NA` |
| - | `—` | `—` | `—` | `NA` |
| \* | `—` | `—` | `INTERVAL` | `NA` |
| / | `—` | `—` | `—` | `NA` |

Examples You can add an interval value expression to a start time. Consider the sample table `oe.orders` with a column `order_date`. The following statement adds 30 days to the value of the `order_date` column:

```
SELECT order_id, order_date + INTERVAL '30' DAY AS "Due Date"
  FROM orders
  ORDER BY order_id, "Due Date";
```

### Support for Daylight Saving Times

Oracle Database automatically determines, for any given time zone region, whether daylight saving is in effect and returns local time values accordingly. The datetime value is sufficient for Oracle to determine whether daylight saving time is in effect for a given region in all cases except boundary cases. A boundary case occurs during the period when daylight saving goes into or comes out of effect. For example, in the US-Pacific region, when daylight saving goes into effect, the time changes from 2:00 a.m. to 3:00 a.m. The one hour interval between 2 and 3 a.m. does not exist. When daylight saving goes out of effect, the time changes from 2:00 a.m. back to 1:00 a.m., and the one-hour interval between 1 and 2 a.m. is repeated.

To resolve these boundary cases, Oracle uses the `TZR` and `TZD` format elements, as described in [Table 2-17](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#g195443). `TZR` represents the time zone region name in datetime input strings. Examples are '`Australia/North`', '`UTC`', and '`Singapore`'. `TZD` represents an abbreviated form of the time zone region name with daylight saving information. Examples are '`PST`' for US/Pacific standard time and '`PDT`' for US/Pacific daylight time. To see a listing of valid values for the `TZR` and `TZD` format elements, query the `TZNAME` and `TZABBREV` columns of the `V$TIMEZONE_NAMES` dynamic performance view.

Note:

Time zone region names are needed by the daylight saving feature. These names are stored in two types of time zone files: one large and one small. One of these files is the default file, depending on your environment and the release of Oracle Database you are using. For more information regarding time zone files and names, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/applocaledata.htm#NLSPG014).

For a complete listing of the time zone region names in both files, refer to [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/applocaledata.htm#NLSPG0141).

Oracle time zone data is derived from the public domain information available at `http://www.iana.org/time-zones/`. Oracle time zone data may not reflect the most recent data available at this site.

See Also:

- ["Datetime Format Models"](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#i34924) for information on the format elements and the session parameter [ERROR\_ON\_OVERLAP\_TIME](https://docs.oracle.com/database/121/SQLRF/statements_2015.htm#i2252050).

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch4datetime.htm#NLSPG004) for more information on Oracle time zone data

- [Oracle Database Reference](https://docs.oracle.com/database/121/REFRN/GUID-6AB7E3F0-C345-46A4-9558-3F4F60CCC2F3.htm#REFRN30290) for information on the dynamic performance views


### Datetime and Interval Examples

The following example shows how to specify some datetime and interval data types.

```
CREATE TABLE time_table
  (start_time    TIMESTAMP,
   duration_1    INTERVAL DAY (6) TO SECOND (5),
   duration_2    INTERVAL YEAR TO MONTH);
```

The `start_time` column is of type `TIMESTAMP`. The implicit fractional seconds precision of `TIMESTAMP` is 6.

The `duration_1` column is of type `INTERVAL``DAY``TO``SECOND`. The maximum number of digits in field `DAY` is 6 and the maximum number of digits in the fractional second is 5. The maximum number of digits in all other datetime fields is 2.

The `duration_2` column is of type `INTERVAL``YEAR``TO``MONTH`. The maximum number of digits of the value in each field (`YEAR` and `MONTH`) is 2.

Interval data types do not have format models. Therefore, to adjust their presentation, you must combine character functions such as `EXTRACT` and concatenate the components. For example, the following examples query the `hr.employees` and `oe.orders` tables, respectively, and change interval output from the form "yy-mm" to "yy years mm months" and from "dd-hh" to "dddd days hh hours":

```
SELECT last_name, EXTRACT(YEAR FROM (SYSDATE - hire_date) YEAR TO MONTH)
       || ' years '
       || EXTRACT(MONTH FROM (SYSDATE - hire_date) YEAR TO MONTH)
       || ' months'  "Interval"
  FROM employees;

LAST_NAME                 Interval
------------------------- --------------------
OConnell                  2 years 3 months
Grant                     1 years 9 months
Whalen                    6 years 1 months
Hartstein                 5 years 8 months
Fay                       4 years 2 months
Mavris                    7 years 4 months
Baer                      7 years 4 months
Higgins                   7 years 4 months
Gietz                     7 years 4 months
. . .

SELECT order_id, EXTRACT(DAY FROM (SYSDATE - order_date) DAY TO SECOND)
       || ' days '
       || EXTRACT(HOUR FROM (SYSDATE - order_date) DAY TO SECOND)
       || ' hours' "Interval"
  FROM orders;

  ORDER_ID Interval
---------- --------------------
      2458 780 days 23 hours
      2397 685 days 22 hours
      2454 733 days 21 hours
      2354 447 days 20 hours
      2358 635 days 20 hours
      2381 508 days 18 hours
      2440 765 days 17 hours
      2357 1365 days 16 hours
      2394 602 days 15 hours
      2435 763 days 15 hours
. . .
```

### RAW and LONG RAW Data Types

The `RAW` and `LONG``RAW` data types store data that is not to be explicitly converted by Oracle Database when moving data between different systems. These data types are intended for binary data or byte strings. For example, you can use `LONG``RAW` to store graphics, sound, documents, or arrays of binary data, for which the interpretation is dependent on the use.

Oracle strongly recommends that you convert `LONG``RAW` columns to binary LOB (`BLOB`) columns. LOB columns are subject to far fewer restrictions than `LONG` columns. See [TO\_LOB](https://docs.oracle.com/database/121/SQLRF/functions221.htm#i79464) for more information.

`RAW` is a variable-length data type like `VARCHAR2`, except that Oracle Net (which connects client software to a database or one database to another) and the Oracle import and export utilities do not perform character conversion when transmitting `RAW` or `LONG``RAW` data. In contrast, Oracle Net and the Oracle import and export utilities automatically convert `CHAR`, `VARCHAR2`, and `LONG` data between different database character sets, if data is transported between databases, or between the database character set and the client character set, if data is transported between a database and a client. The client character set is determined by the type of the client interface, such as OCI or JDBC, and the client configuration (for example, the `NLS_LANG` environment variable).

When Oracle implicitly converts `RAW` or `LONG``RAW` data to character data, the resulting character value contains a hexadecimal representation of the binary input, where each character is a hexadecimal digit (`0`-`9`, `A`-`F`) representing four consecutive bits of `RAW` data. For example, one byte of `RAW` data with bits 11001011 becomes the value `CB`.

When Oracle implicitly converts character data to `RAW` or `LONG``RAW`, it interprets each consecutive input character as a hexadecimal representation of four consecutive bits of binary data and builds the resulting `RAW` or `LONG``RAW` value by concatenating those bits. If any of the input characters is not a hexadecimal digit (`0`-`9`, `A`-`F`, `a`-`f`), then an error is reported. If the number of characters is odd, then the result is undefined.

The SQL functions `RAWTOHEX` and `HEXTORAW` perform explicit conversions that are equivalent to the above implicit conversions. Other types of conversions between `RAW` and character data are possible with functions in the Oracle-supplied PL/SQL packages `UTL_RAW` and `UTL_I18N`.

Large Object (LOB) Data Types

The built-in LOB data types `BLOB`, `CLOB`, and `NCLOB` (stored internally) and `BFILE` (stored externally) can store large and unstructured data such as text, image, video, and spatial data. The size of `BLOB`, `CLOB`, and `NCLOB` data can be up to (232-1 bytes) \* (the value of the `CHUNK` parameter of LOB storage). If the tablespaces in your database are of standard block size, and if you have used the default value of the `CHUNK` parameter of LOB storage when creating a LOB column, then this is equivalent to (232-1 bytes) \* (database block size). `BFILE` data can be up to 264-1 bytes, although your operating system may impose restrictions on this maximum.

When creating a table, you can optionally specify different tablespace and storage characteristics for LOB columns or LOB object attributes from those specified for the table.

`CLOB`, `NCLOB`, and `BLOB` values up to approximately 4000 bytes are stored inline if you enable storage in row at the time the LOB column is created. LOBs greater than 4000 bytes are always stored externally. Refer to [ENABLE STORAGE IN ROW](https://docs.oracle.com/database/121/SQLRF/statements_7002.htm#BABHDBGB) for more information.

LOB columns contain LOB locators that can refer to internal (in the database) or external (outside the database) LOB values. Selecting a LOB from a table actually returns the LOB locator and not the entire LOB value. The `DBMS_LOB` package and Oracle Call Interface (OCI) operations on LOBs are performed through these locators.

LOBs are similar to `LONG` and `LONG``RAW` types, but differ in the following ways:

- LOBs can be attributes of an object type (user-defined data type).

- The LOB locator is stored in the table column, either with or without the actual LOB value. `BLOB`, `NCLOB`, and `CLOB` values can be stored in separate tablespaces. `BFILE` data is stored in an external file on the server.

- When you access a LOB column, the locator is returned.

- A LOB can be up to (232-1 bytes)\*(database block size) in size. `BFILE` data can be up to 264-1 bytes, although your operating system may impose restrictions on this maximum.

- LOBs permit efficient, random, piece-wise access to and manipulation of data.

- You can define more than one LOB column in a table.

- With the exception of `NCLOB`, you can define one or more LOB attributes in an object.

- You can declare LOB bind variables.

- You can select LOB columns and LOB attributes.

- You can insert a new row or update an existing row that contains one or more LOB columns or an object with one or more LOB attributes. In update operations, you can set the internal LOB value to `NULL`, empty, or replace the entire LOB with data. You can set the `BFILE` to `NULL` or make it point to a different file.

- You can update a LOB row-column intersection or a LOB attribute with another LOB row-column intersection or LOB attribute.

- You can delete a row containing a LOB column or LOB attribute and thereby also delete the LOB value. For BFILEs, the actual operating system file is not deleted.


You can access and populate rows of an inline LOB column (a LOB column stored in the database) or a LOB attribute (an attribute of an object type column stored in the database) simply by issuing an `INSERT` or `UPDATE` statement.

Restrictions on LOB Columns LOB columns are subject to a number of rules and restrictions. See [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/database/121/ADLOB/adlob_working.htm#ADLOB2010) for a complete listing.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/database/121/ARPLS/d_lob.htm#ARPLS600) and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/database/121/LNOCI/oci07lob.htm#LNOCI070) for more information about these interfaces and LOBs

- the `modify_col_properties` clause of [ALTER TABLE](https://docs.oracle.com/database/121/SQLRF/statements_3001.htm#CJAHHIBI) and [TO\_LOB](https://docs.oracle.com/database/121/SQLRF/functions221.htm#i79464) for more information on converting `LONG` columns to LOB columns


### BFILE Data Type

The `BFILE` data type enables access to binary file LOBs that are stored in file systems outside Oracle Database. A `BFILE` column or attribute stores a `BFILE` locator, which serves as a pointer to a binary file on the server file system. The locator maintains the directory name and the filename.

You can change the filename and path of a `BFILE` without affecting the base table by using the `BFILENAME` function. Refer to [BFILENAME](https://docs.oracle.com/database/121/SQLRF/functions020.htm#i76871) for more information on this built-in SQL function.

Binary file LOBs do not participate in transactions and are not recoverable. Rather, the underlying operating system provides file integrity and durability. `BFILE` data can be up to 264-1 bytes, although your operating system may impose restrictions on this maximum.

The database administrator must ensure that the external file exists and that Oracle processes have operating system read permissions on the file.

The `BFILE` data type enables read-only support of large binary files. You cannot modify or replicate such a file. Oracle provides APIs to access file data. The primary interfaces that you use to access file data are the `DBMS_LOB` package and Oracle Call Interface (OCI).

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/database/121/ADLOB/adlob_bfile_ops.htm#ADLOB012) and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/database/121/LNOCI/oci07lob.htm#LNOCI070) for more information about LOBs and [CREATE DIRECTORY](https://docs.oracle.com/database/121/SQLRF/statements_5008.htm#i2061958)

### BLOB Data Type

The `BLOB` data type stores unstructured binary large objects. `BLOB` objects can be thought of as bitstreams with no character set semantics. `BLOB` objects can store binary data up to (4 gigabytes -1) \* (the value of the `CHUNK` parameter of LOB storage). If the tablespaces in your database are of standard block size, and if you have used the default value of the `CHUNK` parameter of LOB storage when creating a LOB column, then this is equivalent to (4 gigabytes - 1) \* (database block size).

`BLOB` objects have full transactional support. Changes made through SQL, the `DBMS_LOB` package, or Oracle Call Interface (OCI) participate fully in the transaction. `BLOB` value manipulations can be committed and rolled back. However, you cannot save a `BLOB` locator in a PL/SQL or OCI variable in one transaction and then use it in another transaction or session.

### CLOB Data Type

The `CLOB` data type stores single-byte and multibyte character data. Both fixed-width and variable-width character sets are supported, and both use the database character set. `CLOB` objects can store up to (4 gigabytes -1) \* (the value of the `CHUNK` parameter of LOB storage) of character data. If the tablespaces in your database are of standard block size, and if you have used the default value of the `CHUNK` parameter of LOB storage when creating a LOB column, then this is equivalent to (4 gigabytes - 1) \* (database block size).

`CLOB` objects have full transactional support. Changes made through SQL, the `DBMS_LOB` package, or Oracle Call Interface (OCI) participate fully in the transaction. `CLOB` value manipulations can be committed and rolled back. However, you cannot save a `CLOB` locator in a PL/SQL or OCI variable in one transaction and then use it in another transaction or session.

### NCLOB Data Type

The `NCLOB` data type stores Unicode data. Both fixed-width and variable-width character sets are supported, and both use the national character set. `NCLOB` objects can store up to (4 gigabytes -1) \* (the value of the `CHUNK` parameter of LOB storage) of character text data. If the tablespaces in your database are of standard block size, and if you have used the default value of the `CHUNK` parameter of LOB storage when creating a LOB column, then this is equivalent to (4 gigabytes - 1) \* (database block size).

`NCLOB` objects have full transactional support. Changes made through SQL, the `DBMS_LOB` package, or OCI participate fully in the transaction. `NCLOB` value manipulations can be committed and rolled back. However, you cannot save an `NCLOB` locator in a PL/SQL or OCI variable in one transaction and then use it in another transaction or session.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/database/121/NLSPG/ch6unicode.htm#NLSPG006) for information on Unicode data type support

## Extended Data Types

Beginning with Oracle Database 12c, you can specify a maximum size of 32767 bytes for the `VARCHAR2`, `NVARCHAR2`, and `RAW` data types. You can control whether your database supports this new maximum size by setting the initialization parameter `MAX_STRING_SIZE` as follows:

- If `MAX_STRING_SIZE``=``STANDARD`, then the size limits for releases prior to Oracle Database 12c apply: 4000 bytes for the `VARCHAR2` and `NVARCHAR2` data types, and 2000 bytes for the `RAW` data type. This is the default.

- If `MAX_STRING_SIZE``=``EXTENDED`, then the size limit is 32767 bytes for the `VARCHAR2`, `NVARCHAR2`, and `RAW` data types.


Note:

Setting `MAX_STRING_SIZE` = `EXTENDED` may update database objects and possibly invalidate them. Refer to [Oracle Database Reference](https://docs.oracle.com/database/121/REFRN/GUID-D424D23B-0933-425F-BC69-9C0E6724693C.htm#REFRN10321) for complete information on the implications of this parameter and how to set and enable this new functionality.

A `VARCHAR2` or `NVARCHAR2` data type with a declared size of greater than 4000 bytes, or a `RAW` data type with a declared size of greater than 2000 bytes, is an extendeddatatype. Extended data type columns are stored out-of-line, leveraging Oracle's LOB technology. The LOB storage is always aligned with the table. In tablespaces managed with Automatic Segment Space Management (ASSM), extended data type columns are stored as SecureFiles LOBs. Otherwise, they are stored as BasicFiles LOBs. The use of LOBs as a storage mechanism is internal only. Therefore, you cannot manipulate these LOBs using the `DBMS_LOB` package.

Notes:

- Oracle strongly discourages the use of BasicFiles LOBs as a storage mechanism. BasicFiles LOBs not only impose restrictions on the capabilities of extended data type columns, but the BasicFiles data type is planned to be deprecated in a future release.

- Extended data types are subject to the same rules and restrictions as LOBs. Refer to [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/database/121/ADLOB/adlob_working.htm#ADLOB2010) for more information.


Note that, although you must set `MAX_STRING_SIZE``=``EXTENDED` in order to set the size of a `RAW` data type to greater than 2000 bytes, a `RAW` data type is stored as an out-of-line LOB only if it has a size of greater than 4000 bytes. For example, you must set `MAX_STRING_SIZE``=``EXTENDED` in order to declare a `RAW(3000)` data type. However, the column is stored inline.

You can use extended data types just as you would standard data types, with the following considerations:

- For special considerations when creating an index on an extended data type column, or when requiring an index to enforce a primary key or unique constraint, see ["Creating an Index on an Extended Data Type Column"](https://docs.oracle.com/database/121/SQLRF/statements_5013.htm#BGECBJDG).

- If the partitioning key column for a list partition is an extended data type column, then the list of values that you want to specify for a partition may exceed the 4K byte limit for the partition bounds. See the [list\_partitions](https://docs.oracle.com/database/121/SQLRF/statements_7002.htm#BABDGHIB) clause of `CREATE``TABLE` for information on how to work around this issue.

- The value of the initialization parameter `MAX_STRING_SIZE` affects the following:
  - The maximum length of a text literal. See ["Text Literals"](https://docs.oracle.com/database/121/SQLRF/sql_elements003.htm#i42617) for more information.

  - The size limit for concatenating two character strings. See ["Concatenation Operator"](https://docs.oracle.com/database/121/SQLRF/operators003.htm#i997789) for more information.

  - The length of the collation key returned by the `NLSSORT` function. See [NLSSORT](https://docs.oracle.com/database/121/SQLRF/functions125.htm#i78399).

  - The size of some of the attributes of the `XMLFormat` object. See ["XML Format Model"](https://docs.oracle.com/database/121/SQLRF/sql_elements004.htm#i54997) for more information.

  - The size of some expressions in the following XML functions: [XMLCOLATTVAL](https://docs.oracle.com/database/121/SQLRF/functions254.htm#i1129374), [XMLELEMENT](https://docs.oracle.com/database/121/SQLRF/functions258.htm#i1129193), [XMLFOREST](https://docs.oracle.com/database/121/SQLRF/functions260.htm#i1172404), [XMLPI](https://docs.oracle.com/database/121/SQLRF/functions264.htm#CIHGJCBF), and [XMLTABLE](https://docs.oracle.com/database/121/SQLRF/functions269.htm#CIHGGHFB).

## Rowid Data Types

Each row in the database has an address. The sections that follow describe the two forms of row address in an Oracle Database.

### ROWID Data Type

The rows in heap-organized tables that are native to Oracle Database have row addresses called rowids. You can examine a rowid row address by querying the pseudocolumn `ROWID`. Values of this pseudocolumn are strings representing the address of each row. These strings have the data type `ROWID`. You can also create tables and clusters that contain actual columns having the `ROWID` data type. Oracle Database does not guarantee that the values of such columns are valid rowids. Refer to [Chapter 3, "Pseudocolumns"](https://docs.oracle.com/database/121/SQLRF/pseudocolumns.htm#g1020307) for more information on the `ROWID` pseudocolumn.

Rowids contain the following information:

- The data block of the data file containing the row. The length of this string depends on your operating system.

- The row in the data block.

- The database file containing the row. The first data file has the number 1. The length of this string depends on your operating system.

- The data object number, which is an identification number assigned to every database segment. You can retrieve the data object number from the data dictionary views `USER_OBJECTS`, `DBA_OBJECTS`, and `ALL_OBJECTS`. Objects that share the same segment (clustered tables in the same cluster, for example) have the same object number.


Rowids are stored as base 64 values that can contain the characters A-Z, a-z, 0-9, and the plus sign (+) and forward slash (/). Rowids are not available directly. You can use the supplied package `DBMS_ROWID` to interpret rowid contents. The package functions extract and provide information on the four rowid elements listed above.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/database/121/ARPLS/d_rowid.htm#ARPLS053) for information on the functions available with the `DBMS_ROWID` package and how to use them

### UROWID Data Type

The rows of some tables have addresses that are not physical or permanent or were not generated by Oracle Database. For example, the row addresses of index-organized tables are stored in index leaves, which can move. Rowids of foreign tables (such as DB2 tables accessed through a gateway) are not standard Oracle rowids.

Oracle uses universal rowids (urowids) to store the addresses of index-organized and foreign tables. Index-organized tables have logical urowids and foreign tables have foreign urowids. Both types of urowid are stored in the `ROWID` pseudocolumn (as are the physical rowids of heap-organized tables).

Oracle creates logical rowids based on the primary key of the table. The logical rowids do not change as long as the primary key does not change. The `ROWID` pseudocolumn of an index-organized table has a data type of `UROWID`. You can access this pseudocolumn as you would the `ROWID` pseudocolumn of a heap-organized table (using a `SELECT` ... `ROWID` statement). If you want `to` store the rowids of an index-organized table, then you can define a column of type `UROWID` for the table and retrieve the value of the `ROWID` pseudocolumn into that column.

## ANSI, DB2, and SQL/DS Data Types

SQL statements that create tables and clusters can also use ANSI data types and data types from the IBM products SQL/DS and DB2. Oracle recognizes the ANSI or IBM data type name that differs from the Oracle Database data type name. It converts the data type to the equivalent Oracle data type, records the Oracle data type as the name of the column data type, and stores the column data in the Oracle data type based on the conversions shown in the tables that follow.

Table 2-6 ANSI Data Types Converted to Oracle Data Types

| ANSI SQL Data Type | Oracle Data Type |
| --- | --- |
| `CHARACTER(n)`<br>`CHAR(n)` | `CHAR(n)` |
| `CHARACTER VARYING(n)`<br>`CHAR VARYING(n)` | `VARCHAR2(n)` |
| `NATIONAL CHARACTER(n)`<br>`NATIONAL CHAR(n)`<br>`NCHAR(n)` | `NCHAR(n)` |
| `NATIONAL CHARACTER VARYING(n)`<br>`NATIONAL CHAR VARYING(n)`<br>`NCHAR VARYING(n)` | `NVARCHAR2(n)` |
| `NUMERIC[(p,s)]`<br>`DECIMAL[(p,s)]` (Note 1) | `NUMBER(p,s)` |
| `INTEGER`<br>`INT`<br>`SMALLINT` | `NUMBER(p,0)` |
| `FLOAT` (Note 2)<br>`DOUBLE PRECISION` (Note 3)<br>`REAL` (Note 4) | `FLOAT(126)`<br>`FLOAT(126)`<br>`FLOAT(63)` |

Notes:

1. The `NUMERIC` and `DECIMAL` data types can specify only fixed-point numbers. For those data types, the scale (`s`) defaults to 0.

2. The `FLOAT` data type is a floating-point number with a binary precision b. The default precision for this data type is 126 binary, or 38 decimal.

3. The `DOUBLE PRECISION` data type is a floating-point number with binary precision 126.

4. The `REAL` data type is a floating-point number with a binary precision of 63, or 18 decimal.


Do not define columns with the following SQL/DS and DB2 data types, because they have no corresponding Oracle data type:

- `GRAPHIC`

- `LONG``VARGRAPHIC`

- `VARGRAPHIC`

- `TIME`


Note that data of type `TIME` can also be expressed as Oracle datetime data.

See Also:

["Datetime and Interval Data Types"](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#BABIHEID)

Table 2-7 SQL/DS and DB2 Data Types Converted to Oracle Data Types

| SQL/DS or DB2 Data Type | Oracle Data Type |
| --- | --- |
| `CHARACTER(n)` | `CHAR(n)` |
| `VARCHAR(n)` | `VARCHAR(n)` |
| `LONG VARCHAR` | `LONG` |
| `DECIMAL(p,s)` (Note 1) | `NUMBER(p,s)` |
| `INTEGER`<br>`SMALLINT` | `NUMBER(p,0)` |
| `FLOAT` (Note 2) | `NUMBER` |

Notes:

1. The `DECIMAL` data type can specify only fixed-point numbers. For this data type, `s` defaults to 0.

2. The `FLOAT` data type is a floating-point number with a binary precision `b`. The default precision for this data type is 126 binary or 38 decimal.


## User-Defined Types

User-defined data types use Oracle built-in data types and other user-defined data types as the building blocks of object types that model the structure and behavior of data in applications. The sections that follow describe the various categories of user-defined types.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/database/121/CNCPT/tablecls.htm#CNCPT113) for information about Oracle built-in data types

- [CREATE TYPE](https://docs.oracle.com/database/121/SQLRF/statements_8001.htm#BABHJHEB) and the [CREATE TYPE BODY](https://docs.oracle.com/database/121/SQLRF/statements_8002.htm#i2064997) for information about creating user-defined types

- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/database/121/ADOBJ/adobjdes.htm#ADOBJ008) for information about using user-defined types


### Object Types

Object types are abstractions of the real-world entities, such as purchase orders, that application programs deal with. An object type is a schema object with three kinds of components:

- A name, which identifies the object type uniquely within that schema.

- Attributes, which are built-in types or other user-defined types. Attributes model the structure of the real-world entity.

- Methods, which are functions or procedures written in PL/SQL and stored in the database, or written in a language like C or Java and stored externally. Methods implement operations the application can perform on the real-world entity.


### REF Data Types

An object identifier (represented by the keyword `OID`) uniquely identifies an object and enables you to reference the object from other objects or from relational tables. A data type category called `REF` represents such references. A `REF` data type is a container for an object identifier. `REF` values are pointers to objects.

When a `REF` value points to a nonexistent object, the `REF` is said to be "dangling". A dangling `REF` is different from a null `REF`. To determine whether a `REF` is dangling or not, use the condition `IS` \[`NOT`\] `DANGLING`. For example, given object view `oc_orders` in the sample schema `oe`, the column `customer_ref` is of type `REF` to type `customer_typ`, which has an attribute `cust_email`:

```
SELECT o.customer_ref.cust_email
  FROM oc_orders o
  WHERE o.customer_ref IS NOT DANGLING;
```

### Varrays

An array is an ordered set of data elements. All elements of a given array are of the same data type. Each element has an index, which is a number corresponding to the position of the element in the array.

The number of elements in an array is the size of the array. Oracle arrays are of variable size, which is why they are called varrays. You must specify a maximum size when you declare the varray.

When you declare a varray, it does not allocate space. It defines a type, which you can use as:

- The data type of a column of a relational table

- An object type attribute

- A PL/SQL variable, parameter, or function return type


Oracle normally stores an array object either in line (as part of the row data) or out of line (in a LOB), depending on its size. However, if you specify separate storage characteristics for a varray, then Oracle stores it out of line, regardless of its size. Refer to the [varray\_col\_properties](https://docs.oracle.com/database/121/SQLRF/statements_7002.htm#i2143624) of [CREATE TABLE](https://docs.oracle.com/database/121/SQLRF/statements_7002.htm#i2095331) for more information about varray storage.

### Nested Tables

A nested table type models an unordered set of elements. The elements may be built-in types or user-defined types. You can view a nested table as a single-column table or, if the nested table is an object type, as a multicolumn table, with a column for each attribute of the object type.

A nested table definition does not allocate space. It defines a type, which you can use to declare:

- The data type of a column of a relational table

- An object type attribute

- A PL/SQL variable, parameter, or function return type


When a nested table appears as the type of a column in a relational table or as an attribute of the underlying object type of an object table, Oracle stores all of the nested table data in a single table, which it associates with the enclosing relational or object table.

## Oracle-Supplied Types

Oracle provides SQL-based interfaces for defining new types when the built-in or ANSI-supported types are not sufficient. The behavior for these types can be implemented in C/C++, Java, or PL/ SQL. Oracle Database automatically provides the low-level infrastructure services needed for input-output, heterogeneous client-side access for new data types, and optimizations for data transfers between the application and the database.

These interfaces can be used to build user-defined (or object) types and are also used by Oracle to create some commonly useful data types. Several such data types are supplied with the server, and they serve both broad horizontal application areas (for example, the `Any` types) and specific vertical ones (for example, the spatial types).

The Oracle-supplied types, along with cross-references to the documentation of their implementation and use, are described in the following sections:

- [Any Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i107578)

- [XML Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i160550)

- [Spatial Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i107588)

- [Media Types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#i121058)


## Any Types

The `Any` types provide highly flexible modeling of procedure parameters and table columns where the actual type is not known. These data types let you dynamically encapsulate and access type descriptions, data instances, and sets of data instances of any other SQL type. These types have OCI and PL/SQL interfaces for construction and access.

### ANYTYPE

This type can contain a type description of any named SQL type or unnamed transient type.

### ANYDATA

This type contains an instance of a given type, with data, plus a description of the type. `ANYDATA` can be used as a table column data type and lets you store heterogeneous values in a single column. The values can be of SQL built-in types as well as user-defined types.

### ANYDATASET

This type contains a description of a given type plus a set of data instances of that type. `ANYDATASET` can be used as a procedure parameter data type where such flexibility is needed. The values of the data instances can be of SQL built-in types as well as user-defined types.

See Also:

Oracle Database PL/SQL Packages and Types Reference for information on the [`ANYTYPE`](https://docs.oracle.com/database/121/ARPLS/t_anytyp.htm#ARPLS079), [`ANYDATA`](https://docs.oracle.com/database/121/ARPLS/t_anydat.htm#ARPLS077), and [`ANYDATASET`](https://docs.oracle.com/database/121/ARPLS/t_anyset.htm#ARPLS078) types

## XML Types

Extensible Markup Language (XML) is a standard format developed by the World Wide Web Consortium (W3C) for representing structured and unstructured data on the World Wide Web. Universal resource identifiers (URIs) identify resources such as Web pages anywhere on the Web. Oracle provides types to handle XML and URI data, as well as a class of URIs called `DBURIRef` types to access data stored within the database itself. It also provides a set of types to store and access both external and internal URIs from within the database.

### XMLType

This Oracle-supplied type can be used to store and query XML data in the database. `XMLType` has member functions you can use to access, extract, and query the XML data using XPath expressions. XPath is another standard developed by the W3C committee to traverse XML documents. Oracle `XMLType` functions support many W3C XPath expressions. Oracle also provides a set of SQL functions and PL/SQL packages to create `XMLType` values from existing relational or object-relational data.

`XMLType` is a system-defined type, so you can use it as an argument of a function or as the data type of a table or view column. You can also create tables and views of `XMLType`. When you create an `XMLType` column in a table, you can choose to store the XML data in a `CLOB` column, as binary XML (stored internally as a `CLOB`), or object relationally.

You can also register the schema (using the `DBMS_XMLSCHEMA` package) and create a table or column conforming to the registered schema. In this case Oracle stores the XML data in underlying object-relational columns by default, but you can specify storage in a `CLOB` or binary XML column even for schema-based data.

Queries and DML on `XMLType` columns operate the same regardless of the storage mechanism.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/database/121/ADXDB/xdb04cre.htm#ADXDB0400) for information about using XMLType columns

### URI Data Types

Oracle supplies a family of URI types—`URIType`, `DBURIType`, `XDBURIType`, and `HTTPURIType`—which are related by an inheritance hierarchy. `URIType` is an object type and the others are subtypes of `URIType`. Since `URIType` is the supertype, you can create columns of this type and store `DBURIType` or `HTTPURIType` type instances in this column.

HTTPURIType You can use `HTTPURIType` to store URLs to external Web pages or to files. Oracle accesses these files using HTTP (Hypertext Transfer Protocol).

XDBURIType You can use `XDBURIType` to expose documents in the XML database hierarchy as URIs that can be embedded in any `URIType` column in a table. The `XDBURIType` consists of a URL, which comprises the hierarchical name of the XML document to which it refers and an optional fragment representing the XPath syntax. The fragment is separated from the URL part by a pound sign (#). The following lines are examples of `XDBURIType`:

```
/home/oe/doc1.xml
/home/oe/doc1.xml#/orders/order_item
```

DBURIType `DBURIType` can be used to store `DBURIRef` values, which reference data inside the database. Storing `DBURIRef` values lets you reference data stored inside or outside the database and access the data consistently.

`DBURIRef` values use an XPath-like representation to reference data inside the database. If you imagine the database as an XML tree, then you would see the tables, rows, and columns as elements in the XML document. For example, the sample human resources user `hr` would see the following XML tree:

```
<HR>
  <EMPLOYEES>
    <ROW>
      <EMPLOYEE_ID>205</EMPLOYEE_ID>
      <LAST_NAME>Higgins</LAST_NAME>
      <SALARY>12008</SALARY>
      .. <!-- other columns -->
    </ROW>
    ... <!-- other rows -->
  </EMPLOYEES>
  <!-- other tables..-->
</HR>
<!-- other user schemas on which you have some privilege on..-->
```

The `DBURIRef` is an XPath expression over this virtual XML document. So to reference the `SALARY` value in the `EMPLOYEES` table for the employee with employee number 205, you can write a `DBURIRef` as,

```
/HR/EMPLOYEES/ROW[EMPLOYEE_ID=205]/SALARY
```

Using this model, you can reference data stored in `CLOB` columns or other columns and expose them as URLs to the external world.

### URIFactory Package

Oracle also provides the `URIFactory` package, which can create and return instances of the various subtypes of the `URITypes`. The package analyzes the URL string, identifies the type of URL (HTTP, `DBURI`, and so on), and creates an instance of the subtype. To create a `DBURI` instance, the URL must begin with the prefix `/oradb`. For example, `URIFactory.getURI('/oradb/HR/EMPLOYEES')` would create a `DBURIType` instance and `URIFactory.getUri('/sys/schema')` would create an `XDBURIType` instance.

See Also:

- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/database/121/ADOBJ/adobjbas.htm#ADOBJ00205) for general information on object types and type inheritance

- [Oracle XML DB Developer's Guide](https://docs.oracle.com/database/121/ADXDB/xdb15dbu.htm#ADXDB1900) for more information about these supplied types and their implementation

- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/database/121/ADQUE/aq_intro.htm#ADQUE0100) for information about using `XMLType` with Oracle Advanced Queuing


## Spatial Types

Oracle Spatial and Graph is designed to make spatial data management easier and more natural to users of location-enabled applications, geographic information system (GIS) applications, and geoimaging applications. After the spatial data is stored in an Oracle Database, you can easily manipulate, retrieve, and relate it to all the other data stored in the database. The following data types are available only if you have installed Oracle Spatial and Graph.

### SDO\_GEOMETRY

The geometric description of a spatial object is stored in a single row, in a single column of object type `SDO_GEOMETRY` in a user-defined table. Any table that has a column of type `SDO_GEOMETRY` must have another column, or set of columns, that defines a unique primary key for that table. Tables of this sort are sometimes called geometry tables.

The `SDO_GEOMETRY` object type has the following definition:

```
CREATE TYPE SDO_GEOMETRY AS OBJECT
  (sgo_gtype        NUMBER,
   sdo_srid         NUMBER,
   sdo_point        SDO_POINT_TYPE,
   sdo_elem_info    SDO_ELEM_INFO_ARRAY,
   sdo_ordinates    SDO_ORDINATE_ARRAY);
/
```

### SDO\_TOPO\_GEOMETRY

This type describes a topology geometry, which is stored in a single row, in a single column of object type `SDO_TOPO_GEOMETRY` in a user-defined table.

The `SDO_TOPO_GEOMETRY` object type has the following definition:

```
CREATE TYPE SDO_TOPO_GEOMETRY AS OBJECT
  (tg_type        NUMBER,
   tg_id          NUMBER,
   tg_layer_id    NUMBER,
   topology_id    NUMBER);
/
```

### SDO\_GEORASTER

In the GeoRaster object-relational model, a raster grid or image object is stored in a single row, in a single column of object type `SDO_GEORASTER` in a user-defined table. Tables of this sort are called GeoRaster tables.

The `SDO_GEORASTER` object type has the following definition:

```
CREATE TYPE SDO_GEORASTER AS OBJECT
  (rasterType         NUMBER,
   spatialExtent      SDO_GEOMETRY,
   rasterDataTable    VARCHAR2(32),
   rasterID           NUMBER,
   metadata           XMLType);
/
```

See Also:

[Oracle Spatial and Graph Developer's Guide](https://docs.oracle.com/database/121/SPATL/spatial-data-types-and-metadata.htm#SPATL020), [Oracle Spatial and Graph Topology Data Model and Network Data Model Graph Developer's Guide](https://docs.oracle.com/database/121/TOPOL/topology-data-model-overview.htm#TOPOL100), and [Oracle Spatial and Graph GeoRaster Developer's Guide](https://docs.oracle.com/database/121/GEORS/geor_operations.htm#GEORS200) for information on the full implementation of the spatial data types and guidelines for using them

## Media Types

Oracle Multimedia uses object types, similar to Java or C++ classes, to describe multimedia data. An instance of these object types consists of attributes, including metadata and the media data, and methods. The Multimedia data types are created in the `ORDSYS` schema. Public synonyms exist for all the data types, so you can access them without specifying the schema name.

Oracle Multimedia provides the following object types:

- `ORDAudio`

Supports the storage and management of audio data.

- `ORDDicom`

Supports the storage and management of Digital Imaging and Communications in Medicine (DICOM), the format universally recognized as the standard for medical imaging.

- `ORDDoc`

Supports storage and management of any type of media data, including audio, image and video data. Use this type when you want all media to be stored in a single column.

- `ORDImage`

Supports the storage and management of image data.

- `ORDVideo`

Supports the storage and management of video data.


The following data types provide compliance with the ISO-IEC 13249-5 Still Image standard, commonly referred to as SQL/MM StillImage:

- `SI_AverageColor`

Represents a feature that characterizes an image by its average color.

- `SI_Color`

Encapsulates color values.

- `SI_ColorHistogram`

Represents a feature that characterizes an image by the relative frequencies of the colors exhibited by samples of the raw image.

- `SI_FeatureList`

A list containing up to four of the image features represented by the preceding object types (`SI_AverageColor`, `SI_ColorHistogram`, `SI_PositionalColor`, and `SI_Texture`), where each feature is associated with a feature weight.

- `SI_PositionalColor`

Given an image divided into `n` by `m` rectangles, the `SI_PositionalColor` object type represents the feature that characterizes an image by the `n` by `m` most significant colors of the rectangles.

- `SI_StillImage`

Represents digital images with inherent image characteristics such as height, width, and format.

- `SI_Texture`

Represents a feature that characterizes an image by the size of repeating items (coarseness), brightness variations (contrast), and predominant direction (directionality).


See Also:

- [Oracle Multimedia DICOM Developer's Guide](https://docs.oracle.com/database/121/IMDCM/ch_dev_ref.htm#IMDCM4000) for information on the `ORDDicom` object type

- [Oracle Multimedia Reference](https://docs.oracle.com/database/121/AIVUG/toc.htm) for information on all other object types listed in this section


[Previous Page](https://docs.oracle.com/database/121/SQLRF/sql_elements.htm "Go to previous page")

Page 12 of 555

[Next Page](https://docs.oracle.com/database/121/SQLRF/sql_elements002.htm "Go to next page")