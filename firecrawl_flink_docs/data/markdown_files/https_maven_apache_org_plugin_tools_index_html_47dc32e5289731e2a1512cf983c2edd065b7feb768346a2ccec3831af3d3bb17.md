# Maven Plugin Tools

The Maven Plugin Tools contains the necessary tools to generate repetitive content such as descriptor,
help, and documentation.

| **Module** | **Overview** |
| --- | --- |
| **[maven-plugin-plugin](https://maven.apache.org/plugin-tools/maven-plugin-plugin/index.html)** | Create a Maven plugin descriptor for any mojos found in the source tree, generate reports, create help goal. |
| **[maven-plugin-report-plugin](https://maven.apache.org/plugin-tools/maven-plugin-report-plugin/index.html)** | The Plugin Report Plugin is used to create reports about the plugin being built. |
| [maven-plugin-tools-generators](https://maven.apache.org/plugin-tools/maven-plugin-tools-generators/index.html) | Generators (XML descriptor, help, documentation), used by maven-plugin-plugin to generate content from descriptor extracted from sources. |
| [maven-plugin-tools-api](https://maven.apache.org/plugin-tools/maven-plugin-tools-api/index.html) | Extractor API, used by maven-plugin-plugin to extract Mojo information. |
| [maven-plugin-tools-java](https://maven.apache.org/plugin-tools/maven-plugin-tools-java/index.html) | Extractor for plugins written in Java annotated with Mojo Javadoc Tags. |
| [maven-plugin-tools-annotations](https://maven.apache.org/plugin-tools/maven-plugin-tools-annotations/index.html) | Extractor for plugins written in Java with Java annotations. |
| [maven-plugin-annotations](https://maven.apache.org/plugin-tools/maven-plugin-annotations/index.html) | Provides the Java annotations to use in Mojos. |
| [maven-script](https://maven.apache.org/plugin-tools/maven-script/index.html) (deprecated) | Maven Script Mojo Support lets developer write Maven plugins/goals with scripting languages instead of compiled Java.<br> Deprecated since 3.7.0 |

## Plugin Descriptors

The plugin descriptor is first being generated in memory finally containing some values in HTML format before being persisted into three different XML files.
The formats differ in


- whether they contain all elements or just a limited set of elements defined by the [Plugin Descriptor Spec](https://maven.apache.org/ref/current/maven-plugin-api/plugin.html)
- whether descriptive elements contain HTML or plain text values
- whether they are packaged in the resulting JAR or not

Javadoc tags are in general being resolved and replaced by their XHTML value before they end up in the according plugin descriptor attributes `description` and `deprecated`.
Also javadoc code links via `{@link}` or `@see` are replaced by links to the according Javadoc pages if configured accordingly.
Plaintext is afterwards being generated out of the XHTML (where most XHTML element are just stripped and links are emitted inside angle brackets).



| File name | Allows HTML | Limited Elements | Contained in JAR |
| --- | --- | --- | --- |
| plugin.xml | no | no | yes |
| plugin-help.xml | no | yes | yes |
| plugin-enhanced.xml | no | yes | no (volatile file) |

![](https://maven.apache.org/plugin-tools/images/plugin-descriptors.svg)

## See Also

- [Maven Plugin Testing](https://maven.apache.org/plugin-testing/)
- [Maven Plugin API](https://maven.apache.org/ref/current/maven-plugin-api/)

* * *