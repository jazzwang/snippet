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

## 2026-03-31

- 如何查詢某一個 Sub-initiative 底下的 Feature
> type = Epic AND issue in linkedIssues("BUDGETCY26-123456")

- 參考：https://www.testmanagement.com/blog/2023/09/using-jira-jql-to-search-for-related-issues/

> issue in linkedIssues("SCR-26")

這篇文章也有提到可以查 Child

> parent = SCR-10

> parent in (SCR-26, SCR-10)

- 其他參考：
  - Jira JQL: advanced search queries made easy
    - https://www.valiantys.com/en/resources/jql
  - How can I search for all tickets that have issue links to another project?
    - https://community.atlassian.com/forums/Jira-questions/How-can-I-search-for-all-tickets-that-have-issue-links-to/qaq-p/1231423
    - Will all issues which are linked or links project JQL
        > issue in linkedByIssueProject("JQL")
    - Find issues which link at least one issue from project JQL. 
        > issue in links("project = JQL")
    - Find issues which "blocks" at least one issue from project JQL. 
        > issue in links("blocks", "project = JQL")

## 2026-04-12

- 緣起：想查 "Feature Link" (= "Epic Link") 底下的所有 Story
- 查詢：Gemini
- 結果：
  ```jql
  "Epic Link" in (ABC-XXX, ABC-YYY, ABC-ZZZ)
  ```
- 參考：

Finding Stories within a specific Epic in Jira is a common task, but the JQL (Jira Query Language) syntax depends slightly on whether you are using **Jira Cloud** or **Jira Data Center/Server**.

### 1\. The Standard Method (Jira Cloud)

In Jira Cloud, Epics and Stories are linked via the **Parent** field. This is the most reliable way to pull your list.

**The Query:**

`parent = [Epic-Key]`

-   **Example:** `parent = PROJ-123`
-   **Refined search (to ensure you only get Stories):** `parent = PROJ-123 AND issuetype = Story`

### 2\. The Traditional Method (Jira Data Center / Server)

Older versions of Jira (and some specific configurations) use a custom field called **Epic Link**.

**The Query:**

`"Epic Link" = [Epic-Key]`

-   **Example:** `"Epic Link" = PROJ-123`
-   **Note:** You must use quotation marks around "Epic Link" because of the space in the field name.

### 3\. Dynamic Searching (Advanced)

If you don't have the specific key handy or want to search for Stories belonging to multiple Epics based on criteria (like a name), you can use functions or broader filters.

| **Goal** | **JQL Syntax** |
| --- |  --- |
| **Search by Epic Name** | `parent in membersOf("Epic Name")` *(Cloud)* |
| **Stories in "Done" Epics** | `parent in (leaflets(status = Done))` |
| **Multiple Epics** | `parent in (PROJ-123, PROJ-456, PROJ-789)` |

### Pro-Tips for Clean Results

-   **Order by Status:** Add `ORDER BY status ASC` to the end of your query to see what is still "In Progress" versus "Done."
-   **Exclude Sub-tasks:** If your Stories have sub-tasks and you *only* want the Stories, add `AND issuetype != Sub-task`.

> **Check your field name:** If `parent` doesn't work, start typing `Epic` into the JQL search bar; Jira's auto-complete will usually suggest the correct field name (like `Epic Link` or `cf`) used in your specific instance.

Which version of Jira are you currently using, and are you trying to export this list or just view it in a dashboard?
