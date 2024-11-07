# Slidev

> Presentation Slides for Developers

- https://sli.dev/
- Git Repo: https://github.com/slidevjs/slidev

## 2024-11-07

- 緣起：
  - 在 [Better Bolt + FREE Mistral & Github API : STOP PAYING for V0 & BOLT with this FULLY FREE Alternative](https://www.youtube.com/watch?v=p_tyWtQZx48) 學到 [V0](https://v0.dev/) 跟 [Bolt.new](https://github.com/stackblitz/bolt.new)
  - 在 https://bolt.new/ 下方看到一個 prompt `Draft a presentation with Slidev`
  - 所以查一下 Slidev 跟 Reveal.js 兩者的差異。
- 比較：
  - https://sli.dev/guide/why#comparisons
  - 我想差異最大的地方，確實就是 Reveal.js 多數狀況得要熟悉 HTML 跟 CSS 語法來達成一些效果。對於想要專注用 Markdown 製作投影片的人來說，會比較吃力一點。至於 Vue, Vite 跟 CSS 這些優勢，我可能還暫時還用不到。

> [Reveal.js](https://revealjs.com/) is a popular HTML presentation framework. It is also open source and supports Markdown.
> 
> Compared to Reveal.js, Slidev has the following advantages:
>
> -   More concise: Slidev uses an extended Markdown format, while <mark>Reveal.js encourages you to write HTML</mark> to organize your slides.
> -   Vue support: You can use Vue components in Slidev to make your slides interactive.
> -   Vite-based: Slidev is built on top of Vite, which provides instant HMR and flexible plugin API.
> -   Atomatic CSS: You can [UnoCSS](https://unocss.dev/) out of the box to style your slides.

- 我覺得比較特殊的地方應該是對於程式碼行號等的支援
  - https://sli.dev/features/shiki-magic-move
- 甚至可以作到 hover 到特定物件上可以顯示些資訊（註：看起來只支援 TypeScript/JavaScript 程式碼解說的投影片）
  - https://sli.dev/features/twoslash
- 比較有趣的是 slidev 用 Playwright 來匯出成 PDF
  - https://sli.dev/guide/exporting
- 從 Demo Slide 看起來，特效是蠻多的。Eye Candy 很多。（像是 Notation 畫底線，手繪感覺的畫圈）
  - https://sli.dev/demo/starter/
- 要 Host slidev 雖然有 github page 可以選，不過感覺有那麼點小複雜。需要嘗試才知道好不好用。
  - https://sli.dev/guide/hosting

### Installation

- 參考文件：https://sli.dev/guide/
- 測試環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet/js/slidev$ gh cs code
? Choose codespace: jazzwang/snippet (master*): snippet
```
- 雖然文件不建議單一個檔案的 markdown，不過相信剛開始只需要單一檔案即可
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ npm i -g @slidev/cli

added 686 packages in 1m

200 packages are looking for funding
  run `npm fund` for details
@jazzwang ➜ /tmp $ touch slides.md
@jazzwang ➜ /tmp $ slidev slides.md 
✔ The theme "@slidev/theme-default" was not found globally, do you want to install it now? … yes

added 4 packages in 2s

4 packages are looking for funding
  run `npm fund` for details


  ●■▲
  Slidev  v0.50.0-beta.5 (global)

  theme       @slidev/theme-default
  css engine  unocss
  entry       /tmp/slides.md

  public slide show   > http://localhost:3030/
  presenter mode      > http://localhost:3030/presenter/
  slides overview     > http://localhost:3030/overview/
  remote control      > pass --remote to enable

  shortcuts           > restart | open | edit | quit
```
- 當我修改 `slides.md` 內容時，開啟的 http://localhost:3030/ 內容會跟著變。當然需要一點時間重新 render 修改。
- 例如：我在 `slides.md` 輸入如下內容：
```md
# Topic

## this is a test
```
- 網頁就會變成
- 某種程度上，是還蠻合理的（我相信 Vue 應該類似 React ，所以用 Frontend 的角度去思考，這樣的設計就不意外了）。
- 但這種設計比較不像我用 `Markdown Preview Enhanced` 的預覽功能那麼直觀。要額外開一個瀏覽器，總覺得有點多餘。
- 簡單評測到此，後續應該還是會先用 reveal.js 的一些語法來寫投影片。