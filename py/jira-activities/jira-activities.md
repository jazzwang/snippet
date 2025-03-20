# MEMO

## RESTful API

### Authentication

- https://developer.atlassian.com/server/jira/platform/basic-authentication/#construct-the-authorization-header
    - Build a string of the form `username:password`.
    - Encode the string to `Base64`.
    - Supply an authorization header with format Authorization: Basic {encoded-string}. Make sure to replace {encoded-string} with your encoded string from Step 2.
- 產生 `Base64` 字串的方式
```python
import base64
print base64.b64encode "username:password"
```
  - 注意：Python 2.7 與 Python 3.x 的 base64 輸入參數不同，前者是 [string](https://docs.python.org/2/library/base64.html)，後者是 [bytes-like object](https://docs.python.org/3/library/base64.html)
```
Python 2.7.16 (default, Jun  5 2020, 22:59:21)
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> base64.b64encode("abc")
'YWJj'
>>> exit()
-----------------------------------------------------------
Python 3.7.3 (default, Apr 24 2020, 18:51:23)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> base64.b64encode(b"abc")
b'YWJj'
>>> quit()
```
- https://stackoverflow.com/questions/18241077/base-64-encoding-with-scala-or-java
```scala
scala> import java.nio.charset.StandardCharsets
import java.nio.charset.StandardCharsets

scala> import java.util.Base64
import java.util.Base64

scala> Base64.getEncoder.encodeToString("user:pass".getBytes(StandardCharsets.UTF_8))
res3: String = dXNlcjpwYXNz
```
- 採用基本認證(Basic Authentication)的 RESTful API 測試語法
```
~$ curl -s -k -H "Authorization: Basic ${base64_string}" https://issues.apache.org/jira/rest/api/2/myself | jq .
{
  "self": "https://issues.apache.org/jira/rest/api/2/user?username=jazzwang",
  "key": "jazzwang",
  "name": "jazzwang",
  "avatarUrls": {
    "48x48": "https://issues.apache.org/jira/secure/useravatar?ownerId=jazzwang&avatarId=23991",
    "24x24": "https://issues.apache.org/jira/secure/useravatar?size=small&ownerId=jazzwang&avatarId=23991",
    "16x16": "https://issues.apache.org/jira/secure/useravatar?size=xsmall&ownerId=jazzwang&avatarId=23991",
    "32x32": "https://issues.apache.org/jira/secure/useravatar?size=medium&ownerId=jazzwang&avatarId=23991"
  },
  "displayName": "Yao-Tsung Wang",
  "active": true,
  "timeZone": "Asia/Taipei",
  "locale": "en_UK",
  "groups": {
    "size": 1,
    "items": []
  },
  "applicationRoles": {
    "size": 1,
    "items": []
  },
  "expand": "groups,applicationRoles"
}
```

### JIRA Version

```
~$ curl -s -k https://issues.apache.org/jira/rest/api/2/serverInfo | jq .
{
  "baseUrl": "https://issues.apache.org/jira",
  "version": "8.3.4",
  "versionNumbers": [
    8,
    3,
    4
  ],
  "deploymentType": "Server",
  "buildNumber": 803005,
  "buildDate": "2019-09-13T00:00:00.000+0000",
  "databaseBuildNumber": 803005,
  "scmInfo": "1f96e09b3c60279a408a2ae47be3c745f571388b",
  "serverTitle": "ASF JIRA"
}
```

### JIRA Activity RSS

- 要注意像是 `evans_ye` 會變成 `evans%5C_ye` ，所以需要額外處理特殊字元 `_` 變成 `%5C_`
```
curl -s -k -H "Authorization: Basic ${base64_string}" https://issues.apache.org/jira/activity?maxResults=10&streams=user+IS+evans%5C_ye&os_authType=basic&title=undefined
```
- 可以直接用 curl 指令把 RSS XML 結果存成檔案
```
~/git/snippet/python/jira-activities$ curl -s -k -H "Authorization: Basic ${base64_string}" "https://issues.apache.org/jira/activity?maxResults=300&streams=user+IS+jayunit100&os_authType=basic&title=undefined" -o jayunit100.xml
```