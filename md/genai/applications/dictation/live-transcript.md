# Audio (Speech) to Text (Transcript) Live

- 緣起：
  - 工作上越來越多線上會議，但是有些場合又不合適按錄影，透過 MS Teams 錄影的方式來產生 Transcript。
- 思路：
  - 有沒有辦法開「分身」，將瀏覽器的 audio output 導入成某個應用程式的 audio input 然後做即時轉譯呢？
- 實作：
  - 目前看到的多半都是離線轉譯，也就是上傳影片或錄音來產生翻譯字幕檔。且很多是基於 Whisper 模型。
  - 初步找到一個 Client-Server 架構的實作，有瀏覽器擴充套件的實作，可以把語音「近即時」轉成文字檔案。
    - https://github.com/collabora/WhisperLive?tab=readme-ov-file#browser-extensions
  - 不過暫時還沒找到時間可以測試合不合用。