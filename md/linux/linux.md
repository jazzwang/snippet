# Linux

## 2024-12-16

- https://people.math.ethz.ch/~michele/mutt-oauth2-outlook
- https://movementarian.org/blog/posts/a-headless-office-365-proxy/

## 2024-12-31

- 有人在 DRBL Sourceforge 論壇詢問怎麼讓 Diskless Client 也可以使用 Network Bonding
- Ubuntu Network Binding
  - https://help.ubuntu.com/community/UbuntuBonding
  - https://roychou121.github.io/2021/02/04/ubuntu-network-bond/
- 2016 進 TenMax 後，我就改用 macOS 了。這 8.5 年來 Ubuntu 確實也改變了許多。
  - 像是新的 snap 套件管理，netplan 網路管理
  - https://ubuntu.com/core/docs/networkmanager/networkmanager-and-netplan
  - https://zonego.tw/2022/12/25/ubuntu22-netsetting/
- 最近有點好奇 Debian Maintainer / Debian Developer (DD) 人數上是否有衰退的現象。

## 2025-01-08

- 緣起：筆電電池開始老化得有點嚴重，所以查一下怎麼用 command line 查電池的狀態。
- 參考：
  - https://www.cyberciti.biz/faq/check-see-laptop-battery-health-in-linux-command/
  - https://www.linuxjournal.com/content/how-check-battery-status-using-linux-command-line

- List the current device paths using the upower command:

  ```bash
  upower --enumerate
  ```
  Note down the battery path:

  ```bash
  /org/freedesktop/UPower/devices/line_power_AC
  /org/freedesktop/UPower/devices/battery_BAT0
  /org/freedesktop/UPower/devices/mouse_dev_CD_27_F1_E6_00_B3
  /org/freedesktop/UPower/devices/mouse_hidpp_battery_10
  /org/freedesktop/UPower/devices/DisplayDevice
  ```

  Say your device path is battery_BAT0 as follows from the --enumerate option:

  ```bash
  upower -i /org/freedesktop/UPower/devices/battery_BAT0
  ```

  This will list all of the power source information on your system, including your battery health status in Linux.
  
- You can also use acpi command to print battery information in Linux. For example:

  ```bash
  acpi -b
  ```

- You can also try the inxi command which is a command line system information tool made for console users. Try installing it first and then pass the `-B` or `--battery` option to see the system battery data, charge, condition at the CLI. The syntax is:

```
$inxi --battery
$inxi -B
```

Outputs:

```
Battery:
  ID-1: BAT0 charge: 40.6 Wh condition: 46.7/50.5 Wh (93%)
```