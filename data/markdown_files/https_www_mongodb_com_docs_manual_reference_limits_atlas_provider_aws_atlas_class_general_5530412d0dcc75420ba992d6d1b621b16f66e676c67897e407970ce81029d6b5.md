Docs Menu

Ask MongoDB AI

[Docs Home](https://www.mongodb.com/docs/)

/

[Development](https://www.mongodb.com/docs/development)

/

[Reference](https://www.mongodb.com/docs/manual/reference)

[Docs Home](https://www.mongodb.com/docs/)

/

[Development](https://www.mongodb.com/docs/development)

/

[Reference](https://www.mongodb.com/docs/manual/reference)

[Docs Home](https://www.mongodb.com/docs/)

/

[Development](https://www.mongodb.com/docs/development)

/

[Reference](https://www.mongodb.com/docs/manual/reference)

# MongoDB Limits and Thresholds [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-limits-and-thresholds "Permalink to this heading")

Copy page

This document provides a collection of hard and soft limitations of the
MongoDB system. The limitations on this page apply to deployments hosted
in Atlas and self-hosted MongoDB deployments, unless specified
otherwise.

## MongoDB Atlas Limitations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-limitations "Permalink to this heading")

The following limitations apply only to deployments hosted in
MongoDB Atlas. If any of these limits present a problem for your organization, contact [Atlas support.](https://www.mongodb.com/docs/atlas/support/)

### MongoDB Atlas Cluster Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-cluster-limits "Permalink to this heading")

| Component | Limit |
| --- | --- |
| Shards in<br>[multi-region clusters](https://www.mongodb.com/docs/atlas/cluster-config/multi-cloud-distribution/) | 12 |
| Shards in single-region clusters | 70 |
| [Cross-region network permissions](https://www.mongodb.com/docs/atlas/reference/faq/networking/#std-label-faq-cross-region)<br>for a multi-region cluster | 40\. Additionally, a cluster in any [project](https://www.mongodb.com/docs/atlas/organizations-projects/#std-label-projects) spans more than 40 regions, you can't create a<br>multi-region cluster in this project. |
| [Electable nodes](https://www.mongodb.com/docs/manual/core/replica-set-elections/#std-label-replica-set-elections) per<br>replica set or shard | 7 |
| [Cluster tier](https://www.mongodb.com/docs/atlas/manage-clusters/#select-cluster-tier)<br>for the [Config server](https://www.mongodb.com/docs/manual/core/sharded-cluster-config-servers/#std-label-sharding-config-server) (minimum<br>and maximum) | `M30` |

### MongoDB Atlas Connection Limits and Cluster Tier [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-connection-limits-and-cluster-tier "Permalink to this heading")

MongoDB Atlas limits concurrent incoming connections
based on the cluster tier and [class](https://www.mongodb.com/docs/atlas/customize-storage/#std-label-storage-class-ui).
MongoDB Atlas connection limits apply per node. For
sharded clusters, MongoDB Atlas connection limits apply per
[mongos](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-sharding-read-operations) router. The number of
[mongos](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-sharding-read-operations) routers is equal to
the number of replica set nodes across all shards.

Your [read preference](https://www.mongodb.com/docs/manual/core/read-preference/) also
contributes to the total number of connections that MongoDB Atlas can
allocate for a given query.

MongoDB Atlas has the following connection limits for the specified cluster
tiers:

Atlas Provider

AWS

Atlas Class

General Class

| MongoDB Atlas Cluster Tier | Maximum Connections Per Node |
| --- | --- |
| `Free` | 500 |
| `Flex` | 500 |
| `M10` | 1500 |
| `M20` | 3000 |
| `M30` | 3000 |
| `M40` | 6000 |
| `M50` | 16000 |
| `M60` | 32000 |
| `M80` | 96000 |
| `M140` | 96000 |
| `M200` | 128000 |
| `M300` | 128000 |

## Note

MongoDB Atlas reserves a small number of connections to each cluster for
supporting MongoDB Atlas services.

### MongoDB Atlas Multi-Cloud Connection Limitation [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-multi-cloud-connection-limitation "Permalink to this heading")

If you're connecting to a multi-cloud MongoDB Atlas deployment through a
[private connection](https://www.mongodb.com/docs/atlas/reference/faq/connection-changes/#std-label-conn-string-options), you can access only
the nodes in the same cloud provider that you're connecting from. This
cloud provider might not have the [primary](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary) node in its region.
When this happens, you must specify the
[secondary read preference](https://www.mongodb.com/docs/manual/core/read-preference/#std-label-read-preference) mode in the
connection string to access the deployment.

If you need access to all nodes for your multi-cloud MongoDB Atlas
deployment from your current provider through a private connection, you
must perform one of the following actions:

- Configure a VPN in the current provider to each of the remaining
providers.

- Configure a [private endpoint](https://www.mongodb.com/docs/atlas/security-configure-private-endpoints/#std-label-private-endpoint) to MongoDB Atlas
for each of the remaining providers.


### MongoDB Atlas Collection and Index Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-collection-and-index-limits "Permalink to this heading")

While there is no hard limit on the number of collections in a single
MongoDB Atlas cluster, the performance of a cluster might degrade if it
serves a large number of collections and indexes. Larger collections
have a greater impact on performance.

The recommended maximum combined number of collections and indexes by
MongoDB Atlas cluster tier are as follows:

| MongoDB Atlas Cluster Tier | Recommended Maximum |
| --- | --- |
| `M10` | 5,000 collections and indexes |
| `M20` / `M30` | 10,000 collections and indexes |
| `M40`/+ | 100,000 collections and indexes |

### MongoDB Atlas Organization and Project Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-organization-and-project-limits "Permalink to this heading")

MongoDB Atlas deployments have the following organization and project
limits:

| Component | Limit |
| --- | --- |
| [Database users](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/) per<br>MongoDB Atlas project | 100 |
| [Atlas users](https://www.mongodb.com/docs/atlas/access/manage-org-users/) per<br>MongoDB Atlas project | 500 |
| Atlas users per MongoDB Atlas organization | 500 |
| API Keys per MongoDB Atlas organization | 500 |
| [Access list entries](https://www.mongodb.com/docs/atlas/security/ip-access-list/) per<br>MongoDB Atlas Project | 200 |
| Users per MongoDB Atlas team | 250 |
| Teams per MongoDB Atlas project | 100 |
| Teams per MongoDB Atlas organization | 250 |
| Teams per MongoDB Atlas user | 100 |
| Organizations per MongoDB Atlas user | 250 |
| [Linked organizations](https://www.mongodb.com/docs/atlas/billing/#std-label-cross-org-billing) per<br>cross-organization configuration | 250 |
| Clusters per MongoDB Atlas project | 25 |
| Projects per MongoDB Atlas organization | 250 |
| [Custom MongoDB roles](https://www.mongodb.com/docs/atlas/security-add-mongodb-roles/) per<br>MongoDB Atlas project | 100 |
| Assigned roles per database user | 100 |
| Hourly billing per MongoDB Atlas organization | $50 |
| [Federated database instances](https://www.mongodb.com/docs/atlas/data-federation/#std-label-atlas-data-federation) per<br>MongoDB Atlas project | 25 |
| Total Network Peering Connections per MongoDB Atlas<br>project | 50\. Additionally, MongoDB Atlas limits the number of nodes per<br>[Network Peering connection](https://www.mongodb.com/docs/atlas/security-vpc-peering/#std-label-vpc-peering) based on the<br>CIDR block and the<br>[region](https://www.mongodb.com/docs/atlas/cloud-providers-regions/)<br>selected for the project. |
| Pending network peering connections per MongoDB Atlas<br>project | 25 |
| [AWS Private Link](https://www.mongodb.com/docs/atlas/security-private-endpoint/#std-label-atlas-pl-limitations) addressable<br>targets per region | 50 |
| [Azure PrivateLink](https://www.mongodb.com/docs/atlas/security-private-endpoint/#std-label-atlas-pl-limitations) addressable<br>targets per region | 150 |
| Unique shard keys per MongoDB Atlas-managed Global Cluster project | 40\. This applies only to Global Clusters with [Atlas-Managed\<br>Sharding](https://www.mongodb.com/docs/atlas/tutorial/create-global-cluster/). There are no limits on<br>the number of unique shard keys per project for [Global Clusters\<br>with Self-Managed Sharding.](https://www.mongodb.com/docs/atlas/shard-global-collection/) |
| `Free` clusters per MongoDB Atlas project | 1 |
| Number of [alert configurations](https://www.mongodb.com/docs/atlas/configure-alerts/#std-label-configure-alerts) for<br>each MongoDB Atlas project. | 500 |

### MongoDB Atlas Service Account Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-service-account-limits "Permalink to this heading")

MongoDB Atlas service accounts have the following organization and project
limits:

| Component | Limit |
| --- | --- |
| [Atlas service accounts](https://www.mongodb.com/docs/atlas/configure-api-access/) per MongoDB Atlas organization | 200 |
| [Access list entries](https://www.mongodb.com/docs/atlas/security/ip-access-list/) per MongoDB Atlas service account | 200 |
| [Secrets](https://www.mongodb.com/docs/atlas/configure-api-access/) per MongoDB Atlas service account | 2 |
| [Active tokens](https://www.mongodb.com/docs/atlas/configure-api-access/) per MongoDB Atlas service account | 100 |

### MongoDB Atlas Label Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-label-limits "Permalink to this heading")

MongoDB Atlas limits the length and enforces ReGex requirements for the
following component labels:

| Component | Character Limit | RegEx Pattern |
| --- | --- | --- |
| Cluster Name | 64 [\[1\]](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#footnote-1) | `^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$` [\[2\]](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#footnote-2) |
| Project Name | 64 | `^[\p{L}\p{N}\-_.(),:&@+']{1,64}$` [\[3\]](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#footnote-3) |
| Organization Name | 64 | `^[\p{L}\p{N}\-_.(),:&@+']{1,64}$` [\[3\]](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#footnote-3) |
| API Key Description | 250 |  |

|     |     |
| --- | --- |
| \[ [1](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#ref-1-id1)\] | If you have [peering-only mode enabled](https://www.mongodb.com/docs/atlas/reference/faq/connection-changes/#std-label-atlas-faq-azure-gcp-peering-only), the cluster name<br>character limit is 23. |

|     |     |
| --- | --- |
| \[ [2](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#ref-2-id2)\] | MongoDB Atlas uses the first 23 characters of a cluster's name.<br>These characters must be unique within the cluster's project.<br>Cluster names with fewer than 23 characters can't end with a<br>hyphen (`-`). Cluster names with more than 23 characters can't<br>have a hyphen as the 23rd character. |

|     |     |
| --- | --- |
| \[3\] | _( [1](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#ref-3-id3), [2](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#ref-3-id4))_ Organization and project names can include any Unicode letter or<br>number plus the following punctuation: `-_.(),:&@+'`. |

### Free Cluster, and Flex Cluster Limitations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#free-cluster--and-flex-cluster-limitations "Permalink to this heading")

Additional limitations apply to MongoDB Atlas free clusters, and Flex clusters.
To learn more, see the following resources:

- [Atlas Free Cluster Limitations](https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/)

- [Atlas Flex Limitations](https://www.mongodb.com/docs/atlas/reference/flex-limitations/)


### MongoDB Atlas Command Limitations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-atlas-command-limitations "Permalink to this heading")

Some MongoDB commands are unsupported in MongoDB Atlas. Additionally, some
commands are supported only in MongoDB Atlas free clusters. To learn more,
see the following resources:

- [Unsupported Commands in Atlas](https://www.mongodb.com/docs/atlas/unsupported-commands/)

- [Commands Available Only in Free Clusters](https://www.mongodb.com/docs/atlas/free-tier-commands/)


## Collection and Database Size Limits [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#collection-and-database-size-limits "Permalink to this heading")

MongoDB does not impose a hard limit on collection or database sizes.
The maximum size of a collection or database depends on the file system
of the host server. For example:

- **ext4**: Maximum file size of 16 tebibytes (TiB).

- **XFS**: Maximum file size of 8 exbibytes (EiB).


To scale beyond file system or hardware limits, MongoDB offers
strategies such as [sharding](https://www.mongodb.com/docs/manual/sharding/#std-label-sharding-sharded-cluster),
which allows collections to grow indefinitely. For collections nearing
these limits or performance bottlenecks, MongoDB recommends sharding or
migrating to a clustered setup such MongoDB Atlas, which
supports auto-scaling.

### Sharding and Initial Size [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#sharding-and-initial-size "Permalink to this heading")

When sharding a collection, MongoDB determines initial chunk ranges
based on the shard key and splits your data into manageable chunks.
These limits only affect the initial sharding operation:

- `chunkSize` (default: 128 MB).

- Average Shard Key Size (typical size is 16 bytes).


## BSON Documents [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#bson-documents "Permalink to this heading")

BSON Document Size [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-BSON-Document-Size "Permalink to this definition")

The maximum BSON document size is 16 mebibytes.

The maximum document size helps ensure that a single document cannot use an
excessive amount of RAM or, during transmission, an excessive amount of
bandwidth. To store documents larger than the maximum size, MongoDB provides the
GridFS API. For more information about GridFS, see [`mongofiles`](https://www.mongodb.com/docs/database-tools/mongofiles/#mongodb-binary-bin.mongofiles) and
the documentation for your [driver](https://www.mongodb.com/docs/drivers/)

Nested Depth for BSON Documents [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Nested-Depth-for-BSON-Documents "Permalink to this definition")

MongoDB supports no more than 100 levels of nesting for [BSON\\
documents](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-document). Each object or array adds a level.

## Naming Restrictions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#naming-restrictions "Permalink to this heading")

Use of Case in Database Names [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Use-of-Case-in-Database-Names "Permalink to this definition")

Do not rely on case to distinguish between databases. For example,
you cannot use two databases with names like, `salesData` and
`SalesData`.

After you create a database in MongoDB, you must use consistent
capitalization when you refer to it. For example, if you create the
`salesData` database, do not refer to it using alternate
capitalization such as `salesdata` or `SalesData`.

Restrictions on Database Names for Windows [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Restrictions-on-Database-Names-for-Windows "Permalink to this definition")

For MongoDB deployments running on Windows, database names cannot
contain any of the following characters:

```
/\. "$*<>:|?
```

Also database names cannot contain the null character.

Restrictions on Database Names for Unix and Linux Systems [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Restrictions-on-Database-Names-for-Unix-and-Linux-Systems "Permalink to this definition")

For MongoDB deployments running on Unix and Linux systems, database
names cannot contain any of the following characters:

```
/\. "$
```

Also database names cannot contain the null character.

Length of Database Names [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Length-of-Database-Names "Permalink to this definition")

Database names cannot be empty and must be less than 64 bytes.

Restriction on Collection Names [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Restriction-on-Collection-Names "Permalink to this definition")

Collection names should begin with an underscore or a letter
character, and _cannot_:

- contain the `$`.

- be an empty string (e.g. `""`).

- contain the null character.

- begin with the `system.` prefix. (Reserved for internal use.)

- contain `.system.`.


If your collection name includes special characters, such as the
underscore character, or begins with numbers, then to access the
collection use the [`db.getCollection()`](https://www.mongodb.com/docs/manual/reference/method/db.getCollection/#mongodb-method-db.getCollection) method in
[`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh) or a [similar method for your driver.](https://api.mongodb.com/)

Namespace Length:

The namespace length limit for unsharded collections and views is 255 bytes,
and 235 bytes for sharded collections. For a collection or a view, the namespace
includes the database name, the dot (`.`) separator, and the collection/view
name (e.g. `<database>.<collection>`).

Restrictions on Field Names [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Restrictions-on-Field-Names "Permalink to this definition")

- Field names **cannot** contain the `null` character.

- The server permits storage of field names that contain dots (`.`)
and dollar signs (`$`).

- MongodB 5.0 adds improved support for the use of (`$`) and (`.`)
in field names. There are some restrictions. See
[Field Name Considerations](https://www.mongodb.com/docs/manual/core/dot-dollar-considerations/#std-label-crud-concepts-dot-dollar-considerations) for more details.

- Each field name must be unique within the document. You must not store
documents with duplicate fields because MongoDB [CRUD](https://www.mongodb.com/docs/manual/crud/#std-label-crud)
operations might behave unexpectedly if a document has duplicate
fields.


Restrictions on \_id [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Restrictions-on-_id "Permalink to this definition")

The field name `_id` is reserved for use as a primary key; its value
must be unique in the collection, is immutable, and may be of any type
other than an array or regex. If the `_id` contains subfields, the
subfield names cannot begin with a (`$`) symbol.

## Naming Warnings [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#naming-warnings "Permalink to this heading")

## Warning

Use caution, the issues discussed in this section could lead to data
loss or corruption.

### MongoDB does not support duplicate field names [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#mongodb-does-not-support-duplicate-field-names "Permalink to this heading")

The MongoDB Query Language doesn't support documents with duplicate
field names:

- Although some BSON builders may support creating a BSON document with
duplicate field names, inserting these documents into MongoDB isn't
supported even if the insert succeeds, or appears to succeed.

- For example, inserting a BSON document with duplicate field names
through a MongoDB driver may result in the driver silently dropping
the duplicate values prior to insertion, or may result in an invalid
document being inserted that contains duplicate fields. Querying those
documents leads to inconsistent results.

- Updating documents with duplicate field names isn't
supported, even if the update succeeds or appears to succeed.


Starting in MongoDB 6.1, to see if a document has duplicate field names,
use the [`validate`](https://www.mongodb.com/docs/manual/reference/command/validate/#mongodb-dbcommand-dbcmd.validate) command with the `full` field set to
`true`. In any MongoDB version, use the [`$objectToArray`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/objectToArray/#mongodb-expression-exp.-objectToArray)
aggregation operator to see if a document has duplicate field names.

### Avoid Ambiguous Field Names [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#avoid-ambiguous-field-names "Permalink to this heading")

Do not use a field name that is the same as the
[dot notation](https://www.mongodb.com/docs/manual/core/document/#std-label-document-dot-notation-embedded-fields) for an
embedded field. If you have a document with an embedded field
`{ "a" : { "b": ... } }`, other documents in that collection should
**not** have a top-level field `"a.b"`.

If you can reference an embedded field and a top-level field in the same
way, indexing and sharding operations happen on the embedded field.
You cannot index or shard on the top-level field `"a.b"` while the
collection has an embedded field that you reference in the same way.

For example, if your collection contains documents with both an embedded
field `{ "a" : { "b": ... } }` and a top-level field `"a.b"`,
indexing and sharding operations happen on the embedded field. It is not
possible to index or shard on the top-level field `"a.b"` when your
collection also contains an embedded field `{ "a" : { "b": ... } }`.

### Import and Export Concerns With Dollar Signs (`$`) and Periods (`.`) [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#import-and-export-concerns-with-dollar-signs-----and-periods--.- "Permalink to this heading")

Starting in MongoDB 5.0, document field names can be dollar (`$`)
prefixed and can contain periods (`.`). However,
[`mongoimport`](https://www.mongodb.com/docs/database-tools/mongoimport/#mongodb-binary-bin.mongoimport) and [`mongoexport`](https://www.mongodb.com/docs/database-tools/mongoexport/#mongodb-binary-bin.mongoexport) may not work
as expected in some situations with field names that make use of these
characters.

[MongoDB Extended JSON v2](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/#std-label-extended-json-high-level-ref-v2)
cannot differentiate between type wrappers and fields that happen to
have the same name as type wrappers. Do not use Extended JSON
formats in contexts where the corresponding BSON representations
might include dollar (`$`) prefixed keys. The
[DBRef](https://www.mongodb.com/docs/manual/reference/database-references/#std-label-dbref-explanation) mechanism is an exception to this
general rule.

There are also restrictions on using [`mongoimport`](https://www.mongodb.com/docs/database-tools/mongoimport/#mongodb-binary-bin.mongoimport) and
[`mongoexport`](https://www.mongodb.com/docs/database-tools/mongoexport/#mongodb-binary-bin.mongoexport) with periods (`.`) in field names. Since
CSV files use the period (`.`) to represent data hierarchies, a
period (`.`) in a field name will be misinterpreted as a level of
nesting.

### Possible Data Loss With Dollar Signs (`$`) and Periods (`.`) [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#possible-data-loss-with-dollar-signs-----and-periods--.- "Permalink to this heading")

There is a small chance of data loss when using dollar (`$`) prefixed
field names or field names that contain periods (`.`) if these
field names are used in conjunction with unacknowledged writes
( [write concern](https://www.mongodb.com/docs/manual/reference/write-concern/#std-label-write-concern)`w=0`) on servers
that are older than MongoDB 5.0.

When running [`insert`](https://www.mongodb.com/docs/manual/reference/command/insert/#mongodb-dbcommand-dbcmd.insert), [`update`](https://www.mongodb.com/docs/manual/reference/command/update/#mongodb-dbcommand-dbcmd.update), and
[`findAndModify`](https://www.mongodb.com/docs/manual/reference/command/findAndModify/#mongodb-dbcommand-dbcmd.findAndModify) commands, drivers that are 5.0 compatible
remove restrictions on using documents with field names that are
dollar (`$`) prefixed or that contain periods (`.`). These field
names generated a client-side error in earlier driver versions.

The restrictions are removed regardless of the server version the
driver is connected to. If a 5.0 driver sends a document to an older
server, the document will be rejected without sending an error.

## Namespaces [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#namespaces "Permalink to this heading")

Namespace Length [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Namespace-Length "Permalink to this definition")

The namespace length limit for unsharded collections and views is 255 bytes,
and 235 bytes for sharded collections. For a collection or a view, the namespace
includes the database name, the dot (`.`) separator, and the collection/view
name (e.g. `<database>.<collection>`).

## Tip

[Naming Restrictions](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#std-label-faq-restrictions-on-collection-names)

## Indexes [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#indexes "Permalink to this heading")

Number of Indexes per Collection [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Number-of-Indexes-per-Collection "Permalink to this definition")

A single collection can have _no more_ than 64 indexes.

Number of Indexed Fields in a Compound Index [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Number-of-Indexed-Fields-in-a-Compound-Index "Permalink to this definition")

There can be no more than 32 fields in a compound index.

Queries cannot use both text and Geospatial Indexes [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Queries-cannot-use-both-text-and-Geospatial-Indexes "Permalink to this definition")

You cannot combine the [`$text`](https://www.mongodb.com/docs/manual/reference/operator/query/text/#mongodb-query-op.-text) query, which requires a
special [text index](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-text/create-text-index/#std-label-create-text-index), with a query operator
that requires a different type of special index. For example you
cannot combine [`$text`](https://www.mongodb.com/docs/manual/reference/operator/query/text/#mongodb-query-op.-text) query with the [`$near`](https://www.mongodb.com/docs/manual/reference/operator/query/near/#mongodb-query-op.-near) operator.

Fields with 2dsphere Indexes can only hold Geometries [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Fields-with-2dsphere-Indexes-can-only-hold-Geometries "Permalink to this definition")

Fields with [2dsphere](https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2dsphere/#std-label-2dsphere-index) indexes must hold geometry
data in the form of [coordinate pairs](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-legacy-coordinate-pairs)
or [GeoJSON](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-GeoJSON) data. If you attempt to insert a document with
non-geometry data in a `2dsphere` indexed field, or build a
`2dsphere` index on a collection where the indexed field has
non-geometry data, the operation will fail.

## Tip

The unique indexes limit in [Sharding Operational Restrictions.](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#std-label-limits-sharding-operations)

Limited Number of 2dsphere index keys [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Limited-Number-of-2dsphere-index-keys "Permalink to this definition")

To generate keys for a 2dsphere index, [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) maps
[GeoJSON shapes](https://www.mongodb.com/docs/manual/reference/geojson/#std-label-geospatial-indexes-store-geojson) to an internal
representation. The resulting internal representation may be a large
array of values.

When [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) generates index keys on a field that holds an
array, [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) generates an index key for each array element.
For compound indexes, [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) calculates the [cartesian product](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-cartesian-product) of the sets of keys that are generated for each field. If both
sets are large, then calculating the cartesian product could cause the
operation to exceed memory limits.

[`indexMaxNumGeneratedKeysPerDocument`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.indexMaxNumGeneratedKeysPerDocument) limits the maximum
number of keys generated for a single document to prevent out of
memory errors. The default is 100000 index keys per document. It is
possible to raise the limit, but if an operation requires more keys
than the [`indexMaxNumGeneratedKeysPerDocument`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.indexMaxNumGeneratedKeysPerDocument) parameter
specifies, the operation will fail.

NaN values returned from Covered Queries by the WiredTiger Storage Engine are always of type double [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-NaN-values-returned-from-Covered-Queries-by-the-WiredTiger-Storage-Engine-are-always-of-type-double "Permalink to this definition")

If the value of a field returned from a query that is [covered\\
by an index](https://www.mongodb.com/docs/manual/core/query-optimization/#std-label-covered-queries) is `NaN`, the type of that `NaN`
value is _always_`double`.

Multikey Index [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Multikey-Index "Permalink to this definition")

[Multikey indexes](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/#std-label-index-type-multikey) cannot cover queries over
array fields.

Geospatial Index [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Geospatial-Index "Permalink to this definition")

Geospatial indexes can't [cover a query.](https://www.mongodb.com/docs/manual/core/query-optimization/#std-label-covered-queries)

Memory Usage in Index Builds [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Memory-Usage-in-Index-Builds "Permalink to this definition")

[`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes) supports building one or more indexes on a collection.
[`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes) uses a combination of memory and temporary files on disk to
build indexes. The default memory limit is 200 megabytes per [`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes)
command, shared equally among all indexes built in that command. For example, if you
build 10 indexes with one [`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes) command, MongoDB allocates each index
20 megabytes for the index build process when using the default memory limit of 200.
When you reach the memory limit, MongoDB creates temporary files in the `_tmp` subdirectory
within [`--dbpath`](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--dbpath) to complete the build.

You can adjust the memory limit with the [`maxIndexBuildMemoryUsageMegabytes`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.maxIndexBuildMemoryUsageMegabytes) parameter.
Setting a higher memory limit may result in faster completion of index
builds. However, setting this limit too high relative to the unused RAM
on your system can result in memory exhaustion and server shutdown.

Each [`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes) command has a limit of [`maxIndexBuildMemoryUsageMegabytes`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.maxIndexBuildMemoryUsageMegabytes).
When using the default [`maxNumActiveUserIndexBuilds`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.maxNumActiveUserIndexBuilds) of 3, the
total memory usage for all concurrent index builds can reach up
to 3 times the value of [`maxIndexBuildMemoryUsageMegabytes`.](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.maxIndexBuildMemoryUsageMegabytes)

The [`maxIndexBuildMemoryUsageMegabytes`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.maxIndexBuildMemoryUsageMegabytes) limit applies to all
index builds initiated by user commands like [`createIndexes`](https://www.mongodb.com/docs/manual/reference/command/createIndexes/#mongodb-dbcommand-dbcmd.createIndexes) or
administrative processes like [initial sync.](https://www.mongodb.com/docs/manual/core/replica-set-sync/#std-label-replica-set-sync)

An [initial sync](https://www.mongodb.com/docs/manual/core/replica-set-sync/#std-label-replica-set-sync) populates only one collection
at a time and has no risk of exceeding the memory limit. However, it is
possible for a user to start index builds on multiple collections in
multiple databases simultaneously.

Collation and Index Types [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Collation-and-Index-Types "Permalink to this definition")

The following index types only support simple binary comparison and
do not support [collation:](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation)

- [Text](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-text/#std-label-index-type-text) indexes

- [2d](https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2d/#std-label-2d-index) indexes


## Tip

To create a `text` or `2d` index on a collection that has a
non-simple collation, you must explicitly specify `{collation:
{locale: "simple"} }` when creating the index.

Hidden Indexes [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Hidden-Indexes "Permalink to this definition")

- You cannot [hide](https://www.mongodb.com/docs/manual/core/index-hidden/#std-label-index-type-hidden) the `_id` index.

- You cannot use [`hint()`](https://www.mongodb.com/docs/manual/reference/method/cursor.hint/#mongodb-method-cursor.hint) on a [hidden index.](https://www.mongodb.com/docs/manual/core/index-hidden/)


## Sorts [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#sorts "Permalink to this heading")

Maximum Number of Sort Keys [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Maximum-Number-of-Sort-Keys "Permalink to this definition")

- You can sort on a maximum of 32 keys.

- Providing a sort pattern with duplicate fields causes an error.


## Data [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#data "Permalink to this heading")

Maximum Number of Documents in a Capped Collection [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Maximum-Number-of-Documents-in-a-Capped-Collection "Permalink to this definition")

If you specify the maximum number of documents in a capped
collection with [`create`](https://www.mongodb.com/docs/manual/reference/command/create/#mongodb-dbcommand-dbcmd.create)'s `max` parameter, the value
must be less than 2 31 documents.

If you do not specify a maximum number of documents when creating a
capped collection, there is no limit on the number of documents.

## Replica Sets [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#replica-sets "Permalink to this heading")

Number of Members of a Replica Set [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Number-of-Members-of-a-Replica-Set "Permalink to this definition")

Replica sets can have up to 50 members.

Number of Voting Members of a Replica Set [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Number-of-Voting-Members-of-a-Replica-Set "Permalink to this definition")

Replica sets can have up to 7 voting members. For replica sets with
more than 7 total members, see [Non-Voting Members.](https://www.mongodb.com/docs/manual/core/replica-set-elections/#std-label-replica-set-non-voting-members)

Maximum Size of Auto-Created Oplog [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Maximum-Size-of-Auto-Created-Oplog "Permalink to this definition")

If you do not explicitly specify an oplog size (i.e. with
[`oplogSizeMB`](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-replication.oplogSizeMB) or [`--oplogSize`](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--oplogSize)) MongoDB will create an oplog that is no
larger than 50 gigabytes. [\[4\]](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#footnote-oplog)

|     |     |
| --- | --- |
| \[ [4](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#ref-oplog-id5)\] | The oplog can grow past its configured size<br>limit to avoid deleting the [`majority commit point`.](https://www.mongodb.com/docs/manual/reference/command/replSetGetStatus/#mongodb-data-replSetGetStatus.optimes.lastCommittedOpTime) |

## Sharded Clusters [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#sharded-clusters "Permalink to this heading")

Sharded clusters have the restrictions and thresholds described here.

### Sharding Operational Restrictions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#sharding-operational-restrictions "Permalink to this heading")

Operations Unavailable in Sharded Environments [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Operations-Unavailable-in-Sharded-Environments "Permalink to this definition")

[`$where`](https://www.mongodb.com/docs/manual/reference/operator/query/where/#mongodb-query-op.-where) does not permit references to the `db` object
from the [`$where`](https://www.mongodb.com/docs/manual/reference/operator/query/where/#mongodb-query-op.-where) function. This is uncommon in
un-sharded collections.

Covered Queries in Sharded Clusters [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Covered-Queries-in-Sharded-Clusters "Permalink to this definition")

When run on [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#std-program-mongos), indexes can only [cover](https://www.mongodb.com/docs/manual/core/query-optimization/#std-label-covered-queries) queries on
[sharded](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard) collections if the index contains
the shard key.

Single Document Modification Operations in Sharded Collections [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Single-Document-Modification-Operations-in-Sharded-Collections "Permalink to this definition")

To use [`update`](https://www.mongodb.com/docs/manual/reference/command/update/#mongodb-dbcommand-dbcmd.update) and [`remove()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.remove/#mongodb-method-db.collection.remove) operations for a sharded
collection that specify the `justOne` or `multi: false` option:

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the [shard key](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard-key) or the `_id` field in the query
specification.


Unique Indexes in Sharded Collections [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Unique-Indexes-in-Sharded-Collections "Permalink to this definition")

MongoDB does not support unique indexes across shards, except when
the unique index contains the full shard key as a prefix of the
index. In these situations MongoDB will enforce uniqueness across
the full key, not a single field.

## Tip

### **See:**

[Unique Constraints on Arbitrary Fields](https://www.mongodb.com/docs/manual/tutorial/unique-constraints-on-arbitrary-fields/#std-label-shard-key-arbitrary-uniqueness) for an alternate approach.

Maximum Number of Documents Per Range to Migrate [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Maximum-Number-of-Documents-Per-Range-to-Migrate "Permalink to this definition")

By default, MongoDB cannot move a range if the number of documents in
the range is greater than 2 times the result of dividing the
configured [range size](https://www.mongodb.com/docs/manual/core/sharding-data-partitioning/#std-label-sharding-range-size) by the average
document size. If MongoDB can move a sub-range of a chunk and reduce the
size to less than that, the balancer does so by migrating a range.
[`db.collection.stats()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.stats/#mongodb-method-db.collection.stats) includes the `avgObjSize` field,
which represents the average document size in the collection.

For chunks that are [too large to migrate:](https://www.mongodb.com/docs/manual/core/sharding-balancer-administration/#std-label-migration-chunk-size-limit)

- The balancer setting `attemptToBalanceJumboChunks` allows the
balancer to migrate chunks too large to move as long as the chunks
are not labeled [jumbo](https://www.mongodb.com/docs/manual/core/sharding-data-partitioning/#std-label-jumbo-chunk). See
[Balance Ranges that Exceed Size Limit](https://www.mongodb.com/docs/manual/tutorial/manage-sharded-cluster-balancer/#std-label-balance-chunks-that-exceed-size-limit) for details.

When issuing [`moveRange`](https://www.mongodb.com/docs/manual/reference/command/moveRange/#mongodb-dbcommand-dbcmd.moveRange) and [`moveChunk`](https://www.mongodb.com/docs/manual/reference/command/moveChunk/#mongodb-dbcommand-dbcmd.moveChunk)
commands, it's possible to specify the [forceJumbo](https://www.mongodb.com/docs/manual/reference/command/moveRange/#std-label-moverange-forceJumbo) option to allow for the migration of ranges
that are too large to move. The ranges may or may not be labeled
[jumbo.](https://www.mongodb.com/docs/manual/core/sharding-data-partitioning/#std-label-jumbo-chunk)


### Shard Key Limitations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#shard-key-limitations "Permalink to this heading")

Shard Key Index Type [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Shard-Key-Index-Type "Permalink to this definition")

A [shard key](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard-key) index can be an ascending index on the shard
key, a compound index that starts with the shard key and specifies
ascending order for the shard key, or a [hashed index.](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-hashed/#std-label-index-type-hashed)

A [shard key](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard-key) index _cannot_ be:

- A descending index on the shard key

- A [partial index](https://www.mongodb.com/docs/manual/core/index-partial/#std-label-index-type-partial)

- Any of the following index types:

  - [Geospatial](https://www.mongodb.com/docs/manual/geospatial-queries/#std-label-index-feature-geospatial)

  - [Multikey](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/#std-label-index-type-multikey)

  - [Text](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-text/#std-label-index-type-text)

  - [Wildcard](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-wildcard/#std-label-wildcard-index-core)

Shard Key Selection [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Shard-Key-Selection "Permalink to this definition")

Your options for changing a shard key depend on the version of
MongoDB that you are running:

- Starting in MongoDB 5.0, you can [reshard a collection](https://www.mongodb.com/docs/manual/core/sharding-reshard-a-collection/#std-label-sharding-resharding) by changing a document's shard key.

- You can [refine a shard key](https://www.mongodb.com/docs/manual/core/sharding-refine-a-shard-key/#std-label-shard-key-refine) by adding a suffix
field or fields to the existing shard key.


Monotonically Increasing Shard Keys Can Limit Insert Throughput [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Monotonically-Increasing-Shard-Keys-Can-Limit-Insert-Throughput "Permalink to this definition")

For clusters with high insert volumes, a shard key with
monotonically increasing and decreasing keys can affect insert
throughput. If your shard key is the `_id` field, be aware that
the default values of the `_id` fields are [ObjectIds](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-ObjectId) which have generally increasing values.

When inserting documents with monotonically increasing shard keys, all inserts
belong to the same [chunk](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-chunk) on a single [shard](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard). The system
eventually divides the chunk range that receives all write operations and
migrates its contents to distribute data more evenly. However, at any moment
the cluster directs insert operations only to a single shard, which creates an
insert throughput bottleneck.

If the operations on the cluster are predominately read operations
and updates, this limitation may not affect the cluster.

To avoid this constraint, use a [hashed shard key](https://www.mongodb.com/docs/manual/core/hashed-sharding/#std-label-sharding-hashed-sharding) or select a field that does not
increase or decrease monotonically.

[Hashed shard keys](https://www.mongodb.com/docs/manual/core/hashed-sharding/#std-label-sharding-hashed-sharding) and [hashed\\
indexes](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-hashed/#std-label-index-type-hashed) store hashes of keys with ascending values.

## Operations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#operations "Permalink to this heading")

Sort Operations [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Sort-Operations "Permalink to this definition")

If MongoDB cannot use an index or indexes to obtain the sort order,
MongoDB must perform an in-memory sort operation on the data.

For more information on sorts and index use, see
[Sort and Index Use.](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/#std-label-sort-index-use)

Aggregation Pipeline Stages [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Aggregation-Pipeline-Stages "Permalink to this definition")

MongoDB limits the number of [aggregation pipeline stages](https://www.mongodb.com/docs/manual/reference/mql/aggregation-stages/#std-label-aggregation-pipeline-operator-reference) allowed in a single
pipeline to 1000.

If an aggregation pipeline exceeds the stage limit before or after being parsed,
you receive an error.

Aggregation Pipeline Memory [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Aggregation-Pipeline-Memory "Permalink to this definition")

Starting in MongoDB 6.0, the [`allowDiskUseByDefault`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.allowDiskUseByDefault)
parameter controls whether pipeline stages that require more than 100
megabytes of memory to execute write temporary files to disk by
default.

- If [`allowDiskUseByDefault`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.allowDiskUseByDefault) is set to `true`, pipeline
stages that require more than 100 megabytes of memory to execute
write temporary files to disk by default. You can disable writing
temporary files to disk for specific `find` or `aggregate`
commands using the `{ allowDiskUse: false }` option.

- If [`allowDiskUseByDefault`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.allowDiskUseByDefault) is set to `false`, pipeline
stages that require more than 100 megabytes of memory to execute
raise an error by default. You can enable writing temporary files to
disk for specific `find` or `aggregate` using
the `{ allowDiskUse: true }` option.


The [`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search) aggregation stage is not restricted to
100 megabytes of RAM because it runs in a separate process.

Examples of stages that can write temporary files to disk when
[allowDiskUse](https://www.mongodb.com/docs/manual/reference/command/aggregate/#std-label-aggregate-cmd-allowDiskUse) is `true` are:

- [`$bucket`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucket/#mongodb-pipeline-pipe.-bucket)

- [`$bucketAuto`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucketAuto/#mongodb-pipeline-pipe.-bucketAuto)

- [`$group`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group)

- [`$setWindowFields`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields)

- [`$sort`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) when the sort operation is not supported by an
index

- [`$sortByCount`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sortByCount/#mongodb-pipeline-pipe.-sortByCount)


## Note

Pipeline stages operate on streams of documents with each pipeline
stage taking in documents, processing them, and then outputting the
resulting documents.

Some stages can't output any documents until they have processed all
incoming documents. These pipeline stages must keep their stage
output in RAM until all incoming documents are processed. As a
result, these pipeline stages may require more space than the 100 MB
limit.

If the results of one of your [`$sort`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) pipeline stages exceed
the limit, consider [adding a $limit stage.](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/#std-label-sort-limit-sequence)

The [profiler log messages](https://www.mongodb.com/docs/manual/tutorial/manage-the-database-profiler/#std-label-database-profiler) and [diagnostic log\\
messages](https://www.mongodb.com/docs/manual/reference/log-messages/#std-label-log-messages-ref) includes a `usedDisk`
indicator if any aggregation stage wrote data to temporary files due
to [memory restrictions.](https://www.mongodb.com/docs/manual/core/aggregation-pipeline-limits/#std-label-agg-memory-restrictions)

Aggregation and Read Concern [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Aggregation-and-Read-Concern "Permalink to this definition")

- The [`$out`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/#mongodb-pipeline-pipe.-out) stage cannot be used in conjunction with read concern
[`"linearizable"`](https://www.mongodb.com/docs/manual/reference/read-concern-linearizable/#mongodb-readconcern-readconcern.-linearizable-). If you specify [`"linearizable"`](https://www.mongodb.com/docs/manual/reference/read-concern-linearizable/#mongodb-readconcern-readconcern.-linearizable-)
read concern for [`db.collection.aggregate()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.aggregate/#mongodb-method-db.collection.aggregate), you cannot include the
[`$out`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/#mongodb-pipeline-pipe.-out) stage in the pipeline.

- The [`$merge`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/#mongodb-pipeline-pipe.-merge) stage cannot be used in conjunction with read
concern [`"linearizable"`](https://www.mongodb.com/docs/manual/reference/read-concern-linearizable/#mongodb-readconcern-readconcern.-linearizable-). That is, if you specify
[`"linearizable"`](https://www.mongodb.com/docs/manual/reference/read-concern-linearizable/#mongodb-readconcern-readconcern.-linearizable-) read concern for
[`db.collection.aggregate()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.aggregate/#mongodb-method-db.collection.aggregate), you cannot include the
[`$merge`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/#mongodb-pipeline-pipe.-merge) stage in the pipeline.


2d Geospatial queries cannot use the $or operator [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-2d-Geospatial-queries-cannot-use-the--or-operator "Permalink to this definition")

## Tip

### **See:**

- [`$or`](https://www.mongodb.com/docs/manual/reference/operator/query/or/#mongodb-query-op.-or)

- [2d Index Internals](https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2d/internals/#std-label-2d-index-internals)


Geospatial Queries [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Geospatial-Queries "Permalink to this definition")

Using a `2d` index for queries on spherical data
can return incorrect results or an error. For example,
`2d` indexes don't support spherical queries that wrap
around the poles.

Geospatial Coordinates [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Geospatial-Coordinates "Permalink to this definition")

- Valid longitude values are between `-180` and `180`, both
inclusive.

- Valid latitude values are between `-90` and `90`, both
inclusive.


Area of GeoJSON Polygons [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Area-of-GeoJSON-Polygons "Permalink to this definition")

For [`$geoIntersects`](https://www.mongodb.com/docs/manual/reference/operator/query/geoIntersects/#mongodb-query-op.-geoIntersects) or [`$geoWithin`](https://www.mongodb.com/docs/manual/reference/operator/query/geoWithin/#mongodb-query-op.-geoWithin), if you specify a single-ringed polygon that
has an area greater than a single hemisphere, include the custom MongoDB
coordinate reference system in the [`$geometry`](https://www.mongodb.com/docs/manual/reference/operator/query/geometry/#mongodb-query-op.-geometry)
expression. Otherwise, [`$geoIntersects`](https://www.mongodb.com/docs/manual/reference/operator/query/geoIntersects/#mongodb-query-op.-geoIntersects) or [`$geoWithin`](https://www.mongodb.com/docs/manual/reference/operator/query/geoWithin/#mongodb-query-op.-geoWithin) queries for the
complementary geometry. For all other GeoJSON polygons with areas
greater than a hemisphere, [`$geoIntersects`](https://www.mongodb.com/docs/manual/reference/operator/query/geoIntersects/#mongodb-query-op.-geoIntersects) or [`$geoWithin`](https://www.mongodb.com/docs/manual/reference/operator/query/geoWithin/#mongodb-query-op.-geoWithin) queries for the
complementary geometry.

Multi-document Transactions [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Multi-document-Transactions "Permalink to this definition")

For [multi-document transactions:](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions)

- You can create collections and indexes in transactions. For
details, see [Create Collections and Indexes in a Transaction](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-create-collections-indexes)

- The collections used in a transaction can be in different
databases.



## Note





You cannot create new collections in cross-shard write transactions.
For example, if you write to an existing collection in one shard and
implicitly create a collection in a different shard, MongoDB cannot
perform both operations in the same transaction.

- You cannot write to [capped](https://www.mongodb.com/docs/manual/core/capped-collections/#std-label-manual-capped-collection)
collections.

- You cannot use read concern [`"snapshot"`](https://www.mongodb.com/docs/manual/reference/read-concern-snapshot/#mongodb-readconcern-readconcern.-snapshot-) when reading
from a [capped](https://www.mongodb.com/docs/manual/core/capped-collections/#std-label-manual-capped-collection) collection.
(Starting in MongoDB 5.0)

- You cannot read/write to collections in the `config`, `admin`,
or `local` databases.

- You cannot write to `system.*` collections.

- You cannot return the supported operation's query plan using
`explain` or similar commands.


- For cursors created outside of a transaction, you cannot call
[`getMore`](https://www.mongodb.com/docs/manual/reference/command/getMore/#mongodb-dbcommand-dbcmd.getMore) inside the transaction.

- For cursors created in a transaction, you cannot call
[`getMore`](https://www.mongodb.com/docs/manual/reference/command/getMore/#mongodb-dbcommand-dbcmd.getMore) outside the transaction.


- You cannot specify the [`killCursors`](https://www.mongodb.com/docs/manual/reference/command/killCursors/#mongodb-dbcommand-dbcmd.killCursors) command as
the first operation in a [transaction.](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions)

Additionally, if you run the `killCursors` command within a
transaction, the server immediately stops the specified
cursors. It does **not** wait for the transaction to commit.


The following operations are not allowed in transactions:

- Creating new collections in cross-shard write transactions. For
example, if you write to an existing collection in one shard and
implicitly create a collection in a different shard, MongoDB cannot
perform both operations in the same transaction.

- [Explicit creation of collections](https://www.mongodb.com/docs/manual/core/transactions-operations/#std-label-transactions-operations-ddl-explicit), e.g.
[`db.createCollection()`](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/#mongodb-method-db.createCollection) method, and indexes, e.g.
[`db.collection.createIndexes()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndexes/#mongodb-method-db.collection.createIndexes) and
[`db.collection.createIndex()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/#mongodb-method-db.collection.createIndex) methods, when using a read
concern level other than [`"local"`.](https://www.mongodb.com/docs/manual/reference/read-concern-local/#mongodb-readconcern-readconcern.-local-)

- The [`listCollections`](https://www.mongodb.com/docs/manual/reference/command/listCollections/#mongodb-dbcommand-dbcmd.listCollections) and [`listIndexes`](https://www.mongodb.com/docs/manual/reference/command/listIndexes/#mongodb-dbcommand-dbcmd.listIndexes)
commands and their helper methods.

- Other non-CRUD and non-informational operations, such as
[`createUser`](https://www.mongodb.com/docs/manual/reference/command/createUser/#mongodb-dbcommand-dbcmd.createUser), [`getParameter`](https://www.mongodb.com/docs/manual/reference/command/getParameter/#mongodb-dbcommand-dbcmd.getParameter),
[`count`](https://www.mongodb.com/docs/manual/reference/command/count/#mongodb-dbcommand-dbcmd.count), etc. and their helpers.

- Parallel operations. To update multiple namespaces concurrently, consider
using the [`bulkWrite`](https://www.mongodb.com/docs/manual/reference/command/bulkWrite/#mongodb-dbcommand-dbcmd.bulkWrite) command instead.


Transactions have a lifetime limit as specified by
[`transactionLifetimeLimitSeconds`](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.transactionLifetimeLimitSeconds). The default is 60 seconds.

Write Command Batch Limit Size [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Write-Command-Batch-Limit-Size "Permalink to this definition")

While MongoDB doesn't have a limit on the number of batch operations it can
perform, it allows a maximum of 100,000 [writes](https://www.mongodb.com/docs/manual/reference/mql/crud-commands/#std-label-query-and-write-commands) in a single batch operation. A single batch
refers to a single request to the server. If the number of writes in a batch
operation exceeds 100,000, the client driver divides the batch into
smaller groups with counts less than or equal to 100,000.

Views [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Views "Permalink to this definition")

A view definition `pipeline` cannot include the [`$out`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/#mongodb-pipeline-pipe.-out) or
the [`$merge`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/#mongodb-pipeline-pipe.-merge) stage. This restriction also applies to
embedded pipelines, such as pipelines used in [`$lookup`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) or
[`$facet`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/#mongodb-pipeline-pipe.-facet) stages.

Views have the following operation restrictions:

- Views are read-only.

- You cannot rename [views.](https://www.mongodb.com/docs/manual/core/views/#std-label-views-landing-page)

- [`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) operations on views do not support
the following [find command projection operators:](https://www.mongodb.com/docs/manual/reference/mql/projection/#std-label-projection-operators-ref)

  - [`$`](https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#mongodb-projection-proj.-)

  - [`$elemMatch`](https://www.mongodb.com/docs/manual/reference/operator/projection/elemMatch/#mongodb-projection-proj.-elemMatch)

  - [`$slice`](https://www.mongodb.com/docs/manual/reference/operator/projection/slice/#mongodb-projection-proj.-slice)

  - [`$meta`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/meta/#mongodb-expression-exp.-meta)
- [Views](https://www.mongodb.com/docs/manual/core/views/#std-label-views-landing-page) do not support `$text`.

- [Views](https://www.mongodb.com/docs/manual/core/views/#std-label-views-landing-page) do not support map-reduce operations.


Projection Restrictions [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Projection-Restrictions "Permalink to this definition")`$`-Prefixed Field Path RestrictionThe [`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) and [`findAndModify()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify) projection cannot project a field that starts with
`$` with the exception of the [DBRef fields.](https://www.mongodb.com/docs/manual/reference/database-references/#std-label-dbref-explanation) For example, the following operation is invalid:

```
db.inventory.find( {}, { "$instock.warehouse": 0, "$item": 0, "detail.$price": 1 } )
```

`$` Positional Operator Placement RestrictionThe [`$`](https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#mongodb-projection-proj.-) projection operator can only appear at the end of the
field path, for example `"field.$"` or `"fieldA.fieldB.$"`.For example, the following operation is invalid:

```
db.inventory.find( { }, { "instock.$.qty": 1 } )
```

To resolve, remove the component of the field path that follows the
[`$`](https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#mongodb-projection-proj.-) projection operator.Empty Field Name Projection Restriction[`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) and [`findAndModify()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify) projection cannot include a projection of an empty field
name.For example, the following operation is invalid:

```
db.inventory.find( { }, { "": 0 } )
```

In previous versions, MongoDB treats the inclusion/exclusion of the
empty field as it would the projection of non-existing fields.Path Collision: Embedded Documents and Its FieldsYou cannot project an embedded document with any of the embedded
document's fields.For example, consider a collection `inventory` with documents that
contain a `size` field:

```
{ ..., size: { h: 10, w: 15.25, uom: "cm" }, ... }
```

The following operation fails with a `Path collision` error because it
attempts to project both `size` document and the `size.uom` field:

```
db.inventory.find( {}, { size: 1, "size.uom": 1 } )
```

In previous versions, lattermost projection between the embedded
documents and its fields determines the projection:

- If the projection of the embedded document comes after any and all
projections of its fields, MongoDB projects the embedded document.
For example, the projection document `{ "size.uom": 1, size: 1 }`
produces the same result as the projection document `{ size: 1 }`.

- If the projection of the embedded document comes before the
projection any of its fields, MongoDB projects the specified field or
fields. For example, the projection document `{ "size.uom": 1, size:
1, "size.h": 1 }` produces the same result as the projection
document `{ "size.uom": 1, "size.h": 1 }`.


Path Collision: `$slice` of an Array and Embedded Fields[`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) and [`findAndModify()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify) projection cannot contain both a [`$slice`](https://www.mongodb.com/docs/manual/reference/operator/projection/slice/#mongodb-projection-proj.-slice) of an
array and a field embedded in the array.For example, consider a collection `inventory` that contains an array
field `instock`:

```
{ ..., instock: [ { warehouse: "A", qty: 35 }, { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ], ... }
```

The following operation fails with a `Path
collision` error:

```
db.inventory.find( {}, { "instock": { $slice: 1 }, "instock.warehouse": 0 } )
```

In previous versions, the projection applies both projections and
returns the first element (`$slice: 1`) in the `instock` array
but suppresses the `warehouse` field in the projected element.
Starting in MongoDB 4.4, to achieve the same result, use the
[`db.collection.aggregate()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.aggregate/#mongodb-method-db.collection.aggregate) method with two separate
[`$project`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/#mongodb-pipeline-pipe.-project) stages.`$` Positional Operator and `$slice` Restriction[`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) and [`findAndModify()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify) projection cannot include [`$slice`](https://www.mongodb.com/docs/manual/reference/operator/projection/slice/#mongodb-projection-proj.-slice) projection
expression as part of a [`$`](https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#mongodb-projection-proj.-) projection expression.For example, the following operation is invalid:

```
db.inventory.find( { "instock.qty": { $gt: 25 } }, { "instock.$": { $slice: 1 } } )
```

In previous versions, MongoDB returns the first element
(`instock.$`) in the `instock` array that matches the query
condition; i.e. the positional projection `"instock.$"` takes
precedence and the `$slice:1` is a no-op. The `"instock.$": {
$slice: 1 }` does not exclude any other document field.

## Sessions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general\#sessions "Permalink to this heading")

Sessions and $external Username Limit [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Sessions-and--external-Username-Limit "Permalink to this definition")

To use [Client Sessions and Causal Consistency Guarantees](https://www.mongodb.com/docs/manual/core/read-isolation-consistency-recency/#std-label-sessions) with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

Session Idle Timeout [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-limit-Session-Idle-Timeout "Permalink to this definition")

Sessions that receive no read or write operations for 30 minutes _or_
that are not refreshed using [`refreshSessions`](https://www.mongodb.com/docs/manual/reference/command/refreshSessions/#mongodb-dbcommand-dbcmd.refreshSessions) within this
threshold are marked as expired and can be closed by the MongoDB
server at any time. Closing a session kills any in-progress
operations and open cursors associated with the session. This
includes cursors configured with [`noCursorTimeout()`](https://www.mongodb.com/docs/manual/reference/method/cursor.noCursorTimeout/#mongodb-method-cursor.noCursorTimeout) or
a [`maxTimeMS()`](https://www.mongodb.com/docs/manual/reference/method/cursor.maxTimeMS/#mongodb-method-cursor.maxTimeMS) greater than 30 minutes.

Consider an application that issues a [`db.collection.find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find).
The server returns a cursor along with a batch of documents defined
by the [`cursor.batchSize()`](https://www.mongodb.com/docs/manual/reference/method/cursor.batchSize/#mongodb-method-cursor.batchSize) of the
[`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find). The session refreshes each time the
application requests a new batch of documents from the server.
However, if the application takes longer than 30 minutes to process
the current batch of documents, the session is marked as expired and
closed. When the application requests the next batch of documents,
the server returns an error as the cursor was killed when the session
was closed.

For operations that return a cursor, if the cursor may be idle for
longer than 30 minutes, issue the operation within an explicit
session using [`Mongo.startSession()`](https://www.mongodb.com/docs/manual/reference/method/Mongo.startSession/#mongodb-method-Mongo.startSession) and periodically
refresh the session using the [`refreshSessions`](https://www.mongodb.com/docs/manual/reference/command/refreshSessions/#mongodb-dbcommand-dbcmd.refreshSessions) command.
For example:

```
var session = db.getMongo().startSession()
var sessionId = session
sessionId  // show the sessionId

var cursor = session.getDatabase("examples").getCollection("data").find().noCursorTimeout()
var refreshTimestamp = new Date() // take note of time at operation start

while (cursor.hasNext()) {

  // Check if more than 5 minutes have passed since the last refresh
  if ( (new Date()-refreshTimestamp)/1000 > 300 ) {
    print("refreshing session")
    db.adminCommand({"refreshSessions" : [sessionId]})
    refreshTimestamp = new Date()
  }

  // process cursor normally

}
```

In the example operation, the [`db.collection.find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) method
is associated with an explicit session. The cursor is configured with
[`noCursorTimeout()`](https://www.mongodb.com/docs/manual/reference/method/cursor.noCursorTimeout/#mongodb-method-cursor.noCursorTimeout) to prevent the server from
closing the cursor if idle. The `while` loop includes a block that
uses [`refreshSessions`](https://www.mongodb.com/docs/manual/reference/command/refreshSessions/#mongodb-dbcommand-dbcmd.refreshSessions) to refresh the session every 5
minutes. Since the session will never exceed the 30 minute idle
timeout, the cursor can remain open indefinitely.

For MongoDB drivers, defer to the [driver documentation](https://www.mongodb.com/docs/drivers/) for instructions and syntax for creating sessions.

[Back\\
\\
Log Messages](https://www.mongodb.com/docs/manual/reference/log-messages/ "Previous Section")

[Next\\
\\
MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/ "Next Section")

Rate this page

On this page

- [MongoDB Atlas Limitations](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-atlas-limitations)
- [Collection and Database Size Limits](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#collection-and-database-size-limits)
- [BSON Documents](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#bson-documents)
- [Naming Restrictions](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#naming-restrictions)
- [Naming Warnings](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#naming-warnings)
- [Namespaces](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#namespaces)
- [Indexes](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#indexes)
- [Sorts](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sorts)
- [Data](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#data)
- [Replica Sets](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#replica-sets)
- [Sharded Clusters](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sharded-clusters)
- [Operations](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#operations)
- [Sessions](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sessions)

On this page

- [MongoDB Atlas Limitations](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#mongodb-atlas-limitations)
- [Collection and Database Size Limits](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#collection-and-database-size-limits)
- [BSON Documents](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#bson-documents)
- [Naming Restrictions](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#naming-restrictions)
- [Naming Warnings](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#naming-warnings)
- [Namespaces](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#namespaces)
- [Indexes](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#indexes)
- [Sorts](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sorts)
- [Data](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#data)
- [Replica Sets](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#replica-sets)
- [Sharded Clusters](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sharded-clusters)
- [Operations](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#operations)
- [Sessions](https://www.mongodb.com/docs/manual/reference/limits/?atlas-provider=aws&atlas-class=general#sessions)

Navigated to MongoDB Limits and Thresholds

0 more notification

0 more notification