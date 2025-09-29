# Mounting a USB Drive in WSL

- 2025-10-06
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