# OpenSearch CLI

- 2025-05-27 at 11:54 AM
- 
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