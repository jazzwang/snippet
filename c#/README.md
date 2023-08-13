# README

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
- Install [VS Code C# Dev Kit extension]()
```bash
~$ code --install-extension ms-dotnettools.csdevkit
```