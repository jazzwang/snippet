# YouTube Music

## 2026-01-02

- 因為有訂閱 YouTube 所以平常比較常用 YouTube Music 來聽一些背景音樂。以前也會用 Google Podcast 訂閱一些 Podcast，可惜後來終止服務，並且併入 YouTube Music，所以一些 Podcast 就得到 Apple Podcast 或 Spotify 才能找得到。
- 印象前陣子有看到「AI 懶人報」的一個 Podcast，可是在 YouTube Music 的 Podcast 找不到。所以找了一下怎麼取得 Podcast RSS 然後新增到 YouTube Music
  - 「AI 懶人報」 - https://linktr.ee/ailanrenbao
    - Apple Podcast 頻道 https://podcasts.apple.com/tw/podcast/ai%E6%87%B6%E4%BA%BA%E5%A0%B1/id1817340034
  - https://www.facebook.com/groups/gaitech/posts/1426174611900083/
  - 印象這個作者是用 `n8n` 串了一堆流程來自動生成 podcast （好一個被動收入）
    - 概念：『社群網路內容<mark>**再利用**</mark>』
  - 其次，這次再聽，因為被置入了「語音廣告」，所以知道作者改用「VoAI 絕好聲創」
- 參考：
  - https://podnews.net/article/youtube-music-rss 提到了手動新增 Podcast RSS 到 YouTube Music 的方法
  > 不難，就是需要 (1) Podcast RSS URL (2) 把網址轉成 base64 格式
  > https://music.youtube.com/library/podcasts?addrssfeed=(a base64URL of the full RSS feed address)
  - 為了查 Apple Podcast 的 RSS，先看了這篇 https://www.geeksforgeeks.org/techtips/how-to-get-rss-feed-from-apple-podcasts/
  - 可惜好不容易登入 Apple 帳號（有陣子沒用了，沒 masOS 裝置在手邊，居然要繞兩圈驗證才能登入），仍找不到 RSS 的按鈕
  - 後來看到這篇 Threads 討論 https://www.threads.com/@janetkuo/post/DAK5-GtR-Th
  > [janetkuo](https://www.threads.com/@janetkuo) - [09/21/24](https://www.threads.com/@janetkuo/post/DAK5-GtR-Th)
  > 搜不到的 podcasts 還是可以透過 RSS feed 訂閱（步驟見圖片），這個 podcast 的 RSS 連結是 [feeds.soundon.fm/podca...](https://feeds.soundon.fm/podcasts/b3778f90-f749-4310-8054-35efac5c9380.xml)RSS feed 連結可以在 [getrssfeed.com](https://getrssfeed.com/) 輸入 podcast 網址得到順便分享一下創作者直接在 SoundOn 發佈到 YouTube Music 的步驟 [support.soundon.fm/zh-TW...](https://support.soundon.fm/zh-TW/articles/8644252-%E5%A6%82%E4%BD%95%E5%B0%87-podcast-%E7%99%BC%E4%BD%88%E5%88%B0-youtube-music)
  - 其實如果上架 SoundOn 平台的，只需要把頻道的 UUID 換貼到 feed 網址即可
    - SoundOn 頻道:
      - https://player.soundon.fm/p/<mark>ca974d36-6fcc-46fc-a339-ba7ed8902c80</mark>
    - RSS feed:
      - https://feeds.soundon.fm/podcasts/<mark>ca974d36-6fcc-46fc-a339-ba7ed8902c80</mark>.xml
  - 該 Thread 討論也提到 https://getrssfeed.com/ 可以把 Apple Podcast 頻道取出 RSS Feed
  - 後來逆向看 Apple Podcast 原始碼，搜尋 `"feedUrl":` 第一個結果就是了 `*^_^*`
  ```bash
  ~/git/snippet$ cat ~/bin/apple-podcast-rss
  #!/bin/bash
  url=$1
  curl -s "$url" | grep '"feedUrl":'  | sed 's#.*"feedUrl":##' | sed 's#,.*##'
  ```
