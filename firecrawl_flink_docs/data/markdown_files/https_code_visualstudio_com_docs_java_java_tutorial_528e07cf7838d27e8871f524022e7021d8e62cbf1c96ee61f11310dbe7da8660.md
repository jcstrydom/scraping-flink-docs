[Version 1.108](https://code.visualstudio.com/updates) is now available! Read about the new features and fixes from December.

Dismiss this update

# Getting Started with Java in VS Code

This tutorial shows you how to write and run Hello World program in Java with Visual Studio Code. It also covers a few advanced features, which you can explore by reading other documents in this section.

For an overview of the features available for Java in VS Code, see [Java Language Overview](https://code.visualstudio.com/docs/languages/java).

If you run into any issues when following this tutorial, you can contact us by entering an [issue](https://github.com/microsoft/vscode-java-pack/issues).

## [Setting up VS Code for Java development](https://code.visualstudio.com/docs/java/java-tutorial\#_setting-up-vs-code-for-java-development)

### [Coding Pack for Java](https://code.visualstudio.com/docs/java/java-tutorial\#_coding-pack-for-java)

To help you set up quickly, you can install the **Coding Pack for Java**, which includes VS Code, the Java Development Kit (JDK), and essential Java extensions. The Coding Pack can be used as a clean installation, or to update or repair an existing development environment.

[Install the Coding Pack for Java - Windows](https://aka.ms/vscode-java-installer-win)

[Install the Coding Pack for Java - macOS](https://aka.ms/vscode-java-installer-mac)

> **Note**: The Coding Pack for Java is only available for Windows and macOS. For other operating systems, you will need to manually install a JDK, VS Code, and Java extensions.

### [Installing extensions](https://code.visualstudio.com/docs/java/java-tutorial\#_installing-extensions)

If you are an existing VS Code user, you can also add Java support by installing the [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack), which includes these extensions:

- [Language Support for Java™ by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.java)
- [Debugger for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
- [Test Runner for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-test)
- [Maven for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)
- [Project Manager for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-dependency)
- [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

[Install the Extension Pack for Java](vscode:extension/vscjava.vscode-java-pack)

The [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) provides a Quick Start guide and tips for code editing and debugging. It also has a FAQ that answers some frequently asked questions. Use the command **Java: Tips for Beginners** from the Command Palette (Ctrl+Shift+P) to launch the guide.

![Java Getting Started](https://code.visualstudio.com/assets/docs/java/java-tutorial/getting-started.png)

You can also install extensions separately. The **Extensions Guide** is provided to help you. You can launch the guide with the **Java: Extensions Guide** command.

For this tutorial, the only required extensions are:

- [Language Support for Java™ by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.java)
- [Debugger for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)

## [Installing and setting up a Java Development Kit (JDK)](https://code.visualstudio.com/docs/java/java-tutorial\#_installing-and-setting-up-a-java-development-kit-jdk)

To use Java within Visual Studio Code, you need to install a Java Development Kit (JDK) on your local environment. JDK is a software development environment used for developing Java applications.

### [Supported Java versions](https://code.visualstudio.com/docs/java/java-tutorial\#_supported-java-versions)

The [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) supports Java version 1.8 or above.

> **Note**: To configure JDKs for your projects, see [Configure Runtime for Projects](https://code.visualstudio.com/docs/java/java-project#_configure-runtime-for-projects). To enable Java preview features, see [How can I use VS Code with new Java versions](https://code.visualstudio.com/docs/java/java-faq#_how-can-i-use-visual-studio-code-with-new-java-versions).

### [Installing a Java Development Kit (JDK)](https://code.visualstudio.com/docs/java/java-tutorial\#_installing-a-java-development-kit-jdk)

If you have never installed a JDK before and need to install one, we recommend you to choose from one of these sources:

- [Amazon Corretto](https://aws.amazon.com/corretto)
- [Azul Zulu](https://www.azul.com/downloads/?package=jdk)
- [Eclipse Adoptium's Temurin](https://adoptium.net/)
- [IBM Semeru Runtimes](https://developer.ibm.com/languages/java/semeru-runtimes)
- [Microsoft Build of OpenJDK](https://www.microsoft.com/openjdk)
- [Oracle Java SE](https://www.oracle.com/java/technologies/javase-downloads.html)
- [Red Hat build of OpenJDK](https://developers.redhat.com/products/openjdk/download)
- [SapMachine](https://sapmachine.io/)

## [Creating a source code file](https://code.visualstudio.com/docs/java/java-tutorial\#_creating-a-source-code-file)

Create a folder for your Java program and open the folder with VS Code. Then in VS Code, create a new file and save it with the name `Hello.java`. When you open that file, the Java Language Server automatically starts loading, and you should see a language status item with a loading icon on the right side of the Status Bar showing the language status is busy. After it finishes loading, you can hover on the language status item and find the loading process has been finished successfully. You can also choose to pin the status item in the status bar.

> **Note**: If you open a Java file in VS Code without opening its folder, the Java Language Server might not work properly.

VS Code will also try to figure out the correct package for the new type and fill the new file from a template. See [Create new file](https://code.visualstudio.com/docs/java/java-editing#_create-new-file).

You can also create a Java project using the **Java: Create Java Project** command. Bring up the **Command Palette** (Ctrl+Shift+P) and then type `java` to search for this command. After selecting the command, you will be prompted for the location and name of the project. You can also choose your build tool from this command.

Visual Studio Code also supports more complex Java projects — see [Project Management](https://code.visualstudio.com/docs/java/java-project).

## [Editing source code](https://code.visualstudio.com/docs/java/java-tutorial\#_editing-source-code)

You can use code snippets to scaffold your classes and methods. VS Code also provides IntelliSense for code completion, and various refactor methods.

To learn more about editing Java, see [Java Editing](https://code.visualstudio.com/docs/java/java-editing).

## [Running and debugging your program](https://code.visualstudio.com/docs/java/java-tutorial\#_running-and-debugging-your-program)

To run and debug Java code, set a breakpoint, then either press F5 on your keyboard or use the **Run** \> **Start Debugging** menu item. You can also use the **Run\|Debug** CodeLens option in the editor. After the code compiles, you can see all your variables and threads in the **Run and Debug** view.

The debugger also supports advanced features such as [Hot Code Replace](https://code.visualstudio.com/docs/java/java-debugging#_hot-code-replace) and conditional breakpoints.

For more information, see [Java Debugging](https://code.visualstudio.com/docs/java/java-debugging).

## [More features](https://code.visualstudio.com/docs/java/java-tutorial\#_more-features)

The editor also has many more capabilities to assist with your Java workload.

- [Editing Java](https://code.visualstudio.com/docs/java/java-editing) explains how to navigate and edit Java in more details
- [Debugging](https://code.visualstudio.com/docs/java/java-debugging) illustrates all the key features of the Java Debugger
- [Testing](https://code.visualstudio.com/docs/java/java-testing) provides comprehensive support for JUnit and TestNG framework
- [Java Project Management](https://code.visualstudio.com/docs/java/java-project) shows you how to use a project view and work with Maven
- [Spring Boot](https://code.visualstudio.com/docs/java/java-spring-boot) and [Tomcat and Jetty](https://code.visualstudio.com/docs/java/java-tomcat-jetty) demonstrate great framework support
- [Java Web Apps](https://code.visualstudio.com/docs/java/java-webapp) shows how to work with Java Web App in VS Code

## Help and support

### Still need help?

- [![](https://code.visualstudio.com/assets/community/sidebar/stackoverflow.svg)Ask the community](https://stackoverflow.com/questions/tagged/vscode)
- [![](https://code.visualstudio.com/assets/community/sidebar/github.svg)Request features](https://go.microsoft.com/fwlink/?LinkID=533482)
- [![](https://code.visualstudio.com/assets/community/sidebar/issue.svg)Report issues](https://www.github.com/Microsoft/vscode/issues)

### Help us improve

All VS Code docs are open source. See something that's wrong or unclear? [Submit a pull request](https://vscode.dev/github/microsoft/vscode-docs/blob/main/docs/java/java-tutorial.md).

1/4/2022

- [![RSS](https://code.visualstudio.com/assets/community/sidebar/rss.svg)RSS Feed](https://code.visualstudio.com/feed.xml)
- [![Stackoverflow](https://code.visualstudio.com/assets/community/sidebar/stackoverflow.svg)Ask questions](https://stackoverflow.com/questions/tagged/vscode)
- [![Twitter](https://code.visualstudio.com/assets/community/sidebar/twitter.svg)Follow @code](https://go.microsoft.com/fwlink/?LinkID=533687)
- [![GitHub](https://code.visualstudio.com/assets/community/sidebar/github.svg)Request features](https://go.microsoft.com/fwlink/?LinkID=533482)
- [![Issues](https://code.visualstudio.com/assets/community/sidebar/issue.svg)Report issues](https://www.github.com/Microsoft/vscode/issues)
- [![YouTube](https://code.visualstudio.com/assets/community/sidebar/youtube.svg)Watch videos](https://www.youtube.com/channel/UCs5Y5_7XK8HLDX0SLNwkd3w)

![Search](https://code.visualstudio.com/assets/icons/search-dark.svg)![Search](https://code.visualstudio.com/assets/icons/search.svg)