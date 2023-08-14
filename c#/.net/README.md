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