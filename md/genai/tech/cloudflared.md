# cloudflared

- Website
  - [https://try.cloudflare.com/](https://try.cloudflare.com/)

## 2026-09-22

- Tool: Pi Agent +  google/gemini-2.5-flash
- Learn from : https://blog.gslin.org/archives/2026/09/21/13216/

> [!QUESTION]
> 將 `cloudflare-quick-tunnels.md` 整理成繁體中文部落格文章，使用 speak-human-tw skill 潤飾詞句，不必列表，請直接修改，最後存成 `cloudflare-quick-tunnels.blog.md`

- title: "Cloudflare Quick Tunnels (cloudflare.com)"
- source: "https://news.ycombinator.com/item?id=49754785"
- author: "[[jcbhmr]]"
- published: 2026-09-18
- created: 2026-09-22

## Cloudflare Quick Tunnels：新瓶舊酒還是實用工具？網路社群熱議大盤點

近期，Cloudflare 推出了一個全新的「Quick Tunnels」登陸頁面，再度引發了網路開發者社群的熱烈討論。這項服務究竟是否如其名般快速便利？它與現有的 Cloudflare Tunnels 有何不同？在眾多內網穿透解決方案中，Quick Tunnels 的定位又在哪裡？本文將彙整社群的多元觀點，帶你一窺這項服務的真實面貌與其中爭議。

### Cloudflare Quick Tunnels 是什麼？

Cloudflare Quick Tunnels 主打提供一種快速、免身份驗證的方式，將本機服務公開到網際網路。透過單一指令，使用者即可建立 HTTPS 隧道，將本機開發中的應用程式、私人服務等，安全地暴露給外部存取。對於需要測試網頁應用程式、分享原型或臨時存取本機資源的開發者來說，這提供了一個輕量級的解決方案。

### 爭議點一：是新產品還是舊酒新瓶？

社群中一個主要爭論點是，Cloudflare Quick Tunnels 究竟是不是新產品。許多資深使用者指出，匿名快速隧道（anonymous quick tunnels）至少在五年前就已存在，而現在看到的更像是一個「換上新潮介面」的舊產品。這引發了一些關於資訊透明度的討論，認為像 Hacker News 這樣的平台，在分享這類文章時，應該註明其發布日期或更新性質。

### 用途與價值：誰需要 Quick Tunnels？

儘管存在爭議，許多使用者仍發現 Quick Tunnels 相當實用。例如：
*   **本機 LLM 模型部署：** 將本機執行的大型語言模型（LLM）透過 HTTPS 公開，供其他工具或機器存取。
*   **分享迷你應用程式：** 夫妻或團隊間共享基於本機開發的迷你應用程式，例如購物清單、葡萄酒追蹤器等。
*   **測試與原型開發：** 快速公開開發中的網頁應用程式，便於手機測試或向同事展示原型。
整體來說，對於需要臨時、快速、免配置公開本機服務的場景，Quick Tunnels 提供了一個便捷的選項。

### 競爭者與替代方案

討論中，Cloudflare Quick Tunnels 不可避免地被拿來與其他內網穿透或 VPN 服務比較：
*   **Tailscale / Netbird / Pangolin：** 這些服務提供基於 WireGuard 的網狀 VPN 解決方案，強調 P2P 連接、身份驗證、存取控制和 NAT 穿透。Tailscale Funnel 甚至提供了類似 Quick Tunnels 的公開服務功能，但通常在 Tailnet 內部更為強大，且可設定路徑來路由到不同本機埠。使用者普遍認為 Tailscale 在易用性和功能整合上更勝一籌，但也有人抱怨其 iPhone 版有耗電問題。Netbird 和 Pangolin 則被視為 Tailscale 的自託管替代方案，提供更精細的控制和更豐富的 UI。
*   **WireGuard：** 被認為是基礎技術，Tailscale 等產品在其之上提供了更友善的「可用性層」。對於熟悉網路配置且需求單純的用戶，直接使用 WireGuard 也是個選擇。
*   **ngrok / frp / bore：** 這些是更直接的隧道服務競爭者，其中 `frp` 因其輕量和自託管特性而受到好評，可用於將本機服務（如 Minecraft 伺服器）公開。
*   **OpenZiti：** 提供「暗服務」（dark services）功能，強調粒度化的存取控制和路由，確保服務不會直接暴露在公網上。

### 疑慮與批評：社群的不安

社群對 Cloudflare Quick Tunnels 也提出了一些擔憂：
*   **產品成熟度與維護：** 有人指出 `cloudflared` 工具在 macOS 上的安裝問題自 2021 年就存在，顯示 Cloudflare 對隧道產品的維護投入可能不足。也有人批評其 API 混亂、不斷更名重組，難以跟上。
*   **「AI 味」的登陸頁面：** 不少人直指 Quick Tunnels 的新登陸頁面充滿了「AI 生成」的痕跡，例如奇怪的措辭、不一致的設計品質、手機版渲染問題等，這讓人懷疑 Cloudflare 是否投入足夠的人力進行品質審查。
*   **中心化與隱私：** 由於所有流量都經過 Cloudflare 系統，這引發了對數據隱私和單點故障的擔憂。雖然 Cloudflare 擁有強大的基礎設施能處理巨量流量，但這種中心化趨勢仍讓部分使用者感到不安，尤其是在考慮到美國公司可能受政府指令影響的情況下。此外，也有人擔心 Cloudflare 會「監看」通過隧道的明文流量（儘管可以透過 TLS / mTLS 加密解決）。
*   **企業級功能：** 儘管 Quick Tunnels 旨在簡化個人使用，但 Cloudflare 的許多產品仍偏向企業級應用，導致個人使用者在配置上遇到困難。

### 結論

Cloudflare Quick Tunnels 作為一個快速、免費的本機服務公開工具，在特定場景下確實能帶來便利。然而，其產品歷史、頁面設計品質，以及隨之而來的中心化與隱私考量，都讓網路社群對其抱持著複雜的態度。對於尋求簡單解決方案的開發者來說，它不失為一個選項；但若考量長期穩定性、功能彈性或對中心化的擔憂，市場上仍有許多強大的替代方案值得探索。最終，選擇哪種工具，端看個人或團隊的需求與信任偏好。
