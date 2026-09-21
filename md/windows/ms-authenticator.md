# Microsoft Authenticator

## 2026-09-21

> [!QUESTION]
> 換手機時,如何重新取得 Microsoft 365 MFA organization QR code?

換手機時，若需要重新取得 Microsoft 365 MFA（多重身份驗證）的組織 QR code 來綁定新手機，主要取決於您目前是否還能登入公司/學校帳戶。
請依照您的實際狀況，選擇以下對應的解決步驟：

### 情況一：還能登入帳戶（仍可透過舊手機、簡訊或信任設備登入）

如果您還能透過其他方式（例如：舊手機還在、能收簡訊驗證碼，或在已經信任的電腦上）登入 Microsoft 365，您可以自己重新產生 QR code：

   1. 前往設定頁面： 在電腦上開啟瀏覽器，登入微軟的 [我的登入資訊 (My Sign-Ins)](https://mysignins.microsoft.com/security-info) 頁面。
   2. 新增驗證方法： 點擊 「+ 新增登入方法」，並在下拉選單中選擇 「驗證器應用程式」。
   3. 在新手機操作： 打開新手機上的 [Microsoft Authenticator](https://learn.microsoft.com/zh-tw/entra/identity/authentication/how-to-transfer-authenticator-new-phone)，點擊 「+ 新增帳戶」 > 選擇 「工作或學校帳戶」 > 點擊 「掃描 QR 代碼」。
   4. 掃描並完成： 用新手機掃描電腦螢幕上出現的全新 QR code，並配合完成一次畫面上的數字核准測試即可。
   5. (安全提醒)：成功綁定新手機後，請記得在同一個網頁中，將「舊手機」的驗證裝置名稱刪除。 [1, 2, 3]

### 情況二：完全無法登入（舊手機已無法使用，且無其他驗證方式）

如果您因為換手機，現在完全卡在登入畫面（畫面要求輸入驗證碼，但您收不到），您自己是無法取得 QR code 的。 [4, 5]

* 唯一的解決方法：聯絡您公司或學校的「IT 管理員」。 [4, 5]
* 管理員需要做的事：
請 IT 管理員登入 [Microsoft 365 系統管理中心 (Microsoft 365 admin center)](https://learn.microsoft.com/zh-cn/answers/questions/5107684/microsoft-authenticator-qr)，找到您的使用者帳號，並為您執行「要求重新登冊多重要素驗證」（重置 MFA）。 [5]
* 重置後的結果： 當管理員重置完成後，您下一次在電腦上登入 Microsoft 365 時，系統就會自動跳出全新的 QR code 綁定畫面，您就能直接用新手機掃描了。 [3, 5]

### 💡 實用小撇步：如何避免下次換手機這麼麻煩？

如果您使用的是 Microsoft Authenticator，建議平時就開啟雲端備份功能，這樣下次換手機時可以直接從雲端還原，不需要重新掃描組織的 QR code： [6]

* iPhone (iOS)： 開啟 App 內的「設定」> 啟用 「iCloud 備份」。
* Android： 開啟 App 內的「設定」> 啟用 「雲端備份」 並連結您的個人微軟帳戶（如 Hotmail / Outlook）。
* 注意：換到新手機時，在尚未登入任何帳戶前，先點擊畫面下方的 「從備份還原」 即可快速轉移。 [6, 7]

[1] [https://support.microsoft.com](https://support.microsoft.com/zh-tw/authenticator/how-to-add-your-accounts-to-microsoft-authenticator)
[2] [https://cc.csmu.edu.tw](https://cc.csmu.edu.tw/p/404-1028-71437.php?Lang=zh-tw)
[3] [https://mail.cch.org.tw](https://mail.cch.org.tw/MFA%E9%A9%97%E8%AD%89%E6%8F%9B%E6%89%8B%E6%A9%9F%E7%B6%81%E5%AE%9A%E6%95%99%E5%AD%B8/MFA2.html)
[4] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/answers/questions/4549684/qr)
[5] [https://learn.microsoft.com](https://learn.microsoft.com/zh-cn/answers/questions/5107684/microsoft-authenticator-qr)
[6] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/entra/identity/authentication/how-to-transfer-authenticator-new-phone)
[7] [https://support.microsoft.com](https://support.microsoft.com/zh-tw/authenticator/restore-account-credentials-from-microsoft-authenticator)

## 實測

- 筆電端：
  - STEP 1: https://mysignins.microsoft.com/security-info
  - STEP 2: 點擊「+ 新增登入方法」()，然後選「Microsoft Authenticator」
- 手機端：
  - STEP 1: 安裝 Microsoft Authenticator
  - STEP 2: 如果有個人 live.com / hotmail.com 帳號，在舊手機登入，選擇備份資料。到新手機一樣登入，選擇還原，就會有多數的 MFA。但是企業用戶 Microsoft 365 不能還原，必須重新掃描 QR Code。這時候在筆電端先做上述步驟，理論上會顯示 QR Code
  - STEP 3: 點選還原後需要額外掃描 QR Code 的帳號，對著筆電螢幕上的 QR Code 就可以將新筆電加入企業帳號的 MFA Device 清單中。
