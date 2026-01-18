[Skip to content](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java) to refresh your session.Dismiss alert

{{ message }}

[apache](https://github.com/apache)/ **[flink](https://github.com/apache/flink)** Public

- [Notifications](https://github.com/login?return_to=%2Fapache%2Fflink) You must be signed in to change notification settings
- [Fork\\
13.8k](https://github.com/login?return_to=%2Fapache%2Fflink)
- [Star\\
25.7k](https://github.com/login?return_to=%2Fapache%2Fflink)


## Collapse file tree

## Files

View file on default branch

release-1.20

Search this repository

/

# SupportsRowLevelUpdate.java

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

![luoyuxia](https://avatars.githubusercontent.com/u/20389154?v=4&size=40)![lincoln-lil](https://avatars.githubusercontent.com/u/3712895?v=4&size=40)

[luoyuxia](https://github.com/apache/flink/commits?author=luoyuxia)

and

[lincoln-lil](https://github.com/apache/flink/commits?author=lincoln-lil)

[\[](https://github.com/apache/flink/commit/904c695776a6c28e67c50ce21115141a99446aa8) [FLINK-30661](https://issues.apache.org/jira/browse/FLINK-30661) [\]\[table\] introduce SupportsRowLevelUpdate interface](https://github.com/apache/flink/commit/904c695776a6c28e67c50ce21115141a99446aa8)

4 years agoJan 16, 2023

[904c695](https://github.com/apache/flink/commit/904c695776a6c28e67c50ce21115141a99446aa8) · 4 years agoJan 16, 2023

## History

[History](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java)

Open commit details

[View commit history for this file.](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java)

113 lines (103 loc) · 4.59 KB

/

# SupportsRowLevelUpdate.java

Top

## File metadata and controls

- Code

- Blame


113 lines (103 loc) · 4.59 KB

[Raw](https://github.com/apache/flink/raw/refs/heads/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelUpdate.java)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

/\*

\\* Licensed to the Apache Software Foundation (ASF) under one

\\* or more contributor license agreements. See the NOTICE file

\\* distributed with this work for additional information

\\* regarding copyright ownership. The ASF licenses this file

\\* to you under the Apache License, Version 2.0 (the

\\* "License"); you may not use this file except in compliance

\\* with the License. You may obtain a copy of the License at

\*

\\* http://www.apache.org/licenses/LICENSE-2.0

\*

\\* Unless required by applicable law or agreed to in writing, software

\\* distributed under the License is distributed on an "AS IS" BASIS,

\\* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

\\* See the License for the specific language governing permissions and

\\* limitations under the License.

\*/

packageorg.apache.flink.table.connector.sink.abilities;

importorg.apache.flink.annotation.PublicEvolving;

importorg.apache.flink.table.catalog.Column;

importorg.apache.flink.table.connector.RowLevelModificationScanContext;

importorg.apache.flink.table.connector.sink.DynamicTableSink;

importorg.apache.flink.table.connector.source.abilities.SupportsRowLevelModificationScan;

importjavax.annotation.Nullable;

importjava.util.List;

importjava.util.Optional;

/\*\*

\\* Interface for {@link DynamicTableSink}s that support update existing data according to row-level

\\* changes. The table sink is responsible for telling planner how to produce the row changes, and

\\* consuming them to achieve the purpose of row(s) update.

\*

\\* <p>The planner will call method {@link #applyRowLevelUpdate(List,

\\* RowLevelModificationScanContext)} to get the {@link RowLevelUpdateInfo} returned by sink, and

\\* rewrite the update statement based on the retrieved {@link RowLevelUpdateInfo} to produce rows to

\\* {@link DynamicTableSink}.

\*/

@PublicEvolving

publicinterfaceSupportsRowLevelUpdate {

/\*\*

\\* Applies row-level update with providing the updated columns and {@link

\\* RowLevelModificationScanContext}, and return {@link RowLevelUpdateInfo}.

\*

\\* @param updatedColumns the columns updated by update statement in table column order.

\\* @param context the context passed by table source which implement {@link

\\* SupportsRowLevelModificationScan}. It'll be null if the table source doesn't implement

\\* it.

\*/

RowLevelUpdateInfoapplyRowLevelUpdate(

List<Column\> updatedColumns, @NullableRowLevelModificationScanContextcontext);

/\\*\\* The information that guides the planner on how to rewrite the update statement. \*/

@PublicEvolving

interfaceRowLevelUpdateInfo {

/\*\*

\\* The required columns by the sink to perform row-level update. The rows consumed by sink

\\* will contain the required columns in order. If return Optional.empty(), it will contain

\\* all columns.

\*/

defaultOptional<List<Column>\> requiredColumns() {

returnOptional.empty();

}

/\*\*

\\* Planner will rewrite the update statement to query base on the {@link

\\* RowLevelUpdateMode}, keeping the query of update unchanged by default(in \`UPDATED\_ROWS\`

\\* mode), or changing the query to union the updated rows and the other rows (in \`ALL\_ROWS\`

\\* mode).

\*

\\* <p>Take the following SQL as an example:

\*

\\* <pre>{@code

\\* UPDATE t SET x = 1 WHERE y = 2;

\\* }</pre>

\*

\\* <p>If returns {@link RowLevelUpdateMode#UPDATED\_ROWS}, the sink will get the update after

\\* rows which match the filter \[y = 2\].

\*

\\* <p>If returns {@link RowLevelUpdateMode#ALL\_ROWS}, the sink will get both the update

\\* after rows which match the filter \[y = 2\] and the other rows that don't match the filter

\\* \[y = 2\].

\*

\\* <p>Note: All rows will have RowKind#UPDATE\_AFTER when RowLevelUpdateMode is UPDATED\_ROWS,

\\* and RowKind#INSERT when RowLevelUpdateMode is ALL\_ROWS.

\*/

defaultRowLevelUpdateModegetRowLevelUpdateMode() {

returnRowLevelUpdateMode.UPDATED\_ROWS;

}

}

/\*\*

\\* Type of update modes that the sink expects for update purpose.

\*

\\* <p>Currently, two modes are supported:

\*

\\* <ul>

\\* <li>UPDATED\_ROWS - in this mode, the sink will only get the update after rows.

\\* <li>ALL\_ROWS - in this mode, the sink will get all the rows including both the update after

\\* rows and the other rows that don't need to be updated.

\\* </ul>

\*/

@PublicEvolving

enumRowLevelUpdateMode {

UPDATED\_ROWS,

ALL\_ROWS

}

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.