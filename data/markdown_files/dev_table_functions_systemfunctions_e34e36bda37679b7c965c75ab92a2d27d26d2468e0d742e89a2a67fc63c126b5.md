# System (Built-in) Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#system-built-in-functions)

Flink Table API & SQL provides users with a set of built-in functions for data transformations. This page gives a brief overview of them.
If a function that you need is not supported yet, you can implement a [user-defined function](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/udfs/).
If you think that the function is general enough, please [open a Jira issue](https://issues.apache.org/jira/secure/CreateIssue!default.jspa) for it with a detailed description.

## Scalar Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#scalar-functions)

The scalar functions take zero, one or more values as the input and return a single value as the result.

### Comparison Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#comparison-functions)

| SQL Function | Table Function | Description |
| --- | --- | --- |
| value1 = value2 | value1 === value2 | Returns TRUE if value1 is equal to value2; returns UNKNOWN if value1 or value2 is NULL. |
| value1 <> value2 | value1 !== value2 | Returns TRUE if value1 is not equal to value2; returns UNKNOWN if value1 or value2 is NULL. |
| value1 > value2 | value1 > value2 | Returns TRUE if value1 is greater than value2; returns UNKNOWN if value1 or value2 is NULL. |
| value1 >= value2 | value1 >= value2 | Returns TRUE if value1 is greater than or equal to value2; returns UNKNOWN if value1 or value2 is NULL. |
| value1 < value2 | value1 < value2 | Returns TRUE if value1 is less than value2; returns UNKNOWN if value1 or value2 is NULL. |
| value1 <= value2 | value1 <= value2 | Returns TRUE if value1 is less than or equal to value2; returns UNKNOWN if value1 or value2 is NULL. |
| value IS NULL | value.isNull | Returns TRUE if value is NULL. |
| value IS NOT NULL | value.isNotNull | Returns TRUE if value is not NULL. |
| value1 IS DISTINCT FROM value2 | N/A | Returns TRUE if two values are different. NULL values are treated as identical here. E.g., 1 IS DISTINCT FROM NULL returns TRUE; NULL IS DISTINCT FROM NULL returns FALSE. |
| value1 IS NOT DISTINCT FROM value2 | N/A | Returns TRUE if two values are equal. NULL values are treated as identical here. E.g., 1 IS NOT DISTINCT FROM NULL returns FALSE; NULL IS NOT DISTINCT FROM NULL returns TRUE. |
| value1 BETWEEN \[ ASYMMETRIC \| SYMMETRIC \] value2 AND value3 | N/A | By default (or with the ASYMMETRIC keyword), returns TRUE if value1 is greater than or equal to value2 and less than or equal to value3. With the SYMMETRIC keyword, returns TRUE if value1 is inclusively between value2 and value3. When either value2 or value3 is NULL, returns FALSE or UNKNOWN. E.g., 12 BETWEEN 15 AND 12 returns FALSE; 12 BETWEEN SYMMETRIC 15 AND 12 returns TRUE; 12 BETWEEN 10 AND NULL returns UNKNOWN; 12 BETWEEN NULL AND 10 returns FALSE; 12 BETWEEN SYMMETRIC NULL AND 12 returns UNKNOWN. |
| value1 NOT BETWEEN \[ ASYMMETRIC \| SYMMETRIC \] value2 AND value3 | N/A | By default (or with the ASYMMETRIC keyword), returns TRUE if value1 is less than value2 or greater than value3. With the SYMMETRIC keyword, returns TRUE if value1 is not inclusively between value2 and value3. When either value2 or value3 is NULL, returns TRUE or UNKNOWN. E.g., 12 NOT BETWEEN 15 AND 12 returns TRUE; 12 NOT BETWEEN SYMMETRIC 15 AND 12 returns FALSE; 12 NOT BETWEEN NULL AND 15 returns UNKNOWN; 12 NOT BETWEEN 15 AND NULL returns TRUE; 12 NOT BETWEEN SYMMETRIC 12 AND NULL returns UNKNOWN. |
| string1 LIKE string2 \[ ESCAPE char \] | string1.like(string2\[, char\]) | Returns TRUE if string1 matches pattern string2; returns UNKNOWN if string1 or string2 is NULL. An escape character consisting of a single char can be defined if necessary, ‘' by default. |
| string1 NOT LIKE string2 \[ ESCAPE char \] | N/A | Returns TRUE if string1 does not match pattern string2; returns UNKNOWN if string1 or string2 is NULL. An escape character consisting of a single char can be defined if necessary, ‘' by default. |
| string1 SIMILAR TO string2 \[ ESCAPE char \] | string1.similar(string2) | Returns TRUE if string1 matches SQL regular expression string2; returns UNKNOWN if string1 or string2 is NULL. An escape character can be defined if necessary. The escape character has not been supported yet. |
| string1 NOT SIMILAR TO string2 \[ ESCAPE char \] | N/A | Returns TRUE if string1 does not match SQL regular expression string2; returns UNKNOWN if string1 or string2 is NULL. An escape character can be defined if necessary. The escape character has not been supported yet. |
| value1 IN (value2 \[, value3\]\* ) | value1.in(valu2) | Returns TRUE if value1 exists in the given list (value2, value3, …). When (value2, value3, …). contains NULL, returns TRUE if the element can be found and UNKNOWN otherwise. Always returns UNKNOWN if value1 is NULL. E.g., 4 IN (1, 2, 3) returns FALSE; 1 IN (1, 2, NULL) returns TRUE; 4 IN (1, 2, NULL) returns UNKNOWN. |
| value1 NOT IN (value2 \[, value3\]\* ) | N/A | Returns TRUE if value1 does not exist in the given list (value2, value3, …). When (value2, value3, …). contains NULL, returns FALSE if value1 can be found and UNKNOWN otherwise. Always returns UNKNOWN if value1 is NULL. E.g., 4 NOT IN (1, 2, 3) returns TRUE; 1 NOT IN (1, 2, NULL) returns FALSE; 4 NOT IN (1, 2, NULL) returns UNKNOWN. |
| EXISTS (sub-query) | N/A | Returns TRUE if sub-query returns at least one row. Only supported if the operation can be rewritten in a join and group operation. For streaming queries the operation is rewritten in a join and group operation. The required state to compute the query result might grow infinitely depending on the number of distinct input rows. Please provide a query configuration with valid retention interval to prevent excessive state size. |
| value IN (sub-query) | value.in(TABLE) | Returns TRUE if value is equal to a row returned by sub-query. |
| value NOT IN (sub-query) | N/A | Returns TRUE if value is not equal to a row returned by sub-query. |
| N/A | value1.between(value2, value3) | Returns TRUE if value1 is greater than or equal to value2 and less than or equal to value3. When either value2 or value3 is NULL, returns FALSE or UNKNOWN. |
| N/A | value1.notBetween(value2, value3) | Returns FALSE if value1 is greater than or equal to value2 and less than or equal to value3. When either value2 or value3 is NULL, returns TRUE or UNKNOWN. |

### Logical Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#logical-functions)

| SQL Function | Table Function | Description |
| --- | --- | --- |
| boolean1 OR boolean2 | BOOLEAN1 \|\| BOOLEAN2 | Returns TRUE if BOOLEAN1 is TRUE or BOOLEAN2 is TRUE. Supports three-valued logic. E.g., true \|\| Null(BOOLEAN) returns TRUE. |
| boolean1 AND boolean2 | BOOLEAN1 && BOOLEAN2 | Returns TRUE if BOOLEAN1 and BOOLEAN2 are both TRUE. Supports three-valued logic. E.g., true && Null(BOOLEAN) returns UNKNOWN. |
| NOT boolean | BOOLEAN.not(), not(BOOLEAN), or '!BOOLEAN' (Scala only) | Returns TRUE if boolean is FALSE; returns FALSE if boolean is TRUE; returns UNKNOWN if boolean is UNKNOWN. |
| boolean IS FALSE | BOOLEAN.isFalse | Returns TRUE if boolean is FALSE; returns FALSE if boolean is TRUE or UNKNOWN. |
| boolean IS NOT FALSE | BOOLEAN.isNotFalse | Returns TRUE if BOOLEAN is TRUE or UNKNOWN; returns FALSE if BOOLEAN is FALSE. |
| boolean IS TRUE | BOOLEAN.isTrue | Returns TRUE if BOOLEAN is TRUE; returns FALSE if BOOLEAN is FALSE or UNKNOWN. |
| boolean IS NOT TRUE | BOOLEAN.isNotTrue | Returns TRUE if boolean is FALSE or UNKNOWN; returns FALSE if boolean is TRUE. |
| boolean IS UNKNOWN | N/A | Returns TRUE if boolean is UNKNOWN; returns FALSE if boolean is TRUE or FALSE. |
| boolean IS NOT UNKNOWN | N/A | Returns TRUE if boolean is TRUE or FALSE; returns FALSE if boolean is UNKNOWN. |

### Arithmetic Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#arithmetic-functions)

| SQL Function | Table Function | Description |
| --- | --- | --- |
| - numeric | \+ NUMERIC | Returns NUMERIC. |
| - numeric | \- numeric | Returns negative Numeric |
| numeric1 + numeric2 | NUMERIC1 + NUMERIC2 | Returns NUMERIC1 plus NUMERIC2. |
| numeric1 - numeric2 | NUMERIC1 - NUMERIC2 | Return NUMERIC1 minus NUMERIC2 |
| numeric1 \* numberic2 | NUMERIC1 \* NUMERIC2 | Returns NUMERIC1 multiplied by NUMERIC2 |
| numeric1 / numeric2 | NUMERIC1 / NUMERIC2 | Returns NUMERIC1 divided by NUMERIC2 |
| numeric1 % numeric2 | MOD(numeric1, numeric2) | Returns the remainder (modulus) of numeric1 divided by numeric2. The result is negative only if numeric1 is negative. |
| POWER(numeric1, numeric2) | NUMERIC1.power(NUMERIC2) | NUMERIC1.power(NUMERIC2) |
| ABS(numeric) | numeric.abs() | Returns the absolute value of numeric. |
| SQRT(numeric) | NUMERIC.sqrt() | Returns the square root of NUMERIC. |
| LN(numeric) | NUMERIC.ln() | Returns the natural logarithm (base e) of NUMERIC. |
| LOG10(numeric) | numeric.log10() | Returns the base 10 logarithm of numeric. |
| LOG2(numeric) | numeric.log2() | Returns the base 2 logarithm of numeric. |
| LOG(numeric2)<br>LOG(numeric1, numeric2) | NUMERIC1.log()<br>NUMERIC1.log(NUMERIC2) | When called with one argument, returns the natural logarithm of numeric2. When called with two arguments, this function returns the logarithm of numeric2 to the base numeric1. Currently, numeric2 must be greater than 0 and numeric1 must be greater than 1. |
| EXP(numeric) | NUMERIC.exp() | Returns e raised to the power of numeric. |
| CEIL(numeric)<br>CEILING(numeric) | NUMERIC.ceil()<br>NUMERIC.ceiling() | Rounds numeric up, and returns the smallest number that is greater than or equal to numeric. |
| FLOOR(numeric) | NUMERIC.floor() | Rounds numeric down, and returns the largest number that is less than or equal to numeric. |
| SIN(numeric) | NUMERIC.sin() | Returns the sine of numeric. |
| SINH(numeric) | NUMERIC.sinh() | Returns the hyperbolic sine of numeric. The return type is DOUBLE. |
| COS(numeric) | NUMERIC.cos() | Returns the cosine of numeric. |
| TAN(numeric) | NUMERIC.tan() | Returns the tangent of numeric. |
| TANH(numeric) | NUMERIC.tanh() | Returns the hyperbolic tangent of numeric. The return type is DOUBLE. |
| COT(numeric) | NUMERIC.cot() | Returns the cotangent of a numeric. |
| ASIN(numeric) | NUMERIC.asin() | Returns the arc sine of numeric. |
| ACOS(numeric) | NUMERIC.acos() | Returns the arc cosine of numeric. |
| ATAN(numeric) | NUMERIC.atan() | Returns the arc tangent of numeric. |
| ATAN2(numeric1, numeric2) | atan2(NUMERIC1, NUMERIC2) | Returns the arc tangent of a coordinate (NUMERIC1, NUMERIC2). |
| COSH(numeric) | NUMERIC.cosh() | Returns the hyperbolic cosine of NUMERIC. Return value type is DOUBLE. |
| DEGREES(numeric) | NUMERIC.degrees() | Returns the degree representation of a radian NUMERIC. |
| RADIANS(numeric) | NUMERIC.radians() | Returns the radian representation of a degree NUMERIC. |
| SIGN(numeric) | NUMERIC.sign() | Returns the signum of NUMERIC. |
| ROUND(NUMERIC, INT) | NUMERIC.round(INT) | Returns a number rounded to INT decimal places for NUMERIC. |
| PI() | pi() | Returns a value that is closer than any other values to pi. |
| E() | e() | Returns a value that is closer than any other values to e. |
| RAND() | rand() | Returns a pseudorandom double value in the range \[0.0, 1.0) |\
| RAND(INT) | rand(INT) | Returns a pseudorandom double value in the range \[0.0, 1.0) with an initial seed integer. Two RAND functions will return identical sequences of numbers if they have the same initial seed. |\
| RAND\_INTEGER(INT) | randInteger(INT) | Returns a pseudorandom integer value in the range \[0, INT) |\
| RAND\_INTEGER(INT1, INT2) | randInteger(INT1, INT2) | Returns a pseudorandom integer value in the range \[0, INT2) with an initial seed INT1. Two RAND\_INTGER functions will return idential sequences of numbers if they have the same initial seed and bound. |\
| UUID() | uuid() | Returns an UUID (Universally Unique Identifier) string (e.g., “3d3c68f7-f608-473f-b60c-b0c44ad4cc4e”) according to RFC 4122 type 4 (pseudo randomly generated) UUID. The UUID is generated using a cryptographically strong pseudo random number generator. |\
| BIN(INT) | INT.bin() | Returns a string representation of INTEGER in binary format. Returns NULL if INTEGER is NULL. E.g., 4.bin() returns “100” and 12.bin() returns “1100”. |\
| HEX(numeric)<br>HEX(string) | NUMERIC.hex()<br>STRING.hex() | Returns a string representation of an integer NUMERIC value or a STRING in hex format. Returns NULL if the argument is NULL. E.g. a numeric 20 leads to “14”, a numeric 100 leads to “64”, a string “hello,world” leads to “68656C6C6F2C776F726C64”. |\
| UNHEX(expr) | expr.unhex() | Converts hexadecimal string expr to BINARY. If the length of expr is odd, the first character is discarded and the result is left padded with a null byte.<br>E.g., SELECT DECODE(UNHEX(‘466C696E6B’) , ‘UTF-8’ ) or ‘466C696E6B’.unhex().decode(‘UTF-8’) returns “Flink”.<br>expr <CHAR \| VARCHAR><br>Returns a BINARY. `NULL` if expr is `NULL` or expr contains non-hex characters. |\
| TRUNCATE(numeric1, integer2) | NUMERIC1.truncate(INTEGER2) | Returns a numeric of truncated to integer2 decimal places. Returns NULL if numeric1 or integer2 is NULL. If integer2 is 0, the result has no decimal point or fractional part. integer2 can be negative to cause integer2 digits left of the decimal point of the value to become zero. This function can also pass in only one numeric1 parameter and not set integer2 to use. If integer2 is not set, the function truncates as if integer2 were 0. E.g. 42.324.truncate(2) to 42.32. and 42.324.truncate() to 42.0. |\
| PERCENTILE(expr, percentage\[, frequency\]) | expr.percentile(percentage\[, frequency\]) | Returns the percentile value of expr at the specified percentage using continuous distribution.<br>E.g., SELECT PERCENTILE(age, 0.25) FROM (VALUES (10), (20), (30), (40)) AS age or $(‘age’).percentile(0.25) returns 17.5<br>The percentage must be a literal numeric value between `[0.0, 1.0]` or an array of such values.<br>If a variable expression is passed to this function, the result will be calculated using any one of them.<br>frequency describes how many times expr should be counted, the default value is 1.<br>If no expr lies exactly at the desired percentile, the result is calculated using linear interpolation of the two nearest exprs.<br>If expr or frequency is `NULL`, or frequency is not positive, the input row will be ignored.<br>NOTE: It is recommended to use this function in a window scenario, as it typically offers better performance.<br>In a regular group aggregation scenario, users should be aware of the performance overhead caused by a full sort triggered by each record.<br>`value <NUMERIC>, percentage [<NUMERIC NOT NULL> | <ARRAY<NUMERIC NOT NULL> NOT NULL>], frequency <INTEGER_NUMERIC>``(INTEGER_NUMERIC: TINYINT, SMALLINT, INTEGER, BIGINT)``(NUMERIC: INTEGER_NUMERIC, FLOAT, DOUBLE, DECIMAL)`<br>Returns a `DOUBLE` if percentage is numeric, or an `ARRAY<DOUBLE>` if percentage is an array. `NULL` if percentage is an empty array. |\
\
### String Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#string-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| string1 \|\| string2 | STRING1 + STRING2 | Returns the concatenation of STRING1 and STRING2. |\
| CHAR\_LENGTH(string)<br>CHARACTER\_LENGTH(string) | STRING.charLength() | Returns the number of characters in STRING. |\
| UPPER(string) | STRING.upperCase() | Returns STRING in uppercase. |\
| LOWER(string) | STRING.lowerCase() | Returns string in lowercase. |\
| POSITION(string1 IN string2) | STRING1.position(STRING2) | Returns the position (start from 1) of the first occurrence of STRING1 in STRING2; returns 0 if STRING1 cannot be found in STRING2. |\
| PRINTF(format\[, obj\]\*) | format.printf(obj...) | Returns a formatted string from printf-style format string.<br>The function exploits the java.util.Formatter class with Locale.US.<br>null obj is formated as a string “null”.<br>format <CHAR \| VARCHAR>, obj <br>Returns a STRING representation of the formatted string. `NULL` if format is `NULL` or invalid. |\
| TRIM(\[ BOTH \| LEADING \| TRAILING \] string1 FROM string2) | STRING1.trim(LEADING, STRING2)<br>STRING1.trim(TRAILING, STRING2)<br>STRING1.trim(BOTH, STRING2)<br>STRING1.trim(BOTH)<br>STRING1.trim() | Returns a string that removes leading and/or trailing characters STRING2 from STRING1. By default, whitespaces at both sides are removed. |\
| LTRIM(str\[, trimStr\]) | str.ltrim(\[trimStr\]) | Removes any leading characters within trimStr from str. trimStr is set to whitespace by default.<br>E.g., ’ This is a test String.’.ltrim() returns “This is a test String.”.<br>str <CHAR \| VARCHAR>, trimStr <CHAR \| VARCHAR><br>Returns a STRING representation of the trimmed str. `NULL` if any of the arguments are `NULL`. |\
| RTRIM(str\[, trimStr\]) | str.rtrim(\[trimStr\]) | Removes any trailing characters within trimStr from str. trimStr is set to whitespace by default.<br>E.g., ‘This is a test String. ‘.rtrim() returns “This is a test String.”.<br>str <CHAR \| VARCHAR>, trimStr <CHAR \| VARCHAR><br>Returns a STRING representation of the trimmed str. `NULL` if any of the arguments are `NULL`. |\
| BTRIM(str\[, trimStr\]) | str.btrim(\[trimStr\]) | Removes any leading and trailing characters within trimStr from str. trimStr is set to whitespace by default.<br>E.g., BTRIM(’ [www.apache.org](https://www.apache.org/) ‘) or ’ [www.apache.org](https://www.apache.org/) ‘.btrim() returns “ [www.apache.org](https://www.apache.org/)”, BTRIM(’/www.apache.org/’, ‘/’) or ’ [www.apache.org](https://www.apache.org/) ‘.btrim() returns “ [www.apache.org](https://www.apache.org/)”.<br>str <CHAR \| VARCHAR>, trimStr <CHAR \| VARCHAR><br>Returns a STRING representation of the trimmed str. `NULL` if any of the arguments are `NULL`. |\
| REPEAT(string, int) | STRING.repeat(INT) | Returns a string that repeats the base string integer times. E.g., REPEAT(‘This is a test String.’, 2) returns “This is a test String.This is a test String.”. |\
| REGEXP\_REPLACE(string1, string2, string3) | STRING1.regexpReplace(STRING2, STRING3) | Returns a string from STRING1 with all the substrings that match a regular expression STRING2 consecutively being replaced with STRING3. E.g., ‘foobar’.regexpReplace(‘oo\|ar’, ‘’) returns “fb”. |\
| OVERLAY(string1 PLACING string2 FROM integer1 \[ FOR integer2 \]) | STRING1.overlay(STRING2, INT1)<br>STRING1.overlay(STRING2, INT1, INT2) | Returns a string that replaces INT2 (STRING2’s length by default) characters of STRING1 with STRING2 from position INT1. E.g., ‘xxxxxtest’.overlay(‘xxxx’, 6) returns “xxxxxxxxx”; ‘xxxxxtest’.overlay(‘xxxx’, 6, 2) returns “xxxxxxxxxst”. |\
| STARTSWITH(expr, startExpr) | expr.startsWith(startExpr) | Returns whether expr starts with startExpr. If startExpr is empty, the result is true.<br>expr and startExpr should have same type.<br>`expr <CHAR | VARCHAR>, startExpr <CHAR | VARCHAR>`<br>`expr <BINARY | VARBINARY>, startExpr <BINARY | VARBINARY>`<br>Returns a `BOOLEAN`. `NULL` if any of the arguments are `NULL`. |\
| ENDSWITH(expr, endExpr) | expr.endsWith(endExpr) | Returns whether expr ends with endExpr. If endExpr is empty, the result is true.<br>expr and endExpr should have same type.<br>`expr <CHAR | VARCHAR>, endExpr <CHAR | VARCHAR>`<br>`expr <BINARY | VARBINARY>, endExpr <BINARY | VARBINARY>`<br>Returns a `BOOLEAN`. `NULL` if any of the arguments are `NULL`. |\
| SUBSTRING(string FROM integer1 \[ FOR integer2 \]) | STRING.substring(INT1)<br>STRING.substring(INT1, INT2) | Returns a substring of STRING starting from position INT1 with length INT2 (to the end by default). |\
| REPLACE(string1, string2, string3) | STRING1.replace(STRING2, STRING3) | Returns a new string which replaces all the occurrences of STRING2 with STRING3 (non-overlapping) from STRING1. E.g., ‘hello world’.replace(‘world’, ‘flink’) returns ‘hello flink’; ‘ababab’.replace(‘abab’, ‘z’) returns ‘zab’. |\
| REGEXP\_COUNT(str, regex) | str.regexpCount(regex) | Returns the number of times str matches the regex pattern. regex must be a Java regular expression.<br>`str <CHAR | VARCHAR>, regex <CHAR | VARCHAR>`<br>Returns an `INTEGER` representation of the number of matches. `NULL` if any of the arguments are `NULL` or regex is invalid. |\
| REGEXP\_EXTRACT(string1, string2\[, integer\]) | STRING1.regexpExtract(STRING2\[, INTEGER1\]) | Returns a string from string1 which extracted with a specified<br>regular expression string2 and a regex match group index integer.<br>The regex match group index starts from 1 and 0 means matching<br>the whole regex. In addition, the regex match group index should<br>not exceed the number of the defined groups.<br>E.g. REGEXP\_EXTRACT(‘foothebar’, ‘foo(.\*?)(bar)’, 2)" returns “bar”. |\
| REGEXP\_EXTRACT\_ALL(str, regex\[, extractIndex\]) | str.regexpExtractAll(regex\[, extractIndex\]) | Extracts all the substrings in str that match the regex expression and correspond to the regex group extractIndex.<br>regex may contain multiple groups. extractIndex indicates which regex group to extract and starts from 1, also the default value if not specified. 0 means matching the entire regular expression.<br>`str <CHAR | VARCHAR>, regex <CHAR | VARCHAR>, extractIndex <TINYINT | SMALLINT | INTEGER | BIGINT>`<br>Returns an `ARRAY<STRING>` representation of all the matched substrings. `NULL` if any of the arguments are `NULL` or invalid. |\
| REGEXP\_INSTR(str, regex) | str.regexpInstr(regex) | Returns the position of the first substring in str that matches regex.<br>Result indexes begin at 1, 0 if there is no match.<br>`str <CHAR | VARCHAR>, regex <CHAR | VARCHAR>`<br>Returns an `INTEGER` representation of the first matched substring index. `NULL` if any of the arguments are `NULL` or regex is invalid. |\
| REGEXP\_SUBSTR(str, regex) | str.regexpSubstr(regex) | Returns the first substring in str that matches regex.<br>`str <CHAR | VARCHAR>, regex <CHAR | VARCHAR>`<br>Returns an `STRING` representation of the first matched substring. `NULL` if any of the arguments are `NULL` or regex if invalid or pattern is not found. |\
| TRANSLATE(expr, fromStr, toStr) | expr.translate(fromStr, toStr) | Translate an expr where all characters in fromStr have been replaced with those in toStr. If toStr has a shorter length than fromStr, unmatched characters are removed.<br>E.g., SELECT TRANSLATE3(‘ [www.apache.org](https://www.apache.org/)’, ‘wapcheorg’, ’ APCHEcom’) or ‘ [www.apache.org](https://www.apache.org/)’.translate(‘wapcheorg’, ’ APCHEcom’) returns " .APACHE.com".<br>`expr <CHAR | VARCHAR>, fromStr <CHAR | VARCHAR>, toStr <CHAR | VARCHAR>`<br>Returns a `STRING` of translated expr. |\
| INITCAP(string) | STRING.initCap() | Returns a new form of STRING with the first character of each word converted to uppercase and the rest characters to lowercase. Here a word means a sequences of alphanumeric characters. |\
| CONCAT(string1, string2,…) | concat(STRING1, STRING2, ...) | Returns a string that concatenates string1, string2, …. Returns NULL if any argument is NULL. E.g., CONCAT(‘AA’, ‘BB’, ‘CC’) returns “AABBCC”. |\
| CONCAT\_WS(string1, string2, string3,…) | concat\_ws(STRING1, STRING2, STRING3, ...) | Returns a string that concatenates STRING2, STRING3, … with a separator STRING1. The separator is added between the strings to be concatenated. Returns NULL If STRING1 is NULL. Compared with concat(), concat\_ws() automatically skips NULL arguments. E.g., concat\_ws(’~’, ‘AA’, Null(STRING), ‘BB’, ‘’, ‘CC’) returns “AA~BB~~CC”. |\
| LPAD(string1, integer, string2) | STRING1.lpad(INT, STRING2) | Returns a new string from string1 left-padded with string2 to a length of integer characters. If the length of string1 is shorter than integer, returns string1 shortened to integer characters. E.g., LPAD(‘hi’, 4, ‘??’) returns “??hi”; LPAD(‘hi’, 1, ‘??’) returns “h”. |\
| RPAD(string1, integer, string2) | STRING1.rpad(INT, STRING2) | Returns a new string from string1 right-padded with string2 to a length of integer characters. If the length of string1 is shorter than integer, returns string1 shortened to integer characters. E.g., RPAD(‘hi’, 4, ‘??’) returns “hi??”, RPAD(‘hi’, 1, ‘??’) returns “h”. |\
| FROM\_BASE64(string) | STRING.fromBase64() | Returns the base64-decoded result from string; returns NULL if string is NULL. E.g., FROM\_BASE64(‘aGVsbG8gd29ybGQ=’) returns “hello world”. |\
| TO\_BASE64(string) | STRING.toBase64() | Returns the base64-encoded result from string; returns NULL if string is NULL. E.g., TO\_BASE64(‘hello world’) returns “aGVsbG8gd29ybGQ=”. |\
| ASCII(string) | STRING.ascii() | Returns the numeric value of the first character of string. Returns NULL if string is NULL. E.g., ascii(‘abc’) returns 97, and ascii(CAST(NULL AS VARCHAR)) returns NULL. |\
| CHR(integer) | INT.chr() | Returns the ASCII character having the binary equivalent to integer. If integer is larger than 255, we will get the modulus of integer divided by 255 first, and returns CHR of the modulus. Returns NULL if integer is NULL. E.g., chr(97) returns a, chr(353) returns a, and ascii(CAST(NULL AS VARCHAR)) returns NULL. |\
| DECODE(binary, string) | BINARY.decode(STRING) | Decodes the first argument into a String using the provided character set (one of ‘US-ASCII’, ‘ISO-8859-1’, ‘UTF-8’, ‘UTF-16BE’, ‘UTF-16LE’, ‘UTF-16’). If either argument is null, the result will also be null. |\
| ENCODE(string1, string2) | STRING1.encode(STRING2) | Encodes the string1 into a BINARY using the provided string2 character set (one of ‘US-ASCII’, ‘ISO-8859-1’, ‘UTF-8’, ‘UTF-16BE’, ‘UTF-16LE’, ‘UTF-16’). If either argument is null, the result will also be null. |\
| INSTR(string1, string2) | STRING1.instr(STRING2) | Returns the position of the first occurrence of string2 in string1. Returns NULL if any of arguments is NULL. |\
| LEFT(string, integer) | STRING.LEFT(INT) | Returns the leftmost integer characters from the string. Returns EMPTY String if integer is negative. Returns NULL if any argument is NULL. |\
| RIGHT(string, integer) | STRING.RIGHT(INT) | Returns the rightmost integer characters from the string. Returns EMPTY String if integer is negative. Returns NULL if any argument is NULL. |\
| LOCATE(string1, string2\[, integer\]) | STRING1.locate(STRING2\[, INTEGER\]) | Returns the position of the first occurrence of string1 in string2 after position integer. Returns 0 if not found. Returns NULL if any of arguments is NULL. |\
| URL\_DECODE(string) | STRING.urlDecode() | Decodes a given string in ‘application/x-www-form-urlencoded’ format using the UTF-8 encoding scheme. If the input is NULL, or there is an issue with the decoding process(such as encountering an illegal escape pattern), or the encoding scheme is not supported, the function returns NULL. |\
| URL\_ENCODE(string) | STRING.urlEncode() | Translates a string into ‘application/x-www-form-urlencoded’ format using the UTF-8 encoding scheme. If the input is NULL, or there is an issue with the encoding process, or the encoding scheme is not supported, will return NULL. |\
| PARSE\_URL(string1, string2\[, string3\]) | STRING1.parseUrl(STRING2\[, STRING3\]) | Returns the specified part from the URL. Valid values for string2 include ‘HOST’, ‘PATH’, ‘QUERY’, ‘REF’, ‘PROTOCOL’, ‘AUTHORITY’, ‘FILE’, and ‘USERINFO’. Returns NULL if any of arguments is NULL.<br>E.g., parse\_url(‘ [http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1'](http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1%27), ‘HOST’), returns ‘facebook.com’.<br>Also a value of a particular key in QUERY can be extracted by providing the key as the third argument string3.<br>E.g., parse\_url(‘ [http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1'](http://facebook.com/path1/p.php?k1=v1&k2=v2#Ref1%27), ‘QUERY’, ‘k1’) returns ‘v1’. |\
| REGEXP(string1, string2) | STRING1.regexp(STRING2) | Returns TRUE if any (possibly empty) substring of string1 matches the Java regular expression string2, otherwise FALSE. Returns NULL if any of arguments is NULL. |\
| REVERSE(string) | STRING.reverse() | Returns the reversed string. Returns NULL if string is NULL. |\
| SPLIT\_INDEX(string1, string2, integer1) | STRING1.splitIndex(STRING2, INTEGER1) | Splits string1 by the delimiter string2, returns the integerth (zero-based) string of the split strings. Returns NULL if integer is negative. Returns NULL if any of arguments is NULL. |\
| STR\_TO\_MAP(string1\[, string2, string3\]) | STRING1.strToMap(\[STRING2, STRING3\]) | Returns a map after splitting the string1 into key/value pairs using delimiters. string2 is the pair delimiter, default is ‘,’. And string3 is the key-value delimiter, default is ‘=’.<br>Both pair delimiter and key-value delimiter are treated as regular expressions. So special characters (e.g. `<([{\^-=$!|]})?*+.>`) need to be properly escaped before using as a delimiter literally. |\
| SUBSTR(string, integer1\[, integer2\]) | STRING.substr(INTEGER1\[, INTEGER2\]) | Returns a substring of string starting from position integer1 with length integer2 (to the end by default). |\
| JSON\_QUOTE(string) | STRING.JsonQuote() | Quotes a string as a JSON value by wrapping it with double quote characters, escaping interior quote and special characters (’"’, ‘', ‘/’, ‘b’, ‘f’, ’n’, ‘r’, ’t’), and returning the result as a string. If the argument is NULL, the function returns NULL. |\
| JSON\_UNQUOTE(string) | STRING.JsonUnquote() | Unquotes JSON value, unescapes escaped special characters (’"’, ‘', ‘/’, ‘b’, ‘f’, ’n’, ‘r’, ’t’, ‘u’ hex hex hex hex), and returns the result as a string. If the argument is NULL, returns NULL. If the value does not start and end with double quotes or if it starts and ends with double quotes but is not a valid JSON string literal, the value is passed through unmodified. |\
| ELT(index, expr\[, exprs\]\*) | index.elt(expr, exprs...) | Returns the index-th expression. index must be an integer between 1 and the number of expressions.<br>E.g., SELECT ELT(2, ‘scala-1’, ‘java-2’, ‘go-3’) or 2.elt(‘scala-1’, ‘java-2’, ‘go-3’) returns “java-2”.<br>index <TINYINT \| SMALLINT \| INTEGER \| BIGINT>, expr <CHAR \| VARCHAR>, exprs <CHAR \| VARCHAR><br>index <TINYINT \| SMALLINT \| INTEGER \| BIGINT>, expr <BINARY \| VARBINARY>, exprs <BINARY \| VARBINARY><br>The result has the type of the least common type of all expressions. `NULL` if index is `NULL` or out of range. |\
\
### Temporal Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#temporal-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| DATE string | STRING.toDate() | Returns a SQL date parsed from string in form of “yyyy-MM-dd”. |\
| TIME string | STRING.toTime() | Returns a SQL time parsed from string in form of “HH:mm:ss”. |\
| TIMESTAMP string | STRING.toTimestamp() | Returns a SQL timestamp parsed from string in form of “yyyy-MM-dd HH:mm:ss\[.SSS\]”. |\
| INTERVAL string range | N/A | Parses an interval string in the form “dd hh:mm:ss.fff” for SQL intervals of milliseconds or “yyyy-mm” for SQL intervals of months.<br>An interval range might be DAY, MINUTE, DAY TO HOUR, or DAY TO SECOND for intervals of milliseconds; YEAR or YEAR TO MONTH for intervals of months.<br>E.g., INTERVAL ‘10 00:00:00.004’ DAY TO SECOND, INTERVAL ‘10’ DAY, or INTERVAL ‘2-10’ YEAR TO MONTH return intervals. |\
| N/A | NUMERIC.year<br>NUMERIC.years | Creates an interval of months for NUMERIC years. |\
| N/A | NUMERIC.quarter<br>NUMERIC.quarters | Creates an interval of months for NUMERIC quarters. E.g., 2.quarters returns 6. |\
| N/A | NUMERIC.month<br>NUMERIC.months | Creates an interval of NUMERIC months. |\
| N/A | NUMERIC.week<br>NUMERIC.weeks | Creates an interval of milliseconds for NUMERIC weeks. E.g., 2.weeks returns 1209600000. |\
| N/A | NUMERIC.day<br>NUMERIC.days | Creates an interval of milliseconds for NUMERIC days. |\
| N/A | NUMERIC.hour<br>NUMERIC.hours | Creates an interval of milliseconds for NUMERIC hours. |\
| N/A | NUMERIC.minute<br>NUMERIC.minutes | Creates an interval of milliseconds for NUMERIC minutes. |\
| N/A | NUMERIC.second<br>NUMERIC.seconds | Creates an interval of milliseconds for NUMERIC seconds. |\
| N/A | NUMERIC.milli<br>NUMERIC.millis | Creates an interval of NUMERIC milliseconds. |\
| LOCALTIME | localTime() | Returns the current SQL time in the local time zone, the return type is TIME(0). It is evaluated for each record in streaming mode. But in batch mode, it is evaluated once as the query starts and uses the same result for every row. |\
| LOCALTIMESTAMP | localTimestamp() | Returns the current SQL timestamp in local time zone, the return type is TIMESTAMP(3). It is evaluated for each record in streaming mode. But in batch mode, it is evaluated once as the query starts and uses the same result for every row. |\
| CURRENT\_TIME | currentTime() | Returns the current SQL time in the local time zone, this is a synonym of LOCAL\_TIME. |\
| CURRENT\_DATE | currentDate() | Returns the current SQL date in the local time zone. It is evaluated for each record in streaming mode. But in batch mode, it is evaluated once as the query starts and uses the same result for every row. |\
| CURRENT\_TIMESTAMP | currentTimestamp() | Returns the current SQL timestamp in the local time zone, the return type is TIMESTAMP\_LTZ(3). It is evaluated for each record in streaming mode. But in batch mode, it is evaluated once as the query starts and uses the same result for every row. |\
| NOW() | N/A | Returns the current SQL timestamp in the local time zone, this is a synonym of CURRENT\_TIMESTAMP. |\
| CURRENT\_ROW\_TIMESTAMP() | N/A | Returns the current SQL timestamp in the local time zone, the return type is TIMESTAMP\_LTZ(3). It is evaluated for each record no matter in batch or streaming mode. |\
| EXTRACT(timeinteravlunit FROM temporal) | TEMPORAL.extract(TIMEINTERVALUNIT) | Returns a long value extracted from the timeintervalunit part of temporal. E.g., EXTRACT(DAY FROM DATE ‘2006-06-05’) returns 5. |\
| YEAR(date) | N/A | Returns the year from SQL date. Equivalent to EXTRACT(YEAR FROM date). E.g., YEAR(DATE ‘1994-09-27’) returns 1994. |\
| QUARTER(date) | N/A | Returns the quarter of a year (an integer between 1 and 4) from SQL date. Equivalent to EXTRACT(QUARTER FROM date). E.g., QUARTER(DATE ‘1994-09-27’) returns 3. |\
| MONTH(date) | N/A | Returns the month of a year (an integer between 1 and 12) from SQL date. Equivalent to EXTRACT(MONTH FROM date). E.g., MONTH(DATE ‘1994-09-27’) returns 9. |\
| WEEK(date) | N/A | Returns the week of a year (an integer between 1 and 53) from SQL date. Equivalent to EXTRACT(WEEK FROM date). E.g., WEEK(DATE ‘1994-09-27’) returns 39. |\
| DAYOFYEAR(date) | N/A | Returns the day of a year (an integer between 1 and 366) from SQL date. Equivalent to EXTRACT(DOY FROM date). E.g., DAYOFYEAR(DATE ‘1994-09-27’) returns 270. |\
| DAYOFMONTH(date) | N/A | Returns the day of a month (an integer between 1 and 31) from SQL date. Equivalent to EXTRACT(DAY FROM date). E.g., DAYOFMONTH(DATE ‘1994-09-27’) returns 27. |\
| DAYOFWEEK(date) | N/A | Returns the day of a week (an integer between 1 and 7) from SQL date. Equivalent to EXTRACT(DOW FROM date). E.g., DAYOFWEEK(DATE ‘1994-09-27’) returns 3. |\
| HOUR(timestamp) | N/A | Returns the hour of a day (an integer between 0 and 23) from SQL timestamp timestamp. Equivalent to EXTRACT(HOUR FROM timestamp). E.g., MINUTE(TIMESTAMP ‘1994-09-27 13:14:15’) returns 14. |\
| MINUTE(timestamp) | N/A | Returns the minute of an hour (an integer between 0 and 59) from SQL timestamp timestamp. Equivalent to EXTRACT(MINUTE FROM timestamp). E.g., MINUTE(TIMESTAMP ‘1994-09-27 13:14:15’) returns 14. |\
| SECOND(timestamp) | N/A | Returns the second of a minute (an integer between 0 and 59) from SQL timestamp. Equivalent to EXTRACT(SECOND FROM timestamp). E.g., SECOND(TIMESTAMP ‘1994-09-27 13:14:15’) returns 15. |\
| FLOOR(timepoint TO timeintervalunit) | TIMEPOINT.floor(TIMEINTERVALUNIT) | Returns a value that rounds timepoint down to the time unit timeintervalunit. E.g., FLOOR(TIME ‘12:44:31’ TO MINUTE) returns 12:44:00. |\
| CEIL(timepoint TO timeintervaluntit) | TIMEPOINT.ceil(TIMEINTERVALUNIT) | Returns a value that rounds timepoint up to the time unit timeintervalunit. E.g., CEIL(TIME ‘12:44:31’ TO MINUTE) returns 12:45:00. |\
| (timepoint1, temporal1) OVERLAPS (timepoint2, temporal2) | temporalOverlaps(TIMEPOINT1, TEMPORAL1, TIMEPOINT2, TEMPORAL2) | Returns TRUE if two time intervals defined by (timepoint1, temporal1) and (timepoint2, temporal2) overlap. The temporal values could be either a time point or a time interval. E.g., (TIME ‘2:55:00’, INTERVAL ‘1’ HOUR) OVERLAPS (TIME ‘3:30:00’, INTERVAL ‘2’ HOUR) returns TRUE; (TIME ‘9:00:00’, TIME ‘10:00:00’) OVERLAPS (TIME ‘10:15:00’, INTERVAL ‘3’ HOUR) returns FALSE. |\
| DATE\_FORMAT(timestamp, string) | dateFormat(TIMESTAMP, STRING) | Converts timestamp to a value of string in the format specified by the date format string. The format string is compatible with Java’s SimpleDateFormat. |\
| TIMESTAMPADD(timeintervalunit, interval, timepoint) | N/A |  |\
| TIMESTAMPDIFF(timepointunit, timepoint1, timepoint2) | timestampDiff(TIMEPOINTUNIT, TIMEPOINT1, TIMEPOINT2) | Returns the (signed) number of timepointunit between timepoint1 and timepoint2. The unit for the interval is given by the first argument, which should be one of the following values: SECOND, MINUTE, HOUR, DAY, MONTH, or YEAR. |\
| CONVERT\_TZ(string1, string2, string3) | convertTz(STRING1, STRING2, STRING3) | Converts a datetime string1 (with default ISO timestamp format ‘yyyy-MM-dd HH:mm:ss’) from time zone string2 to time zone string3. The format of time zone should be either an abbreviation such as “PST”, a full name such as “America/Los\_Angeles”, or a custom ID such as “GMT-08:00”. E.g., CONVERT\_TZ(‘1970-01-01 00:00:00’, ‘UTC’, ‘America/Los\_Angeles’) returns ‘1969-12-31 16:00:00’. |\
| FROM\_UNIXTIME(numeric\[, string\]) | fromUnixtime(NUMERIC\[, STRING\]) | Returns a representation of the numeric argument as a value in string format (default is ‘yyyy-MM-dd HH:mm:ss’). numeric is an internal timestamp value representing seconds since ‘1970-01-01 00:00:00’ UTC, such as produced by the UNIX\_TIMESTAMP() function. The return value is expressed in the session time zone (specified in TableConfig). E.g., FROM\_UNIXTIME(44) returns ‘1970-01-01 00:00:44’ if in UTC time zone, but returns ‘1970-01-01 09:00:44’ if in ‘Asia/Tokyo’ time zone. |\
| UNIX\_TIMESTAMP() | unixTimestamp() | Gets current Unix timestamp in seconds. This function is not deterministic which means the value would be recalculated for each record. |\
| UNIX\_TIMESTAMP(string1\[, string2\]) | unixTimestamp(STRING1\[, STRING2\]) | Converts a date time string string1 with format string2 (by default: yyyy-MM-dd HH:mm:ss if not specified) to Unix timestamp (in seconds), using the specified timezone in table config.<br>If a time zone is specified in the date time string and parsed by UTC+X format such as “yyyy-MM-dd HH:mm:ss.SSS X”, this function will use the specified timezone in the date time string instead of the timezone in table config.<br>If the date time string can not be parsed, the default value Long.MIN\_VALUE(-9223372036854775808) will be returned.<br>```sql<br>Flink SQL> SET 'table.local-time-zone' = 'Europe/Berlin';<br>-- Returns 25201<br>Flink SQL> SELECT UNIX_TIMESTAMP('1970-01-01 08:00:01.001', 'yyyy-MM-dd HH:mm:ss.SSS');<br>-- Returns 1<br>Flink SQL> SELECT UNIX_TIMESTAMP('1970-01-01 08:00:01.001 +0800', 'yyyy-MM-dd HH:mm:ss.SSS X');<br>-- Returns 25201<br>Flink SQL> SELECT UNIX_TIMESTAMP('1970-01-01 08:00:01.001 +0800', 'yyyy-MM-dd HH:mm:ss.SSS');<br>-- Returns -9223372036854775808<br>Flink SQL> SELECT UNIX_TIMESTAMP('1970-01-01 08:00:01.001', 'yyyy-MM-dd HH:mm:ss.SSS X');<br>``` |\
| TO\_DATE(string1\[, string2\]) | toDate(STRING1\[, STRING2\]) | Converts a date string string1 with format string2 (by default ‘yyyy-MM-dd’) to a date. |\
| TO\_TIMESTAMP\_LTZ(numeric\[, precision\]) | toTimestampLtz(NUMERIC, PRECISION) | Converts an epoch seconds or epoch milliseconds to a TIMESTAMP\_LTZ, the valid precision is 0 or 3, the 0 represents TO\_TIMESTAMP\_LTZ(epochSeconds, 0), the 3 represents TO\_TIMESTAMP\_LTZ(epochMilliseconds, 3). If no precision is provided, the default precision is 3. If any input is null, the function will return null. |\
| TO\_TIMESTAMP\_LTZ(string1\[, string2\[, string3\]\]) | toTimestampLtz(STRING1\[, STRING2\[, STRING3\]\]) | Converts a timestamp string string1 with format string2 (by default ‘yyyy-MM-dd HH:mm:ss.SSS’) in time zone string3 (by default ‘UTC’) to a TIMESTAMP\_LTZ. If any input is null, the function will return null. |\
| TO\_TIMESTAMP(string1\[, string2\]) | toTimestamp(STRING1\[, STRING2\]) | Converts date time string string1 with format string2 (by default: ‘yyyy-MM-dd HH:mm:ss’) to a timestamp, without time zone. |\
| CURRENT\_WATERMARK(rowtime) | N/A | Returns the current watermark for the given rowtime attribute, or `NULL` if no common watermark of all upstream operations is available at the current operation in the pipeline.<br>The return type of the function is inferred to match that of the provided rowtime attribute, but with an adjusted precision of 3. For example, if the rowtime attribute is `TIMESTAMP_LTZ(9)`, the function will return `TIMESTAMP_LTZ(3)`.<br>Note that this function can return `NULL`, and you may have to consider this case. For example, if you want to filter out late data you can use:<br>```sql<br>WHERE<br>  CURRENT_WATERMARK(ts) IS NULL<br>  OR ts > CURRENT_WATERMARK(ts)<br>``` |\
\
### Conditional Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#conditional-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| CASE value<br>WHEN value1\_1 \[, value1\_2\]\* THEN RESULT1<br>(WHEN value2\_1 \[, value2\_2 \]\* THEN result\_2)\*<br>(ELSE result\_z)<br>END | N/A | Returns resultX when the first time value is contained in (valueX\_1, valueX\_2, …). When no value matches, returns result\_z if it is provided and returns NULL otherwise. |\
| CASE<br>WHEN condition1 THEN result1<br>(WHEN condition2 THEN result2)\*<br>(ELSE result\_z)<br>END | N/A | Returns resultX when the first conditionX is met. When no condition is met, returns result\_z if it is provided and returns NULL otherwise. |\
| NULLIF(value1, value2) | N/A | Returns NULL if value1 is equal to value2; returns value1 otherwise. E.g., NULLIF(5, 5) returns NULL; NULLIF(5, 0) returns 5. |\
| COALESCE(value1 \[, value2\]\*) | coalesce(value1, \[, value2\]\*) | Returns the first argument that is not NULL.<br>If all arguments are NULL, it returns NULL as well. The return type is the least restrictive, common type of all of its arguments.<br>The return type is nullable if all arguments are nullable as well.<br>```sql<br>-- Returns 'default'<br>COALESCE(NULL, 'default')<br>-- Returns the first non-null value among f0 and f1,<br>-- or 'default' if f0 and f1 are both NULL<br>COALESCE(f0, f1, 'default')<br>``` |\
| IF(condition, true\_value, false\_value) | N/A | Returns the true\_value if condition is met, otherwise false\_value. E.g., IF(5 > 3, 5, 3) returns 5. |\
| IFNULL(input, null\_replacement) | input.ifNull(nullReplacement) | Returns null\_replacement if input is NULL; otherwise input is returned.<br>Compared to COALESCE or CASE WHEN, this function returns a data type that is very specific in terms of nullability. The returned type is the common type of both arguments but only nullable if the null\_replacement is nullable.<br>The function allows to pass nullable columns into a function or table that is declared with a NOT NULL constraint.<br>E.g., IFNULL(nullable\_column, 5) returns never NULL. |\
| IS\_ALPHA(string) | N/A | Returns true if all characters in string are letter, otherwise false. |\
| IS\_DECIMAL(string) | N/A | Returns true if string can be parsed to a valid numeric, otherwise false. |\
| IS\_DIGIT(string) | N/A | Returns true if all characters in string are digit, otherwise false. |\
| N/A | BOOLEAN.?(VALUE1, VALUE2) | Returns VALUE1 if BOOLEAN evaluates to TRUE; returns VALUE2 otherwise. E.g., (42 > 5).?(‘A’, ‘B’) returns “A”. |\
| GREATEST(value1\[, value2\]\*) | N/A | Returns the greatest value of the list of arguments. Returns NULL if any argument is NULL. |\
| LEAST(value1\[, value2\]\*) | N/A | Returns the least value of the list of arguments. Returns NULL if any argument is NULL. |\
\
### Type Conversion Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#type-conversion-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| CAST(value AS type) | ANY.cast(TYPE) | Returns a new value being cast to type type. A CAST error throws an exception and fails the job. When performing a cast operation that may fail, like STRING to INT, one should rather use TRY\_CAST, in order to handle errors. If “table.exec.legacy-cast-behaviour” is enabled, CAST behaves like TRY\_CAST. E.g., CAST(‘42’ AS INT) returns 42; CAST(NULL AS STRING) returns NULL of type STRING; CAST(’non-number’ AS INT) throws an exception and fails the job. |\
| TRY\_CAST(value AS type) | ANY.tryCast(TYPE) | Like CAST, but in case of error, returns NULL rather than failing the job. E.g., TRY\_CAST(‘42’ AS INT) returns 42; TRY\_CAST(NULL AS STRING) returns NULL of type STRING; TRY\_CAST(’non-number’ AS INT) returns NULL of type INT; COALESCE(TRY\_CAST(’non-number’ AS INT), 0) returns 0 of type INT. |\
| TYPEOF(input)<br>TYPEOF(input, force\_serializable) | call("TYPEOF", input)<br>call("TYPEOF", input, force\_serializable) | Returns the string representation of the input expression’s data type. By default, the returned string is a summary string that might omit certain details for readability. If force\_serializable is set to TRUE, the string represents a full data type that could be persisted in a catalog. Note that especially anonymous, inline data types have no serializable string representation. In this case, NULL is returned. |\
\
### Collection Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#collection-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| CARDINALITY(array) | ARRAY.cardinality() | Returns the number of elements in array. |\
| array ‘\[’ INT ‘\]’ | ARRAY.at(INT) | Returns the element at position INT in array. The index starts from 1. |\
| ELEMENT(array) | ARRAY.element() | Returns the sole element of array (whose cardinality should be one); returns NULL if array is empty. Throws an exception if array has more than one element. |\
| CARDINALITY(map) | MAP.cardinality() | Returns the number of entries in map. |\
| map ‘\[’ value ‘\]’ | MAP.at(ANY) | Returns the value specified by key value in map. |\
| ARRAY\_APPEND(array, element) | array.arrayAppend(element) | Appends an element to the end of the array and returns the result. If the array itself is null, the function will return null. If an element to add is null, the null element will be added to the end of the array. |\
| ARRAY\_CONTAINS(haystack, needle) | haystack.arrayContains(needle) | Returns whether the given element exists in an array. Checking for null elements in the array is supported. If the array itself is null, the function will return null. The given element is cast implicitly to the array’s element type if necessary. |\
| ARRAY\_DISTINCT(haystack) | haystack.arrayDistinct() | Returns an array with unique elements. If the array itself is null, the function will return null. Keeps ordering of elements. |\
| ARRAY\_POSITION(haystack, needle) | haystack.arrayPosition(needle) | Returns the position of the first occurrence of element in the given array as int. Returns 0 if the given value could not be found in the array. Returns null if either of the arguments are null. And this is not zero based, but 1-based index. The first element in the array has index 1. |\
| ARRAY\_PREPEND(array, element) | array.arrayPrepend(element) | Appends an element to the beginning of the array and returns the result. If the array itself is null, the function will return null. If an element to add is null, the null element will be added to the beginning of the array. |\
| ARRAY\_REMOVE(haystack, needle) | haystack.arrayRemove(needle) | Removes all elements that equal to element from array. If the array itself is null, the function will return null. Keeps ordering of elements. |\
| ARRAY\_REVERSE(haystack) | haystack.arrayReverse() | Returns an array in reverse order. If the array itself is null, the function will return null. |\
| ARRAY\_SLICE(array, start\_offset\[, end\_offset\]) | array.arraySlice(start\_offset\[, end\_offset\]) | Returns a subarray of the input array between ‘start\_offset’ and ’end\_offset’ inclusive. The offsets are 1-based however 0 is also treated as the beginning of the array. Positive values are counted from the beginning of the array while negative from the end. If ’end\_offset’ is omitted then this offset is treated as the length of the array. If ‘start\_offset’ is after ’end\_offset’ or both are out of array bounds an empty array will be returned. Returns null if any input is null. |\
| ARRAY\_SORT(array\[, ascending\_order\[, null\_first\]\]) | array.arraySort(\[, ascendingOrder\[, null\_first\]\]) | Returns the array in sorted order.The function sorts an array, defaulting to ascending order with NULLs at the start when only the array is input. Specifying ascending\_order as true orders the array in ascending with NULLs first, and setting it to false orders it in descending with NULLs last. Independently, null\_first as true moves NULLs to the beginning, and as false to the end, irrespective of the sorting order. The function returns null if any input is null. |\
| ARRAY\_UNION(array1, array2) | haystack.arrayUnion(array) | Returns an array of the elements in the union of array1 and array2, without duplicates. If any of the array is null, the function will return null. |\
| ARRAY\_CONCAT(array1, …) | array1.arrayConcat(...) | Returns an array that is the result of concatenating at least one array. This array contains all the elements in the first array, followed by all the elements in the second array, and so forth, up to the Nth array. If any input array is NULL, the function returns NULL. |\
| ARRAY\_EXCEPT(array1, array2) | arrayOne.arrayExcept(arrayTwo) | Returns an ARRAY that contains the elements from array1 that are not in array2, without duplicates. If no elements remain after excluding the elements in array2 from array1, the function returns an empty ARRAY. If one or both arguments are NULL, the function returns NULL. The order of the elements from array1 is kept. |\
| ARRAY\_INTERSECT(array1, array2) | array1.arrayIntersect(array2) | Returns an ARRAY that contains the elements from array1 that are also in array2, without duplicates. If no elements that are both in array1 and array2, the function returns an empty ARRAY. If any of the array is null, the function will return null. The order of the elements from array1 is kept. |\
| ARRAY\_MAX(array) | array.arrayMax() | Returns the maximum value from the array, if array itself is null, the function returns null. |\
| ARRAY\_JOIN(array, delimiter\[, nullReplacement\]) | array.arrayJoin(delimiter\[, nullReplacement\]) | Returns a string that represents the concatenation of the elements in the given array and the elements’ data type in the given array is string. The delimiter is a string that separates each pair of consecutive elements of the array. The optional nullReplacement is a string that replaces null elements in the array. If nullReplacement is not specified, null elements in the array will be omitted from the resulting string. Returns null if input array or delimiter or nullReplacement are null. |\
| ARRAY\_MIN(array) | array.arrayMin() | Returns the minimum value from the array, if array itself is null, the function returns null. |\
| MAP\_KEYS(map) | MAP.mapKeys() | Returns the keys of the map as array. No order guaranteed. |\
| MAP\_UNION(map1, …) | map1.mapUnion(...) | Returns a map created by merging at least one map. These maps should have a common map type. If there are overlapping keys, the value from ‘map2’ will overwrite the value from ‘map1’, the value from ‘map3’ will overwrite the value from ‘map2’, the value from ‘mapn’ will overwrite the value from ‘map(n-1)’. If any of maps is null, return null. |\
| MAP\_VALUES(map) | MAP.mapValues() | Returns the values of the map as array. No order guaranteed. |\
| MAP\_ENTRIES(map) | MAP.mapEntries() | Returns an array of all entries in the given map. No order guaranteed. |\
| MAP\_FROM\_ARRAYS(array\_of\_keys, array\_of\_values) | mapFromArrays(array\_of\_keys, array\_of\_values) | Returns a map created from an arrays of keys and values. Note that the lengths of two arrays should be the same. |\
| SPLIT(string, delimiter) | string.split(delimiter) | Returns an array of substrings by splitting the input string based on the given delimiter. If the delimiter is not found in the string, the original string is returned as the only element in the array. If the delimiter is empty, every character in the string is split. If the string or delimiter is null, a null value is returned. If the delimiter is found at the beginning or end of the string, or there are contiguous delimiters, then an empty string is added to the array. |\
\
### JSON Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#json-functions)\
\
JSON functions make use of JSON path expressions as described in ISO/IEC TR 19075-6 of the SQL\
standard. Their syntax is inspired by and adopts many features of ECMAScript, but is neither a\
subset nor superset thereof.\
\
Path expressions come in two flavors, lax and strict. When omitted, it defaults to the strict mode.\
Strict mode is intended to examine data from a schema perspective and will throw errors whenever\
data does not adhere to the path expression. However, functions like `JSON_VALUE` allow defining\
fallback behavior if an error is encountered. Lax mode, on the other hand, is more forgiving and\
converts errors to empty sequences.\
\
The special character `$` denotes the root node in a JSON path. Paths can access properties (`$.a`),\
array elements (`$.a[0].b`), or branch over all elements in an array (`$.a[*].b`).\
\
Known Limitations:\
\
- Not all features of Lax mode are currently supported correctly. This is an upstream bug\
(CALCITE-4717). Non-standard behavior is not guaranteed.\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| IS JSON \[ { VALUE \| SCALAR \| ARRAY \| OBJECT } \] | STRING.isJson(\[JsonType type\]) | Determine whether a given string is valid JSON.<br>Specifying the optional type argument puts a constraint on which type of JSON object is<br>allowed. If the string is valid JSON, but not that type, `false` is returned. The default is<br>`VALUE`.<br>```sql<br>-- TRUE<br>'1' IS JSON<br>'[]' IS JSON<br>'{}' IS JSON<br>-- TRUE<br>'"abc"' IS JSON<br>-- FALSE<br>'abc' IS JSON<br>NULL IS JSON<br>-- TRUE<br>'1' IS JSON SCALAR<br>-- FALSE<br>'1' IS JSON ARRAY<br>-- FALSE<br>'1' IS JSON OBJECT<br>-- FALSE<br>'{}' IS JSON SCALAR<br>-- FALSE<br>'{}' IS JSON ARRAY<br>-- TRUE<br>'{}' IS JSON OBJECT<br>``` |\
| JSON\_EXISTS(jsonValue, path \[ { TRUE \| FALSE \| UNKNOWN \| ERROR } ON ERROR \]) | STRING.jsonExists(STRING path \[, JsonExistsOnError onError\]) | Determines whether a JSON string satisfies a given path search criterion.<br>If the error behavior is omitted, `FALSE ON ERROR` is assumed as the default.<br>```sql<br>-- TRUE<br>SELECT JSON_EXISTS('{"a": true}', '$.a');<br>-- FALSE<br>SELECT JSON_EXISTS('{"a": true}', '$.b');<br>-- TRUE<br>SELECT JSON_EXISTS('{"a": [{ "b": 1 }]}',<br>  '$.a[0].b');<br>-- TRUE<br>SELECT JSON_EXISTS('{"a": true}',<br>  'strict $.b' TRUE ON ERROR);<br>-- FALSE<br>SELECT JSON_EXISTS('{"a": true}',<br>  'strict $.b' FALSE ON ERROR);<br>``` |\
| JSON\_STRING(value) | jsonString(value) | Serializes a value into JSON.<br>This function returns a JSON string containing the serialized value. If the value is `NULL`,<br>the function returns `NULL`.<br>```sql<br>-- NULL<br>JSON_STRING(CAST(NULL AS INT))<br>-- '1'<br>JSON_STRING(1)<br>-- 'true'<br>JSON_STRING(TRUE)<br>-- '"Hello, World!"'<br>JSON_STRING('Hello, World!')<br>-- '[1,2]'<br>JSON_STRING(ARRAY[1, 2])<br>``` |\
| JSON\_VALUE(jsonValue, path \[RETURNING \] \[ { NULL \| ERROR \| DEFAULT  } ON EMPTY \] \[ { NULL \| ERROR \| DEFAULT  } ON ERROR \]) | STRING.jsonValue(STRING path \[, returnType, onEmpty, defaultOnEmpty, onError, defaultOnError\]) | Extracts a scalar from a JSON string.<br>This method searches a JSON string for a given path expression and returns the value if the<br>value at that path is scalar. Non-scalar values cannot be returned. By default, the value is<br>returned as `STRING`. Using `dataType` a different type can be chosen, with the following<br>types being supported:<br>- `VARCHAR` / `STRING`<br>- `BOOLEAN`<br>- `INTEGER`<br>- `DOUBLE`<br>For empty path expressions or errors a behavior can be defined to either return `null`, raise<br>an error or return a defined default value instead. When omitted, the default is<br>`NULL ON EMPTY` or `NULL ON ERROR`, respectively. The default value may be a literal or an<br>expression. If the default value itself raises an error, it falls through to the error<br>behavior for `ON EMPTY`, and raises an error for `ON ERROR`.<br>For path contains special characters such as spaces, you can use `['property']` or `["property"]`<br>to select the specified property in a parent object. Be sure to put single or double quotes around the property name.<br>When using JSON\_VALUE in SQL, the path is a character parameter which is already single quoted,<br>so you have to escape the single quotes around property name, such as `JSON_VALUE('{"a b": "true"}', '$.[''a b'']')`.<br>```sql<br>-- "true"<br>JSON_VALUE('{"a": true}', '$.a')<br>-- TRUE<br>JSON_VALUE('{"a": true}', '$.a' RETURNING BOOLEAN)<br>-- "false"<br>JSON_VALUE('{"a": true}', 'lax $.b'<br>    DEFAULT FALSE ON EMPTY)<br>-- "false"<br>JSON_VALUE('{"a": true}', 'strict $.b'<br>    DEFAULT FALSE ON ERROR)<br>-- 0.998D<br>JSON_VALUE('{"a.b": [0.998,0.996]}','$.["a.b"][0]' <br>    RETURNING DOUBLE)<br>-- "right"<br>JSON_VALUE('{"contains blank": "right"}', 'strict $.[''contains blank'']' NULL ON EMPTY DEFAULT 'wrong' ON ERROR)<br>``` |\
| JSON\_QUERY(jsonValue, path \[RETURNING \] \[ { WITHOUT \| WITH CONDITIONAL \| WITH UNCONDITIONAL } \[ ARRAY \] WRAPPER \] \[ { NULL \| EMPTY ARRAY \| EMPTY OBJECT \| ERROR } ON EMPTY \] \[ { NULL \| EMPTY ARRAY \| EMPTY OBJECT \| ERROR } ON ERROR \]) | STRING.jsonQuery(path \[, returnType \[, JsonQueryWrapper \[, JsonQueryOnEmptyOrError, JsonQueryOnEmptyOrError \] \] \]) | Extracts JSON values from a JSON string.<br>The result is returned as a `STRING` or `ARRAY<STRING>`. This can be controlled with the `RETURNING` clause.<br>The `wrappingBehavior` determines whether the extracted value should be wrapped into an array,<br>and whether to do so unconditionally or only if the value itself isn’t an array already.<br>`onEmpty` and `onError` determine the behavior in case the path expression is empty, or in<br>case an error was raised, respectively. By default, in both cases `null` is returned. Other<br>choices are to use an empty array, an empty object, or to raise an error.<br>```sql<br>-- '{ "b": 1 }'<br>JSON_QUERY('{ "a": { "b": 1 } }', '$.a')<br>-- '[1, 2]'<br>JSON_QUERY('[1, 2]', '$')<br>-- NULL<br>JSON_QUERY(CAST(NULL AS STRING), '$')<br>-- '["c1","c2"]'<br>JSON_QUERY('{"a":[{"c":"c1"},{"c":"c2"}]}',<br>    'lax $.a[*].c')<br>-- ['c1','c2']<br>JSON_QUERY('{"a":[{"c":"c1"},{"c":"c2"}]}', 'lax $.a[*].c' RETURNING ARRAY<STRING>)<br>-- Wrap result into an array<br>-- '[{}]'<br>JSON_QUERY('{}', '$' WITH CONDITIONAL ARRAY WRAPPER)<br>-- '[1, 2]'<br>JSON_QUERY('[1, 2]', '$' WITH CONDITIONAL ARRAY WRAPPER)<br>-- '[[1, 2]]'<br>JSON_QUERY('[1, 2]', '$' WITH UNCONDITIONAL ARRAY WRAPPER)<br>-- Scalars must be wrapped to be returned<br>-- NULL<br>JSON_QUERY(1, '$')<br>-- '[1]'<br>JSON_QUERY(1, '$' WITH CONDITIONAL ARRAY WRAPPER)<br>-- Behavior if path expression is empty / there is an error<br>-- '{}'<br>JSON_QUERY('{}', 'lax $.invalid' EMPTY OBJECT ON EMPTY)<br>-- '[]'<br>JSON_QUERY('{}', 'strict $.invalid' EMPTY ARRAY ON ERROR)<br>``` |\
| JSON\_OBJECT(\[\[KEY\] key VALUE value\]\* \[ { NULL \| ABSENT } ON NULL \]) | jsonObject(JsonOnNull, keyValues...) | Builds a JSON object string from a list of key-value pairs.<br>Note that keys must be non-`NULL` string literals, while values may be arbitrary expressions.<br>This function returns a JSON string. The `ON NULL` behavior defines how to treat `NULL`<br>values. If omitted, `NULL ON NULL` is assumed by default.<br>Values which are created from another JSON construction function call (`JSON_OBJECT`,<br>`JSON_ARRAY`) are inserted directly rather than as a string. This allows building nested JSON<br>structures.<br>```sql<br>-- '{}'<br>JSON_OBJECT()<br>-- '{"K1":"V1","K2":"V2"}'<br>JSON_OBJECT('K1' VALUE 'V1', 'K2' VALUE 'V2')<br>-- Expressions as values<br>JSON_OBJECT('orderNo' VALUE orders.orderId)<br>-- ON NULL<br>JSON_OBJECT(KEY 'K1' VALUE CAST(NULL AS STRING) NULL ON NULL)   -- '{"K1":null}'<br>JSON_OBJECT(KEY 'K1' VALUE CAST(NULL AS STRING) ABSENT ON NULL) -- '{}'<br>-- '{"K1":{"nested_json":{"value":42}}}'<br>JSON_OBJECT('K1' VALUE JSON('{"nested_json": {"value": 42}}'))<br>-- '{"K1":{"K2":"V"}}'<br>JSON_OBJECT(<br>  KEY 'K1'<br>  VALUE JSON_OBJECT(<br>    KEY 'K2'<br>    VALUE 'V'<br>  )<br>)<br>``` |\
| JSON(value) | json(value) | Expects a raw, pre-formatted JSON string and returns its values as-is without escaping it as a string.<br>This function can currently only be used within the `JSON_OBJECT` and `JSON_ARRAY` functions.<br>It allows passing pre-formatted JSON strings that will be inserted directly into the<br>resulting JSON structure rather than being escaped as a string value. This allows storing<br>nested JSON structures in a `JSON_OBJECT` or `JSON_ARRAY` without processing them as strings,<br>which is often useful when ingesting already formatted json data. If the value is NULL or empty,<br>the function returns NULL.<br>```sql<br>-- {"K":{"K2":42}}<br>JSON_OBJECT('K' VALUE JSON('{"K2": 42}'))<br>-- {"K":{"K2":{"K3":42}}}<br>JSON_OBJECT('K' VALUE JSON('{"K2":{"K3":42}}'))<br>-- {"K": null}<br>JSON_OBJECT('K' VALUE JSON(''))<br>-- [{"K2":42}]<br>JSON_ARRAY(JSON('{"K2": 42}'))<br>-- [{"K":{"K1":42}}]<br>JSON_ARRAY(JSON('{"K":{"K1":42}}'))<br>-- [{"K":{"K1":42}}, {"K":{"K1":87}}]<br>JSON_ARRAY(JSON('{"K":{"K1":42}}'), JSON('{"K":{"K1":87}}'))<br>-- [null]<br>JSON_ARRAY(JSON('') NULL ON NULL)<br>-- Invalid - JSON function can only be used within JSON_OBJECT<br>JSON('{"value": 42}')<br>``` |\
| JSON\_ARRAY(\[value\]\* \[ { NULL \| ABSENT } ON NULL \]) | jsonArray(JsonOnNull, values...) | Builds a JSON array string from a list of values.<br>This function returns a JSON string. The values can be arbitrary expressions. The `ON NULL`<br>behavior defines how to treat `NULL` values. If omitted, `ABSENT ON NULL` is assumed by<br>default.<br>Elements which are created from another JSON construction function call (`JSON_OBJECT`,<br>`JSON_ARRAY`) are inserted directly rather than as a string. This allows building nested JSON<br>structures.<br>```sql<br>-- '[]'<br>JSON_ARRAY()<br>-- '[1,"2"]'<br>JSON_ARRAY(1, '2')<br>-- Expressions as values<br>JSON_ARRAY(orders.orderId)<br>-- ON NULL<br>JSON_ARRAY(CAST(NULL AS STRING) NULL ON NULL) -- '[null]'<br>JSON_ARRAY(CAST(NULL AS STRING) ABSENT ON NULL) -- '[]'<br>-- '[[1]]'<br>JSON_ARRAY(JSON_ARRAY(1))<br>-- [{"nested_json":{"value":42}}]<br>JSON_ARRAY(JSON('{"nested_json": {"value": 42}}'))<br>``` |\
\
### Variant Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#variant-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| PARSE\_JSON(json\_string\[, allow\_duplicate\_keys\]) | N/A | Parse a JSON string into a Variant. If the JSON string is invalid, an error will be thrown.<br>To return NULL instead of an error, use the `TRY_PARSE_JSON` function.<br>If there are duplicate keys in the input JSON string, when `allowDuplicateKeys` is true, the<br>parser will keep the last occurrence of all fields with the same key, otherwise when<br>`allowDuplicateKeys` is false it will throw an error. The default value of<br>`allowDuplicateKeys` is false. |\
| TRY\_PARSE\_JSON(json\_string\[, allow\_duplicate\_keys\]) | N/A | Try to parse a JSON string into a Variant if possible. If the JSON string is invalid, return<br>NULL. To throw an error instead of returning NULL, use the `PARSE_JSON` function.<br>If there are duplicate keys in the input JSON string, when `allowDuplicateKeys` is true, the<br>parser will keep the last occurrence of all fields with the same key, otherwise when<br>`allowDuplicateKeys` is false it will throw an error. The default value of<br>`allowDuplicateKeys` is false. |\
\
### Value Construction Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#value-construction-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| **implicit** constructor with parenthesis<br>(value1 \[, value2\]\*)<br>**explicit** ROW constructor with<br>ROW(value1 \[, value2\]\*) | row(ANY1, ANY2, ...) | Returns a row created from a list of values (value1, value2,…).<br>The implicit row constructor requires at least two fields. The explicit row constructor can deal with an arbitrary number of fields. Both of them support arbitrary expressions as fields. |\
| ARRAY ‘\[’ value1 \[, value2 \]\* ‘\]’ | array(ANY1, ANY2, ...) | Returns an array created from a list of values (value1, value2, …). |\
| MAP ‘\[’ value1, value2 \[, value3, value4 \]\* ‘\]’ | map(ANY1, ANY2, ANY3, ANY4, ...) | Returns a map created from a list of key-value pairs ((value1, value2), (value3, value4), …). |\
| DESCRIPTOR ‘(’ identifier1 \[, identifier2 \]\* ‘)’ | descriptor(STRING1, STRING2, ...) | Returns a literal describing an arbitrary, unvalidated list of column names. Passing a list of columns<br>can be useful for parameterizing a function. In particular, it enables declaring the `on_time` argument<br>for process table functions (PTFs).<br>```sql<br>f(columns => DESCRIPTOR(`col1`, `col2`), on_time => DESCRIPTOR(`ts`))<br>``` |\
| OBJECT\_OF(className, \[key, value \[, key, value , …\]\]) | objectOf(STRING, Object...) | Creates a structured object from a list of key-value pairs.<br>This function creates an instance of a structured type identified by the given class name.<br>The structured type is created by providing alternating key-value pairs where keys must be<br>string literals and values can be arbitrary expressions.<br>Note: The class name is only used for distinguishing two structured types with identical fields.<br>Structured types are internally handled with suitable data structures. Thus, serialization and equality checks are managed by the system.<br>In Table API and UDF calls, the system will attempt to resolve the class name to an actual implementation class.<br>In this case the class name needs to be present in the user classpath. If resolution fails, Row is used as a fallback.<br>```sql<br>-- Creates a User object with complex fields "name", "age", and "address"<br>OBJECT_OF('com.example.User', 'name', 'Bob', 'age', 21, 'address', OBJECT_OF('com.example.Address', 'street', 'primary', 'city', 'Berlin'))<br>``` |\
| N/A | NUMERIC.rows | Creates a NUMERIC interval of rows (commonly used in window creation). |\
\
### Value Access Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#value-access-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| tableName.compositeType.field | COMPOSITE.get(STRING)<br>COMPOSITE.get(INT) | Returns the value of a field from a Flink composite type (e.g., Tuple, POJO) by name. |\
| tableName.compositeType.\* | ANY.flatten() | Returns a flat representation of a Flink composite type (e.g., Tuple, POJO) that converts each of its direct subtype into a separate field. In most cases the fields of the flat representation are named similarly to the original fields but with a dollar separator (e.g., mypojo$mytuple$f0). |\
\
### Grouping Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#grouping-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| GROUP\_ID() | N/A | Returns an integer that uniquely identifies the combination of grouping keys. |\
| GROUPING(expression1 \[, expression2\]\* )<br>GROUPING\_ID(expression1 \[, expression2\]\* ) | N/A | Returns a bit vector of the given grouping expressions. |\
\
### Hash Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#hash-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| MD5(string) | STRING.md5() | Returns the MD5 hash of string as a string of 32 hexadecimal digits; returns NULL if string is NULL. |\
| SHA1(string) | STRING.sha1() | Returns the SHA-1 hash of string as a string of 40 hexadecimal digits; returns NULL if string is NULL. |\
| SHA224(string) | STRING.sha224() | Returns the SHA-224 hash of string as a string of 56 hexadecimal digits; returns NULL if string is NULL. |\
| SHA256(string) | STRING.sha256() | Returns the SHA-256 hash of string as a string of 64 hexadecimal digits; returns NULL if string is NULL. |\
| SHA384(string) | STRING.sha384() | Returns the SHA-384 hash of string as a string of 96 hexadecimal digits; returns NULL if string is NULL. |\
| SHA512(string) | STRING.sha512() | Returns the SHA-512 hash of string as a string of 128 hexadecimal digits; returns NULL if string is NULL. |\
| SHA2(string, hashLength) | STRING.sha2(INT) | Returns the hash using the SHA-2 family of hash functions (SHA-224, SHA-256, SHA-384, or SHA-512). The first argument string is the string to be hashed and the second argument hashLength is the bit length of the result (224, 256, 384, or 512). Returns NULL if string or hashLength is NULL. |\
\
### Auxiliary Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#auxiliary-functions)\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
\
## Aggregate Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#aggregate-functions)\
\
The aggregate functions take an expression across all the rows as the input and return a single aggregated value as the result.\
\
| SQL Function | Table Function | Description |\
| --- | --- | --- |\
| COUNT(\[ ALL \] expression \| DISTINCT expression1 \[, expression2\]\*) | N/A | By default or with ALL, returns the number of input rows for which expression is not NULL. Use DISTINCT for one unique instance of each value. |\
| COUNT(\*)<br>COUNT(1) | FIELD.count | Returns the number of input rows. |\
| AVG(\[ ALL \| DISTINCT \] expression) | FIELD.avg | By default or with keyword ALL, returns the average (arithmetic mean) of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| SUM(\[ ALL \| DISTINCT \] expression) | FIELD.sum | By default or with keyword ALL, returns the sum of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| N/A | FIELD.sum0 | Returns the sum of numeric field FIELD across all input rows. If all values are NULL, returns 0. |\
| MAX(\[ ALL \| DISTINCT \] expression) | FIELD.max | By default or with keyword ALL, returns the maximum value of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| MIN(\[ ALL \| DISTINCT \] expression ) | FIELD.min | By default or with keyword ALL, returns the minimum value of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| STDDEV\_POP(\[ ALL \| DISTINCT \] expression) | FIELD.stddevPop | By default or with keyword ALL, returns the population standard deviation of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| STDDEV\_SAMP(\[ ALL \| DISTINCT \] expression) | FIELD.stddevSamp | By default or with keyword ALL, returns the sample standard deviation of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| VAR\_POP(\[ ALL \| DISTINCT \] expression) | FIELD.varPop | By default or with keyword ALL, returns the population variance (square of the population standard deviation) of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| VAR\_SAMP(\[ ALL \| DISTINCT \] expression) | FIELD.varSamp | By default or with keyword ALL, returns the sample variance (square of the sample standard deviation) of expression across all input rows. Use DISTINCT for one unique instance of each value. |\
| COLLECT(\[ ALL \| DISTINCT \] expression) | FIELD.collect | By default or with keyword ALL, returns a multiset of expression across all input rows. NULL values will be ignored. Use DISTINCT for one unique instance of each value. |\
| VARIANCE(\[ ALL \| DISTINCT \] expression) | N/A | Synonyms for VAR\_SAMP(). |\
| RANK() | N/A | Returns the rank of a value in a group of values. The result is one plus the number of rows preceding or equal to the current row in the ordering of the partition. The values will produce gaps in the sequence. |\
| DENSE\_RANK() | N/A | Returns the rank of a value in a group of values. The result is one plus the previously assigned rank value. Unlike the function rank, dense\_rank will not produce gaps in the ranking sequence. |\
| ROW\_NUMBER() | N/A | Assigns a unique, sequential number to each row, starting with one, according to the ordering of rows within the window partition. ROW\_NUMBER and RANK are similar. ROW\_NUMBER numbers all rows sequentially (for example 1, 2, 3, 4, 5). RANK provides the same numeric value for ties (for example 1, 2, 2, 4, 5). |\
| LEAD(expression \[, offset\] \[, default\]) | lead(expression \[, offset\] \[, default\]) | Returns the value of expression at the offsetth row after the current row in the window. The default value of offset is 1 and the default value of default is NULL. |\
| LAG(expression \[, offset\] \[, default\]) | lag(expression \[, offset\] \[, default\]) | Returns the value of expression at the offsetth row before the current row in the window. The default value of offset is 1 and the default value of default is NULL. |\
| FIRST\_VALUE(expression) | FIELD.firstValue | Returns the first value in an ordered set of values. |\
| LAST\_VALUE(expression) | FIELD.lastValue | Returns the last value in an ordered set of values. |\
| LISTAGG(expression \[, separator\]) | FIELD.listagg | Concatenates the values of string expressions and places separator values between them. The separator is not added at the end of string. The default value of separator is ‘,’. |\
| CUME\_DIST() | N/A | Return the cumulative distribution of a value in a group of values. The result is the number of rows preceding or equal to the current row in the ordering of the partition divided by the number of rows in the window partition. |\
| PERCENT\_RANK() | N/A | Return the percentage ranking of a value in a group of values. The result is the rank value minus one, divided by the number of rows in the parition minus one. If the partition only contains one row, the function will return 0. |\
| NTILE(n) | N/A | Divides the rows for each window partition into `n` buckets ranging from 1 to at most `n`.<br>If the number of rows in the window partition doesn’t divide evenly into the number of buckets, then the remainder values are distributed one per bucket, starting with the first bucket.<br>For example, with 6 rows and 4 buckets, the bucket values would be as follows: 1 1 2 2 3 4 |\
| ARRAY\_AGG(\[ ALL \| DISTINCT \] expression \[ RESPECT NULLS \| IGNORE NULLS \]) | FIELD.arrayAgg | By default or with keyword `ALL` and, return an array that concatenates the input rows<br>and returns `NULL` if there are no input rows. Use `DISTINCT` for one unique instance of each value.<br>By default `NULL` values are respected, use `IGNORE NULLS` to skip `NULL` values.<br>The `ORDER BY` clause is currently not supported. |\
| JSON\_OBJECTAGG(\[KEY\] key VALUE value \[ { NULL \| ABSENT } ON NULL \]) | jsonObjectAgg(JsonOnNull, keyExpression, valueExpression) | Builds a JSON object string by aggregating key-value expressions into a single JSON object.<br>The key expression must return a non-nullable character string. Value expressions can be<br>arbitrary, including other JSON functions. If a value is `NULL`, the `ON NULL` behavior<br>defines what to do. If omitted, `NULL ON NULL` is assumed by default.<br>Note that keys must be unique. If a key occurs multiple times, an error will be thrown.<br>This function is currently not supported in `OVER` windows.<br>```sql<br>-- '{"Apple":2,"Banana":17,"Orange":0}'<br>SELECT<br>  JSON_OBJECTAGG(KEY product VALUE cnt)<br>FROM orders<br>``` |\
| JSON\_ARRAYAGG(items \[ { NULL \| ABSENT } ON NULL \]) | jsonArrayAgg(JsonOnNull, itemExpression) | Builds a JSON object string by aggregating items into an array.<br>Item expressions can be arbitrary, including other JSON functions. If a value is `NULL`, the<br>`ON NULL` behavior defines what to do. If omitted, `ABSENT ON NULL` is assumed by default.<br>This function is currently not supported in `OVER` windows, unbounded session windows, or hop<br>windows.<br>```sql<br>-- '["Apple","Banana","Orange"]'<br>SELECT<br>  JSON_ARRAYAGG(product)<br>FROM orders<br>``` |\
\
## Time Interval and Point Unit Specifiers  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#time-interval-and-point-unit-specifiers)\
\
The following table lists specifiers for time interval and time point units.\
\
For Table API, please use `_` for spaces (e.g., `DAY_TO_HOUR`).\
Plural works for SQL only.\
\
| Time Interval Unit | Time Point Unit |\
| --- | --- |\
| `MILLENNIUM` |  |\
| `CENTURY` |  |\
| `DECADE` |  |\
| `YEAR(S)` | `YEAR` |\
| `YEAR(S) TO MONTH(S)` |  |\
| `QUARTER(S)` | `QUARTER` |\
| `MONTH(S)` | `MONTH` |\
| `WEEK(S)` | `WEEK` |\
| `DAY(S)` | `DAY` |\
| `DAY(S) TO HOUR(S)` |  |\
| `DAY(S) TO MINUTE(S)` |  |\
| `DAY(S) TO SECOND(S)` |  |\
| `HOUR(S)` | `HOUR` |\
| `HOUR(S) TO MINUTE(S)` |  |\
| `HOUR(S) TO SECOND(S)` |  |\
| `MINUTE(S)` | `MINUTE` |\
| `MINUTE(S) TO SECOND(S)` |  |\
| `SECOND(S)` | `SECOND` |\
| `MILLISECOND` | `MILLISECOND` |\
| `MICROSECOND` | `MICROSECOND` |\
| `NANOSECOND` |  |\
| `EPOCH` |  |\
| `DOY` _(SQL-only)_ |  |\
| `DOW` _(SQL-only)_ |  |\
| `EPOCH` _(SQL-only)_ |  |\
| `ISODOW` _(SQL-only)_ |  |\
| `ISOYEAR` _(SQL-only)_ |  |\
|  | `SQL_TSI_YEAR` _(SQL-only)_ |\
|  | `SQL_TSI_QUARTER` _(SQL-only)_ |\
|  | `SQL_TSI_MONTH` _(SQL-only)_ |\
|  | `SQL_TSI_WEEK` _(SQL-only)_ |\
|  | `SQL_TSI_DAY` _(SQL-only)_ |\
|  | `SQL_TSI_HOUR` _(SQL-only)_ |\
|  | `SQL_TSI_MINUTE` _(SQL-only)_ |\
|  | `SQL_TSI_SECOND` _(SQL-only)_ |\
\
## Column Functions  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#column-functions)\
\
The column functions are used to select or deselect table columns.\
\
> Column functions are only used in Table API.\
\
| SYNTAX | DESC |\
| --- | --- |\
| withColumns(…) | select the specified columns |\
| withoutColumns(…) | deselect the columns specified |\
| withAllColumns() | select all columns (like `SELECT *` in SQL) |\
\
The detailed syntax is as follows:\
\
```text\
columnFunction:\
    withColumns(columnExprs)\
    withoutColumns(columnExprs)\
    withAllColumns()\
\
columnExprs:\
    columnExpr [, columnExpr]*\
\
columnExpr:\
    columnRef | columnIndex to columnIndex | columnName to columnName\
\
columnRef:\
    columnName(The field name that exists in the table) | columnIndex(a positive integer starting from 1)\
```\
\
The usage of the column function is illustrated in the following table. (Suppose we have a table with 5 columns: `(a: Int, b: Long, c: String, d:String, e: String)`):\
\
| API | Usage | Description |\
| --- | --- | --- |\
| withColumns($(\*)) | select(withColumns($("\*"))) = select($(“a”), $(“b”), $(“c”), $(“d”), $(“e”)) | all the columns |\
| withColumns(m to n) | select(withColumns(range(2, 4))) = select($(“b”), $(“c”), $(“d”)) | columns from m to n |\
| withColumns(m, n, k) | select(withColumns(lit(1), lit(3), $(“e”))) = select($(“a”), $(“c”), $(“e”)) | columns m, n, k |\
| withColumns(m, n to k) | select(withColumns(lit(1), range(3, 5))) = select($(“a”), $(“c”), $(“d”), $(“e”)) | mixing of the above two representation |\
| withoutColumns(m to n) | select(withoutColumns(range(2, 4))) = select($(“a”), $(“e”)) | deselect columns from m to n |\
| withoutColumns(m, n, k) | select(withoutColumns(lit(1), lit(3), lit(5))) = select($(“b”), $(“d”)) | deselect columns m, n, k |\
| withoutColumns(m, n to k) | select(withoutColumns(lit(1), range(3, 5))) = select($(“b”)) | mixing of the above two representation |\
\
The column functions can be used in all places where column fields are expected, such as `select, groupBy, orderBy, UDFs etc.` e.g.:\
\
Java\
\
```java\
table\
    .groupBy(withColumns(range(1, 3)))\
    .select(withColumns(range("a", "b")), myUDAgg(myUDF(withColumns(range(5, 20)))));\
```\
\
Scala\
\
```scala\
table\
    .groupBy(withColumns(range(1, 3)))\
    .select(withColumns('a to 'b), myUDAgg(myUDF(withColumns(5 to 20))))\
```\
\
Python\
\
```python\
table \\
    .group_by(with_columns(range_(1, 3))) \\
    .select(with_columns(range_('a', 'b')), myUDAgg(myUDF(with_columns(range_(5, 20)))))\
```\
\
## Named Arguments  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/table/functions/systemfunctions/\#named-arguments)\
\
By default, values and expressions are mapped to a function’s arguments based on the position in the function call,\
for example `f(42, true)`. All functions in both SQL and Table API support position-based arguments.\
\
If the function declares a static signature, named arguments are available as a convenient alternative.\
The framework is able to reorder named arguments and consider optional arguments accordingly, before passing them\
into the function call. Thus, the order of arguments doesn’t matter when calling a function and optional arguments\
don’t have to be provided.\
\
In `DESCRIBE FUNCTION` and documentation a static signature is indicated by the `=>` assignment operator,\
for example `f(left => INT, right => BOOLEAN)`. Note that not every function supports named arguments. Named\
arguments are not available for signatures that are overloaded, use varargs, or any other kind of input type strategy.\
User-defined functions with a single `eval()` method usually qualify for named arguments.\
\
Named arguments can be used as shown below:\
\
SQL\
\
```text\
SELECT MyUdf(input => my_column, threshold => 42)\
```\
\
Table API\
\
```java\
table.select(\
  call(\
    MyUdf.class,\
    $("my_column").asArgument("input"),\
    lit(42).asArgument("threshold")\
  )\
);\
```