<table>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
如何在 reveal.js 簡報中加入一頁「引言 Quote」？
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

在 **reveal.js** 中加入一頁「引言（Quote）」非常簡單，因為 reveal.js 本質上是 HTML，所以你可以利用標準的 HTML 標籤或是 Markdown 語法來達成。

以下提供三種最常用的方法，從最基礎的寫法到進階的美化樣式：

---

### 方法一：使用標準 HTML 標籤（最推薦）

這是最穩定的方法，利用 `<blockquote>` 標籤來語意化地標示引言。Reveal.js 的預設主題通常會自動對這個標籤進行美化（例如加上左邊框或改變字體樣式）。

**程式碼範例：**

```html
<section>
  <figure>
    <blockquote cite="https://www.example.com/source">
      &ldquo;設計不僅僅是外觀和感覺，設計是關於它是如何運作的。&rdquo;
    </blockquote>
    <figcaption>
      — Steve Jobs, <cite>The New York Times Magazine</cite>
    </figcaption>
  </figure>
</section>

```

**重點說明：**

* **`<blockquote>`**: 用來包覆引言內容。
* **`&ldquo;` 和 `&rdquo;**`: 這是左雙引號和右雙引號的 HTML 實體代碼，比直接打 `"` 更美觀且不易出錯。
* **`<figcaption>`**: 用來標示作者或出處。

---

### 方法二：使用 Markdown 語法

如果你在 reveal.js 中啟用了 Markdown plugin，你可以使用更簡潔的寫法。

**程式碼範例：**

```markdown
<section data-markdown>
  <textarea data-template>
  
  > "Stay hungry, stay foolish."
  >
  > -- Steve Jobs

  </textarea>
</section>

```

**注意：** 這需要你的專案中有正確設定 `RevealMarkdown` 插件。

---

### 方法三：進階美化技巧（讓引言更吸睛）

單純的文字有時不夠震撼，你可以透過以下三個技巧來增強視覺效果：

#### 1. 加入背景圖片

引言頁面通常適合搭配一張滿版的高畫質圖片。

```html
<section data-background-image="https://source.unsplash.com/random/1920x1080?technology">
  <div style="background-color: rgba(0, 0, 0, 0.6); padding: 20px; border-radius: 10px;">
    <h2 style="color: white;">"Code is Poetry."</h2>
    <p style="color: #ddd;">— WordPress</p>
  </div>
</section>

```

#### 2. 使用 `r-fit-text` 自動縮放

如果你希望引言文字能夠**盡可能的大**，填滿整個螢幕寬度，可以使用 reveal.js 內建的 `r-fit-text` class。

```html
<section>
  <h2 class="r-fit-text">SIMPLE IS BEST</h2>
  <p>— The Philosophy</p>
</section>

```

#### 3. 加入逐行出現動畫 (Fragments)

先顯示引言，講完後再顯示作者。

```html
<section>
  <blockquote>
    "I have not failed. I've just found 10,000 ways that won't work."
  </blockquote>
  <p class="fragment" style="text-align: right;">— Thomas Edison</p>
</section>

```

---

### 快速總結

| 需求 | 推薦方法 |
| --- | --- |
| **標準、快速** | 使用 `<section>` 包覆 `<blockquote>` |
| **懶人、筆記流** | 使用 Markdown 的 `>` 語法 |
| **視覺衝擊** | 使用 `data-background-image` 配合半透明遮罩 |

**您希望我為您提供一段自定義的 CSS 代碼，讓您的引言擁有特殊的字型或邊框樣式嗎？**

</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
提供一段自定義的 CSS 代碼，讓引言擁有特殊的字型或邊框樣式
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

沒問題！要讓引言在簡報中脫穎而出，CSS 是最強大的武器。Reveal.js 的預設樣式有時稍微單調，我們可以透過自定義 CSS 來增加**層次感**與**設計感**。

你可以將以下代碼直接放入 HTML 檔案的 `<style>` 標籤內，或是放入獨立的 `.css` 檔案中。

