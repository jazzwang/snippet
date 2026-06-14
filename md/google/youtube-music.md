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
  > 搜不到的 podcasts 還是可以透過 RSS feed 訂閱（步驟見圖片），這個 podcast 的 RSS 連結是 [feeds.soundon.fm/podcast...](https://feeds.soundon.fm/podcasts/b3778f90-f749-4310-8054-35efac5c9380.xml)RSS feed 連結可以在 [getrssfeed.com](https://getrssfeed.com/) 輸入 podcast 網址得到順便分享一下創作者直接在 SoundOn 發佈到 YouTube Music 的步驟 [support.soundon.fm/zh-TW...](https://support.soundon.fm/zh-TW/articles/8644252-%E5%A6%82%E4%BD%95%E5%B0%87-podcast-%E7%99%BC%E4%BD%88%E5%88%B0-youtube-music)
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

## 2026-06-14

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
為什麼 YouTube Music 網頁版會把播放紀錄同步到 YouTube，而 YouTube Music Mobile App 卻不會？
</td></tr><tr><td>A:</td><td>

### YouTube Music - 歷史紀錄 - 網頁版與行動版行為不同

這是因為 YouTube Music 網頁版與 YouTube 本質上共享同一個瀏覽器架構與帳號快取，而行動 App 版則是完全獨立運作的應用程式。
雖然 YouTube 和 YouTube Music 屬於同一個 Google 帳號，但網頁版和手機 App 在系統底層的資料回傳與同步邏輯有很大的差異，主要原因包含以下幾點：

#### 1. 網頁版與 YouTube 共享「同一個 Cookie 緩存」

當你在電腦上打開 YouTube Music 網頁版（youtube.com）時，它與標準的 YouTube 網站共享同一個網域的 Cookie、快取以及瀏覽器 Session。

-   網頁版播放音樂時，瀏覽器會直接呼叫 YouTube 的核心 API。
-   系統常常會將網頁版的點擊與播放行為，直接判定為同一瀏覽器環境下的「影片觀看」，導致播放紀錄即時同步到你的 YouTube 觀看歷史中。

#### 2. 行動 App 擁有「完全獨立的資料通道」

手機上的 YouTube Music App 和 YouTube App 是兩個完全分離的獨立應用程式（沙盒機制）。

-   手機 App 在設計時，Google 為了避免音樂紀錄污染使用者的影片觀看推薦，針對 App 端的 API 進行了嚴格的資料分流。
-   你在手機 Music App 聽歌時，播放紀錄會被單獨歸類在「音樂歷史」中，並不會主動推播給 YouTube App 的主要觀賞歷史。

#### 3. 「純音訊」與「影片」的判定差異

-   網頁版預設整合： 網頁版即便切換到「純音訊」模式，底層運作依然與 YouTube 影片播放器的網頁框架綁定，容易觸發觀看歷史紀錄。
-   App 版深度優化： 手機 App 在背景播放或純音訊模式下，系統會啟用專門的串流音訊協定，這與 YouTube App 的影片串流完全分家。

#### 如何解決網頁版污染 YouTube 紀錄的問題？

如果你不希望電腦聽歌影響到 YouTube 影片的推薦演算法，可以嘗試以下方法：

-   使用獨立的「品牌帳戶」： 在 YouTube 設定中建立一個專門聽歌的品牌帳戶，將音樂與日常看影片的帳戶分開。
-   暫停觀看紀錄： 聽歌前，前往 Google 活動控制項 暫停 YouTube 的觀看歷史紀錄，但這會導致你暫時無法儲存任何看過影片的進度。
-   安裝 PWA 應用程式： 將 YouTube Music 網頁版「安裝為桌面應用程式 (PWA)」，有時能減少部分與標準網頁瀏覽器的紀錄重疊（視瀏覽器核心而定）。 [1]

如果需要進一步檢查你的帳戶歷史紀錄同步狀態，可以前往 YouTube 說明中心 查詢官方對於觀看紀錄管理的詳細說明。
你目前遇到這個問題，是主要覺得 YouTube 的首頁推薦被音樂打亂，還是單純不喜歡 歷史紀錄看起來很雜亂 呢？

[1] [https://www.reddit.com](https://www.reddit.com/r/YoutubeMusic/comments/1ptav16/is_there_a_way_to_have_yt_music_playlists/?tl=zh-hans)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
單純不喜歡 歷史紀錄看起來很雜亂
</td></tr><tr><td>A:</td><td>

### YouTube Music 如何簡化歷史紀錄

如果你只是單純不喜歡歷史紀錄看起來很雜亂，你可以透過以下幾個簡單的設定，把音樂紀錄從 YouTube 的歷史紀錄中徹底隱藏或清除：

#### 1. 善用 YouTube 歷史紀錄的「篩選器」

其實 YouTube 網頁版和 App 都有內建分類功能，你可以選擇只看「影片」紀錄：

-   網頁版： 點進「歷史紀錄」頁面後，右側通常會有類別篩選（例如：影片、社群貼文）。點選「影片」，就能把 YouTube Music 產生的音樂紀錄暫時濾掉。

#### 2. 前往「我的 Google 活動」批量刪除

如果你想把已經產生的音樂紀錄刪掉，直接在 YouTube 刪除會很沒效率，建議到後台一鍵清理：

-   操作步驟：

        1.  打開瀏覽器前往 Google 我的活動 (My Activity)。
        2.  點選「依日期與產品篩選」。
        3.  在產品列表中，勾選「YouTube Music」（不要勾選 YouTube）。
        4.  點選搜尋後，系統會列出「只有」在 YouTube Music 產生的紀錄。
        5.  點選右上角的「刪除」，即可一次清空所有聽歌紀錄，還你乾淨的 YouTube 影片歷史。

#### 3. 使用瀏覽器「無痕模式」聽歌

如果你習慣用電腦邊工作邊聽歌，又不想留下任何痕跡：

-   在電腦上開啟無痕視窗 (Incognito Window)。
-   登入 YouTube Music 網頁版聽歌。
-   *優點：* 關閉視窗後，剛剛聽的所有歌都不會被寫進你的 Google 歷史紀錄中。

如果想徹底根治這個問題，最推薦的方法還是建立一個「品牌帳戶」，把看影片和聽音樂的身份完全切開。
你需要我提供 如何建立 YouTube 品牌帳戶並轉移音樂設定 的詳細步驟教學嗎？

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>

### YouTube 品牌帳號

只要你用「同一個 Google 帳號（Email）」來建立品牌帳戶，新建立的品牌帳戶就能無縫共享你原本訂閱的 YouTube Premium 福利，完全不需要額外付費。 [1, 2]
YouTube Premium 的會員資格是綁定在整個 Google 帳號上，而不是單一頻道。因此，在同一個帳號下切換成品牌帳戶聽歌，依然能享有免廣告、背景播放與下載功能。 [1, 2, 3]
請依照以下 3 個步驟，建立你的專屬音樂/影片獨立頻道：

#### 步驟一：建立全新的品牌帳戶頻道 [4]

1.  使用電腦瀏覽器打開並登入你的 Premium 帳號，前往 YouTube 頻道列表。
2.  點選「建立新頻道」。
3.  輸入新頻道的名稱（例如：「我的音樂專區」或「乾淨看片用」），勾選同意條款後點選「建立」。 [5, 6]

#### 步驟二：在 YouTube 與 YouTube Music 之間切換

全新頻道建立完成後，你在同一個 Google 帳號下就會同時擁有「個人原始頻道」與「新品牌頻道」。 [1]

-   聽歌時（網頁版）： 打開 YouTube Music 網頁版，點擊右上角大頭貼 → 點選「切換帳戶」，選擇你剛剛建立的新品牌頻道。
-   看影片時（網頁/App）： 打開 YouTube，同樣點擊大頭貼 → 「切換帳戶」，維持在你原本的個人原始頻道。 [1]

#### 步驟三：享受「紀錄分家」的乾淨體驗

透過這個設定，你的看片與聽歌紀錄會完全分流：

-   網頁版 YouTube Music 的播放紀錄只會同步到「新品牌頻道」的歷史中。
-   你日常使用的「個人原始頻道」歷史紀錄將變得非常乾淨，首頁的影片推薦也再也不會被音樂給打亂。

#### ⚠️ 重要注意事項：

-   請勿將主要頻道「轉移」過去： 請單純「建立新頻道」並透過「切換帳戶」來使用即可。千萬不要點選進階設定中的「將頻道轉移至品牌帳戶」，這會導致你舊頻道的訂閱與觀看紀錄被覆蓋或刪除。 [1, 5, 7]
-   必須是主要擁有者： Premium 福利只會跟隨購買方案的「帳號擁有者」。如果你把這個品牌帳戶的「管理員權限」分享給別人的 Google 帳號，對方的帳號是無法平白共享你的 Premium 的。 [2]

你在建立新頻道或是切換帳戶的過程中，有遇到任何簡訊驗證或是介面找不到按鈕的問題嗎？ [8]
[1] [https://support.google.com](https://support.google.com/youtube/answer/3046356?hl=zh-Hant&co=GENIE.Platform%3DDesktop)
[2] [https://support.google.com](https://support.google.com/youtube/answer/6312076?hl=zh-Hant)
[3] [https://www.hk01.com](https://www.hk01.com/%E6%95%B8%E7%A2%BC%E7%94%9F%E6%B4%BB/1067145/youtube-premium-lite%E6%8E%A8%E5%B9%B3%E5%83%B9%E7%89%88%E6%9C%88%E8%B2%BB%E5%8D%8A%E5%83%B9-%E5%85%8D%E5%BB%A3%E5%91%8A%E4%BD%86%E5%B0%91%E4%B8%89%E9%A0%85%E9%87%8D%E9%BB%9E%E5%8A%9F%E8%83%BD)
[4] [https://support.google.com](https://support.google.com/youtube/answer/3056283?hl=zh-Hant)
[5] [https://monkeyjhong.pixnet.net](https://monkeyjhong.pixnet.net/blog/posts/17311873138)
[6] [https://www.soft4fun.net](https://www.soft4fun.net/social-networks/google-plus-sns/%E6%95%99%E5%AD%B8-%E5%BB%BA%E7%AB%8B%E5%93%81%E7%89%8C%E5%B0%88%E5%B1%AC%E7%9A%84-google-%E9%A0%81%E9%9D%A2%EF%BC%88%E7%94%A2%E5%93%81%E6%88%96%E5%93%81%E7%89%8C%EF%BC%89.htm)
[7] [https://support.google.com](https://support.google.com/youtube/answer/3056283?hl=zh-Hant)
[8] [https://www.scu.edu](https://www.scu.edu/training/resources/youtubebrandaccounts/)

</td></tr>
</table>
