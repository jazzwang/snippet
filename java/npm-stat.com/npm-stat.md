# npm-stat

- Git Repo
  - https://github.com/pvorb/npm-stat.com
- DeepWiki
  - https://deepwiki.com/pvorb/npm-stat.com

## 2025-11-18

- 需求：
  - 想比較不同的 npm 套件下載趨勢，特別是 gemini-cli 類似的實作
- 思路：
  - 嘗試了解 npm-stat.com 的實作
    - 從 api.npmjs.org 取得 downloads

> C:\Users\jazzw\.local\bin\aider --no-auto-commits --no-gitignore --model gemini/gemini-2.5-flash  
> Aider v0.86.1  
> Model: gemini/gemini-2.5-flash with diff-fenced edit format  
> Git repo: .git with 109 files  
> Repo-map: using 4096 tokens, auto refresh  

#### high-level overview

This Git repository appears to contain a Spring Boot application named "NpmStatApp" that interacts with npm APIs to retrieve package download statistics and author-related package information.

Key components include:
*   **API Clients**: Feign clients (`DownloadsClient`, `SearchClient`) for fetching data from npm's download and registry APIs.
*   **Data Processing**: Services (`GapFinder`, `AuthorPackageProvider`) for identifying gaps in download data and extracting package names from search results.
*   **Persistence**: jOOQ-generated classes (`DownloadCount`, `DefaultCatalog`, `Public`, etc.) and a `LocalDateConverter` for database interaction, likely storing download counts.
*   **Web Frontend**: JavaScript files (`charts.js`, `highcharts-3.0.10.min.js`, `jquery-2.0.3.min.js`) suggest a web interface for displaying charts and data.
*   **Build System**: Maven is used as the build tool.

#### could you explain the purpose of each folder in this repo?  

Based on the provided file summaries, here is the purpose of each folder:

*   **`src\main\java\de\vorb\npmstat\`**: This is the root package for the main Java application code. It contains the core Spring Boot application class (`NpmStatApp`) and other top-level configuration.
    *   **`src\main\java\de\vorb\npmstat\clients\`**: This folder contains classes related to external API clients.
        *   **`src\main\java\de\vorb\npmstat\clients\authors\`**: This subfolder specifically holds components for interacting with the npm registry's author/package search API, including client interfaces (`SearchClient`) and data transfer objects (`PackageDetailsJson`, `SearchResultJson`, `SearchResultRowJson`).
        *   **`src\main\java\de\vorb\npmstat\clients\downloads\`**: This subfolder contains components for interacting with the npm download counts API, including the client interface (`DownloadsClient`) and data transfer objects (`DownloadsJson`).
    *   **`src\main\java\de\vorb\npmstat\persistence\`**: This folder is dedicated to database persistence logic.
        *   **`src\main\java\de\vorb\npmstat\persistence\converters\`**: This subfolder contains custom converters, such as `LocalDateConverter`, used for mapping Java objects to database types.
        *   **`src\main\java\de\vorb\npmstat\persistence\jooq\`**: This subfolder holds the jOOQ-generated classes for database interaction, representing the schema, tables, and records.
            *   **`src\main\java\de\vorb\npmstat\persistence\jooq\tables\`**: This subfolder contains the jOOQ-generated classes that represent the database tables (e.g., `DownloadCount`, `HypertableRelationSize`).
                *   **`src\main\java\de\vorb\npmstat\persistence\jooq\tables\pojos\`**: This subfolder contains the jOOQ-generated Plain Old Java Objects (POJOs) corresponding to the rows of the database tables.
                *   **`src\main\java\de\vorb\npmstat\persistence\jooq\tables\records\`**: This subfolder contains the jOOQ-generated record classes used for interacting with individual rows of the database tables.
    *   **`src\main\java\de\vorb\npmstat\services\`**: This folder contains business logic services, such as `AuthorPackageProvider` and `GapFinder`, which encapsulate application-specific operations.
*   **`src\main\js\`**: This folder contains unminified, source JavaScript files, likely for the frontend application logic (`charts.js`, `escape-html.js`).
*   **`src\main\resources\static\`**: This folder holds static web resources that are served directly by the Spring Boot application, including compiled/minified JavaScript files (`charts.js`, `highcharts-3.0.10.min.js`, `jquery-2.0.3.min.js`).

#### main backend program

The main backend program is located at `src\main\java\de\vorb\npmstat\NpmStatApp.java`.

#### sequence diagram of those backend classes

Here is a high-level sequence diagram showing interactions between the identified backend classes. This diagram illustrates two common flows: finding packages by an author and fetching package download statistics to identify gaps.

```plantuml
@startuml
skinparam monochrome true
skinparam packageStyle rectangle

actor Client as C

participant NpmStatApp as App
participant AuthorPackageProvider as APP
participant SearchClient as SC
collections "npm Registry (External)" as NPM_REGISTRY
participant DownloadsClient as DC
collections "npm API (External)" as NPM_API
participant GapFinder as GF

C -> App: 1. Request to find packages for an author (e.g., via a controller)

App -> APP: 2. findPackageNamesForAuthor(authorName)
APP -> SC: 3. search("maintainer:" + authorName)
activate SC
SC -> NPM_REGISTRY: 4. GET /-/v1/search?text=... (query external npm registry)
activate NPM_REGISTRY
NPM_REGISTRY --> SC: 5. SearchResultJson
deactivate NPM_REGISTRY
SC --> APP: 6. SearchResultJson
deactivate SC
APP --> App: 7. Process SearchResultJson (extract package names)
App --> C: 8. Return Set<String> of package names

