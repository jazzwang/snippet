# crawl4ai

> 

- Git Repo:
  - https://github.com/unclecode/crawl4ai

## 2025-01-16

- 在 [Turn ANY Website into LLM Knowledge in SECONDS | 在幾秒鐘內將任何網站轉變為 LLM 知識](https://www.youtube.com/watch?v=JWfNLF_g_V0) 看到 `crawl4ai`
  - 範例程式：
    - https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent/crawl4AI-examples
    - 影片中的完整 Crawl4AI-agent 原始碼則在[上一層目錄](https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent/)
- 看了一下 crawl4ai 專案的 [requirements.txt](https://github.com/unclecode/crawl4ai/blob/main/requirements.txt) 觀察相依性，也做一個初步的逆向架構理解，紀錄一下幾個已知跟沒看過的專案。
  - litellm - 呼應 AI 的部份，用來串接不同的 LLM
  - playwright - 呼應 crawl 的部份，可以開不同的瀏覽器在背景(Headless Mode)來爬取資料
  - [tf-playwright-stealth](https://github.com/tinyfish-io/tf-playwright-stealth) - 讓 playwright 可以偽裝，避免爬蟲被偵測到而被擋掉。
  - [pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library
  - [snowballstemmer](https://pypi.org/project/snowballstemmer/) - 看起來是為了一些加速的目的（#TODO 待研究）