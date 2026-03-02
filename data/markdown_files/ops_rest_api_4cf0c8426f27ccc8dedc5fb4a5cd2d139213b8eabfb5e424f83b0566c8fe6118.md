# REST API  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#rest-api)

Flink has a monitoring API that can be used to query status and statistics of running jobs, as well as recent completed jobs.
This monitoring API is used by Flink’s own dashboard, but is designed to be used also by custom monitoring tools.

The monitoring API is a REST-ful API that accepts HTTP requests and responds with JSON data.

## Overview  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#overview)

The monitoring API is backed by a web server that runs as part of the _JobManager_. By default, this server listens at port `8081`, which can be configured in [Flink configuration file](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#flink-configuration-file) via `rest.port`. Note that the monitoring API web server and the web dashboard web server are currently the same and thus run together at the same port. They respond to different HTTP URLs, though.

In the case of multiple JobManagers (for high availability), each JobManager will run its own instance of the monitoring API, which offers information about completed and running job while that JobManager was elected the cluster leader.

## Developing  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#developing)

The REST API backend is in the `flink-runtime` project. The core class is `org.apache.flink.runtime.webmonitor.WebMonitorEndpoint`, which sets up the server and the request routing.

We use _Netty_ and the _Netty Router_ library to handle REST requests and translate URLs. This choice was made because this combination has lightweight dependencies, and the performance of Netty HTTP is very good.

To add new requests, one needs to

- add a new `MessageHeaders` class which serves as an interface for the new request,
- add a new `AbstractRestHandler` class which handles the request according to the added `MessageHeaders` class,
- add the handler to `org.apache.flink.runtime.webmonitor.WebMonitorEndpoint#initializeHandlers()`.

A good example is the `org.apache.flink.runtime.rest.handler.job.JobExceptionsHandler` that uses the `org.apache.flink.runtime.rest.messages.JobExceptionsHeaders`.

## API  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#api)

The REST API is versioned, with specific versions being queryable by prefixing the url with the version prefix. Prefixes are always of the form `v[version_number]`.
For example, to access version 1 of `/foo/bar` one would query `/v1/foo/bar`.

If no version is specified Flink will default to the _oldest_ version supporting the request.

Querying unsupported/non-existing versions will return a 404 error.

There exist several async operations among these APIs, e.g. `trigger savepoint`, `rescale a job`. They would return a `triggerid` to identify the operation you just POST and then you need to use that `triggerid` to query for the status of the operation.

For (stop-with-)savepoint operations you can control this `triggerId` by setting it in the body of the request that triggers the operation.
This allow you to safely\* retry such operations without triggering multiple savepoints.

> The retry is only safe until the [async operation store duration](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/deployment/config/#rest-async-store-duration) has elapsed.

### JobManager  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager)

[OpenAPI specification](https://nightlies.apache.org/flink/flink-docs-release-2.2/generated/rest_v1_dispatcher.yml)

> The OpenAPI specification is still experimental.

#### API reference  [\#](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#api-reference)

v1

|     |     |
| --- | --- |
| ##### **/cluster** [Anchor link for: cluster](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#cluster) |
| Verb: `DELETE` | Response code: `200 OK` |
| Shuts down the cluster |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{}<br>``` |

|     |     |
| --- | --- |
| ##### **/config** [Anchor link for: config](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#config) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the configuration of the WebUI. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:DashboardConfiguration",<br>  "properties" : {<br>    "features" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:DashboardConfiguration:Features",<br>      "properties" : {<br>        "web-cancel" : {<br>          "type" : "boolean"<br>        },<br>        "web-history" : {<br>          "type" : "boolean"<br>        },<br>        "web-rescale" : {<br>          "type" : "boolean"<br>        },<br>        "web-submit" : {<br>          "type" : "boolean"<br>        }<br>      }<br>    },<br>    "flink-revision" : {<br>      "type" : "string"<br>    },<br>    "flink-version" : {<br>      "type" : "string"<br>    },<br>    "refresh-interval" : {<br>      "type" : "integer"<br>    },<br>    "timezone-name" : {<br>      "type" : "string"<br>    },<br>    "timezone-offset" : {<br>      "type" : "integer"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/datasets** [Anchor link for: datasets](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#datasets) |
| Verb: `GET` | Response code: `200 OK` |
| Returns all cluster data sets. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:dataset:ClusterDataSetListResponseBody",<br>  "properties" : {<br>    "dataSets" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:dataset:ClusterDataSetEntry",<br>        "properties" : {<br>          "id" : {<br>            "type" : "string"<br>          },<br>          "isComplete" : {<br>            "type" : "boolean"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/datasets/delete/:triggerid** [Anchor link for: datasets delete triggerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#datasets-delete-triggerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the status for the delete operation of a cluster data set. |
| Path parameters |
| - `triggerid` \- 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationResult",<br>  "properties" : {<br>    "operation" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationInfo",<br>      "properties" : {<br>        "failure-cause" : {<br>          "type" : "any"<br>        }<br>      }<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/datasets/:datasetid** [Anchor link for: datasets datasetid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#datasets-datasetid) |
| Verb: `DELETE` | Response code: `202 Accepted` |
| Triggers the deletion of a cluster data set. This async operation would return a 'triggerid' for further query identifier. |
| Path parameters |
| - `datasetid` \- 32-character hexadecimal string value that identifies a cluster data set. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jars** [Anchor link for: jars](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jars) |
| Verb: `GET` | Response code: `200 OK` |
| Returns a list of all jars previously uploaded via '/jars/upload'. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarListInfo",<br>  "properties" : {<br>    "address" : {<br>      "type" : "string"<br>    },<br>    "files" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarListInfo:JarFileInfo",<br>        "properties" : {<br>          "entry" : {<br>            "type" : "array",<br>            "items" : {<br>              "type" : "object",<br>              "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarListInfo:JarEntryInfo",<br>              "properties" : {<br>                "description" : {<br>                  "type" : "string"<br>                },<br>                "name" : {<br>                  "type" : "string"<br>                }<br>              }<br>            }<br>          },<br>          "id" : {<br>            "type" : "string"<br>          },<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "uploaded" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jars/upload** [Anchor link for: jars upload](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jars-upload) |
| Verb: `POST` | Response code: `200 OK` |
| Uploads a jar to the cluster. The jar must be sent as multi-part data. Make sure that the "Content-Type" header is set to "application/x-java-archive", as some http libraries do not add the header by default.<br>Using 'curl' you can upload a jar via 'curl -X POST -H "Expect:" -F "jarfile=@path/to/flink-job.jar" http://hostname:port/jars/upload'. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarUploadResponseBody",<br>  "properties" : {<br>    "filename" : {<br>      "type" : "string"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "success" ]<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jars/:jarid** [Anchor link for: jars jarid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jars-jarid) |
| Verb: `DELETE` | Response code: `200 OK` |
| Deletes a jar previously uploaded via '/jars/upload'. |
| Path parameters |
| - `jarid` \- String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the \`id\` field in the list of uploaded jars (/jars). |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{}<br>``` |

|     |     |
| --- | --- |
| ##### **/jars/:jarid/plan** [Anchor link for: jars jarid plan](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jars-jarid-plan) |
| Verb: `POST` | Response code: `200 OK` |
| Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters. |
| Path parameters |
| - `jarid` \- String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the \`id\` field in the list of uploaded jars (/jars). |
| Query parameters |
| - `programArg` (optional): Comma-separated list of program arguments.<br>- `entry-class` (optional): String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest.<br>- `parallelism` (optional): Positive integer value that specifies the desired parallelism for the job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarPlanRequestBody",<br>  "properties" : {<br>    "entryClass" : {<br>      "type" : "string"<br>    },<br>    "flinkConfiguration" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "string"<br>      }<br>    },<br>    "jobId" : {<br>      "type" : "any"<br>    },<br>    "parallelism" : {<br>      "type" : "integer"<br>    },<br>    "programArgsList" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "string"<br>      }<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo",<br>  "properties" : {<br>    "plan" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan",<br>      "properties" : {<br>        "jid" : {<br>          "type" : "string"<br>        },<br>        "name" : {<br>          "type" : "string"<br>        },<br>        "nodes" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node",<br>            "properties" : {<br>              "description" : {<br>                "type" : "string"<br>              },<br>              "id" : {<br>                "type" : "string"<br>              },<br>              "inputs" : {<br>                "type" : "array",<br>                "items" : {<br>                  "type" : "object",<br>                  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node:Input",<br>                  "properties" : {<br>                    "caching" : {<br>                      "type" : "string"<br>                    },<br>                    "exchange" : {<br>                      "type" : "string"<br>                    },<br>                    "id" : {<br>                      "type" : "string"<br>                    },<br>                    "local_strategy" : {<br>                      "type" : "string"<br>                    },<br>                    "num" : {<br>                      "type" : "integer"<br>                    },<br>                    "ship_strategy" : {<br>                      "type" : "string"<br>                    }<br>                  }<br>                }<br>              },<br>              "operator" : {<br>                "type" : "string"<br>              },<br>              "operator_strategy" : {<br>                "type" : "string"<br>              },<br>              "optimizer_properties" : {<br>                "type" : "object",<br>                "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:RawJson"<br>              },<br>              "parallelism" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        },<br>        "type" : {<br>          "type" : "string"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jars/:jarid/run** [Anchor link for: jars jarid run](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jars-jarid-run) |
| Verb: `POST` | Response code: `200 OK` |
| Submits a job by running a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters. |
| Path parameters |
| - `jarid` \- String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the \`id\` field in the list of uploaded jars (/jars). |
| Query parameters |
| - `allowNonRestoredState` (optional): Boolean value that specifies whether the job submission should be rejected if the savepoint contains state that cannot be mapped back to the job.<br>- `savepointPath` (optional): String value that specifies the path of the savepoint to restore the job from.<br>- `programArg` (optional): Comma-separated list of program arguments.<br>- `entry-class` (optional): String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest.<br>- `parallelism` (optional): Positive integer value that specifies the desired parallelism for the job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarRunRequestBody",<br>  "properties" : {<br>    "allowNonRestoredState" : {<br>      "type" : "boolean"<br>    },<br>    "claimMode" : {<br>      "type" : "string",<br>      "enum" : [ "CLAIM", "NO_CLAIM", "LEGACY" ]<br>    },<br>    "entryClass" : {<br>      "type" : "string"<br>    },<br>    "flinkConfiguration" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "string"<br>      }<br>    },<br>    "jobId" : {<br>      "type" : "any"<br>    },<br>    "parallelism" : {<br>      "type" : "integer"<br>    },<br>    "programArgsList" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "string"<br>      }<br>    },<br>    "restoreMode" : {<br>      "type" : "string",<br>      "enum" : [ "CLAIM", "NO_CLAIM", "LEGACY" ]<br>    },<br>    "savepointPath" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:handlers:JarRunResponseBody",<br>  "properties" : {<br>    "jobid" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobmanager/config** [Anchor link for: jobmanager config](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager-config) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the cluster configuration. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "array",<br>  "items" : {<br>    "type" : "object",<br>    "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ConfigurationInfoEntry",<br>    "properties" : {<br>      "key" : {<br>        "type" : "string"<br>      },<br>      "value" : {<br>        "type" : "string"<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobmanager/environment** [Anchor link for: jobmanager environment](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager-environment) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the jobmanager environment. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:EnvironmentInfo",<br>  "properties" : {<br>    "classpath" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "string"<br>      }<br>    },<br>    "jvm" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:EnvironmentInfo:JVMInfo",<br>      "properties" : {<br>        "arch" : {<br>          "type" : "string"<br>        },<br>        "options" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "string"<br>          }<br>        },<br>        "version" : {<br>          "type" : "string"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobmanager/logs** [Anchor link for: jobmanager logs](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager-logs) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the list of log files on the JobManager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogListInfo",<br>  "properties" : {<br>    "logs" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogInfo",<br>        "properties" : {<br>          "mtime" : {<br>            "type" : "integer"<br>          },<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "size" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobmanager/metrics** [Anchor link for: jobmanager metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to job manager metrics. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobmanager/thread-dump** [Anchor link for: jobmanager thread dump](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobmanager-thread-dump) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the thread dump of the JobManager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ThreadDumpInfo",<br>  "properties" : {<br>    "threadInfos" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ThreadDumpInfo:ThreadInfo",<br>        "properties" : {<br>          "stringifiedThreadInfo" : {<br>            "type" : "string"<br>          },<br>          "threadName" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs** [Anchor link for: jobs](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs) |
| Verb: `GET` | Response code: `200 OK` |
| Returns an overview over all jobs and their current state. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:messages:webmonitor:JobIdsWithStatusOverview",<br>  "properties" : {<br>    "jobs" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:messages:webmonitor:JobIdsWithStatusOverview:JobIdWithStatus",<br>        "properties" : {<br>          "id" : {<br>            "type" : "any"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "INITIALIZING", "CREATED", "RUNNING", "FAILING", "FAILED", "CANCELLING", "CANCELED", "FINISHED", "RESTARTING", "SUSPENDED", "RECONCILING" ]<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/metrics** [Anchor link for: jobs metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to aggregated job metrics. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics.<br>- `agg` (optional): Comma-separated list of aggregation modes which should be calculated. Available aggregations are: "min, max, sum, avg, skew".<br>- `jobs` (optional): Comma-separated list of 32-character hexadecimal strings to select specific jobs. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/overview** [Anchor link for: jobs overview](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-overview) |
| Verb: `GET` | Response code: `200 OK` |
| Returns an overview over all jobs. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:messages:webmonitor:MultipleJobsDetails",<br>  "properties" : {<br>    "jobs" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:messages:webmonitor:JobDetails",<br>        "properties" : {<br>          "duration" : {<br>            "type" : "integer"<br>          },<br>          "end-time" : {<br>            "type" : "integer"<br>          },<br>          "jid" : {<br>            "type" : "any"<br>          },<br>          "last-modification" : {<br>            "type" : "integer"<br>          },<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "pending-operators" : {<br>            "type" : "integer"<br>          },<br>          "start-time" : {<br>            "type" : "integer"<br>          },<br>          "state" : {<br>            "type" : "string",<br>            "enum" : [ "INITIALIZING", "CREATED", "RUNNING", "FAILING", "FAILED", "CANCELLING", "CANCELED", "FINISHED", "RESTARTING", "SUSPENDED", "RECONCILING" ]<br>          },<br>          "tasks" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid** [Anchor link for: jobs jobid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details of a job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:JobDetailsInfo",<br>  "properties" : {<br>    "duration" : {<br>      "type" : "integer"<br>    },<br>    "end-time" : {<br>      "type" : "integer"<br>    },<br>    "isStoppable" : {<br>      "type" : "boolean"<br>    },<br>    "jid" : {<br>      "type" : "any"<br>    },<br>    "job-type" : {<br>      "type" : "string",<br>      "enum" : [ "BATCH", "STREAMING" ]<br>    },<br>    "maxParallelism" : {<br>      "type" : "integer"<br>    },<br>    "name" : {<br>      "type" : "string"<br>    },<br>    "now" : {<br>      "type" : "integer"<br>    },<br>    "pending-operators" : {<br>      "type" : "integer"<br>    },<br>    "plan" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan",<br>      "properties" : {<br>        "jid" : {<br>          "type" : "string"<br>        },<br>        "name" : {<br>          "type" : "string"<br>        },<br>        "nodes" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node",<br>            "properties" : {<br>              "description" : {<br>                "type" : "string"<br>              },<br>              "id" : {<br>                "type" : "string"<br>              },<br>              "inputs" : {<br>                "type" : "array",<br>                "items" : {<br>                  "type" : "object",<br>                  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node:Input",<br>                  "properties" : {<br>                    "caching" : {<br>                      "type" : "string"<br>                    },<br>                    "exchange" : {<br>                      "type" : "string"<br>                    },<br>                    "id" : {<br>                      "type" : "string"<br>                    },<br>                    "local_strategy" : {<br>                      "type" : "string"<br>                    },<br>                    "num" : {<br>                      "type" : "integer"<br>                    },<br>                    "ship_strategy" : {<br>                      "type" : "string"<br>                    }<br>                  }<br>                }<br>              },<br>              "operator" : {<br>                "type" : "string"<br>              },<br>              "operator_strategy" : {<br>                "type" : "string"<br>              },<br>              "optimizer_properties" : {<br>                "type" : "object",<br>                "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:RawJson"<br>              },<br>              "parallelism" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        },<br>        "type" : {<br>          "type" : "string"<br>        }<br>      }<br>    },<br>    "start-time" : {<br>      "type" : "integer"<br>    },<br>    "state" : {<br>      "type" : "string",<br>      "enum" : [ "INITIALIZING", "CREATED", "RUNNING", "FAILING", "FAILED", "CANCELLING", "CANCELED", "FINISHED", "RESTARTING", "SUSPENDED", "RECONCILING" ]<br>    },<br>    "status-counts" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "integer"<br>      }<br>    },<br>    "stream-graph" : {<br>      "type" : "object",<br>      "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:RawJson"<br>    },<br>    "timestamps" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "integer"<br>      }<br>    },<br>    "vertices" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:JobDetailsInfo:JobVertexDetailsInfo",<br>        "properties" : {<br>          "duration" : {<br>            "type" : "integer"<br>          },<br>          "end-time" : {<br>            "type" : "integer"<br>          },<br>          "id" : {<br>            "type" : "any"<br>          },<br>          "maxParallelism" : {<br>            "type" : "integer"<br>          },<br>          "metrics" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:metrics:IOMetricsInfo",<br>            "properties" : {<br>              "accumulated-backpressured-time" : {<br>                "type" : "integer"<br>              },<br>              "accumulated-busy-time" : {<br>                "type" : "number"<br>              },<br>              "accumulated-idle-time" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "read-records" : {<br>                "type" : "integer"<br>              },<br>              "read-records-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-bytes" : {<br>                "type" : "integer"<br>              },<br>              "write-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-records" : {<br>                "type" : "integer"<br>              },<br>              "write-records-complete" : {<br>                "type" : "boolean"<br>              }<br>            }<br>          },<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "parallelism" : {<br>            "type" : "integer"<br>          },<br>          "slotSharingGroupId" : {<br>            "type" : "any"<br>          },<br>          "start-time" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING", "INITIALIZING" ]<br>          },<br>          "tasks" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid** [Anchor link for: jobs jobid 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-1) |
| Verb: `PATCH` | Response code: `202 Accepted` |
| Terminates a job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Query parameters |
| - `mode` (optional): String value that specifies the termination mode. The only supported value is: "cancel". |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/accumulators** [Anchor link for: jobs jobid accumulators](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-accumulators) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the accumulators for all tasks of a job, aggregated across the respective subtasks. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Query parameters |
| - `includeSerializedValue` (optional): Boolean value that specifies whether serialized user task accumulators should be included in the response. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobAccumulatorsInfo",<br>  "properties" : {<br>    "job-accumulators" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobAccumulatorsInfo:JobAccumulator"<br>      }<br>    },<br>    "serialized-user-task-accumulators" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "any"<br>      }<br>    },<br>    "user-task-accumulators" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobAccumulatorsInfo:UserTaskAccumulator",<br>        "properties" : {<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "type" : {<br>            "type" : "string"<br>          },<br>          "value" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints** [Anchor link for: jobs jobid checkpoints](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints) |
| Verb: `GET` | Response code: `200 OK` |
| Returns checkpointing statistics for a job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointingStatistics",<br>  "properties" : {<br>    "counts" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointingStatistics:Counts",<br>      "properties" : {<br>        "completed" : {<br>          "type" : "integer"<br>        },<br>        "failed" : {<br>          "type" : "integer"<br>        },<br>        "in_progress" : {<br>          "type" : "integer"<br>        },<br>        "restored" : {<br>          "type" : "integer"<br>        },<br>        "total" : {<br>          "type" : "integer"<br>        }<br>      }<br>    },<br>    "history" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointStatistics",<br>        "properties" : {<br>          "alignment_buffered" : {<br>            "type" : "integer"<br>          },<br>          "checkpoint_type" : {<br>            "type" : "string",<br>            "enum" : [ "CHECKPOINT", "UNALIGNED_CHECKPOINT", "SAVEPOINT", "SYNC_SAVEPOINT" ]<br>          },<br>          "checkpointed_size" : {<br>            "type" : "integer"<br>          },<br>          "end_to_end_duration" : {<br>            "type" : "integer"<br>          },<br>          "id" : {<br>            "type" : "integer"<br>          },<br>          "is_savepoint" : {<br>            "type" : "boolean"<br>          },<br>          "latest_ack_timestamp" : {<br>            "type" : "integer"<br>          },<br>          "num_acknowledged_subtasks" : {<br>            "type" : "integer"<br>          },<br>          "num_subtasks" : {<br>            "type" : "integer"<br>          },<br>          "persisted_data" : {<br>            "type" : "integer"<br>          },<br>          "processed_data" : {<br>            "type" : "integer"<br>          },<br>          "savepointFormat" : {<br>            "type" : "string"<br>          },<br>          "state_size" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>          },<br>          "tasks" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatistics"<br>            }<br>          },<br>          "trigger_timestamp" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    },<br>    "latest" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointingStatistics:LatestCheckpoints",<br>      "properties" : {<br>        "completed" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointStatistics:CompletedCheckpointStatistics",<br>          "properties" : {<br>            "alignment_buffered" : {<br>              "type" : "integer"<br>            },<br>            "checkpoint_type" : {<br>              "type" : "string",<br>              "enum" : [ "CHECKPOINT", "UNALIGNED_CHECKPOINT", "SAVEPOINT", "SYNC_SAVEPOINT" ]<br>            },<br>            "checkpointed_size" : {<br>              "type" : "integer"<br>            },<br>            "discarded" : {<br>              "type" : "boolean"<br>            },<br>            "end_to_end_duration" : {<br>              "type" : "integer"<br>            },<br>            "external_path" : {<br>              "type" : "string"<br>            },<br>            "id" : {<br>              "type" : "integer"<br>            },<br>            "is_savepoint" : {<br>              "type" : "boolean"<br>            },<br>            "latest_ack_timestamp" : {<br>              "type" : "integer"<br>            },<br>            "num_acknowledged_subtasks" : {<br>              "type" : "integer"<br>            },<br>            "num_subtasks" : {<br>              "type" : "integer"<br>            },<br>            "persisted_data" : {<br>              "type" : "integer"<br>            },<br>            "processed_data" : {<br>              "type" : "integer"<br>            },<br>            "savepointFormat" : {<br>              "type" : "string"<br>            },<br>            "state_size" : {<br>              "type" : "integer"<br>            },<br>            "status" : {<br>              "type" : "string",<br>              "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>            },<br>            "tasks" : {<br>              "type" : "object",<br>              "additionalProperties" : {<br>                "type" : "object",<br>                "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatistics",<br>                "properties" : {<br>                  "alignment_buffered" : {<br>                    "type" : "integer"<br>                  },<br>                  "checkpointed_size" : {<br>                    "type" : "integer"<br>                  },<br>                  "end_to_end_duration" : {<br>                    "type" : "integer"<br>                  },<br>                  "id" : {<br>                    "type" : "integer"<br>                  },<br>                  "latest_ack_timestamp" : {<br>                    "type" : "integer"<br>                  },<br>                  "num_acknowledged_subtasks" : {<br>                    "type" : "integer"<br>                  },<br>                  "num_subtasks" : {<br>                    "type" : "integer"<br>                  },<br>                  "persisted_data" : {<br>                    "type" : "integer"<br>                  },<br>                  "processed_data" : {<br>                    "type" : "integer"<br>                  },<br>                  "state_size" : {<br>                    "type" : "integer"<br>                  },<br>                  "status" : {<br>                    "type" : "string",<br>                    "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>                  }<br>                }<br>              }<br>            },<br>            "trigger_timestamp" : {<br>              "type" : "integer"<br>            }<br>          }<br>        },<br>        "failed" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointStatistics:FailedCheckpointStatistics",<br>          "properties" : {<br>            "alignment_buffered" : {<br>              "type" : "integer"<br>            },<br>            "checkpoint_type" : {<br>              "type" : "string",<br>              "enum" : [ "CHECKPOINT", "UNALIGNED_CHECKPOINT", "SAVEPOINT", "SYNC_SAVEPOINT" ]<br>            },<br>            "checkpointed_size" : {<br>              "type" : "integer"<br>            },<br>            "end_to_end_duration" : {<br>              "type" : "integer"<br>            },<br>            "failure_message" : {<br>              "type" : "string"<br>            },<br>            "failure_timestamp" : {<br>              "type" : "integer"<br>            },<br>            "id" : {<br>              "type" : "integer"<br>            },<br>            "is_savepoint" : {<br>              "type" : "boolean"<br>            },<br>            "latest_ack_timestamp" : {<br>              "type" : "integer"<br>            },<br>            "num_acknowledged_subtasks" : {<br>              "type" : "integer"<br>            },<br>            "num_subtasks" : {<br>              "type" : "integer"<br>            },<br>            "persisted_data" : {<br>              "type" : "integer"<br>            },<br>            "processed_data" : {<br>              "type" : "integer"<br>            },<br>            "savepointFormat" : {<br>              "type" : "string"<br>            },<br>            "state_size" : {<br>              "type" : "integer"<br>            },<br>            "status" : {<br>              "type" : "string",<br>              "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>            },<br>            "tasks" : {<br>              "type" : "object",<br>              "additionalProperties" : {<br>                "type" : "object",<br>                "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatistics"<br>              }<br>            },<br>            "trigger_timestamp" : {<br>              "type" : "integer"<br>            }<br>          }<br>        },<br>        "restored" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointingStatistics:RestoredCheckpointStatistics",<br>          "properties" : {<br>            "external_path" : {<br>              "type" : "string"<br>            },<br>            "id" : {<br>              "type" : "integer"<br>            },<br>            "is_savepoint" : {<br>              "type" : "boolean"<br>            },<br>            "restore_timestamp" : {<br>              "type" : "integer"<br>            }<br>          }<br>        },<br>        "savepoint" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointStatistics:CompletedCheckpointStatistics"<br>        }<br>      }<br>    },<br>    "summary" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointingStatistics:Summary",<br>      "properties" : {<br>        "alignment_buffered" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "checkpointed_size" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto",<br>          "properties" : {<br>            "avg" : {<br>              "type" : "integer"<br>            },<br>            "max" : {<br>              "type" : "integer"<br>            },<br>            "min" : {<br>              "type" : "integer"<br>            },<br>            "p50" : {<br>              "type" : "number"<br>            },<br>            "p90" : {<br>              "type" : "number"<br>            },<br>            "p95" : {<br>              "type" : "number"<br>            },<br>            "p99" : {<br>              "type" : "number"<br>            },<br>            "p999" : {<br>              "type" : "number"<br>            }<br>          }<br>        },<br>        "end_to_end_duration" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "persisted_data" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "processed_data" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "state_size" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints** [Anchor link for: jobs jobid checkpoints 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints-1) |
| Verb: `POST` | Response code: `202 Accepted` |
| Triggers a checkpoint. The 'checkpointType' parameter does not support 'INCREMENTAL' option for now. See FLINK-33723. This async operation would return a 'triggerid' for further query identifier. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointTriggerRequestBody",<br>  "properties" : {<br>    "checkpointType" : {<br>      "type" : "string",<br>      "enum" : [ "CONFIGURED", "FULL", "INCREMENTAL" ]<br>    },<br>    "triggerId" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints/config** [Anchor link for: jobs jobid checkpoints config](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints-config) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the checkpointing configuration. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointConfigInfo",<br>  "properties" : {<br>    "aligned_checkpoint_timeout" : {<br>      "type" : "integer"<br>    },<br>    "changelog_periodic_materialization_interval" : {<br>      "type" : "integer"<br>    },<br>    "changelog_storage" : {<br>      "type" : "string"<br>    },<br>    "checkpoint_storage" : {<br>      "type" : "string"<br>    },<br>    "checkpoints_after_tasks_finish" : {<br>      "type" : "boolean"<br>    },<br>    "externalization" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointConfigInfo:ExternalizedCheckpointInfo",<br>      "properties" : {<br>        "delete_on_cancellation" : {<br>          "type" : "boolean"<br>        },<br>        "enabled" : {<br>          "type" : "boolean"<br>        }<br>      }<br>    },<br>    "interval" : {<br>      "type" : "integer"<br>    },<br>    "max_concurrent" : {<br>      "type" : "integer"<br>    },<br>    "min_pause" : {<br>      "type" : "integer"<br>    },<br>    "mode" : {<br>      "type" : "any"<br>    },<br>    "state_backend" : {<br>      "type" : "string"<br>    },<br>    "state_changelog_enabled" : {<br>      "type" : "boolean"<br>    },<br>    "timeout" : {<br>      "type" : "integer"<br>    },<br>    "tolerable_failed_checkpoints" : {<br>      "type" : "integer"<br>    },<br>    "unaligned_checkpoints" : {<br>      "type" : "boolean"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints/details/:checkpointid** [Anchor link for: jobs jobid checkpoints details checkpointid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints-details-checkpointid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details for a checkpoint. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `checkpointid` \- Long value that identifies a checkpoint. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointStatistics",<br>  "properties" : {<br>    "alignment_buffered" : {<br>      "type" : "integer"<br>    },<br>    "checkpoint_type" : {<br>      "type" : "string",<br>      "enum" : [ "CHECKPOINT", "UNALIGNED_CHECKPOINT", "SAVEPOINT", "SYNC_SAVEPOINT" ]<br>    },<br>    "checkpointed_size" : {<br>      "type" : "integer"<br>    },<br>    "end_to_end_duration" : {<br>      "type" : "integer"<br>    },<br>    "id" : {<br>      "type" : "integer"<br>    },<br>    "is_savepoint" : {<br>      "type" : "boolean"<br>    },<br>    "latest_ack_timestamp" : {<br>      "type" : "integer"<br>    },<br>    "num_acknowledged_subtasks" : {<br>      "type" : "integer"<br>    },<br>    "num_subtasks" : {<br>      "type" : "integer"<br>    },<br>    "persisted_data" : {<br>      "type" : "integer"<br>    },<br>    "processed_data" : {<br>      "type" : "integer"<br>    },<br>    "savepointFormat" : {<br>      "type" : "string"<br>    },<br>    "state_size" : {<br>      "type" : "integer"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>    },<br>    "tasks" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatistics",<br>        "properties" : {<br>          "alignment_buffered" : {<br>            "type" : "integer"<br>          },<br>          "checkpointed_size" : {<br>            "type" : "integer"<br>          },<br>          "end_to_end_duration" : {<br>            "type" : "integer"<br>          },<br>          "id" : {<br>            "type" : "integer"<br>          },<br>          "latest_ack_timestamp" : {<br>            "type" : "integer"<br>          },<br>          "num_acknowledged_subtasks" : {<br>            "type" : "integer"<br>          },<br>          "num_subtasks" : {<br>            "type" : "integer"<br>          },<br>          "persisted_data" : {<br>            "type" : "integer"<br>          },<br>          "processed_data" : {<br>            "type" : "integer"<br>          },<br>          "state_size" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>          }<br>        }<br>      }<br>    },<br>    "trigger_timestamp" : {<br>      "type" : "integer"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints/details/:checkpointid/subtasks/:vertexid** [Anchor link for: jobs jobid checkpoints details checkpointid subtasks vertexid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints-details-checkpointid-subtasks-vertexid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns checkpoint statistics for a task and its subtasks. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `checkpointid` \- Long value that identifies a checkpoint.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatisticsWithSubtaskDetails",<br>  "properties" : {<br>    "alignment_buffered" : {<br>      "type" : "integer"<br>    },<br>    "checkpointed_size" : {<br>      "type" : "integer"<br>    },<br>    "end_to_end_duration" : {<br>      "type" : "integer"<br>    },<br>    "id" : {<br>      "type" : "integer"<br>    },<br>    "latest_ack_timestamp" : {<br>      "type" : "integer"<br>    },<br>    "num_acknowledged_subtasks" : {<br>      "type" : "integer"<br>    },<br>    "num_subtasks" : {<br>      "type" : "integer"<br>    },<br>    "persisted_data" : {<br>      "type" : "integer"<br>    },<br>    "processed_data" : {<br>      "type" : "integer"<br>    },<br>    "state_size" : {<br>      "type" : "integer"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "IN_PROGRESS", "COMPLETED", "FAILED" ]<br>    },<br>    "subtasks" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:SubtaskCheckpointStatistics",<br>        "properties" : {<br>          "index" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    },<br>    "summary" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatisticsWithSubtaskDetails:Summary",<br>      "properties" : {<br>        "alignment" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatisticsWithSubtaskDetails:CheckpointAlignment",<br>          "properties" : {<br>            "buffered" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            },<br>            "duration" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            },<br>            "persisted" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            },<br>            "processed" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            }<br>          }<br>        },<br>        "checkpoint_duration" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:TaskCheckpointStatisticsWithSubtaskDetails:CheckpointDuration",<br>          "properties" : {<br>            "async" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            },<br>            "sync" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>            }<br>          }<br>        },<br>        "checkpointed_size" : {<br>          "type" : "object",<br>          "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto",<br>          "properties" : {<br>            "avg" : {<br>              "type" : "integer"<br>            },<br>            "max" : {<br>              "type" : "integer"<br>            },<br>            "min" : {<br>              "type" : "integer"<br>            },<br>            "p50" : {<br>              "type" : "number"<br>            },<br>            "p90" : {<br>              "type" : "number"<br>            },<br>            "p95" : {<br>              "type" : "number"<br>            },<br>            "p99" : {<br>              "type" : "number"<br>            },<br>            "p999" : {<br>              "type" : "number"<br>            }<br>          }<br>        },<br>        "end_to_end_duration" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "start_delay" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        },<br>        "state_size" : {<br>          "type" : "object",<br>          "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:util.stats:StatsSummaryDto"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/checkpoints/:triggerid** [Anchor link for: jobs jobid checkpoints triggerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-checkpoints-triggerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the status of a checkpoint trigger operation. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `triggerid` \- 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationResult",<br>  "properties" : {<br>    "operation" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:checkpoints:CheckpointInfo",<br>      "properties" : {<br>        "checkpointId" : {<br>          "type" : "integer"<br>        },<br>        "failureCause" : {<br>          "type" : "any"<br>        }<br>      }<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/clientHeartbeat** [Anchor link for: jobs jobid clientheartbeat](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-clientheartbeat) |
| Verb: `PATCH` | Response code: `202 Accepted` |
| Report the jobClient's aliveness. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobClientHeartbeatRequestBody",<br>  "properties" : {<br>    "expiredTimestamp" : {<br>      "type" : "integer"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/config** [Anchor link for: jobs jobid config](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-config) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the configuration of a job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/exceptions** [Anchor link for: jobs jobid exceptions](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-exceptions) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the most recent exceptions that have been handled by Flink for this job. The 'exceptionHistory.truncated' flag defines whether exceptions were filtered out through the GET parameter. The backend collects only a specific amount of most recent exceptions per job. This can be configured through web.exception-history-size in the Flink configuration. The following first-level members are deprecated: 'root-exception', 'timestamp', 'all-exceptions', and 'truncated'. Use the data provided through 'exceptionHistory', instead. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Query parameters |
| - `maxExceptions` (optional): Comma-separated list of integer values that specifies the upper limit of exceptions to return.<br>- `failureLabelFilter` (optional): Collection of string values working as a filter in the form of \`key:value\` pairs allowing only exceptions with ALL of the specified failure labels to be returned. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobExceptionsInfoWithHistory",<br>  "properties" : {<br>    "exceptionHistory" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobExceptionsInfoWithHistory:JobExceptionHistory",<br>      "properties" : {<br>        "entries" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobExceptionsInfoWithHistory:RootExceptionInfo",<br>            "properties" : {<br>              "concurrentExceptions" : {<br>                "type" : "array",<br>                "items" : {<br>                  "type" : "object",<br>                  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobExceptionsInfoWithHistory:ExceptionInfo",<br>                  "properties" : {<br>                    "endpoint" : {<br>                      "type" : "string"<br>                    },<br>                    "exceptionName" : {<br>                      "type" : "string"<br>                    },<br>                    "failureLabels" : {<br>                      "type" : "object",<br>                      "additionalProperties" : {<br>                        "type" : "string"<br>                      }<br>                    },<br>                    "stacktrace" : {<br>                      "type" : "string"<br>                    },<br>                    "taskManagerId" : {<br>                      "type" : "string"<br>                    },<br>                    "taskName" : {<br>                      "type" : "string"<br>                    },<br>                    "timestamp" : {<br>                      "type" : "integer"<br>                    }<br>                  }<br>                }<br>              },<br>              "endpoint" : {<br>                "type" : "string"<br>              },<br>              "exceptionName" : {<br>                "type" : "string"<br>              },<br>              "failureLabels" : {<br>                "type" : "object",<br>                "additionalProperties" : {<br>                  "type" : "string"<br>                }<br>              },<br>              "stacktrace" : {<br>                "type" : "string"<br>              },<br>              "taskManagerId" : {<br>                "type" : "string"<br>              },<br>              "taskName" : {<br>                "type" : "string"<br>              },<br>              "timestamp" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        },<br>        "truncated" : {<br>          "type" : "boolean"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/execution-result** [Anchor link for: jobs jobid execution result](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-execution-result) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:JobExecutionResultResponseBody",<br>  "properties" : {<br>    "job-execution-result" : {<br>      "type" : "any"<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "required" : true,<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/jobmanager/config** [Anchor link for: jobs jobid jobmanager config](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-jobmanager-config) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the jobmanager's configuration of a specific job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "array",<br>  "items" : {<br>    "type" : "object",<br>    "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ConfigurationInfoEntry",<br>    "properties" : {<br>      "key" : {<br>        "type" : "string"<br>      },<br>      "value" : {<br>        "type" : "string"<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/jobmanager/environment** [Anchor link for: jobs jobid jobmanager environment](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-jobmanager-environment) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the jobmanager's environment of a specific job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:EnvironmentInfo",<br>  "properties" : {<br>    "classpath" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "string"<br>      }<br>    },<br>    "jvm" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:EnvironmentInfo:JVMInfo",<br>      "properties" : {<br>        "arch" : {<br>          "type" : "string"<br>        },<br>        "options" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "string"<br>          }<br>        },<br>        "version" : {<br>          "type" : "string"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/jobmanager/log-url** [Anchor link for: jobs jobid jobmanager log url](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-jobmanager-log-url) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the log url of jobmanager of a specific job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogUrlResponse",<br>  "properties" : {<br>    "url" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/metrics** [Anchor link for: jobs jobid metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to job metrics. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/plan** [Anchor link for: jobs jobid plan](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-plan) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the dataflow plan of a job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo",<br>  "properties" : {<br>    "plan" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan",<br>      "properties" : {<br>        "jid" : {<br>          "type" : "string"<br>        },<br>        "name" : {<br>          "type" : "string"<br>        },<br>        "nodes" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node",<br>            "properties" : {<br>              "description" : {<br>                "type" : "string"<br>              },<br>              "id" : {<br>                "type" : "string"<br>              },<br>              "inputs" : {<br>                "type" : "array",<br>                "items" : {<br>                  "type" : "object",<br>                  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:Plan:Node:Input",<br>                  "properties" : {<br>                    "caching" : {<br>                      "type" : "string"<br>                    },<br>                    "exchange" : {<br>                      "type" : "string"<br>                    },<br>                    "id" : {<br>                      "type" : "string"<br>                    },<br>                    "local_strategy" : {<br>                      "type" : "string"<br>                    },<br>                    "num" : {<br>                      "type" : "integer"<br>                    },<br>                    "ship_strategy" : {<br>                      "type" : "string"<br>                    }<br>                  }<br>                }<br>              },<br>              "operator" : {<br>                "type" : "string"<br>              },<br>              "operator_strategy" : {<br>                "type" : "string"<br>              },<br>              "optimizer_properties" : {<br>                "type" : "object",<br>                "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobPlanInfo:RawJson"<br>              },<br>              "parallelism" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        },<br>        "type" : {<br>          "type" : "string"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/rescaling** [Anchor link for: jobs jobid rescaling](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-rescaling) |
| Verb: `PATCH` | Response code: `200 OK` |
| Triggers the rescaling of a job. This async operation would return a 'triggerid' for further query identifier. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Query parameters |
| - `parallelism` (mandatory): Positive integer value that specifies the desired parallelism. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/rescaling/:triggerid** [Anchor link for: jobs jobid rescaling triggerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-rescaling-triggerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the status of a rescaling operation. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `triggerid` \- 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationResult",<br>  "properties" : {<br>    "operation" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationInfo",<br>      "properties" : {<br>        "failure-cause" : {<br>          "type" : "any"<br>        }<br>      }<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/resource-requirements** [Anchor link for: jobs jobid resource requirements](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-resource-requirements) |
| Verb: `GET` | Response code: `200 OK` |
| Request details on the job's resource requirements. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:JobResourceRequirementsBody",<br>  "additionalProperties" : {<br>    "type" : "object",<br>    "id" : "urn:jsonschema:org:apache:flink:runtime:jobgraph:JobVertexResourceRequirements",<br>    "properties" : {<br>      "parallelism" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:jobgraph:JobVertexResourceRequirements:Parallelism",<br>        "properties" : {<br>          "lowerBound" : {<br>            "type" : "integer"<br>          },<br>          "upperBound" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/resource-requirements** [Anchor link for: jobs jobid resource requirements 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-resource-requirements-1) |
| Verb: `PUT` | Response code: `200 OK` |
| Request to update job's resource requirements. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:JobResourceRequirementsBody",<br>  "additionalProperties" : {<br>    "type" : "object",<br>    "id" : "urn:jsonschema:org:apache:flink:runtime:jobgraph:JobVertexResourceRequirements",<br>    "properties" : {<br>      "parallelism" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:jobgraph:JobVertexResourceRequirements:Parallelism",<br>        "properties" : {<br>          "lowerBound" : {<br>            "type" : "integer"<br>          },<br>          "upperBound" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/savepoints** [Anchor link for: jobs jobid savepoints](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-savepoints) |
| Verb: `POST` | Response code: `202 Accepted` |
| Triggers a savepoint, and optionally cancels the job afterwards. This async operation would return a 'triggerid' for further query identifier. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:savepoints:SavepointTriggerRequestBody",<br>  "properties" : {<br>    "cancel-job" : {<br>      "type" : "boolean"<br>    },<br>    "formatType" : {<br>      "type" : "string",<br>      "enum" : [ "CANONICAL", "NATIVE" ]<br>    },<br>    "target-directory" : {<br>      "type" : "string"<br>    },<br>    "triggerId" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/savepoints/:triggerid** [Anchor link for: jobs jobid savepoints triggerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-savepoints-triggerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the status of a savepoint operation. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `triggerid` \- 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationResult",<br>  "properties" : {<br>    "operation" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:savepoints:SavepointInfo",<br>      "properties" : {<br>        "failure-cause" : {<br>          "type" : "any"<br>        },<br>        "location" : {<br>          "type" : "string"<br>        }<br>      }<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/status** [Anchor link for: jobs jobid status](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-status) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the current status of a job execution. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:messages:webmonitor:JobStatusInfo",<br>  "properties" : {<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "INITIALIZING", "CREATED", "RUNNING", "FAILING", "FAILED", "CANCELLING", "CANCELED", "FINISHED", "RESTARTING", "SUSPENDED", "RECONCILING" ]<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/stop** [Anchor link for: jobs jobid stop](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-stop) |
| Verb: `POST` | Response code: `202 Accepted` |
| Stops a job with a savepoint. Optionally, it can also emit a MAX\_WATERMARK before taking the savepoint to flush out any state waiting for timers to fire. This async operation would return a 'triggerid' for further query identifier. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:savepoints:stop:StopWithSavepointRequestBody",<br>  "properties" : {<br>    "drain" : {<br>      "type" : "boolean"<br>    },<br>    "formatType" : {<br>      "type" : "string",<br>      "enum" : [ "CANONICAL", "NATIVE" ]<br>    },<br>    "targetDirectory" : {<br>      "type" : "string"<br>    },<br>    "triggerId" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/taskmanagers/:taskmanagerid/log-url** [Anchor link for: jobs jobid taskmanagers taskmanagerid log url](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-taskmanagers-taskmanagerid-log-url) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the log url of jobmanager of a specific job. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `taskmanagerid` \- 32-character hexadecimal string that identifies a task manager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogUrlResponse",<br>  "properties" : {<br>    "url" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid** [Anchor link for: jobs jobid vertices vertexid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details for a task, with a summary for each of its subtasks. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexDetailsInfo",<br>  "properties" : {<br>    "aggregated" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:AggregatedTaskDetailsInfo",<br>      "properties" : {<br>        "metrics" : {<br>          "type" : "object",<br>          "additionalProperties" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          }<br>        },<br>        "status-duration" : {<br>          "type" : "object",<br>          "additionalProperties" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          }<br>        }<br>      }<br>    },<br>    "id" : {<br>      "type" : "any"<br>    },<br>    "maxParallelism" : {<br>      "type" : "integer"<br>    },<br>    "name" : {<br>      "type" : "string"<br>    },<br>    "now" : {<br>      "type" : "integer"<br>    },<br>    "parallelism" : {<br>      "type" : "integer"<br>    },<br>    "subtasks" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo",<br>        "properties" : {<br>          "attempt" : {<br>            "type" : "integer"<br>          },<br>          "duration" : {<br>            "type" : "integer"<br>          },<br>          "end-time" : {<br>            "type" : "integer"<br>          },<br>          "endpoint" : {<br>            "type" : "string"<br>          },<br>          "metrics" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:metrics:IOMetricsInfo",<br>            "properties" : {<br>              "accumulated-backpressured-time" : {<br>                "type" : "integer"<br>              },<br>              "accumulated-busy-time" : {<br>                "type" : "number"<br>              },<br>              "accumulated-idle-time" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "read-records" : {<br>                "type" : "integer"<br>              },<br>              "read-records-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-bytes" : {<br>                "type" : "integer"<br>              },<br>              "write-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-records" : {<br>                "type" : "integer"<br>              },<br>              "write-records-complete" : {<br>                "type" : "boolean"<br>              }<br>            }<br>          },<br>          "other-concurrent-attempts" : {<br>            "type" : "array",<br>            "items" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo"<br>            }<br>          },<br>          "start-time" : {<br>            "type" : "integer"<br>          },<br>          "start_time" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING", "INITIALIZING" ]<br>          },<br>          "status-duration" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          },<br>          "subtask" : {<br>            "type" : "integer"<br>          },<br>          "taskmanager-id" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/accumulators** [Anchor link for: jobs jobid vertices vertexid accumulators](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-accumulators) |
| Verb: `GET` | Response code: `200 OK` |
| Returns user-defined accumulators of a task, aggregated across all subtasks. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexAccumulatorsInfo",<br>  "properties" : {<br>    "id" : {<br>      "type" : "string"<br>    },<br>    "user-accumulators" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:UserAccumulator",<br>        "properties" : {<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "type" : {<br>            "type" : "string"<br>          },<br>          "value" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/backpressure** [Anchor link for: jobs jobid vertices vertexid backpressure](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-backpressure) |
| Verb: `GET` | Response code: `200 OK` |
| Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexBackPressureInfo",<br>  "properties" : {<br>    "backpressure-level" : {<br>      "type" : "string",<br>      "enum" : [ "ok", "low", "high" ]<br>    },<br>    "backpressureLevel" : {<br>      "type" : "string",<br>      "enum" : [ "ok", "low", "high" ]<br>    },<br>    "end-timestamp" : {<br>      "type" : "integer"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "deprecated", "ok" ]<br>    },<br>    "subtasks" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexBackPressureInfo:SubtaskBackPressureInfo",<br>        "properties" : {<br>          "attempt-number" : {<br>            "type" : "integer"<br>          },<br>          "backpressure-level" : {<br>            "type" : "string",<br>            "enum" : [ "ok", "low", "high" ]<br>          },<br>          "backpressureLevel" : {<br>            "type" : "string",<br>            "enum" : [ "ok", "low", "high" ]<br>          },<br>          "busyRatio" : {<br>            "type" : "number"<br>          },<br>          "idleRatio" : {<br>            "type" : "number"<br>          },<br>          "other-concurrent-attempts" : {<br>            "type" : "array",<br>            "items" : {<br>              "type" : "object",<br>              "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexBackPressureInfo:SubtaskBackPressureInfo"<br>            }<br>          },<br>          "ratio" : {<br>            "type" : "number"<br>          },<br>          "subtask" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/flamegraph** [Anchor link for: jobs jobid vertices vertexid flamegraph](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-flamegraph) |
| Verb: `GET` | Response code: `200 OK` |
| Returns flame graph information for a vertex, and may initiate flame graph sampling if necessary. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Query parameters |
| - `type` (optional): String value that specifies the Flame Graph type. Supported options are: "\[FULL, ON\_CPU, OFF\_CPU\]".<br>- `subtaskindex` (optional): Positive integer value that identifies a subtask. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:threadinfo:VertexFlameGraph",<br>  "properties" : {<br>    "data" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:threadinfo:VertexFlameGraph:Node",<br>      "properties" : {<br>        "children" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "$ref" : "urn:jsonschema:org:apache:flink:runtime:webmonitor:threadinfo:VertexFlameGraph:Node"<br>          }<br>        },<br>        "name" : {<br>          "type" : "string"<br>        },<br>        "value" : {<br>          "type" : "integer"<br>        }<br>      }<br>    },<br>    "endTimestamp" : {<br>      "type" : "integer"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/jm-operator-metrics** [Anchor link for: jobs jobid vertices vertexid jm operator metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-jm-operator-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to jobmanager operator metrics. This is an operator that executes on the jobmanager and the coordinator for FLIP 27 sources is one example of such an operator. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/metrics** [Anchor link for: jobs jobid vertices vertexid metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to task metrics. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/accumulators** [Anchor link for: jobs jobid vertices vertexid subtasks accumulators](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-accumulators) |
| Verb: `GET` | Response code: `200 OK` |
| Returns all user-defined accumulators for all subtasks of a task. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtasksAllAccumulatorsInfo",<br>  "properties" : {<br>    "id" : {<br>      "type" : "any"<br>    },<br>    "parallelism" : {<br>      "type" : "integer"<br>    },<br>    "subtasks" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtasksAllAccumulatorsInfo:SubtaskAccumulatorsInfo",<br>        "properties" : {<br>          "attempt" : {<br>            "type" : "integer"<br>          },<br>          "endpoint" : {<br>            "type" : "string"<br>          },<br>          "subtask" : {<br>            "type" : "integer"<br>          },<br>          "user-accumulators" : {<br>            "type" : "array",<br>            "items" : {<br>              "type" : "object",<br>              "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:UserAccumulator",<br>              "properties" : {<br>                "name" : {<br>                  "type" : "string"<br>                },<br>                "type" : {<br>                  "type" : "string"<br>                },<br>                "value" : {<br>                  "type" : "string"<br>                }<br>              }<br>            }<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/metrics** [Anchor link for: jobs jobid vertices vertexid subtasks metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to aggregated subtask metrics. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics.<br>- `agg` (optional): Comma-separated list of aggregation modes which should be calculated. Available aggregations are: "min, max, sum, avg, skew".<br>- `subtasks` (optional): Comma-separated list of integer ranges (e.g. "1,3,5-9") to select specific subtasks. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/:subtaskindex** [Anchor link for: jobs jobid vertices vertexid subtasks subtaskindex](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-subtaskindex) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details of the current or latest execution attempt of a subtask. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex.<br>- `subtaskindex` \- Positive integer value that identifies a subtask. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo",<br>  "properties" : {<br>    "attempt" : {<br>      "type" : "integer"<br>    },<br>    "duration" : {<br>      "type" : "integer"<br>    },<br>    "end-time" : {<br>      "type" : "integer"<br>    },<br>    "endpoint" : {<br>      "type" : "string"<br>    },<br>    "metrics" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:metrics:IOMetricsInfo",<br>      "properties" : {<br>        "accumulated-backpressured-time" : {<br>          "type" : "integer"<br>        },<br>        "accumulated-busy-time" : {<br>          "type" : "number"<br>        },<br>        "accumulated-idle-time" : {<br>          "type" : "integer"<br>        },<br>        "read-bytes" : {<br>          "type" : "integer"<br>        },<br>        "read-bytes-complete" : {<br>          "type" : "boolean"<br>        },<br>        "read-records" : {<br>          "type" : "integer"<br>        },<br>        "read-records-complete" : {<br>          "type" : "boolean"<br>        },<br>        "write-bytes" : {<br>          "type" : "integer"<br>        },<br>        "write-bytes-complete" : {<br>          "type" : "boolean"<br>        },<br>        "write-records" : {<br>          "type" : "integer"<br>        },<br>        "write-records-complete" : {<br>          "type" : "boolean"<br>        }<br>      }<br>    },<br>    "other-concurrent-attempts" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo"<br>      }<br>    },<br>    "start-time" : {<br>      "type" : "integer"<br>    },<br>    "start_time" : {<br>      "type" : "integer"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING", "INITIALIZING" ]<br>    },<br>    "status-duration" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "integer"<br>      }<br>    },<br>    "subtask" : {<br>      "type" : "integer"<br>    },<br>    "taskmanager-id" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/:subtaskindex/attempts/:attempt** [Anchor link for: jobs jobid vertices vertexid subtasks subtaskindex attempts att](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-subtaskindex-attempts-att) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex.<br>- `subtaskindex` \- Positive integer value that identifies a subtask.<br>- `attempt` \- Positive integer value that identifies an execution attempt. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo",<br>  "properties" : {<br>    "attempt" : {<br>      "type" : "integer"<br>    },<br>    "duration" : {<br>      "type" : "integer"<br>    },<br>    "end-time" : {<br>      "type" : "integer"<br>    },<br>    "endpoint" : {<br>      "type" : "string"<br>    },<br>    "metrics" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:metrics:IOMetricsInfo",<br>      "properties" : {<br>        "accumulated-backpressured-time" : {<br>          "type" : "integer"<br>        },<br>        "accumulated-busy-time" : {<br>          "type" : "number"<br>        },<br>        "accumulated-idle-time" : {<br>          "type" : "integer"<br>        },<br>        "read-bytes" : {<br>          "type" : "integer"<br>        },<br>        "read-bytes-complete" : {<br>          "type" : "boolean"<br>        },<br>        "read-records" : {<br>          "type" : "integer"<br>        },<br>        "read-records-complete" : {<br>          "type" : "boolean"<br>        },<br>        "write-bytes" : {<br>          "type" : "integer"<br>        },<br>        "write-bytes-complete" : {<br>          "type" : "boolean"<br>        },<br>        "write-records" : {<br>          "type" : "integer"<br>        },<br>        "write-records-complete" : {<br>          "type" : "boolean"<br>        }<br>      }<br>    },<br>    "other-concurrent-attempts" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptDetailsInfo"<br>      }<br>    },<br>    "start-time" : {<br>      "type" : "integer"<br>    },<br>    "start_time" : {<br>      "type" : "integer"<br>    },<br>    "status" : {<br>      "type" : "string",<br>      "enum" : [ "CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING", "INITIALIZING" ]<br>    },<br>    "status-duration" : {<br>      "type" : "object",<br>      "additionalProperties" : {<br>        "type" : "integer"<br>      }<br>    },<br>    "subtask" : {<br>      "type" : "integer"<br>    },<br>    "taskmanager-id" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/:subtaskindex/attempts/:attempt/accumulators** [Anchor link for: jobs jobid vertices vertexid subtasks subtaskindex attempts att 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-subtaskindex-attempts-att-1) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex.<br>- `subtaskindex` \- Positive integer value that identifies a subtask.<br>- `attempt` \- Positive integer value that identifies an execution attempt. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:SubtaskExecutionAttemptAccumulatorsInfo",<br>  "properties" : {<br>    "attempt" : {<br>      "type" : "integer"<br>    },<br>    "id" : {<br>      "type" : "string"<br>    },<br>    "subtask" : {<br>      "type" : "integer"<br>    },<br>    "user-accumulators" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:UserAccumulator",<br>        "properties" : {<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "type" : {<br>            "type" : "string"<br>          },<br>          "value" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasks/:subtaskindex/metrics** [Anchor link for: jobs jobid vertices vertexid subtasks subtaskindex metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasks-subtaskindex-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to subtask metrics. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex.<br>- `subtaskindex` \- Positive integer value that identifies a subtask. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/subtasktimes** [Anchor link for: jobs jobid vertices vertexid subtasktimes](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-subtasktimes) |
| Verb: `GET` | Response code: `200 OK` |
| Returns time-related information for all subtasks of a task. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:SubtasksTimesInfo",<br>  "properties" : {<br>    "id" : {<br>      "type" : "string"<br>    },<br>    "name" : {<br>      "type" : "string"<br>    },<br>    "now" : {<br>      "type" : "integer"<br>    },<br>    "subtasks" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:SubtasksTimesInfo:SubtaskTimeInfo",<br>        "properties" : {<br>          "duration" : {<br>            "type" : "integer"<br>          },<br>          "endpoint" : {<br>            "type" : "string"<br>          },<br>          "subtask" : {<br>            "type" : "integer"<br>          },<br>          "timestamps" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/taskmanagers** [Anchor link for: jobs jobid vertices vertexid taskmanagers](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-taskmanagers) |
| Verb: `GET` | Response code: `200 OK` |
| Returns task information aggregated by task manager. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexTaskManagersInfo",<br>  "properties" : {<br>    "id" : {<br>      "type" : "any"<br>    },<br>    "name" : {<br>      "type" : "string"<br>    },<br>    "now" : {<br>      "type" : "integer"<br>    },<br>    "taskmanagers" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:JobVertexTaskManagersInfo:TaskManagersInfo",<br>        "properties" : {<br>          "aggregated" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:AggregatedTaskDetailsInfo",<br>            "properties" : {<br>              "metrics" : {<br>                "type" : "object",<br>                "additionalProperties" : {<br>                  "type" : "object",<br>                  "additionalProperties" : {<br>                    "type" : "integer"<br>                  }<br>                }<br>              },<br>              "status-duration" : {<br>                "type" : "object",<br>                "additionalProperties" : {<br>                  "type" : "object",<br>                  "additionalProperties" : {<br>                    "type" : "integer"<br>                  }<br>                }<br>              }<br>            }<br>          },<br>          "duration" : {<br>            "type" : "integer"<br>          },<br>          "end-time" : {<br>            "type" : "integer"<br>          },<br>          "endpoint" : {<br>            "type" : "string"<br>          },<br>          "metrics" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:metrics:IOMetricsInfo",<br>            "properties" : {<br>              "accumulated-backpressured-time" : {<br>                "type" : "integer"<br>              },<br>              "accumulated-busy-time" : {<br>                "type" : "number"<br>              },<br>              "accumulated-idle-time" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes" : {<br>                "type" : "integer"<br>              },<br>              "read-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "read-records" : {<br>                "type" : "integer"<br>              },<br>              "read-records-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-bytes" : {<br>                "type" : "integer"<br>              },<br>              "write-bytes-complete" : {<br>                "type" : "boolean"<br>              },<br>              "write-records" : {<br>                "type" : "integer"<br>              },<br>              "write-records-complete" : {<br>                "type" : "boolean"<br>              }<br>            }<br>          },<br>          "start-time" : {<br>            "type" : "integer"<br>          },<br>          "status" : {<br>            "type" : "string",<br>            "enum" : [ "CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING", "INITIALIZING" ]<br>          },<br>          "status-counts" : {<br>            "type" : "object",<br>            "additionalProperties" : {<br>              "type" : "integer"<br>            }<br>          },<br>          "taskmanager-id" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/jobs/:jobid/vertices/:vertexid/watermarks** [Anchor link for: jobs jobid vertices vertexid watermarks](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#jobs-jobid-vertices-vertexid-watermarks) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the watermarks for all subtasks of a task. |
| Path parameters |
| - `jobid` \- 32-character hexadecimal string value that identifies a job.<br>- `vertexid` \- 32-character hexadecimal string value that identifies a job vertex. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/overview** [Anchor link for: overview 1](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#overview-1) |
| Verb: `GET` | Response code: `200 OK` |
| Returns an overview over the Flink cluster. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:legacy:messages:ClusterOverviewWithVersion",<br>  "properties" : {<br>    "flink-commit" : {<br>      "type" : "string"<br>    },<br>    "flink-version" : {<br>      "type" : "string"<br>    },<br>    "jobs-cancelled" : {<br>      "type" : "integer"<br>    },<br>    "jobs-failed" : {<br>      "type" : "integer"<br>    },<br>    "jobs-finished" : {<br>      "type" : "integer"<br>    },<br>    "jobs-running" : {<br>      "type" : "integer"<br>    },<br>    "slots-available" : {<br>      "type" : "integer"<br>    },<br>    "slots-free-and-blocked" : {<br>      "type" : "integer"<br>    },<br>    "slots-total" : {<br>      "type" : "integer"<br>    },<br>    "taskmanagers" : {<br>      "type" : "integer"<br>    },<br>    "taskmanagers-blocked" : {<br>      "type" : "integer"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/savepoint-disposal** [Anchor link for: savepoint disposal](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#savepoint-disposal) |
| Verb: `POST` | Response code: `200 OK` |
| Triggers the desposal of a savepoint. This async operation would return a 'triggerid' for further query identifier. |
| Request<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:job:savepoints:SavepointDisposalRequest",<br>  "properties" : {<br>    "savepoint-path" : {<br>      "type" : "string"<br>    }<br>  }<br>}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:TriggerResponse",<br>  "properties" : {<br>    "request-id" : {<br>      "type" : "any"<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/savepoint-disposal/:triggerid** [Anchor link for: savepoint disposal triggerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#savepoint-disposal-triggerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the status of a savepoint disposal operation. |
| Path parameters |
| - `triggerid` \- 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationResult",<br>  "properties" : {<br>    "operation" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:handler:async:AsynchronousOperationInfo",<br>      "properties" : {<br>        "failure-cause" : {<br>          "type" : "any"<br>        }<br>      }<br>    },<br>    "status" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:queue:QueueStatus",<br>      "properties" : {<br>        "id" : {<br>          "type" : "string",<br>          "required" : true,<br>          "enum" : [ "IN_PROGRESS", "COMPLETED" ]<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers** [Anchor link for: taskmanagers](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers) |
| Verb: `GET` | Response code: `200 OK` |
| Returns an overview over all task managers. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:TaskManagersInfo",<br>  "properties" : {<br>    "taskmanagers" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:TaskManagerInfo",<br>        "properties" : {<br>          "blocked" : {<br>            "type" : "boolean"<br>          },<br>          "dataPort" : {<br>            "type" : "integer"<br>          },<br>          "freeResource" : {<br>            "type" : "object",<br>            "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ResourceProfileInfo"<br>          },<br>          "freeSlots" : {<br>            "type" : "integer"<br>          },<br>          "hardware" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:instance:HardwareDescription",<br>            "properties" : {<br>              "cpuCores" : {<br>                "type" : "integer"<br>              },<br>              "freeMemory" : {<br>                "type" : "integer"<br>              },<br>              "managedMemory" : {<br>                "type" : "integer"<br>              },<br>              "physicalMemory" : {<br>                "type" : "integer"<br>              }<br>            }<br>          },<br>          "id" : {<br>            "type" : "any"<br>          },<br>          "jmxPort" : {<br>            "type" : "integer"<br>          },<br>          "memoryConfiguration" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:taskexecutor:TaskExecutorMemoryConfiguration",<br>            "properties" : {<br>              "frameworkHeap" : {<br>                "type" : "integer"<br>              },<br>              "frameworkOffHeap" : {<br>                "type" : "integer"<br>              },<br>              "jvmMetaspace" : {<br>                "type" : "integer"<br>              },<br>              "jvmOverhead" : {<br>                "type" : "integer"<br>              },<br>              "managedMemory" : {<br>                "type" : "integer"<br>              },<br>              "networkMemory" : {<br>                "type" : "integer"<br>              },<br>              "taskHeap" : {<br>                "type" : "integer"<br>              },<br>              "taskOffHeap" : {<br>                "type" : "integer"<br>              },<br>              "totalFlinkMemory" : {<br>                "type" : "integer"<br>              },<br>              "totalProcessMemory" : {<br>                "type" : "integer"<br>              }<br>            }<br>          },<br>          "path" : {<br>            "type" : "string"<br>          },<br>          "slotsNumber" : {<br>            "type" : "integer"<br>          },<br>          "timeSinceLastHeartbeat" : {<br>            "type" : "integer"<br>          },<br>          "totalResource" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ResourceProfileInfo",<br>            "properties" : {<br>              "cpuCores" : {<br>                "type" : "number"<br>              },<br>              "extendedResources" : {<br>                "type" : "object",<br>                "additionalProperties" : {<br>                  "type" : "number"<br>                }<br>              },<br>              "managedMemory" : {<br>                "type" : "integer"<br>              },<br>              "networkMemory" : {<br>                "type" : "integer"<br>              },<br>              "taskHeapMemory" : {<br>                "type" : "integer"<br>              },<br>              "taskOffHeapMemory" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers/metrics** [Anchor link for: taskmanagers metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to aggregated task manager metrics. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics.<br>- `agg` (optional): Comma-separated list of aggregation modes which should be calculated. Available aggregations are: "min, max, sum, avg, skew".<br>- `taskmanagers` (optional): Comma-separated list of 32-character hexadecimal strings to select specific task managers. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers/:taskmanagerid** [Anchor link for: taskmanagers taskmanagerid](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers-taskmanagerid) |
| Verb: `GET` | Response code: `200 OK` |
| Returns details for a task manager. |
| Path parameters |
| - `taskmanagerid` \- 32-character hexadecimal string that identifies a task manager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:TaskManagerDetailsInfo",<br>  "properties" : {<br>    "allocatedSlots" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:SlotInfo",<br>        "properties" : {<br>          "jobId" : {<br>            "type" : "any"<br>          },<br>          "resource" : {<br>            "type" : "object",<br>            "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ResourceProfileInfo"<br>          }<br>        }<br>      }<br>    },<br>    "blocked" : {<br>      "type" : "boolean"<br>    },<br>    "dataPort" : {<br>      "type" : "integer"<br>    },<br>    "freeResource" : {<br>      "type" : "object",<br>      "$ref" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ResourceProfileInfo"<br>    },<br>    "freeSlots" : {<br>      "type" : "integer"<br>    },<br>    "hardware" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:instance:HardwareDescription",<br>      "properties" : {<br>        "cpuCores" : {<br>          "type" : "integer"<br>        },<br>        "freeMemory" : {<br>          "type" : "integer"<br>        },<br>        "managedMemory" : {<br>          "type" : "integer"<br>        },<br>        "physicalMemory" : {<br>          "type" : "integer"<br>        }<br>      }<br>    },<br>    "id" : {<br>      "type" : "any"<br>    },<br>    "jmxPort" : {<br>      "type" : "integer"<br>    },<br>    "memoryConfiguration" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:taskexecutor:TaskExecutorMemoryConfiguration",<br>      "properties" : {<br>        "frameworkHeap" : {<br>          "type" : "integer"<br>        },<br>        "frameworkOffHeap" : {<br>          "type" : "integer"<br>        },<br>        "jvmMetaspace" : {<br>          "type" : "integer"<br>        },<br>        "jvmOverhead" : {<br>          "type" : "integer"<br>        },<br>        "managedMemory" : {<br>          "type" : "integer"<br>        },<br>        "networkMemory" : {<br>          "type" : "integer"<br>        },<br>        "taskHeap" : {<br>          "type" : "integer"<br>        },<br>        "taskOffHeap" : {<br>          "type" : "integer"<br>        },<br>        "totalFlinkMemory" : {<br>          "type" : "integer"<br>        },<br>        "totalProcessMemory" : {<br>          "type" : "integer"<br>        }<br>      }<br>    },<br>    "metrics" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:TaskManagerMetricsInfo",<br>      "properties" : {<br>        "directCount" : {<br>          "type" : "integer"<br>        },<br>        "directMax" : {<br>          "type" : "integer"<br>        },<br>        "directUsed" : {<br>          "type" : "integer"<br>        },<br>        "garbageCollectors" : {<br>          "type" : "array",<br>          "items" : {<br>            "type" : "object",<br>            "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:taskmanager:TaskManagerMetricsInfo:GarbageCollectorInfo",<br>            "properties" : {<br>              "count" : {<br>                "type" : "integer"<br>              },<br>              "name" : {<br>                "type" : "string"<br>              },<br>              "time" : {<br>                "type" : "integer"<br>              }<br>            }<br>          }<br>        },<br>        "heapCommitted" : {<br>          "type" : "integer"<br>        },<br>        "heapMax" : {<br>          "type" : "integer"<br>        },<br>        "heapUsed" : {<br>          "type" : "integer"<br>        },<br>        "mappedCount" : {<br>          "type" : "integer"<br>        },<br>        "mappedMax" : {<br>          "type" : "integer"<br>        },<br>        "mappedUsed" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemoryAvailable" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemorySegmentsAvailable" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemorySegmentsTotal" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemorySegmentsUsed" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemoryTotal" : {<br>          "type" : "integer"<br>        },<br>        "nettyShuffleMemoryUsed" : {<br>          "type" : "integer"<br>        },<br>        "nonHeapCommitted" : {<br>          "type" : "integer"<br>        },<br>        "nonHeapMax" : {<br>          "type" : "integer"<br>        },<br>        "nonHeapUsed" : {<br>          "type" : "integer"<br>        }<br>      }<br>    },<br>    "path" : {<br>      "type" : "string"<br>    },<br>    "slotsNumber" : {<br>      "type" : "integer"<br>    },<br>    "timeSinceLastHeartbeat" : {<br>      "type" : "integer"<br>    },<br>    "totalResource" : {<br>      "type" : "object",<br>      "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ResourceProfileInfo",<br>      "properties" : {<br>        "cpuCores" : {<br>          "type" : "number"<br>        },<br>        "extendedResources" : {<br>          "type" : "object",<br>          "additionalProperties" : {<br>            "type" : "number"<br>          }<br>        },<br>        "managedMemory" : {<br>          "type" : "integer"<br>        },<br>        "networkMemory" : {<br>          "type" : "integer"<br>        },<br>        "taskHeapMemory" : {<br>          "type" : "integer"<br>        },<br>        "taskOffHeapMemory" : {<br>          "type" : "integer"<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers/:taskmanagerid/logs** [Anchor link for: taskmanagers taskmanagerid logs](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers-taskmanagerid-logs) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the list of log files on a TaskManager. |
| Path parameters |
| - `taskmanagerid` \- 32-character hexadecimal string that identifies a task manager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogListInfo",<br>  "properties" : {<br>    "logs" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:LogInfo",<br>        "properties" : {<br>          "mtime" : {<br>            "type" : "integer"<br>          },<br>          "name" : {<br>            "type" : "string"<br>          },<br>          "size" : {<br>            "type" : "integer"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers/:taskmanagerid/metrics** [Anchor link for: taskmanagers taskmanagerid metrics](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers-taskmanagerid-metrics) |
| Verb: `GET` | Response code: `200 OK` |
| Provides access to task manager metrics. |
| Path parameters |
| - `taskmanagerid` \- 32-character hexadecimal string that identifies a task manager. |
| Query parameters |
| - `get` (optional): Comma-separated list of string values to select specific metrics. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "any"<br>}<br>``` |

|     |     |
| --- | --- |
| ##### **/taskmanagers/:taskmanagerid/thread-dump** [Anchor link for: taskmanagers taskmanagerid thread dump](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/rest_api/\#taskmanagers-taskmanagerid-thread-dump) |
| Verb: `GET` | Response code: `200 OK` |
| Returns the thread dump of the requested TaskManager. |
| Path parameters |
| - `taskmanagerid` \- 32-character hexadecimal string that identifies a task manager. |
| Request<br>```<br>{}<br>``` |
| Response<br>```<br>{<br>  "type" : "object",<br>  "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ThreadDumpInfo",<br>  "properties" : {<br>    "threadInfos" : {<br>      "type" : "array",<br>      "items" : {<br>        "type" : "object",<br>        "id" : "urn:jsonschema:org:apache:flink:runtime:rest:messages:ThreadDumpInfo:ThreadInfo",<br>        "properties" : {<br>          "stringifiedThreadInfo" : {<br>            "type" : "string"<br>          },<br>          "threadName" : {<br>            "type" : "string"<br>          }<br>        }<br>      }<br>    }<br>  }<br>}<br>``` |