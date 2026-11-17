# Google API Python Client

- Git Repo
  - https://github.com/googleapis/google-api-python-client/
- PyPI
  - https://pypi.org/project/google-api-python-client/
- Document
  - https://developers.google.com/youtube/data/libraries#python

## 2026-11-06

> [!NOTE]
> 可以在哪裡找到新的 https://www.youtube.com/feed/trending ?
> 有 API 可以取得熱門 YouTube 影片的 JSON 物件嗎

**有的，你可以使用官方的 YouTube Data API v3 格式來取得熱門影片的 JSON 物件。**

### 使用 API 的方法

1.  **申請 API 金鑰 (API Key)**
        -   前往 [Google Cloud Console](https://console.cloud.google.com/)。
        -   建立一個新專案。
        -   在「API 和服務」中搜尋並啟用 **YouTube Data API v3**。
        -   建立憑證並複製你的 **API Key**。
2.  **呼叫 API 端點**
    你要使用的端點是 `videos`，並將 `chart` 參數設定為 `mostPopular`。
    
    **請求網址範例：**

    ```text
    https://googleapis.com
    ```

### 關鍵參數說明

-   **`chart=mostPopular`**：**這是取得熱門影片的核心參數。**
-   `part=snippet,statistics`：指定回傳的資料範圍（`snippet` 包含標題、敘述、縮圖；`statistics` 包含觀看次數、按讚數）。
-   `regionCode=TW`：指定地區（例如 `TW` 代表台灣，`US` 代表美國）。如果不指定，會依據預設地區回傳。
-   `videoCategoryId`：（選填）如果你只想看特定分類（如音樂、遊戲）的熱門影片，可以加上分類 ID。
-   `maxResults=10`：設定回傳數量（最多可設為 50）。

回傳的 JSON 物件結構範例

```json
{
  "kind": "youtube#videoListResponse",
  "etag": "...",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "...",
      "id": "影片ID",
      "snippet": {
        "publishedAt": "2026-11-05T12:00:00Z",
        "channelId": "...",
        "title": "熱門影片的標題",
        "description": "影片敘述...",
        "thumbnails": {
          "default": { "url": "https://...", "width": 120, "height": 90 }
        },
        "channelTitle": "頻道名稱",
        "categoryId": "24"
      },
      "statistics": {
        "viewCount": "1500000",
        "likeCount": "85000",
        "favoriteCount": "0",
        "commentCount": "4200"
      }
    }
  ],
  "nextPageToken": "CAoQAA"
}
```

請問你打算用哪種**程式語言**（例如 **Python, JavaScript/Node.js**）來串接這個 API 呢？我可以為你提供現成的範例程式碼。

> [!NOTE]
> 使用 Python. 可以給我一個範例,查詢過去一週關於 AI 的熱門 YouTube 影片前二十名,並存成 Top20.json

> **請注意：** 由於 YouTube 官方 API 的 `chart="mostPopular"` 參數**不支援**直接傳入關鍵字（如 "AI"）進行過濾，因此要尋找「特定關鍵字的熱門影片」，實務上必須先使用 `search` 端點搜尋過去一週的影片，再將結果依據觀看次數排序。

以下是完整的 Python 範例程式碼，使用官方`google-api-python-client` 庫來達成你的需求：

### 準備工作

請先在終端機安裝 Google API 官方客戶端庫：

```bash
pip install google-api-python-client
```

### Python 範例程式碼


```python
from datetime import datetime, timedelta, timezone
import json
from googleapiclient.discovery import build

# 1. 設定你的 API 金鑰與搜尋參數
API_KEY = "YOUR_YOUTUBE_API_KEY"  # 請替換成你的真實 API Key
QUERY = "AI"
MAX_RESULTS = 20

# 2. 計算過去一週的時間（符合 RFC 3339 格式）
one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
published_after = one_week_ago.isoformat()

# 3. 初始化 YouTube API 用戶端
youtube = build("youtube", "v3", developerKey=API_KEY)

print(f"正在搜尋 {published_after} 之後關於 '{QUERY}' 的影片...")

# 4. 步驟一：使用 search().list() 搜尋過去一週相關的影片
# 這裡按 viewCount 排序，以獲取高曝光的影片候選名單
search_response = (
    youtube.search()
    .list(
        q=QUERY,
        part="id,snippet",
        type="video",
        publishedAfter=published_after,
        order="viewCount",  # 依觀看次數排序
        maxResults=MAX_RESULTS,
    )
    .execute()
)

# 提取所有影片的 ID 列表
video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

# 5. 步驟二：使用 videos().list() 獲取這些影片的詳細統計數據（如真實觀看數、點讚數）
video_response = (
    youtube.videos()
    .list(part="snippet,statistics", id=",".join(video_ids))
    .execute()
)

# 6. 步驟三：整理資料並再次排序（確保真實流量由高到低）
video_list = []
for item in video_response.get("items", []):
    stats = item.get("statistics", {})
    snippet = item.get("snippet", {})

    video_data = {
        "video_id": item["id"],
        "title": snippet.get("title"),
        "channel_title": snippet.get("channelTitle"),
        "published_at": snippet.get("publishedAt"),
        "view_count": int(stats.get("viewCount", 0)),
        "like_count": int(stats.get("likeCount", 0)),
        "video_url": f"https://youtube.com{item['id']}",
    }
    video_list.append(video_data)

# 依據觀看次數（view_count）重新由大到小排序
video_list = sorted(video_list, key=lambda x: x["view_count"], reverse=True)

# 7. 儲存為 Top20.json
output_filename = "Top20.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(video_list, f, ensure_ascii=False, indent=2)

print(f"已成功將前 {len(video_list)} 名熱門影片存入 {output_filename}！")
```

程式碼關鍵邏輯說明

1.  **`publishedAfter`**：利用 Python 的 `datetime` 計算出 7 天前的時間，並轉為 ISO 8601 格式，用來精準過濾出過去一週上傳的影片。
2.  **兩階段查詢**：因為 `search` 端點回傳的 `statistics`（觀看數）並不完整，所以標準做法是先透過 `search` 拿到 20 個熱門影片 ID，再用 `videos` 端點批次打包查出最準確的觀看次數與點讚數。
3.  **`ensure_ascii=False`**：在儲存 JSON 時加上這個參數，能確保影片標題中的中文、日文等非英文系文字能以正常文字儲存，而不會變成 `\u4e2d\u6587` 這種編碼。

如果執行程式時遇到 **API 配額限制（Quota Exceeded）** 或任何報錯，請告訴我，我可以幫你優化 **欄位篩選（fields 參數）** 來節省配額！

## 2026-11-17

- Tool: Pi Agent + unsloth/Qwen3.5-9B

```
Date:       11/17/2026, 12:47:17 PM
Models:     llama.cpp/unsloth/Qwen3.5-9B
Messages:   1 user, 27 assistant, 24 tool results, 1 compactions
Tool Calls: 24
Tokens:     ↑52k ↓9.5k R335k
Cost:       0.000
```

> [!NOTE]
> 根據 "https://github.com/googleapis/google-api-python-client/ https://developers.google.com/youtube/data/libraries#python" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "py/google-api-python-client/google-api-python-client.md" .

## Google API Python Client 技術報告

### 概觀

Google API Python Client 是 Google 為其基於 discovery 的 API 所提供的官方 Python 用戶端程式庫。此程式庫讓開發者能夠透過 Python 輕鬆地與 Google 各項服務進行互動。

> **重要說明**：此程式庫目前處於維護模式，僅修復關鍵 bug 和安全性問題，不會新增功能。對於新開發專案，Google 官方建議使用 [Cloud Client Libraries for Python](https://github.com/googleapis/google-cloud-python)。

### 目錄

1. [安裝步驟](#1-安裝步驟)
2. [環境驗證](#2-環境驗證)
3. [OAuth 2.0 認證設定](#3-oauth-20-認證設定)
4. [API 初始化](#4-api-初始化)
5. [YouTube Data API 範例](#5-youtube-data-api-範例)
6. [測試與驗證](#6-測試與驗證)
7. [注意事項](#7-注意事項)

### 1. 安裝步驟

#### 1.1 必要條件

- Python 3.10 或更高版本
- `pip` 套件管理工具
- Google Cloud 專案

#### 1.2 使用虛擬環境安裝（推薦）

虛擬環境可隔離依賴套件版本，避免與系統套件衝突。

##### Mac/Linux

```bash
## 安裝 virtualenv（若尚未安裝）
pip3 install virtualenv

## 建立虛擬環境
virtualenv <your-env>

## 啟用虛擬環境
source <your-env>/bin/activate

## 安裝 google-api-python-client
<your-env>/bin/pip install google-api-python-client
```

##### Windows

```batch
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-api-python-client
```

#### 1.3 直接安裝

```bash
pip install google-api-python-client
```

#### 1.4 安裝相依套件

安裝 `google-api-python-client` 時會自動安裝以下相依套件：

- `httplib2` - HTTP 客戶端實現
- `uritemplate` - URI 模板處理

若需開發功能，建議額外安裝：

```bash
pip install google-auth google-auth-httplib2 google-auth-oauthlib
```

### 2. 環境驗證

#### 2.1 檢查 Python 版本

```bash
python --version
## 或
python3 --version
```

輸出應為 Python 3.10 或更高版本。

#### 2.2 檢查已安裝套件

```bash
pip show google-api-python-client
```

確認套件已成功安裝，並顯示版本資訊。

#### 2.3 測試基本功能

建立測試檔案 `test_basic.py`：

```python
from googleapiclient.discovery import build

## 測試 API 初始化（需 API 金鑰）
try:
    youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
    print("✓ API 初始化成功")
except Exception as e:
    print(f"✗ API 初始化失敗：{e}")
```

執行測試：

```bash
python test_basic.py
```

### 3. OAuth 2.0 認證設定

OAuth 2.0 是存取使用者資料的標準認證機制。以下說明如何設定 OAuth 2.0 用戶端。

#### 3.1 建立 Google Cloud 專案

1. 開啟 [Google Cloud Console](https://console.cloud.google.com/)
2. 建立或選擇專案
3. 啟用所需的 API（例如 YouTube Data API v3）

#### 3.2 建立 OAuth 2.0 用戶端憑證

1. 在 Google Cloud Console 中，前往 **Credentials**（憑證）頁面
2. 點選 **Create Credentials**（建立憑證）> **OAuth 2.0 Client ID**
3. 設定應用程式類型：
   - **Desktop app**（電腦版應用程式）- 推薦用於桌面應用程式
   - 或使用 **Installed application**
4. 設定授權同意畫面（OAuth Consent Screen）：
   - App name：應用程式名稱
   - User support email：使用者支援電子郵件
   - Audience：選擇 **Internal**（內部使用）
5. 下載憑證檔案（`client_secret.json`）
6. 將憑證檔案保存在安全位置

#### 3.3 設定 Redirect URI

在建立 OAuth 2.0 用戶端時，Google 會提供兩種 redirect URI 選項：

| Redirect URI | 說明 | 使用時機 |
|-------------|------|---------|
| `http://localhost` | 回轉到本地伺服器的查詢參數 | 本地開發，需要本地伺服器處理回轉 |
| `urn:ietf:wg:oauth:2.0:oob` | 回轉到瀏覽器標題列 | 無本地伺服器時，使用者複製貼上授權碼 |
| `urn:ietf:wg:oauth:2.0:oob:auto` | 類似 oob，但不顯示複製提示 | 自動讀取瀏覽器標題列的應用程式 |

#### 3.4 設定 Python 程式碼

建立 `credentials.py` 檔案：

```python
"""
Google API OAuth 2.0 認證設定
"""

import os
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow

## 設定憑證檔案名稱
CLIENT_SECRETS_FILE = "client_secret.json"

## 設定授權範圍（Scopes）
## 根據所需 API 權限選擇合適的範圍
SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',  # 僅讀取 YouTube 資料
    'https://www.googleapis.com/auth/youtube',           # 完整存取權限
]

## API 服務名稱和版本
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    """
    建立認證的服務物件
    
    Returns:
        認證的 YouTube API 服務物件
    """
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES
        )
        
        # 使用 run_console 模式（瀏覽器開啟，使用者複製貼上授權碼）
        credentials = flow.run_console()
        
        return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
        
    except Exception as e:
        print(f"認證失敗：{e}")
        raise


def get_credentials():
    """
    僅建立認證物件（不初始化 API）
    
    Returns:
        OAuth 2.0 認證物件
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES
    )
    return flow.run_console()


## 環境變數：禁用 HTTPS 驗證（僅用於本地開發）
if os.environ.get('OAUTHLIB_INSECURE_TRANSPORT') != '1':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
```

### 4. API 初始化

#### 4.1 使用 API 金鑰（無需認證）

適用於存取公開資料，不需使用者授權。

```python
from googleapiclient.discovery import build

## 建立 YouTube API 服務物件
youtube = build(
    'youtube',
    'v3',
    developerKey='YOUR_API_KEY_HERE'
)

## 查詢公開頻道資訊
response = youtube.channels().list(
    part='contentDetails',
    forUsername='GoogleDevelopers'
).execute()

print(f"找到 {len(response['items'])} 個頻道")
```

#### 4.2 使用 OAuth 2.0 認證

適用於存取使用者私人的資料。

```python
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

## 建立服務帳號認證
SCOPES = ['https://www.googleapis.com/auth/youtube']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'path/to/service-account.json',
    scopes=SCOPES
)

## 建立認證的服務物件
youtube = build('youtube', 'v3', credentials=credentials)

## 查詢使用者自己的頻道
response = youtube.channels().list(
    part='snippet',
    mine=True
).execute()

for channel in response['items']:
    print(f"使用者頻道名稱：{channel['snippet']['title']}")
```

#### 4.3 使用 OAuth 2.0 本地安裝程式認證

```python
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

## 建立認證物件
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.readonly']
)
credentials = flow.run_console()

## 建立認證的服務物件
youtube = build('youtube', 'v3', credentials=credentials)

## 查詢使用者自己的頻道
response = youtube.channels().list(
    part='snippet',
    mine=True
).execute()

print(f"使用者頻道：{response['items'][0]['snippet']['title']}")
```

### 5. YouTube Data API 範例

#### 5.1 範例一：查詢公開頻道（使用 API 金鑰）

```python
"""
範例一：使用 API 金鑰查詢公開 YouTube 頻道資訊
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

def get_channel_info_by_id(api_key, channel_id):
    """
    根據頻道 ID 查詢頻道資訊
    
    Args:
        api_key: Google API 金鑰
        channel_id: YouTube 頻道 ID
    
    Returns:
        頻道資訊字典
    """
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        request = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        )
        response = request.execute()
        
        return response['items'][0]
        
    except HttpError as e:
        print(f"API 錯誤：{e}")
        return None
    except Exception as e:
        print(f"發生錯誤：{e}")
        return None


def main():
    # 設定 API 金鑰（請替換為您的金鑰）
    API_KEY = 'YOUR_API_KEY_HERE'
    
    # GoogleDevelopers 頻道 ID
    CHANNEL_ID = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'
    
    # 查詢頻道資訊
    channel = get_channel_info_by_id(API_KEY, CHANNEL_ID)
    
    if channel:
        print("=" * 60)
        print("YouTube 頻道資訊")
        print("=" * 60)
        
        # 顯示基本資訊
        print(f"\n【基本資訊】")
        print(f"  頻道名稱：{channel['snippet']['title']}")
        print(f"  頻道描述：{channel['snippet']['description'][:100]}...")
        print(f"  頻道網址：https://www.youtube.com/{channel['snippet']['customUrl']}")
        
        # 顯示統計數據
        print(f"\n【統計數據】")
        print(f"  訂閱人數：{channel['statistics']['subscriberCount']:,}")
        print(f"  總瀏覽數：{channel['statistics']['viewCount']:,}")
        print(f"  影片數：{channel['statistics']['videoCount']:,}")
        
        # 顯示內容詳情
        print(f"\n【內容詳情】")
        print(f"  最大影片長度：{channel['contentDetails']['maxUploadLengthShort']:,} 小時")
        print(f"  最大影片長度：{channel['contentDetails']['maxUploadLengthLong']:,} 小時")
        
        print("=" * 60)


if __name__ == '__main__':
    main()
```

#### 5.2 範例二：查詢使用者自己的頻道（使用 OAuth 認證）

```python
"""
範例二：使用 OAuth 2.0 認證查詢使用者自己的 YouTube 頻道
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pprint

## 設定憑證檔案
CLIENT_SECRETS_FILE = "client_secret.json"

## 授權範圍
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

## API 設定
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    """建立認證的服務物件"""
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES
        )
        credentials = flow.run_console()
        return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
        
    except Exception as e:
        print(f"認證失敗：{e}")
        raise


def list_my_channels(youtube):
    """列出使用者自己的頻道"""
    try:
        response = youtube.channels().list(
            part='snippet',
            mine=True
        ).execute()
        
        if response.get('items'):
            print(f"\n找到 {len(response['items'])} 個使用者頻道：\n")
            print("=" * 60)
            
            for channel in response['items']:
                snippet = channel['snippet']
                print(f"【{snippet['title']}"]
                print(f"  頻道 ID: {snippet['channelId']}")
                print(f"  網址：https://www.youtube.com/{snippet['customUrl']}")
                print(f"  描述：{snippet['description'][:100]}...")
                print("-" * 60)
        else:
            print("未找到使用者頻道。")
            
    except HttpError as e:
        print(f"API 錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")


def list_my_videos(youtube):
    """列出使用者上傳的影片"""
    try:
        response = youtube.videos().list(
            part='snippet',
            mine=True,
            maxResults=10
        ).execute()
        
        if response.get('items'):
            print(f"\n使用者最近上傳的 {len(response['items'])} 個影片：\n")
            print("=" * 60)
            
            for video in response['items']:
                snippet = video['snippet']
                print(f"【{snippet['title']}"]
                print(f"  影片 ID: {snippet['resourceId']['videoId']}")
                print(f"  網址：https://www.youtube.com/watch?v={snippet['resourceId']['videoId']}")
                print(f"  發佈日期：{snippet['publishedAt']}")
                print("-" * 60)
        else:
            print("未找到使用者上傳的影片。")
            
    except HttpError as e:
        print(f"API 錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")


def main():
    print("請在瀏覽器中開啟授權頁面...")
    print("授權流程完成後，請將授權碼複製並貼上到終端機")
    print("-" * 60)
    
    service = get_authenticated_service()
    
    print("\n正在查詢您的 YouTube 頻道資訊...")
    list_my_channels(service)
    
    print("\n正在查詢您的 YouTube 影片...")
    list_my_videos(service)


if __name__ == '__main__':
    # 禁用 HTTPS 驗證（僅用於本地開發）
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    main()
```

#### 5.3 範例三：搜尋 YouTube 影片

```python
"""
範例三：使用 YouTube Data API 搜尋影片
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

def search_videos(api_key, query, max_results=10):
    """
    搜尋 YouTube 影片
    
    Args:
        api_key: Google API 金鑰
        query: 搜尋關鍵字
        max_results: 返回結果數量（上限 50）
    
    Returns:
        影片清單
    """
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            videoCategoryId='10',  # 娛樂類別
            maxResults=max_results
        )
        
        response = request.execute()
        
        videos = []
        for item in response.get('items', []):
            video_id = item['id']['videoId']
            snippet = item['snippet']
            
            videos.append({
                'videoId': video_id,
                'title': snippet['title'],
                'description': snippet['description'][:100],
                'thumbnails': snippet['thumbnails']['default']['url'],
                'channelId': snippet['channelId'],
                'publishedAt': snippet['publishedAt']
            })
        
        return videos
        
    except HttpError as e:
        print(f"API 錯誤：{e}")
        return []
    except Exception as e:
        print(f"發生錯誤：{e}")
        return []


def main():
    API_KEY = 'YOUR_API_KEY_HERE'
    query = 'Python programming tutorial'
    
    print(f"搜尋：{query}")
    print("=" * 60)
    
    videos = search_videos(API_KEY, query, max_results=10)
    
    if videos:
        for i, video in enumerate(videos, 1):
            print(f"\n[{i}] {video['title']}")
            print(f"    ID: {video['videoId']}")
            print(f"    網址：https://www.youtube.com/watch?v={video['videoId']}")
            print(f"    描述：{video['description']}")
    else:
        print("未找到相關影片。")


if __name__ == '__main__':
    main()
```

### 6. 測試與驗證

#### 6.1 測試環境配置

建立 `test_environment.py` 檔案：

```python
"""
Google API Python Client 環境測試
"""

import sys
import subprocess
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

def test_python_version():
    """測試 Python 版本"""
    print("=" * 60)
    print("Python 版本測試")
    print("=" * 60)
    
    version = sys.version_info
    print(f"Python 版本：{version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 10:
        print("✓ Python 版本符合要求（>= 3.10）")
        return True
    else:
        print(f"✗ Python 版本不符合要求（需要 >= 3.10）")
        return False


def test_installed_packages():
    """測試已安裝的套件"""
    print("\n" + "=" * 60)
    print("套件安裝測試")
    print("=" * 60)
    
    packages = [
        'google-api-python-client',
        'google-auth',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'httplib2',
        'uritemplate'
    ]
    
    all_installed = True
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} - 未安裝")
            all_installed = False
    
    return all_installed


def test_basic_api():
    """測試基本 API 功能"""
    print("\n" + "=" * 60)
    print("基本 API 功能測試")
    print("=" * 60)
    
    # 測試 API 初始化
    try:
        # 使用測試 API 金鑰（會失敗，但測試初始化邏輯）
        youtube = build('youtube', 'v3', developerKey='test_key')
        print("✓ API 初始化邏輯正常")
    except Exception as e:
        print(f"✗ API 初始化錯誤：{e}")
        return False
    
    return True


def test_auth_flow():
    """測試認證流程（僅測試邏輯，不實際認證）"""
    print("\n" + "=" * 60)
    print("認證流程測試")
    print("=" * 60)
    
    # 檢查憑證檔案是否存在
    if not os.path.exists('client_secret.json'):
        print("✗ 請先建立 client_secret.json 憑證檔案")
        return False
    
    # 測試 Flow 物件建立
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/youtube.readonly']
        )
        print("✓ OAuth 2.0 Flow 物件建立成功")
        return True
    except Exception as e:
        print(f"✗ Flow 物件建立失敗：{e}")
        return False


def run_all_tests():
    """執行所有測試"""
    print("\n" + "=" * 60)
    print("Google API Python Client 環境測試")
    print("=" * 60)
    
    import os
    
    results = []
    
    # 測試 Python 版本
    results.append(("Python 版本", test_python_version()))
    
    # 測試套件安裝
    results.append(("套件安裝", test_installed_packages()))
    
    # 測試基本 API
    results.append(("基本 API", test_basic_api()))
    
    # 測試認證流程
    results.append(("認證流程", test_auth_flow()))
    
    # 輸出結果
    print("\n" + "=" * 60)
    print("測試結果總覽")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✓ 通過" if passed else "✗ 失敗"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("恭喜！所有測試通過。")
    else:
        print("部分測試未通過，請修正問題後再試。")
    print("=" * 60)
    
    return all_passed


if __name__ == '__main__':
    run_all_tests()
```

執行測試：

```bash
python test_environment.py
```

#### 6.2 測試範例程式碼

建立 `test_examples.py` 檔案：

```python
"""
Google API Python Client 範例測試
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def test_channel_search():
    """測試頻道搜尋"""
    print("\n【測試 1：搜尋 GoogleDevelopers 頻道】")
    print("-" * 60)
    
    API_KEY = 'YOUR_API_KEY_HERE'  # 請替換為您的 API 金鑰
    
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        response = youtube.channels().list(
            part='snippet,statistics',
            forUsername='GoogleDevelopers',
            maxResults=1
        ).execute()
        
        if response.get('items'):
            channel = response['items'][0]
            print(f"✓ 找到頻道：{channel['snippet']['title']}")
            print(f"  訂閱人數：{channel['statistics']['subscriberCount']:,}")
        else:
            print("✗ 未找到頻道")
            
    except HttpError as e:
        print(f"✗ API 錯誤：{e}")
    except Exception as e:
        print(f"✗ 發生錯誤：{e}")


def test_video_search():
    """測試影片搜尋"""
    print("\n【測試 2：搜尋 Python 相關影片】")
    print("-" * 60)
    
    API_KEY = 'YOUR_API_KEY_HERE'
    
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        response = youtube.search().list(
            part='snippet',
            q='Python programming',
            type='video',
            maxResults=5
        ).execute()
        
        if response.get('items'):
            print(f"✓ 找到 {len(response['items'])} 個影片")
            for item in response['items'][:3]:
                print(f"  - {item['snippet']['title']}")
        else:
            print("✗ 未找到影片")
            
    except HttpError as e:
        print(f"✗ API 錯誤：{e}")
    except Exception as e:
        print(f"✗ 發生錯誤：{e}")


def test_my_channels():
    """測試使用者自己的頻道（需要認證）"""
    print("\n【測試 3：查詢使用者自己的頻道】")
    print("-" * 60)
    
    print("此測試需要 OAuth 2.0 認證...")
    print("請先完成認證流程，然後執行此測試。")
    
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        
        CLIENT_SECRETS_FILE = 'client_secret.json'
        SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
        
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES
        )
        credentials = flow.run_console()
        
        youtube = build('youtube', 'v3', credentials=credentials)
        
        response = youtube.channels().list(
            part='snippet',
            mine=True
        ).execute()
        
        if response.get('items'):
            print(f"✓ 找到 {len(response['items'])} 個使用者頻道")
            for channel in response['items']:
                print(f"  - {channel['snippet']['title']}")
        else:
            print("✗ 未找到使用者頻道")
            
    except Exception as e:
        print(f"✗ 發生錯誤：{e}")


if __name__ == '__main__':
    import os
    
    # 檢查是否已配置 API 金鑰
    if 'YOUR_API_KEY_HERE' in open('test_examples.py').read():
        print("⚠ 請先將 test_examples.py 中的 'YOUR_API_KEY_HERE' 替換為您的 API 金鑰")
        print("  或者，使用 OAuth 認證方式測試。")
    else:
        test_channel_search()
        test_video_search()
        
        if os.path.exists('client_secret.json'):
            test_my_channels()
```

執行測試：

```bash
python test_examples.py
```

### 7. 注意事項

#### 7.1 安全性注意事項

1. **API 金鑰保護**：
   - 不要將 API 金鑰公開在版本控制系統（如 GitHub）中
   - 使用環境變數或配置檔案管理 API 金鑰
   - 定期輪換 API 金鑰

2. **OAuth 2.0 憑證保護**：
   - `client_secret.json` 不應該上傳到版本控制系統
   - 建議使用 `.gitignore` 排除憑證檔案
   - 限制憑證檔案的存取權限（如 `chmod 600 client_secret.json`）

3. **授權範圍最小化**：
   - 只請求所需的授權範圍
   - 定期審查和更新授權範圍

#### 7.2 最佳實踐

1. **使用虛擬環境**：避免依賴套件衝突
2. **使用 API 金鑰時**：
   - 限制金鑰的使用範圍
   - 設定每日使用額度限制
3. **使用 OAuth 2.0 時**：
   - 定期輪換存取令牌
   - 妥善處理存取令牌過期的情況

#### 7.3 常見問題

| 問題 | 解決方案 |
|------|---------|
| API 金鑰無效 | 檢查金鑰是否正確，確認 API 已啟用 |
| OAuth 認證失敗 | 檢查憑證檔案路徑，確認授權範圍設定正確 |
| 找不到憑證檔案 | 使用絕對路徑或相對路徑指定憑證檔案位置 |
| 套件安裝錯誤 | 使用 Python 3.10 或更高版本，檢查網路連線 |

#### 7.4 額外資源

- [Google API Python Client 官方文檔](https://googleapis.github.io/google-api-python-client/)
- [YouTube Data API 參考文檔](https://developers.google.com/youtube/data/reference/rest)
- [Google API Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained)
- [OAuth 2.0 官方指南](https://developers.google.com/identity/protocols/oauth2)

### 附錄

#### A. 常用 API 範圍（Scopes）

| 範圍 | 說明 |
|------|------|
| `https://www.googleapis.com/auth/youtube.readonly` | 僅讀取 YouTube 資料 |
| `https://www.googleapis.com/auth/youtube` | 完整存取 YouTube |
| `https://www.googleapis.com/auth/youtube.force-ssl` | 使用 HTTPS 存取 YouTube |
| `https://www.googleapis.com/auth/youtube.upload` | 上傳影片 |

#### B. 常用 API 端點

| API | 版本 | 端點 |
|-----|------|------|
| YouTube Data API | v3 | https://www.googleapis.com/youtube/v3 |
| Google Drive API | v3 | https://www.googleapis.com/drive/v3 |
| Google Sheets API | v4 | https://www.googleapis.com/sheets/v4 |

#### C. 錯誤碼說明

| 錯誤碼 | 說明 |
|--------|------|
| 401 Unauthorized | 認證失敗 |
| 403 Forbidden | 無權限存取 |
| 404 Not Found | 資源不存在 |
| 429 Too Many Requests | 請求超過限制 |
| 500 Internal Server Error | 伺服器錯誤 |

**報告版本**：1.0  
**最後更新**：$(date)  
**作者**：AI Assistant  
**參考來源**：  
- https://github.com/googleapis/google-api-python-client/  
- https://developers.google.com/youtube/data/libraries#python
