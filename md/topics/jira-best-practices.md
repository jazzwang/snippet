# Jira Best Practices

## Days in column

### 2025-04-26

- 緣起：
  - 在「實體看板」，我們是靠在便利貼上點白板筆代表一天。
  - 本來想要找以前看過，讓每張卡片下方出現不同顏色的圓點，來顯示該張卡片停留在同一個階段多久。
    - 確認術語叫做「Days in column」
- 參考文件：
  - https://support.atlassian.com/jira-software-cloud/docs/customize-cards/#Customizingcards-UsingDaysincolumn
  - https://stackoverflow.com/questions/47163826/days-in-column-dots-explanation
    - 這個 StackOverview 提到兩個問題：
    -https://jira.atlassian.com/browse/JSWCLOUD-16004 這個功能只剩下雲版本才有？
    - https://jira.atlassian.com/browse/JSWSERVER-11847 把週末算進工作日（這個當初確實有用過）
- 變通作法：
  - 在目前的界面上有看到可以根據 JQL 改變卡片顏色的作法
  - 這篇文章有完整的範例
    - https://medium.com/@surjitjandu/visualising-work-item-aging-in-jira-23fa7affa97b
  - 範例 JQL
    ```jql
    statusCategory = "In Progress" AND statusCategory ChangedDate <= -11d
    statusCategory = "In Progress" AND statusCategory ChangedDate <= -7d
    statusCategory = "In Progress" AND statusCategoryChangedDate <= -3d
    statusCategory = "In Progress" AND statusCategory ChangedDate > -3d
    ```

## Jira Project Types

| Application | Project type | Application specific feature set |
| --- |  --- |  --- |
| Jira Core | <img src='https://confluence.atlassian.com/jirasoftwareserver0904/files/1188766485/1188766488/1/1600423910215/business_projects.png' height='24'> Business projects | -   Available to all licensed users |
| Jira Software | <img src='https://confluence.atlassian.com/jirasoftwareserver0904/files/1188766485/1188766487/1/1600423910132/service_desk.png' height='24'> Software projects | -   Integration with development tools-   Agile boards-   Release hub for software versions |
| Jira Service Management | <img src='https://confluence.atlassian.com/jirasoftwareserver0904/files/1188766485/1188766486/1/1600423909923/software_projects.png' height='24'> Service projects | -   Service Level Agreements (SLAs)-   A customizable web portal for customers-   Permission schemes allowing customer access |

## Workstream

- 最近想要把同一個 container 的不同團隊切分出來，像以前有多一個 `Workstream` 的欄位。在 Jira 的欄位裡有一個 `Team` 的預設欄位，但是看起來是綁定 `Bamboo` 的團隊設定。

## Bulk Upload

- 以前 Program Manager 很厲害，提供了 Excel 範本讓大家可以先在 Excel 裡面共同編輯，然後一次把整個 PI 六個 Sprint 的工作一次估完，包括每個 Sprint 的 capacity，可工作日/假日/休假天數，然後還可以方便大家在填入 User Story 估算以後，計算是否超出 Sprint Capacity，也會預留 10%~20% 不等的 Buffer 時間，因應 PI 執行到一半時，有一開始沒想到的額外 blocker 跑出來。
- 最近用 User Story 的 Bulk Upload，發現似乎不能根據已經存在的 KEY (Issue Key) 去更新想要修改的欄位。
- 最近團隊的 Test Case 也是用 Bulk Upload 產生，只是用的是 "Import".

## Jira Zephyr

- https://www.getzephyr.com
- https://smartbear.com/test-management/zephyr/

## JQL

### 2025-08-30

- Copilot Search Branding

> [!NOTE]
> jql linked issues type is bug

To filter issues in Jira using JQL (Jira Query Language) where the linked issues are of type "Bug," you can use the following query:

```jql
issueFunction in linkedIssuesOf("issuetype = Bug")
```

**Explanation**:

- `issueFunction` in `linkedIssuesOf`: This function identifies issues linked to other issues that match the specified JQL query.
- `"issuetype = Bug"`: This filters for linked issues specifically of the type "Bug."

Notes:

- The `issueFunction` feature is part of Jira's ScriptRunner plugin. If you don't have ScriptRunner installed, this query won't work. Unfortunately, Jira's native JQL does not support filtering directly by linked issue types without plugins.
- If you need a workaround without plugins, you might need to manually tag or label issues for easier filtering.

Let me know if you need further clarification! 😊
---

> [!NOTE]
> "issueFunction" site:atlassian.com

##### IssueFunction Documentation in JQL

