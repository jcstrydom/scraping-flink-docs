[Skip to content](https://github.com/apache/flink/blob/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink/blob/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java) to refresh your session.Dismiss alert

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

# StateBackendFactory.java

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

![Rufus Refactor](https://github.githubassets.com/images/gravatars/gravatar-user-420.png?size=40)![zentol](https://avatars.githubusercontent.com/u/5725237?v=4&size=40)

Rufus Refactor

and

[zentol](https://github.com/apache/flink/commits?author=zentol)

[\[](https://github.com/apache/flink/commit/c6997c97c575d334679915c328792b8a3067cfb5) [FLINK-20651](https://issues.apache.org/jira/browse/FLINK-20651) [\] Format code with Spotless/google-java-format](https://github.com/apache/flink/commit/c6997c97c575d334679915c328792b8a3067cfb5)

6 years agoDec 28, 2020

[c6997c9](https://github.com/apache/flink/commit/c6997c97c575d334679915c328792b8a3067cfb5) · 6 years agoDec 28, 2020

## History

[History](https://github.com/apache/flink/commits/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java)

Open commit details

[View commit history for this file.](https://github.com/apache/flink/commits/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java)

51 lines (46 loc) · 2.09 KB

/

# StateBackendFactory.java

Top

## File metadata and controls

- Code

- Blame


51 lines (46 loc) · 2.09 KB

[Raw](https://github.com/apache/flink/raw/refs/heads/release-1.20/flink-runtime/src/main/java/org/apache/flink/runtime/state/StateBackendFactory.java)

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

packageorg.apache.flink.runtime.state;

importorg.apache.flink.annotation.PublicEvolving;

importorg.apache.flink.configuration.IllegalConfigurationException;

importorg.apache.flink.configuration.ReadableConfig;

importjava.io.IOException;

/\*\*

\\* A factory to create a specific state backend. The state backend creation gets a Configuration

\\* object that can be used to read further config values.

\*

\\* <p>The state backend factory is typically specified in the configuration to produce a configured

\\* state backend.

\*

\\* @param <T> The type of the state backend created.

\*/

@PublicEvolving

publicinterfaceStateBackendFactory<TextendsStateBackend\> {

/\*\*

\\* Creates the state backend, optionally using the given configuration.

\*

\\* @param config The Flink configuration (loaded by the TaskManager).

\\* @param classLoader The class loader that should be used to load the state backend.

\\* @return The created state backend.

\\* @throws IllegalConfigurationException If the configuration misses critical values, or

\\* specifies invalid values

\\* @throws IOException If the state backend initialization failed due to an I/O exception

\*/

TcreateFromConfig(ReadableConfigconfig, ClassLoaderclassLoader)

throwsIllegalConfigurationException, IOException;

}

You can’t perform that action at this time.


While the code is focused, press Alt+F1 for a menu of operations.