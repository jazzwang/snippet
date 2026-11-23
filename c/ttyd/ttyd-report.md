# ttyd 技術報告

**報告日期：** 2026-11-22  
**工具：** ttyd (Terminal over the Web Daemon)  
**版本：** 1.6.0

## 1. 簡介

ttyd 是一個簡單的終端機分享工具，可讓使用者透過瀏覽器共享本地終端機指令。該工具基於 libuv 和 libwebsockets 建構，支援 CJK（中文、日文、韓文）輸入法和 IME，並提供 ZMODEM/trzsz 檔案傳輸、Sixel 影像輸出等功能。

**官方網站：** https://tsl0922.github.io/ttyd  
**GitHub 儲存庫：** https://github.com/tsl0922/ttyd

### 主要特性

- 基於 libuv 和 libwebsockets，效能優異
- 完整功能終端機，支援 CJK 文字和 IME
- ZMODEM / trzsz 檔案傳輸支援
- Sixel 影像輸出支援
- SSL 加密支援（OpenSSL / Mbed TLS）
- 可執行自訂命令
- 基本認證支援
- 跨平台：macOS、Linux、FreeBSD/OpenBSD、OpenWrt、Windows

## 2. 系統需求

### 必要相依套件

| 平台 | 相依套件 |
|------|----------|
| Linux (Debian/Ubuntu) | build-essential, cmake, git, libjson-c-dev, libwebsockets-dev |
| macOS | Homebrew 或 MacPorts |
| Windows | MSYS2 或 MinGW（需自行編譯） |

### 額外依賴（從原始碼編譯時）

- libwebsockets（若系統套件過舊，需自行編譯）
- lrzsz（用於 ZMODEM 檔案傳輸）
- img2sixel 或 lsix（用於 Sixel 影像輸出）

## 3. 安裝步驟

### 3.1 Linux (Debian/Ubuntu)

#### 方法一：使用系統套件（推薦）

```bash
# 安裝系統套件
sudo apt update
sudo apt install ttyd

# 檢查版本
ttyd --version
```

#### 方法二：從原始碼編譯

```bash
# 安裝必要相依套件
sudo apt install build-essential cmake git libjson-c-dev libwebsockets-dev

# 克隆儲存庫
git clone https://github.com/tsl0922/ttyd.git
cd ttyd

# 建立編譯目錄並編譯
mkdir build && cd build
cmake ..
make && make install

# 確認安裝成功
ttyd --version
```

#### 方法三：使用 Snap

```bash
sudo snap install ttyd --classic
```

### 3.2 macOS

#### 使用 Homebrew

```bash
# 安裝 ttyd
brew install ttyd

# 檢查版本
ttyd --version
```

#### 使用 MacPorts

```bash
sudo port install ttyd
```

### 3.3 Windows

#### 方法一：下載二進位檔案（推薦）

```powershell
# 從 GitHub Releases 下載
# https://github.com/tsl0922/ttyd/releases

# 將 ttyd.exe 複製到 PATH 目錄（例如 C:\Windows\System32）
# 或建立目錄並將 ttyd.exe 加入該目錄
```

#### 方法二：使用 WinGet

```powershell
winget install tsl0922.ttyd
```

#### 方法三：使用 Scoop

```powershell
scoop install ttyd
```

#### 方法四：自行編譯

```bash
# 使用 MSYS2 或 MinGW
git clone https://github.com/tsl0922/ttyd.git
cd ttyd
# 參考官方 Wiki 編譯步驟
# https://github.com/tsl0922/ttyd/wiki/Compile-on-Windows
```

### 3.4 OpenWrt

```bash
opkg update
opkg install ttyd
```

## 4. 測試與驗證

### 4.1 基本功能測試

#### 啟動 ttyd 並驗證

```bash
# 使用預設命令和端口
ttyd bash

# 或使用自訂命令
ttyd --port 7681 echo "Hello, ttyd!"

# 在另一終端機檢查是否監聽
netstat -tlnp | grep 7681
# 或
ss -tlnp | grep 7681
```

