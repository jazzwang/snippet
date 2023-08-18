# README

[TOC]

## 2022-05-04

- https://docs.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?view=aspnetcore-6.0&tabs=visual-studio
- ( 2022-05-04 16:35:01 )
- Q: How to generate .net core web api template?
- Reference:
  - https://stackoverflow.com/a/68921795
  - https://github.com/RicoSuter/NSwag

## 2023-08-06

- ( 2023-08-06 21:39:38 )
- https://dotnet.microsoft.com/en-us/languages

> You can write .NET apps in <font color="red">C#, F#, or Visual Basic.</font>
>  - C# is a simple, modern, object-oriented, and type-safe programming language.
>  - F# is a programming language that makes it easy to write succinct, robust, and performant code.
>  - Visual Basic is an approachable language with a simple syntax for building type-safe, object-oriented apps.

### .NET Core

- Source: [^1]
  * [Clean Code .NET](https://github.com/thangchung/clean-code-dotnet)
  * [Entity Framework Core Succinctly](https://www.syncfusion.com/succinctly-free-ebooks/entity-frame-work-core-succinctly) - Ricardo Peres
  * [.NET documentation - Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/)
  * [Using .NET Core, Docker, and Kubernetes Succinctly](https://www.syncfusion.com/ebooks/using-netcore-docker-and-kubernetes-succinctly) - Michele Aponte

[^1]: [Free Programming Books > .Net Core](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md#net-core)

## 2023-08-10

1. .NET Core Microservices - The Complete Guide (.NET 6 MVC) (11h 52m)
    - Video: https://learning.oreilly.com/videos/net-core-microservices/9781803247793/

### Visual Studio Code for C#

1. Working with C#
    - https://code.visualstudio.com/docs/languages/csharp

2. Using .NET in Visual Studio Code
    - https://code.visualstudio.com/docs/languages/dotnet

3. VS Code .csproj Extension
    - https://marketplace.visualstudio.com/items?itemName=lucasazzola.vscode-csproj

    > This extension will helps you keep your csproj files in sync when using VS Code. <font color='hotpink'>This is useful if you work in a team that uses both VS Code and Visual Studio.</font>

### Modern Web App

- https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/
- https://github.com/dotnet-architecture/eShopOnWeb

## 2022-08-14

### Swagger to .Net Core

- ( 2023-08-14 21:49:10 )

**Jazz:** Are the tools to convert swagger API contract to .net core code?
**ChatGPT:**

>  Yes, there are tools available that can help you generate .NET Core code from a Swagger API contract (also known as an OpenAPI specification). These tools can automate the process of generating API client libraries, server code, or other related components based on the API specification. Here are a couple of popular options:
>
>  1. **NSwag**: NSwag is a popular open-source toolchain that provides a variety of code generation capabilities for working with Swagger and OpenAPI specifications. It can generate client code, server stubs, API documentation, and more. NSwag supports several programming languages, including C#, TypeScript, and others. It can be used as a .NET Core CLI tool, a Visual Studio extension, or integrated into your build process.
>
> You can find NSwag on GitHub: https://github.com/RicoSuter/NSwag
>
>  2. **AutoRest**: AutoRest is another popular open-source tool for generating client libraries from OpenAPI specifications. It's specifically designed to generate client libraries for interacting with RESTful APIs. AutoRest supports multiple programming languages, including C# for .NET Core. It offers advanced customization options and can generate strongly-typed clients based on the API contract.
>
>    You can find AutoRest on GitHub: https://github.com/Azure/autorest
>
>  Both of these tools provide command-line interfaces that allow you to generate code based on your API specification. You'll typically provide the path to your OpenAPI or Swagger JSON/YAML file along with some configuration options, and the tools will generate the desired code for you.
>
>  It's worth noting that while these tools can significantly speed up the process of generating code from API contracts, some manual adjustments or customization might still be required to align the generated code with your specific project's architecture and requirements.

### NSwag

- ( 2023-08-14 22:13:16 )
- In [README.md of NSwag](https://github.com/RicoSuter/NSwag/blob/master/README.md), this project includes functionality of AutoRest already. Let's start from digging into this project.

> The project combines the functionality of Swashbuckle (OpenAPI/Swagger generation) and **<font color='red'>AutoRest</font>** (client generation) in one toolchain (these two libs are not needed).

- ( 2023-08-14 22:15:48 )
- **Goal:** can we convert https://petstore.swagger.io/#/pet/addPet to .Net core project?
- ( 2023-08-14 22:34:56 )
- Installation:
```bash
~$ git clone https://github.com/RicoSuter/NSwag.git
Cloning into 'NSwag'...
remote: Enumerating objects: 80719, done.
remote: Counting objects: 100% (318/318), done.
remote: Compressing objects: 100% (193/193), done.
remote: Total 80719 (delta 173), reused 207 (delta 125), pack-reused 80401
Receiving objects: 100% (80719/80719), 57.28 MiB | 23.49 MiB/s, done.
Resolving deltas: 100% (68752/68752), done.
~$ cd NSwag/
~/NSwag$ dotnet

Usage: dotnet [options]
Usage: dotnet [path-to-application]

{
Options:
  -h|--help         Display help.
  --info            Display .NET information.
  --list-sdks       Display the installed SDKs.
  --list-runtimes   Display the installed runtimes.

path-to-application:
  The path to an application .dll file to execute.
~/NSwag$ dotnet --version
The command could not be loaded, possibly because:
  * You intended to execute a .NET application:
      The application '--version' does not exist.
  * You intended to execute a .NET SDK command:
      A compatible .NET SDK was not found.

Requested SDK version: 7.0.100
global.json file: /home/jazz_innova18/NSwag/global.json

Installed SDKs:
2.1.818 [/usr/share/dotnet/sdk]
3.1.426 [/usr/share/dotnet/sdk]
5.0.408 [/usr/share/dotnet/sdk]
6.0.412 [/usr/share/dotnet/sdk]

Install the [7.0.100] .NET SDK or update [/home/jazz_innova18/NSwag/global.json] to match an installed SDK.

Learn about SDK resolution:
https://aka.ms/dotnet/sdk-not-found
~/NSwag$ vi global.json
~/NSwag$ cat global.json
{
  "sdk": {
    "version": "6.0.412",
    "rollForward": "latestMinor"
  }
}
~/NSwag$ ./build.sh
GNU bash, version 5.1.4(1)-release (x86_64-pc-linux-gnu)
Microsoft (R) .NET SDK version 6.0.412
/usr/share/dotnet/sdk/6.0.412/Sdks/Microsoft.NET.Sdk/targets/Microsoft.NET.TargetFrameworkInference.targets(144,5): error NETSDK1045: The current .NET SDK does not support targeting .NET 7.0.  Either target .NET 6.0 or lower, or use a version of the .NET SDK that supports .NET 7.0. [/home/jazz_innova18/NSwag/build/_build.csproj]
```
- ( 2023-08-14 22:39:33 )
- https://www.npmjs.com/package/nswag
```bash
~$ npm install nswag -g

added 1 package in 2s
~$ which nswag
/usr/local/nvm/versions/node/v18.12.1/bin/nswag
~$ nswag version
NSwag NPM CLI
NSwag command line tool for .NET Core Net60, toolchain v13.19.0.0 (NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0))
Visit http://NSwag.org for more information.
NSwag bin directory: /usr/local/nvm/versions/node/v18.12.1/lib/node_modules/nswag/bin/binaries/Net60

NSwag version: 13.19.0.0
NJsonSchema version: 10.9.0.0 (Newtonsoft.Json v13.0.0.0)

Duration: 00:00:00.0080436
```
- ( 2023-08-14 22:45:27 )
- https://github.com/RicoSuter/NSwag/wiki/CSharpControllerGenerator
```bash
~$ mkdir -p petstore
~$ cd petstore
~/petstore$ nswag openapi2cscontroller /input:https://petstore.swagger.io/v2/swagger.json /classname:petstore /namespace:me.3du /output:Controllers/ResourceController.cs /UseLiquidTemplates:true /AspNetNamespace:"Microsoft.AspNetCore.Mvc" /ControllerBaseClass:"Microsoft.AspNetCore.Mvc.Controller"
NSwag NPM CLI
NSwag command line tool for .NET Core Net60, toolchain v13.19.0.0 (NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0))
Visit http://NSwag.org for more information.
NSwag bin directory: /usr/local/nvm/versions/node/v18.12.1/lib/node_modules/nswag/bin/binaries/Net60
Code has been successfully written to file.

Duration: 00:00:01.6041773

~/petstore$ tree
.
└── Controllers
    └── ResourceController.cs

1 directory, 1 file
```

### OpenAPI Generator

- ( 2023-08-14 22:52:52 )
- Installation: https://openapi-generator.tech/docs/installation
```bash
~$ npm install @openapitools/openapi-generator-cli -g
npm install @openapitools/openapi-generator-cli -g

added 113 packages in 25s

23 packages are looking for funding
  run `npm fund` for details

~$ openapi-generator-cli version
Download 6.6.0 ...
Downloaded 6.6.0
Did set selected version to 6.6.0
6.6.0

~$ openapi-generator-cli list -s | tr ',' '\n'

ada
ada-server
android
apache2
apex
asciidoc
aspnetcore
avro-schema
bash
crystal
c
clojure
cwiki
cpp-qt-client
cpp-qt-qhttpengine-server
cpp-pistache-server
cpp-restbed-server
cpp-restbed-server-deprecated
cpp-restsdk
cpp-tiny
cpp-tizen
cpp-ue4
csharp
csharp-netcore
csharp-netcore-functions
dart
dart-dio
eiffel
elixir
elm
erlang-client
erlang-proper
erlang-server
fsharp-functions
fsharp-giraffe-server
go
go-echo-server
go-server
go-gin-server
graphql-schema
graphql-nodejs-express-server
groovy
kotlin
kotlin-server
kotlin-spring
kotlin-vertx
ktorm-schema
haskell-http-client
haskell
haskell-yesod
java
jaxrs-cxf-client
java-helidon-client
java-helidon-server
java-inflector
java-micronaut-client
java-micronaut-server
java-msf4j
java-pkmst
java-play-framework
java-undertow-server
java-vertx-web
java-camel
jaxrs-cxf
jaxrs-cxf-extended
jaxrs-cxf-cdi
jaxrs-jersey
jaxrs-resteasy
jaxrs-resteasy-eap
jaxrs-spec
javascript
javascript-flowtyped
javascript-closure-angular
jetbrains-http-client
jmeter
julia-client
julia-server
k6
lua
markdown
mysql-schema
n4js
nim
nodejs-express-server
objc
ocaml
openapi
openapi-yaml
plantuml
perl
php
php-laravel
php-lumen
php-slim4
php-symfony
php-mezzio-ph
php-dt
powershell
protobuf-schema
python-legacy
python-nextgen
python
python-fastapi
python-prior
python-flask
python-aiohttp
python-blueplanet
r
ruby
ruby-on-rails
ruby-sinatra
rust
rust-server
scalatra
scala-akka
scala-akka-http-server
scala-finch
scala-gatling
scala-lagom-server
scala-play-server
scala-sttp
scalaz
spring
dynamic-html
html
html2
swift5
typescript
typescript-angular
typescript-aurelia
typescript-axios
typescript-fetch
typescript-inversify
typescript-jquery
typescript-nestjs
typescript-node
typescript-redux-query
typescript-rxjs
wsdl-schema
xojo-client
~$ mkdir pet
~$ cd pet/
~/pet$ wget -q https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml
~/pet$ openapi-generator-cli generate -i petstore.yaml -g csharp-netcore
Did set selected version to 6.6.0
[main] INFO  o.o.codegen.DefaultGenerator - Generating with dryRun=false
[main] INFO  o.o.c.ignore.CodegenIgnoreProcessor - No .openapi-generator-ignore file found.
[main] INFO  o.o.codegen.DefaultGenerator - OpenAPI Generator: csharp-netcore (client)
[main] INFO  o.o.codegen.DefaultGenerator - Generator 'csharp-netcore' is considered stable.
[main] INFO  o.o.c.l.AbstractCSharpCodegen - Environment variable CSHARP_POST_PROCESS_FILE not defined so the C# code may not be properly formatted by uncrustify (0.66 or later) or other code formatter. To define it, try `export CSHARP_POST_PROCESS_FILE="/usr/local/bin/uncrustify --no-backup" && export UNCRUSTIFY_CONFIG=/path/to/uncrustify-rules.cfg` (Linux/Mac). Note: replace /path/to with the location of uncrustify-rules.cfg
[main] INFO  o.o.c.l.AbstractCSharpCodegen - NOTE: To enable file post-processing, 'enablePostProcessFile' must be set to `true` (--enable-post-process-file for CLI).
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] WARN  o.o.c.languages.CSharpClientCodegen - If using built-in templates, RestSharp only supports netstandard 2.0 or later.
[main] INFO  o.o.c.languages.CSharpClientCodegen - Generating code for .NET Framework netstandard2.0
[main] INFO  o.o.codegen.InlineModelResolver - Inline schema created as updatePetWithForm_request. To have complete control of the model name, set the `title` field or use the inlineSchemaNameMapping option (--inline-schema-name-mappings in CLI).
[main] INFO  o.o.codegen.InlineModelResolver - Inline schema created as uploadFile_request. To have complete control of the model name, set the `title` field or use the inlineSchemaNameMapping option (--inline-schema-name-mappings in CLI).
[main] INFO  o.o.codegen.DefaultGenerator - Model updatePetWithForm_request not generated since it's marked as unused (due to form parameters) and `skipFormModel` (global property) set to true (default)
[main] INFO  o.o.codegen.DefaultGenerator - Model uploadFile_request not generated since it's marked as unused (due to form parameters) and `skipFormModel` (global property) set to true (default)
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/ApiResponse.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/ApiResponseTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/ApiResponse.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/Category.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/CategoryTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/Category.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/Order.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/OrderTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/Order.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/Pet.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/PetTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/Pet.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/Tag.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/TagTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/Tag.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/User.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Model/UserTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/User.md
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/json)
[main] WARN  o.o.codegen.DefaultCodegen - Multiple MediaTypes found, using only the first one
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/json)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/xml)
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Api/PetApi.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Api/PetApiTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/PetApi.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Api/StoreApi.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Api/StoreApiTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/StoreApi.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Api/UserApi.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Api/UserApiTests.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./docs/UserApi.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/IApiAccessor.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/Configuration.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ApiClient.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ApiException.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ApiResponse.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ExceptionFactory.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/OpenAPIDateConverter.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ClientUtils.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/HttpMethod.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/IAsynchronousClient.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/ISynchronousClient.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/RequestOptions.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/Multimap.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/RetryConfiguration.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/IReadableConfiguration.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/GlobalConfiguration.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./README.md
[main] INFO  o.o.codegen.TemplateManager - writing file ./git_push.sh
[main] INFO  o.o.codegen.TemplateManager - writing file ./.gitignore
[main] INFO  o.o.codegen.TemplateManager - writing file ./Org.OpenAPITools.sln
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Org.OpenAPITools.csproj
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools.Test/Org.OpenAPITools.Test.csproj
[main] INFO  o.o.codegen.TemplateManager - writing file ./appveyor.yml
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Model/AbstractOpenAPISchema.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/Auth/OAuthAuthenticator.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/Auth/TokenResponse.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./src/Org.OpenAPITools/Client/Auth/OAuthFlow.cs
[main] INFO  o.o.codegen.TemplateManager - writing file ./api/openapi.yaml
[main] INFO  o.o.codegen.TemplateManager - writing file /home/jazz_innova18/pet/./.openapi-generator-ignore
[main] INFO  o.o.codegen.TemplateManager - writing file ./.openapi-generator/VERSION
[main] INFO  o.o.codegen.TemplateManager - writing file ./.openapi-generator/FILES
################################################################################
# Thanks for using OpenAPI Generator.                                          #
# Please consider donation to help us maintain this project 🙏                 #
# https://opencollective.com/openapi_generator/donate                          #
#                                                                              #
# This generator's contributed by Jim Schubert (https://github.com/jimschubert)#
# Please support his work directly via https://patreon.com/jimschubert 🙏      #
################################################################################

~/pet$ tree
.
├── api
│   └── openapi.yaml
├── appveyor.yml
├── docs
│   ├── ApiResponse.md
│   ├── Category.md
│   ├── Order.md
│   ├── PetApi.md
│   ├── Pet.md
│   ├── StoreApi.md
│   ├── Tag.md
│   ├── UserApi.md
│   └── User.md
├── git_push.sh
├── openapitools.json
├── Org.OpenAPITools.sln
├── petstore.yaml
├── README.md
└── src
    ├── Org.OpenAPITools
    │   ├── Api
    │   │   ├── PetApi.cs
    │   │   ├── StoreApi.cs
    │   │   └── UserApi.cs
    │   ├── Client
    │   │   ├── ApiClient.cs
    │   │   ├── ApiException.cs
    │   │   ├── ApiResponse.cs
    │   │   ├── Auth
    │   │   │   ├── OAuthAuthenticator.cs
    │   │   │   ├── OAuthFlow.cs
    │   │   │   └── TokenResponse.cs
    │   │   ├── ClientUtils.cs
    │   │   ├── Configuration.cs
    │   │   ├── ExceptionFactory.cs
    │   │   ├── GlobalConfiguration.cs
    │   │   ├── HttpMethod.cs
    │   │   ├── IApiAccessor.cs
    │   │   ├── IAsynchronousClient.cs
    │   │   ├── IReadableConfiguration.cs
    │   │   ├── ISynchronousClient.cs
    │   │   ├── Multimap.cs
    │   │   ├── OpenAPIDateConverter.cs
    │   │   ├── RequestOptions.cs
    │   │   └── RetryConfiguration.cs
    │   ├── Model
    │   │   ├── AbstractOpenAPISchema.cs
    │   │   ├── ApiResponse.cs
    │   │   ├── Category.cs
    │   │   ├── Order.cs
    │   │   ├── Pet.cs
    │   │   ├── Tag.cs
    │   │   └── User.cs
    │   └── Org.OpenAPITools.csproj
    └── Org.OpenAPITools.Test
        ├── Api
        │   ├── PetApiTests.cs
        │   ├── StoreApiTests.cs
        │   └── UserApiTests.cs
        ├── Model
        │   ├── ApiResponseTests.cs
        │   ├── CategoryTests.cs
        │   ├── OrderTests.cs
        │   ├── PetTests.cs
        │   ├── TagTests.cs
        │   └── UserTests.cs
        └── Org.OpenAPITools.Test.csproj

11 directories, 56 files
```


## 2023-08-18

- ( 2023-08-18 23:20:39 )
- test on gitpod.io
```bash
gitpod /workspace/gitpod-labs (main) $ pwd
/workspace/gitpod-labs
gitpod /workspace/gitpod-labs (main) $ python -m venv venv
gitpod /workspace/gitpod-labs (main) $ source venv/bin/activate
(venv) gitpod /workspace/gitpod-labs (main) $ pip install openapi-generator-cli
(venv) gitpod /workspace/gitpod-labs (main) $ openapi-generator version
Picked up JAVA_TOOL_OPTIONS:  -Xmx12884m
4.3.1
(venv) gitpod /workspace/gitpod-labs (main) $ openapi-generator list
Picked up JAVA_TOOL_OPTIONS:  -Xmx12884m
The following generators are available:

CLIENT generators:
    - ada
    - android
    - apex
    - bash
    - c
    - clojure
    - cpp-qt5-client
    - cpp-restsdk
    - cpp-tizen
    - csharp
    - csharp-netcore
    - dart
    - dart-dio
    - dart-jaguar
    - eiffel
    - elixir
    - elm
    - erlang-client
    - erlang-proper
    - flash
    - go
    - go-experimental (experimental)
    - groovy
    - haskell-http-client
    - java
    - javascript
    - javascript-apollo (beta)
    - javascript-closure-angular
    - javascript-flowtyped
    - jaxrs-cxf-client
    - jmeter
    - k6 (beta)
    - kotlin
    - lua
    - nim (beta)
    - objc
    - ocaml
    - perl
    - php
    - powershell
    - powershell-experimental (beta)
    - python
    - python-experimental (experimental)
    - r
    - ruby
    - rust
    - scala-akka
    - scala-gatling
    - scala-sttp (beta)
    - scalaz
    - swift4
    - swift5 (beta)
    - typescript-angular
    - typescript-angularjs
    - typescript-aurelia
    - typescript-axios
    - typescript-fetch
    - typescript-inversify
    - typescript-jquery
    - typescript-node
    - typescript-redux-query
    - typescript-rxjs


SERVER generators:
    - ada-server
    - aspnetcore
    - cpp-pistache-server
    - cpp-qt5-qhttpengine-server
    - cpp-restbed-server
    - csharp-nancyfx
    - erlang-server
    - fsharp-functions (beta)
    - fsharp-giraffe-server (beta)
    - go-gin-server
    - go-server
    - graphql-nodejs-express-server
    - haskell
    - java-inflector
    - java-msf4j
    - java-pkmst
    - java-play-framework
    - java-undertow-server
    - java-vertx
    - java-vertx-web (beta)
    - jaxrs-cxf
    - jaxrs-cxf-cdi
    - jaxrs-cxf-extended
    - jaxrs-jersey
    - jaxrs-resteasy
    - jaxrs-resteasy-eap
    - jaxrs-spec
    - kotlin-server
    - kotlin-spring
    - kotlin-vertx (beta)
    - nodejs-express-server (beta)
    - php-laravel
    - php-lumen
    - php-silex
    - php-slim4
    - php-symfony
    - php-ze-ph
    - python-aiohttp
    - python-blueplanet
    - python-flask
    - ruby-on-rails
    - ruby-sinatra
    - rust-server
    - scala-akka-http-server (beta)
    - scala-finch
    - scala-lagom-server
    - scala-play-server
    - scalatra
    - spring


DOCUMENTATION generators:
    - asciidoc
    - cwiki
    - dynamic-html
    - html
    - html2
    - markdown (beta)
    - openapi
    - openapi-yaml


SCHEMA generators:
    - avro-schema (beta)
    - mysql-schema


CONFIG generators:
    - apache2
    - graphql-schema
    - protobuf-schema (beta)

(venv) gitpod /workspace/gitpod-labs (main) $ curl https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 58994  100 58994    0     0  30307      0  0:00:01  0:00:01 --:--:-- 30299
dotnet-install: Attempting to download using aka.ms link https://dotnetcli.azureedge.net/dotnet/Sdk/6.0.413/dotnet-sdk-6.0.413-linux-x64.tar.gz
dotnet-install: Extracting zip from https://dotnetcli.azureedge.net/dotnet/Sdk/6.0.413/dotnet-sdk-6.0.413-linux-x64.tar.gz
dotnet-install: Installed version is 6.0.413
dotnet-install: Adding to current process PATH: `/home/gitpod/.dotnet`. Note: This change will be visible only when sourcing script.
dotnet-install: Note that the script does not resolve dependencies during installation.
dotnet-install: To check the list of dependencies, go to https://learn.microsoft.com/dotnet/core/install, select your operating system and check the "Dependencies" section.
dotnet-install: Installation finished successfully.

(venv) gitpod /workspace/gitpod-labs (main) $ mv /home/gitpod/.dotnet .
(venv) gitpod /workspace/gitpod-labs (main) $ du -sh .dotnet/
493M	.dotnet/
(venv) gitpod /workspace/gitpod-labs (main) $ export HOME=/workspace/gitpod-labs
(venv) gitpod /workspace/gitpod-labs (main) $ cd
(venv) gitpod /workspace/gitpod-labs (main) $ export PATH=$PATH:~/.dotnet
(venv) gitpod ~ (main) $ wget https://raw.githubusercontent.com/jazzwang/snippet/master/go/petstore/add-pet.yaml
```
- <mark>以後應該習慣性把 $HOME 設成 `workspace` 路徑，這樣就不會遇到 gitpod 被關閉後，下次回來 `/home/gitpod` 被清掉造成的問題。</mark>