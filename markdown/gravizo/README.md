# Graphviz 線上服務

## 緣起

以前喜歡用 [Trac](https://trac.edgewall.org/) 並且搭配它的 [Graphviz](https://graphviz.org/) 擴充元件。這樣就可以在 Wiki 裡面直接鑲嵌 [Graphviz](https://graphviz.org/) 語法，然後靠後端的指令產生對應的圖片。好處是能**版本控制**圖片的內容，其次是用語法就可以產生圖片，很常用來畫一些像是 Debian package 的相依性啦～後來也常用來畫 [Homebrew](https://brew.sh/) 的相依性。

隨著撰寫筆記的習慣從 Wiki 語法轉變成 Markdown 語法，漸漸地也不再需要用 VPS 自架靜態網站，Github 或 Gitlab 都已經提供很好的 Markdown 支援，不過用 Markdown 直接繪圖倒是仍有些不方便。

## 解法

網路上有許多可以透過 javascript 產生 UML 圖或者類似 graphviz 圖的工具。
- [PlantUML](https://plantuml.com/) 就提供了直接產生多種 UML 圖的服務，也算是裡面看過支援種類最廣的一個實作。
  - [UMLGraph](https://www.spinellis.gr/umlgraph/) 相對支援的種類就少一些
- [Viz.js](http://viz-js.com/) 看起來則提供了很不錯的 Grpahviz 支援
  - 原始碼：https://github.com/mdaines/viz.js
  - 不過這個 git repo 已經設為 Archived (代表不再活躍維護)
  - CDN: https://cdnjs.com/libraries/viz.js/2.1.2

搜尋相關實作時，發現了 [Gravizo](http://www.gravizo.com/) 的服務。
- 優點：Github 也可以直接鑲嵌
- 缺點：每張圖都有「Gravizo」的 Logo

## 範例

- 使用 HTML 語法
```html
<img src='https://g.gravizo.com/svg?
 digraph G {
   main -> parse -> execute;
   main -> init;
   main -> cleanup;
   execute -> make_string;
   execute -> printf
   init -> make_string;
   main -> printf;
   execute -> compare;
 }
'/>
```

- 結果

  <img src='https://g.gravizo.com/svg?
  digraph G {
    main -> parse -> execute;
    main -> init;
    main -> cleanup;
    execute -> make_string;
    execute -> printf
    init -> make_string;
    main -> printf;
    execute -> compare;
  }
  '/>

- 使用 Markdown 語法 - 必須使用複製圖片網址的方式

```
![](https://g.gravizo.com/svg?digraph%20G%20{%20%20main%20-%3E%20parse%20-%3E%20execute;%20%20main%20-%3E%20init;%20%20main%20-%3E%20cleanup;%20%20execute%20-%3E%20make_string;%20%20execute%20-%3E%20printf%20%20init%20-%3E%20make_string;%20%20main%20-%3E%20printf;%20%20execute%20-%3E%20compare;})
```

- 結果

![](https://g.gravizo.com/svg?digraph%20G%20{%20%20main%20-%3E%20parse%20-%3E%20execute;%20%20main%20-%3E%20init;%20%20main%20-%3E%20cleanup;%20%20execute%20-%3E%20make_string;%20%20execute%20-%3E%20printf%20%20init%20-%3E%20make_string;%20%20main%20-%3E%20printf;%20%20execute%20-%3E%20compare;})

- 拿來試一下 homebrew 相依圖

![](https://g.gravizo.com/source/brew-dep?https%3A%2F%2Fraw.githubusercontent.com%2Fjazzwang%2Fsnippet%2Fmaster%2Fmarkdown%2Fgravizo%2FREADME.md)

<details>
<summary></summary>
brew-dep
digraph "brew-dep" { rankdir=LR; node [shape=record];
"gdbm"->"python@3.8"; "gettext"->"git"; "gettext"->"libidn2"; "gettext"->"wget"; "libidn2"->"wget"; "libunistring"->"libidn2"; "libunistring"->"wget"; "ncurses"->"htop"; "oniguruma"->"jq"; "openssl@1.1"->"mosh"; "openssl@1.1"->"nmap"; "openssl@1.1"->"python@3.8"; "openssl@1.1"->"wget"; "pcre2"->"git"; "protobuf"->"mosh"; "readline"->"python@3.8"; "readline"->"sqlite"; "readline"->"tig"; "sqlite"->"python@3.8"; "xz"->"python@3.8"; "bash-completion"; "coreutils"; "dos2unix"; "gdbm"; "gettext"; "git-extras"; "icu4c"; "libunistring"; "mtr"; "ncurses"; "oniguruma"; "openssl@1.1"; "pcre2"; "pidof"; "protobuf"; "readline"; "tree"; "unrar"; "xz";
}
brew-dep
</details>