#### 驗證網頁介面

1. 在瀏覽器中開啟 `http://localhost:7681`
2. 確認出現 ttyd 終端機介面
3. 測試基本輸入輸出功能

**預期結果：**
- 網頁能正常載入 ttyd 介面
- 可在終端機輸入文字並看到回顯
- 可以執行命令（如 `echo`、`ls`、`pwd`）

### 4.2 認證測試

```bash
# 啟用基本認證
ttyd --port 7681 --credential "admin:password123" bash

# 在瀏覽器中訪問 http://localhost:7681
# 輸入認證 admin / password123
```

**預期結果：**
- 未提供正確認證時，網頁顯示登入畫面
- 提供正確認證後，可進入終端機

### 4.3 檔案傳輸測試（ZMODEM）

```bash
# 啟動 ttyd
ttyd bash

# 在瀏覽器中打開 ttyd 終端機
# 使用檔案傳輸功能（Ctrl+Shift+U 或點擊檔案傳輸圖示）
# 拖曳檔案到終端機視窗
```

**預期結果：**
- 檔案可透過 ZMODEM 協議傳輸
- 若已安裝 lrzsz，可執行 `rz` 或 `sz` 命令進行檔案傳輸

### 4.4 SSL 加密測試

```bash
# 生成自簽名證書（僅測試用）
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# 啟動 ttyd 並啟用 SSL
ttyd --port 7681 --ssl --ssl-cert cert.pem --ssl-key key.pem bash

# 在瀏覽器中訪問 https://localhost:7681（需接受不安全連接）
```

**預期結果：**
- 瀏覽器顯示 SSL 警告（因使用自簽名證書）
- 終端機連接正常運作

### 4.5 最大連接數測試

```bash
# 限制最大連接數為 2
ttyd --port 7681 --max-clients 2 bash
```

**預期結果：**
- 第 3 個連線嘗試時，應顯示「Maximum clients reached」錯誤訊息

### 4.6 讀取模式測試（只讀）

```bash
# 啟動只讀終端機
ttyd --port 7681 --readonly echo "This terminal is readonly"
```

**預期結果：**
- 終端機可顯示輸出，但無法輸入文字

### 4.7 單一連線模式測試

```bash
# 僅接受一個連線，連線斷開後退出
ttyd --port 7681 --once bash

# 第一個連線會啟動終端機
# 連線斷開後，ttyd 程式會自動退出
```

**預期結果：**
- 斷開連線後，ttyd 程式立即終止

### 4.8 工作目錄測試

```bash
# 指定工作目錄
mkdir /tmp/ttyd-test
cd /tmp/ttyd-test
echo "test content" > test.txt

ttyd --port 7681 --cwd /tmp/ttyd-test pwd
```

**預期結果：**
- 終端機顯示 `/tmp/ttyd-test` 為工作目錄

### 4.9 客戶端選項測試

```bash
# 發送客戶端選項（如終端機類型）
ttyd --port 7681 -t "term=xterm-256color" -t "cols=120" -t "rows=40" bash
```

**預期結果：**
- 終端機使用指定的列數、行數和終端機類型

### 4.10 IPv6 測試

```bash
# 啟用 IPv6
ttyd --port 7681 --ipv6 bash

# 在瀏覽器訪問 http://[::1]:7681
```

**預期結果：**
- IPv6 地址可正常連線

### 4.11 UNIX Domain Socket 測試

```bash
# 使用 UNIX domain socket
ttyd --interface /tmp/ttyd.sock bash
```

**預期結果：**
- 可透過 socket 文件連線（需配合反向代理使用）

## 5. 常見使用範例

### 5.1 基本使用

```bash
# 啟動 bash 終端機（預設端口 7681）
ttyd bash

# 啟動特定命令
ttyd npm run dev

# 指定端口
ttyd --port 8080 python3 app.py
```

### 5.2 生產環境配置

```bash
# 啟用認證和限制連線數
ttyd \
  --port 7681 \
  --max-clients 10 \
  --credential "admin:your_password" \
  --ping-interval 5 \
  python3 app.py
```

