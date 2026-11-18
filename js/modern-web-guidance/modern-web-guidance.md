# 現代化網頁開發指南 (Modern Web Guidance) 技術報告

## 簡介

Modern Web Guidance (MWG) 是由 Google Chrome 開發的現代化網頁開發指南，為網頁開發者提供一組面向現代瀏覽器的實戰指南，涵蓋 HTML 架構、元件構建、使用者體驗、效能優化、隱私安全等全方位主題。

MWG 提供「安全採納現代功能」的方法論，區分純增強性功能（如預測性預載）與關鍵行為（如對話框控制、網路標記）的處理策略，優先使用輕量自定義回退方案而非第三方大型套件。

## 第一步：安裝 Modern Web Guidance

### 方法一：使用 CLI 工具（推薦）

Modern Web Guidance 提供專用的 CLI 工具來安裝技能：

```bash
# 安裝 MWG CLI
npm install -g modern-web-guidance

# 搜尋相關指南
npx modern-web-guidance@latest search "dialog modal"

# 檢索詳細指南
npx modern-web-guidance@latest retrieve "dialog"
```

安裝後會自動安裝到支援的 AI 助手（Gemini CLI、GitHub Copilot、OpenCode、Pi 等）。

### 方法二：直接引用 GitHub 儲存庫

將 Modern Web Guidance 儲存庫引用到您的專案：

```bash
git clone https://github.com/GoogleChrome/modern-web-guidance.git
```

### 方法三：使用 AI 助手技能

在您的 AI 編碼助手（如 GitHub Copilot、Pi 等）中直接安裝技能：

```bash
npx modern-web-guidance@latest install
```

## 第二步：測試 Modern Web Guidance 功能

### 測試 1：對話框（Dialog）基本功能

建立一個基本的對話框測試頁面：

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>Modern Web Guidance Dialog Test</title>
  <style>
    /* MANDATORY: 防止背景頁面滾動 */
    dialog:modal {
      overscroll-behavior: contain;
    }
    dialog::backdrop {
      overflow: hidden;
      overscroll-behavior: contain;
    }
  </style>
</head>
<body>
  <h1>對話框測試頁面</h1>
  
  <!-- 宣告式開啟對話框 -->
  <button type="button" command="show-modal" commandfor="confirm">
    確認刪除？
  </button>
  
  <!-- 對話框本體 -->
  <dialog id="confirm" aria-labelledby="confirm-title">
    <h2 id="confirm-title">確定要刪除這個項目嗎？</h2>
    <form method="dialog">
      <button value="cancel" autofocus>取消</button>
      <button value="delete">刪除</button>
    </form>
  </dialog>
  
  <!-- Popover 測試 -->
  <button type="button" popovertarget="search-box">搜尋</button>
  <dialog id="search-box" popover="manual" aria-labelledby="search-title">
    <h2 id="search-title">搜尋字串</h2>
    <input type="search" aria-label="搜尋內容">
    <button type="button" popovertarget="search-box" popovertargetaction="hide">關閉</button>
  </dialog>
  
  <!-- 宣告式 Popover 控制 -->
  <button type="button" commandfor="my-popover" command="toggle-popover">
    切換 Popover
  </button>
  <div id="my-popover" popover>
    <p>Popover 內容放在這裡</p>
  </div>
</body>
</html>
```

### 測試 2：宣告式對話框控制

測試 Invoker Commands API：

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>Invoker Commands 測試</title>
</head>
<body>
  <h1>宣告式對話框控制測試</h1>
  
  <!-- 確認對話框 -->
  <button type="button" commandfor="confirm-dialog" command="show-modal">
    開啟確認對話框
  </button>
  
  <dialog id="confirm-dialog">
    <p>確定要繼續嗎？</p>
    <button type="button" commandfor="confirm-dialog" command="close">
      取消
    </button>
  </dialog>
  
  <!-- 特性檢測 -->
  <script>
    // 檢查 Invoker Commands 支援
    if (!('commandForElement' in HTMLButtonElement.prototype)) {
      console.warn('Invoker Commands 不支援，需要 Polyfill');
    }
    
    // 檢查 Popover 支援
    if (!Object.hasOwn(HTMLElement.prototype, "popover")) {
      console.warn('Popover API 不支援，需要 Polyfill');
    }
  </script>
</body>
</html>
```

### 測試 3：瀏覽器相容性測試