---

## 方案一：優雅現代感 (Modern Elegant)

這款設計使用了**左側粗邊框**、**微陰影**以及**柔和的背景色**，非常適合商務或正式報告。

```css
/* 自定義引言樣式 - 現代優雅 */
.reveal blockquote {
    background: rgba(255, 255, 255, 0.05); /* 微透明背景 */
    border-left: 10px solid #42affa;        /* 左側主題色粗邊框 */
    box-shadow: 0 10px 20px rgba(0,0,0,0.2); /* 增加立體感 */
    padding: 30px 40px;
    width: 80%;
    font-style: italic;                      /* 斜體 */
    font-family: "Noto Serif TC", serif;     /* 建議搭配襯線體 */
    line-height: 1.6;
    text-align: left;                        /* 左對齊更有質感 */
    margin: 20px auto;
}

/* 引言出處的樣式 */
.reveal .quote-author {
    display: block;
    text-align: right;
    margin-top: 20px;
    font-size: 0.8em;
    color: #aaa;
}

```

---

## 方案二：大氣語錄感 (The Giant Quote)

這款設計利用 **CSS 偽元素 (`::before`)** 在左上角加上一個超大的「引號」，非常有視覺衝擊力，適合用來強調某個核心觀點。

```css
/* 自定義引言樣式 - 巨型引號 */
.reveal .big-quote {
    position: relative;
    border: none;           /* 去掉預設邊框 */
    background: none;       /* 去掉背景 */
    box-shadow: none;       /* 去掉陰影 */
    font-size: 1.5em;
    padding: 60px;
    text-align: center;
}

.reveal .big-quote::before {
    content: "\201C";       /* 左雙引號的 Unicode */
    position: absolute;
    top: -20px;
    left: 0;
    font-size: 4em;
    color: #42affa;         /* 引號顏色 */
    opacity: 0.3;           /* 半透明 */
    font-family: Georgia, serif;
}

.reveal .big-quote::after {
    content: "\201D";       /* 右雙引號的 Unicode */
    position: absolute;
    bottom: -40px;
    right: 0;
    font-size: 4em;
    color: #42affa;
    opacity: 0.3;
    font-family: Georgia, serif;
}

```

---

### 如何在 HTML 中使用這些樣式？

你可以根據選擇的方案，調整你的 HTML 結構：

**對應方案一的 HTML：**

```html
<section>
  <blockquote cite="Steve Jobs">
    “最重要的事，是擁有追隨你的心與直覺的勇氣。”
    <span class="quote-author">— 史蒂夫·賈伯斯</span>
  </blockquote>
</section>

```

**對應方案二的 HTML：**

```html
<section>
  <blockquote class="big-quote">
    生命中最美好的事物不是物品，而是時刻。
  </blockquote>
</section>

```

---

### 💡 小撇步：加入 Google Fonts 字體

好的引言需要好的字體。如果你希望呈現人文氣息，可以在 `<head>` 加入這行，並在 CSS 中引用：

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@700&display=swap" rel="stylesheet">

```

> **注意：** 如果你的 reveal.js 背景是暗色的，請確保邊框色（如 `#42affa`）有足夠的對比度，這樣觀眾才看得到喔！

---

**您希望我幫您整合一段完整的 HTML 模板，包含這些 CSS 與字體設定，讓您直接複製就能運行嗎？**
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
整合一段完整的 HTML 模板，包含這些 CSS 與字體設定
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

沒問題！這是一個完整的 **reveal.js** 單檔案模板。我幫你把剛剛討論的「現代優雅」與「巨型引號」兩種風格都整合進去了，並且加入了 Google Fonts 的思源宋體，讓文字看起來更有深度。

你可以直接將這段代碼存成 `.html` 檔案（例如 `index.html`），用瀏覽器打開就能看到效果。

