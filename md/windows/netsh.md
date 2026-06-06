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

## 2026-06-06

- 狀況：
  - 家裡的光世代在用 MS Teams 甚至一些影音串流的平台 (YouTube, Netflix, 甚至天下雜誌用 KKCompany  的 BlendVision) 都會遇到偶發性的斷線
- 徵狀：
  - 有時候會整個 WiFi 會直接斷線（訊號還在，Windows 系統列的狀態直接顯示「斷線」）
  - 有時候會顯示 DNS 無法反查。
- 問題排查：
  - 一直有點懷疑是預設 IPv6 DNS 的問題，因為 `ipconfig /all` 的結果，IPv6 DNS 的優先順序高於 IPv4 DNS。
  - 曾經透過修改 Registry 的方式，試圖改成 IPv4 優先。

### netsh interface ipv6 show prefixpolicies

```powershell
PS C:\WINDOWS\system32> netsh interface ipv6 show prefixpolicies
Querying active state...

Precedence  Label  Prefix
----------  -----  --------------------------------
        50      0  ::ffff:0:0/96
        40      1  ::1/128
        30      2  ::/0
        20      3  2002::/16
         5      5  2001::/32
         3     13  fc00::/7
         1     11  fec0::/10
         1     12  3ffe::/16
         1      4  ::/96
```

### netsh interface ipv6 reset

```powershell
PS C:\WINDOWS\system32> netsh interface ipv6 reset
Resetting Compartment Forwarding, OK!
Resetting Compartment, OK!
Resetting Control Protocol, OK!
Resetting Echo Sequence Request, OK!
Resetting Global, OK!
Resetting Interface, OK!
Resetting Anycast Address, OK!
Resetting Multicast Address, OK!
Resetting Unicast Address, OK!
Resetting Neighbor, OK!
Resetting Path, OK!
Resetting Potential, OK!
Resetting Prefix Policy, OK!
Resetting Proxy Neighbor, OK!
Resetting Route, OK!
Resetting Site Prefix, OK!
Resetting Subinterface, OK!
Resetting Wakeup Pattern, OK!
Resetting Resolve Neighbor, OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , failed.
Access is denied.

Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Restart the computer to complete this action.
```

### netsh interface ipv4 reset

```powershell
PS C:\WINDOWS\system32> netsh interface ipv4 reset
Resetting Compartment Forwarding, OK!
Resetting Compartment, OK!
Resetting Control Protocol, OK!
Resetting Echo Sequence Request, OK!
Resetting Global, OK!
Resetting Interface, OK!
Resetting Anycast Address, OK!
Resetting Multicast Address, OK!
Resetting Unicast Address, OK!
Resetting Neighbor, OK!
Resetting Path, OK!
Resetting Potential, OK!
Resetting Prefix Policy, OK!
Resetting Proxy Neighbor, OK!
Resetting Route, OK!
Resetting Site Prefix, OK!
Resetting Subinterface, OK!
Resetting Wakeup Pattern, OK!
Resetting Resolve Neighbor, OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , failed.
Access is denied.

Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Resetting , OK!
Restart the computer to complete this action.
```

### netsh interface ipv4

```powershell
PS C:\WINDOWS\system32> netsh interface ipv4

The following commands are available:

Commands in this context:
?              - Displays a list of commands.
add            - Adds a configuration entry to a table.
delete         - Deletes a configuration entry from a table.
dump           - Displays a configuration script.
help           - Displays a list of commands.
install        - Install the IP protocol.
reset          - Reset the IP configurations.
set            - Sets configuration information.
show           - Displays information.
uninstall      - Uninstall the IP protocol.

To view help for a command, type the command, followed by a space, and then
 type ?.
```