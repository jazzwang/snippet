# Notes from Databricks Assistant

## 2025-06-16

### Databricks Access Token

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you show me where to create my databricks token?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
To create a Databricks personal access token, follow these steps:

1.  In your Databricks workspace, click your Databricks username in the top bar, and then select **Settings** from the drop-down menu.
2.  Click **Developer**.
3.  Next to **Access tokens**, click **Manage**.
4.  Click **Generate new token**.
5.  Enter a comment that helps you to identify this token in the future.
6.  Set the token's lifetime in days. If you leave the Lifetime (days) box empty, the token lifetime is set to the maximum lifetime for your workspace. By default, the maximum token lifetime for a workspace is 730 days.
7.  Click **Generate**.
8.  Copy the displayed token to a secure location, and then click **Done**.

Be sure to save the copied token in a secure location. Do not share your copied token with others. If you lose the copied token, you cannot regenerate that exact same token. Instead, you must repeat this procedure to create a new token. If you lose the copied token, or you believe that the token has been compromised, Databricks strongly recommends that you immediately delete that token from your workspace by clicking the trash can (Revoke) icon next to the token on the Access tokens page.

If you are not able to create or use tokens in your workspace, this might be because your workspace administrator has disabled tokens or has not given you permission to create or use tokens [[1]](https://docs.databricks.com/aws/en/dev-tools/auth/pat).

- [1] [Databricks personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat)
</td></tr></table>

- 術語：PAT = `Personal Access Token`

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
How do I configure the Databricks CLI with my personal access token?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
To configure the Databricks CLI with your personal access token, follow these steps:

1.  **Install the Databricks CLI**:
    -   If you haven't already installed the Databricks CLI, you can do so by following the installation instructions in the Databricks documentation.
2.  **Generate a Personal Access Token**:
    -   Before configuring the CLI, you need to generate a personal access token from your Databricks workspace. Follow the steps to create a token as described in the Databricks documentation.
3.  **Configure the CLI**:
    -   Open your terminal or command prompt.
    -   Run the following command to start the configuration process:
```bash
databricks configure
```
-   When prompted, enter your Databricks workspace instance URL. For example:
```bash
Databricks Host (should begin with 
https://): https://dbc\-xxx\-xxxx.cloud.databricks.com
```
-   When prompted, enter your personal access token:
```bash
Personal Access Token: <your-personal-access-token>
```
4.  **Verify the Configuration**:
    -   After entering the required information, the CLI will create a configuration profile in your .databrickscfg file, typically located in your home directory.
    -   You can verify the configuration by running a simple Databricks CLI command, such as listing the clusters:
```bash
databricks clusters list
```
If you want to create a configuration profile with a specific name, you can use the \--profile option. For example:

```bash
databricks configure --profile my-profile
```

Then follow the same prompts to enter your Databricks host URL and personal access token.

This process will add the configuration profile to your `.databrickscfg` file, allowing you to use the Databricks CLI with your personal access token for authentication [[1]](https://docs.databricks.com/aws/en/dev-tools/auth/pat) [[2]](https://docs.databricks.com/aws/en/dev-tools/cli/authentication).

- [1] [Databricks personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat) 
- [2] [Authentication for the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/authentication)
</td></tr></table>

## Databricks CLI

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
</td></tr></table>
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
</td></tr></table>

## Databricks Tutorials

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
</td></tr></table>