C -> App: 9. Request to get package downloads and analyze (e.g., via a controller)

App -> DC: 10. getPackageDownloadsForTimeRange(packageName, from, until)
activate DC
DC -> NPM_API: 11. GET /downloads/range/{from}:{until}/{package} (query external npm API)
activate NPM_API
NPM_API --> DC: 12. DownloadsJson
deactivate NPM_API
DC --> App: 13. DownloadsJson
deactivate DC
App -> GF: 14. findGaps(from, until, downloadCountsMap)
activate GF
GF --> App: 15. List<Gap>
deactivate GF
App --> C: 16. Return DownloadsJson and/or List<Gap>

@enduml
```

#### how does the backend fetch npm downloads?  

The backend fetches npm downloads through the `DownloadsClient` interface.

1.  The `DownloadsClient` is a Spring Cloud OpenFeign client configured to interact with the npm API's download endpoint, with its base URL set by `${npm.api.baseUrl}/downloads/`.
2.  The `getPackageDownloadsForTimeRange` method within this interface is annotated with `@GetMapping("range/{from}:{until}/{package}")`.
3.  When this method is called, Feign constructs and executes an HTTP GET request to the npm API. The URL will be similar to `http://<npm.api.baseUrl>/downloads/range/<from_date>:<until_date>/<package_name>`.
4.  The `packageName`, `from` (start date), and `until` (end date) parameters are used to populate the path variables in the request URL.
5.  The npm API's response is then automatically deserialized into a `DownloadsJson` object, which contains the download statistics.

> Tokens: 8.9k sent, 201 received. Cost: $0.0036 message, $0.03 session.  

#### sequence diagram of `NpmStatApp`

```plantuml
@startuml
skinparam monochrome true
skinparam packageStyle rectangle

participant JVM as JVM
participant NpmStatApp as App
participant "Spring Boot Framework" as SpringBoot
participant "SpringApplicationBuilder" as Builder

JVM -> App: main(String... args)
activate App

App -> SpringBoot: run(App.class, args)
activate SpringBoot

' During application context initialization, Spring Boot interacts with App's methods
SpringBoot -> App: configure(SpringApplicationBuilder application)
activate App
App -> Builder: application.sources(App.class)
activate Builder
Builder --> App: configured builder
deactivate Builder
App --> SpringBoot: configured application builder
deactivate App

SpringBoot -> App: clock() : Clock (create bean)
activate App
App --> SpringBoot: returns Clock.systemUTC()
deactivate App

SpringBoot -> App: localDateFormatter() : Formatter<LocalDate> (create bean)
activate App
App --> SpringBoot: returns new Formatter<LocalDate>() {...}
deactivate App

SpringBoot --> App: application context initialized
deactivate SpringBoot

App --> JVM: application started
deactivate App

@enduml
```

#### create a flow diagram of npmstat using plantuml syntax  

```plantuml
@startuml
skinparam monochrome true
skinparam packageStyle rectangle

rectangle "Client" as Client

rectangle "npmstat Backend Application" as Backend {
  component "Author Package Provider" as AuthorPackageProvider
  component "Search Client (Feign)" as SearchClient
  component "Downloads Client (Feign)" as DownloadsClient
  component "Gap Finder Service" as GapFinder
  component "Persistence Layer (jOOQ)" as Persistence
}

rectangle "External npm Services" as ExternalNpm {
  cloud "npm Registry API" as NpmRegistry
  cloud "npm Downloads API" as NpmApi
}

Client --> Backend : 1. User Request (e.g., find packages by author)
Backend --> AuthorPackageProvider : 2. Invoke findPackageNamesForAuthor
AuthorPackageProvider --> SearchClient : 3. Call search API
SearchClient --> NpmRegistry : 4. Request package search ("maintainer:...")
NpmRegistry --> SearchClient : 5. Return SearchResultJson
SearchClient --> AuthorPackageProvider : 6. Provide search results
AuthorPackageProvider --> Backend : 7. Return Set<String> of package names

Client --> Backend : 8. User Request (e.g., get package download stats)
Backend --> DownloadsClient : 9. Invoke getPackageDownloadsForTimeRange
DownloadsClient --> NpmApi : 10. Request downloads for package and time range
NpmApi --> DownloadsClient : 11. Return DownloadsJson
DownloadsClient --> Backend : 12. Provide download data

Backend --> Persistence : 13. Store/Retrieve Download Data (DownloadCountRecord)
Backend --> GapFinder : 14. Invoke findGaps with download data
GapFinder --> Backend : 15. Return List<Gap>

Backend --> Client : 16. Return Response (e.g., package names, download stats, gaps)

@enduml
```

- ( 2025-11-18 13:59:33 )
- 透過 deepwiki 來了解實作方式
- https://deepwiki.com/pvorb/npm-stat.com#service-layer

> ### Client Layer
> 
> -   **DownloadsClient**: Feign client for `api.npmjs.org/downloads/*` endpoints
> -   **SearchClient**: Feign client for `registry.npmjs.org/-/v1/search` endpoint

- 短結論：如果我想比較 `aider-chat` (PyPI 下載量) 跟 `@google/gemini-cli`, `@anthropic-ai/claude-code
` , `opencode-ai` (npm 下載量)，可能要參考 ClickPy 跟 npm-stat 的資料源
  - https://clickpy.clickhouse.com/dashboard/aider-chat
  - https://www.npmjs.com/package/@anthropic-ai/claude-code
  - https://www.npmjs.com/package/@google/gemini-cli
  - https://www.npmjs.com/package/@github/copilot
  - https://www.npmjs.com/package/opencode-ai