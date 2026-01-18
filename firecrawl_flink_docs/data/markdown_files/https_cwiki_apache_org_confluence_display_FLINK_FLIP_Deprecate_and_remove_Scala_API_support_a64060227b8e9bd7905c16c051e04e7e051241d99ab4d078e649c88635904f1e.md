DUE TO SPAM, SIGN-UP IS DISABLED. Goto [Selfserve wiki signup](https://selfserve.apache.org/confluence-account.html) and request an account.

[![Apache Flink](https://cwiki.apache.org/confluence/download/attachments/44302795/FLINK?version=1&modificationDate=1468231075000&api=v2)](https://cwiki.apache.org/confluence/display/FLINK/Apache+Flink+Home "Apache Flink")

[Apache Flink](https://cwiki.apache.org/confluence/display/FLINK/Apache+Flink+Home "Apache Flink")

## Page tree

Browse pages

ConfigureSpace tools

- [More options](https://cwiki.apache.org/confluence/display/FLINK/FLIP-265+Deprecate+and+remove+Scala+API+support#)




  - [Attachments (0)](https://cwiki.apache.org/confluence/pages/viewpageattachments.action?pageId=231115782 "View Attachments")
  - [Page History](https://cwiki.apache.org/confluence/pages/viewpreviousversions.action?pageId=231115782 "")

  - [Resolved comments](https://cwiki.apache.org/confluence "")
  - [Page Information](https://cwiki.apache.org/confluence/pages/viewinfo.action?pageId=231115782 "")
  - [View in Hierarchy](https://cwiki.apache.org/confluence/pages/reorderpages.action?key=FLINK&openId=231115782#selectedPageInHierarchy "")
  - [View Source](https://cwiki.apache.org/confluence/plugins/viewsource/viewpagesrc.action?pageId=231115782 "")
  - [Export to PDF](https://cwiki.apache.org/confluence/spaces/flyingpdf/pdfpageexport.action?pageId=231115782 "")
  - [Export to Word](https://cwiki.apache.org/confluence/exportword?pageId=231115782 "")

  - [Copy Page Tree](https://cwiki.apache.org/confluence/plugins/tree-copy/preparing-copying.action?pageId=231115782 "")

- [Unrestricted](https://cwiki.apache.org/confluence/display/FLINK/FLIP-265+Deprecate+and+remove+Scala+API+support "Unrestricted")
- [Jira links](https://cwiki.apache.org/confluence/display/FLINK/FLIP-265+Deprecate+and+remove+Scala+API+support "")

# [FLIP-265 Deprecate and remove Scala API support](https://cwiki.apache.org/confluence/display/FLINK/FLIP-265+Deprecate+and+remove+Scala+API+support)

-







Created by [Martijn Visser](https://cwiki.apache.org/confluence/display/~martijnvisser), last modified on [Oct 24, 2022](https://cwiki.apache.org/confluence/pages/diffpagesbyversion.action?pageId=231115782&selectedPageVersions=3&selectedPageVersions=4 "Show changes")

| Discussion thread | [https://lists.apache.org/thread/d3borhdzj496nnggohq42fyb6zkwob3h](https://lists.apache.org/thread/d3borhdzj496nnggohq42fyb6zkwob3h) |
| Vote thread | [https://lists.apache.org/thread/qfz4opcbc2p59fhmymncxyzxb70cn098](https://lists.apache.org/thread/qfz4opcbc2p59fhmymncxyzxb70cn098) |
| JIRA | [FLINK-29739](https://issues.apache.org/jira/browse/FLINK-29739)<br> -<br>Getting issue details...STATUS |
| Release | 1.17 / 2.0 |

Please keep the discussion on the mailing list rather than commenting on the wiki (wiki discussions get unwieldy fast).

# Motivation

Apache Flink offers APIs for building your Flink application using the DataStream and Table API. These are offered in Java and Scala. The Python APIs use the Java APIs under the hood. Over the course of time, the primary focus of the Flink community has shifted towards the Java API and the Scala support in Flink is not up-to-par with the Java API. A couple of examples:

1. Flink still only supports Scala 2.12.7 and can only upgrade to a later version of Scala 2.12 by breaking compatibility [FLINK-20969](https://issues.apache.org/jira/browse/FLINK-20969)
    -
    Getting issue details...STATUS
2. Flink doesn't support Scala 2.13 even though the initial ticket was created in July 2019 [FLINK-13414](https://issues.apache.org/jira/browse/FLINK-13414)
    -
    Getting issue details...STATUS.
3. The DataStream API in Java has more features available compared to the DataStream API in Scala. For example [FLINK-29498](https://issues.apache.org/jira/browse/FLINK-29498)
    -
    Getting issue details...STATUS

Prior to Flink 1.15, there was tight dependency on Scala (Scala was always on the classpath). As of Flink 1.15, there is an option to use the Java API from any Scala version. The changes in Flink 1.15 are explained in-depth in a blogpost from the project website, which you can find at [https://flink.apache.org/2022/02/22/scala-free.html](https://flink.apache.org/2022/02/22/scala-free.html)

The current state of Scala in Flink can be summarised as:

- Most of the Scala-related contributions were/are focussed on unblocking users to use the Java API with any Scala version
- The Flink community is lacking maintainers with Scala knowledge who can help forward the Scala support directly in Flink
- New API interfaces that are added to Flink are created first for Java and are not or have limited support in Scala
- The open source community (outside of the ASF Flink project) are creating initiatives to help with Scala support in Flink, such as [https://github.com/ariskk/flink4s](https://github.com/ariskk/flink4s) (wraps Java APIs for Scala 3 users) and [https://github.com/findify/flink-adt](https://github.com/findify/flink-adt) (which replaces the \`TypeInformation\` derivation mechanism in flink-scala)

Given the current state of Scala, this FLIP proposes to deprecate all Scala APIs in Flink 1.17 and remove all Scala APIs from Flink 2.0.

One of the primary parts of Flink that's using Scala is the table-planner. This is out of scope for deprecation since these are `@Internal`  interfaces. Removing Scala from the table-planner is still considered future work as first outlined in FLIP-32.

# Public Interfaces

None

# Proposed Changes

- Deprecate all customer-facing Scala APIs in the next Flink 1.x version, meaning:
  - We annotate all `@Public, @PublicEvolving and @Experimental Scala APIs as @Deprecated.`
  - We remove all Scala API code examples from the codebase
  - We remove all Scala API documentation
- Remove these APIs in the next Flink major (2.x) version.

# Compatibility, Deprecation, and Migration Plan

- Users who rely on the Scala APIs can and should consider porting to their equivalent from the Java APIs
- Otherwise, Flink 1.x will be the last version that the Flink Scala users can use.

# Test Plan

N/A

# Rejected Alternatives

None

- [accepted](https://cwiki.apache.org/confluence/label/FLINK/accepted)

Overview

Content Tools

{"serverDuration": 95, "requestCorrelationId": "3526ed453baf2707"}