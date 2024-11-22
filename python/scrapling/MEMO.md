# Scrapling

- https://github.com/D4Vinci/Scrapling

> Undetectable, Lightning-Fast, and Adaptive Web Scraping for Python

## 2024-11-22

- 緣起：
  - 在 LinkedIn 看到 [分享](https://www.linkedin.com/posts/largitdata_iwvjfcnbtoim-iwvjfciiqiro-hxeiunjkajlb-activity-7261743534448230400-MjBt/) - [Link](https://www.linkedin.com/feed/update/urn:li:activity:7261743534448230400)
  - 從 README 看起來，我平常慣用的 `BS4 + Lxml` 相對還是比較慢，可以研究看看～
- 其他有趣的點：
  - 使用了 https://github.com/daijro/camoufox 這個 anti-bot browser 來繞過這種追蹤，加快 Webscraping 的爬蟲速度。
  - 如果網頁格式有變化，也會用**相似度**去找元件。

### 官方測試數據：Text Extraction Speed Test (5000 nested elements).

| # |      Library      | Time (ms) | vs Scrapling | 
|---|:-----------------:|:---------:|:------------:|
| 1 |     Scrapling     |   5.44    |     1.0x     |
| 2 |   Parsel/Scrapy   |   5.53    |    1.017x    |
| 3 |     Raw Lxml      |   6.76    |    1.243x    |
| 4 |      PyQuery      |   21.96   |    4.037x    |
| 5 |    Selectolax     |   67.12   |   12.338x    |
| 6 |   BS4 with Lxml   |  1307.03  |   240.263x   |
| 7 |  MechanicalSoup   |  1322.64  |   243.132x   |
| 8 | BS4 with html5lib |  3373.75  |   620.175x   |

As you see, Scrapling is on par with Scrapy and slightly faster than Lxml which both libraries are built on top of