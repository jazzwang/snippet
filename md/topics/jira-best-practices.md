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