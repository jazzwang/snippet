# Deploy React App to Github Page

## 2024-10-09

- 緣起：小孩寫國語作業需要知道「部首」在國字裡的位置。經查詢，有一個字型可以突顯「部首」的位置。所以想試試看可否部屬一個 React App 到 Github Page
  - [中文如何做出「部首變色」效果？使用免費的課本生詞「曉聲通部首字型」。](https://toneoz.com/blog/2023/03/27/radical/)
  - https://app.intcome.com/public/jy 這個 React App 可以用有注音的字體顯示打出來的中文字
- 作法：
  - 請 Perplexity AI 幫忙：https://www.perplexity.ai/search/how-to-deploy-react-app-to-git-k4WtH02cRruugqs_5hLCTg#0
- ( 2024-10-10 13:48:29 )
- 因為 Github Page 需要獨立的 repo，所以使用 Github CLI 來產生一個新的專案。然後用 CodeSpace 來做開發，就不用在本地端建立 node.js 環境 :P
```
~/git$ gh repo create
? What would you like to do? Create a new repository on GitHub from scratch
? Repository name react-github-page

? Repository name react-github-page
? Repository owner jazzwang
? Description Example React.js App deploy to Github Page

? Description Example React.js App deploy to Github Page
? Visibility Public
? Would you like to add a README file? No
? Would you like to add a .gitignore? No
? Would you like to add a license? No
? This will create "react-github-page" as a public repository on GitHub. Continue? Yes
✓ Created repository jazzwang/react-github-page on GitHub
? Clone the new repository locally? Yes
```