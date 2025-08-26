# Jira Best Practices

## 2025-04-26
## Days in column

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