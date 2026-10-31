# AI Detector

- 緣起：
  - 原本是看到 https://huggingface.co/jialinyyzz/humanizer 這個模型的討論區提到了幾個偵測 AI 生成文章的服務
  - 後來有看到 Google DeepMind 公佈了
- 工具列表：
  - Turnitin
    - https://www.turnitin.tw/
  - Originality
    - https://app.originality.ai/home/scan
    - 實測結果：
      - 拿我自己 2022 年以前發表的文章（e.g. 科技大觀園 - 或 網管人 - 淺談雲端運算）去測，就 90% 以上認定是人寫的。
      - 但拿 2026 LinkedIn 亂找的貼文，卻很高的比例是 GenAI 生成的。
  - GPTZero
    - https://gptzero.me/ (算是老牌了，不過早期測試時發現只能偵測 OpenAI GPT 的文字，其他 Gemini 生的通通偵測不出來）
  - Pangram - 這個最強，Humanizer 的作者說多數都通過不了 Pangram 的掃描
    - https://www.pangram.com/
