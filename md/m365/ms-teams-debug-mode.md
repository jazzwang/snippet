# MS Teams Debug Mode (DevTool-like)

## 2025-07-03

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
is it possible to open chrome devtool-like console of Microsoft Teams?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, it is absolutely possible to open a Chrome DevTools-like console for Microsoft Teams, especially for debugging purposes. The exact method depends on whether you're using the web version or the desktop client (and if it's the "new" Teams client or the "classic" one).

Here's a breakdown based on the information available:

**For Microsoft Teams Web Version:**

If you're using Teams in a web browser (like Chrome, Edge, or Firefox), you can simply use the browser's built-in developer tools.

  * **Windows:** Press `F12` or `Ctrl+Shift+I`.
  * **macOS:** Press `Command+Option+I`.

This will open the standard browser developer tools, giving you access to the console, elements, network, etc., for the Teams web application.

**For Microsoft Teams Desktop Client (Windows - New Teams):**

The "New" Microsoft Teams client uses Edge WebView2 as its host, so the process is a bit different than the classic client.

1.  **Enable Public Preview:** You might need to enable "Public preview" in your Teams settings.
2.  **Create `configuration.json` file:**
      * Navigate to: `%localappdata%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams`
      * Create a new file named `configuration.json` in this directory.
      * Add the following content to the file:
        ```json
        {
          "core/devMenuEnabled": true
        }
        ```
      * Save the file.
3.  **Restart Teams:** Make sure to fully quit Teams (right-click the icon in the system tray and select "Quit") and then reopen it.
4.  **Open Dev Tools:**
      * Right-click the Microsoft Teams icon in the system tray.
      * You should now see an "Engineering Tools" menu.
      * Under "Engineering Tools," select "Open Dev Tools." This will open a separate Edge Developer Tools window.

**For Microsoft Teams Desktop Client (macOS - New Teams):**

The process on macOS is generally more straightforward:

1.  **Open the app/tab you want to debug.**
2.  **Right-click (or Ctrl + Click) on the app/tab area.**
3.  In the context menu that appears, you should see an "Inspect" option. Clicking this will open the Edge developer tools for that specific part of the Teams client.

**For Microsoft Teams Desktop Client (Windows - Classic Teams - Older Method):**

In the classic Teams client, there was a "secret" method:

1.  Make sure Teams is running in the background.
2.  Locate the Teams icon in your system tray (you might need to click the "show hidden icons" arrow).
3.  **Left-click the Teams icon 6 times quickly.**
4.  On the **seventh click, right-click** the Teams icon.
5.  A special menu should appear with "DevTools" options. Select "Open DevTools (Main Window)" or similar.

**For Android and iOS Clients:**

  * **Android:** DevTools are available on the beta version of the Teams app. You'll need to enable "Public preview" and then connect your device to your desktop for remote debugging via `chrome://inspect/#devices` in your Chrome browser.
  * **iOS:** This involves more prerequisites, including a Mac system with Safari, Teams iOS version 6.10.0 or later, enabling "targeted release" for your user/tenant, activating developer preview in the app, and enabling Web Inspector on your Mac. You'll then use Safari's "Develop" menu to inspect the Teams app.

**What you can do with the Dev Tools:**

  * View console logs (errors, warnings, custom messages).
  * Inspect and modify HTML and CSS during runtime.
  * Monitor network requests.
  * Add breakpoints to JavaScript code for interactive debugging.

Keep in mind that Microsoft might change these methods with updates to Teams. If you encounter issues, always check the official Microsoft Teams developer documentation for the most up-to-date instructions.
</td></tr></table>

- 實測：
  - 啟用 `"core/devMenuEnabled": true`
```bash
~/git/snippet$ cmd
C:\Users\jazzw>cd %localappdata%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams

C:\Users\jazzw\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams>dir
 Volume in drive C is OS
 Volume Serial Number is C04F-8CF9

 Directory of C:\Users\jazzw\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams

06/10/2025  06:52 PM    <DIR>          .
09/12/2024  02:26 PM    <DIR>          ..
07/03/2025  01:54 PM             1,511 app_settings.json
10/02/2024  11:28 AM    <DIR>          Backgrounds
06/10/2025  11:02 AM             1,232 cmd_settings.json
07/03/2025  08:44 AM                14 crash_reports_cache.json
07/03/2025  02:22 PM    <DIR>          EBWebView
07/01/2025  06:29 PM               274 ecs_request_param.json
07/03/2025  02:09 PM         2,117,664 ecs_settings.dat64
07/03/2025  01:44 PM    <DIR>          Logs
07/03/2025  02:09 PM               704 previous_session_data.json
07/01/2025  04:28 PM    <DIR>          tfl
07/03/2025  08:44 AM    <DIR>          tfw
02/04/2025  10:59 AM               142 uae.json
02/03/2025  10:23 AM    <DIR>          UserAvatarIcons
               7 File(s)      2,121,541 bytes
               8 Dir(s)  736,728,449,024 bytes free

C:\Users\jazzw\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams>code configuration.json

C:\Users\jazzw\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams>type configuration.json
{
  "core/devMenuEnabled": true
}
C:\Users\jazzw\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams>
```
- 重開 Teams