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

## 2026-03-31

- 緣起：想確認 Windows WSL 的 Linux Kernel 參數設定

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
can I find current Linux kernel (runtime) config within `/proc`?
</td></tr></table>

Yes, you absolutely can, though there is a small "if" involved regarding how your specific kernel was compiled.

The primary place to look is **`/proc/config.gz`**.

### How to Access It
Since the file is compressed to save space in memory, you can't just `cat` it and expect readable text. You'll need to decompress it on the fly:

```bash
zcat /proc/config.gz
```

If you are looking for a specific setting (for example, regarding Intel virtualization), you can pipe it to `grep`:

```bash
zcat /proc/config.gz | grep CONFIG_INTEL_IOMMU
```

---

### The "Catch": `CONFIG_IKCONFIG_PROC`
The `/proc/config.gz` file only exists if your kernel was built with the following options enabled:
1.  **`CONFIG_IKCONFIG`**: This embeds the configuration file directly into the kernel binary.
2.  **`CONFIG_IKCONFIG_PROC`**: This surfaces that embedded config through the `/proc` filesystem.

Most major distributions (Ubuntu, Fedora, Arch, etc.) enable this by default because it is incredibly helpful for debugging. However, if you are on a hardened system or a custom minimal build, it might be missing.

---

### Alternatives if `/proc/config.gz` is Missing
If you don't see that file, don't panic. There are two other standard places to find your runtime configuration:

* **The `/boot` directory:** Most package managers save the config file used to build the kernel right next to the kernel image itself.
    * Look for: `/boot/config-$(uname -r)`
* **The `extract-ikconfig` script:** If the config is embedded in the kernel but not shown in `/proc`, you can extract it directly from the kernel image file using a script usually found in the kernel source tree or your distro's "scripts" package.

### Why use `/proc` instead of `/boot`?
The version in `/proc` is the "source of truth." It represents exactly what the **currently running** kernel thinks its config is. While the file in `/boot` is usually identical, if someone manually replaced the kernel binary without updating the `/boot/config-*` file, `/proc` is the only place that will give you the real story.

Are you trying to troubleshoot a specific module issue, or just poking around the kernel internals?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
I'm trying to figure out why self-compile kernel for WSL2 is different from official WSL2. 
I only add config to support HFSplus and it breaks the support of docker within WSL2
</td></tr></table>

It sounds like your custom kernel is missing the specific **cgroups** or **namespace** configurations that Docker requires to function. When you compile a kernel for WSL2, you can't just use a "blank slate" or a generic Linux config—you must use Microsoft's official base configuration as your starting point.

### The Root Cause
Docker relies heavily on kernel features like `Namespaces`, `Control Groups (cgroups)`, and specific `Networking` options. If you simply ran `make menuconfig` on a fresh kernel source and only enabled HFS+, you likely missed hundreds of required flags that Microsoft includes by default in their official WSL2 kernel.

### How to Fix Your Build
To ensure Docker works, you must base your custom kernel on the official Microsoft config:

1.  **Clone the official WSL2 Kernel source:**
    ```bash
    git clone https://github.com/microsoft/WSL2-Linux-Kernel.git
    cd WSL2-Linux-Kernel
    ```
2.  **Use the official Microsoft config as your `.config`:**
    ```bash
    cp Microsoft/config-wsl .config
    ```
    *This step is critical. It ensures all Docker-essential flags are present.*
3.  **Add HFSplus support:**
    ```bash
    make menuconfig
    ```
    * Navigate to **File systems** -> **Miscellaneous filesystems**.
    * Select **Apple Macintosh file system support (HFS+ support)**.
4.  **Recompile and Swap:**
    * Compile: `make -j$(nproc)`.
    * Copy the resulting `arch/x86/boot/bzImage` to your Windows host.
    * Update your `%USERPROFILE%\.wslconfig` to point to the new image.

---

### Verifying the Difference
If you want to see exactly what is missing that broke Docker, you can compare your "broken" config with the official one:

* **Official Config:** Found at `Microsoft/config-wsl` in the source tree.
* **Your Current Config:** Run `zcat /proc/config.gz > my_config` in your current WSL instance.

Use a tool like `diff` or `vimdiff` to compare them:
```bash
diff Microsoft/config-wsl my_config | grep "not set"
```
You will likely see many `CONFIG_CGROUP` or `CONFIG_NETFILTER` options that are set in the official version but missing in yours.

### Pro-Tip: Docker Desktop vs. Native Docker
If you are using **Docker Desktop**, it is particularly sensitive to custom kernels and is not "officially" supported with them. If the above steps don't fix it, ensure `CONFIG_LOCALVERSION` in your kernel config is set to something recognizable (e.g., `-microsoft-standard-HFS+`) so you can verify with `uname -a` that WSL is actually loading your new kernel and hasn't reverted to a backup.