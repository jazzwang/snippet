# n8n - Workflow automation tool

[TOC]

> Free and source-available fair-code licensed workflow automation tool. Easily automate tasks across different services.

- 官網：https://n8n.io/
- Git Repo: https://github.com/n8n-io/n8n

- **緣起：**
  - 在 [零程式碼建置 AI 智能體！](https://www.youtube.com/watch?v=hE_CeOUY2h0&t=470s) 影片中，看到除了 [LangFlow](https://github.com/langflow-ai/langflow) 或 [Flowise](https://github.com/FlowiseAI/Flowise) 以外，一款用 TypeScript 搭配 Vue.js 寫成的 Workflow automation tool。

## 2024-11-06

### 安裝 Installation

- ( 2024-11-06 22:05:51 )
- 看起來似乎不難，只需要跑 `npx n8n` 就會跑起來了
- 實驗環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet/js/n8n$ gh cs code
? Choose codespace: jazzwang/snippet (master*): snippet
```
- ( 2024-11-06 22:09:00 )
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp
@jazzwang ➜ /tmp $ ls
dockerd.log  sshd.log
@jazzwang ➜ /tmp $ npx n8n
Need to install the following packages:
n8n@1.65.2
Ok to proceed? (y) y

... (ignore) ...

No encryption key found - Auto-generated and saved to: /home/codespace/.n8n/config
Permissions 0644 for n8n settings file /home/codespace/.n8n/config are too wide. This is ignored for now, but in the future n8n will attempt to change the permissions automatically. To automatically enforce correct permissions now set N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true (recommended), or turn this check off set N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=false.
Initializing n8n process
n8n ready on 0.0.0.0, port 5678
Migrations in progress, please do NOT stop the process.
Starting migration InitialMigration1588102412422
Finished migration InitialMigration1588102412422
Starting migration WebhookModel1592445003908
Finished migration WebhookModel1592445003908
Starting migration CreateIndexStoppedAt1594825041918
Finished migration CreateIndexStoppedAt1594825041918
Starting migration MakeStoppedAtNullable1607431743769
Finished migration MakeStoppedAtNullable1607431743769
Starting migration AddWebhookId1611071044839
Finished migration AddWebhookId1611071044839
Starting migration CreateTagEntity1617213344594
Finished migration CreateTagEntity1617213344594
Starting migration UniqueWorkflowNames1620821879465
Finished migration UniqueWorkflowNames1620821879465
Starting migration AddWaitColumn1621707690587
Finished migration AddWaitColumn1621707690587
Starting migration UpdateWorkflowCredentials1630330987096
Finished migration UpdateWorkflowCredentials1630330987096
Starting migration AddExecutionEntityIndexes1644421939510
Finished migration AddExecutionEntityIndexes1644421939510
Starting migration CreateUserManagement1646992772331
Finished migration CreateUserManagement1646992772331
Starting migration LowerCaseUserEmail1648740597343
Finished migration LowerCaseUserEmail1648740597343
Starting migration CommunityNodes1652254514001
Finished migration CommunityNodes1652254514001
Starting migration AddUserSettings1652367743993
Finished migration AddUserSettings1652367743993
Starting migration AddAPIKeyColumn1652905585850
Finished migration AddAPIKeyColumn1652905585850
Starting migration IntroducePinData1654089251344
Finished migration IntroducePinData1654089251344
Starting migration AddNodeIds1658930531669
Finished migration AddNodeIds1658930531669
Starting migration AddJsonKeyPinData1659888469333
Finished migration AddJsonKeyPinData1659888469333
Starting migration CreateCredentialsUserRole1660062385367
Finished migration CreateCredentialsUserRole1660062385367
Starting migration CreateWorkflowsEditorRole1663755770892
Finished migration CreateWorkflowsEditorRole1663755770892
Starting migration WorkflowStatistics1664196174000
Finished migration WorkflowStatistics1664196174000
Starting migration CreateCredentialUsageTable1665484192211
Finished migration CreateCredentialUsageTable1665484192211
Starting migration RemoveCredentialUsageTable1665754637024
Finished migration RemoveCredentialUsageTable1665754637024
Starting migration AddWorkflowVersionIdColumn1669739707124
Finished migration AddWorkflowVersionIdColumn1669739707124
Starting migration AddTriggerCountColumn1669823906993
Finished migration AddTriggerCountColumn1669823906993
Starting migration MessageEventBusDestinations1671535397530
Finished migration MessageEventBusDestinations1671535397530
Starting migration RemoveWorkflowDataLoadedFlag1671726148419
Finished migration RemoveWorkflowDataLoadedFlag1671726148419
Starting migration DeleteExecutionsWithWorkflows1673268682475
Finished migration DeleteExecutionsWithWorkflows1673268682475
Starting migration AddStatusToExecutions1674138566000
Finished migration AddStatusToExecutions1674138566000
Starting migration CreateLdapEntities1674509946020
Finished migration CreateLdapEntities1674509946020
Starting migration PurgeInvalidWorkflowConnections1675940580449
Finished migration PurgeInvalidWorkflowConnections1675940580449
Starting migration MigrateExecutionStatus1676996103000
Finished migration MigrateExecutionStatus1676996103000
Starting migration UpdateRunningExecutionStatus1677237073720
Finished migration UpdateRunningExecutionStatus1677237073720
Starting migration CreateVariables1677501636752
Finished migration CreateVariables1677501636752
Starting migration CreateExecutionMetadataTable1679416281777
Finished migration CreateExecutionMetadataTable1679416281777
Starting migration AddUserActivatedProperty1681134145996
Finished migration AddUserActivatedProperty1681134145996
Starting migration RemoveSkipOwnerSetup1681134145997
Finished migration RemoveSkipOwnerSetup1681134145997
Starting migration MigrateIntegerKeysToString1690000000002
Finished migration MigrateIntegerKeysToString1690000000002
Starting migration SeparateExecutionData1690000000010
Finished migration SeparateExecutionData1690000000010
Starting migration FixMissingIndicesFromStringIdMigration1690000000020
Finished migration FixMissingIndicesFromStringIdMigration1690000000020
Starting migration RemoveResetPasswordColumns1690000000030
Finished migration RemoveResetPasswordColumns1690000000030
Starting migration AddMfaColumns1690000000030
Finished migration AddMfaColumns1690000000030
Starting migration CreateWorkflowNameIndex1691088862123
Finished migration CreateWorkflowNameIndex1691088862123
Starting migration CreateWorkflowHistoryTable1692967111175
Finished migration CreateWorkflowHistoryTable1692967111175
Starting migration ExecutionSoftDelete1693491613982
Finished migration ExecutionSoftDelete1693491613982
Starting migration DisallowOrphanExecutions1693554410387
Finished migration DisallowOrphanExecutions1693554410387
Starting migration AddWorkflowMetadata1695128658538
Finished migration AddWorkflowMetadata1695128658538
Starting migration ModifyWorkflowHistoryNodesAndConnections1695829275184
Finished migration ModifyWorkflowHistoryNodesAndConnections1695829275184
Starting migration AddGlobalAdminRole1700571993961
Finished migration AddGlobalAdminRole1700571993961
Starting migration DropRoleMapping1705429061930
Finished migration DropRoleMapping1705429061930
Starting migration RemoveFailedExecutionStatus1711018413374
Finished migration RemoveFailedExecutionStatus1711018413374
Starting migration MoveSshKeysToDatabase1711390882123
[MoveSshKeysToDatabase1711390882123] No SSH keys in filesystem, skipping
Finished migration MoveSshKeysToDatabase1711390882123
Starting migration RemoveNodesAccess1712044305787
Finished migration RemoveNodesAccess1712044305787
Starting migration CreateProject1714133768519
Finished migration CreateProject1714133768519
Starting migration MakeExecutionStatusNonNullable1714133768521
Finished migration MakeExecutionStatusNonNullable1714133768521
Starting migration AddActivatedAtUserSetting1717498465931
Finished migration AddActivatedAtUserSetting1717498465931
Starting migration AddConstraintToExecutionMetadata1720101653148
Finished migration AddConstraintToExecutionMetadata1720101653148
Starting migration CreateInvalidAuthTokenTable1723627610222
Finished migration CreateInvalidAuthTokenTable1723627610222
Starting migration RefactorExecutionIndices1723796243146
Finished migration RefactorExecutionIndices1723796243146
Starting migration CreateAnnotationTables1724753530828
Finished migration CreateAnnotationTables1724753530828
Starting migration AddApiKeysTable1724951148974
Finished migration AddApiKeysTable1724951148974
Starting migration CreateProcessedDataTable1726606152711
Finished migration CreateProcessedDataTable1726606152711
Starting migration SeparateExecutionCreationFromStart1727427440136
Finished migration SeparateExecutionCreationFromStart1727427440136
Starting migration AddMissingPrimaryKeyOnAnnotationTagMapping1728659839644
Finished migration AddMissingPrimaryKeyOnAnnotationTagMapping1728659839644
Starting migration UpdateProcessedDataValueColumnToText1729607673464
Finished migration UpdateProcessedDataValueColumnToText1729607673464
Version: 1.65.2

Editor is now accessible via:
http://localhost:5678/

Press "o" to open in Browser.
```
- 確實開得起來，啟用的程序有點小繁瑣。要 Email，設定帳號密碼，回答一些行銷目的問卷。

## 2024-11-21

- 2024-11-19: 看到 `n8n` 被定位成 No-Code Workflow Engine
  - [Zapier、Make、n8n，哪個自動化工具更適合你？3 款 NoCode 服務比一比](https://fc.bnext.com.tw/articles/view/3412)
- 想法：
  - Q: 可否拿 n8n 來做會議籌備的跨服務整合呢？
  - Q: 可否把 n8n 跑在 GCP Cloud Run 呢？
  - A: 可以
    - https://github.com/luke-lewandowski/n8n-cloudrun-example - 用 Terraform 佈署 n8n 跟相依的 PostgreSQL 到 Cloud Run
    - https://docs.n8n.io/hosting/installation/server-setups/google-cloud/#clone-configuration-repository - 官方文件（有提到 Cloud Run，但偏向用 GKE 佈署）