### 5.3 使用反向代理

```bash
# 設定 base-path 和允許反向代理
ttyd \
  --port 7681 \
  --base-path /terminal \
  --max-clients 0 \
  bash
```

**反向代理配置（Nginx 範例）：**

```nginx
server {
    listen 80;
    server_name example.com;

    location /terminal {
        proxy_pass http://localhost:7681;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 5.4 Docker 部署

```dockerfile
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libjson-c-dev \
    libwebsockets-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN cmake . && make

EXPOSE 7681
CMD ["ttyd", "bash"]
```

## 6. 故障排除

### 6.1 無法啟動 ttyd

**問題：** `ttyd: command not found`

**解決方案：**
```bash
# 檢查是否安裝正確
which ttyd

# 若未找到，檢查 PATH 是否包含安裝目錄
# 或重新編譯並執行 make install
```

### 6.2 端口已被使用

**問題：** `bind: address already in use`

**解決方案：**
```bash
# 使用隨機端口
ttyd --port 0 bash

# 或指定其他端口
ttyd --port 8080 bash
```

### 6.3 無法連線

**問題：** 瀏覽器顯示「無法連線」或「網路錯誤」

**檢查事項：**
```bash
# 確認服務正在運行
ps aux | grep ttyd

# 確認端口監聽
netstat -tlnp | grep 7681

# 確認防火牆設定
# Linux: sudo ufw allow 7681/tcp
# macOS: 系統設定 > 安全性與隱私權 > 防火牆
```

### 6.4 SSL 錯誤

**問題：** 瀏覽器顯示 SSL 證書錯誤

**解決方案：**
```bash
# 使用有效的證書（非自簽名）
# 或僅用於測試時接受不安全連接
```

## 7. 安全考量

### 7.1 生產環境建議配置

```bash
# 完整的安全配置範例
ttyd \
  --port 7681 \
  --max-clients 10 \
  --credential "admin:secure_password" \
  --ping-interval 5 \
  --check-origin \
  --once \
  bash
```

### 7.2 注意事項

- **不要暴露於公開網路**：建議使用反向代理並限制訪問
- **使用 SSL**：生產環境應啟用 SSL 加密
- **限制連線數**：設定 `--max-clients` 避免資源耗盡
- **定期更新**：保持 ttyd 為最新版本以獲得安全修補

## 8. 參考資源

- **官方網站：** https://tsl0922.github.io/ttyd
- **GitHub 儲存庫：** https://github.com/tsl0922/ttyd
- **編譯指南（Windows）：** https://github.com/tsl0922/ttyd/wiki/Compile-on-Windows
- **使用範例：** https://github.com/tsl0922/ttyd/wiki/Example-Usage
- **DockerHub：** https://hub.docker.com/r/tsl0922/ttyd
- **Releases：** https://github.com/tsl0922/ttyd/releases

## 9. 附錄：主要參數列表

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `-p, --port` | 監聽端口 | 7681 |
| `-i, --interface` | 網路介面或 UNIX socket | - |
| `-c, --credential` | 基本認證 | - |
| `-S, --ssl` | 啟用 SSL | 關閉 |
| `-C, --ssl-cert` | SSL 證書檔案路徑 | - |
| `-K, --ssl-key` | SSL 金鑰檔案路徑 | - |
| `-m, --max-clients` | 最大連線數 | 0（無限制） |
| `-o, --once` | 僅接受一個連線 | 關閉 |
| `-B, --browser` | 開啟預設瀏覽器 | 關閉 |
| `-R, --readonly` | 只讀模式 | 關閉 |
| `-t, --client-option` | 客戶端選項 | - |
| `-d, --debug` | 日誌級別 | 7 |
| `-6, --ipv6` | 啟用 IPv6 | 關閉 |
| `--url-arg` | 允許 URL 參數傳遞命令 | 關閉 |
| `--check-origin` | 檢查來源 | 關閉 |

**報告結束**
