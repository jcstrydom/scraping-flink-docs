DUE TO SPAM, SIGN-UP IS DISABLED. Goto [Selfserve wiki signup](https://selfserve.apache.org/confluence-account.html) and request an account.

[![Apache Hive](https://cwiki.apache.org/confluence/download/attachments/27362113/Hive?version=2&modificationDate=1317659390000&api=v2)](https://cwiki.apache.org/confluence/display/Hive/Home?src=sidebar "Apache Hive")

[Apache Hive](https://cwiki.apache.org/confluence/display/Hive/Home?src=sidebar "Apache Hive")

- [Pages](https://cwiki.apache.org/confluence/collector/pages.action?key=Hive&src=sidebar-pages)
- [Blog](https://cwiki.apache.org/confluence/pages/viewrecentblogposts.action?key=Hive&src=sidebar-blogs)

## Space shortcuts

- [How-to articles](https://cwiki.apache.org/confluence/display/Hive/How-to+articles?src=spaceshortcut)

##### Child pages

- [Home](https://cwiki.apache.org/confluence/display/Hive/Home?src=contextnavchildmode "Home")

- HiveServer2 Overview

- [Hive Metrics](https://cwiki.apache.org/confluence/display/Hive/Hive+Metrics?src=contextnavchildmode "Hive Metrics")

[ (Type 'g' then 's')](https://cwiki.apache.org/confluence/collector/pages.action?key=Hive&src=sidebar " (Type 'g' then 's')")

Browse pages

ConfigureSpace tools

- [Overview](https://cwiki.apache.org/confluence/spaces/viewspacesummary.action?key=Hive&src=spacetools)
- [Content Tools](https://cwiki.apache.org/confluence/pages/reorderpages.action?key=Hive&src=spacetools)

- [Browse pages](https://cwiki.apache.org/confluence/pages/reorderpages.action?key=Hive&src=spacetools)

[Collapse sidebar ( [ )](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
**This wiki is now read only. This and new content has been migrated to a**[new location![](https://cwiki.apache.org/confluence/images/icons/linkext7.gif)](https://hive.apache.org/docs/latest/)\
\
- [More options](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
\
\
\
  - [Attachments (0)](https://cwiki.apache.org/confluence/pages/viewpageattachments.action?pageId=65147648 "View Attachments (Type 't')")\
  - [Page History](https://cwiki.apache.org/confluence/pages/viewpreviousversions.action?pageId=65147648 "")\
\
  - [Resolved comments (0)](https://cwiki.apache.org/confluence "")\
  - [Page Information](https://cwiki.apache.org/confluence/pages/viewinfo.action?pageId=65147648 "")\
  - [View in Hierarchy](https://cwiki.apache.org/confluence/pages/reorderpages.action?key=Hive&openId=65147648#selectedPageInHierarchy "")\
  - [View Source](https://cwiki.apache.org/confluence/plugins/viewsource/viewpagesrc.action?pageId=65147648 "")\
  - [Export to PDF](https://cwiki.apache.org/confluence/spaces/flyingpdf/pdfpageexport.action?pageId=65147648 "")\
  - [Export to Word](https://cwiki.apache.org/confluence/exportword?pageId=65147648 "")\
\
  - [Copy Page Tree](https://cwiki.apache.org/confluence/plugins/tree-copy/preparing-copying.action?pageId=65147648 "")\
\
- [Unrestricted](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview "Unrestricted")\
- [Jira links](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview "")\
\
# [HiveServer2 Overview](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview)\
\
-\
\
\
\
\
\
\
\
Created by [Tom Li](https://cwiki.apache.org/confluence/display/~tli), last modified by [Lefty Leverenz](https://cwiki.apache.org/confluence/display/~leftyl) on [Oct 16, 2016](https://cwiki.apache.org/confluence/pages/diffpagesbyversion.action?pageId=65147648&selectedPageVersions=32&selectedPageVersions=33 "Show changes")\
\
- 1 [Introduction](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Introduction)\
- 2 [HS2 Architecture](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-HS2Architecture)\
  - 2.1 [Server](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Server)\
  - 2.2 [Transport](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Transport)\
  - 2.3 [Protocol](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Protocol)\
  - 2.4 [Processor](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Processor)\
- 3 [Dependencies of HS2](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-DependenciesofHS2)\
- 4 [JDBC Client](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-JDBCClient)\
- 5 [Source Code Description](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-SourceCodeDescription)\
  - 5.1 [Server Side](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-ServerSide)\
  - 5.2 [Client Side](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-ClientSide)\
  - 5.3 [Interaction between Client and Server](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-InteractionbetweenClientandServer)\
- 6 [Resources](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#HiveServer2Overview-Resources)\
\
# Introduction\
\
HiveServer2 (HS2) is a service that enables clients to execute queries against Hive. HiveServer2 is the successor to [HiveServer1](https://cwiki.apache.org/confluence/display/Hive/HiveServer) which has been deprecated. HS2 supports multi-client concurrency and authentication. It is designed to provide better support for open API clients like JDBC and ODBC.\
\
HS2 is a single process running as a composite service, which includes the Thrift-based Hive service (TCP or HTTP) and a [Jetty](http://www.eclipse.org/jetty/) web server for web UI.\
\
# HS2 Architecture\
\
The Thrift-based Hive service is the core of HS2 and responsible for servicing the Hive queries (e.g., from Beeline). [Thrift](https://thrift.apache.org/) is an RPC framework for building cross-platform services. Its stack consists of 4 layers: Server, Transport, Protocol, and Processor. You can find more details about the layers at [https://thrift.apache.org/docs/concepts](https://thrift.apache.org/docs/concepts).\
\
The usage of those layers in the HS2 implementation is described below.\
\
## Server\
\
HS2 uses a TThreadPoolServer (from Thrift) for TCP mode, or a Jetty server for the HTTP mode.\
\
The TThreadPoolServer allocates one worker thread per TCP connection. Each thread is always associated with a connection even if the connection is idle. So there is a potential performance issue resulting from a large number of threads due to a large number of concurrent connections. In the future HS2 might switch to another server type for TCP mode, for example TThreadedSelectorServer. Here is an [article](https://github.com/m1ch1/mapkeeper/wiki/Thrift-Java-Servers-Compared) about a performance comparison between different Thrift Java servers.\
\
## Transport\
\
HTTP mode is required when a proxy is needed between the client and server (for example, for load balancing or security reasons). That is why it is supported, as well as TCP mode. You can specify the transport mode of the Thrift service through the Hive configuration property [hive.server2.transport.mode](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties#ConfigurationProperties-hive.server2.transport.mode).\
\
## Protocol\
\
The Protocol implementation is responsible for serialization and deserialization. HS2 is currently using TBinaryProtocol as its Thrift protocol for serialization. In the future other protocols may be considered, such as TCompactProtocol, based on more performance evaluation.\
\
## Processor\
\
Process implementation is the application logic to handle requests. For example, the ThriftCLIService.ExecuteStatement() method implements the logic to compile and execute a Hive query.\
\
# Dependencies of HS2\
\
- [Metastore](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Metastore+Administration)\
\
The metastore can be configured as embedded (in the same process as HS2) or as a remote server (which is a Thrift-based service as well). HS2 talks to the metastore for the metadata required for query compilation.\
\
- Hadoop cluster\
\
HS2 prepares physical execution plans for various execution engines (MapReduce/Tez/Spark) and submits jobs to the Hadoop cluster for execution.\
\
You can find a diagram of the interactions between HS2 and its dependencies [here](https://cwiki.apache.org/confluence/display/Hive/Design#Design-HiveArchitecture).\
\
# JDBC Client\
\
The JDBC driver is recommended for the client side to interact with HS2. Note that there are some use cases (e.g., [Hadoop Hue](http://gethue.com/)) where the Thrift client is used directly and JDBC is bypassed.\
\
Here is a sequence of API calls involved to make the first query:\
\
- The JDBC client (e.g., Beeline) creates a HiveConnection by initiating a transport connection (e.g., TCP connection) followed by an OpenSession API call to get a SessionHandle. The session is created from the server side.\
- The HiveStatement is executed (following JDBC standards) and an ExecuteStatement API call is made from the Thrift client. In the API call, SessionHandle information is passed to the server along with the query information.\
- The HS2 server receives the request and asks the driver (which is a CommandProcessor) for query parsing and compilation. The driver kicks off a background job that will talk to Hadoop and then immediately returns a response to the client. This is an asynchronous design of the ExecuteStatement API. The response contains an OperationHandle created from the server side.\
- The client uses the OperationHandle to talk to HS2 to poll the status of the query execution.\
\
# Source Code Description\
\
The following sections help you locate some basic components of HiveServer2 in the source code.\
\
## Server Side\
\
- **Thrift IDL file for TCLIService**: [https://github.com/apache/hive/blob/master/service-rpc/if/TCLIService.thrift](https://github.com/apache/hive/blob/master/service-rpc/if/TCLIService.thrift).\
- **TCL** **IService** **.Iface implemented by**: _org.apache.hive.service.cli.thrift.ThriftCLIService_ class.\
- **ThriftCLIService subclassed by**: _org.apache.hive.service.cli.thrift.ThriftBinaryCLIService_ and _org.apache.hive.service.cli.thrift.ThriftHttpCLIService_ for TCP mode and HTTP mode respectively _._\
- **org.apache.hive.service.cli.thrift.EmbeddedThriftBinaryCLIService class:** Embedded mode for HS2. Don't get confused with embedded metastore, which is a different service (although the embedded mode concept is similar).\
- **org.apache.hive.service.cli.session.HiveSessionImpl class**: Instances of this class are created on the server side and managed by an _org.apache.accumulo.tserver.TabletServer.SessionManager_ instance _._\
\
- **org.apache.hive.service.cli.operation.Operation class**: Defines an operation (e.g., a query). Instances of this class are created on the server and managed by an _org.apache.hive.service.cli.operation.OperationManager_ instance _._\
- **org.apache.hive.service.auth.HiveAuthFactory class**: A helper used by both HTTP and TCP mode for authentication. Refer to [Setting Up HiveServer2](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2) for various authentication options, in particular [Authentication/Security Configuration](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2#SettingUpHiveServer2-Authentication/SecurityConfiguration) and [Cookie Based Authentication](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2#SettingUpHiveServer2-CookieBasedAuthentication).\
\
## Client Side\
\
- **org.apache.hive.jdbc.HiveConnection class _:_** Implements the _java.sql.Connection_ interface (part of JDBC _)_ _._ An instance of this class holds a reference to a _SessionHandle_ instance which is retrieved when making Thrift API calls to the server _._\
- **org.apache.hive.jdbc.HiveStatement class:** Implements the _java.sql.Statement_ interface (part of JDBC). The client (e.g., Beeline) calls the _HiveStatement.execute()_ method for the query. Inside the _execute_() method, the Thrift client is used to make API calls.\
- **org.apache.hive.jdbc.HiveDriver class**: Implements the _java.sql.Driver_ interface (part of JDBC) _._ The core method is _connect_() which is used by the JDBC client to initiate a SQL connection.\
\
## Interaction between Client and Server\
\
- **org.apache.hive.service.cli.SessionHandle class:** Session identifier.Instances of this class are returned from the server and used by the client as input for Thrift API calls _._\
- **org.apache.hive.service.cli.OperationHandle class**: Operation identifier. Instances of this class are returned from the server and used by the client to poll the execution status of an operation.\
\
# Resources\
\
How to set up HS2: [Setting Up HiveServer2](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2)\
\
HS2 clients: [HiveServer2 Clients](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients)\
\
User interface:  [Web UI for HiveServer2](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2#SettingUpHiveServer2-WebUIforHiveServer2)\
\
Metrics:  [Hive Metrics](https://cwiki.apache.org/confluence/display/Hive/Hive+Metrics)\
\
Cloudera blog on HS2: [http://blog.cloudera.com/blog/2013/07/how-hiveserver2-brings-security-and-concurrency-to-apache-hive/](http://blog.cloudera.com/blog/2013/07/how-hiveserver2-brings-security-and-concurrency-to-apache-hive/)\
\
[5 people](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview) like this\
\
- No labels\
\
\
Overview\
\
Content Tools\
\
**This wiki is now read only. This and new content has been migrated to a**[new location![](https://cwiki.apache.org/confluence/images/icons/linkext7.gif)](https://hive.apache.org/docs/latest/)\
\
{"serverDuration": 99, "requestCorrelationId": "21c9571179612fcf"}\
\
You are not logged in. Any changes you make will be marked as anonymous. You may want to [Log In](https://cwiki.apache.org/confluence/login.action?os_destination=%2Fdisplay%2Fhive%2Fhiveserver2%2Boverview) if you already have an account.\
\
search\
\
attachments\
\
weblink\
\
advanced\
\
image-effects\
\
image-attributes\
\
- [Paragraph](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
  - [Paragraph](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 1](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 2](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 3](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 4](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 5](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Heading 6](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Preformatted](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Quote](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Bold](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Italic](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Underline](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Color picker](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
[More colors](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
\
\
\
\
  - [Black](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Burnt orange](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Dark olive](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Dark green](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Dark azure](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Navy blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Indigo](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Very dark grey](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Maroon](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Orange](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Olive](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Green](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Teal](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Greyish blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Grey](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Red](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Amber](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Yellow green](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Sea green](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Turquoise](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Royal blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Purple](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Medium grey](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Magenta](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Gold](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Yellow](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Lime](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Aqua](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Sky blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Red violet](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Light grey](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Pink](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Peach](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Light yellow](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Pale green](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Pale cyan](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Light sky blue](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Plum](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [White](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Formatting](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
\
\
\
\
  - [Strikethrough](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Subscript](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Superscript](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Monospace](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
  - [Clear formatting](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Bullet list](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Numbered list](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Task list](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Outdent](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Indent](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Align left](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Align center](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Align right](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Page layout](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Link](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Table](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
\
- [Insert](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
\
\
Insert content\
\
  - [Files and images](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Link](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Markup](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Horizontal rule](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Task list](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Date](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Symbol](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
Insert macro\
\
  - [Handy Timestamp](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Handy Status](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Handy Tip](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [User mention](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Table Plus](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [draw.io Diagram](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Embed draw.io Diagram](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [draw.io Board Diagram](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Gliffy Diagram](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Jira Issue/Filter](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Info](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Status](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Gallery](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Table of Contents](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
  - [Other macros](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Page layout](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
  - [No layout](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column (simple)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column (simple, left sidebar)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column (simple, right sidebar)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Three column (simple)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column (left sidebar)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Two column (right sidebar)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Three column](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
  - [Three column (left and right sidebars)](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Undo](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [Redo](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Find/Replace](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Keyboard shortcuts help](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
You are not logged in. Any changes you make will be marked as anonymous. You may want to [Log In](https://cwiki.apache.org/confluence/login.action?os_destination=%2Fdisplay%2Fhive%2Fhiveserver2%2Boverview) if you already have an account.\
\
This page is also being edited by . Your changes will be merged with theirs when you save.\
\
If you are unable to use this CAPTCHA please <a href="administrators.action" tabindex="5">contact your administrator</a> for assistance.![CAPTCHA image](https://cwiki.apache.org/confluence/jcaptcha?id=1285281608)\
\
Connecting...\
\
Edit\
\
Save\
\
Close\
\
- [Preview](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
- [View changes](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)\
\
- [Revert to last published version](https://cwiki.apache.org/confluence/display/hive/hiveserver2+overview#)