# Chrome Extensions

- 緣起：
  - 原本想要找能否從 Dev Tool Console 就可以把網頁存成 MHTML 的作法
  - 結果找到 Chrome Extension 有一個 pageCapture 的 API
    - https://developer.chrome.com/docs/extensions/reference/api/pageCapture
  - 其次，最近有一些常用的 Chrome Extension 都被標記成未來將從 [Chrome Web Store](https://chromewebstore.google.com/category/extensions) 下架的警告。
    所以想了解一下怎麼修改，使其合規。初步理解是 Manifest v3 跟 
    > These extensions may soon no longer be supported
      Remove or replace them with similar extensions from the [Chrome Web Store](https://chromewebstore.google.com/category/extensions)
- 看起來要學習 Chrome Extension 開發，可以從 https://developer.chrome.com/docs/extensions 開始

## 2025-01-02

- 緣起：最近使用中的某幾個 chrome extensions 被標註成不再支援
- https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3
![Manifest V3 migration timeline](https://developer.chrome.com/static/images/mv3-timeline_856.png)
- ( 2025-01-02 16:29:43 )
- 根據 https://developer.chrome.com/docs/extensions/develop/migrate/checklist 第一步是
  - [Change the manifest version number](https://developer.chrome.com/docs/extensions/develop/migrate/manifest#change-version)
```diff
diff --cc manifest.json
index af8b92b,06af4b0..08e61c5
--- a/manifest.json
+++ b/manifest.json
@@@ -1,7 -1,7 +1,7 @@@
  {
        "name": "Tracking Token Stripper",
-       "version": "2.10",
-       "manifest_version": 2,
+       "version": "2.12",
 -      "manifest_version": 2,
++      "manifest_version": 3,
        "author": "Jon Parise",
        "description": "Removes Google Analytics (UTM) parameters, and various other click tracking tokens, from URL query strings.",
        "homepage_url": "https://github.com/jparise/chrome-utm-stripper",
```
- 改過 manifest version number 之後，確實就不會警告「將不被支援」
- 出現新的 error
  - 'background.scripts' requires manifest version of 2 or lower.
  - 'webRequestBlocking' requires manifest version of 2 or lower.
  - Permission 'https://*/*?*' is unknown or URL pattern is malformed.
  - Permission 'http://*/*?*' is unknown or URL pattern is malformed.
- ( 2025-01-02 16:36:40 )
- 第二步是 [Update host permissions](https://developer.chrome.com/docs/extensions/develop/migrate/manifest#update-host-permissions)
```diff
diff --git a/manifest.json b/manifest.json
index 08e61c5..e6d71cb 100644
--- a/manifest.json
+++ b/manifest.json
@@ -14,7 +14,9 @@
        },
        "permissions": [
                "webRequest",
-               "webRequestBlocking",
+               "webRequestBlocking"
+       ],
+       "host_permissions": [
                "https://*/*?*",
                "http://*/*?*"
        ]
```
- ( 2025-01-02 16:40:08 )
- 修改後，剩下兩個 Error
  - 'background.scripts' requires manifest version of 2 or lower.
  - 'webRequestBlocking' requires manifest version of 2 or lower.
- ( 2025-01-02 16:43:45 )
- 根據 https://developer.chrome.com/docs/extensions/develop/migrate/blocking-web-requests#block-a-single-url
  - 把 `webRequestBlocking` 改成 `declarativeNetRequest`
```diff
diff --git a/manifest.json b/manifest.json
index 08e61c5..d29fd44 100644
--- a/manifest.json
+++ b/manifest.json
@@ -14,7 +14,9 @@
        },
        "permissions": [
                "webRequest",
-               "webRequestBlocking",
+               "declarativeNetRequest"
       ],
       "host_permissions": [
                "https://*/*?*",
                "http://*/*?*"
        ]
```
- ( 2025-01-02 16:49:51 )
- 根據 https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers#update-bg-field
  - 把 `background.scripts` 改成 `background.service_worker`
```diff
diff --git a/manifest.json b/manifest.json
index 08e61c5..f3567cf 100644
--- a/manifest.json
+++ b/manifest.json
@@ -10,11 +10,13 @@
                "128" : "icon-128.png"
        },
        "background": {
-               "scripts": ["background.js"]
+               "service_worker": "background.js"
        },
        "permissions": [
                "webRequest",
```
- 改完之後，錯誤訊息變成：
> Unchecked runtime.lastError: You do not have permission to use blocking webRequest listeners. Be sure to declare the webRequestBlocking permission in your manifest. Note that webRequestBlocking is only allowed for extensions that are installed using ExtensionInstallForcelist.

**Context**
> Unknown

**Stack Trace**
> :0 (anonymous function)

- 所以看起來要改 background.js 裡面，呼叫 `chrome.webRequest.onBeforeRequest.addListener()` 的寫法。
- 看了一下兩份文件：
  - https://developer.chrome.com/docs/extensions/reference/api/webRequest
    - 嘗試把 `blocking` 改成 `asyncBlocking` [失敗]
    > Uncaught TypeError: Error at parameter 'extraInfoSpec': Error at index 0: Value must be one of blocking, extraHeaders, requestBody.
    - 改成 `requestBody` 還是不對。
    - 改成 `extraHeaders` 還是沒效。
  - https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest
    - 感覺要把原本 `background.js` 的正規表示法，改寫成 declarativeNetRequest 的 `Rule`
    - ( 2025-01-02 17:16:09 )
    - 先改到這兒。下回再戰～