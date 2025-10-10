# Jira JQL

## 2025-10-10

- 需求：查詢最近兩週的異動
- Bing Copilot Search
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
jql last 14 days
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
To create a JQL (Jira Query Language) query for issues related to the **last 14 days**, you can use the `-14d` relative date format. Below are some examples based on common use cases:

* * * *

#### 1\. **Issues Created in the Last 14 Days**

```jql
created >= -14d
```

This query will return all issues that were created within the last 14 days.

* * * *

#### 2\. **Issues Updated in the Last 14 Days**

```jql
updated >= -14d
```

This query will return all issues that were updated within the last 14 days.

* * * *

#### 3\. **Issues Resolved in the Last 14 Days**

```jql
resolved >= -14d
```

This query will return all issues that were resolved within the last 14 days.

* * * *

#### 4\. **Issues Commented On in the Last 14 Days**

Unfortunately, JQL does not natively support filtering by the last comment date. However, if you have an app like **ScriptRunner** or **JXL**, you can use custom JQL functions to achieve this. For example, with ScriptRunner:

```jql
issueFunction in commented("after -14d")
```

If you don't have such plugins, you may need to rely on workarounds like sorting issues by the "Updated" field and manually checking comments.

* * * *

#### 5\. **Issues Due in the Next 14 Days**

```jql
due >= now() AND due <= 14d
```

This query will return all issues that are due within the next 14 days.

* * * *

#### Notes:

-   `-14d` refers to 14 days ago, relative to the current date.
-   `now()` refers to the current date and time.
-   These queries can be combined with other filters, such as project, assignee, status, etc. For example:

    ```jql
    project = "ABC" AND created >= -14d AND status = "In Progress"
    ```

Let me know if you need further clarification or additional examples!
</td></tr></table>

- 參考：
  - https://confluence.atlassian.com/jirasoftwareserver103/advanced-searching-1489806138.html