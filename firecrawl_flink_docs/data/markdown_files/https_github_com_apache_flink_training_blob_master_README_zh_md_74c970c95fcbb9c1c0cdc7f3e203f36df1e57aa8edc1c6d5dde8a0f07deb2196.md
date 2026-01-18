[Skip to content](https://github.com/apache/flink-training/blob/master/README_zh.md#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/README_zh.md) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/README_zh.md) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/apache/flink-training/blob/master/README_zh.md) to refresh your session.Dismiss alert

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

# README\_zh.md

Copy path

BlameMore file actions

BlameMore file actions

## Latest commit

[![yoda-mon](https://avatars.githubusercontent.com/u/14937752?v=4&size=40)](https://github.com/yoda-mon)[yoda-mon](https://github.com/apache/flink-training/commits?author=yoda-mon)

[\[](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) [FLINK-33711](https://issues.apache.org/jira/browse/FLINK-33711) [\] Fix numbers of field of the taxi event / Fix broken link (](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c)

Open commit details

3 years agoDec 1, 2023

[dc81157](https://github.com/apache/flink-training/commit/dc81157f826649b6084d968689f623ce41a1b46c) · 3 years agoDec 1, 2023

## History

[History](https://github.com/apache/flink-training/commits/master/README_zh.md)

Open commit details

[View commit history for this file.](https://github.com/apache/flink-training/commits/master/README_zh.md)

274 lines (184 loc) · 11.1 KB

/

# README\_zh.md

Top

## File metadata and controls

- Preview

- Code

- Blame


274 lines (184 loc) · 11.1 KB

[Raw](https://github.com/apache/flink-training/raw/refs/heads/master/README_zh.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Apache Flink 实践练习

[Permalink: Apache Flink 实践练习](https://github.com/apache/flink-training/blob/master/README_zh.md#apache-flink-%E5%AE%9E%E8%B7%B5%E7%BB%83%E4%B9%A0)

与文档中实践练习内容相关的练习。

## 目录

[Permalink: 目录](https://github.com/apache/flink-training/blob/master/README_zh.md#%E7%9B%AE%E5%BD%95)

[**设置开发环境**](https://github.com/apache/flink-training/blob/master/README_zh.md#set-up-your-development-environment)

1. [软件要求](https://github.com/apache/flink-training/blob/master/README_zh.md#software-requirements)
2. [克隆并构建 flink-training 项目](https://github.com/apache/flink-training/blob/master/README_zh.md#clone-and-build-the-flink-training-project)
3. [将 flink-training 项目导入 IDE](https://github.com/apache/flink-training/blob/master/README_zh.md#import-the-flink-training-project-into-your-ide)

[**使用出租车数据流(taxi data stream)**](https://github.com/apache/flink-training/blob/master/README_zh.md#using-the-taxi-data-streams)

1. [出租车车程(taxi ride)事件结构](https://github.com/apache/flink-training/blob/master/README_zh.md#schema-of-taxi-ride-events)
2. [出租车费用(taxi fare)事件结构](https://github.com/apache/flink-training/blob/master/README_zh.md#schema-of-taxi-fare-events)

[**如何做练习**](https://github.com/apache/flink-training/blob/master/README_zh.md#how-to-do-the-lab-exercises)

1. [了解数据](https://github.com/apache/flink-training/blob/master/README_zh.md#learn-about-the-data)
2. [在 IDE 中运行和调试 Flink 程序](https://github.com/apache/flink-training/blob/master/README_zh.md#run-and-debug-flink-programs-in-your-ide)
3. [练习、测试及解决方案](https://github.com/apache/flink-training/blob/master/README_zh.md#exercises-tests-and-solutions)

[**练习**](https://github.com/apache/flink-training/blob/master/README_zh.md#lab-exercises)

[**提交贡献**](https://github.com/apache/flink-training/blob/master/README_zh.md#contributing)

[**许可证**](https://github.com/apache/flink-training/blob/master/README_zh.md#license)

## 设置开发环境

[Permalink: 设置开发环境](https://github.com/apache/flink-training/blob/master/README_zh.md#%E8%AE%BE%E7%BD%AE%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83)

你需要设置便于进行开发、调试并运行实践练习的示例和解决方案的环境。

### 软件要求

[Permalink: 软件要求](https://github.com/apache/flink-training/blob/master/README_zh.md#%E8%BD%AF%E4%BB%B6%E8%A6%81%E6%B1%82)

Linux、OS X 和 Windows 均可作为 Flink 程序和本地执行的开发环境。 Flink 开发设置需要以下软件，它们应该安装在系统上：

- Git
- Java 8 或者 Java 11 版本的 JDK (JRE不满足要求；目前不支持其他版本的Java)
- 支持 Gradle 的 Java (及/或 Scala) 开发IDE
  - 推荐使用 [IntelliJ](https://www.jetbrains.com/idea/), 但 [Eclipse](https://www.eclipse.org/downloads/) 或 [Visual Studio Code](https://code.visualstudio.com/) (安装 [Java extension pack](https://code.visualstudio.com/docs/java/java-tutorial) 插件) 也可以用于Java环境
  - 为了使用 Scala, 需要使用 IntelliJ (及其 [Scala plugin](https://plugins.jetbrains.com/plugin/1347-scala/) 插件)

> **ℹ️ Windows 用户须知：** 实践说明中提供的 shell 命令示例适用于 UNIX 环境。
> 您可能会发现值得在 Windows 环境中设置 cygwin 或 WSL。对于开发 Flink 作业(jobs)，Windows工作的相当好：可以在单机上运行 Flink 集群、提交作业、运行 webUI 并在IDE中执行作业。

### 克隆并构建 flink-training 项目

[Permalink: 克隆并构建 flink-training 项目](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%85%8B%E9%9A%86%E5%B9%B6%E6%9E%84%E5%BB%BA-flink-training-%E9%A1%B9%E7%9B%AE)

`flink-training` 仓库包含编程练习的习题、测试和参考解决方案。

> **ℹ️ 仓库格局:** 本仓库有几个分支，分别指向不同的 Apache Flink 版本，类似于 [apache/flink](https://github.com/apache/flink) 仓库：
>
> - 每个 Apache Flink 次要版本的发布分支，例如 `release-1.10`，和
> - 一个指向当前 Flink 版本的 `master` 分支（不是 `flink:master`！）
>
> 如果想在当前 Flink 版本以外的版本上工作，请务必签出相应的分支。

从 GitHub 克隆出 `flink-training` 仓库，导航到本地项目仓库并构建它：

```
git clone https://github.com/apache/flink-training.git
cd flink-training
./gradlew test shadowJar
```

如果是第一次构建，将会下载此 Flink 练习项目的所有依赖项。这通常需要几分钟时间，但具体取决于互联网连接速度。

如果所有测试都通过并且构建成功，这说明你的实践练习已经开了一个好头。

**🇨🇳 中国用户: 点击这里了解如何使用本地 Maven 镜像。**

如果你在中国，我们建议将 Maven 存储库配置为使用镜像。 可以通过在 [`build.gradle`](https://github.com/apache/flink-training/blob/master/build.gradle) 文件中取消注释此部分来做到这一点：

```
    repositories {
        // for access from China, you may need to uncomment this line
        maven { url 'https://maven.aliyun.com/repository/public/' }
        mavenCentral()
        maven {
            url "https://repository.apache.org/content/repositories/snapshots/"
            mavenContent {
                snapshotsOnly()
            }
        }
    }
```

**启用 Scala (可选)**
这个项目中的练习也可以使用 Scala ，但由于非 Scala 用户报告的一些问题，我们决定默认禁用 Scala。
可以通过以下的方法修改 \`gradle.properties\` 文件以重新启用所有 Scala 练习和解决方案：

[`gradle.properties`](https://github.com/apache/flink-training/blob/master/gradle.properties) 文件如下：

```
#...

# Scala exercises can be enabled by setting this to true
org.gradle.project.enable_scala = true
```

如果需要，还可以选择性地在单个子项目中应用该插件。

### 将 flink-training 项目导入IDE

[Permalink: 将 flink-training 项目导入IDE](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%B0%86-flink-training-%E9%A1%B9%E7%9B%AE%E5%AF%BC%E5%85%A5ide)

本项目应作为 gradle 项目导入到IDE中。

然后应该可以打开 [`RideCleansingTest`](https://github.com/apache/flink-training/blob/master/ride-cleansing/src/test/java/org/apache/flink/training/exercises/ridecleansing/RideCleansingTest.java) 并运行此测试。

> **ℹ️ Scala 用户须知:** 需要将 IntelliJ 与 JetBrains Scala 插件一起使用，并且需要将 Scala 2.12 SDK 添加到项目结构的全局库部分以及工作模块中。
> 当打开 Scala 文件时，IntelliJ 会要求提供后者(JetBrains Scala 插件)。
> 请注意 Scala 2.12.8 及以上版本不受支持 (详细信息参见 [Flink Scala Versions](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/project-configuration/#scala-versions))!

## 使用出租车数据流(taxi data stream)

[Permalink: 使用出租车数据流(taxi data stream)](https://github.com/apache/flink-training/blob/master/README_zh.md#%E4%BD%BF%E7%94%A8%E5%87%BA%E7%A7%9F%E8%BD%A6%E6%95%B0%E6%8D%AE%E6%B5%81taxi-data-stream)

练习中使用数据 [生成器(generators)](https://github.com/apache/flink-training/blob/master/common/src/main/java/org/apache/flink/training/exercises/common/sources) 产生模拟的事件流。
该数据的灵感来自 [纽约市出租车与豪华礼车管理局(New York City Taxi & Limousine Commission)](http://www.nyc.gov/html/tlc/html/home/home.shtml)
的公开 [数据集](https://uofi.app.box.com/NYCtaxidata) 中有关纽约市出租车的车程情况。

### 出租车车程(taxi ride)事件结构

[Permalink: 出租车车程(taxi ride)事件结构](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%87%BA%E7%A7%9F%E8%BD%A6%E8%BD%A6%E7%A8%8Btaxi-ride%E4%BA%8B%E4%BB%B6%E7%BB%93%E6%9E%84)

出租车数据集包含有关纽约市个人出租车的车程信息。

每次车程都由两个事件表示：行程开始(trip start)和行程结束(trip end)。

每个事件都由十个字段组成：

```
rideId         : Long      // 每次车程的唯一id
taxiId         : Long      // 每一辆出租车的唯一id
driverId       : Long      // 每一位司机的唯一id
isStart        : Boolean   // 行程开始事件为 TRUE， 行程结束事件为 FALSE
eventTime      : Instant   // 事件的时间戳
startLon       : Float     // 车程开始位置的经度
startLat       : Float     // 车程开始位置的维度
endLon         : Float     // 车程结束位置的经度
endLat         : Float     // 车程结束位置的维度
passengerCnt   : Short     // 乘车人数
```

### 出租车车费(taxi fare)事件结构

[Permalink: 出租车车费(taxi fare)事件结构](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%87%BA%E7%A7%9F%E8%BD%A6%E8%BD%A6%E8%B4%B9taxi-fare%E4%BA%8B%E4%BB%B6%E7%BB%93%E6%9E%84)

还有一个包含与车程相关费用的数据集，它具有以下字段：

```
rideId         : Long      // 每次车程的唯一id
taxiId         : Long      // 每一辆出租车的唯一id
driverId       : Long      // 每一位司机的唯一id
startTime      : Instant   // 车程开始时间
paymentType    : String    // 现金(CASH)或刷卡(CARD)
tip            : Float     // 小费
tolls          : Float     // 过路费
totalFare      : Float     // 总计车费
```

## 如何做练习

[Permalink: 如何做练习](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%A6%82%E4%BD%95%E5%81%9A%E7%BB%83%E4%B9%A0)

在实践课程中，你将使用各种 Flink API 实现 Flink 程序。

以下步骤将指导你完成使用提供的数据流、实现第一个 Flink 流程序以及在 IDE 中执行程序的过程。

我们假设你已根据 [设置指南](https://github.com/apache/flink-training/blob/master/README_zh.md#set-up-your-development-environment) 准备好了开发环境。

### 了解数据

[Permalink: 了解数据](https://github.com/apache/flink-training/blob/master/README_zh.md#%E4%BA%86%E8%A7%A3%E6%95%B0%E6%8D%AE)

最初的一组练习都是基于有关出租车车程和出租车车费的事件数据流。这些流由从输入文件读取数据的源函数产生。
参见 [说明](https://github.com/apache/flink-training/blob/master/README_zh.md#using-the-taxi-data-streams) 以了解如何使用它们。

### 在 IDE 中运行和调试 Flink 程序

[Permalink: 在 IDE 中运行和调试 Flink 程序](https://github.com/apache/flink-training/blob/master/README_zh.md#%E5%9C%A8-ide-%E4%B8%AD%E8%BF%90%E8%A1%8C%E5%92%8C%E8%B0%83%E8%AF%95-flink-%E7%A8%8B%E5%BA%8F)

Flink 程序可以在 IDE 中执行和调试。这显著地简化了开发过程，并可提供类似于使用任何其他 Java（或 Scala）应用程序的体验。

要在 IDE 中启动 Flink 程序，请运行它的 `main()` 方法。在后台，执行环境将在同一进程中启动本地 Flink 实例。因此，可以在代码中放置断点并对其进行调试。

如果 IDE 已导入 `flink-training` 项目，则可以通过以下方式运行（或调试）流式作业：

- 在 IDE 中打开 `org.apache.flink.training.examples.ridecount.RideCountExample` 类
- 使用 IDE 运行（或调试）`RideCountExample` 类的`main()` 方法

### 练习、测试及解决方案

[Permalink: 练习、测试及解决方案](https://github.com/apache/flink-training/blob/master/README_zh.md#%E7%BB%83%E4%B9%A0%E6%B5%8B%E8%AF%95%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)

每一项练习都包括：

- 一个 `...Exercise` 类，其中包含运行所需地大多数样板代码
- 一个 JUnit 测试类（`...Test`），其中包含一些针对实现的测试
- 具有完整解决方案的 `...Solution` 类

所有练习、测试和解决方案类都有 Java 和 Scala 版本。 它们都可以在 IntelliJ 中运行。

> **ℹ️ 注意:** 只要 `...Exercise` 类抛出 `MissingSolutionException` 异常，那么所提供的 JUnit 测试类将忽略该失败并转而验证已提供的参考解决方案实现的正确性。

你可以使用 `gradlew` 命令运行练习、解决方案和测试。

运行测试：

```
./gradlew test
./gradlew :<subproject>:test
```

对于 Java/Scala 练习和解决方案，我们提供了可以获取清单的特殊任务：

```
./gradlew printRunTasks
```

👇 至此，你已准备好开始进行练习。 👇

## 练习

[Permalink: 练习](https://github.com/apache/flink-training/blob/master/README_zh.md#%E7%BB%83%E4%B9%A0)

1. [过滤流(车程清理)](https://github.com/apache/flink-training/blob/master/ride-cleansing/README_zh.md)
2. [有状态的增强(车程及车费)](https://github.com/apache/flink-training/blob/master/rides-and-fares/README_zh.md)
3. [窗口分析(每小时小费)](https://github.com/apache/flink-training/blob/master/hourly-tips/README_zh.md)
   - [练习](https://github.com/apache/flink-training/blob/master/hourly-tips/README_zh.md)
   - [讨论](https://github.com/apache/flink-training/blob/master/hourly-tips/DISCUSSION_zh.md)
4. [`ProcessFunction` 及定时器(长车程警报)](https://github.com/apache/flink-training/blob/master/long-ride-alerts/README_zh.md)
   - [练习](https://github.com/apache/flink-training/blob/master/long-ride-alerts/README_zh.md)
   - [讨论](https://github.com/apache/flink-training/blob/master/long-ride-alerts/DISCUSSION.md)

## 提交贡献

[Permalink: 提交贡献](https://github.com/apache/flink-training/blob/master/README_zh.md#%E6%8F%90%E4%BA%A4%E8%B4%A1%E7%8C%AE)

如果你想为此仓库做出贡献或添加新练习，请阅读 [提交贡献](https://github.com/apache/flink-training/blob/master/CONTRIBUTING.md) 指南。

## 许可证

[Permalink: 许可证](https://github.com/apache/flink-training/blob/master/README_zh.md#%E8%AE%B8%E5%8F%AF%E8%AF%81)

本仓库中的代码基于 [Apache Software License 2](https://github.com/apache/flink-training/blob/master/LICENSE) 许可证。

You can’t perform that action at this time.