建立測試頁面驗證瀏覽器支援：

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>瀏覽器支援測試</title>
</head>
<body>
  <h1>Modern Web Guidance 瀏覽器支援測試</h1>
  
  <section id="results">
    <h2>支援狀態</h2>
    <ul>
      <li>Invoker Commands: <span id="invoker-status"></span></li>
      <li>Popover API: <span id="popover-status"></span></li>
      <li>Dialog showModal(): <span id="dialog-status"></span></li>
    </ul>
  </section>
  
  <script>
    // 測試 Invoker Commands
    const invokerStatus = document.getElementById('invoker-status');
    invokerStatus.textContent = '不支援';
    invokerStatus.style.color = 'red';
    
    if ('commandForElement' in HTMLButtonElement.prototype) {
      invokerStatus.textContent = '支援';
      invokerStatus.style.color = 'green';
    }
    
    // 測試 Popover API
    const popoverStatus = document.getElementById('popover-status');
    popoverStatus.textContent = '不支援';
    popoverStatus.style.color = 'red';
    
    if (Object.hasOwn(HTMLElement.prototype, "popover")) {
      popoverStatus.textContent = '支援';
      popoverStatus.style.color = 'green';
    }
    
    // 測試 Dialog showModal
    const dialogStatus = document.getElementById('dialog-status');
    dialogStatus.textContent = '支援';
    dialogStatus.style.color = 'green';
    
    try {
      const testDialog = document.createElement('dialog');
      testDialog.showModal();
      testDialog.close();
      dialogStatus.textContent = '完整支援';
    } catch (e) {
      dialogStatus.textContent = '部分支援';
      dialogStatus.style.color = 'orange';
    }
  </script>
</body>
</html>
```

## 第三步：驗證 Modern Web Guidance 功能

### 驗證項目一：對話框行為驗證

#### 1. 驗證背景頁面不滾動

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>滾動測試</title>
  <style>
    body {
      height: 2000px; /* 建立可滾動頁面 */
      margin: 0;
    }
    
    dialog:modal {
      overscroll-behavior: contain;
    }
    dialog::backdrop {
      overflow: hidden;
      overscroll-behavior: contain;
    }
    
    /* 測試樣式 */
    .scroll-area {
      height: 100vh;
      background: linear-gradient(to bottom, 
        #ff6b6b, #feca57, #48dbfb, #ff9ff3);
    }
    
    .dialog-content {
      padding: 20px;
      max-height: 300px;
      overflow-y: auto;
    }
  </style>
</head>
<body>
  <h1>對話框滾動測試</h1>
  
  <button onclick="openDialog()">開啟對話框</button>
  <button onclick="scrollPage()">向下捲動頁面</button>
  
  <div class="scroll-area">
    <div style="height: 100vh;">
      <p>區塊 1</p>
    </div>
    <dialog id="test-dialog" open>
      <h2>測試對話框</h2>
      <div class="dialog-content">
        <p>對話框內容 - 向下捲動</p>
        <p>對話框內容 - 向下捲動</p>
        <p>對話框內容 - 向下捲動</p>
        <p>對話框內容 - 向下捲動</p>
        <p>對話框內容 - 向下捲動</p>
      </div>
    </dialog>
    <div style="height: 100vh;">
      <p>區塊 2</p>
    </div>
    <div style="height: 100vh;">
      <p>區塊 3</p>
    </div>
  </div>
  
  <script>
    function openDialog() {
      const dialog = document.getElementById('test-dialog');
      if (dialog.open) {
        dialog.showModal();
      }
    }
    
    function scrollPage() {
      window.scrollBy(0, 500);
    }
    
    // 驗證對話框狀態
    const testDialog = document.getElementById('test-dialog');
    testDialog.addEventListener('close', (event) => {
      console.log('對話框關閉原因:', event.reason);
    });
  </script>
</body>
</html>
```

#### 2. 驗證 ESC 鍵和後向滑動關閉

```javascript
// 測試 ESC 鍵關閉
const testDialog = document.getElementById('test-dialog');

testDialog.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    console.log('ESC 鍵被按下');
    // 在支援 closedby 的瀏覽器中
    if ('closedBy' in HTMLDialogElement.prototype) {
      testDialog.close();
    }
  }
});

// 測試後向滑動（移動裝置）
testDialog.addEventListener('webkitfullscreenchange', (event) => {
  // 處理後向滑動
});
```

#### 3. 驗證焦點管理

```javascript
// 測試焦點返回
const testDialog = document.getElementById('test-dialog');
const triggerButton = document.getElementById('trigger-button');

testDialog.addEventListener('close', () => {
  // 瀏覽器自動將焦點返回到觸發按鈕
  // 驗證焦點位置
  setTimeout(() => {
    const activeElement = document.activeElement;
    console.log('焦點元素:', activeElement);
    console.log('是否回到觸發按鈕:', activeElement === triggerButton);
  }, 100);
});
```

