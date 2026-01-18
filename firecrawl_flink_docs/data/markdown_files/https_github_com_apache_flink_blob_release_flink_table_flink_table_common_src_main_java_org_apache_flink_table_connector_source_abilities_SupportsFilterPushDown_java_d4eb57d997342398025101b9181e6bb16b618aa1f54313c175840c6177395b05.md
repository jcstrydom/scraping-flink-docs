[Skip to content](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java) to refresh your session.Dismiss alert

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

# SupportsFilterPushDown.java

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

![Airblader](https://avatars.githubusercontent.com/u/2392216?v=4&size=40)![twalthr](https://avatars.githubusercontent.com/u/5746567?v=4&size=40)

[Airblader](https://github.com/apache/flink/commits?author=Airblader)

and

[twalthr](https://github.com/apache/flink/commits?author=twalthr)

[\[](https://github.com/apache/flink/commit/a09cc4704433cb76b936a51b422d812e1ae57945) [FLINK-25047](https://issues.apache.org/jira/browse/FLINK-25047) [\]\[table\] Resolve architectural violations](https://github.com/apache/flink/commit/a09cc4704433cb76b936a51b422d812e1ae57945)

Open commit details

5 years agoNov 30, 2021

[a09cc47](https://github.com/apache/flink/commit/a09cc4704433cb76b936a51b422d812e1ae57945) · 5 years agoNov 30, 2021

## History

[History](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java)

Open commit details

[View commit history for this file.](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java)

113 lines (103 loc) · 4.46 KB

/

# SupportsFilterPushDown.java

Top

## File metadata and controls

- Code

- Blame


113 lines (103 loc) · 4.46 KB

[Raw](https://github.com/apache/flink/raw/refs/heads/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/source/abilities/SupportsFilterPushDown.java)

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

packageorg.apache.flink.table.connector.source.abilities;

importorg.apache.flink.annotation.PublicEvolving;

importorg.apache.flink.table.connector.source.ScanTableSource;

importorg.apache.flink.table.expressions.ExpressionVisitor;

importorg.apache.flink.table.expressions.ResolvedExpression;

importjava.util.List;

/\*\*

\\* Enables to push down filters into a {@link ScanTableSource}.

\*

\\* <p>Given the following SQL:

\*

\\* <pre>{@code

\\* SELECT \* FROM t WHERE (a = '1' OR a = '2') AND b IS NOT NULL;

\\* }</pre>

\*

\\* <p>In the example above, {@code \[a = '1' OR a = '2'\]} and {@code \[b IS NOT NULL\]} are acceptable

\\* filters.

\*

\\* <p>By default, if this interface is not implemented, filters are applied in a subsequent

\\* operation after the source.

\*

\\* <p>For efficiency, a source can push filters further down in order to be close to the actual data

\\* generation. The passed filters are translated into conjunctive form. A source can pick filters

\\* and return the accepted and remaining filters.

\*

\\* <p>Accepted filters are filters that are consumed by the source but may be applied on a best

\\* effort basis. The information about accepted filters helps the planner to adjust the cost

\\* estimation for the current plan. A subsequent filter operation will still take place by the

\\* runtime depending on the remaining filters.

\*

\\* <p>Remaining filters are filters that cannot be fully applied by the source. The remaining

\\* filters decide if a subsequent filter operation will still take place by the runtime.

\*

\\* <p>By the above definition, accepted filters and remaining filters must not be disjunctive lists.

\\* A filter can occur in both list. However, all given filters must be present in at least one list.

\*

\\* <p>Note: A source is not allowed to change the given expressions in the returned {@link Result}.

\*

\\* <p>Use {@link ExpressionVisitor} to traverse filter expressions.

\*/

@PublicEvolving

publicinterfaceSupportsFilterPushDown {

/\*\*

\\* Provides a list of filters in conjunctive form. A source can pick filters and return the

\\* accepted and remaining filters.

\*

\\* <p>See the documentation of {@link SupportsFilterPushDown} for more information.

\*/

ResultapplyFilters(List<ResolvedExpression\> filters);

/\*\*

\\* Result of a filter push down. It represents the communication of the source to the planner

\\* during optimization.

\*/

@PublicEvolving

finalclassResult {

privatefinalList<ResolvedExpression\> acceptedFilters;

privatefinalList<ResolvedExpression\> remainingFilters;

privateResult(

List<ResolvedExpression\> acceptedFilters,

List<ResolvedExpression\> remainingFilters) {

this.acceptedFilters = acceptedFilters;

this.remainingFilters = remainingFilters;

}

/\*\*

\\* Constructs a filter push-down result.

\*

\\* <p>See the documentation of {@link SupportsFilterPushDown} for more information.

\*

\\* @param acceptedFilters filters that are consumed by the source but may be applied on a

\\* best effort basis

\\* @param remainingFilters filters that a subsequent filter operation still needs to perform

\\* during runtime

\*/

publicstaticResultof(

List<ResolvedExpression\> acceptedFilters,

List<ResolvedExpression\> remainingFilters) {

returnnewResult(acceptedFilters, remainingFilters);

}

publicList<ResolvedExpression\> getAcceptedFilters() {

returnacceptedFilters;

}

publicList<ResolvedExpression\> getRemainingFilters() {

returnremainingFilters;

}

}

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.