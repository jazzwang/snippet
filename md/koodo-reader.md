# Koodo Reader

- 源起：先前偶爾會下載一些 ePUB 格式的電子書來看。macOS 上有 `Books` 可以用，Windows 上試了幾套，還是只有 [`calibre`](https://github.com/kovidgoyal/calibre) 能夠正確顯示中文 ePUB 的一些排版。Android 上應該可以用 「Google 圖書」，其他 Kindle 等就暫時沒研究。想找一個方便管理散亂的電子書，可以「劃線」，可以「備份」「同步」的工具。因此在 Github 上找到 https://github.com/topics/epub 排行第二的 Koodo Reader 來試用看看，不曉得合不合手感。
- 官網：https://www.koodoreader.com/
- Git repo: https://github.com/koodo-reader/koodo-reader

## 2024-10-29

- 實驗環境：Github Codespace
```bash
jazzw@JazzBook:~$ gh cs code
? Choose codespace: jazzwang/snippet (master*): snippet
```
- 打開 VS Code 以後，開啟 Terminal，先用指令直接開啟 Docker 容器來試用看看。
```bash
@jazzwang ➜ /workspaces/snippet (master) $ docker run -d -p 80:80 --name koodo-reader ghcr.io/koodo-reader/koodo-reader:master
Unable to find image 'ghcr.io/koodo-reader/koodo-reader:master' locally
master: Pulling from koodo-reader/koodo-reader
43c4264eed91: Pull complete 
02040ba779ee: Pull complete 
c257707c9719: Pull complete 
06ce39c94b8d: Pull complete 
4f4fb700ef54: Pull complete 
c4e7cb918e73: Pull complete 
Digest: sha256:d87fbed39e224c71ec4eaf3221b73bfc9a22997802439752ba78a02c1e7b8c70
Status: Downloaded newer image for ghcr.io/koodo-reader/koodo-reader:master
b20070e024645c1cea6b47dc420bd0e28ef4f300bd94f1968a10dcfb504548fe
```
- 感謝 Github Cosespace 自動 port forward，開啟瀏覽器預覽(Open in Browser) http://127.0.0.1 就可以看到 Koodo Reader 的 Web UI 了。
- 界面還算乾淨舒服，第一步是點選右上角 Import 按鈕，選擇本地的 ePUB 檔案，上傳後就可以開始閱讀了。算是流暢的啟用體驗。
![](https://i.pinimg.com/originals/77/32/fe/7732fe5296fc3c449ff387cddf90a7af.gif)

- ( 2024-10-29 17:45:01 )
- 問題一：上傳的檔案在 Docker 的哪裡？
- 解答：All your data is stored locally in your <mark>**browser cache**</mark> -- 網頁版
```
@jazzwang ➜ /workspaces/snippet/md (master) $ docker ps
CONTAINER ID   IMAGE                                      COMMAND                  CREATED          STATUS          PORTS                                                           NAMES
b20070e02464   ghcr.io/koodo-reader/koodo-reader:master   "caddy run --config …"   50 minutes ago   Up 50 minutes   443/tcp, 0.0.0.0:80->80/tcp, :::80->80/tcp, 2019/tcp, 443/udp   koodo-reader
@jazzwang ➜ /workspaces/snippet (master) $ docker logs koodo-reader
{"level":"info","ts":1730192849.3041413,"msg":"using config from file","file":"/etc/caddy/Caddyfile"}
{"level":"info","ts":1730192849.3048954,"msg":"adapted config to JSON","adapter":"caddyfile"}
{"level":"info","ts":1730192849.3056831,"logger":"admin","msg":"admin endpoint started","address":"localhost:2019","enforce_origin":false,"origins":["//localhost:2019","//[::1]:2019","//127.0.0.1:2019"]}
{"level":"warn","ts":1730192849.305992,"logger":"http.auto_https","msg":"server is listening only on the HTTP port, so no automatic HTTPS will be applied to this server","server_name":"srv0","http_port":80}
{"level":"info","ts":1730192849.306088,"logger":"tls.cache.maintenance","msg":"started background certificate maintenance","cache":"0xc000163000"}
{"level":"info","ts":1730192849.3076398,"logger":"http.log","msg":"server running","name":"srv0","protocols":["h1","h2","h3"]}
{"level":"info","ts":1730192849.30795,"msg":"autosaved config (load with --resume flag)","file":"/config/caddy/autosave.json"}
{"level":"info","ts":1730192849.3079574,"msg":"serving initial configuration"}
{"level":"info","ts":1730192849.3198473,"logger":"tls","msg":"cleaning storage unit","storage":"FileStorage:/data/caddy"}
{"level":"info","ts":1730192849.320195,"logger":"tls","msg":"finished cleaning storage units"}
@jazzwang ➜ /workspaces/snippet (master) $ docker exec -it koodo-reader /bin/sh
/srv # cd /data/caddy/
/data/caddy # tree
.
├── instance.uuid
├── last_clean.json
└── locks

1 directories, 2 files
/data/caddy #
/data/caddy # cd /config/
/config # tree
.
└── caddy
    └── autosave.json

1 directories, 1 files
/config # cd
~ # pwd
/root
~ # ps ax
PID   USER     TIME  COMMAND
    1 root      0:00 caddy run --config /etc/caddy/Caddyfile --adapter caddyfile
   48 root      0:00 /bin/sh
   60 root      0:00 ps ax

~ # tree /etc/caddy/
/etc/caddy/
└── Caddyfile

0 directories, 1 files

~ # tree /usr/share/caddy/
/usr/share/caddy/
├── LICENSE
├── asset-manifest.json
├── assets
│   ├── empty.svg
│   ├── empty_light.svg
│   ├── icon.png
│   ├── label.png
│   ├── label_light.png
│   └── styles
│       ├── blue.css
│       ├── dark.css
│       ├── default.css
│       ├── green.css
│       ├── purple.css
│       └── red.css
├── favicon.png
├── index.html
├── lib
│   ├── 7z-wasm
│   │   ├── 7zz.umd.js
│   │   ├── 7zz.wasm
│   │   └── License.txt
│   ├── Dropbox
│   │   └── Dropbox-sdk.min.js
│   ├── Hammer
│   │   └── hammer.min.js
│   ├── JSZip
│   │   └── jszip.min.js
│   ├── Rangy
│   │   ├── rangy-classapplier.js
│   │   ├── rangy-core.js
│   │   ├── rangy-highlighter.js
│   │   ├── rangy-serializer.js
│   │   └── rangy-textrange.js
│   ├── chinese-s2t
│   │   └── chinese-s2t.js
│   ├── fflate
│   │   └── fflate.min.js
│   ├── filesaver
│   │   └── FileSaver.min.js
│   ├── js-untar
│   │   └── untar.js
│   ├── jschardet
│   │   ├── LICENSE.txt
│   │   └── jschardet.min.js
│   ├── kookit
│   │   └── kookit.min.js
│   ├── libunrar
│   │   ├── Promise.min.js
│   │   ├── libunrar.js
│   │   ├── libunrar.wasm
│   │   ├── rpc.js
│   │   └── worker.js
│   ├── localforage
│   │   └── localforage.min.js
│   ├── mammoth
│   │   └── mammoth.browser.min.js
│   ├── marked
│   │   └── marked.js
│   ├── mhtml2html
│   │   └── mhtml2html.js
│   ├── pdf
│   │   ├── build
│   │   │   ├── pdf.js
│   │   │   ├── pdf.js.map
│   │   │   ├── pdf.sandbox.js
│   │   │   ├── pdf.sandbox.js.map
│   │   │   ├── pdf.worker.js
│   │   │   └── pdf.worker.js.map
│   │   └── web
│   │       ├── cmaps
│   │       │   ├── 78-EUC-H.bcmap
│   │       │   ├── 78-EUC-V.bcmap
│   │       │   ├── 78-H.bcmap
│   │       │   ├── 78-RKSJ-H.bcmap
│   │       │   ├── 78-RKSJ-V.bcmap
│   │       │   ├── 78-V.bcmap
│   │       │   ├── 78ms-RKSJ-H.bcmap
│   │       │   ├── 78ms-RKSJ-V.bcmap
│   │       │   ├── 83pv-RKSJ-H.bcmap
│   │       │   ├── 90ms-RKSJ-H.bcmap
│   │       │   ├── 90ms-RKSJ-V.bcmap
│   │       │   ├── 90msp-RKSJ-H.bcmap
│   │       │   ├── 90msp-RKSJ-V.bcmap
│   │       │   ├── 90pv-RKSJ-H.bcmap
│   │       │   ├── 90pv-RKSJ-V.bcmap
│   │       │   ├── Add-H.bcmap
│   │       │   ├── Add-RKSJ-H.bcmap
│   │       │   ├── Add-RKSJ-V.bcmap
│   │       │   ├── Add-V.bcmap
│   │       │   ├── Adobe-CNS1-0.bcmap
│   │       │   ├── Adobe-CNS1-1.bcmap
│   │       │   ├── Adobe-CNS1-2.bcmap
│   │       │   ├── Adobe-CNS1-3.bcmap
│   │       │   ├── Adobe-CNS1-4.bcmap
│   │       │   ├── Adobe-CNS1-5.bcmap
│   │       │   ├── Adobe-CNS1-6.bcmap
│   │       │   ├── Adobe-CNS1-UCS2.bcmap
│   │       │   ├── Adobe-GB1-0.bcmap
│   │       │   ├── Adobe-GB1-1.bcmap
│   │       │   ├── Adobe-GB1-2.bcmap
│   │       │   ├── Adobe-GB1-3.bcmap
│   │       │   ├── Adobe-GB1-4.bcmap
│   │       │   ├── Adobe-GB1-5.bcmap
│   │       │   ├── Adobe-GB1-UCS2.bcmap
│   │       │   ├── Adobe-Japan1-0.bcmap
│   │       │   ├── Adobe-Japan1-1.bcmap
│   │       │   ├── Adobe-Japan1-2.bcmap
│   │       │   ├── Adobe-Japan1-3.bcmap
│   │       │   ├── Adobe-Japan1-4.bcmap
│   │       │   ├── Adobe-Japan1-5.bcmap
│   │       │   ├── Adobe-Japan1-6.bcmap
│   │       │   ├── Adobe-Japan1-UCS2.bcmap
│   │       │   ├── Adobe-Korea1-0.bcmap
│   │       │   ├── Adobe-Korea1-1.bcmap
│   │       │   ├── Adobe-Korea1-2.bcmap
│   │       │   ├── Adobe-Korea1-UCS2.bcmap
│   │       │   ├── B5-H.bcmap
│   │       │   ├── B5-V.bcmap
│   │       │   ├── B5pc-H.bcmap
│   │       │   ├── B5pc-V.bcmap
│   │       │   ├── CNS-EUC-H.bcmap
│   │       │   ├── CNS-EUC-V.bcmap
│   │       │   ├── CNS1-H.bcmap
│   │       │   ├── CNS1-V.bcmap
│   │       │   ├── CNS2-H.bcmap
│   │       │   ├── CNS2-V.bcmap
│   │       │   ├── ETHK-B5-H.bcmap
│   │       │   ├── ETHK-B5-V.bcmap
│   │       │   ├── ETen-B5-H.bcmap
│   │       │   ├── ETen-B5-V.bcmap
│   │       │   ├── ETenms-B5-H.bcmap
│   │       │   ├── ETenms-B5-V.bcmap
│   │       │   ├── EUC-H.bcmap
│   │       │   ├── EUC-V.bcmap
│   │       │   ├── Ext-H.bcmap
│   │       │   ├── Ext-RKSJ-H.bcmap
│   │       │   ├── Ext-RKSJ-V.bcmap
│   │       │   ├── Ext-V.bcmap
│   │       │   ├── GB-EUC-H.bcmap
│   │       │   ├── GB-EUC-V.bcmap
│   │       │   ├── GB-H.bcmap
│   │       │   ├── GB-V.bcmap
│   │       │   ├── GBK-EUC-H.bcmap
│   │       │   ├── GBK-EUC-V.bcmap
│   │       │   ├── GBK2K-H.bcmap
│   │       │   ├── GBK2K-V.bcmap
│   │       │   ├── GBKp-EUC-H.bcmap
│   │       │   ├── GBKp-EUC-V.bcmap
│   │       │   ├── GBT-EUC-H.bcmap
│   │       │   ├── GBT-EUC-V.bcmap
│   │       │   ├── GBT-H.bcmap
│   │       │   ├── GBT-V.bcmap
│   │       │   ├── GBTpc-EUC-H.bcmap
│   │       │   ├── GBTpc-EUC-V.bcmap
│   │       │   ├── GBpc-EUC-H.bcmap
│   │       │   ├── GBpc-EUC-V.bcmap
│   │       │   ├── H.bcmap
│   │       │   ├── HKdla-B5-H.bcmap
│   │       │   ├── HKdla-B5-V.bcmap
│   │       │   ├── HKdlb-B5-H.bcmap
│   │       │   ├── HKdlb-B5-V.bcmap
│   │       │   ├── HKgccs-B5-H.bcmap
│   │       │   ├── HKgccs-B5-V.bcmap
│   │       │   ├── HKm314-B5-H.bcmap
│   │       │   ├── HKm314-B5-V.bcmap
│   │       │   ├── HKm471-B5-H.bcmap
│   │       │   ├── HKm471-B5-V.bcmap
│   │       │   ├── HKscs-B5-H.bcmap
│   │       │   ├── HKscs-B5-V.bcmap
│   │       │   ├── Hankaku.bcmap
│   │       │   ├── Hiragana.bcmap
│   │       │   ├── KSC-EUC-H.bcmap
│   │       │   ├── KSC-EUC-V.bcmap
│   │       │   ├── KSC-H.bcmap
│   │       │   ├── KSC-Johab-H.bcmap
│   │       │   ├── KSC-Johab-V.bcmap
│   │       │   ├── KSC-V.bcmap
│   │       │   ├── KSCms-UHC-H.bcmap
│   │       │   ├── KSCms-UHC-HW-H.bcmap
│   │       │   ├── KSCms-UHC-HW-V.bcmap
│   │       │   ├── KSCms-UHC-V.bcmap
│   │       │   ├── KSCpc-EUC-H.bcmap
│   │       │   ├── KSCpc-EUC-V.bcmap
│   │       │   ├── Katakana.bcmap
│   │       │   ├── LICENSE
│   │       │   ├── NWP-H.bcmap
│   │       │   ├── NWP-V.bcmap
│   │       │   ├── RKSJ-H.bcmap
│   │       │   ├── RKSJ-V.bcmap
│   │       │   ├── Roman.bcmap
│   │       │   ├── UniCNS-UCS2-H.bcmap
│   │       │   ├── UniCNS-UCS2-V.bcmap
│   │       │   ├── UniCNS-UTF16-H.bcmap
│   │       │   ├── UniCNS-UTF16-V.bcmap
│   │       │   ├── UniCNS-UTF32-H.bcmap
│   │       │   ├── UniCNS-UTF32-V.bcmap
│   │       │   ├── UniCNS-UTF8-H.bcmap
│   │       │   ├── UniCNS-UTF8-V.bcmap
│   │       │   ├── UniGB-UCS2-H.bcmap
│   │       │   ├── UniGB-UCS2-V.bcmap
│   │       │   ├── UniGB-UTF16-H.bcmap
│   │       │   ├── UniGB-UTF16-V.bcmap
│   │       │   ├── UniGB-UTF32-H.bcmap
│   │       │   ├── UniGB-UTF32-V.bcmap
│   │       │   ├── UniGB-UTF8-H.bcmap
│   │       │   ├── UniGB-UTF8-V.bcmap
│   │       │   ├── UniJIS-UCS2-H.bcmap
│   │       │   ├── UniJIS-UCS2-HW-H.bcmap
│   │       │   ├── UniJIS-UCS2-HW-V.bcmap
│   │       │   ├── UniJIS-UCS2-V.bcmap
│   │       │   ├── UniJIS-UTF16-H.bcmap
│   │       │   ├── UniJIS-UTF16-V.bcmap
│   │       │   ├── UniJIS-UTF32-H.bcmap
│   │       │   ├── UniJIS-UTF32-V.bcmap
│   │       │   ├── UniJIS-UTF8-H.bcmap
│   │       │   ├── UniJIS-UTF8-V.bcmap
│   │       │   ├── UniJIS2004-UTF16-H.bcmap
│   │       │   ├── UniJIS2004-UTF16-V.bcmap
│   │       │   ├── UniJIS2004-UTF32-H.bcmap
│   │       │   ├── UniJIS2004-UTF32-V.bcmap
│   │       │   ├── UniJIS2004-UTF8-H.bcmap
│   │       │   ├── UniJIS2004-UTF8-V.bcmap
│   │       │   ├── UniJISPro-UCS2-HW-V.bcmap
│   │       │   ├── UniJISPro-UCS2-V.bcmap
│   │       │   ├── UniJISPro-UTF8-V.bcmap
│   │       │   ├── UniJISX0213-UTF32-H.bcmap
│   │       │   ├── UniJISX0213-UTF32-V.bcmap
│   │       │   ├── UniJISX02132004-UTF32-H.bcmap
│   │       │   ├── UniJISX02132004-UTF32-V.bcmap
│   │       │   ├── UniKS-UCS2-H.bcmap
│   │       │   ├── UniKS-UCS2-V.bcmap
│   │       │   ├── UniKS-UTF16-H.bcmap
│   │       │   ├── UniKS-UTF16-V.bcmap
│   │       │   ├── UniKS-UTF32-H.bcmap
│   │       │   ├── UniKS-UTF32-V.bcmap
│   │       │   ├── UniKS-UTF8-H.bcmap
│   │       │   ├── UniKS-UTF8-V.bcmap
│   │       │   ├── V.bcmap
│   │       │   └── WP-Symbol.bcmap
│   │       ├── debugger.js
│   │       ├── images
│   │       │   ├── annotation-check.svg
│   │       │   ├── annotation-comment.svg
│   │       │   ├── annotation-help.svg
│   │       │   ├── annotation-insert.svg
│   │       │   ├── annotation-key.svg
│   │       │   ├── annotation-newparagraph.svg
│   │       │   ├── annotation-noicon.svg
│   │       │   ├── annotation-note.svg
│   │       │   ├── annotation-paragraph.svg
│   │       │   ├── findbarButton-next.svg
│   │       │   ├── findbarButton-previous.svg
│   │       │   ├── grab.cur
│   │       │   ├── grabbing.cur
│   │       │   ├── loading-dark.svg
│   │       │   ├── loading-icon.gif
│   │       │   ├── loading.svg
│   │       │   ├── secondaryToolbarButton-documentProperties.svg
│   │       │   ├── secondaryToolbarButton-firstPage.svg
│   │       │   ├── secondaryToolbarButton-handTool.svg
│   │       │   ├── secondaryToolbarButton-lastPage.svg
│   │       │   ├── secondaryToolbarButton-rotateCcw.svg
│   │       │   ├── secondaryToolbarButton-rotateCw.svg
│   │       │   ├── secondaryToolbarButton-scrollHorizontal.svg
│   │       │   ├── secondaryToolbarButton-scrollVertical.svg
│   │       │   ├── secondaryToolbarButton-scrollWrapped.svg
│   │       │   ├── secondaryToolbarButton-selectTool.svg
│   │       │   ├── secondaryToolbarButton-spreadEven.svg
│   │       │   ├── secondaryToolbarButton-spreadNone.svg
│   │       │   ├── secondaryToolbarButton-spreadOdd.svg
│   │       │   ├── shadow.png
│   │       │   ├── toolbarButton-bookmark.svg
│   │       │   ├── toolbarButton-currentOutlineItem.svg
│   │       │   ├── toolbarButton-download.svg
│   │       │   ├── toolbarButton-menuArrow.svg
│   │       │   ├── toolbarButton-openFile.svg
│   │       │   ├── toolbarButton-pageDown.svg
│   │       │   ├── toolbarButton-pageUp.svg
│   │       │   ├── toolbarButton-presentationMode.svg
│   │       │   ├── toolbarButton-print.svg
│   │       │   ├── toolbarButton-search.svg
│   │       │   ├── toolbarButton-secondaryToolbarToggle.svg
│   │       │   ├── toolbarButton-sidebarToggle.svg
│   │       │   ├── toolbarButton-viewAttachments.svg
│   │       │   ├── toolbarButton-viewLayers.svg
│   │       │   ├── toolbarButton-viewOutline.svg
│   │       │   ├── toolbarButton-viewThumbnail.svg
│   │       │   ├── toolbarButton-zoomIn.svg
│   │       │   ├── toolbarButton-zoomOut.svg
│   │       │   ├── treeitem-collapsed.svg
│   │       │   └── treeitem-expanded.svg
│   │       ├── locale
│   │       │   ├── ach
│   │       │   │   └── viewer.properties
│   │       │   ├── af
│   │       │   │   └── viewer.properties
│   │       │   ├── an
│   │       │   │   └── viewer.properties
│   │       │   ├── ar
│   │       │   │   └── viewer.properties
│   │       │   ├── ast
│   │       │   │   └── viewer.properties
│   │       │   ├── az
│   │       │   │   └── viewer.properties
│   │       │   ├── be
│   │       │   │   └── viewer.properties
│   │       │   ├── bg
│   │       │   │   └── viewer.properties
│   │       │   ├── bn
│   │       │   │   └── viewer.properties
│   │       │   ├── bo
│   │       │   │   └── viewer.properties
│   │       │   ├── br
│   │       │   │   └── viewer.properties
│   │       │   ├── brx
│   │       │   │   └── viewer.properties
│   │       │   ├── bs
│   │       │   │   └── viewer.properties
│   │       │   ├── ca
│   │       │   │   └── viewer.properties
│   │       │   ├── cak
│   │       │   │   └── viewer.properties
│   │       │   ├── ckb
│   │       │   │   └── viewer.properties
│   │       │   ├── cs
│   │       │   │   └── viewer.properties
│   │       │   ├── cy
│   │       │   │   └── viewer.properties
│   │       │   ├── da
│   │       │   │   └── viewer.properties
│   │       │   ├── de
│   │       │   │   └── viewer.properties
│   │       │   ├── dsb
│   │       │   │   └── viewer.properties
│   │       │   ├── el
│   │       │   │   └── viewer.properties
│   │       │   ├── en-CA
│   │       │   │   └── viewer.properties
│   │       │   ├── en-GB
│   │       │   │   └── viewer.properties
│   │       │   ├── en-US
│   │       │   │   └── viewer.properties
│   │       │   ├── eo
│   │       │   │   └── viewer.properties
│   │       │   ├── es-AR
│   │       │   │   └── viewer.properties
│   │       │   ├── es-CL
│   │       │   │   └── viewer.properties
│   │       │   ├── es-ES
│   │       │   │   └── viewer.properties
│   │       │   ├── es-MX
│   │       │   │   └── viewer.properties
│   │       │   ├── et
│   │       │   │   └── viewer.properties
│   │       │   ├── eu
│   │       │   │   └── viewer.properties
│   │       │   ├── fa
│   │       │   │   └── viewer.properties
│   │       │   ├── ff
│   │       │   │   └── viewer.properties
│   │       │   ├── fi
│   │       │   │   └── viewer.properties
│   │       │   ├── fr
│   │       │   │   └── viewer.properties
│   │       │   ├── fy-NL
│   │       │   │   └── viewer.properties
│   │       │   ├── ga-IE
│   │       │   │   └── viewer.properties
│   │       │   ├── gd
│   │       │   │   └── viewer.properties
│   │       │   ├── gl
│   │       │   │   └── viewer.properties
│   │       │   ├── gn
│   │       │   │   └── viewer.properties
│   │       │   ├── gu-IN
│   │       │   │   └── viewer.properties
│   │       │   ├── he
│   │       │   │   └── viewer.properties
│   │       │   ├── hi-IN
│   │       │   │   └── viewer.properties
│   │       │   ├── hr
│   │       │   │   └── viewer.properties
│   │       │   ├── hsb
│   │       │   │   └── viewer.properties
│   │       │   ├── hu
│   │       │   │   └── viewer.properties
│   │       │   ├── hy-AM
│   │       │   │   └── viewer.properties
│   │       │   ├── hye
│   │       │   │   └── viewer.properties
│   │       │   ├── ia
│   │       │   │   └── viewer.properties
│   │       │   ├── id
│   │       │   │   └── viewer.properties
│   │       │   ├── is
│   │       │   │   └── viewer.properties
│   │       │   ├── it
│   │       │   │   └── viewer.properties
│   │       │   ├── ja
│   │       │   │   └── viewer.properties
│   │       │   ├── ka
│   │       │   │   └── viewer.properties
│   │       │   ├── kab
│   │       │   │   └── viewer.properties
│   │       │   ├── kk
│   │       │   │   └── viewer.properties
│   │       │   ├── km
│   │       │   │   └── viewer.properties
│   │       │   ├── kn
│   │       │   │   └── viewer.properties
│   │       │   ├── ko
│   │       │   │   └── viewer.properties
│   │       │   ├── lij
│   │       │   │   └── viewer.properties
│   │       │   ├── lo
│   │       │   │   └── viewer.properties
│   │       │   ├── locale.properties
│   │       │   ├── lt
│   │       │   │   └── viewer.properties
│   │       │   ├── ltg
│   │       │   │   └── viewer.properties
│   │       │   ├── lv
│   │       │   │   └── viewer.properties
│   │       │   ├── meh
│   │       │   │   └── viewer.properties
│   │       │   ├── mk
│   │       │   │   └── viewer.properties
│   │       │   ├── mr
│   │       │   │   └── viewer.properties
│   │       │   ├── ms
│   │       │   │   └── viewer.properties
│   │       │   ├── my
│   │       │   │   └── viewer.properties
│   │       │   ├── nb-NO
│   │       │   │   └── viewer.properties
│   │       │   ├── ne-NP
│   │       │   │   └── viewer.properties
│   │       │   ├── nl
│   │       │   │   └── viewer.properties
│   │       │   ├── nn-NO
│   │       │   │   └── viewer.properties
│   │       │   ├── oc
│   │       │   │   └── viewer.properties
│   │       │   ├── pa-IN
│   │       │   │   └── viewer.properties
│   │       │   ├── pl
│   │       │   │   └── viewer.properties
│   │       │   ├── pt-BR
│   │       │   │   └── viewer.properties
│   │       │   ├── pt-PT
│   │       │   │   └── viewer.properties
│   │       │   ├── rm
│   │       │   │   └── viewer.properties
│   │       │   ├── ro
│   │       │   │   └── viewer.properties
│   │       │   ├── ru
│   │       │   │   └── viewer.properties
│   │       │   ├── scn
│   │       │   │   └── viewer.properties
│   │       │   ├── si
│   │       │   │   └── viewer.properties
│   │       │   ├── sk
│   │       │   │   └── viewer.properties
│   │       │   ├── sl
│   │       │   │   └── viewer.properties
│   │       │   ├── son
│   │       │   │   └── viewer.properties
│   │       │   ├── sq
│   │       │   │   └── viewer.properties
│   │       │   ├── sr
│   │       │   │   └── viewer.properties
│   │       │   ├── sv-SE
│   │       │   │   └── viewer.properties
│   │       │   ├── szl
│   │       │   │   └── viewer.properties
│   │       │   ├── ta
│   │       │   │   └── viewer.properties
│   │       │   ├── te
│   │       │   │   └── viewer.properties
│   │       │   ├── th
│   │       │   │   └── viewer.properties
│   │       │   ├── tl
│   │       │   │   └── viewer.properties
│   │       │   ├── tr
│   │       │   │   └── viewer.properties
│   │       │   ├── trs
│   │       │   │   └── viewer.properties
│   │       │   ├── uk
│   │       │   │   └── viewer.properties
│   │       │   ├── ur
│   │       │   │   └── viewer.properties
│   │       │   ├── uz
│   │       │   │   └── viewer.properties
│   │       │   ├── vi
│   │       │   │   └── viewer.properties
│   │       │   ├── wo
│   │       │   │   └── viewer.properties
│   │       │   ├── xh
│   │       │   │   └── viewer.properties
│   │       │   ├── zh-CN
│   │       │   │   └── viewer.properties
│   │       │   └── zh-TW
│   │       │       └── viewer.properties
│   │       ├── localforage.min.js
│   │       ├── viewer.css
│   │       ├── viewer.html
│   │       ├── viewer.js
│   │       └── viewer.js.map
│   ├── underscore
│   │   └── underscore-umd-min.js
│   └── zipjs
│       └── zip-no-worker.min.js
├── robots.txt
└── static
    ├── css
    │   ├── main.dddaf293.css
    │   └── main.dddaf293.css.map
    ├── js
    │   ├── main.2c093079.js
    │   ├── main.2c093079.js.LICENSE.txt
    │   └── main.2c093079.js.map
    └── media
        ├── icomoon.0f33e89b836ceae52797.woff
        ├── icomoon.a27c49e25e3b160b9077.svg
        ├── icomoon.b543d9cdaf8d6ebdd255.ttf
        └── icomoon.db7937fbbfec5af306fb.eot

136 directories, 391 files
```
- 從 [Dockerfile](https://github.com/koodo-reader/koodo-reader/blob/master/Dockerfile) 知道 node.js build 好的結果放在 `/usr/share/caddy`
- 在 Docker 容器內遍尋不到上傳的檔案，所以懷疑存在本機。（也合理，不然怎麼 import ePUB 時，速度飛快）
- 文件內有說：
> Web Version: All your data is stored locally in your browser cache. Other than you, nobody can access these data. when you visit web version on a different computer or browser, you need to reimport your book in order to read it. 