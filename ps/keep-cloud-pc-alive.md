# Powershell Script to keep Cloud PC available after disconnected

- 緣起：
  - 需要開分身聽 MS Teams Meeting (純做會議紀錄用)
- 限制：Azure Cloud PC 會在 Windows App 或 Client 斷線後，自動登出
- 需求：怎麼讓 Cloud PC 不要自動登出呢？可否每一段時間送出某個特殊鍵盤事件？
- 2025-07-25 9:56 AM @ Gemini 2.5 Flash
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how to send numlock key every 5 seconds using powershell?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You can send the NumLock key every 5 seconds using PowerShell by utilizing the `SendKeys` method from the .NET Framework's `System.Windows.Forms` namespace. Here's a script that accomplishes this:

```powershell
Add-Type -AssemblyName System.Windows.Forms

while ($true) {
    # Send the NumLock key
    [System.Windows.Forms.SendKeys]::SendWait("{NUMLOCK}")
    Write-Host "NumLock key sent at $(Get-Date)"

    # Wait for 5 seconds
    Start-Sleep -Seconds 5
}
```

**Explanation:**

1.  **`Add-Type -AssemblyName System.Windows.Forms`**: This line loads the `System.Windows.Forms` assembly, which contains the `SendKeys` class necessary to simulate keyboard input.
2.  **`while ($true)`**: This creates an infinite loop, causing the script to continuously send the NumLock key.
3.  **`[System.Windows.Forms.SendKeys]::SendWait("{NUMLOCK}")`**: This is the core command.
      * `[System.Windows.Forms.SendKeys]` accesses the `SendKeys` class.
      * `::SendWait()` is a static method that sends the specified keystrokes to the active application and waits for them to be processed.
      * `"{NUMLOCK}"` is the special key code for the NumLock key. `SendKeys` uses curly braces `{}` to represent special keys.
4.  **`Write-Host "NumLock key sent at $(Get-Date)"`**: This line is optional but helpful for debugging and confirmation. It prints a message to the console indicating when the NumLock key was sent, along with the current timestamp.
5.  **`Start-Sleep -Seconds 5`**: This command pauses the script execution for 5 seconds before the loop reiterates and sends the NumLock key again.

**How to use it:**

1.  Open PowerShell.
2.  Copy and paste the script into the PowerShell console.
3.  Press Enter to run it.

To stop the script, press `Ctrl+C` in the PowerShell console.

**Important Considerations:**

  * **Active Window:** `SendKeys` sends keys to the **currently active window**. If you switch to another application, the NumLock key will be sent to that application.
  * **Administrative Privileges:** In most cases, you won't need administrative privileges for this script, but if you encounter issues with applications not responding, try running PowerShell as an administrator.
  * **Security:** Be cautious when using `SendKeys` in more complex scripts, as it can potentially interfere with user input or trigger unintended actions if not managed carefully.
  * **Alternative (Less Common for this specific task):** For more robust and controlled automation, especially in scenarios where you need to interact with specific UI elements regardless of the active window, consider using UI automation libraries like `WinAppDriver` (for Windows applications) or `Selenium` (for web browsers) if your goal extends beyond just toggling NumLock. However, for simply sending the NumLock key, `SendKeys` is the most straightforward approach.
</td></tr></table>

- 實測：直接在 Cloud PC 的 Powershell 視窗貼上以下程式碼：

```powershell
Add-Type -AssemblyName System.Windows.Forms

while ($true) {
    # Send the NumLock key
    [System.Windows.Forms.SendKeys]::SendWait("{NUMLOCK}")
    Write-Host "NumLock key sent at $(Get-Date)"

    # Wait for 5 minutes
    Start-Sleep -Seconds 300
}
```
