# SonarQube

## 2025-09-11

- 2025-09-11 13:36 PM
- By Google Gemini 2.5 Flash

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
What is the config file of SonarQube that we can put in a Java SpringBoot git repository?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
For a Java Spring Boot project, the main configuration file for SonarQube is `sonar-project.properties`. ⚙️ This file is placed in the **root directory** of your Git repository and defines the project-specific settings for the SonarScanner.

-----

### Key Properties in `sonar-project.properties`

The `sonar-project.properties` file uses a simple key-value format. Here are the most common and essential properties for a Java Spring Boot project:

  * **`sonar.projectKey`**: A unique key that identifies your project in SonarQube. It's often in a format like `my-company:my-project`.
  * **`sonar.projectName`**: The name of the project as it will appear in the SonarQube UI.
  * **`sonar.projectVersion`**: The version number of your project. This is optional but good practice.
  * **`sonar.sources`**: The directory or directories containing the source code to be analyzed. For most Spring Boot projects, this is `src/main/java`.
  * **`sonar.tests`**: The directory or directories containing your test code. For Java, this is typically `src/test/java`.
  * **`sonar.java.binaries`**: The location of the compiled class files. For Maven projects, this is usually `target/classes`.
  * **`sonar.sourceEncoding`**: The character encoding of your source files, such as `UTF-8`.
  * **`sonar.host.url`**: The URL of your SonarQube server. This is often passed through the CI/CD pipeline, but can be set here.
  * **`sonar.login`**: The authentication token for the SonarScanner to connect to the SonarQube server. For security, it's highly recommended to store this as a secret in your CI/CD environment and not commit it to your repository.

-----

### Example `sonar-project.properties` File

Here is a simple, commented example of what your `sonar-project.properties` file might look like:

```properties
# Required properties
sonar.projectKey=your-organization-or-project-key
sonar.projectName=Your Spring Boot Project Name
sonar.projectVersion=1.0.0

# Path to the source code (relative to the project root)
sonar.sources=src/main/java

# Path to the test code
sonar.tests=src/test/java

# Path to the compiled binaries (for code coverage and analysis)
sonar.java.binaries=target/classes

# Optional properties
sonar.sourceEncoding=UTF-8

# Server connection details (often set in CI/CD)
# sonar.host.url=http://localhost:9000
# sonar.login=your-scanner-authentication-token
```

### Alternatives and Additional Configurations

While `sonar-project.properties` is the standard for standalone projects, if you're using a build tool like **Maven** or **Gradle**, the SonarQube properties are often configured directly in the build file (`pom.xml` for Maven or `build.gradle` for Gradle) or passed as command-line arguments during the build process. This is common in automated CI/CD pipelines, as it keeps the repository cleaner and allows for dynamic configuration.
</td></tr></table>

- 2025-09-11 13:40 PM
- By Google Gemini

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step command line instruction to create a sample springboot project and configure sonarqube for code coverage scan?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Creating a Spring Boot project and configuring SonarQube for code coverage involves a few command-line steps using Maven. The key is to first generate a report with a tool like JaCoCo and then provide that report to the SonarScanner during the analysis.

### Step 1: Create a Spring Boot Project

You can use the Maven command line to generate a new Spring Boot project. This command uses the Spring Boot archetype to scaffold a basic project.

```bash
mvn archetype:generate \
  -DgroupId=com.example \
  -DartifactId=my-spring-boot-app \
  -DarchetypeArtifactId=spring-boot-archetype \
  -DarchetypeVersion=2.7.1 \
  -DinteractiveMode=false
```

This command will create a new directory named **`my-spring-boot-app`** with a standard Spring Boot project structure and a `pom.xml` file.

-----

### Step 2: Add JaCoCo and SonarQube Plugins to `pom.xml`

Navigate into your new project's directory and edit the `pom.xml` file to add the necessary plugins for code coverage and SonarQube analysis.

Add the following to the `<plugins>` section within the `<build>` tag:

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>

<plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.9.1.2184</version>
</plugin>
```

Add these properties to the `<properties>` section of your `pom.xml`.

```xml
<properties>
    <sonar.host.url>http://localhost:9000</sonar.host.url>
    <sonar.coverage.jacoco.xmlReportPaths>${project.basedir}/target/site/jacoco/jacoco.xml</sonar.coverage.jacoco.xmlReportPaths>
</properties>
```

The `sonar.host.url` should point to your SonarQube server's address. If you're running it locally, `http://localhost:9000` is the default. The `sonar.coverage.jacoco.xmlReportPaths` property tells SonarQube where to find the JaCoCo report.

-----

### Step 3: Run the SonarQube Analysis

With the plugins configured, you can run a single Maven command to execute the tests, generate the JaCoCo coverage report, and then send the results to SonarQube.

The `-Dsonar.login` flag is where you'll pass the authentication token for your SonarQube project.

```bash
mvn clean verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar \
  -Dsonar.login=YOUR_SONARQUBE_TOKEN
```

  * **`mvn clean verify`**: This command first cleans the project and then runs the entire build lifecycle up to the `verify` phase, which includes running unit tests and, consequently, generating the JaCoCo report.
  * **`org.sonarsource.scanner.maven:sonar-maven-plugin:sonar`**: This is the explicit goal to run the SonarQube analysis.
  * **`-Dsonar.login=YOUR_SONARQUBE_TOKEN`**: This provides your authentication token, which you must get from your SonarQube instance. **Never commit this token to your repository.** It should be handled as a secret, especially in CI/CD pipelines.

Once the command completes, you'll see a link in the terminal output to your project's dashboard on the SonarQube server, where you can view the analysis results, including the code coverage.
</td></tr></table>