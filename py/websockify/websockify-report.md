# Websockify 技術報告

**生成日期:** 2026-11-23

## 概述

Websockify 是一個 WebSocket 代理工具，原本名為 `wsproxy`，是 [noVNC](https://github.com/novnc/noVNC) 專案的一部分。它的核心功能是在 WebSocket 流量與普通 Socket 流量之間進行轉換：接受 WebSocket 握手、解析請求，然後將流量雙向轉發給目標端點。

## 系統需求

- **Python 3.x**
- **NumPy**（可選，用於提升效能）
- **OpenSSL**（如需加密連接 wss://）

## 安裝步驟

### 方法一：從 PyPI 安裝

```bash
pip3 install websockify
```

### 方法二：從源碼安裝

```bash
# 下載並解壓 source 碼
git clone https://github.com/novnc/websockify.git
cd websockify

# 以 root 身分執行安裝（會自動安裝 NumPy）
python3 setup.py install

# 確認安裝成功
websockify --help
```

**注意：** 如果無法編譯 NumPy 或不想安裝，可編輯 `setup.py` 移除 `install_requires=['numpy']` 行。

### 方法三：使用 Docker

```bash
# 建置映像
./docker/build.sh

# 執行（以 port 7000 轉發至 10.1.1.1:5902 為例）
docker run -it --rm -p 7000:80 novnc/websockify 80 10.1.1.1:5902
```

## 基本使用範例

### 1. 簡單轉發（端口映射）

將本地 7000 端口轉發至遠端服務：

```bash
websockify 7000 10.1.1.1:5902
```

### 2. 監聽所有介面

```bash
websockify 7000 -- hostname:5901
```

### 3. 繞轉程式（Wrap a Program）

啟動並代理本地程式的 TCP 連接：

```bash
# 繞轉 vncserver
./run 5901 --wrap-mode=ignore -- vncserver -geometry 1024x768 :1

# 繞轉 telnetd（設定重新啟動）
sudo ./run 2023 --wrap-mode=respawn -- telnetd -debug 2023
```

## 測試步驟

### 測試一：基本握手測試

1. 啟動 websockify：

   ```bash
   websockify 7000 localhost:5901
   ```

2. 使用瀏覽器開啟 WebSocket 測試頁面：

   ```html
   <script>
     const ws = new WebSocket('ws://localhost:7000');
     ws.onopen = () => console.log('WebSocket 連線成功');
     ws.onmessage = (event) => console.log('收到訊息:', event.data);
     ws.send('Hello');
   </script>
   ```

3. 觀察終端輸出是否顯示 WebSocket 握手完成及流量轉發。

### 測試二：使用 noVNC 客戶端測試

1. 啟動 websockify：

   ```bash
   websockify 7000 localhost:5901
   ```

2. 開啟瀏覽器至 `http://localhost:7000/novnc`

3. 設定 VNC 連線目標為 `localhost:5901`

4. 驗證能否正常顯示並控制 VNC 畫面。

### 測試三：程式繞轉測試

```bash
# 啟動測試服務（如 telnetd）
sudo ./run 2023 --wrap-mode=respawn -- telnetd -debug 2023
```

使用 WebSocket 客戶端連線至 `ws://localhost:2023`，驗證流量能否正確轉發至 telnetd 的 2023 端口。

## 驗證步驟

### 一、加密連接驗證（WSS）

#### 1. 產生自簽名憑證

```bash
openssl req -new -x509 -days 365 -nodes -out self.pem -keyout self.pem
```

- Common Name 輸入 WebSocket 伺服器主機名

#### 2. 啟動加密 WebSocket

```bash
websockify 7000 localhost:5901 --cert=self.pem --key=self.pem
```

#### 3. 驗證加密連接

```bash
# 使用瀏覽器開啟 WSS 頁面
const ws = new WebSocket('wss://localhost:7000');
```

#### 4. 處理自簽名憑證信任問題

瀏覽器可能要求信任憑證，可透過以下方式處理：

- 將憑證安裝到系統信任庫
- 或先連線至相同憑證的 HTTPS 網址並批准例外

**範例：**

```
https://my.local:8443 → 批准例外
wss://my.local:8001 → 使用相同憑證
```

#### 5. 商業憑證設定

若有商業 SSL 憑證，需將伺服器憑證與中間憑證合併：

```bash
websockify 443 --cert=all.pem --key=key.pem :443 --ssl-only --ssl-version tlsv1_2
```

### 二、Session Recording 驗證

```bash
websockify 7000 localhost:5901 --record=recording.log
```

- 確認 WebSocket 流量被記錄至 `recording.log`
- 驗證記錄檔案包含完整的雙向流量

### 三、Mini Webserver 驗證

```bash
websockify 7000 localhost:5901 --web=/path/to/webroot
```

- 開啟瀏覽器至 `http://localhost:7000`
- 驗證靜態檔案能否正常顯示
- 同時驗證 WebSocket 代理功能不受影響

### 四、Authentication 驗證

```bash
websockify 7000 localhost:5901 --auth-plugin BasicAuth --auth-source=users.json
```

- 測試是否需要提供認證資訊
- 驗證錯誤認證被拒絕

### 五、Token Plugin 驗證

```bash
websockify 7000 localhost:5901 --token-plugin TokenRedis --token-source=myredis
```

- 測試不同 token 能否連接到不同目標
- 驗證 token 參數 `?token=xxx` 正確生效

## 常見選項

| 選項 | 說明 |
|------|------|
| `-D` | 以 daemon 模式執行 |
| `--web DIR` | 附加靜態檔案伺服器 |
| `--cert/CERT` | SSL 憑證檔名 |
| `--key/KEY` | SSL 金鑰檔名 |
| `--log-file FILE` | 記錄日誌至檔案 |
| `--record FILE` | 記錄 WebSocket 流量 |
| `--auth-plugin CLASS` | 啟用認證 |
| `--token-plugin CLASS` | 啟用 token 分發 |
| `--ssl-only` | 僅允許加密連接 |
| `--wrap-mode MODE` | 設定繞轉模式（ignore/respawn） |

## 繞轉模式說明

| 模式 | 說明 |
|------|------|
| `ignore` | 程式退出或 daemon 時保持靜默 |
| `respawn` | 程式退出時重新啟動 |

## Docker 執行範例

```bash
# 簡單端口轉發
docker run -it --rm -p 7000:80 novnc/websockify 80 10.1.1.1:5902

# 附加靜態檔案與加密
docker run -it --rm \
  -p 443:443 \
  -v websockify-data:/data \
  novnc/websockify \
  --cert /data/self.pem \
  --web /data/noVNC \
  :443 \
  --token-plugin TokenRedis \
  --token-source myredis.local:6379 \
  --ssl-only \
  --ssl-version tlsv1_2
```

## 注意事項

1. **WebSocket 協議版本**：Websockify 0.5.0+ 僅支援 HyBi / IETF 6455 協議，不支援舊版 Base64 編碼格式。

2. **SSL 自動偵測**：Websockify 會自動偵測客戶端發送的頭一個 byte：
   - `\x16` → SSL/TLS
   - `\x80` → WebSocket

3. **端口衝突處理**：若目標端點已被佔用，websockify 可透過繞轉程式或 rebind 庫自動處理。

4. **認證與 token**：
   - `--auth-plugin` 可對 WebSocket 或普通 HTTP 請求進行認證
   - `--token-plugin` 可根據 token 參數路由至不同目標

## 參考資源

- [GitHub 原始碼](https://github.com/novnc/websockify)
- [noVNC 專案](https://github.com/novnc/noVNC)
- [特性矩陣](https://github.com/novnc/websockify/wiki/Feature_Matrix)
- [Discussions](https://groups.google.com/forum/?fromgroups#!forum/novnc)
- [GitHub Issues](https://github.com/novnc/websockify/issues)

## 附錄：其他語言實作

- [websockify-js](https://github.com/novnc/websockify-js)（JavaScript/Node.js）
- [websockify-other](https://github.com/novnc/websockify-other)（C、Clojure、Ruby）

## 附錄：整合 SSH 與 Websockify

### 概述
Websockify 本身**不支援 SSH 協議**，它只是將 WebSocket 流量轉換為原始 TCP 流量。因此，websockify 本身**無法直接與 openssh-server 整合**，但透過以下方式可以實現功能。

### 方案一：Websockify + websocat

#### 伺服器端設定
```bash
# 基本設定（監聽 port 8080，轉發至 port 22）
websockify 8080 127.0.0.1:22

# 加密設定（WSS over SSL on port 443）
websockify --cert=/path/to/fullchain.pem --key=/path/to/privkey.pem 443 127.0.0.1:22
```

#### 客戶端連線
```bash
# 使用 websocat 連線
ssh -o ProxyCommand="websocat -b - wss://your-server:8080" user@your-server

# 加入 ~/.ssh/config
Host my-ssh
    HostName your-server
    User your-username
    ProxyCommand websocat -b - wss://%h:8080

ssh my-ssh
```

### 方案二：Websockify 繞轉 sshd（Wrap Mode）

```bash
# 每次 WebSocket 連線時啟動新的 sshd 進程
websockify 8080 --wrap-mode=respawn -- /usr/sbin/sshd -i
```

**優點**：不需要在伺服器端設定 port 22
**缺點**：SSH 認證流程可能需要調整

### 支援 WebSocket 的 SSH 客戶端工具

| 工具 | 說明 | 特點 |
|------|------|------|
| **websocat** | CLI 工具 | 輕量、高效，支援 ProxyCommand |
| **MoltSSH** | 專為 WebSocket SSH 設計 | 提供 session resume、path probing 功能 |
| **webssh** | Web 瀏覽器內嵌 SSH 客戶端 | Python/Tornado，支援金鑰認證、2FA |
| **browser-based SSH** | xterm.js + ssh2 | 在瀏覽器中實作 SSH 客戶端 |

### 使用 Nginx + Websockify 後端

```nginx
server {
    listen 443 ssl;
    server_name ssh.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location /ws {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_read_timeout 86400s;
    }
}
```

SSH 連線設定：
```bash
ssh -o ProxyCommand="websocat -b - wss://ssh.yourdomain.com/ws" user@ssh.yourdomain.com
```

### 限制與注意事項

| 項目 | 說明 |
|------|------|
| **協議轉換** | websockify 僅轉換 WebSocket ↔ TCP，不解析 SSH 協議 |
| **認證方式** | 需確保 sshd 支援 password/public-key 認證（繞轉模式可能影響） |
| **加密** | 建議使用 WSS（加密 WebSocket）並搭配 Nginx SSL |
| **Firewall** | 通常可透過 80/443 端口繞過防火牆限制 |
| **性能** | 相比直連 SSH，WebSocket 會增加額外的協議層 |

### 建議架構

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│   SSH Client    │      │    Websockify   │      │  openssh-server │
│  (websocat /    │◄────►│   (Proxy)       │◄────►│   (sshd)        │
│   MoltSSH)      │      │                 │      │                 │
└─────────────────┘      └─────────────────┘      └─────────────────┘
          │                          │
          │ wss:// (port 443/8080)   │ TCP (port 22)
          ▼                          ▼
    ┌─────────────────┐      ┌─────────────────┐
    │    Nginx        │      │   Firewall      │
    │  (SSL Terminate)│      │  (Bypass Port 22)│
    └─────────────────┘      └─────────────────┘
```

### 結論

✅ **可以整合**：透過 websockify 將 SSH 流量轉換為 WebSocket 流量

⚠️ **需要工具**：需要 websocat、MoltSSH 等支援 WebSocket 的 SSH 客戶端

🔒 **安全性**：建議使用 WSS + Nginx SSL 終端加密

🚀 **最佳實踐**：websockify + websocat + Nginx 是目前最成熟的解決方案

---

**報告更新日期:** 2026-11-23
**對話記錄:** 關於 websockify 與 openssh-server 的整合
```
