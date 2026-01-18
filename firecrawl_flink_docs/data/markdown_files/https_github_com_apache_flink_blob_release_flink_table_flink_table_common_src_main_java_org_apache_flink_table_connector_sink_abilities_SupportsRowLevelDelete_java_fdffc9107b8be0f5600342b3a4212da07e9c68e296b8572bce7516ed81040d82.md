[Skip to content](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java) to refresh your session.Dismiss alert

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

# SupportsRowLevelDelete.java

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

![luoyuxia](https://avatars.githubusercontent.com/u/20389154?v=4&size=40)![lincoln-lil](https://avatars.githubusercontent.com/u/3712895?v=4&size=40)

[luoyuxia](https://github.com/apache/flink/commits?author=luoyuxia)

and

[lincoln-lil](https://github.com/apache/flink/commits?author=lincoln-lil)

[\[](https://github.com/apache/flink/commit/e25ea3fe1d9ed3ab9f62ac01eb4aaec57b2c6ed2) [FLINK-30661](https://issues.apache.org/jira/browse/FLINK-30661) [\]\[table\] introduce SupportsRowLevelDelete interface](https://github.com/apache/flink/commit/e25ea3fe1d9ed3ab9f62ac01eb4aaec57b2c6ed2)

4 years agoJan 16, 2023

[e25ea3f](https://github.com/apache/flink/commit/e25ea3fe1d9ed3ab9f62ac01eb4aaec57b2c6ed2) · 4 years agoJan 16, 2023

## History

[History](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java)

Open commit details

[View commit history for this file.](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java)

114 lines (103 loc) · 4.65 KB

/

# SupportsRowLevelDelete.java

Top

## File metadata and controls

- Code

- Blame


114 lines (103 loc) · 4.65 KB

[Raw](https://github.com/apache/flink/raw/refs/heads/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/abilities/SupportsRowLevelDelete.java)

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

114

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

\\* Interface for {@link DynamicTableSink}s that support delete existing data according to row-level

\\* changes. The table sink is responsible for telling planner how to produce the row changes, and

\\* consuming them to achieve the purpose of row(s) deletion.

\*

\\* <p>The planner will call the method {@link #applyRowLevelDelete(RowLevelModificationScanContext)}

\\* to get the {@link RowLevelDeleteInfo} returned by sink, and rewrite the delete statement based on

\\* the retrieved {@link RowLevelDeleteInfo} to produce rows to {@link DynamicTableSink}.

\*

\\* <p>Note: For the cases where the table sink implement both {@link SupportsDeletePushDown} and

\\* {@link SupportsRowLevelDelete}, the planner always prefers {@link SupportsDeletePushDown} over

\\* {@link SupportsRowLevelDelete} on condition that {@link

\\* SupportsDeletePushDown#applyDeleteFilters(List)} return true.

\*/

@PublicEvolving

publicinterfaceSupportsRowLevelDelete {

/\*\*

\\* Applies row-level delete with {@link RowLevelModificationScanContext}, and return a {@link

\\* RowLevelDeleteInfo}.

\*

\\* @param context the context passed by table source which implement {@link

\\* SupportsRowLevelModificationScan}. It'll be null if the table source doesn't implement

\\* it.

\*/

RowLevelDeleteInfoapplyRowLevelDelete(@NullableRowLevelModificationScanContextcontext);

/\\*\\* The information that guides the planner on how to rewrite the delete statement. \*/

@PublicEvolving

interfaceRowLevelDeleteInfo {

/\*\*

\\* The required columns by the sink to perform row-level delete. The rows consumed by sink

\\* will contain the required columns in order. If return Optional.empty(), it will contain

\\* all columns.

\*/

defaultOptional<List<Column>\> requiredColumns() {

returnOptional.empty();

}

/\*\*

\\* Planner will rewrite delete statement to query base on the {@link RowLevelDeleteInfo},

\\* keeping the query of delete unchanged by default(in \`DELETE\_ROWS\` mode), or changing the

\\* query to the complementary set in REMAINING\_ROWS mode.

\*

\\* <p>Take the following SQL as an example:

\*

\\* <pre>{@code

\\* DELETE FROM t WHERE y = 2;

\\* }</pre>

\*

\\* <p>If returns {@link SupportsRowLevelDelete.RowLevelDeleteMode#DELETED\_ROWS}, the sink

\\* will get the rows to be deleted which match the filter \[y = 2\].

\*

\\* <p>If returns {@link SupportsRowLevelDelete.RowLevelDeleteMode#REMAINING\_ROWS}, the sink

\\* will get the rows which don't match the filter \[y = 2\].

\*

\\* <p>Note: All rows will be of RowKind#DELETE when RowLevelDeleteMode is DELETED\_ROWS, and

\\* RowKind#INSERT when RowLevelDeleteMode is REMAINING\_ROWS.

\*/

defaultRowLevelDeleteModegetRowLevelDeleteMode() {

returnRowLevelDeleteMode.DELETED\_ROWS;

}

}

/\*\*

\\* Type of delete modes that the sink expects for delete purpose.

\*

\\* <p>Currently, two modes are supported:

\*

\\* <ul>

\\* <li>DELETED\_ROWS - in this mode, the sink will only get the rows that need to be deleted.

\\* <li>REMAINING\_ROWS - in this mode, the sink will only get the remaining rows after

\\* deletion.

\\* </ul>

\*/

@PublicEvolving

enumRowLevelDeleteMode {

DELETED\_ROWS,

REMAINING\_ROWS

}

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.