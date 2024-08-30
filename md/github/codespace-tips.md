# Github Codespace Tips

## 2024-08-28 Codespace Copilot Demo

- 看到 Copilit 的一個 Demo Link 是要我開 https://github.com/github/copilot-codespaces-demo 的 codespace
- 用這個 copilot-codespaces-demo 就可以跑兩個 Copilot 自動補完程式碼的展示。
- 好奇這到底是預先寫好的？還是真的有靠 Copilot 執行。所以研究了一下程式碼，簡單紀錄一下一些發現。
```
jazzwang:~/git/copilot-codespaces-demo$ tree -a
.
├── .devcontainer
│   ├── devcontainer.json
│   ├── icon.png
│   └── welcome-message.txt
├── .git
│   ├── (SKIP)
├── .tours
│   ├── ConvertCommentsToCode.tour
│   └── JSONtoUser.tour
├── CODEOWNERS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── convert_comments_to_code.py
├── json_to_user.py
└── media
    ├── screenshot1.png
    ├── screenshot2.png
    └── screenshot3.png

20 directories, 45 files
```
- 發現一：`.devcontainer/devcontainer.json` 有安裝 Copilot `github.copilot` 延伸套件跟 Tutoral 延伸套件 `vsls-contrib.codetour`
```json showLineNumbers highlightLine=1-5,8
{
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "hostRequirements": {
      "cpus": 4
  },
  "name": "Try Copilot",
  "postCreateCommand": "sudo cp --force ./.devcontainer/welcome-message.txt /usr/local/etc/vscode-dev-containers/first-run-notice.txt",
  "customizations": {
      "vscode": {
      "extensions": [
        "github.copilot",
        "vsls-contrib.codetour",
        "ms-python.python"
      ]}
  }
}
```
- 發現二：`vsls-contrib.codetour` 擴充套件會去讀 `.tours/JSONtoUser.tour` 的檔案來顯示每一步要做什麼。
```json
{
  "$schema": "https://aka.ms/codetour-schema",
  "title": "JSONtoUser",
  "steps": [
    {
      "file": "json_to_user.py",
      "description": "Welcome to your GitHub Copilot tour! We're going to jump right into a common use case for Copilot: helping write boilerplate code. Here you can see an example of the User class, as well as a  JSON representation of a user. \n\n Press `Next` to continue 👇",
      "line": 1
    },
    {
      "file": "json_to_user.py",
      "description": "We can use Copilot to automatically serialize the json into the class. Press __ENTER__ at the end of line 14 to prompt Copilot to generate the boilerplate code, and __TAB__ to accept the generated code. \n\nOnce it's generated the code, press `Next` to continue 👇",
      "line": 14
    },

    {
      "file": "json_to_user.py",
      "description": "We can also use Copilot to  write a function to convert from the class to JSON. Press __ENTER__ at the end of line 18 to prompt Copilot to generate the boilerplate code, and __TAB__ to accept the generated code. \n\nOnce it's generated the code, press `Next` to continue 👇",
      "line": 18
    },
    {
      "file": "json_to_user.py",
      "description": "Thank you for trying out the GitHub JSONtoUser Demo! Try out some new Code Tours in the bottom left panel! If you would like to sign up for Copilot visit here: https://github.com/features/copilot#pricing",
      "line": 42
    }
  ]
}
```
- 看起來 https://aka.ms/codetour-schema 是微軟定義的標準 :P
    - 縮網址指向 https://cdn.jsdelivr.net/gh/microsoft/codetour@main/schema.json 是個 JSON Schema
- 更多關於 Codetour 的實作，可參考 https://github.com/microsoft/codetour

## 2024-08-29 MOAW Codepilot Workshop

- 在找 Copilot Workshop 時看到這些 https://moaw.dev/catalog/?search=copilot
- https://moaw.dev/
    - 微軟縮網址 https://aka.ms/moaw
- https://moaw.dev/workshop/create-workshop/ 有說明怎麼產生 Workshop
- 更多關於 MOAW (喵) 🌳 The Mother Of All Workshops (MOAW)
    - 參考 https://github.com/microsoft/moaw