```html
<!doctype html>
<html lang="zh-Hant">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>Reveal.js 引言模板</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/black.min.css">

    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">

    <style>
        /* 1. 通用字體設定 */
        :root {
            --accent-color: #42affa; /* 主題色：水藍色 */
        }
        
        .reveal h1, .reveal h2, .reveal h3 {
            font-family: 'Noto Serif TC', serif;
        }

        /* 2. 方案一：現代優雅 (Modern Elegant) */
        .reveal .quote-modern {
            background: rgba(255, 255, 255, 0.05);
            border-left: 10px solid var(--accent-color);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 40px 50px;
            width: 85%;
            font-style: italic;
            font-family: 'Noto Serif TC', serif;
            line-height: 1.6;
            text-align: left;
            margin: 0 auto;
        }

        .reveal .quote-author {
            display: block;
            text-align: right;
            margin-top: 25px;
            font-size: 0.8em;
            color: #aaa;
            font-style: normal;
        }

        /* 3. 方案二：大氣語錄感 (The Giant Quote) */
        .reveal .big-quote {
            position: relative;
            border: none;
            background: none;
            box-shadow: none;
            font-size: 1.4em;
            padding: 60px;
            text-align: center;
            font-family: 'Noto Serif TC', serif;
            font-weight: 700;
            width: 80%;
            margin: 0 auto;
        }

        .reveal .big-quote::before {
            content: "\201C"; /* 左雙引號 */
            position: absolute;
            top: -40px;
            left: -20px;
            font-size: 5em;
            color: var(--accent-color);
            opacity: 0.3;
            font-family: Georgia, serif;
        }

        .reveal .big-quote::after {
            content: "\201D"; /* 右雙引號 */
            position: absolute;
            bottom: -60px;
            right: -20px;
            font-size: 5em;
            color: var(--accent-color);
            opacity: 0.3;
            font-family: Georgia, serif;
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">

            <section>
                <h1>Reveal.js</h1>
                <p>引言樣式展示</p>
            </section>

            <section>
                <h3>風格一：現代優雅</h3>
                <blockquote class="quote-modern">
                    “設計不僅僅是外觀和感覺，設計是關於它是如何運作的。”
                    <span class="quote-author">— 史蒂夫·賈伯斯 (Steve Jobs)</span>
                </blockquote>
            </section>

            <section>
                <h3>風格二：大氣語錄</h3>
                <blockquote class="big-quote">
                    生命中最美好的事物不是物品，而是那些令人屏息的時刻。
                </blockquote>
            </section>

            <section>
                <h3>結合動畫效果</h3>
                <blockquote class="quote-modern">
                    “我沒有失敗。我只是發現了一萬種行不通的方法。”
                    <span class="quote-author fragment">— 湯瑪斯·愛迪生 (Thomas Edison)</span>
                </blockquote>
                <p class="fragment" style="margin-top: 20px; color: var(--accent-color);">↑ 點擊下一頁才顯示作者</p>
            </section>

            <section data-background-image="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop">
                <div style="background: rgba(0,0,0,0.6); padding: 40px; border-radius: 15px;">
                    <h2 style="color: white;">“Code is Poetry.”</h2>
                    <p>— WordPress 核心理念</p>
                </div>
            </section>

        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.js"></script>
    <script>
        // 初始化 Reveal.js
        Reveal.initialize({
            hash: true,
            center: true, // 垂直居中
            transition: 'slide' // 切換動畫
        });
    </script>
</body>
</html>

```

---

### 如何調整與優化？

* **更改主題色**：在 CSS 的 `:root` 裡修改 `--accent-color`，就可以一次更換所有引號與邊框的顏色。
* **字體粗細**：引言如果想要更有力道，可以在 `blockquote` 加上 `font-weight: 700;`。
* **出處位置**：如果你想要作者名字靠左或居中，修改 `.quote-author` 裡的 `text-align` 即可。

**想試試看為這些引言加上一些進階的過場動畫（例如文字逐個淡入）嗎？**
</td></tr>
</table>