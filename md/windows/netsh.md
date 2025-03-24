# netsh

## 2025-03-24

- 緣起：想確認無線網路密碼存在哪裡，是否可以從 regedit 查到。
- 行動：[Is there a way to get saved wifi password from... | Try in Microsoft 365 Copilot](https://www.microsoft365.com/chat/entity1-d870f6cd-4aa5-4d42-9626-ab690c041429/eyJpZCI6IlZYTmxjbFl4ZkdoMGRIQnpPaTh2YzNWaWMzUnlZWFJsTFdsdWRDNXZabVpwWTJVdVkyOXRMM3hQU1VRNll6VXpObVl6TmpRdE1EYzRPUzAwTTJVMExXSTBaamN0WVdaak1qQXlNMlF6WTJRMGZHWTFNMk0yTUdReExXVXdNMll0TkRjeVppMWlPVEZtTFRNMVpqWm1aamcwT1RJM00zd3lNREkxTFRBekxUSTBWREF6T2pNNU9qSTBMakE0TXpjeU56TmEiLCJzY2VuYXJpbyI6InNoYXJlTGlua1ZpYVJpY2hDb3B5IiwicHJvcGVydGllcyI6eyJwcm9tcHRTb3VyY2UiOiJ1c2VyIiwiY2xpY2tUaW1lc3RhbXAiOiIyMDI1LTAzLTI0VDAzOjM5OjIzLjgxMVoifSwiY2hhdFR5cGUiOiJ3ZWIiLCJ2ZXJzaW9uIjoxLjF9)
<table><tr><td>Q:</td><td>
Is there a way to get saved wifi password from regedit?
</td></tr><tr><td>A:</td><td>

The Wi-Fi passwords are not stored directly in the Windows Registry. Instead, they are encrypted in XML files located at `C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces\[Interface Guid]` [[1]](https://community.spiceworks.com/t/how-to-extract-wireless-network-info-from-registry-with-passwords/966143). 

To retrieve saved Wi-Fi passwords, you can use the following methods:

1. **Command Line**:
   - Open Command Prompt or PowerShell.
   - Run `netsh wlan show profiles` to list all saved Wi-Fi networks.
   - Run `netsh wlan show profile name="NETWORK_NAME" key=clear` to display the password for a specific network.

2. **Third-Party Software**:
   - Tools like **NirSoft's WirelessKeyView** can display all saved Wi-Fi passwords on your system [[2]](https://www.howtogeek.com/426257/how-to-see-all-your-pcs-saved-wi-fi-passwords/).

Would you like more detailed instructions on any of these methods?
</td></tr></table>

### `netsh wlan profiles`

- 列出所有已儲存的 Wireless SSID 的 Profile

### `netsh wlan profile name="<SSID>" key=clear`

- 指定特定 SSID，若有權限，可以在 `Key Content` 看到密碼。
- 參考: https://www.howtogeek.com/426257/how-to-see-all-your-pcs-saved-wi-fi-passwords/

![](https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/12/2-example-pw.png)