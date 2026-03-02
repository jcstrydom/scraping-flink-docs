Docs Menu

Ask MongoDB AI

[Docs Home](https://www.mongodb.com/docs/)

/

/

[Java Sync Driver](https://www.mongodb.com/docs/drivers/java/sync/current)

[Docs Home](https://www.mongodb.com/docs/)

/

[Client Libraries](https://www.mongodb.com/docs/drivers)

/

[Java](https://www.mongodb.com/docs/languages/java)

/

[Java Sync Driver](https://www.mongodb.com/docs/drivers/java/sync/current)

[Docs Home](https://www.mongodb.com/docs/)

/

[Client Libraries](https://www.mongodb.com/docs/drivers)

/

[Java](https://www.mongodb.com/docs/languages/java)

/

[Java Sync Driver](https://www.mongodb.com/docs/drivers/java/sync/current)

# Document Data Format: Extended JSON [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#document-data-format--extended-json "Permalink to this heading")

Copy page

## Overview [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#overview "Permalink to this heading")

In this guide, you can learn how to use the Extended JSON format in the
MongoDB Java driver.

JSON is a data format that represents the values of objects, arrays, numbers,
strings, booleans, and nulls. The **Extended JSON** format defines a reserved
set of keys prefixed with "`$`" to represent field type information that
directly corresponds to each type in BSON, the format that MongoDB uses to
store data.

This guide explains the following topics:

- The different MongoDB Extended JSON formats

- How to use the BSON library to convert between Extended JSON and Java objects

- How to create a custom conversion of BSON types


For more information about the difference between these formats, see our
[article on JSON and BSON.](https://www.mongodb.com/json-and-bson)

## Extended JSON Formats [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#extended-json-formats "Permalink to this heading")

MongoDB Extended JSON features different string formats to represent BSON data.
Each of the different formats conform to the JSON RFC
and meet specific use cases. The **extended** format, also known as the
**canonical** format, features specific representations for every BSON type
for bidirectional conversion without loss of information. The **Relaxed mode**
format is more concise and closer to ordinary JSON, but does not represent
all the type information such as the specific byte size of number fields.

See the following table to see a description of each format:

| Name | Description |
| --- | --- |
| **Extended** | Also known as the _canonical_ format, this JSON representation avoids loss of BSON type information.<br>This format prioritizes type preservation at the loss of human-readability and interoperability with older formats. |
| **Relaxed Mode** | JSON representation that describes BSON documents with some type information loss.<br>This format prioritizes human-readability and interoperability at the loss of certain type information. |
| **Shell** | JSON representation that matches the syntax used in the MongoDB shell.<br>This format prioritizes compatibility with the MongoDB shell which often uses JavaScript functions to represent types. |
| **Strict** | _Deprecated._ This representation is the legacy format that fully conforms to the [JSON RFC](http://www.json.org/) which allows any JSON parser to read the type information.<br>The legacy API uses this format. |

## Note

The driver parses the `$uuid` Extended JSON type from a string to a
`BsonBinary` object of binary subtype 4. For more information about `$uuid` field
parsing, see the
[special rules for parsing $uuid fields](https://github.com/mongodb/specifications/blob/master/source/extended-json.rst#special-rules-for-parsing-uuid-fields)
section in the extended JSON specification.

For more detailed information on these formats, see the following
resources:

- [JSON RFC](https://tools.ietf.org/html/rfc7159) Official Documentation

- [MongoDB Extended JSON](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) Server Manual Entry

- [BsonBinary](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/BsonBinary.html) API Documentation

- [Extended JSON specification](https://github.com/mongodb/specifications/blob/master/source/extended-json.rst) GitHub Documentation


### Extended JSON Examples [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#extended-json-examples "Permalink to this heading")

The following examples show a document containing an ObjectId, date, and long
number field represented in each Extended JSON format. Click the tab that
corresponds to the format of the example you want to see:

Extended

Relaxed Mode

Shell

Strict

```
{
  "_id": { "$oid": "573a1391f29313caabcd9637" },
  "createdAt": { "$date": { "$numberLong": "1601499609" }},
  "numViews": { "$numberLong": "36520312" }
}
```

```
{
  "_id": { "$oid": "573a1391f29313caabcd9637" },
  "createdAt": { "$date": "2020-09-30T18:22:51.648Z" },
  "numViews": 36520312
}
```

```
{
  "_id": ObjectId("573a1391f29313caabcd9637"),
  "createdAt": ISODate("2020-09-30T18:22:51.648Z"),
  "numViews": NumberLong("36520312")
}
```

```
{
  "_id": { "$oid": "573a1391f29313caabcd9637" },
  "createdAt": { "$date": 1601499609 },
  "numViews": { "$numberLong": "36520312" }
}
```

## Read Extended JSON [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#read-extended-json "Permalink to this heading")

### Using the Document Classes [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#using-the-document-classes "Permalink to this heading")

You can read an Extended JSON string into a Java document object by calling
the `parse()` static method from either the `Document` or `BsonDocument`
class, depending on which object type you need. This method parses the Extended
JSON string in any of the formats and returns an instance of that class
containing the data.

The following example shows how you can use the `Document` class to read
an example Extended JSON string into a `Document` object using the
`parse()` method:

```
String ejsonStr = "{ \"_id\": { \"$oid\": \"507f1f77bcf86cd799439011\"}," +
                  "\"myNumber\": {\"$numberLong\": \"4794261\" }}}";

Document doc = Document.parse(ejsonStr);
System.out.println(doc);
```

VIEW OUTPUT

```
Document{{_id=507f1f77bcf86cd799439011, myNumber=4794261}}
```

For more information, see our Fundamentals page
on [Documents.](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/documents/#std-label-fundamentals-documents)

### Using the BSON Library [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#using-the-bson-library "Permalink to this heading")

You can also read an Extended JSON string into Java objects without using
the MongoDB Java driver's document classes by using the `JsonReader` class.
This class contains methods to sequentially parse the fields and values
in any format of the Extended JSON string, and returns them as Java objects.
The driver's document classes also use this class to parse Extended JSON.

The following code example shows how you can use the `JsonReader` class to convert
an Extended JSON string into Java objects:

```
String ejsonStr = "{ \"_id\": { \"$oid\": \"507f1f77bcf86cd799439011\"}," +
                  "\"myNumber\": {\"$numberLong\": \"4794261\" }}}";

JsonReader jsonReader = new JsonReader(ejsonStr);

jsonReader.readStartDocument();

jsonReader.readName("_id");
ObjectId id = jsonReader.readObjectId();
jsonReader.readName("myNumber");
Long myNumber = jsonReader.readInt64();

jsonReader.readEndDocument();

System.out.println(id + " is type: " + id.getClass().getName());
System.out.println(myNumber + " is type: " + myNumber.getClass().getName());

jsonReader.close();
```

VIEW OUTPUT

```
507f1f77bcf86cd799439011 is type: org.bson.types.ObjectId
4794261 is type: java.lang.Long
```

For more information, see the [JsonReader](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/JsonReader.html) API Documentation.

## Write Extended JSON [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#write-extended-json "Permalink to this heading")

### Using the Document Classes [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#using-the-document-classes-1 "Permalink to this heading")

You can write an Extended JSON string from an instance of `Document` or
`BsonDocument` by calling the `toJson()` method, optionally passing it an
instance of `JsonWriterSettings` to specify the Extended JSON format.

In this example, we output the Extended JSON in the Relaxed mode format.

```
Document myDoc = new Document();
myDoc.append("_id", new ObjectId("507f1f77bcf86cd799439012")).append("myNumber", 11223344);

JsonWriterSettings settings = JsonWriterSettings.builder().outputMode(JsonMode.RELAXED).build();
System.out.println(doc.toJson(settings));
```

VIEW OUTPUT

```
{"_id": {"$oid": "507f1f77bcf86cd799439012"}, "myNumber": 11223344}
```

### Using the BSON Library [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#using-the-bson-library-1 "Permalink to this heading")

You can also output an Extended JSON string from data in Java objects using
the BSON library with the `JsonWriter` class. To construct an instance
of `JsonWriter`, pass a subclass of a Java `Writer` to specify how
you want to output the Extended JSON. You can optionally pass a `JsonWriterSettings`
instance to specify options such as the Extended JSON format. By default, the
`JsonWriter` uses the Relaxed mode format. The MongoDB Java driver's
document classes also use this class to convert BSON to Extended JSON.

The following code example shows how you can use `JsonWriter` to create an
Extended JSON string and output it to `System.out`. We specify the format
by passing the `outputMode()` builder method the `JsonMode.EXTENDED` constant:

```
JsonWriterSettings settings = JsonWriterSettings.builder().outputMode(JsonMode.EXTENDED).build();

try (JsonWriter jsonWriter = new JsonWriter(new BufferedWriter(new OutputStreamWriter(System.out)), settings)) {
    jsonWriter.writeStartDocument();
    jsonWriter.writeObjectId("_id", new ObjectId("507f1f77bcf86cd799439012"));
    jsonWriter.writeInt64("myNumber", 11223344);
    jsonWriter.writeEndDocument();
    jsonWriter.flush();
}
```

VIEW OUTPUT

```
{"_id": {"$oid": "507f1f77bcf86cd799439012"}, "myNumber": {"$numberLong": "11223344"}}
```

For more information about the methods and classes mentioned in this section,
see the following API Documentation:

- [JsonWriter](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/JsonWriter.html)

- [JsonWriterSettings](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/JsonWriterSettings.html)

- [outputMode()](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/JsonWriterSettings.Builder.html#outputMode(org.bson.json.JsonMode))


## Custom BSON Type Conversion [Permalink to this heading](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/\#custom-bson-type-conversion "Permalink to this heading")

In addition to specifying the `outputMode()` to format the JSON output, you
can further customize the output by adding converters to your
`JsonWriterSettings.Builder`. These converter methods detect the Java types
and execute the logic defined by the `Converter` passed to them.

The following sample code shows how to append converters, defined as lambda
expressions, to simplify the Relaxed mode JSON output.

```
JsonWriterSettings settings = JsonWriterSettings.builder().outputMode(JsonMode.RELAXED)
        .objectIdConverter((value, writer) -> writer.writeString(value.toHexString()))
        .dateTimeConverter(
                (value, writer) -> {
                    ZonedDateTime zonedDateTime = Instant.ofEpochMilli(value).atZone(ZoneOffset.UTC);
                    writer.writeString(DateTimeFormatter.ISO_DATE_TIME.format(zonedDateTime));
                })
        .build();

Document doc = new Document()
     .append("_id", new ObjectId("507f1f77bcf86cd799439012"))
     .append("createdAt", Date.from(Instant.ofEpochMilli(1601499609000L)))
     .append("myNumber", 4794261);

System.out.println(doc.toJson(settings)));
```

The output of this code resembles the following text:

```
{"_id": "507f1f77bcf86cd799439012", "createdAt": "2020-09-30T21:00:09Z", "myNumber": 4794261}
```

Without specifying the converters, the Relaxed mode JSON output resembles the following text:

```
{"_id": {"$oid": "507f1f77bcf86cd799439012"}, "createdAt": {"$date": "2020-09-30T21:00:09Z"}, "myNumber": 4794261}
```

For more information about the methods and classes mentioned in this section,
see the following API Documentation:

- [Converter](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/Converter.html)

- [JsonWriterSettings.Builder](https://mongodb.github.io/mongo-java-driver/5.6/apidocs/bson/org/bson/json/JsonWriterSettings.Builder.html)


[Back\\
\\
BSON](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-bson/ "Previous Section")

[Next\\
\\
Documents](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/documents/ "Next Section")

Rate this page

On this page

- [Overview](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#overview)
- [Extended JSON Formats](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#extended-json-formats)
- [Extended JSON Examples](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#extended-json-examples)
- [Read Extended JSON](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#read-extended-json)
- [Using the Document Classes](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-document-classes)
- [Using the BSON Library](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-bson-library)
- [Write Extended JSON](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#write-extended-json)
- [Using the Document Classes](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-document-classes-1)
- [Using the BSON Library](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-bson-library-1)
- [Custom BSON Type Conversion](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#custom-bson-type-conversion)

On this page

- [Overview](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#overview)
- [Extended JSON Formats](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#extended-json-formats)
- [Extended JSON Examples](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#extended-json-examples)
- [Read Extended JSON](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#read-extended-json)
- [Using the Document Classes](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-document-classes)
- [Using the BSON Library](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-bson-library)
- [Write Extended JSON](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#write-extended-json)
- [Using the Document Classes](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-document-classes-1)
- [Using the BSON Library](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#using-the-bson-library-1)
- [Custom BSON Type Conversion](https://www.mongodb.com/docs/drivers/java/sync/current/data-formats/document-data-format-extended-json/#custom-bson-type-conversion)

0 more notification

0 more notification