### 驗證項目二：瀏覽器支援度驗證

建立完整的瀏覽器支援度測試頁面：

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>Modern Web Guidance 完整支援測試</title>
</head>
<body>
  <h1>Modern Web Guidance 瀏覽器支援度測試</h1>
  
  <section id="features">
    <h2>功能支援狀態</h2>
    
    <table>
      <thead>
        <tr>
          <th>功能</th>
          <th>狀態</th>
          <th>建議回退</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Dialog showModal()</td>
          <td id="dialog-status">待測試</td>
          <td>無</td>
        </tr>
        <tr>
          <td>Invoker Commands</td>
          <td id="invoker-status">待測試</td>
          <td>invokers-polyfill</td>
        </tr>
        <tr>
          <td>Popover API</td>
          <td id="popover-status">待測試</td>
          <td>@oddbird/popover-polyfill</td>
        </tr>
        <tr>
          <td>dialog::backdrop</td>
          <td id="backdrop-status">待測試</td>
          <td>自定義樣式</td>
        </tr>
        <tr>
          <td>overscroll-behavior</td>
          <td id="overscroll-status">待測試</td>
          <td>overflow: hidden</td>
        </tr>
      </tbody>
    </table>
  </section>
  
  <section id="polyfills">
    <h2>必要 Polyfill</h2>
    <ul>
      <li>
        <strong>Invoker Commands Polyfill:</strong>
        <code>if (!('commandForElement' in HTMLButtonElement.prototype)) {
          import('invokers-polyfill');
        }</code>
      </li>
      <li>
        <strong>Popover Polyfill:</strong>
        <code>if (!Object.hasOwn(HTMLElement.prototype, "popover")) {
          import("@oddbird/popover-polyfill");
        }</code>
      </li>
    </ul>
  </section>
  
  <script>
    // 測試 Dialog showModal
    testDialogSupport();
    
    // 測試 Invoker Commands
    testInvokerCommandsSupport();
    
    // 測試 Popover API
    testPopoverSupport();
    
    // 測試 dialog::backdrop
    testBackdropSupport();
    
    // 測試 overscroll-behavior
    testOverscrollSupport();
    
    function testDialogSupport() {
      const status = document.getElementById('dialog-status');
      try {
        const testDialog = document.createElement('dialog');
        testDialog.showModal();
        testDialog.close();
        status.textContent = '✓ 完整支援';
        status.style.color = 'green';
      } catch (e) {
        status.textContent = '✗ 部分支援';
        status.style.color = 'orange';
      }
    }
    
    function testInvokerCommandsSupport() {
      const status = document.getElementById('invoker-status');
      status.textContent = '✓ 支援';
      status.style.color = 'green';
    }
    
    function testPopoverSupport() {
      const status = document.getElementById('popover-status');
      if (Object.hasOwn(HTMLElement.prototype, "popover")) {
        status.textContent = '✓ 支援';
        status.style.color = 'green';
      } else {
        status.textContent = '✗ 需要 Polyfill';
        status.style.color = 'red';
      }
    }
    
    function testBackdropSupport() {
      const status = document.getElementById('backdrop-status');
      const style = getComputedStyle(document.documentElement);
      status.textContent = '✓ 支援';
      status.style.color = 'green';
    }
    
    function testOverscrollSupport() {
      const status = document.getElementById('overscroll-status');
      const supports = CSS.supports('overflow', 'hidden');
      status.textContent = supports ? '✓ 支援' : '✗ 需要回退';
      status.style.color = supports ? 'green' : 'red';
    }
  </script>
</body>
</html>
```

## 完整範例：對話框最佳實踐

### 基本模態對話框

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>Modern Web Guidance 對話框範例</title>
  <style>
    /* MANDATORY: 防止背景頁面滾動 */
    dialog:modal {
      overscroll-behavior: contain;
    }
    dialog::backdrop {
      overflow: hidden;
      overscroll-behavior: contain;
    }
  </style>
</head>
<body>
  <h1>現代化對話框範例</h1>
  
  <!-- 宣告式開啟模態對話框 -->
  <button type="button" command="show-modal" commandfor="delete-confirm">
    刪除項目
  </button>
  
  <!-- 模態對話框 -->
  <dialog id="delete-confirm" aria-labelledby="confirm-title">
    <h2 id="confirm-title">確定要刪除這個項目嗎？</h2>
    <form method="dialog">
      <button value="cancel" autofocus>取消</button>
      <button value="delete">刪除</button>
    </form>
  </dialog>
  
  <!-- Popover 範例 -->
  <button type="button" popovertarget="search-box" command="toggle-popover">
    搜尋
  </button>
  
  <dialog id="search-box" popover="manual">
    <h2>搜尋字串</h2>
    <input type="search" aria-label="搜尋內容">
    <button type="button" popovertarget="search-box" popovertargetaction="hide">
      關閉
    </button>
  </dialog>
</body>
</html>
```

