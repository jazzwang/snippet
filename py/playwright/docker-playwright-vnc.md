# Docker Playwright VNC

- https://github.com/Booza1981/docker-playwright-vnc

## 2025-07-14

- 緣起：
  - 需要「分身」來跑 MS Teams Live Caption 的 JavaScript
  - 希望可以「多重影分身」，所以把腦筋動到 Playwright 跟 Github Codespaces 身上，這樣就可以透過預先儲存的 Browser Profile 跟登入過的 local storage 來自動化開啟 Live Caption 並且儲存下來。甚至也可以寫成 Github Actions 來排程想紀錄的會議。
- 搜尋：
  - 找到 https://github.com/Booza1981/docker-playwright-vnc 似乎可以滿足部份需求，所以實測一下。

## 2025-07-15

- 實測：
  - 直接用 `gh` Github CLI 開啟 Codespace
```bash
[07/15 09:44:22] ~$ gh cs create -R Booza1981/docker-playwright-vnc
  ✓ Codespaces usage for this repository is paid for by jazzwang
? Choose Machine Type:  [Use arrows to move, type to filter]
> 2 cores, 8 GB RAM, 32 GB storage
  4 cores, 16 GB RAM, 32 GB storage
```