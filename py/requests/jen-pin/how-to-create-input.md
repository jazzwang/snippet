# 2026-04-13

- 掃描 QR Code 連到該年級的閩南語網頁，使用 Gmail 登入，並且輸入產品序號
- 開啟 Chrome DevTool，選 Media，然後按 CTRL+R 重新載入頁面
- 逐一點擊每一個連結
- 下載成 HAR 檔案
- 使用 `jq` 生成
```bash
cat 閩南語_6.har | jq -c '.log.entries[].request.url' | sort -n | uniq > 閩南語_6.list
```
