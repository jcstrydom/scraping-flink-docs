Document Feedback

# Overview

Last Updated：2023-12-25 03:49:42  Updated
share

share

OceanBase Database provides various built-in data types. These data types are also called the basic data types of OceanBase Database. This chapter describes the syntax, parameters, and usage instructions of data types supported by the current OceanBase Database version.

Each value in OceanBase Database operations belongs to a specific data type. The data type of a value represents a fixed set of attributes. These attributes allow OceanBase Database to differentiate values of one data type from those of another.

The current version of OceanBase Database supports the following built-in data types:

- [Character data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001108002)

- [Numeric data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107984)

- [Datetime and interval data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107993)

- [RAW data type](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107075)

- [Large object data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107996)

- [Rowid data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107071)

- [JSON data type](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001107999)

- [XML data type](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001108011)


Previous topic

[ROWID pseudocolumn](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001106301)

[Last](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001106301)

Next topic

[Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001108002)

[Next](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001108002)

Preview

- ![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*y6ocSqN8cqsAAAAAAAAAAAAAARQnAQ)
- ![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*BG9IQJyLHF8AAAAAAAAAAAAAARQnAQ)

- ![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*eTWdQKCRKHwAAAAAAAAAAAAAARQnAQ)

编组

[Contact Us](https://en.oceanbase.com/contactus?recordName=right&fromPage=/docs/common-oceanbase-database-10000000001107076)

![](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*GfWWQZaofCAAAAAAAAAAAAAAARQnAQ)

Mouse selected content, quick feedback problems

Select the content in the document with doubts, you can quickly feedback the problem, we will follow up to deal with.

For example:

![demo](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*_RzYS6qOROwAAAAAAAAAAAAAARQnAQ)

Ok, got it

编组 3

![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*y6ocSqN8cqsAAAAAAAAAAAAAARQnAQ)

![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*BG9IQJyLHF8AAAAAAAAAAAAAARQnAQ)

![helpful](https://gw.alipayobjects.com/mdn/ob_asset/afts/img/A*eTWdQKCRKHwAAAAAAAAAAAAAARQnAQ)

编组 7

[Contact Us](https://en.oceanbase.com/contactus?recordName=right&fromPage=/docs/common-oceanbase-database-10000000001107076)

编组

All Products

- Databases
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ob+sever_%E8%93%9D%E8%89%B2icon.png)[OceanBase Database](https://en.oceanbase.com/docs/oceanbase-database)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/%E5%85%AC%E6%9C%89%E4%BA%91_%E8%93%9D%E8%89%B2icon.png)[OceanBase Cloud](https://en.oceanbase.com/docs/oceanbase-cloud)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/%E5%9B%BE%E6%95%B0%E6%8D%AE%E5%BA%93_%E8%93%9D%E8%89%B2icon.png)[OceanBase Tugraph](https://en.oceanbase.com/docs/tugraph-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/%E5%85%AC%E6%9C%89%E4%BA%91_%E8%93%9D%E8%89%B2icon.png)[Interactive Tutorials](https://en.oceanbase.com/docs/interactive-tutorials)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ob+sever_%E8%93%9D%E8%89%B2icon.png)[OceanBase Best Practices](https://en.oceanbase.com/docs/best-practices)
- Tools
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/OCP_%E8%93%9D%E8%89%B2icon.png)[OceanBase Cloud Platform](https://en.oceanbase.com/docs/ocp-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/OMS_%E8%93%9D%E8%89%B2icon.png)[OceanBase Migration Service](https://en.oceanbase.com/docs/oms-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ODC_%E8%93%9D%E8%89%B2icon.png)[OceanBase Developer Center](https://en.oceanbase.com/docs/odc-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/OMA_%E8%93%9D%E8%89%B2icon.png)[OceanBase Migration Assessment](https://en.oceanbase.com/docs/oma-doc-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/OAT_%E8%93%9D%E8%89%B2icon.png)[OceanBase Admin Tool](https://en.oceanbase.com/docs/oat)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/%E5%AF%BC%E6%95%B0%E5%B7%A5%E5%85%B7_%E8%93%9D%E8%89%B2icon.png)[OceanBase Loader and Dumper](https://en.oceanbase.com/docs/obloader-obdumper-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/OBD_%E8%93%9D%E8%89%B2icon.png)[OceanBase Deployer](https://en.oceanbase.com/docs/obd-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ob+sever_%E8%93%9D%E8%89%B2icon.png)[Kubernetes operator for OceanBase](https://en.oceanbase.com/docs/ob-operator-doc-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ob+sever_%E8%93%9D%E8%89%B2icon.png)[OceanBase Diagnostic Tool](https://en.oceanbase.com/docs/obdiag-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/resource-management/image/docs-icon-oblogproxy.png)[OceanBase Binlog Service](https://en.oceanbase.com/docs/oblogproxy)
- Connectors and Middleware
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ODP_%E8%93%9D%E8%89%B2icon.png)[OceanBase Database Proxy](https://en.oceanbase.com/docs/odp-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/%E5%B5%8C%E5%85%A5%E5%BC%8F+SQL+%E9%A2%84%E7%BC%96%E8%AF%91%E5%99%A8_%E8%93%9D%E8%89%B2icon.png)[Embedded SQL in C for OceanBase](https://en.oceanbase.com/docs/ecob-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/C%E8%AF%AD%E8%A8%80%E8%B0%83%E7%94%A8%E6%8E%A5%E5%8F%A3_%E8%93%9D%E8%89%B2icon.png)[OceanBase Call Interface](https://en.oceanbase.com/docs/obci-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/Connector+C_%E8%93%9D%E8%89%B2icon.png)[OceanBase Connector/C](https://en.oceanbase.com/docs/oceanbase-connector-c-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/Connector+J_%E8%93%9D%E8%89%B2icon.png)[OceanBase Connector/J](https://en.oceanbase.com/docs/oceanbase-connector-j-en)
- ![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ODBC_%E8%93%9D%E8%89%B2icon.png)[OceanBase Connector/ODBC](https://en.oceanbase.com/docs/obodbc-en)

![icon](https://obportal.s3.ap-southeast-1.amazonaws.com/product-depository/blue/ob+sever_%E8%93%9D%E8%89%B2icon.png)

OceanBase Database

SQL - V4.2.1

![](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*5Oy_QZjvTg8AAAAAAAAAAAAADiGDAQ/original)

Download PDF

[Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103404 " Overview") [Differences between the Enterprise Edition and the Community Edition](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103405 " Differences between the Enterprise Edition and the Community Edition") [System architecture](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103407 " System architecture") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103658 " Overview") [SQL data types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103660 " SQL data types") [Built-in functions](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103661 " Built-in functions") [System views](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103659 " System views") [Compatibility with MySQL](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103402 " Compatibility with MySQL") [Limitations](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103406 " Limitations") [Quick start with OceanBase Database Community Edition](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103382 " Quick start with OceanBase Database Community Edition") [Before you begin](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103586 " Before you begin") [Basic SQL operations (MySQL mode)](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103585 " Basic SQL operations (MySQL mode)") [Basic SQL operations (Oracle mode)](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103584 " Basic SQL operations (Oracle mode)") [Build a Java application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103583 " Build a Java application") [Build a C application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103582 " Build a C application") [Build a Python application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103590 " Build a Python application") [Build a Java application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103588 " Build a Java application") [Build a C application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103589 " Build a C application") [Build a Go application](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103587 " Build a Go application") [Try out operational OLAP](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103580 " Try out operational OLAP") [Try out parallel import and data compression](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103581 " Try out parallel import and data compression") [Try out the multi-tenant feature](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103578 " Try out the multi-tenant feature") [Video tutorials](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103381 " Video tutorials") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103375 " Overview") [HA deployment solutions for OceanBase clusters](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103376 " HA deployment solutions for OceanBase clusters") [Deployment process](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103577 " Deployment process") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103572 " Overview") [Deploy OceanBase Database in a Kubernetes cluster](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103573 " Deploy OceanBase Database in a Kubernetes cluster") [Clear an OceanBase cluster](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103373 " Clear an OceanBase cluster") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103398 " Overview") [Use OMS to migrate data from a MySQL database to a MySQL tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103630 " Use OMS to migrate data from a MySQL database to a MySQL tenant of OceanBase Database") [Use mydumper and myloader to migrate data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103631 " Use mydumper and myloader to migrate data from a MySQL database to OceanBase Database") [Use DBCAT to migrate schemas from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103635 " Use DBCAT to migrate schemas from a MySQL database to OceanBase Database") [Use DataX to migrate table data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103634 " Use DataX to migrate table data from a MySQL database to OceanBase Database") [Use CloudCanal to migrate data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103633 " Use CloudCanal to migrate data from a MySQL database to OceanBase Database") [Use Canal to synchronize data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103636 " Use Canal to synchronize data from a MySQL database to OceanBase Database") [Use Flink CDC to synchronize data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103629 " Use Flink CDC to synchronize data from a MySQL database to OceanBase Database") [Use ChunJun to migrate data from a MySQL database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103632 " Use ChunJun to migrate data from a MySQL database to OceanBase Database") [Use OMS to migrate data from a MySQL tenant of OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103619 " Use OMS to migrate data from a MySQL tenant of OceanBase Database to a MySQL database") [Use OMS to migrate incremental data from an Oracle tenant of OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103613 " Use OMS to migrate incremental data from an Oracle tenant of OceanBase Database to a MySQL database") [Use DBCAT to migrate schemas from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103617 " Use DBCAT to migrate schemas from OceanBase Database to a MySQL database") [Use DataX to migrate table data from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103612 " Use DataX to migrate table data from OceanBase Database to a MySQL database") [Use Canal to synchronize data from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103616 " Use Canal to synchronize data from OceanBase Database to a MySQL database") [Use CloudCanal to migrate data from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103618 " Use CloudCanal to migrate data from OceanBase Database to a MySQL database") [Use Flink CDC to migrate data from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103614 " Use Flink CDC to migrate data from OceanBase Database to a MySQL database") [Use ChunJun to migrate data from OceanBase Database to a MySQL database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103615 " Use ChunJun to migrate data from OceanBase Database to a MySQL database") [Use OMS to migrate data from an Oracle database to a MySQL tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103611 " Use OMS to migrate data from an Oracle database to a MySQL tenant of OceanBase Database") [Use OMS to migrate data from an Oracle database to an Oracle tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103608 " Use OMS to migrate data from an Oracle database to an Oracle tenant of OceanBase Database") [Use DBCAT to migrate schemas from an Oracle database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103610 " Use DBCAT to migrate schemas from an Oracle database to OceanBase Database") [Use DataX to migrate table data from an Oracle database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103609 " Use DataX to migrate table data from an Oracle database to OceanBase Database") [Use OMS to migrate data from an Oracle tenant of OceanBase Database to an Oracle database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103641 " Use OMS to migrate data from an Oracle tenant of OceanBase Database to an Oracle database") [Use DBCAT to migrate schemas from OceanBase Database to an Oracle database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103639 " Use DBCAT to migrate schemas from OceanBase Database to an Oracle database") [Use DataX to migrate table data from OceanBase Database to an Oracle database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103640 " Use DataX to migrate table data from OceanBase Database to an Oracle database") [Use OMS to migrate data from a DB2 LUW database to a MySQL tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103605 " Use OMS to migrate data from a DB2 LUW database to a MySQL tenant of OceanBase Database") [Use OMS to migrate data from a DB2 LUW database to an Oracle tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103606 " Use OMS to migrate data from a DB2 LUW database to an Oracle tenant of OceanBase Database") [Use DBCAT to migrate table schemas from a DB2 LUW database to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103607 " Use DBCAT to migrate table schemas from a DB2 LUW database to OceanBase Database") [Use OMS to migrate data from a MySQL tenant of OceanBase Database to a DB2 LUW database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103646 " Use OMS to migrate data from a MySQL tenant of OceanBase Database to a DB2 LUW database") [Use OMS to migrate data from an Oracle tenant of OceanBase Database to a DB2 LUW database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103647 " Use OMS to migrate data from an Oracle tenant of OceanBase Database to a DB2 LUW database") [Use OMS to migrate data from a TiDB database to a MySQL tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103648 " Use OMS to migrate data from a TiDB database to a MySQL tenant of OceanBase Database") [Use OMS to migrate data from a PostgreSQL database to a MySQL tenant of OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103642 " Use OMS to migrate data from a PostgreSQL database to a MySQL tenant of OceanBase Database") [Use DataX to migrate CSV files to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103638 " Use DataX to migrate CSV files to OceanBase Database") [Import data by using the LOAD DATA statement](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103637 " Import data by using the LOAD DATA statement") [Import data from SQL files to OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103397 " Import data from SQL files to OceanBase Database") [Use OMS to migrate data from an OceanBase Database tenant to another of the same type](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103621 " Use OMS to migrate data from an OceanBase Database tenant to another of the same type") [Use OMS to migrate data from an OceanBase Database tenant to another of the same type in active-active disaster recovery scenarios](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103622 " Use OMS to migrate data from an OceanBase Database tenant to another of the same type in active-active disaster recovery scenarios") [Use OBLOADER & OBDUMPER to migrate data between MySQL tenants in OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103624 " Use OBLOADER & OBDUMPER to migrate data between MySQL tenants in OceanBase Database") [Use OBLOADER & OBDUMPER to migrate data from a MySQL tenant to an Oracle tenant in OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103620 " Use OBLOADER & OBDUMPER to migrate data from a MySQL tenant to an Oracle tenant in OceanBase Database") [Use OBLOADER & OBDUMPER to migrate data between Oracle tenants in OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103623 " Use OBLOADER & OBDUMPER to migrate data between Oracle tenants in OceanBase Database") [Use OBLOADER & OBDUMPER to migrate data from an Oracle tenant to a MySQL tenant in OceanBase Database](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103625 " Use OBLOADER & OBDUMPER to migrate data from an Oracle tenant to a MySQL tenant in OceanBase Database") [Migrate data between tables](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103645 " Migrate data between tables") [Migrate resource units](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103644 " Migrate resource units") [Export data by using OUTFILE statements](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103643 " Export data by using OUTFILE statements") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103628 " Overview") [Import data in bypass mode by using the LOAD DATA statement](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103627 " Import data in bypass mode by using the LOAD DATA statement") [Import data in bypass mode by using the INSERT INTO SELECT statement](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103626 " Import data in bypass mode by using the INSERT INTO SELECT statement") [Log on to an OceanBase Database tenant](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103367 " Log on to an OceanBase Database tenant") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103521 " Overview") [Cluster parameters](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103520 " Cluster parameters") [Tenant introduction](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103550 " Tenant introduction") [Tenant capacity](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103548 " Tenant capacity") [Tenant types](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103549 " Tenant types") [User tenant introduction](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103546 " User tenant introduction") [Tenant system variables](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103547 " Tenant system variables") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103509 " Overview") [Traffic distribution](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103506 " Traffic distribution") [Data distribution](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103508 " Data distribution") [High availability overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103544 " High availability overview") [Flashback queries](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103543 " Flashback queries") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103528 " Overview") [Introduction to physical backup and restore](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103530 " Introduction to physical backup and restore") [Deploy NFS](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103535 " Deploy NFS") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103563 " Overview") [Cases](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103564 " Cases") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103569 " Overview") [Log levels](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103565 " Log levels") [Log stability](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103570 " Log stability") [Log control](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103568 " Log control") [Log metrics](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103567 " Log metrics") [Overview](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103553 " Overview") [Identify bottlenecks on the data link](https://en.oceanbase.com/docs/common-oceanbase-database-10000000001103552 " Identify bottlenecks on the data link")

![OceanBase](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*fY82Q4Wd8eAAAAAAAAAAAAAADiGDAQ/original)![OceanBase](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*fY82Q4Wd8eAAAAAAAAAAAAAADiGDAQ/original)

OceanBase, A Highly Scalable Database for Transactional, Analytical, and AI Workloads.

Company

[About OceanBase](https://en.oceanbase.com/about) [Contact Us](https://en.oceanbase.com/contactus?recordName=footer&fromPage=/docs/common-oceanbase-database-10000000001107076) [Partner](https://en.oceanbase.com/partner)

Product

[OceanBase Cloud](https://en.oceanbase.com/product/cloud) [OceanBase Enterprise](https://en.oceanbase.com/product/oceanbase) [Quick Start](https://en.oceanbase.com/quickstart) [Download](https://en.oceanbase.com/softwarecenter) [Pricing](https://en.oceanbase.com/docs/common-oceanbase-cloud-10000000000924007)

Resources

[Docs](https://en.oceanbase.com/docs) [Blog](https://en.oceanbase.com/blog) [White Paper](https://en.oceanbase.com/whitepaper) [Trust Center](https://en.oceanbase.com/trust)

Follow us

[![LinkedIn](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*tWwDRZ2e_8QAAAAAAAAAAAAADiGDAQ/original)LinkedIn](https://www.linkedin.com/company/oceanbase) [![Discord](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*aLAhQacaHX8AAAAAJAAAAAgAeiGDAQ/original)Discord](https://discord.gg/74cF8vbNEs) [![Twitter](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*RW0HSb-qAnsAAAAAAAAAAAAADiGDAQ/original)Twitter](https://x.com/oceanbasedb) [![Youtube](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*806wSbAt88MAAAAAI1AAAAgAeiGDAQ/original)Youtube](https://www.youtube.com/@OceanBaseDB) [![Forum](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*lZhcRaAVrY0AAAAAG8AAAAgAeiGDAQ/original)Forum](https://github.com/oceanbase/oceanbase/discussions) [![GitHub](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*R9ZUSLXvdLEAAAAAAAAAAAAADiGDAQ/original)GitHub](https://github.com/oceanbase/oceanbase) [![Stack Overflow](https://mdn.alipayobjects.com/huamei_22khvb/afts/img/A*GgGNSYJ0ZkwAAAAAAAAAAAAADiGDAQ/original)Stack Overflow](https://stackoverflow.com/questions/tagged/oceanbase)

© OceanBase 2024. All rights reserved \| [Cloud Service Agreement](https://en.oceanbase.com/legal/service-agreement) \| [Privacy Policy](https://en.oceanbase.com/legal/privacy) \| [Legal](https://en.oceanbase.com/legal) \| [Security](https://en.oceanbase.com/security)