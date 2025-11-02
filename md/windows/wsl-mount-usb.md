# Mounting a USB Drive in WSL

## 2025-10-06
- By Microsoft Bing

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
mount usb drive wsl2
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
### Mounting a USB Drive in WSL

[1]: https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk
[2]: https://learn.microsoft.com/en-us/windows/wsl/connect-usb
[3]: https://woshub.com/mount-drives-in-wsl/

Mounting a USB drive in Windows Subsystem for Linux (WSL) can be achieved using the *usbipd-win* project, as the *`wsl --mount`* command does not support USB/flash drives/SD card readers. Below are the steps to mount a USB drive in WSL:

#### Prerequisites

1.  **Windows 11 (Build 22000 or later)**: Ensure your system is up-to-date.

2.  **WSL Installed**: Ensure WSL is installed and set up with the latest version.

3.  **USBIPD-WIN Project**: Install the `usbipd-win` project to enable USB device support in WSL.

#### Installing USBIPD-WIN

-   **Download and Install**: Go to the latest release page for the `usbipd-win` project and download the `.msi` installer file. Run the installer to set up the project.

-   **Using Winget**: Alternatively, you can install it using Windows Package Manager (winget) with the command:

```powershell
winget install --interactive --exact dorssel.usbipd-win
```

#### Attaching a USB Device

-   **List USB Devices**: Open **PowerShell in administrator mode** and list all USB devices connected to Windows:

```powershell
usbipd list
```

-   **Bind the USB Device**: Share the device by binding it using the bus ID obtained from the previous step:

```powershell
usbipd bind --busid <busid>
```

-   **Attach the USB Device**: Attach the USB device to WSL:

```powershell
usbipd attach --wsl --busid <busid>
```

-   **Verify Attachment**: Open your **WSL** distribution and verify the attached USB device using:

```bash
lsusb
```

#### Accessing the USB Drive

Once the USB device is attached, you can interact with it using normal Linux tools within your WSL distribution. Depending on your application, you may need to configure *udev* rules to allow non-root users to access the device.

#### Detaching the USB Device

When you are done using the USB device in WSL, you can either physically disconnect the USB device or run the following command from PowerShell:

```powershell
usbipd detach --busid <busid>
```

By following these steps, you can successfully mount and access a USB drive in WSL, enabling you to perform various tasks such as flashing an Arduino or accessing a smartcard reader
</td></tr></table>

- 2025-05-01:
  - https://blog.tian.it/mount-access-physical-disks-and-usb-devices-into-wsl2/
- https://github.com/lil-greasy/mount-a-drive-in-wsl
- 發現一個有趣的服務：
  - https://deepwiki.com/MicrosoftDocs/WSL/4.2-mounting-disks

## 2025-11-02

- 實測：
  - 先在 PowerShell 裡下 `usbipd` 指令
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\jazzw> usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-4    322e:2233  USB2.0 HD UVC WebCam                                          Not shared
2-3    13d3:3571  Realtek Bluetooth Adapter                                     Not shared
2-5    174c:55aa  USB Attached SCSI (UAS) Mass Storage Device                   Not shared

Persisted:
GUID                                  DEVICE
eaadba8d-084b-4ef2-899e-d2a0021a26e3  USB Mass Storage Device

PS C:\Users\jazzw> usbipd attach --wsl --busid 2-5
usbipd: info: Using WSL distribution 'Ubuntu' to attach; the device will be available in all WSL 2 distributions.
usbipd: info: Loading vhci_hcd module.
usbipd: info: Detected networking mode 'nat'.
usbipd: info: Using IP address 172.29.64.1 to reach the host.
PS C:\Users\jazzw> usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-4    322e:2233  USB2.0 HD UVC WebCam                                          Not shared
2-3    13d3:3571  Realtek Bluetooth Adapter                                     Not shared
2-5    174c:55aa  USB Attached SCSI (UAS) Mass Storage Device                   Attached

Persisted:
GUID                                  DEVICE
eaadba8d-084b-4ef2-899e-d2a0021a26e3  USB Mass Storage Device

PS C:\Users\jazzw>
```
- 原本在 WSL 裡面用 `lsblk` 看不到外接硬碟，不過拔掉 USB 重接，在 PowerShell (Admin) 裡再下一次 `usbipd attach --wsl --busid 2-5` 就看到新的裝置 `/dev/sde`
```bash
~$ lsblk
NAME
    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda   8:0    0 388.4M  1 disk
sdb   8:16   0   186M  1 disk
sdc   8:32   0     4G  0 disk [SWAP]
sdd   8:48   0     1T  0 disk /var/lib/docker
                              /snap
                              /mnt/wslg/distro
                              /
~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 388.4M  1 disk
sdb      8:16   0   186M  1 disk
sdc      8:32   0     4G  0 disk [SWAP]
sdd      8:48   0     1T  0 disk /var/lib/docker
                                 /snap
                                 /mnt/wslg/distro
                                 /
sde      8:64   0 931.5G  0 disk
├─sde1   8:65   0   200M  0 part
└─sde2   8:66   0 931.2G  0 part
```
- 這次裝的不是 EXT4 格式的硬碟，而是 HFS+ 的 macOS 備份碟。
```bash
~$ sudo parted
Warning: Unable to open /dev/sda read-write (Read-only file system).  /dev/sda has been opened read-only.
GNU Parted 3.6
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.

(parted) print all
Model: Msft Virtual Disk (scsi)
Disk /dev/sda: 407MB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags:

Number  Start  End    Size   File system  Flags
 1      0.00B  407MB  407MB  ext2


Warning: Unable to open /dev/sdb read-write (Read-only file system).  /dev/sdb has been opened read-only.
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 195MB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags:

Number  Start  End    Size   File system  Flags
 1      0.00B  195MB  195MB  ext2


Model: Msft Virtual Disk (scsi)
Disk /dev/sdc: 4295MB
Sector size (logical/physical): 512B/4096B
Partition Table: loop
Disk Flags:

Number  Start  End     Size    File system     Flags
 1      0.00B  4295MB  4295MB  linux-swap(v1)


Model: Msft Virtual Disk (scsi)
Disk /dev/sdd: 1100GB
Sector size (logical/physical): 512B/4096B
Partition Table: loop
Disk Flags:

Number  Start  End     Size    File system  Flags
 1      0.00B  1100GB  1100GB  ext4


Model: ASMT 2115 (scsi)
Disk /dev/sde: 1000GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name                  Flags
 1      20.5kB  210MB   210MB   fat32        EFI System Partition  boot, esp
 2      210MB   1000GB  1000GB  hfs+


(parted) exit
```
- 參考 https://superuser.com/a/365270
- 安裝 hfsprogs
```bash
~$ sudo apt-get install hfsprogs
```
- 準備掛載點 `/mnt/usb/macos`
```bash
~$ sudo mkdir -p /mnt/usb/macos
```
```bash
~$ sudo fdisk -l /dev/sde
Disk /dev/sde: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: 2115
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 8D3C86F6-373B-4634-81F0-4DA7B002AEB0

Device      Start        End    Sectors   Size Type
/dev/sde1      40     409639     409600   200M EFI System
/dev/sde2  409640 1953262983 1952853344 931.2G Apple HFS/HFS+
```