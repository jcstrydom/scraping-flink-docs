Docs Menu

Ask MongoDB AI

[Docs Home](https://www.mongodb.com/docs/)

/

/

[mongosh Methods](https://www.mongodb.com/docs/manual/reference/method)

[Docs Home](https://www.mongodb.com/docs/)

/

[Development](https://www.mongodb.com/docs/development)

/

[Reference](https://www.mongodb.com/docs/manual/reference)

/

[mongosh Methods](https://www.mongodb.com/docs/manual/reference/method)

[Docs Home](https://www.mongodb.com/docs/)

/

[Development](https://www.mongodb.com/docs/development)

/

[Reference](https://www.mongodb.com/docs/manual/reference)

/

[mongosh Methods](https://www.mongodb.com/docs/manual/reference/method)

# db.collection.updateOne() (mongosh method) [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#db.collection.updateone----mongosh-method- "Permalink to this heading")

Copy page

MongoDB with drivers

This page documents a [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh) method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

[C#](https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/crud/write-operations/modify/#update-one-document) [Java Sync](https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/crud/write-operations/modify/#update) [Node.js](https://www.mongodb.com/docs/drivers/node/current/fundamentals/crud/write-operations/modify/#update-documents) [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write/update/#update-one-document) [C](https://mongoc.org/libmongoc/current/mongoc_collection_update_one.html) [C++](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/write/update/#update-one-document) [Go](https://www.mongodb.com/docs/drivers/go/current/fundamentals/crud/write-operations/modify/#update) [Java RS](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/write/write-update-documents/) [Kotlin Coroutine](https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/crud/write-operations/modify/#update) [Kotlin Sync](https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/write/update/#update-one-document) [PHP](https://www.mongodb.com/docs/php-library/current/write/update/#update-one-document) [Mongoid](https://www.mongodb.com/docs/mongoid/master/api/Mongoid/Persistable/Updatable.html#update_attribute-instance_method) [Rust](https://www.mongodb.com/docs/drivers/rust/current/fundamentals/crud/write-operations/change/#update-documents) [Scala](https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/write-ops/#update-a-single-document)

Show all

## Definition [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#definition "Permalink to this heading")

`db.collection.updateOne(filter, update, options)` [Permalink to this definition](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne "Permalink to this definition")

Updates a single document within the collection based on the filter.

## Compatibility [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#compatibility "Permalink to this heading")

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
managed service for MongoDB deployments in the cloud


## Note

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see
[Unsupported Commands.](https://www.mongodb.com/docs/atlas/unsupported-commands/)

- [MongoDB Enterprise](https://www.mongodb.com/docs/manual/administration/install-enterprise/#std-label-install-mdb-enterprise): The
subscription-based, self-managed version of MongoDB

- [MongoDB Community](https://www.mongodb.com/docs/manual/administration/install-community/#std-label-install-mdb-community-edition): The
source-available, free-to-use, and self-managed version of MongoDB


## Syntax [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#syntax "Permalink to this heading")

The [`updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method has the following syntax:

```
db.collection.updateOne(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
     writeConcern: <document>,
     collation: <document>,
     arrayFilters: [ <filterdocument1>, ... ],
     hint:  <document|string>,
     let: <document>,
     sort: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>
   }
)
```

### Parameters [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#parameters "Permalink to this heading")

The [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method takes the following
parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| [filter](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter) | document | The selection criteria for the update. The same [query\<br>selectors](https://www.mongodb.com/docs/manual/reference/mql/query-predicates/#std-label-query-selectors) as in the [`find()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) method are available.<br>Specify an empty document `{ }` to update the first document returned in<br>the collection. |
| [update](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-update) | document or pipeline | The modifications to apply. Can be one of the following:

| [Update document](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-method-update-document) | Contains only [update operator expressions.](https://www.mongodb.com/docs/manual/reference/mql/update/#std-label-update-operators)<br>For more information, see<br>[Update with an Update Operator Expressions Document](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-behavior-update-expressions) |
| [Aggregation pipeline](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-method-agg-pipeline) | Contains only the following aggregation stages:<br>- [`$addFields`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields) and its alias [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set)<br>  <br>- [`$project`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/#mongodb-pipeline-pipe.-project) and its alias [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset)<br>  <br>- [`$replaceRoot`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/#mongodb-pipeline-pipe.-replaceRoot) and its alias [`$replaceWith`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/#mongodb-pipeline-pipe.-replaceWith)<br>  <br>For more information, see<br>[Update with an Aggregation Pipeline.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-behavior-aggregation-pipeline) |

To update with a replacement document, see
[`db.collection.replaceOne()`.](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/#mongodb-method-db.collection.replaceOne) |
| `upsert` | boolean | Optional. When `true`, [`updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) either:<br>- Creates a new document if no documents match the `filter`.<br>For more details see [upsert behavior.](https://www.mongodb.com/docs/manual/reference/method/db.collection.update/#std-label-upsert-behavior)<br>  <br>- Updates a single document that matches the `filter`.<br>  <br>To avoid multiple [upserts](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-upsert), ensure that the<br>`filter` field(s) are [uniquely indexed.](https://www.mongodb.com/docs/manual/core/index-unique/#std-label-index-type-unique)<br>Defaults to `false`, which does _not_ insert a new document when no<br>match is found. |
| `writeConcern` | document | Optional. A document expressing the [write concern](https://www.mongodb.com/docs/manual/reference/write-concern/). Omit to use the default write concern.<br>Do not explicitly set the write concern for the operation if run in<br>a transaction. To use write concern with transactions, see<br>[Transactions and Write Concern.](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-write-concern) |
| `collation` | document | Optional.

Specifies the [collation](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation) to use for the operation.

[Collation](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation) allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

The collation option has the following syntax:

```
collation: {
   locale: <string>,
   caseLevel: <boolean>,
   caseFirst: <string>,
   strength: <int>,
   numericOrdering: <boolean>,
   alternate: <string>,
   maxVariable: <string>,
   backwards: <boolean>
}
```

When specifying collation, the `locale` field is mandatory; all
other collation fields are optional. For descriptions of the fields,
see [Collation Document.](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation-document-fields)

If the collation is unspecified but the collection has a
default collation (see [`db.createCollection()`](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/#mongodb-method-db.createCollection)), the
operation uses the collation specified for the collection.

If no collation is specified for the collection or for the
operations, MongoDB uses the simple binary comparison used in prior
versions for string comparisons.

You cannot specify multiple collations for an operation. For
example, you cannot specify different collations per field, or if
performing a find with a sort, you cannot use one collation for the
find and another for the sort. |
| `arrayFilters` | array | Optional. An array of filter documents that determine which array elements to
modify for an update operation on an array field.

In the update document, use the [`$[<identifier>]`](https://www.mongodb.com/docs/manual/reference/operator/update/positional-filtered/#mongodb-update-up.---identifier--) filtered
positional operator to define an identifier, which you then reference
in the array filter documents. You cannot have an array filter
document for an identifier if the identifier is not included in the
update document.

The `<identifier>` must begin with a lowercase letter and
contain only alphanumeric characters.

You can include the same identifier multiple times in the update
document; however, for each distinct identifier (`$[identifier]`)
in the update document, you must specify **exactly one**
corresponding array filter document. That is, you cannot specify
multiple array filter documents for the same identifier. For
example, if the update statement includes the identifier `x`
(possibly multiple times), you cannot specify the following for
`arrayFilters` that includes 2 separate filter documents for `x`:

```
// INVALID

[\
  { "x.a": { $gt: 85 } },\
  { "x.b": { $gt: 80 } }\
]
```

However, you can specify compound conditions on the same identifier
in a single filter document, such as in the following examples:

```
// Example 1
[\
  { $or: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }\
]
// Example 2
[\
  { $and: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }\
]
// Example 3
[\
  { "x.a": { $gt: 85 }, "x.b": { $gt: 80 } }\
]
```

For examples, see [Specify `arrayFilters` for an Array Update Operations.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-arrayFilters) |
| [hint](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-hint) | Document or string | Optional. A document or string that specifies the [index](https://www.mongodb.com/docs/manual/indexes/#std-label-indexes) to use to support the [query predicate.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter)<br>The option can take an index specification document or the index<br>name string.<br>If you specify an index that does not exist, the operation<br>errors.<br>For an example, see [Specify `hint` for Update Operations.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-ex-update-one-hint) |
| `let` | Document | Optional.

Specifies a document with a list of variables. This allows you to
improve command readability by separating the variables from the query
text.

The document syntax is:

```
{
  <variable_name_1>: <expression_1>,
  ...,
  <variable_name_n>: <expression_n>
}
```

The variable is set to the value returned by the expression, and cannot
be changed afterwards.

To access the value of a variable in the command, use the double
dollar sign prefix (`$$`) together with your variable name in the form
`$$<variable_name>`. For example: `$$targetTotal`.

To use a variable to filter results, you must access the variable
within the [`$expr`](https://www.mongodb.com/docs/manual/reference/operator/query/expr/#mongodb-query-op.-expr) operator.

For a complete example using `let` and variables,
see [Update with let Variables.](https://www.mongodb.com/docs/manual/tutorial/update-documents-with-aggregation-pipeline/#std-label-updateMany-let-example) |
| `sort` | Document | Optional.<br>Determines which document the operation updates if the query<br>selects multiple documents. `updateOne` updates<br>the first document in the sort order specified by this argument.<br>If the sort argument is not a document, the operation errors.<br>MongoDB does not store documents in a collection in a particular order.<br>When sorting on a field which contains duplicate values, documents<br>containing those values may be returned in any order.<br>The `$sort` operation is not a "stable sort," which means that documents<br>with equivalent sort keys are not guaranteed to remain in the same relative<br>order in the output as they were in the input.<br>If the field specified in the sort criteria does not exist in two documents, then<br>the value on which they are sorted is the same. The two documents may be returned<br>in any order.<br>If consistent sort order is desired, include at least one field in your<br>sort that contains unique values. The easiest way to guarantee this is<br>to include the `_id` field in your sort query.<br>See [Sort Consistency](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/#std-label-sort-cursor-consistent-sorting) for more information.<br>_New in version 8.0_. |
| [maxTimeMS](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-maxTimeMS) | integer | Optional. Specifies the time limit in milliseconds for the<br>update operation to run before timing out. |
| [bypassDocumentValidation](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-bypassDocumentValidation) | boolean | Optional. Enables [`insert`](https://www.mongodb.com/docs/manual/reference/command/insert/#mongodb-dbcommand-dbcmd.insert) to bypass schema validation<br>during the operation. This lets you insert documents that do not<br>meet the validation requirements. |

### Returns [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#returns "Permalink to this heading")

The method returns a document that contains:

- `matchedCount` containing the number of matched documents

- `modifiedCount` containing the number of modified documents

- `upsertedId` containing the `_id` for the upserted document

- `upsertedCount` containing the number of upserted documents

- A boolean `acknowledged` as `true` if the operation ran with
[write concern](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-write-concern) or `false` if write concern was disabled


## Access Control [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#access-control "Permalink to this heading")

On deployments running with [`authorization`](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-security.authorization), the
user must have access that includes the following privileges:

- [`update`](https://www.mongodb.com/docs/manual/reference/privilege-actions/#mongodb-authaction-update) action on the specified collection(s).

- [`find`](https://www.mongodb.com/docs/manual/reference/privilege-actions/#mongodb-authaction-find) action on the specified collection(s).

- [`insert`](https://www.mongodb.com/docs/manual/reference/privilege-actions/#mongodb-authaction-insert) action on the specified collection(s) if the
operation results in an upsert.


The built-in role [`readWrite`](https://www.mongodb.com/docs/manual/reference/built-in-roles/#mongodb-authrole-readWrite) provides the required
privileges.

## Behavior [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#behavior "Permalink to this heading")

### Updates a Single Document [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#updates-a-single-document "Permalink to this heading")

[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) finds the first document that
matches the [filter](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter) and applies the specified
[update](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-update) modifications.

### Update with an Update Operator Expressions Document [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-an-update-operator-expressions-document "Permalink to this heading")

For the [update specifications](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-update), the
[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method can accept a document that
only contains [update operator](https://www.mongodb.com/docs/manual/reference/mql/update/#std-label-update-operators) expressions.

For example:

```
db.collection.updateOne(
   <query>,
   { $set: { status: "D" }, $inc: { quantity: 2 } },
   ...
)
```

### Update with an Aggregation Pipeline [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-an-aggregation-pipeline "Permalink to this heading")

The [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method can accept an
[aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/#std-label-aggregation-pipeline)`[ <stage1>, <stage2>, ... ]` that specifies the modifications to perform.
The pipeline can consist of the following stages:

- [`$addFields`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields) and its alias [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set)

- [`$project`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/#mongodb-pipeline-pipe.-project) and its alias [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset)

- [`$replaceRoot`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/#mongodb-pipeline-pipe.-replaceRoot) and its alias [`$replaceWith`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/#mongodb-pipeline-pipe.-replaceWith)


Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

For example:

```
db.collection.updateOne(
   <query>,
   [\
      { $set: { status: "Modified", comments: [ "$misc1", "$misc2" ] } },\
      { $unset: [ "misc1", "misc2" ] }\
   ]
   ...
)
```

## Note

The `$set` and `$unset` used in the pipeline refers to the
aggregation stages [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set) and [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset)
respectively, and not the update operators [`$set`](https://www.mongodb.com/docs/manual/reference/operator/update/set/#mongodb-update-up.-set) and [`$unset`.](https://www.mongodb.com/docs/manual/reference/operator/update/unset/#mongodb-update-up.-unset)

For examples, see [Update with Aggregation Pipeline.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-example-agg)

### Upsert [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#upsert "Permalink to this heading")

- Starting in MongoDB 7.1, if you specify `upsert: true` on a
sharded collection, you **do not** need to include the full shard
key in the [filter.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter)

- If `upsert: true` and no documents match the `filter`,
[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) creates a new
document based on the `filter` criteria and `update`
modifications. See [Update with Upsert.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-example-update-with-upsert)

- For additional [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) behavior on a
sharded collection, see [Sharded Collections.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-sharded-collection)


### Capped Collection [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#capped-collection "Permalink to this heading")

If an update operation changes the document size, the operation will fail.

### Sharded Collections [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#sharded-collections "Permalink to this heading")

#### `upsert` on a Sharded Collection [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#upsert-on-a-sharded-collection "Permalink to this heading")

To use [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) on a sharded collection:

- Starting in MongoDB 7.1, if you specify `upsert: true` on a
sharded collection, you **do not** need to include the full shard
key in the [filter.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter)

- If you don't specify `upsert: true`, you must include an exact
match on the `_id` field or target a single shard (such as by
including the shard key in the [filter](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter)).


However, documents in a sharded collection can be
[missing the shard key fields](https://www.mongodb.com/docs/manual/core/sharding-shard-key/#std-label-shard-key-missing). To target a
document that is missing the shard key, you can use the `null`
equality match **in conjunction with** another filter condition
(such as on the `_id` field). For example:

```
{ _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
```

#### Shard Key Modification [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#shard-key-modification "Permalink to this heading")

You can update a document's shard key value unless the shard key field is the
immutable `_id` field.

## Warning

Documents in sharded collections can be missing the shard key fields.
Take precaution to avoid accidentally removing the shard key when changing
a document's shard key value.

To modify the **existing** shard key value with
[`db.collection.updateOne()`:](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne)

- You **must** run on a [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos). Do **not**
issue the operation directly on the shard.

- You **must** run either in a [transaction](https://www.mongodb.com/docs/manual/core/transactions/) or as a [retryable write.](https://www.mongodb.com/docs/manual/core/retryable-writes/)

- You **must** include an equality [filter](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-update-one-filter) on the full shard key.


See also [`upsert` on a Sharded Collection.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-sharded-upsert)

#### Missing Shard Key [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#missing-shard-key "Permalink to this heading")

- Starting in version 7.1, you do not need to provide the [shard key](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard-key)
or `_id` field in the query specification.

- Documents in a sharded collection can be
[missing the shard key fields](https://www.mongodb.com/docs/manual/core/sharding-shard-key/#std-label-shard-key-missing). To use
[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) to set a **missing** shard key,
you **must** run on a [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos). Do **not** issue
the operation directly on the shard.

In addition, the following requirements also apply:




| Task | Requirements |
| --- | --- |
| To set to `null` | Requires equality filter on the full shard key if<br>`upsert: true`. |
| To set to a non-`null` value | **Must** be performed either inside a<br>[transaction](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions) or as a<br>[retryable write.](https://www.mongodb.com/docs/manual/core/retryable-writes/#std-label-retryable-writes)<br>Requires equality filter on the full shard key if `upsert: true`. |





## Tip





Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.


See also:

- [`upsert` on a Sharded Collection](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-sharded-upsert)

- [Missing Shard Key Fields](https://www.mongodb.com/docs/manual/core/sharding-shard-key/#std-label-shard-key-missing)


### Explainability [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#explainability "Permalink to this heading")

[`updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) is not compatible with
[`db.collection.explain()`.](https://www.mongodb.com/docs/manual/reference/method/db.collection.explain/#mongodb-method-db.collection.explain)

### Transactions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#transactions "Permalink to this heading")

[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) can be used inside [distributed transactions.](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions)

## Important

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
[denormalized data model (embedded documents and arrays)](https://www.mongodb.com/docs/manual/data-modeling/embedding/#std-label-data-modeling-embedding) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions.

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
[Production Considerations.](https://www.mongodb.com/docs/manual/core/transactions-production-consideration/#std-label-production-considerations)

#### Upsert within Transactions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#upsert-within-transactions "Permalink to this heading")

You can create collections and indexes inside a [distributed\\
transaction](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-create-collections-indexes) if the
transaction is **not** a cross-shard write transaction.

[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

## Tip

[Create Collections and Indexes in a Transaction](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-create-collections-indexes)

#### Write Concerns and Transactions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#write-concerns-and-transactions "Permalink to this heading")

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
[Transactions and Write Concern.](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-write-concern)

### Oplog Entries [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#oplog-entries "Permalink to this heading")

If a `db.collection.updateOne()` operation successfully updates a
document, the operation adds an entry on the [oplog](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-oplog) (operations
log). If the operation fails or does not find a document to update, the
operation does not add an entry on the oplog.

## Examples [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#examples "Permalink to this heading")

### Update using Update Operator Expressions [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-using-update-operator-expressions "Permalink to this heading")

The `restaurant` collection contains the following documents:

```
db.restaurant.insertMany( [\
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan" },\
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },\
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 0 }\
] )
```

The following operation updates a single document where
`name: "Central Perk Cafe"` with the `violations` field:

```
try {
   db.restaurant.updateOne(
      { "name" : "Central Perk Cafe" },
      { $set: { "violations" : 3 } }
   );
} catch (e) {
   print(e);
}
```

The operation returns:

```
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If no matches were found, the operation instead returns:

```
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```

Setting `upsert: true` would insert the document if no match was found. See
[Update with Upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#std-label-updateOne-example-update-with-upsert)

### Update with Aggregation Pipeline [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-aggregation-pipeline "Permalink to this heading")

The [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) can use an aggregation pipeline for the
update. The pipeline can consist of the following stages:

- [`$addFields`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields) and its alias [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set)

- [`$project`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/#mongodb-pipeline-pipe.-project) and its alias [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset)

- [`$replaceRoot`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/#mongodb-pipeline-pipe.-replaceRoot) and its alias [`$replaceWith`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/#mongodb-pipeline-pipe.-replaceWith)


Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

#### Example 1 [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#example-1 "Permalink to this heading")

The following examples uses the aggregation pipeline to modify a field
using the values of the other fields in the document.

Create a `students` collection with the following documents:

```
db.students.insertMany( [\
   { _id: 1, student: "Skye", points: 75, commentsSemester1: "great at math", commentsSemester2: "loses temper", lastUpdate: ISODate("2019-01-01T00:00:00Z") },\
   { _id: 2, student: "Elizabeth", points: 60, commentsSemester1: "well behaved", commentsSemester2: "needs improvement", lastUpdate: ISODate("2019-01-01T00:00:00Z") }\
] )
```

Assume that instead of separate `commentsSemester1` and `commentsSemester2`
fields in the first document, you want to gather these into a `comments` field,
like the second document. The following update operation uses an
aggregation pipeline to:

- add the new `comments` field and set the `lastUpdate` field.

- remove the `commentsSemester1` and `commentsSemester2` fields for all
documents in the collection.


Make sure that the filter in the update command targets a unique document. The
field `id` in the code below is an example of such a filter:

```
db.students.updateOne(
   { _id: 1 },
   [\
      { $set: { status: "Modified", comments: [ "$commentsSemester1", "$commentsSemester2" ], lastUpdate: "$$NOW" } },\
      { $unset: [ "commentsSemester1", "commentsSemester2" ] }\
   ]
)
```

## Note

The `$set` and `$unset` used in the pipeline refers to the
aggregation stages [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set) and [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset)
respectively, and not the update operators [`$set`](https://www.mongodb.com/docs/manual/reference/operator/update/set/#mongodb-update-up.-set) and [`$unset`.](https://www.mongodb.com/docs/manual/reference/operator/update/unset/#mongodb-update-up.-unset)

First Stage

The [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set) stage:

- creates a new array field `comments` whose elements are the current
content of the `misc1` and `misc2` fields and

- sets the field `lastUpdate` to the value of the aggregation
variable [`NOW`](https://www.mongodb.com/docs/manual/reference/aggregation-variables/#mongodb-variable-variable.NOW). The aggregation variable
[`NOW`](https://www.mongodb.com/docs/manual/reference/aggregation-variables/#mongodb-variable-variable.NOW) resolves to the current datetime value and remains
the same throughout the pipeline. To access aggregation
variables, prefix the variable with double dollar signs `$$`
and enclose in quotes.


Second StageThe [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/#mongodb-pipeline-pipe.-unset) stage removes the `commentsSemester1` and
`commentsSemester2` fields.

After the command, the collection contains the following documents:

```
{ _id: 2, student: "Elizabeth", status: "Modified", points: 60, lastUpdate: ISODate("2020-01-23T05:11:45.784Z"), comments: [ "well behaved", "needs improvement" ] }
{ _id: 1, student: 'Skye', points: 75, commentsSemester1: 'great at math', commentsSemester2: 'loses temper', lastUpdate: ISODate("2019-01-01T00:00:00.000Z") }
```

Note that after introducing a sort, only the first document encountered in the
sort order is modified and the remaining documents are left untouched.

#### Example 2 [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#example-2 "Permalink to this heading")

The aggregation pipeline allows the update to perform conditional
updates based on the current field values as well as use current field
values to calculate a separate field value.

For example, create a `students3` collection with the following documents:

```
db.students3.insertMany( [\
   { _id: 1, tests: [ 95, 92, 90 ], average: 92, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") },\
   { _id: 2, tests: [ 94, 88, 90 ], average: 91, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") },\
   { _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2019-01-01T00:00:00Z") }\
] )
```

The third document `_id: 3` is missing the `average` and `grade`
fields. Using an aggregation pipeline, you can update the document with
the calculated grade average and letter grade.

```
db.students3.updateOne(
   { _id: 3 },
   [\
     { $set: { average: { $trunc: [  { $avg: "$tests" }, 0 ] }, lastUpdate: "$$NOW" } },\
     { $set: { grade: { $switch: {\
                           branches: [\
                               { case: { $gte: [ "$average", 90 ] }, then: "A" },\
                               { case: { $gte: [ "$average", 80 ] }, then: "B" },\
                               { case: { $gte: [ "$average", 70 ] }, then: "C" },\
                               { case: { $gte: [ "$average", 60 ] }, then: "D" }\
                           ],\
                           default: "F"\
     } } } }\
   ]
)
```

## Note

The `$set` used in the pipeline refers to the aggregation stage
[`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set), and not the update operators [`$set`.](https://www.mongodb.com/docs/manual/reference/operator/update/set/#mongodb-update-up.-set)

First Stage

The [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set) stage:

- calculates a new field `average` based on the average of the
`tests` field. See [`$avg`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/avg/#mongodb-group-grp.-avg) for more information on the
`$avg` aggregation operator and [`$trunc`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/trunc/#mongodb-expression-exp.-trunc) for more
information on the `$trunc` truncate aggregation operator.

- sets the field `lastUpdate` to the value of the aggregation
variable [`NOW`](https://www.mongodb.com/docs/manual/reference/aggregation-variables/#mongodb-variable-variable.NOW). The aggregation variable
[`NOW`](https://www.mongodb.com/docs/manual/reference/aggregation-variables/#mongodb-variable-variable.NOW) resolves to the current datetime value and remains
the same throughout the pipeline. To access aggregation
variables, prefix the variable with double dollar signs `$$`
and enclose in quotes.


Second StageThe [`$set`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set) stage calculates a new field `grade` based on
the `average` field calculated in the previous stage. See
[`$switch`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/switch/#mongodb-expression-exp.-switch) for more information on the `$switch`
aggregation operator.

After the command, the collection contains the following documents:

```
{ _id: 1, tests: [ 95, 92, 90 ], average: 92, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") }
{ _id: 2, tests: [ 94, 88, 90 ], average: 91, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") }
{ _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2020-01-24T17:33:30.674Z"), average: 75, grade: "C" }
```

## Tip

[Updates with Aggregation Pipeline](https://www.mongodb.com/docs/manual/tutorial/update-documents-with-aggregation-pipeline/)

### Update with Upsert [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-upsert "Permalink to this heading")

The `restaurant` collection contains the following documents:

```
db.restaurant.insertMany( [\
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },\
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },\
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: "0" }\
] )
```

The following operation attempts to update the document with
`name : "Pizza Rat's Pizzaria"`, while `upsert: true` :

```
try {
   db.restaurant.updateOne(
      { "name" : "Pizza Rat's Pizzaria" },
      { $set: {"_id" : 4, "violations" : 7, "borough" : "Manhattan" } },
      { upsert: true }
   );
} catch (e) {
   print(e);
}
```

Since `upsert:true` the document is `inserted` based on the `filter` and
`update` criteria. The operation returns:

```
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : 4,
   "upsertedCount": 1
}
```

The collection now contains the following documents:

```
{ _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
{ _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
{ _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 4 },
{ _id: 4, name: "Pizza Rat's Pizzaria", Borough: "Manhattan", violations: 7 }
```

The `name` field was filled in using the `filter` criteria, while the
`update` operators were used to create the rest of the document.

The following operation updates the first document with `violations` that
are greater than `10`:

```
try {
   db.restaurant.updateOne(
      { "violations" : { $gt: 10} },
      { $set: { "Closed" : true } },
      { upsert: true }
   );
} catch (e) {
   print(e);
}
```

The operation returns:

```
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : ObjectId("56310c3c0c5cbb6031cafaea")
}
```

The collection now contains the following documents:

```
{ _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
{ _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
{ _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 4 },
{ _id: 4, name: "Pizza Rat's Pizzaria", Borough: "Manhattan", grade: 7 }
{ _id: ObjectId("56310c3c0c5cbb6031cafaea"), Closed: true }
```

Since no documents matched the filter, and `upsert` was `true`,
[`updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) inserted the document with a generated
`_id` and the `update` criteria only.

### Update with Write Concern [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-write-concern "Permalink to this heading")

Given a three member replica set, the following operation specifies a
`w` of `majority`, `wtimeout` of `100`:

```
try {
   db.restaurant.updateOne(
       { "name" : "Pizza Rat's Pizzaria" },
       { $inc: { "violations" : 3}, $set: { "Closed" : true } },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print(e);
}
```

If the primary and at least one secondary acknowledge each write operation
within 100 milliseconds, it returns:

```
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If the acknowledgment takes longer than the `wtimeout` limit, the following
exception is thrown:

```
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : {
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```

The following table explains the possible values of
`errInfo.writeConcern.provenance`:

| Provenance | Description |
| --- | --- |
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined<br>default value. See [`setDefaultRWConcern`.](https://www.mongodb.com/docs/manual/reference/command/setDefaultRWConcern/#mongodb-dbcommand-dbcmd.setDefaultRWConcern) |
| `getLastErrorDefaults` | The write concern originated from the replica set's<br>[`settings.getLastErrorDefaults`](https://www.mongodb.com/docs/manual/reference/replica-configuration/#mongodb-rsconf-rsconf.settings.getLastErrorDefaults) field. |
| `implicitDefault` | The write concern originated from the server in absence<br>of all other write concern specifications. |

### Update with Sort [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-with-sort "Permalink to this heading")

_New in version 8.0_.

The following example deactivates the lowest rated active user:

```
db.people.updateOne(
   { state: "active" },
   { $set: { state: "inactive" } },
   { sort: { rating: 1 } }
)
```

### Specify Collation [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#specify-collation "Permalink to this heading")

[Collation](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation) allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```
db.myColl.insertMany( [\
   { _id: 1, category: "café", status: "A" },\
   { _id: 2, category: "cafe", status: "a" },\
   { _id: 3, category: "cafE", status: "a" }\
] )
```

The following operation includes the [collation](https://www.mongodb.com/docs/manual/reference/collation/#std-label-collation)
option:

```
db.myColl.updateOne(
   { category: "cafe" },
   { $set: { status: "Updated" } },
   { collation: { locale: "fr", strength: 1 } }
);
```

### Specify `arrayFilters` for an Array Update Operations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#specify-arrayfilters-for-an-array-update-operations "Permalink to this heading")

When updating an array field, you can specify `arrayFilters` that
determine which array elements to update.

#### Update Elements Match `arrayFilters` Criteria [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-elements-match-arrayfilters-criteria "Permalink to this heading")

Create a collection `students` with the following documents:

```
db.students.insertMany( [\
   { _id: 1, grades: [ 95, 92, 90 ] },\
   { _id: 2, grades: [ 98, 100, 102 ] },\
   { _id: 3, grades: [ 95, 110, 100 ] }\
] )
```

To modify all elements that are greater than or equal to `100` in the
`grades` array, use the filtered positional operator
[`$[<identifier>]`](https://www.mongodb.com/docs/manual/reference/operator/update/positional-filtered/#mongodb-update-up.---identifier--) with the `arrayFilters` option in the
[`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method:

```
db.students.updateOne(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

The operation updates the `grades` field of a single document, and
after the operation, the collection has the following documents:

```
{ _id: 1, grades: [ 95, 92, 90 ] }
{ _id: 2, grades: [ 98, 100, 100 ] }
{ _id: 3, grades: [ 95, 110, 100 ] }
```

#### Update Specific Elements of an Array of Documents [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#update-specific-elements-of-an-array-of-documents "Permalink to this heading")

Create a collection `students2` with the following documents:

```
db.students2.insertMany( [\
   {\
      _id: 1,\
      grades: [\
         { grade: 80, mean: 75, std: 6 },\
         { grade: 85, mean: 90, std: 4 },\
         { grade: 85, mean: 85, std: 6 }\
      ]\
   },\
   {\
      _id: 2,\
      grades: [\
         { grade: 90, mean: 75, std: 6 },\
         { grade: 87, mean: 90, std: 3 },\
         { grade: 85, mean: 85, std: 4 }\
      ]\
   }\
] )
```

To modify the value of the `mean` field for all elements in the
`grades` array where the grade is greater than or equal to `85`,
use the filtered positional operator [`$[<identifier>]`](https://www.mongodb.com/docs/manual/reference/operator/update/positional-filtered/#mongodb-update-up.---identifier--) with
the `arrayFilters` in the [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) method:

```
db.students2.updateOne(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

The operation updates the array of a single document, and after the
operation, the collection has the following documents:

```
{
   _id: 1,
   grades: [\
      { grade: 80, mean: 75, std: 6 },\
      { grade: 85, mean: 100, std: 4 },\
      { grade: 85, mean: 100, std: 6 }\
    ]
}
{
   _id: 2,
   grades: [\
      { grade: 90, mean: 75, std: 6 },\
      { grade: 87, mean: 90, std: 3 },\
      { grade: 85, mean: 85, std: 4 }\
   ]
}
```

### Specify `hint` for Update Operations [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#specify-hint-for-update-operations "Permalink to this heading")

Create a sample `students` collection with the following documents:

```
db.students.insertMany( [\
   { _id: 1, student: "Richard", grade: "F", points:  0,  comments1: null, comments2: null },\
   { _id: 2, student: "Jane", grade: "A", points: 60,  comments1: "well behaved", comments2: "fantastic student" },\
   { _id: 3, student: "Ronan", grade: "F", points:  0,  comments1: null, comments2: null },\
   { _id: 4, student: "Noah", grade: "D", points: 20,  comments1: "needs improvement", comments2: null },\
   { _id: 5, student: "Adam", grade: "F", points:  0,  comments1: null, comments2: null },\
   { _id: 6, student: "Henry", grade: "A", points: 86,  comments1: "fantastic student", comments2: "well behaved" }\
] )
```

Create the following indexes on the collection:

```
db.students.createIndex( { grade: 1 } )
db.students.createIndex( { points: 1 } )
```

The following update operation explicitly hints to use the index `{
grade: 1 }`:

## Note

If you specify an index that does not exist, the operation errors.

```
db.students.updateOne(
   { "points": { $lte: 20 }, "grade": "F" },
   { $set: { "comments1": "failed class" } },
   { hint: { grade: 1 } }
)
```

The update command returns the following:

```
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

## Note

Even though 3 documents match the criteria of the update, `updateOne` only
modifies the first document it finds. Therefore, even though the students
Richard, Ronan, and Adam all meet the criteria, only Richard will be updated.

To see the index used, run [`explain`](https://www.mongodb.com/docs/manual/reference/command/explain/#mongodb-dbcommand-dbcmd.explain) on the operation:

```
db.students.explain().update(
   { "points": { $lte: 20 }, "grade": "F" },
   { $set: { "comments1": "failed class" } },
   { multi: true, hint: { grade: 1 } }
)
```

### Write Concern Errors in Sharded Clusters [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#write-concern-errors-in-sharded-clusters "Permalink to this heading")

_Changed in version 8.1.2_.

When [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) executes on [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#std-program-mongos) in a sharded cluster, a `writeConcernError` is
always reported in the response, even when one or more other errors occur.
In previous releases, other errors sometimes caused [`db.collection.updateOne()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) to not report write concern errors.

For example, if a document fails validation, triggering a `DocumentValidationFailed` error,
and a write concern error also occurs, both the `DocumentValidationFailed` error and the
`writeConcernError` are returned in the top-level field of the response.

### User Roles and Document Updates [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#user-roles-and-document-updates "Permalink to this heading")

Starting in MongoDB 7.0, you can use the new [`USER_ROLES`](https://www.mongodb.com/docs/manual/reference/aggregation-variables/#mongodb-variable-variable.USER_ROLES)
system variable to return user [roles.](https://www.mongodb.com/docs/manual/core/authorization/#std-label-roles)

The example in this section shows updates to fields in a collection
containing medical information. The example reads the current user roles
from the `USER_ROLES` system variable and only performs the updates if
the user has a specific role.

To use a system variable, add `$$` to the start of the variable name.
Specify the `USER_ROLES` system variable as `$$USER_ROLES`.

The example creates these users:

- `James` with a `Billing` role.

- `Michelle` with a `Provider` role.


Perform the following steps to create the roles, users, and collection:

1

#### Create the roles [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#create-the-roles "Permalink to this heading")

Create roles named `Billing` and `Provider` with the required
privileges and resources.

Run:

```
db.createRole( { role: "Billing", privileges: [ { resource: { db: "test",\
   collection: "medicalView" }, actions: [ "find" ] } ], roles: [ ] } )
db.createRole( { role: "Provider", privileges: [ { resource: { db: "test",\
   collection: "medicalView" }, actions: [ "find" ] } ], roles: [ ] } )
```

2

#### Create the users [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#create-the-users "Permalink to this heading")

Create users named `James` and `Michelle` with the required
roles.

```
db.createUser( {
   user: "James",
   pwd: "js008",
   roles: [\
      { role: "Billing", db: "test" }\
   ]
} )

db.createUser( {
   user: "Michelle",
   pwd: "me009",
   roles: [\
      { role: "Provider", db: "test" }\
   ]
} )
```

3

#### Create the collection [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#create-the-collection "Permalink to this heading")

Run:

```
db.medical.insertMany( [\
   {\
      _id: 0,\
      patientName: "Jack Jones",\
      diagnosisCode: "CAS 17",\
      creditCard: "1234-5678-9012-3456"\
   },\
   {\
      _id: 1,\
      patientName: "Mary Smith",\
      diagnosisCode: "ACH 01",\
      creditCard: "6541-7534-9637-3456"\
   }\
] )
```

Log in as as `Michelle`, who has the `Provider` role, and perform an
update:

1

#### Log in as `Michelle` [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#log-in-as-michelle "Permalink to this heading")

Run:

```
db.auth( "Michelle", "me009" )
```

2

#### Perform update [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#perform-update "Permalink to this heading")

Run:

```
// Attempt to update one document
db.medical.updateOne( {
   // User must have the Provider role to perform the update
   $expr: { $ne: [\
      { $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []\
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 01"} }
)
```

The previous example uses [`$setIntersection`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/setIntersection/#mongodb-expression-exp.-setIntersection) to return
documents where the intersection between the `"Provider"` string and
the user roles from `$$USER_ROLES.role` is not empty. `Michelle` has
the `Provider` role, so the update is performed.

Next, log in as as `James`, who does not have the `Provider` role,
and attempt to perform the same update:

1

#### Log in as `James` [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#log-in-as-james "Permalink to this heading")

Run:

```
db.auth( "James", "js008" )
```

2

#### Attempt to perform update [Permalink to this heading](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/\#attempt-to-perform-update "Permalink to this heading")

Run:

```
// Attempt to update one document
db.medical.updateOne( {
   // User must have the Provider role to perform the update
   $expr: { $ne: [\
      { $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []\
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 01"} }
)
```

The previous example does not update any documents.

## Tip

To update multiple documents, see
[`db.collection.updateMany()`.](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/#mongodb-method-db.collection.updateMany)

[Back\\
\\
db.collection.updateMany](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/ "Previous Section")

[Next\\
\\
db.collection.validate](https://www.mongodb.com/docs/manual/reference/method/db.collection.validate/ "Next Section")

Rate this page

On this page

- [Definition](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#definition)
- [Compatibility](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#compatibility)
- [Syntax](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#syntax)
- [Access Control](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#access-control)
- [Behavior](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#behavior)
- [Examples](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#examples)

On this page

- [Definition](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#definition)
- [Compatibility](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#compatibility)
- [Syntax](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#syntax)
- [Access Control](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#access-control)
- [Behavior](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#behavior)
- [Examples](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#examples)

0 more notification

0 more notification