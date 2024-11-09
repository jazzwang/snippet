# README

[TOC]

## 2023-08-06

- ( 2023-08-06 21:35:47 )
- The Difference Between C# vs .NET
  - https://fullscale.io/blog/csharp-vs-dotnet/
```
In summary, C# is a programming language, while .NET is a developer platform.
```
- ( 2023-08-06 21:39:38 )
- https://dotnet.microsoft.com/en-us/languages

> You can write .NET apps in <font color="red">C#, F#, or Visual Basic.</font>
>  - C# is a simple, modern, object-oriented, and type-safe programming language.
>  - F# is a programming language that makes it easy to write succinct, robust, and performant code.
>  - Visual Basic is an approachable language with a simple syntax for building type-safe, object-oriented apps.

## 2023-08-10

- ( 2023-08-10 22:40:40 )
- Select few training course from O'Reilly Learning

1. C# Basics for Absolute Beginners in C# and .NET (2h 13m)
    - Video: https://learning.oreilly.com/videos/c-basics-for/9781803235837/
    - Github: https://github.com/PacktPublishing/C-sharp-Basics-for-Absolute-Beginners-in-C-Sharp-and-dot-NET

```
$ git submodule add https://github.com/PacktPublishing/C-sharp-Basics-for-Absolute-Beginners-in-C-Sharp-and-dot-NET.git c-sharp-basics
```

2. Visual Studio Code for C# Developers (3h 13m)
    - Video: https://learning.oreilly.com/videos/visual-studio-code/9781803230276/

3. .NET Core Microservices - The Complete Guide (.NET 6 MVC) (11h 52m)
    - Video: https://learning.oreilly.com/videos/net-core-microservices/9781803247793/

### Visual Studio Code for C#

1. Working with C#
    - https://code.visualstudio.com/docs/languages/csharp

2. Using .NET in Visual Studio Code
    - https://code.visualstudio.com/docs/languages/dotnet

3. VS Code .csproj Extension
    - https://marketplace.visualstudio.com/items?itemName=lucasazzola.vscode-csproj
> This extension will helps you keep your csproj files in sync when using VS Code. <font color='hotpink'>This is useful if you work in a team that uses both VS Code and Visual Studio.</font>

### C# Format / Prettier

- Option #1: add hook to `.pre-commit-config.yaml`
  - https://github.com/GeeWee/resharper-pre-commit-hook
  - Reference: https://www.gustavwengel.dk/csharp-prettier
  - Based on https://github.com/GeeWee/resharper-pre-commit-hook/blob/master/install-git-hook.sh#L12-L16 , it will download ReSharper CLI Tools. (Need to check if it requires license)
- Option #2: There are another tool similar to `gofmt` --> `dotnet-format`
  -  please refer https://randulakoralage82.medium.com/format-your-net-code-with-git-hooks-a0dc33f68048
  - `dotnet tool install -g dotnet-format`

### Solution (.sln) file

- https://learn.microsoft.com/en-us/visualstudio/extensibility/internals/solution-dot-sln-file?view=vs-2022

## 2023-08-11

