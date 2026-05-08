# Tank OS

- Git Repo
  - https://github.com/LobsterTrap/tank-os

## 2026-05-07

- 緣起：在 LinkedIn 牆上看到好友 repost 這篇
  - https://www.linkedin.com/feed/update/urn:li:activity:7457052274469785601/
```
當作業系統遇上容器化：Tank OS 重新定義 AI 代理的部署方式

最近關注到一個非常有趣的開源專案 Tank OS，由 Red Hat 的首席工程師發起。

它不僅僅是一個 Linux 發行版，更是將 bootc (Bootable Containers) 技術發揮到極致的實踐。

1. 鏡像即系統 (Image-as-OS)：

透過 bootc，你可以像構建 Docker 鏡像一樣構建整個作業系統。

2. 專為 OpenClaw 打造

預裝 AI Agent 框架，開箱即啟動，實現 AI 代理的「設備化」。

3. 原子化更新

支持事務性更新與回滾，徹底解決系統升級崩潰的噩夢。

4. 安全沙盒

預設使用 Podman 以非 root 權限運行，為 AI 代理提供堅固的隔離環境。

如果你正在尋找如何大規模管理 AI 基礎設施，Tank OS 提供的「不可變基礎設施」思路非常值得參考！
```
- 想法：
  - 用 Podman 確實很符合 Red Hat 首席工程師的風格 :P
  - 太久沒追 container 技術的發展，需要花點時間再追一下 `bootc` 的技術定位。感覺有點像 `init`

## 2026-05-08

- 2026-04-28
  - Building a hardened, image-based foundation for AI agents
  - https://www.redhat.com/en/blog/building-hardened-image-based-foundation-ai-agents
- 2026-05-04
  - 紅帽釋出 Tank OS，打造代理式作業系統原型強化 OpenClaw 企業部署安全
  - https://www.ithome.com.tw/news/175509