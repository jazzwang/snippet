# OpenSearch CLI

- Created with 2.5 Flash May 27, 2025 at 11:54 AM
- https://g.co/gemini/share/3b57f8bc02c7

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Are there CLI tool for OpenSearch?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, OpenSearch provides several command-line interface (CLI) tools for managing your cluster and performing various tasks:

1.  **OpenSearch CLI (`opensearch-cli`)**:

    -   This is a general-purpose CLI for managing your OpenSearch cluster.
    -   It supports various functionalities, including interacting with plugins like Anomaly Detection and k-NN, and making arbitrary REST API calls to your cluster.
    -   You can use it for tasks like creating/deleting detectors, starting/stopping them, and checking k-NN statistics.
    -   It supports different authentication types, including unauthenticated requests, HTTP basic signing, and IAM signing for AWS.
    -   It uses profiles to easily switch between different clusters or credentials.
2.  **SQL and PPL CLI (`opensearchsql`)**:

    -   This is a standalone Python application specifically for interacting with the OpenSearch SQL and PPL (Piped Processing Language) plugins.
    -   It offers features like multi-line input, autocomplete for SQL syntax and index names, syntax highlighting, and formatted output.
    -   You can use it to run SQL and PPL queries against your OpenSearch instance.
    -   It works with or without security enabled and supports loading configuration files.
3.  **OpenSearch Reporting CLI (`@opensearch-project/reporting-cli`)**:

    -   This CLI tool allows you to programmatically create and download reports (in PDF or PNG format) from OpenSearch Dashboards without needing to use the Dashboards UI directly.
    -   It's useful for automating report generation, such as sending reports via email.
    -   It can be installed via npm.

**In summary, if you're looking for a general-purpose tool to manage your OpenSearch cluster and interact with its APIs and plugins, `opensearch-cli` is the way to go. If your primary need is to run SQL and PPL queries from the command line, then the `opensearchsql` CLI is what you're after. And for automating report generation, the `reporting-cli` is available.**

OpenSearch aims to provide a unified command-line interface in the future to integrate these different CLIs into a single tool, making the user experience even smoother.
</td></tr></table>

## OpenSearch CLI

- Git Repo
  - https://github.com/opensearch-project/opensearch-cli
- Document
  - https://docs.opensearch.org/docs/latest/tools/cli/

### Install - Linux

- 到 https://opensearch.org/downloads/#command-line-tools 查
- 在 Github Codespace 上測試
```bash
@jazzwang ➜ /workspaces/snippet (master) $ wget https://artifacts.opensearch.org/opensearch-clients/opensearch-cli/opensearch-cli-1.2.0-linux-x64.zip
@jazzwang ➜ /workspaces/snippet (master) $ unzip opensearch-cli-1.2.0-linux-x64.zip 
Archive:  opensearch-cli-1.2.0-linux-x64.zip
  inflating: opensearch-cli          
@jazzwang ➜ /workspaces/snippet (master) $ ./opensearch-cli 
opensearch-cli is a unified command line interface for managing OpenSearch clusters

Usage:
  opensearch-cli [command]

Available Commands:
  ad          Manage the Anomaly Detection plugin
  completion  Generate completion script for your shell
  curl        Manage OpenSearch platform features
  help        Help about any command
  knn         Manage the k-NN plugin
  profile     Manage a collection of settings and credentials that you can apply to an opensearch-cli command

Flags:
  -c, --config string    Configuration file for opensearch-cli, default is /home/codespace/.opensearch-cli/config.yaml
  -h, --help             Help for opensearch-cli
  -p, --profile string   Use a specific profile from your configuration file
  -v, --version          Version for opensearch-cli

Use "opensearch-cli [command] --help" for more information about a command.
```

### Install - Windows

- 到 https://opensearch.org/downloads/#command-line-tools 查
- 在 Windows 11 上實測
```bash
jazzw@JazzBook:~$ wget https://artifacts.opensearch.org/opensearch-clients/opensearch-cli/opensearch-cli-1.2.0-windows-x64.zip
jazzw@JazzBook:~$ unzip opensearch-cli-1.2.0-windows-x64.zip
Archive:  opensearch-cli-1.2.0-windows-x64.zip
  inflating: opensearch-cli.exe
jazzw@JazzBook:~$ ./opensearch-cli.exe
opensearch-cli is a unified command line interface for managing OpenSearch clusters

Usage:
  opensearch-cli [command]

Available Commands:
  ad          Manage the Anomaly Detection plugin
  completion  Generate completion script for your shell
  curl        Manage OpenSearch platform features
  help        Help about any command
  knn         Manage the k-NN plugin
  profile     Manage a collection of settings and credentials that you can apply to an opensearch-cli command

Flags:
  -c, --config string    Configuration file for opensearch-cli, default is C:\Users\jazzw\.opensearch-cli\config.yaml
  -h, --help             Help for opensearch-cli
  -p, --profile string   Use a specific profile from your configuration file
  -v, --version          Version for opensearch-cli

Use "opensearch-cli [command] --help" for more information about a command.
```