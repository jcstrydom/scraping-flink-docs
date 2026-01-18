[Skip to content](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) to refresh your session.Dismiss alert

{{ message }}

[apache](https://github.com/apache)/ **[flink-training](https://github.com/apache/flink-training)** Public

- [Notifications](https://github.com/login?return_to=%2Fapache%2Fflink-training) You must be signed in to change notification settings
- [Fork\\
702](https://github.com/login?return_to=%2Fapache%2Fflink-training)
- [Star\\
1k](https://github.com/login?return_to=%2Fapache%2Fflink-training)


## File tree

Expand file treeCollapse file tree

## 2 files changed

+4

-4

lines changed

Open diff view settings

Filter options

- [README.md](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)

- [README\_zh.md](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c#diff-bc53aca037f8d406f619f15cf2c5c905a7a61f81f89cab98dd52f7ff65725f6e)


Expand file treeCollapse file tree

## 2 files changed

+4

-4

lines changed

Open diff view settings

Collapse file

### [`‎README.md‎`](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c\#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)

Copy file name to clipboardExpand all lines: README.md

+3-3Lines changed: 3 additions & 3 deletions

- Display the source diff
- Display the rich diff

| Original file line number | Diff line number | Diff line change |
| --- | --- | --- |
| `@@ -31,7 +31,7 @@ Exercises that accompany the training content in the documentation.<br>` |
| `31` | `31` | `1. [Clone and build the flink-training project](#clone-and-build-the-flink-training-project)<br>` |
| `32` | `32` | `1. [Import the flink-training project into your IDE](#import-the-flink-training-project-into-your-ide)<br>` |
| `33` | `33` | `<br>` |
| `34` | `` | `-[**Use the taxi data streams**](#using-the-taxi-data-streams)<br>` |
| `` | `34` | `+[**Use the taxi data streams**](#use-the-taxi-data-streams)<br>` |
| `35` | `35` | `<br>` |
| `36` | `36` | `1. [Schema of taxi ride events](#schema-of-taxi-ride-events)<br>` |
| `37` | `37` | `1. [Schema of taxi fare events](#schema-of-taxi-fare-events)<br>` |
| `@@ -148,7 +148,7 @@ Our taxi data set contains information about individual taxi rides in New York C<br>` |
| `148` | `148` | `<br>` |
| `149` | `149` | `Each ride is represented by two events: a trip start, and a trip end.<br>` |
| `150` | `150` | `<br>` |
| `151` | `` | `-Each event consists of eleven fields:<br>` |
| `` | `151` | `+Each event consists of ten fields:<br>` |
| `152` | `152` | `<br>` |
| `153` | `153` | ``````<br>``` |
| `154` | `154` | `rideId         : Long      // a unique id for each ride<br>` |
| `@@ -189,7 +189,7 @@ We assume you have set up your development environment according to our [setup g<br>` |\
| `189` | `189` | `### Learn about the data<br>` |\
| `190` | `190` | `<br>` |\
| `191` | `191` | `The initial set of exercises are all based on data streams of events about taxi rides and taxi fares. These streams are produced by source functions which reads data from input files.<br>` |\
| `192` | `` | `-Read the [instructions](#using-the-taxi-data-streams) to learn how to use them.<br>` |\
| `` | `192` | `+Read the [instructions](#use-the-taxi-data-streams) to learn how to use them.<br>` |\
| `193` | `193` | `<br>` |\
| `194` | `194` | `### Run and debug Flink programs in your IDE<br>` |\
| `195` | `195` | `<br>` |\
| `<br>` |\
\
Collapse file\
\
### [`‎README_zh.md‎`](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c\#diff-bc53aca037f8d406f619f15cf2c5c905a7a61f81f89cab98dd52f7ff65725f6e)\
\
Copy file name to clipboardExpand all lines: README\_zh.md\
\
+1-1Lines changed: 1 addition & 1 deletion\
\
- Display the source diff\
- Display the rich diff\
\
| Original file line number | Diff line number | Diff line change |\
| --- | --- | --- |\
| `@@ -156,7 +156,7 @@ org.gradle.project.enable_scala = true<br>` |\
| `156` | `156` | `<br>` |\
| `157` | `157` | `每次车程都由两个事件表示：行程开始(trip start)和行程结束(trip end)。<br>` |\
| `158` | `158` | `<br>` |\
| `159` | `` | `-每个事件都由十一个字段组成：<br>` |\
| `` | `159` | `+每个事件都由十个字段组成：<br>` |\
| `160` | `160` | `<br>` |\
| `161` | `161` | ``````<br>``` |\
| `162` | `162` | `rideId         : Long      // 每次车程的唯一id<br>` |\
| `<br>` |\
\
## 0 commit comments\
\
Comments\
\
0 (0)\
\
Please [sign in](https://github.com/login?return_to=https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) to comment.\
\
You can’t perform that action at this time.