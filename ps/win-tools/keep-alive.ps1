## 讓 AVD / IWS 不要進入螢幕保護程式的 PowerShell script
## 註：每 3 秒送出 ScrollLock 按鍵
$wsh = New-Object -ComObject WScript.Shell
while (1) {$wsh.SendKeys('{SCROLLLOCK}'); sleep 3000}
