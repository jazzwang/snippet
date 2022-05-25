# README

## 2022-05-23

- Q: How can I get the `Teams` list of a user?
- A:
  - https://docs.microsoft.com/en-us/answers/questions/283171/how-can-i-get-the-list-of-teams-a-user-belongs-to.html
    - using Microsoft Graph PowerShell - https://docs.microsoft.com/en-us/graph/powershell/installation
    ```
    $user = get-MgUser -Filter "DisplayName eq '<User Name>'"
    get-MgUserJoinedTeam -UserId $user.Id
    ```
    - using  https://docs.microsoft.com/en-us/powershell/module/teams/
    ```
    Get-Team -User user@domain.com
    ```

## 2022-05-25

- Install Microsoft Teams cmdlet
- https://www.powershellgallery.com/packages/MicrosoftTeams/