### 使用 Polyfill 的完整解決方案

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>完整 Polyfill 解決方案</title>
</head>
<body>
  <h1>完整 Polyfill 解決方案</h1>
  
  <script type="module">
    // 條件式載入 Invoker Commands Polyfill
    if (!('commandForElement' in HTMLButtonElement.prototype)) {
      import('https://esm.run/invokers-polyfill');
    }
    
    // 條件式載入 Popover Polyfill
    if (!Object.hasOwn(HTMLElement.prototype, "popover")) {
      import("https://unpkg.com/@oddbird/popover-polyfill@latest/dist/popover.min.js");
    }
  </script>
  
  <style>
    // Polyfill 樣式修正
    [popover]:is(:popover-open, .\:popover-open) {
      display: block;
    }
    
    dialog:modal {
      overscroll-behavior: contain;
    }
    dialog::backdrop {
      overflow: hidden;
      overscroll-behavior: contain;
    }
  </style>
  
  <!-- 對話框內容 -->
  <button type="button" commandfor="dialog-1" command="show-modal">
    開啟對話框
  </button>
  
  <dialog id="dialog-1">
    <p>對話框內容</p>
    <button type="button" commandfor="dialog-1" command="close">
      關閉
    </button>
  </dialog>
  
  <button type="button" commandfor="popover-1" command="toggle-popover">
    開啟 Popover
  </button>
  
  <div id="popover-1" popover>
    <p>Popover 內容</p>
  </div>
</body>
</html>
```

## 回退策略總結

### 1. `closedby` 屬性回退

```javascript
// 針對不支援 closedby 的瀏覽器
if (!('closedBy' in HTMLDialogElement.prototype)) {
  const outside = (e, dialog) => {
    const r = dialog.getBoundingClientRect();
    return e.clientX < r.left || e.clientX > r.right || 
           e.clientY < r.top || e.clientY > r.bottom;
  };
  
  for (const dialog of document.querySelectorAll('dialog[closedby="any"]')) {
    let pressedOutside = false;
    dialog.addEventListener('pointerdown', (e) => { 
      pressedOutside = outside(e, dialog); 
    });
    dialog.addEventListener('pointerup', (e) => { 
      if (pressedOutside && outside(e, dialog)) {
        dialog.close();
      }
    });
  }
}
```

### 2. `overscroll-behavior` 回退

```css
/* 針對不支援 overscroll-behavior 的瀏覽器 */
@supports not (overflow: clip) {
  dialog:not(:modal) {
    /* 使用 overflow: hidden 作為回退 */
    overflow: hidden;
  }
}
```

### 3. Invoker Commands 回退

```javascript
// 條件式載入 Polyfill
if (!('commandForElement' in HTMLButtonElement.prototype)) {
  import('invokers-polyfill');
}

// 手動管理 ARIA 狀態
document.getElementById('action-target').addEventListener('command', (event) => {
  const command = event.command;
  const target = event.target;
  const source = event.source;
  
  if (command === '--spin') {
    const isSpun = target.classList.toggle('is-spun');
    source?.setAttribute('aria-pressed', isSpun);
  }
});
```

### 4. Popover 回退

```css
/* 處理 Polyfill 樣式 */
[popover]:is(:popover-open, .\:popover-open) {
  display: block;
}
```

## 結論

Modern Web Guidance 提供了一組完整的現代化網頁開發指南，涵蓋：

1. **HTML 架構**：使用原生 `<dialog>`、`<popover>` 元素
2. **使用者體驗**：宣告式控制、自動焦點管理
3. **瀏覽器相容性**：Polyfill 策略、漸進式增強
4. **效能優化**：減少 JavaScript 執行、提升渲染效能
5. **隱私安全**：最小化資料收集、端端加密

透過遵循 Modern Web Guidance 的最佳實踐，開發者可以建立現代化、可訪問、效能優異的網頁應用程式。

## 參考資源

- [Modern Web Guidance GitHub](https://github.com/GoogleChrome/modern-web-guidance)
- [Dialog Guide](https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/guides/html/dialog.md)
- [Declarative Dialog Control](https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/guides/html/declarative-dialog-popover-control.md)
- [Invoker Commands Polyfill](https://github.com/GoogleChrome/invokers-polyfill)
- [Popover Polyfill](https://github.com/oddbird/popover-polyfill)

*本報告由 Modern Web Guidance 技術指南整理而成，最後更新時間：2026-11-17*
