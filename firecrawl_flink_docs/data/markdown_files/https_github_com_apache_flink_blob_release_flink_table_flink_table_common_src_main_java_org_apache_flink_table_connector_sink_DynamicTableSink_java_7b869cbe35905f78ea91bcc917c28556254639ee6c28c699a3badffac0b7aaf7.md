[Skip to content](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java) to refresh your session.Dismiss alert

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

# DynamicTableSink.java

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

![jnh5y](https://avatars.githubusercontent.com/u/1915111?v=4&size=40)![twalthr](https://avatars.githubusercontent.com/u/5746567?v=4&size=40)

[jnh5y](https://github.com/apache/flink/commits?author=jnh5y)

and

[twalthr](https://github.com/apache/flink/commits?author=twalthr)

[\[](https://github.com/apache/flink/commit/6c9ac5c6ae06bf5b42d33b57a7dc1006ac2b2744) [FLINK-33495](https://issues.apache.org/jira/browse/FLINK-33495) [\]\[](https://github.com/apache/flink/commit/6c9ac5c6ae06bf5b42d33b57a7dc1006ac2b2744) [FLINK-33496](https://issues.apache.org/jira/browse/FLINK-33496) [\] Add DISTRIBUTED BY clause for CREATE TABLE](https://github.com/apache/flink/commit/6c9ac5c6ae06bf5b42d33b57a7dc1006ac2b2744)

Open commit details

2 years agoFeb 19, 2024

[6c9ac5c](https://github.com/apache/flink/commit/6c9ac5c6ae06bf5b42d33b57a7dc1006ac2b2744) · 2 years agoFeb 19, 2024

## History

[History](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java)

Open commit details

[View commit history for this file.](https://github.com/apache/flink/commits/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java)

230 lines (211 loc) · 9.87 KB

/

# DynamicTableSink.java

Top

## File metadata and controls

- Code

- Blame


230 lines (211 loc) · 9.87 KB

[Raw](https://github.com/apache/flink/raw/refs/heads/release-1.20/flink-table/flink-table-common/src/main/java/org/apache/flink/table/connector/sink/DynamicTableSink.java)

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

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

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

packageorg.apache.flink.table.connector.sink;

importorg.apache.flink.annotation.PublicEvolving;

importorg.apache.flink.api.common.typeinfo.TypeInformation;

importorg.apache.flink.table.catalog.ResolvedSchema;

importorg.apache.flink.table.connector.ChangelogMode;

importorg.apache.flink.table.connector.RuntimeConverter;

importorg.apache.flink.table.connector.sink.abilities.SupportsBucketing;

importorg.apache.flink.table.connector.sink.abilities.SupportsOverwrite;

importorg.apache.flink.table.connector.sink.abilities.SupportsPartitioning;

importorg.apache.flink.table.connector.sink.abilities.SupportsWritingMetadata;

importorg.apache.flink.table.data.RowData;

importorg.apache.flink.table.types.DataType;

importorg.apache.flink.table.types.logical.LogicalType;

importorg.apache.flink.types.Row;

importorg.apache.flink.types.RowKind;

importjavax.annotation.Nullable;

importjava.io.Serializable;

importjava.util.Optional;

/\*\*

\\* Sink of a dynamic table to an external storage system.

\*

\\* <p>Dynamic tables are the core concept of Flink's Table & SQL API for processing both bounded and

\\* unbounded data in a unified fashion. By definition, a dynamic table can change over time.

\*

\\* <p>When writing a dynamic table, the content can always be considered as a changelog (finite or

\\* infinite) for which all changes are written out continuously until the changelog is exhausted.

\\* The given {@link ChangelogMode} indicates the set of changes that the sink accepts during

\\* runtime.

\*

\\* <p>For regular batch scenarios, the sink can solely accept insert-only rows and write out bounded

\\* streams.

\*

\\* <p>For regular streaming scenarios, the sink can solely accept insert-only rows and can write out

\\* unbounded streams.

\*

\\* <p>For change data capture (CDC) scenarios, the sink can write out bounded or unbounded streams

\\* with insert, update, and delete rows. See also {@link RowKind}.

\*

\\* <p>Instances of {@link DynamicTableSink} can be seen as factories that eventually produce

\\* concrete runtime implementation for writing the actual data.

\*

\\* <p>Depending on the optionally declared abilities, the planner might apply changes to an instance

\\* and thus mutate the produced runtime implementation.

\*

\\* <p>A {@link DynamicTableSink} can implement the following abilities:

\*

\\* <ul>

\\* <li>{@link SupportsBucketing}

\\* <li>{@link SupportsPartitioning}

\\* <li>{@link SupportsOverwrite}

\\* <li>{@link SupportsWritingMetadata}

\\* </ul>

\*

\\* <p>In the last step, the planner will call {@link #getSinkRuntimeProvider(Context)} for obtaining

\\* a provider of runtime implementation.

\*/

@PublicEvolving

publicinterfaceDynamicTableSink {

/\*\*

\\* Returns the set of changes that the sink accepts during runtime.

\*

\\* <p>The planner can make suggestions but the sink has the final decision what it requires. If

\\* the planner does not support this mode, it will throw an error. For example, the sink can

\\* return that it only supports {@link ChangelogMode#insertOnly()}.

\*

\\* @param requestedMode expected set of changes by the current plan

\*/

ChangelogModegetChangelogMode(ChangelogModerequestedMode);

/\*\*

\\* Returns a provider of runtime implementation for writing the data.

\*

\\* <p>There might exist different interfaces for runtime implementation which is why {@link

\\* SinkRuntimeProvider} serves as the base interface. Concrete {@link SinkRuntimeProvider}

\\* interfaces might be located in other Flink modules.

\*

\\* <p>Independent of the provider interface, the table runtime expects that a sink

\\* implementation accepts internal data structures (see {@link RowData} for more information).

\*

\\* <p>The given {@link Context} offers utilities by the planner for creating runtime

\\* implementation with minimal dependencies to internal data structures.

\*

\\* <p>{@link SinkV2Provider} is the recommended core interface. {@link SinkProvider}, {@code

\\* SinkFunctionProvider} in {@code flink-table-api-java-bridge} and {@link OutputFormatProvider}

\\* are available for backwards compatibility.

\*

\\* @see SinkV2Provider

\*/

SinkRuntimeProvidergetSinkRuntimeProvider(Contextcontext);

/\*\*

\\* Creates a copy of this instance during planning. The copy should be a deep copy of all

\\* mutable members.

\*/

DynamicTableSinkcopy();

/\\*\\* Returns a string that summarizes this sink for printing to a console or log. \*/

StringasSummaryString();

// --------------------------------------------------------------------------------------------

// Helper interfaces

// --------------------------------------------------------------------------------------------

/\*\*

\\* Context for creating runtime implementation via a {@link SinkRuntimeProvider}.

\*

\\* <p>It offers utilities by the planner for creating runtime implementation with minimal

\\* dependencies to internal data structures.

\*

\\* <p>Methods should be called in {@link #getSinkRuntimeProvider(Context)}. The returned

\\* instances are {@link Serializable} and can be directly passed into the runtime implementation

\\* class.

\*/

@PublicEvolving

interfaceContext {

/\*\*

\\* Returns whether a runtime implementation can expect a finite number of rows.

\*

\\* <p>This information might be derived from the session's execution mode and/or kind of

\\* query.

\*/

booleanisBounded();

/\*\*

\\* Creates type information describing the internal data structures of the given {@link

\\* DataType}.

\*

\\* @see ResolvedSchema#toPhysicalRowDataType()

\*/

<T\> TypeInformation<T\> createTypeInformation(DataTypeconsumedDataType);

/\*\*

\\* Creates type information describing the internal data structures of the given {@link

\\* LogicalType}.

\*/

<T\> TypeInformation<T\> createTypeInformation(LogicalTypeconsumedLogicalType);

/\*\*

\\* Creates a converter for mapping between Flink's internal data structures and objects

\\* specified by the given {@link DataType} that can be passed into a runtime implementation.

\*

\\* <p>For example, {@link RowData} and its fields can be converted into a {@link Row}, or

\\* the internal representation for structured types can be converted back into the original

\\* (possibly nested) POJO.

\*

\\* @see LogicalType#supportsOutputConversion(Class)

\*/

DataStructureConvertercreateDataStructureConverter(DataTypeconsumedDataType);

/\*\*

\\* Returns an {@link Optional} array of column index paths related to user specified target

\\* column list or {@link Optional#empty()} when not specified. The array indices are 0-based

\\* and support composite columns within (possibly nested) structures.

\*

\\* <p>This information comes from the column list of the DML clause, e.g., for a sink table

\\* t1 which schema is: {@code a STRING, b ROW < b1 INT, b2 STRING>, c BIGINT}

\*

\\* <ul>

\\* <li>insert: 'insert into t1(a, b.b2) ...', the column list will be 'a, b.b2', and will

\\* return {@code \[\[0\], \[1, 1\]\]}. The statement 'insert into t1 select ...' without

\\* specifying a column list will return {@link Optional#empty()}.

\\* <li>update: 'update t1 set a=1, b.b1=2 where ...', the column list will be 'a, b.b1',

\\* and will return {@code \[\[0\], \[1, 0\]\]}.

\\* </ul>

\*

\\* <p>Note: will always return empty for the delete statement because it has no column list.

\*/

Optional<int\[\]\[\]\> getTargetColumns();

}

/\*\*

\\* Converter for mapping between Flink's internal data structures and objects specified by the

\\* given {@link DataType} that can be passed into a runtime implementation.

\*

\\* <p>For example, {@link RowData} and its fields can be converted into a {@link Row}, or the

\\* internal representation for structured types can be converted back into the original

\\* (possibly nested) POJO.

\*

\\* @see LogicalType#supportsOutputConversion(Class)

\*/

@PublicEvolving

interfaceDataStructureConverterextendsRuntimeConverter {

/\\*\\* Converts the given internal structure into an external object. \*/

@Nullable

ObjecttoExternal(@NullableObjectinternalStructure);

}

/\*\*

\\* Provides actual runtime implementation for writing the data.

\*

\\* <p>There might exist different interfaces for runtime implementation which is why {@link

\\* SinkRuntimeProvider} serves as the base interface. Concrete {@link SinkRuntimeProvider}

\\* interfaces might be located in other Flink modules.

\*

\\* <p>{@link SinkV2Provider} is the recommended core interface. {@link SinkProvider}, {@code

\\* SinkFunctionProvider} in {@code flink-table-api-java-bridge} and {@link OutputFormatProvider}

\\* are available for backwards compatibility.

\*

\\* @see SinkV2Provider

\*/

@PublicEvolving

interfaceSinkRuntimeProvider {

// marker interface

}

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.