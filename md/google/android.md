# Android

## 2026-06-07

## Android skills 

- https://github.com/android/skills

> Android skills are a dedicated repository of AI-optimized, modular instructions and resources, to help LLMs better understand and execute specific patterns that follow the best practices and guidance on Android development from developer.android.com.

## Android CLI

- https://developer.android.com/tools/agents/android-cli

> Android CLI is a command-line interface that enables you to more easily and efficiently build for Android using any tool of your choice.

## Android Studio

- https://developer.android.com/studio/gemini/skills

> Extend Agent Mode with skills
> Skills let you enhance Agent Mode's capabilities with specialized expertise and custom workflows. They are based on the Agent Skills open standard.

## 2026-11-27

> [!NOTE]
> Q: Android 可以排程幾點幾分自動開啟無線網路然後連上特定網站嗎？有其他類似 MacroDroid 的 Android App 嗎？

### Android 自動開啟無線網路功能

#### 原生設定選項

Android 系統提供部分原生自動化功能，但可用性依手機品牌和系統版本而異：

| 手機品牌 | 功能名稱 | 設定路徑 |
|---------|---------|---------|
| Pixel / 部分 Motorola / Nokia | **活躍 WiFi (Active WiFi)** | 設定 > 網路與網際網路 > WiFi > WiFi 偏好設定 |
| Samsung | **智慧 WiFi (Smart WiFi)** | 設定 > 連線 > WiFi > 智慧 WiFi |
| Xiaomi / Huawei | **自動開啟 WiFi** | 設定 > 網路和網際網路 > 網路偏好設定 |

這些功能通常可設定：
- 當手機偵測到特定區域時自動開啟 WiFi
- 自動連接到已儲存的網路

**限制**：原生功能通常無法設定「指定時間點」自動開啟，只能基於位置觸發。

#### 第三方 App 推薦

可設定時間排程開啟 WiFi 並連接特定網站的 App：

| App 名稱 | 功能 | 評分 | 下載量 |
|---------|------|------|--------|
| **WIFI ON/OFF Pro** | 時間排程開啟/關閉 WiFi | - | - |
| **WiFi Router Admin Setup** | WiFi 時間排程器，可自動開啟/關閉 | 1.9★ | 5K+ |
| **WiFi Auto Connect** | 依使用情況自動控制 WiFi | 4.2★ | 147 |
| **Wifi Shortcuts+** | 可排程任務、切換網路 | - | 10K+ |
| **NexFlow** | 開源自動化 App，時間觸發 | - | 1M+ |

> [!NOTE]
> 類似 MacroDroid 的 Android 自動化 App

#### 主流選擇（2026）

| App | 特色 | 價格 | 適合對象 |
|-----|------|------|---------|
| **Tasker** | 功能最強，支援變數、腳本、插件 | $2.99 | 進階玩家，願意看文檔 |
| **MacroDroid** | 介面友善，上手快，日常自動化 | 免費 + 內購 | 一般用戶，不想看文檔 |
| **Automate** | 視覺化流程圖，可 AI 生成流程 | 免費 + 內購 | 喜歡流程圖思維 |
| **NexFlow** | 開源、Material 3 介面、繁體中文 | 免費 | 開源支持者 |
| **Rulomi** | 從文字描述生成自動化流程 | 免費 | 不想看文檔的新手 |
| **Samsung Modes & Routines** | 三星手機內建 | 免費 | Galaxy 用戶 |

#### App 對比

| 功能 | MacroDroid | Tasker | Automate |
|------|-----------|--------|---------|
| 免費功能 | 基礎 | 極少 | 中等 |
| 上手難度 | 低 | 高 | 中 |
| 視覺化 | 直觀 | 命令式 | 流程圖 |
| 支援 WiFi 控制 | ✅ | ✅ | ✅ |
| 開源 | ❌ | ❌ | ❌ |
| 繁體中文 | ✅ | ✅ | ✅ |

### 設定時間自動開啟 WiFi 的方法

#### 方法一：使用 Tasker/MacroDroid（推薦）
1. 安裝 App
2. 新增觸發條件：**時間 (Time)** → 設定具體時間（如 8:00）
3. 新增動作：**WiFi 開關** → 設定為「開啟」
4. （可選）新增動作：**自動連接網路** → 選擇目標網路

#### 方法二：使用專用的 WiFi 排程 App
- 安裝 **WIFI ON/OFF Pro** 或 **WiFi Router Admin Setup**
- 設定排程時間
- 選擇要連接的網路

#### 方法三：原生設定（有限）
- 三星：設定 > 連線 > WiFi > 智慧 WiFi → 自訂規則
- 部分品牌：可設定「在特定區域」自動開啟，但無法設定時間點

### 注意事項

⚠️ **權限與相容性**
- 部分自動化 App 需要「個人安全」權限
- 中國品牌（華為、小米）可能需 Root 權限才能控制 WiFi
- Android 10+ 的某些功能可能需要 Automate Legacy 擴展

⚠️ **電池消耗**
- 頻繁的自動化觸發可能增加電池消耗
- 建議避免不必要的排程

⚠️ **網站自動連接限制**
- Android 系統不支援「開啟 WiFi 後自動訪問特定網站」
- 只能控制「開啟 WiFi」和「連接到網路」，無法自動開啟瀏覽器或訪問特定網址