- ( 2023-08-11 17:09:16 )
- https://code.visualstudio.com/docs/csharp/get-started
- ( 2023-08-11 17:10:32 )
- Install .Net Core SDK using HomeBrew
```bash
~$ brew install dotnet@6
```
- ( 2023-08-11 17:13:18 )
- Install [VS Code C# Dev Kit extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
```bash
~$ code --install-extension ms-dotnettools.csdevkit
```

## 2023-08-14

- ( 2023-08-14 10:15:39 )
- test on Github workspace
```bash
gitpod /workspace/snippet/c# (master) $ curl https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh | bash
gitpod /workspace/snippet/c# (master) $ export PATH=/home/gitpod/.dotnet:$PATH
```
- ( 2023-08-14 11:48:39 )
```bash
gitpod /workspace/snippet/c# (master) $ mkdir hello
gitpod /workspace/snippet/c# (master) $ cd hello/
itpod /workspace/snippet/c#/hello (master) $ dotnet new console

Welcome to .NET 6.0!
---------------------
SDK Version: 6.0.413

Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
Learn about HTTPS: https://aka.ms/dotnet-https
----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
The template "Console App" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on /workspace/snippet/c#/hello/hello.csproj...
  Determining projects to restore...
  Restored /workspace/snippet/c#/hello/hello.csproj (in 97 ms).
Restore succeeded.

gitpod /workspace/snippet/c#/hello (master) $ dotnet --info
.NET SDK (reflecting any global.json):
 Version:   6.0.413
 Commit:    10710f7d8e

Runtime Environment:
 OS Name:     ubuntu
 OS Version:  22.04
 OS Platform: Linux
 RID:         ubuntu.22.04-x64
 Base Path:   /home/gitpod/.dotnet/sdk/6.0.413/

global.json file:
  Not found

Host:
  Version:      6.0.21
  Architecture: x64
  Commit:       e40b3abf1b

.NET SDKs installed:
  6.0.413 [/home/gitpod/.dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 6.0.21 [/home/gitpod/.dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 6.0.21 [/home/gitpod/.dotnet/shared/Microsoft.NETCore.App]

Download .NET:
  https://aka.ms/dotnet-download

Learn about .NET Runtimes and SDKs:
  https://aka.ms/dotnet/runtimes-sdk-info

gitpod /workspace/snippet/c#/hello (master) $ dotnet -h
Usage: dotnet [runtime-options] [path-to-application] [arguments]

Execute a .NET application.

runtime-options:
  --additionalprobingpath <path>   Path containing probing policy and assemblies to probe for.
  --additional-deps <path>         Path to additional deps.json file.
  --depsfile                       Path to <application>.deps.json file.
  --fx-version <version>           Version of the installed Shared Framework to use to run the application.
  --roll-forward <setting>         Roll forward to framework version  (LatestPatch, Minor, LatestMinor, Major, LatestMajor, Disable).
  --runtimeconfig                  Path to <application>.runtimeconfig.json file.

path-to-application:
  The path to an application .dll file to execute.

Usage: dotnet [sdk-options] [command] [command-options] [arguments]

Execute a .NET SDK command.

sdk-options:
  -d|--diagnostics  Enable diagnostic output.
  -h|--help         Show command line help.
  --info            Display .NET information.
  --list-runtimes   Display the installed runtimes.
  --list-sdks       Display the installed SDKs.
  --version         Display .NET SDK version in use.

SDK commands:
  add               Add a package or reference to a .NET project.
  build             Build a .NET project.
  build-server      Interact with servers started by a build.
  clean             Clean build outputs of a .NET project.
  format            Apply style preferences to a project or solution.
  help              Show command line help.
  list              List project references of a .NET project.
  msbuild           Run Microsoft Build Engine (MSBuild) commands.
  new               Create a new .NET project or file.
  nuget             Provides additional NuGet commands.
  pack              Create a NuGet package.
  publish           Publish a .NET project for deployment.
  remove            Remove a package or reference from a .NET project.
  restore           Restore dependencies specified in a .NET project.
  run               Build and run a .NET project output.
  sdk               Manage .NET SDK installation.
  sln               Modify Visual Studio solution files.
  store             Store the specified assemblies in the runtime package store.
  test              Run unit tests using the test runner specified in a .NET project.
  tool              Install or manage tools that extend the .NET experience.
  vstest            Run Microsoft Test Engine (VSTest) commands.
  workload          Manage optional workloads.

Additional commands from bundled tools:
  dev-certs         Create and manage development certificates.
  fsi               Start F# Interactive / execute F# scripts.
  sql-cache         SQL Server cache command-line tools.
  user-secrets      Manage development user secrets.
  watch             Start a file watcher that runs a command when files change.

Run 'dotnet [command] --help' for more information on a command.

gitpod /workspace/snippet/c#/hello (master) $ dotnet build
MSBuild version 17.3.2+561848881 for .NET
  Determining projects to restore...
  All projects are up-to-date for restore.
/home/gitpod/.dotnet/sdk/6.0.413/Roslyn/Microsoft.CSharp.Core.targets(75,5): error MSB6004: The specified task executable location "/run/containerd/io.containerd.runtime.v2.task/k8s.io/6bb9e8b070e52e10f8766ae1d6893187604ce4e8398c84ba311bc6ee2b5625c7/rootfs/home/gitpod/.dotnet/dotnet" is invalid. [/workspace/snippet/c#/hello/hello.csproj]

Build FAILED.

/home/gitpod/.dotnet/sdk/6.0.413/Roslyn/Microsoft.CSharp.Core.targets(75,5): error MSB6004: The specified task executable location "/run/containerd/io.containerd.runtime.v2.task/k8s.io/6bb9e8b070e52e10f8766ae1d6893187604ce4e8398c84ba311bc6ee2b5625c7/rootfs/home/gitpod/.dotnet/dotnet" is invalid. [/workspace/snippet/c#/hello/hello.csproj]
    0 Warning(s)
    1 Error(s)

Time Elapsed 00:00:01.97
```

- ( 2023-08-14 13:23:53 )
- [Learn to program using C#](https://aka.ms/selfguidedcsharp)

- ( 2023-08-14 18:14:34 )
- test https://aka.ms/dotnet-hello-world with https://shell.cloud.google.com/?show=terminal
```bash
~$ dotnet --version
6.0.412
~$ dotnet new console -o MyApp

Welcome to .NET 6.0!
---------------------
SDK Version: 6.0.412

Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
Learn about HTTPS: https://aka.ms/dotnet-https
----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
The template "Console App" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on /home/jazz_innova18/MyApp/MyApp.csproj...
  Determining projects to restore...
  Restored /home/jazz_innova18/MyApp/MyApp.csproj (in 115 ms).
Restore succeeded.


~$ cd MyApp/
~/MyApp$ dotnet run
Hello, World!
```

## 2023-09-04

- ( 2023-09-04 22:03:16 )
- C# REPL
  - Reference: https://dev.to/tallesl/c-repl-gkn
  - https://github.com/filipw/dotnet-script
  ```
  $ dotnet tool install -g dotnet-script
  $ dotnet script
  ```
  - If you are already on .NET 7 you can install csharprepl:
  ```
  $ dotnet tool install -g csharprepl
  $ csharprepl
  ```

## 2024-11-09

- [Setting up a C# (.NET) project for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-dotnet-project-for-codespaces)
