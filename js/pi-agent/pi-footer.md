# Pi Coding Agent TUI 狀態列說明

Pi Coding Agent 的 TUI footer 可能顯示如下：

```text
↑48 ↓17k R485k W61k $0.045 (sub) 5.8%/1.1M (auto)                                                        (github-copilot) gpt-5.6-luna • medium
```

## Token 與費用統計

| 顯示 | 意義 | 範例值 |
|---|---|---:|
| `↑48` | 累計輸入 token | 48 |
| `↓17k` | 累計輸出 token | 約 17,000 |
| `R485k` | 累計從 prompt cache 讀取的 token | 約 485,000 |
| `W61k` | 累計寫入 prompt cache 的 token | 約 61,000 |
| `$0.045` | 依模型定價估算的累計費用 | 約 US$0.045 |
| `(sub)` | 目前透過訂閱制登入，而非直接 API key 計費 | 例如 GitHub Copilot 訂閱 |
| `5.8%/1.1M` | 目前上下文使用量／模型上下文上限 | 約 5.8%／1,100,000 token |
| `(auto)` | 已啟用自動 context compaction | 接近上限時自動壓縮較舊內容 |

## `↑`、`↓`、`R`、`W`

這些數字是目前 session 的累計值，不是上一輪請求的單次用量：

- `↑`：一般輸入 token。
- `↓`：模型輸出的 token。
- `R`：從 provider 的 prompt cache 命中的 token。
- `W`：寫入 prompt cache 的 token。

一次請求的 prompt 可能同時包含：

```text
一般輸入 token + cache read token + cache write token
```

Pi 會把這些類型分開顯示。工具呼叫、工具結果、摘要生成與 compaction 的用量也可能被計入 session 總量。

`k` 和 `M` 是數量縮寫：

- `17k` 約等於 17,000
- `485k` 約等於 485,000
- `1.1M` 約等於 1,100,000

## `$0.045 (sub)`

`$0.045` 是 Pi 根據目前模型定價與已回報的 token usage 算出的估算金額。

`(sub)` 表示目前 provider 使用的是訂閱制登入，例如 GitHub Copilot subscription。因此這個數字不一定代表會另外收取 US$0.045；它比較像是按照模型 API 定價換算出的資源使用估值。

實際帳務仍以 GitHub Copilot 或對應 provider 的訂閱方案為準。

## `5.8%/1.1M (auto)`

這是目前對話上下文的使用量：

```text
目前使用量 / 模型 context window
5.8% / 1.1M tokens
```

依此例估算，目前上下文約使用：

```text
1,100,000 × 5.8% ≈ 63,800 tokens
```

這個數字和前面的累計 token 不同：

- `↑`、`↓`、`R`、`W` 是整個 session 的累計 usage。
- `5.8%/1.1M` 是目前這一刻的上下文占用量。

`(auto)` 表示 Pi 已開啟自動壓縮。當對話接近 context window 上限時，Pi 會執行 compaction，將較早的對話整理成摘要，以便繼續使用同一個 session。

## Provider、模型與 thinking level

```text
(github-copilot) gpt-5.6-luna • medium
```

| 顯示 | 意義 |
|---|---|
| `(github-copilot)` | 目前使用的 provider |
| `gpt-5.6-luna` | 目前選用的模型 ID |
| `medium` | thinking／reasoning level |

`medium` 表示目前模型使用中等程度的推理設定。可以透過以下方式切換：

```text
/thinking
```

或使用：

```text
Shift+Tab
```

## 整體解讀

這一行代表：

> 目前 session 累計用了約 48 個一般輸入 token、17k 個輸出 token、485k 個 cache read token 與 61k 個 cache write token；依 API 價格估算約為 US$0.045，但目前是 GitHub Copilot 訂閱登入。當前上下文使用量為 1.1M 上限的 5.8%，並且啟用了自動壓縮。使用的模型是 `gpt-5.6-luna`，thinking level 為 `medium`。

## 參考資料

- Pi Coding Agent `README.md` 的 [Interactive Mode](https://github.com/earendil-works/pi/blob/main/README.md#interactive-mode)
- Pi Coding Agent `docs/compaction.md`
- `dist/modes/interactive/components/footer.js`
- Pi Coding Agent `FooterComponent` 實作