**IssueFunction** is a powerful feature in Jira Query Language (JQL) that allows users to perform advanced searches by leveraging custom functions. These functions can be used to retrieve specific subsets of issues based on relationships, workflows, or custom criteria. Below are key details and examples of how IssueFunction can be utilized effectively.

Common Use Cases and Syntax

1\. Subtasks of Specific Issues

The *subtasksOf* function retrieves all subtasks of parent issues that match a given query. This is particularly useful for filtering subtasks based on the parent issue's attributes.

**Syntax:**

```
issueFunction in subtasksOf("JQL Query")
```

**Example:** To find subtasks of issues in project "DI" with the status "New":

```
issueFunction in subtasksOf("project = DI AND status = 'New'")
```

2\. Linked Issues

The *linkedIssues* function identifies issues linked to a specific issue or set of issues. You can also specify the type of link.

**Syntax:**

```
issueFunction in linkedIssues(issueKey, "LinkType")
```

**Example:** To find issues linked to "ABC-123" via the "blocks" link type:

```
issueFunction in linkedIssues("ABC-123", "blocks")
```

3\. Epics and Subtasks

The *epicsOf* and *subtasksOf* functions allow you to search for epics or subtasks based on specific criteria.

**Example:** To find all subtasks of epics in project "XYZ":

```
issueFunction in subtasksOf("project = XYZ AND issuetype = Epic")
```

4\. Combining Multiple Criteria

You can combine multiple criteria using logical operators like *AND*, *OR*, and *NOT*.

**Example:** To find subtasks of issues with multiple statuses:

```
issueFunction in subtasksOf("status IN ('New', 'In Progress', 'Done')")
```

Advanced Tips

-   **Nested Queries:** You can nest JQL queries within IssueFunction to refine results further.

-   **Performance Optimization:** Use specific fields and conditions to narrow down the search scope and improve query performance.

-   **Custom Fields:** IssueFunction works seamlessly with custom fields, allowing tailored searches for unique workflows.

Limitations and Considerations

-   **Permissions:** Ensure you have the necessary permissions to access the issues and fields referenced in your query.

-   **Case Sensitivity:** Field names and values in JQL are case-sensitive.

-   **Dependencies:** Some functions may require plugins like ScriptRunner to be available in your Jira instance.

By leveraging IssueFunction, you can create highly customized and efficient queries to manage and analyze issues in Jira effectively.

Learn more:
- [1 -support.atlassian.com](https://www.bing.com/ck/a?!&&p=1885ee14dad20c7af1eb5047db362203070ab332bbfa152a52fdcdc47e69861bJmltdHM9MTc1NjUxMjAwMA&ptn=3&ver=2&hsh=4&fclid=0a592b39-b9e4-62d4-30f0-3d75b83f6368&u=a1aHR0cHM6Ly9zdXBwb3J0LmF0bGFzc2lhbi5jb20vamlyYS1zb2Z0d2FyZS1jbG91ZC9kb2NzL2pxbC1mdW5jdGlvbnMv&ntb=1)
- [2 -community.atlassian.com](https://www.bing.com/ck/a?!&&p=3884da28c5ec3c52d26ebc58648d1674325d009913b8f474c8414dcee065083aJmltdHM9MTc1NjUxMjAwMA&ptn=3&ver=2&hsh=4&fclid=0a592b39-b9e4-62d4-30f0-3d75b83f6368&u=a1aHR0cHM6Ly9jb21tdW5pdHkuYXRsYXNzaWFuLmNvbS9mb3J1bXMvSmlyYS1xdWVzdGlvbnMvSG93LXRvLXdyaXRlLWEtSlFMLXVzaW5nLUlzc3VlRnVuY3Rpb24tdG8tc2hvdy1hbGwtU3ViLXRhc2tzLW9mL3FhcS1wLzcwNTQwOQ&ntb=1)
- [3 -confluence.atlassian.com](https://www.bing.com/ck/a?!&&p=b0fceff8429333d7e4aee6207c07cf6481a5f107125bef74480ae07a9e61add8JmltdHM9MTc1NjUxMjAwMA&ptn=3&ver=2&hsh=4&fclid=0a592b39-b9e4-62d4-30f0-3d75b83f6368&u=a1aHR0cHM6Ly9jb25mbHVlbmNlLmF0bGFzc2lhbi5jb20vc2VydmljZW1hbmFnZW1lbnRzZXJ2ZXIxMDMvYXNzZXRzLWpxbC1mdW5jdGlvbnMtMTQ4ODU5NjQzMS5odG1s&ntb=1)
---
