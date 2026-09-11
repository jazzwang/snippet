# 2026-04-13

- 掃描 QR Code 連到該年級的閩南語網頁，使用 Gmail 登入，並且輸入產品序號
- 開啟 Chrome DevTool，選 Media，然後按 CTRL+R 重新載入頁面
- 逐一點擊每一個連結
- 下載成 HAR 檔案
- 使用 `jq` 生成
```bash
cat 閩南語_6.har | jq -c '.log.entries[].request.url' | sort -n | uniq > 閩南語_6.list
```

# 2026-09-12

- 必須切換到 WSL2 的 bash 環境才有辦法正常產生 UTF-8 檔名的輸出
```bash
~/git/snippet/py/requests/jen-pin$ cat ~/Downloads/2026-09-12_閩南語_9.har | jq -c '.log.entries[].request.url' | grep "storage" | sort -n | uniq | tr -d '"' | tee 閩南語_9.list
~/git/snippet/py/requests/jen-pin$ wsl
/mnt/c/Users/jazzw/git/snippet/py/requests/jen-pin$ for i in $(cat 閩南語_9.list ); do wget $i; done
```
