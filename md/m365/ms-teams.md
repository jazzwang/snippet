# Microsoft Teams

## 2025-06-21

- 需求: 整合 n8n 跟 Microsoft Teams

### Incoming Webhook

- Create incoming webhooks with Workflows for Microsoft Teams
  - https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498
- 備註：
  - 這個作法也用在跟 Jira Cloud 整合上

### Outgoing Webhook

- Create Outgoing Webhooks
  - https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-outgoing-webhook
- 備註：
  - 這個作法可以拿來觸發 n8n 事件，看起來是付費版 Microsoft Workflow Premium 的 `HTTP` 替代方案。#TODO

## 2025-08-24

- Create a team from an existing team or group in Microsoft Teams
  - https://support.microsoft.com/en-us/office/create-a-team-from-an-existing-team-or-group-in-microsoft-teams-f41a759b-3101-4af6-93bd-6aba0e5d7635
  ![](https://support.microsoft.com/images/en-us/aded9510-611f-404b-b8c7-8640be112c86?format=avif&w=800)
  ![](https://support.microsoft.com/images/en-us/149b4d28-50b2-436a-ba1c-a6c55c21ca3d?format=avif&w=800)
  ![](https://support.microsoft.com/images/en-us/a8e9aa40-18d3-4e20-9e2a-820a7165031f?format=avif&w=800)
  - Create a team from a group: 
    1. Choose **From a group** and then choose from the available Microsoft 365 Groups.  You'll see a list of groups you own, don't have a team connected to them, and have less than 10,000 members.
    2. Select a group and a team with the same name will be created automatically. The team will share the same group privacy, sensitivity and members as the original group.

    > [!NOTE]
    > - This option is not available for groups that have more than 10,000 members or that were already used to create another team.
    > - Groups associated with Viva Engage communities can't be converted to a team.