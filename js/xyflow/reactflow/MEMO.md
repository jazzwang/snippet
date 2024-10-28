# React Flow

- https://reactflow.dev/
- React Flow 12 `@xyflow/react` [packages/react](https://github.com/xyflow/xyflow/tree/main/packages/react)
- React Flow 11 `reactflow` [v11 branch](https://github.com/xyflow/xyflow/tree/v11)

## 2024-10-28

- ( 2024-10-28 08:35:37 )
- 緣起：
  - 先前看到很多 ByteByteGo 或者 LinkedIn 的流程圖，都有 arrow 的動畫效果。好奇他們是用什麼工具畫的，觀察到 React Flow 的結果也有類似效果。
  - [LangFlow](https://github.com/langflow-ai/langflow) 的 UI 也有[相依 reactflow](https://github.com/langflow-ai/langflow/network/dependencies?q=reactflow)
  - 雖然對 React.js 語法不是很熟，但了解一下範例，或許可以作為複雜流程圖的一個替代方案(當 [PlantUML](https://plantuml.com/) 或 [Mermaid.js](https://mermaid.js.org/) 做不出想要的效果時)
- ( 2024-10-28 08:38:12 )
- 安裝：
  - 測試環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet$ gh cs ssh
? Choose codespace:  [Use arrows to move, type to filter]
> jazzwang/snippet (master*): snippet

Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Sun Oct 27 23:58:13 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $
@jazzwang ➜ /workspaces/snippet (master) $ cd js/xyflow/reactflow/
@jazzwang ➜ .../snippet/js/xyflow/reactflow (master) $ npx degit xyflow/vite-react-flow-template lab1
> cloned xyflow/vite-react-flow-template#HEAD to lab1
@jazzwang ➜ .../snippet/js/xyflow/reactflow (master) $ cd lab1/
@jazzwang ➜ .../js/xyflow/reactflow/lab1 (master) $ tree
.
├── LICENSE
├── README.md
├── index.html
├── package-lock.json
├── package.json
├── public
│   └── favicon.ico
├── src
│   ├── App.tsx
│   ├── edges
│   │   └── index.ts
│   ├── index.css
│   ├── main.tsx
│   ├── nodes
│   │   ├── PositionLoggerNode.tsx
│   │   ├── index.ts
│   │   └── types.ts
│   └── vite-env.d.ts
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts

4 directories, 17 files
@jazzwang ➜ .../js/xyflow/reactflow/lab1 (master) $ npm install

added 233 packages, and audited 234 packages in 4s

42 packages are looking for funding
  run `npm fund` for details

4 vulnerabilities (2 moderate, 2 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.

@jazzwang ➜ .../js/xyflow/reactflow/lab1 (master) $ npm run dev

> vite-react-flow-template@0.0.0 dev
> vite


  VITE v5.0.12  ready in 373 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```
- ( 2024-10-28 09:06:20 )
- 結果：
![React Flow Vite Quick Start App](https://i.imgur.com/lVH8Cdx.png)
- 觀察：
  - 還蠻好奇 VS Code 怎麼把 Github Codespace 的 docker `127.0.0.1:5173` 轉到本地開發端的 `127.0.0.1:5173`
  - 從 Codespace 的 `ps ax` 結果，可以看得到 `vite` 跟 `esbuild` 的執行檔。
  - `5173` port 是由 pid 22445 也就是 node 去執行 `vite` 產生的。但沒有看到其他把 port 轉到其他機器的痕跡。
```bash
@jazzwang ➜ /workspaces/snippet (master) $ ps ax
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:00 /sbin/docker-init -- /bin/sh -c echo Container started trap "exit 0" 15 /usr/local/share/ssh-init.sh /usr/local/share/docker-in
      7 ?        S      0:00 sleep infinity
     22 ?        S<s    0:00 sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
   1367 ?        Sl     0:00 dockerd --dns 168.63.129.16
   1374 ?        Ssl    0:00 containerd --config /var/run/docker/containerd/containerd.toml
   5175 ?        Ss     0:00 /bin/sh
   5202 ?        Ss     0:00 /bin/sh
   5383 ?        Ss     0:00 sh /home/codespace/.vscode-remote/bin/384ff7382de624fb94dbaf6da11977bba1ecd427/bin/code-server --log trace --force-disable-user
   5393 ?        Sl     0:05 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd
   5414 ?        Sl     0:35 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node --dns-result-order=ipv4first /vscode/bin/linux-x64/384ff738
   5428 ?        Sl     0:03 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd
   5882 ?        Sl     0:00 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd
   6310 ?        Sl     0:01 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd
   6704 ?        Sl     0:02 /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/node /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd
   6727 pts/1    Ss     0:00 /bin/bash --init-file /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/out/vs/workbench/contrib/terminal/common/s
  19008 pts/0    Ss+    0:00 /bin/bash --init-file /vscode/bin/linux-x64/384ff7382de624fb94dbaf6da11977bba1ecd427/out/vs/workbench/contrib/terminal/common/s
  22433 pts/1    Sl+    0:00 npm run dev
  22444 pts/1    S+     0:00 sh -c vite
  22445 pts/1    Sl+    0:00 node /workspaces/snippet/js/xyflow/reactflow/lab1/node_modules/.bin/vite
  22456 pts/1    Sl+    0:00 /workspaces/snippet/js/xyflow/reactflow/lab1/node_modules/@esbuild/linux-x64/bin/esbuild --service=0.19.12 --ping
  23996 ?        S<s    0:00 sshd: codespace [priv]
  24012 ?        R<     0:00 sshd: codespace@pts/2
  24013 pts/2    S<s    0:00 -bash
  25276 pts/2    R<+    0:00 ps ax
  @jazzwang ➜ /workspaces/snippet (master) $ netstat -nap | grep 5173
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp6       0      0 ::1:5173                :::*                    LISTEN      22445/node
tcp6       0      0 ::1:42322               ::1:5173                ESTABLISHED -
tcp6       0      0 ::1:5173                ::1:42322               ESTABLISHED 22445/node
```
- ( 2024-10-28 09:16:22 )
  - 從 Windows 端觀察，是 `Code.exe` 開了 `5173` port，所以初步只能猜測 VS Code 的 Github Codespace 擴充套件，建立了一個 socket 讓本地端可以直通 github codespace docker 容器的 `5173` port。
  - ![Screenshot 2024-10-28 101034](https://i.imgur.com/2cn5mSK.png)
- ( 2024-10-28 09:55:46 )
  - 看起來應該是 Github Codespace 自身的設計，因為可以從 CLI, IDE/Editor 或 Browser (開啟網頁版 VS Code 的界面)來設定
  - https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace?tool=cli
  - 從 VS Code 的訊息跟文件看起來，分成幾個不同的路徑：
  ![Screenshot 2024-10-28 100038](https://i.imgur.com/sId26nc.png)
    - "Open in Browser" - 就像上面 Windows 程序顯示，VS Code 的 `Code.exe` 會監聽一個 `127.0.0.1:5173`
    - "Preview in Editor" - 感覺是從 Editor (VS Code) 開 Simple Browser，至於到底是連本地端的 `127.0.0.1:5173` 還是遠端的 `127.0.0.1:5173` 就有點難判斷了。
  ![Screenshot (148)](https://i.imgur.com/y2YTwCb.png)
- 雖然 Visibility 有分成 private, public 跟 organization 不同層級，初步判定這應該是 k8s 的網路 port forwarding 功能/權限控管。
```bash
jazzw@JazzBook:~$ gh cs ports
? Choose codespace: jazzwang/snippet (master*): snippet
LABEL  PORT  VISIBILITY  BROWSE URL
       5173  private     https://shiny-zebra-jjrxjgp652gqw-5173.app.github.dev
```
```
jazzw@JazzBook:~$ nslookup shiny-zebra-jjrxjgp652gqw-5173.app.github.dev
Server:  family.cloudflare-dns.com
Address:  2606:4700:4700::1113

Non-authoritative answer:
Name:    tunnels-prod-rel-asse-v3-cluster.southeastasia.cloudapp.azure.com
Address:  20.197.80.108
Aliases:  shiny-zebra-jjrxjgp652gqw-5173.app.github.dev
          tunnels-prod-rel-tm.trafficmanager.net
          v3-asse.cluster.rel.tunnels.api.visualstudio.com
```