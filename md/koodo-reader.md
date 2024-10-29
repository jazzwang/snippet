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
- 感謝 Github Cosespace 自動 port forward，開啟瀏覽器預覽 http://127.0.0.1 就可以看到 Koodo Reader 的 Web UI 了。
- 界面還算乾淨舒服，第一步是點選右上角 Import 按鈕，選擇本地的 ePUB 檔案，上傳後就可以開始閱讀了。算是流暢的啟用體驗。
![](https://i.pinimg.com/originals/77/32/fe/7732fe5296fc3c449ff387cddf90a7af.gif)