[Skip to content](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive) to refresh your session.Dismiss alert

{{ message }}

[dbeaver](https://github.com/dbeaver)/ **[dbeaver](https://github.com/dbeaver/dbeaver)** Public

- [Notifications](https://github.com/login?return_to=%2Fdbeaver%2Fdbeaver) You must be signed in to change notification settings
- [Fork\\
4k](https://github.com/login?return_to=%2Fdbeaver%2Fdbeaver)
- [Star\\
48.3k](https://github.com/login?return_to=%2Fdbeaver%2Fdbeaver)


# Apache Hive

[Jump to bottom](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#wiki-pages-box)

dbeaver-devops edited this page on Oct 27, 2025Oct 27, 2025
·
[14 revisions](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive/_history)

#### Table of contents

[Permalink: Table of contents](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#table-of-contents)

- [Apache Hive specialty](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-specialty)
- [Setting up](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#setting-up)
- [Apache Hive connection settings](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-connection-settings)  - [Connection details](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#connection-details)
- [Apache Hive driver properties](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-driver-properties)
- [Secure Connection Configurations](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#secure-connection-configurations)
- [Secure Storage with Secret Providers](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#secure-storage-with-secret-providers)
- [Powering Apache Hive with DBeaver](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#powering-apache-hive-with-dbeaver)  - [Apache Hive database objects](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-database-objects)
- [Apache Hive features](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-features)

This guide provides instructions on how to set up and use Apache Hive with DBeaver.

Before you start, you must create a connection in DBeaver and select Hive. If you have not done this, please
refer to our [Database Connection](https://github.com/dbeaver/dbeaver/wiki/Create-Connection) article.

DBeaver interacts with the Hive server using a specific driver. It supports all versions of Hive, but the
correct driver must be selected: use `Hive 2` for versions 2.x and earlier, and `Hive 4` for version 4 and later.
DBeaver also supports Hive extensions such as Kyuubi and Spark, depending on your environment
configuration. You must select the appropriate driver in the **Connect to a database** window for these extensions.

![](https://github.com/dbeaver/dbeaver/wiki/images/database/hive/hive-drivers.png)

> **Tip**: Systems like Impala use Hive-compatible drivers, so the standard Hive JDBC driver works in this case.

## Apache Hive specialty

[Permalink: Apache Hive specialty](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-specialty)

Apache Hive is a data warehouse system built on top of Hadoop for querying and analyzing large datasets using a SQL-like
language called HiveQL. It's optimized for batch processing and is commonly used for data summarization, ad-hoc queries,
and analysis of structured data. Hive translates SQL queries into MapReduce jobs, making it well-suited for handling
large-scale data stored in Hadoop Distributed File System (HDFS). Hive is a good fit for OLAP-style workloads and
integrates with other big data tools in the Hadoop ecosystem.

> For more detailed information and a comprehensive understanding of Apache Hive, see
> the [official documentation](https://cwiki.apache.org/confluence/display/Hive/Home).

## Setting up

[Permalink: Setting up](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#setting-up)

This section provides an overview of DBeaver's settings for establishing a direct connection and the
configuration of secure connections using SSH and proxies for Hive.

## Apache Hive connection settings

[Permalink: Apache Hive connection settings](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-connection-settings)

The page of the connection settings requires you to fill in specific fields to establish the initial connection.

![](https://github.com/dbeaver/dbeaver/wiki/images/database/hive/hive-connection-main.png)

| Field | Description |
| --- | --- |
| **Connect by (Host/URL)** | Choose whether you want to connect using a host or a URL. |
| **URL** | If you are connecting via URL, enter the URL of your Hive database here. This field is hidden if you are connecting via the host. |
| **Host** | If you are connecting via host, enter the host address of your Hive database here. |
| **Database/Schema** | Enter the name of the Hive database you want to connect to. |
| **Port** | Enter the port number for your Hive database. The default Hive port is `10000`. |
| **Authentication** | Choose the type of authentication you want to use for the connection. For detailed guides on authentication types, please refer to the following articles:<br> \- [Native Database Authentication](https://github.com/dbeaver/dbeaver/wiki/Authentication-Database-Native)<br> \- [DBeaver Profile Authentication](https://github.com/dbeaver/dbeaver/wiki/Authentication-DBeaver-profile)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)<br> You can also read about [security in DBeaver PRO](https://github.com/dbeaver/dbeaver/wiki/Security-in-DBeaver-PRO). |
| **Connection Details** | Provide [additional connection details](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#connection-details) if necessary. |
| **Driver Name** | This field will be auto-filled based on your selected driver type. |
| **Driver Settings** | If there are any [specific driver settings](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-driver-properties), configure them here. |

### Connection details

[Permalink: Connection details](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#connection-details)

The **Connection Details** section in DBeaver allows you to customize your experience while working with Hive database. This includes
options for adjusting the **Navigator View**, setting up **Security measures**, applying **Filters**, configuring **Connection**
**Initialization** settings, and setting up **Shell Commands**. Each of these settings can significantly impact your database
operations and workflow. For detailed guides on these settings, please refer to the following articles:

- [Connection Details Configuration](https://github.com/dbeaver/dbeaver/wiki/Create-Connection#connection-details)
- [Database Navigator](https://github.com/dbeaver/dbeaver/wiki/Database-Navigator)
- [Security Settings Guide](https://github.com/dbeaver/dbeaver/wiki/Managing-security-restrictions-for-database-connection)
- [Filters Settings Guide](https://github.com/dbeaver/dbeaver/wiki/Configure-Filters)
- [Connection Initialization Settings Guide](https://github.com/dbeaver/dbeaver/wiki/Configure-Connection-Initialization-Settings)
- [Shell Commands Guide](https://github.com/dbeaver/dbeaver/wiki/Working-with-Shell-Commands-in-DBeaver)

## Apache Hive driver properties

[Permalink: Apache Hive driver properties](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-driver-properties)

The settings for Hive **Driver properties** enable you to adjust the performance of the Hive driver.
These adjustments can influence the efficiency, compatibility, and features of your Hive database.

You can customize the Hive driver in DBeaver via the **Edit Driver** page, accessible by clicking on the **Driver**
**Settings** button on the first page of the driver settings. This page offers a range of settings that can influence your
Hive database connections. For a comprehensive guide on these settings, please refer to our [Driver manager](https://github.com/dbeaver/dbeaver/wiki/Driver-Manager) article.

## Secure Connection Configurations

[Permalink: Secure Connection Configurations](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#secure-connection-configurations)

DBeaver supports secure connections to your Hive database. Guidance on configuring such connections,
specifically **SSH**, **Proxy**, **Kubernetes**, and **AWS SSM** connections, can be found in various referenced
articles. For a comprehensive understanding, please refer to these articles:

- [**SSH Configuration**](https://github.com/dbeaver/dbeaver/wiki/SSH-Configuration)

- [**Proxy Configuration**](https://github.com/dbeaver/dbeaver/wiki/Proxy-configuration)

- [**Kubernetes Configuration**](https://github.com/dbeaver/dbeaver/wiki/Kubernetes-configuration)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)

- [**AWS SSM**](https://github.com/dbeaver/dbeaver/wiki/AWS-SSM-Configuration)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)


## Secure Storage with Secret Providers

[Permalink: Secure Storage with Secret Providers](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#secure-storage-with-secret-providers)

DBeaver supports various cloud-based secret providers to retrieve database credentials. For detailed setup
instructions, see [Secret Providers](https://github.com/dbeaver/dbeaver/wiki/Secret-Providers).

## Powering Apache Hive with DBeaver

[Permalink: Powering Apache Hive with DBeaver](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#powering-apache-hive-with-dbeaver)

DBeaver provides a host of features designed for Hive databases. This includes the ability to view and manage
databases, along with numerous unique capabilities aimed at optimizing database operations.

### Apache Hive database objects

[Permalink: Apache Hive database objects](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-database-objects)

DBeaver lets you view and manipulate a wide range of Hive database objects. DBeaver has extensive
support for various Hive metadata types, allowing you to interact with a wide variety of database objects, such as:

- Databases/Schemas
  - Tables
    - Columns
  - Views

> Hive doesn’t support referential integrity, so you won’t see primary keys or foreign keys.
>
> Diagrams also aren’t relevant.

## Apache Hive features

[Permalink: Apache Hive features](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#apache-hive-features)

DBeaver is not limited to typical SQL tasks. It also includes features specific to Hive.

Beyond regular SQL operations, DBeaver provides a range of Hive-oriented capabilities, such as:

| Category | Feature |
| --- | --- |
| Data Types | Hive-specific types like `ARRAY`, `STRUCT`. |
| File System | HDFS. |
| Query Language | HiveQL (SQL-like query language). |

Additional features compatible with Hive, but not exclusive to it:

| Category | Feature |
| --- | --- |
| Data Transfer | [Data Import](https://github.com/dbeaver/dbeaver/wiki/Data-import) |
|  | [Data Export](https://github.com/dbeaver/dbeaver/wiki/Data-export) |
| Data Management | [Data Compare](https://github.com/dbeaver/dbeaver/wiki/Data-compare) |

[DBeaver - Universal Database Manager](https://dbeaver.io/)

#### DBeaver Documentation

[Permalink: DBeaver Documentation](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive#dbeaver-documentation)

- [Getting started](https://github.com/dbeaver/dbeaver/wiki/Getting-started)  - [Installation guide](https://github.com/dbeaver/dbeaver/wiki/Installation)
  - [How to import license](https://github.com/dbeaver/dbeaver/wiki/How-to-Import-License)
  - [Application window overview](https://github.com/dbeaver/dbeaver/wiki/Application-Window-Overview)
  - [Basic operations](https://github.com/dbeaver/dbeaver/wiki/Basic-operations)
- DBeaver configuration
  - [User Interface](https://github.com/dbeaver/dbeaver/wiki/User-Interface-Themes)
  - [Languages](https://github.com/dbeaver/dbeaver/wiki/UI-Language)
  - [Accessibility](https://github.com/dbeaver/dbeaver/wiki/Accessibility-Guide)
  - [Toolbar customization](https://github.com/dbeaver/dbeaver/wiki/Toolbar-Customization)
  - [Shortcuts](https://github.com/dbeaver/dbeaver/wiki/Shortcuts)
- [Security](https://github.com/dbeaver/dbeaver/wiki/Security-in-DBeaver-PRO)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)  - [Security in DBeaver PRO](https://github.com/dbeaver/dbeaver/wiki/Security-in-DBeaver-PRO)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Secure storage](https://github.com/dbeaver/dbeaver/wiki/Security)
  - [Secret management](https://github.com/dbeaver/dbeaver/wiki/Secret-Providers)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
- Connection settings
  - [Create connection](https://github.com/dbeaver/dbeaver/wiki/Create-Connection)
  - [Network configuration](https://github.com/dbeaver/dbeaver/wiki/Network-configuration)
  - [Auto and manual commit modes](https://github.com/dbeaver/dbeaver/wiki/Auto-and-Manual-Commit-Modes)
  - [Driver Manager](https://github.com/dbeaver/dbeaver/wiki/Driver-Manager)
- Databases support
  - Classic
    - [Apache Hive/Spark/Impala](https://github.com/dbeaver/dbeaver/wiki/Apache-Hive)
    - [Cassandra](https://github.com/dbeaver/dbeaver/wiki/Cassandra)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [ClickHouse](https://github.com/dbeaver/dbeaver/wiki/Clickhouse)
    - [Couchbase](https://github.com/dbeaver/dbeaver/wiki/Couchbase)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [Greenplum](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Greenplum)
    - [IBM Db2](https://github.com/dbeaver/dbeaver/wiki/Database-driver-IBM-Db2)
    - [InfluxDB](https://github.com/dbeaver/dbeaver/wiki/InfluxDB)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [MariaDB](https://github.com/dbeaver/dbeaver/wiki/Database-driver-MariaDB)
    - [Microsoft SQL Server](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Microsoft-SQL-Server)
    - [MongoDB](https://github.com/dbeaver/dbeaver/wiki/MongoDB)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [MySQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-MySQL)
    - [Netezza](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Netezza)
    - [Oracle](https://github.com/dbeaver/dbeaver/wiki/Oracle)
    - [PostgreSQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-PostgreSQL)
    - [Redis](https://github.com/dbeaver/dbeaver/wiki/Redis)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [Salesforce](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Salesforce)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [Teradata](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Teradata)
    - [Trino](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Trino)
    - [Yellowbrick](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Yellowbrick)
  - Cloud
    - AWS
      - [Athena](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Amazon-Athena)
      - [DocumentDB](https://github.com/dbeaver/dbeaver/wiki/AWS-DocumentDB)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [DynamoDB](https://github.com/dbeaver/dbeaver/wiki/AWS-DynamoDB)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Keyspaces](https://github.com/dbeaver/dbeaver/wiki/AWS-Keyspaces)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Neptune](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Neptune)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Redshift](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Amazon-Redshift)
      - [Timestream](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Amazon-Timestream)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - Azure
      - [Cosmos DB](https://github.com/dbeaver/dbeaver/wiki/Database-driver-CosmosDB)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Cosmos DB for NoSQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Azure-CosmosDB-for-NoSQL)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Databricks](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Databricks)
    - Google
      - [AlloyDB for PostgreSQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-AlloyDB-for-PostgreSQL)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [BigQuery](https://github.com/dbeaver/dbeaver/wiki/Database-driver-BigQuery)
      - [Bigtable](https://github.com/dbeaver/dbeaver/wiki/Google-Bigtable)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Cloud SQL for MySQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-MySQL-on-Google-Cloud)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Cloud SQL for PostgreSQL](https://github.com/dbeaver/dbeaver/wiki/Database-driver-PostgreSQL-on-Google-Cloud)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Cloud SQL for SQL Server](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Microsoft-SQL-Server-on-Google-Cloud)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Firestore](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Firestore)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
      - [Spanner](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Google-Cloud-Spanner)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [Snowflake](https://github.com/dbeaver/dbeaver/wiki/Snowflake)
  - Embedded
    - [SQLite](https://github.com/dbeaver/dbeaver/wiki/Database-driver-SQLite)
  - File drivers
    - [Multi Source](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Files-MultiSource)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [CSV](https://github.com/dbeaver/dbeaver/wiki/Database-driver-CSV)
    - [JSON](https://github.com/dbeaver/dbeaver/wiki/Database-driver-JSON)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [Parquet](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Parquet)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [XLSX](https://github.com/dbeaver/dbeaver/wiki/Database-driver-XLSX)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
    - [XML](https://github.com/dbeaver/dbeaver/wiki/Database-driver-XML)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - Graph
    - [Neo4j](https://github.com/dbeaver/dbeaver/wiki/Database-driver-Neo4j)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
- [Database Navigator](https://github.com/dbeaver/dbeaver/wiki/Database-Navigator)
- [Data Editor](https://github.com/dbeaver/dbeaver/wiki/Data-Editor)
- [SQL Editor](https://github.com/dbeaver/dbeaver/wiki/SQL-Editor)
- [Entity relation diagrams (ERD)](https://github.com/dbeaver/dbeaver/wiki/ER-Diagrams)
- Cloud services
  - [Cloud Explorer](https://github.com/dbeaver/dbeaver/wiki/Cloud-Explorer)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Cloud Storage](https://github.com/dbeaver/dbeaver/wiki/Cloud-Storage)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
- [AI Assistant](https://github.com/dbeaver/dbeaver/wiki/AI-Smart-Assistance-in-DBeaver-Community)
- [Data transfer and schema compare](https://github.com/dbeaver/dbeaver/wiki/Data-transfer)  - [Data import](https://github.com/dbeaver/dbeaver/wiki/Data-import)
  - [Data export](https://github.com/dbeaver/dbeaver/wiki/Data-export)
  - [Data compare](https://github.com/dbeaver/dbeaver/wiki/Data-compare)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Backup and restore](https://github.com/dbeaver/dbeaver/wiki/Backup-Restore)
  - [Schema compare](https://github.com/dbeaver/dbeaver/wiki/Schema-compare)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
- [Task management](https://github.com/dbeaver/dbeaver/wiki/Task-Management)  - [Task scheduler](https://github.com/dbeaver/dbeaver/wiki/Task-Scheduler)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Composite tasks](https://github.com/dbeaver/dbeaver/wiki/Composite-Tasks)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
- Integrated tools
  - [GIT integration](https://github.com/dbeaver/dbeaver/wiki/Project-team-work)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Tableau integration](https://github.com/dbeaver/dbeaver/wiki/Tableau-integration-in-DBeaver)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Database debugger (PostgreSQL)](https://github.com/dbeaver/dbeaver/wiki/PGDebugger)![](https://github.com/dbeaver/dbeaver/wiki/images/commercial.png)
  - [Session Manager](https://github.com/dbeaver/dbeaver/wiki/Session-Manager-Guide)
  - [Lock Manager](https://github.com/dbeaver/dbeaver/wiki/Lock-Manager)
- Administration
  - [Admin preferences](https://github.com/dbeaver/dbeaver/wiki/Admin-Manage-Preferences)
  - [Configuration files](https://github.com/dbeaver/dbeaver/wiki/Configuration-files-in-DBeaver)
  - [Command line](https://github.com/dbeaver/dbeaver/wiki/Command-Line)
  - [Error log](https://github.com/dbeaver/dbeaver/wiki/Log-files)
  - [Troubleshooting system issues](https://github.com/dbeaver/dbeaver/wiki/Troubleshooting-system-issues)
- DBeaver Editions
  - [Enterprise edition](https://github.com/dbeaver/dbeaver/wiki/Enterprise-Edition)
  - [Lite edition](https://github.com/dbeaver/dbeaver/wiki/Lite-Edition)
  - [Ultimate edition](https://github.com/dbeaver/dbeaver/wiki/Ultimate-Edition)
- [FAQ](https://github.com/dbeaver/dbeaver/wiki/FAQ)
- Development
  - [Build from sources](https://github.com/dbeaver/dbeaver/wiki/Build-from-sources)
  - [Develop in Eclipse](https://github.com/dbeaver/dbeaver/wiki/Develop-in-Eclipse)
  - [Develop in IDEA](https://github.com/dbeaver/dbeaver/wiki/Develop-in-IDEA)
  - [Resources localization](https://github.com/dbeaver/dbeaver/wiki/Localization)
  - [Unit Tests](https://github.com/dbeaver/dbeaver/wiki/Unit-Tests)
  - [Code contribution](https://github.com/dbeaver/dbeaver/wiki/Contribute-your-code)

### Clone this wiki locally

You can’t perform that action at this time.