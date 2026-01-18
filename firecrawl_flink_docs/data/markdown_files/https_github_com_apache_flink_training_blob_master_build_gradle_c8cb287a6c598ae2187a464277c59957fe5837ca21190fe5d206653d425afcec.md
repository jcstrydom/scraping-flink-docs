[Skip to content](https://github.com/apache/flink-training/blob/master/build.gradle#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/build.gradle) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/build.gradle) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/build.gradle) to refresh your session.Dismiss alert

{{ message }}

[apache](https://github.com/apache)/ **[flink-training](https://github.com/apache/flink-training)** Public

- [Notifications](https://github.com/login?return_to=%2Fapache%2Fflink-training) You must be signed in to change notification settings
- [Fork\\
702](https://github.com/login?return_to=%2Fapache%2Fflink-training)
- [Star\\
1k](https://github.com/login?return_to=%2Fapache%2Fflink-training)


## Collapse file tree

## Files

master

Search this repository

/

# build.gradle

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

[![Myasuka](https://avatars.githubusercontent.com/u/1709104?v=4&size=40)](https://github.com/Myasuka)[Myasuka](https://github.com/apache/flink-training/commits?author=Myasuka)

[\[](https://github.com/apache/flink-training/commit/983035c1799ae985b6dbcac5320de4b8a866819f) [FLINK-32096](https://issues.apache.org/jira/browse/FLINK-32096) [\] Upgrade to](https://github.com/apache/flink-training/commit/983035c1799ae985b6dbcac5320de4b8a866819f) [flink-1](https://issues.apache.org/jira/browse/FLINK-1) [.17 version](https://github.com/apache/flink-training/commit/983035c1799ae985b6dbcac5320de4b8a866819f)

3 years agoMay 15, 2023

[983035c](https://github.com/apache/flink-training/commit/983035c1799ae985b6dbcac5320de4b8a866819f) · 3 years agoMay 15, 2023

## History

[History](https://github.com/apache/flink-training/commits/master/build.gradle)

Open commit details

[View commit history for this file.](https://github.com/apache/flink-training/commits/master/build.gradle)

291 lines (254 loc) · 12.1 KB

/

# build.gradle

Top

## File metadata and controls

- Code

- Blame


291 lines (254 loc) · 12.1 KB

[Raw](https://github.com/apache/flink-training/raw/refs/heads/master/build.gradle)

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

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

/\*

\\* Licensed to the Apache Software Foundation (ASF) under one or more

\\* contributor license agreements. See the NOTICE file distributed with

\\* this work for additional information regarding copyright ownership.

\\* The ASF licenses this file to You under the Apache License, Version 2.0

\\* (the "License"); you may not use this file except in compliance with

\\* the License. You may obtain a copy of the License at

\*

\\* http://www.apache.org/licenses/LICENSE-2.0

\*

\\* Unless required by applicable law or agreed to in writing, software

\\* distributed under the License is distributed on an "AS IS" BASIS,

\\* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

\\* See the License for the specific language governing permissions and

\\* limitations under the License.

\*/

plugins {

id 'com.github.johnrengelman.shadow' version '7.0.0' apply false

id "com.diffplug.spotless" version "6.4.2" apply false

}

description ="Flink Training Exercises"

allprojects {

group ='org.apache.flink'

version ='1.17-SNAPSHOT'

apply plugin: 'com.diffplug.spotless'

spotless {

format 'misc', {

target '\*.gradle', '\*.md', '.gitignore'

trimTrailingWhitespace()

indentWithSpaces(4)

endWithNewline()

}

format 'markdown', {

target '\*.md'

licenseHeader '<!--\\n'+

'Licensed to the Apache Software Foundation (ASF) under one\\n'+

'or more contributor license agreements. See the NOTICE file\\n'+

'distributed with this work for additional information\\n'+

'regarding copyright ownership. The ASF licenses this file\\n'+

'to you under the Apache License, Version 2.0 (the\\n'+

'"License"); you may not use this file except in compliance\\n'+

'with the License. You may obtain a copy of the License at\\n'+

'\\n'+

' http://www.apache.org/licenses/LICENSE-2.0\\n'+

'\\n'+

'Unless required by applicable law or agreed to in writing,\\n'+

'software distributed under the License is distributed on an\\n'+

'"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\\n'+

'KIND, either express or implied. See the License for the\\n'+

'specific language governing permissions and limitations\\n'+

'under the License.\\n'+

'-->\\n\\n', '(# )\|(\\\\[.\*\\\\]\\\(.\*\\\))'

}

format 'gradle', {

target '\*.gradle'

licenseHeader '/\*\\n'+

' \\* Licensed to the Apache Software Foundation (ASF) under one or more\\n'+

' \\* contributor license agreements. See the NOTICE file distributed with\\n'+

' \\* this work for additional information regarding copyright ownership.\\n'+

' \\* The ASF licenses this file to You under the Apache License, Version 2.0\\n'+

' \\* (the "License"); you may not use this file except in compliance with\\n'+

' \\* the License. You may obtain a copy of the License at\\n'+

' \*\\n'+

' \\* http://www.apache.org/licenses/LICENSE-2.0\\n'+

' \*\\n'+

' \\* Unless required by applicable law or agreed to in writing, software\\n'+

' \\* distributed under the License is distributed on an "AS IS" BASIS,\\n'+

' \\* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n'+

' \\* See the License for the specific language governing permissions and\\n'+

' \\* limitations under the License.\\n'+

' \*/\\n\\n', '(.\*\\\{)\|(.\\* = .\*)\|(apply plugin:)'

}

}

}

subprojects {

apply plugin: 'java'

if (project.properties\['org.gradle.project.enable\_scala'\].trim() =='true') {

apply plugin: 'scala'

}

apply plugin: 'com.github.johnrengelman.shadow'

apply plugin: 'checkstyle'

apply plugin: 'eclipse'

ext {

javaVersion ='1.8'

flinkVersion ='1.17.0'

scalaBinaryVersion ='2.12'

log4jVersion ='2.12.1'

junitVersion ='4.13'

}

sourceCompatibility = javaVersion

targetCompatibility = javaVersion

tasks.withType(JavaCompile) {

options.encoding ='UTF-8'

}

// declare where to find the dependencies of your project

repositories {

// for access from China, you may need to uncomment this line

// maven { url 'https://maven.aliyun.com/repository/public/' }

mavenCentral()

maven {

url "https://repository.apache.org/content/repositories/snapshots/"

mavenContent {

snapshotsOnly()

}

}

}

// common set of dependencies

dependencies {

shadow "org.apache.logging.log4j:log4j-slf4j-impl:${log4jVersion}"

shadow "org.apache.logging.log4j:log4j-api:${log4jVersion}"

shadow "org.apache.logging.log4j:log4j-core:${log4jVersion}"

shadow "org.apache.flink:flink-clients:${flinkVersion}"

shadow "org.apache.flink:flink-java:${flinkVersion}"

shadow "org.apache.flink:flink-streaming-java:${flinkVersion}"

shadow "org.apache.flink:flink-streaming-scala\_${scalaBinaryVersion}:${flinkVersion}"

// allows using Flink's web UI when running in the IDE:

shadow "org.apache.flink:flink-runtime-web:${flinkVersion}"

if (project != project(":common")) {

implementation project(path: ':common')

testImplementation(project(":common")) {

capabilities { requireCapability("$group:common-test") }

}

}

}

// add solution source dirs:

sourceSets {

main.java.srcDirs +='src/solution/java'

tasks.withType(ScalaCompile) {

main.scala.srcDirs +='src/solution/scala'

}

// Add shadow configuration to runtime class path so that the

// dynamically-generated tasks by IntelliJ are able to run and have

// all dependencies they need. (Luckily, this does not influence what

// ends up in the final shadowJar.)

main.runtimeClasspath += configurations.shadow

test.compileClasspath += configurations.shadow

test.runtimeClasspath += configurations.shadow

}

project.plugins.withId('application') {

\['javaExerciseClassName', 'javaSolutionClassName'\].each { property->

createTrainingRunTask(project, property)

}

}

pluginManager.withPlugin('scala') {

project.plugins.withId('application') {

\['scalaExerciseClassName', 'scalaSolutionClassName'\].each { property->

createTrainingRunTask(project, property)

}

}

}

spotless {

java {

googleJavaFormat('1.7').aosp()

// \\# refers to static imports

importOrder('org.apache.flink', 'org.apache.flink.shaded', '', 'javax', 'java', 'scala', '\\\#')

removeUnusedImports()

targetExclude("\*\*/generated\*/\*.java")

licenseHeader '/\*\\n'+

' \\* Licensed to the Apache Software Foundation (ASF) under one\\n'+

' \\* or more contributor license agreements. See the NOTICE file\\n'+

' \\* distributed with this work for additional information\\n'+

' \\* regarding copyright ownership. The ASF licenses this file\\n'+

' \\* to you under the Apache License, Version 2.0 (the\\n'+

' \\* "License"); you may not use this file except in compliance\\n'+

' \\* with the License. You may obtain a copy of the License at\\n'+

' \*\\n'+

' \\* http://www.apache.org/licenses/LICENSE-2.0\\n'+

' \*\\n'+

' \\* Unless required by applicable law or agreed to in writing, software\\n'+

' \\* distributed under the License is distributed on an "AS IS" BASIS,\\n'+

' \\* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n'+

' \\* See the License for the specific language governing permissions and\\n'+

' \\* limitations under the License.\\n'+

' \*/\\n\\n'

}

}

pluginManager.withPlugin('scala') {

spotless {

scala {

scalafmt('2.7.5').configFile("${rootProject.projectDir}/.scalafmt.conf")

licenseHeader '/\*\\n'+

' \\* Licensed to the Apache Software Foundation (ASF) under one\\n'+

' \\* or more contributor license agreements. See the NOTICE file\\n'+

' \\* distributed with this work for additional information\\n'+

' \\* regarding copyright ownership. The ASF licenses this file\\n'+

' \\* to you under the Apache License, Version 2.0 (the\\n'+

' \\* "License"); you may not use this file except in compliance\\n'+

' \\* with the License. You may obtain a copy of the License at\\n'+

' \*\\n'+

' \\* http://www.apache.org/licenses/LICENSE-2.0\\n'+

' \*\\n'+

' \\* Unless required by applicable law or agreed to in writing, software\\n'+

' \\* distributed under the License is distributed on an "AS IS" BASIS,\\n'+

' \\* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n'+

' \\* See the License for the specific language governing permissions and\\n'+

' \\* limitations under the License.\\n'+

' \*/\\n\\n', 'package '

}

}

}

jar {

manifest {

attributes 'Built-By': System.getProperty('user.name'),

'Build-Jdk': System.getProperty('java.version')

}

}

shadowJar {

mergeServiceFiles()

dependencies {

exclude(dependency("org.apache.flink:force-shading"))

exclude(dependency('com.google.code.findbugs:jsr305'))

exclude(dependency('org.slf4j:.\*'))

exclude(dependency('log4j:.\*'))

exclude(dependency('org.apache.logging.log4j:log4j-to-slf4j'))

// already provided dependencies from serializer frameworks

exclude(dependency('com.esotericsoftware.kryo:kryo'))

exclude(dependency('javax.servlet:servlet-api')) // TODO: check if needed

exclude(dependency('org.apache.httpcomponents:httpclient')) // TODO: check if needed

}

}

assemble.dependsOn(shadowJar)

}

tasks.register('printRunTasks') {

println'\-\-\----------------------------------------------------------'

println'Flink Training Tasks runnable from root project \\''+ project.name +'\\''

println'\-\-\----------------------------------------------------------'

subprojects.findAll { project->

boolean first =true;

project.tasks.withType(JavaExec) { task->

if (task.group =='flink-training') {

if (first) {

println''

println'\> Subproject \\''+ project.name +'\\''

first =false;

}

println'./gradlew :'+ project.name +':'+ task.name

}

}

}

}

staticdefvoidcreateTrainingRunTask(Projectproject, Stringproperty) {

if (project.ext.has(property)) {

project.tasks.create(name: classNamePropertyToTaskName(property), type: JavaExec) {

classpath = project.sourceSets.main.runtimeClasspath

mainClass = project.ext.get(property)

group ='flink-training'

}

}

}

staticdefStringclassNamePropertyToTaskName(Stringproperty) {

return'run'+

property.charAt(0).toString().toUpperCase() +

property.substring(1, property.lastIndexOf('ClassName'))

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.