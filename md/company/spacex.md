# SpaceX

## 2026-06-15

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
SpaceX 在太空建立資料中心,從物理熱力學的角度,在近乎真空的太空中 GPU 真的可以靠輻射散熱嗎?
</td></tr><tr><td>A:</td><td>

## SpaceX 太空資料中心 - 散熱設計

是的，在太空中 GPU 絕對可以、也只能完全依靠「熱輻射」來將熱能最終排入宇宙。然而，雖然這在物理熱力學上完全可行，但它的散熱效率極低，是阻礙太空資料中心規模化的最大物理瓶頸。 [1, 2, 3, 4]
許多人誤以為「太空很冷（約 -270°C）」所以晶片很好降溫，但從物理熱力學的角度來看，太空的真相與解決方案如下： [2, 5]

### 一、 太空散熱的物理困境：保溫瓶效應 [6]

在地球上，資料中心主要依靠對流（Convection），透過風扇吹動空氣（風冷）或泵浦循環水流（液冷）來帶走晶片熱量。 [1, 7, 8]

-   真空無對流：太空中幾乎沒有空氣分子。這意味著微型風扇在太空中毫無作用，熱能無法透過空氣對流傳導。
-   保溫瓶效應：真空是世界上最好的絕熱體（這也是保溫瓶的原理）。GPU 產生的熱能會被「困」在衛星內部，如果不做主動熱管理，晶片會在幾分鐘內因積熱而燒毀。 [1, 7, 9, 10, 11]

### 二、 決定散熱效率的物理公式

根據熱力學的史蒂芬-波茲曼定律（Stefan-Boltzmann law），一個物體透過輻射散發的熱功率（$P$）公式為： [12, 13] 

$P = \epsilon \cdot \sigma \cdot A \cdot T^4$

* $\epsilon$：表面輻射率（介於 0 到 1 之間）。
* $\sigma$：史蒂芬-波茲曼常數（固定值）。
* $A$：輻射板的表面積。
* $T$：輻射板的絕對溫度（Kelvin）。 [3, 12, 14, 15] 

#### 關鍵致命點：$T^4$ 的限制

從公式可以看出，輻射散熱的效率與溫度的「四次方」成正比。想要散熱快，輻射板就必須非常熱。

然而，GPU 的晶片耐溫是有物理極限的（通常在 80°C - 100°C 左右）。根據熱力學第二定律，熱量只能自發地從高溫傳導到低溫，這意味著衛星外側的散熱板溫度不可能高於 GPU 晶片本身的溫度。 [12, 13, 14, 15]

在 80°C（約 353 K）的限制下，每平方公尺的雙面輻射板在理想狀態下只能排掉大約 850W 到 1400W 的熱量。這與地球上透過風冷或水冷每平方公尺輕鬆帶走數萬瓦（kW）的效率相比，完全不在同一個量級。 [11, 13]

### 三、 SpaceX 實際採用的三層散熱架構

為了克服這個物理壁壘，SpaceX 最近公開的 AI1 資料中心衛星（功耗達 120kW-150kW，相當於一個 NVIDIA GB300 機櫃）採用了極致的熱管理架構： [16, 17]

```txt
[ GPU 晶片熱點 ] ──(物理傳導：金剛石)──> [ 內部封閉液冷迴路 ] 
──(熱管輸送)──> [ 衛星外部巨型輻射板 ] ──(紅外線輻射)──> 宇宙深空
```

1.  **晶片端：超高導熱材料（Thermal Conduction）**
    太空中銅和鋁的導熱速度跟不上高密度 GPU 的發熱。SpaceX 與航太供應鏈引入了 CVD 人造金剛石熱沉片。金剛石的導熱率是銅的 5 倍，能在一瞬間將 GPU 核心的極端熱點（Hotspot）均勻攤開導出。 [11]
2.  **中間層：封閉式液冷迴路（Closed-Loop Liquid Cooling）**
    衛星內部並非完全真空，GPU 被封閉在充滿特殊航太冷卻液（如氨水或氟化液，非水）的機箱中。透過機械泵浦或兩相流熱管（Heat Pipes），將冷卻液循環動起來，把熱量從晶片端快速「運送」到外殼。 [3, 16, 18, 19, 20]
3.  **最外層：巨型雙面不對稱輻射板（Radiator）**
    這是黃仁勳曾公開指出「太空散熱板必須做得很巨大」的原因。SpaceX AI1 衛星的展翼寬度達 70 公尺（相當於一架波音 747），其中很大一部分就是部署式的液冷散熱板（Liquid Radiator）。
    -   刀鋒對日（Knife-edge to the sun）：散熱板的側面會永遠對準太陽，避免吸收太陽輻射（1361 W/m²），而大面積的雙面則對準極冷（2.7K）的黑體宇宙深空，將熱能以紅外線形式全力輻射出去。 [3, 13, 16, 21, 22, 23]

### 總結

在太空中，GPU 的確可以靠輻射散熱，物理原理完全支援。但代價是，你在地球上只需要幾顆風扇或一個冷卻水塔解決的事，在太空中需要製造一片網球場大小的航太級巨型輻射板、使用昂貴的金剛石材料，並用火箭將幾噸重的散熱機構送上天。這是一場將「地球上的電費與水費」，轉化為「太空中的發射重量與材料成本」的豪賭。 [2, 3, 4, 7, 11, 24, 25]

SpaceX 預計最快在 2027 年底開始進行這類 AI 運算衛星的試飛演示。如果你對這個領域感興趣，我們可以進一步探討： [26]

-   宇宙射線（Radiation）對太空 GPU 造成的「單電位翻轉（SEU）」錯誤，SpaceX 該如何硬體屏蔽？
-   衛星在軌道上每 90 分鐘經歷一次 ±120°C 的極端溫差熱應力，材料如何防裂？ [4, 11, 27, 28]

[1] [https://abmedia.io](https://abmedia.io/space-compunting-cluster)
[2] [https://www.eet-china.com](https://www.eet-china.com/mp/a472883.html)
[3] [https://www.spacewar.com](https://www.spacewar.com/reports/The_Shadow_Side_The_Thermal_Claim_That_Makes_The_Data_Center_Story_Sound_True_999.html)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=zHJ8PDbCkrI)
[5] [https://www.asiae.co.kr](https://www.asiae.co.kr/en/article/2026020315230879390)
[6] [https://www.cmoney.tw](https://www.cmoney.tw/forum/article/176625643)
[7] [https://www.cmoney.tw](https://www.cmoney.tw/forum/article/179859864)
[8] [https://www.cmoney.tw](https://www.cmoney.tw/forum/article/176625643)
[9] [https://aspeniaonline.it](https://aspeniaonline.it/data-centers-in-space-an-astrophysicists-look-at-a-new-infrastructure-frontier/)
[10] [https://www.reddit.com](https://www.reddit.com/r/Futurology/comments/1qureug/im_not_convinced_that_we_can_build_datacenters_in/?tl=zh-hant)
[11] [https://caifuhao.eastmoney.com](https://caifuhao.eastmoney.com/news/20260610071919119342890)
[12] [https://www.youtube.com](https://www.youtube.com/watch?v=FlQYU3m1e80&t=4)
[13] [https://blog.spacecomputer.io](https://blog.spacecomputer.io/cooling-for-orbital-compute/)
[14] [https://www.youtube.com](https://www.youtube.com/watch?v=U9r2lerk164&t=2)
[15] [https://www.weforum.org](https://www.weforum.org/stories/2026/06/space-data-centres-cooling/)
[16] [https://finance.yahoo.com](https://finance.yahoo.com/sectors/technology/article/spacex-reveals-its-first-orbital-data-center-much-simpler-than-a-starlink-satellite-musk-says-141110185.html)
[17] [https://techorange.com](https://techorange.com/2026/06/09/spacex-data-centers-in-space/)
[18] [https://spectrum.ieee.org](https://spectrum.ieee.org/orbital-inference-data-center)
[19] [https://www.pcmag.com](https://www.pcmag.com/news/spacexs-orbiting-data-centers-will-use-liquid-cooling-but-dont-expect-water)
[20] [https://www.sciopen.com](https://www.sciopen.com/article/10.12465/issn.0253-4339.20251030004)
[21] [https://www.businessinsider.com](https://www.businessinsider.com/elon-musk-ai-data-centers-spacex-will-send-into-space-2026-6)
[22] [https://www.sinotrade.com.tw](https://www.sinotrade.com.tw/richclub/hotstock/%E6%9C%80%E6%96%B0%E9%BB%83%E4%BB%81%E5%8B%B3%E8%AB%87%E5%A4%AA%E7%A9%BA%E7%AE%97%E5%8A%9B%E5%8F%8A%E6%95%A3%E7%86%B1--SpaceX-IPO%E5%A6%82%E4%BD%95%E5%BC%95%E7%88%86%E5%8F%B0%E8%82%A1%E5%A4%AA%E7%A9%BA%E4%BE%9B%E6%87%89%E9%8F%88-%E8%82%A1%E5%B8%82%E8%A9%B1%E9%A1%8C-699fc40c4074db4b4ae26d7c)
[23] [https://satnews.com](https://satnews.com/2026/03/17/the-physics-wall-orbiting-data-centers-face-a-massive-cooling-challenge/)
[24] [https://www.jll.com](https://www.jll.com/en-us/insights/data-centers-in-space)
[25] [https://hk.finance.yahoo.com](https://hk.finance.yahoo.com/news/%E9%A6%AC%E6%96%AF%E5%85%8B%E7%9A%84%E5%A4%AA%E7%A9%BA%E8%B3%87%E6%96%99%E4%B8%AD%E5%BF%83%E7%9C%9F%E5%8F%AF%E8%A1%8C-%E5%B0%88%E5%AE%B6%E9%BB%9E%E5%87%BA%E4%B8%89%E5%A4%A7%E6%8C%91%E6%88%B0-023520457.html)
[26] [https://www.usatoday.com](https://www.usatoday.com/story/news/nation/2026/06/12/elon-musk-spacex-orbital-data-center-ai-satellites/90520416007/)
[27] [https://tspasemiconductor.substack.com](https://tspasemiconductor.substack.com/p/spacex-ipo-building-the-space-economy)
[28] [https://www.hkepc.com](https://www.hkepc.com/25143/%E7%82%BA%E4%BD%95%E5%9C%A8%E5%A4%AA%E7%A9%BA%E6%95%A3%E7%86%B1%E8%AE%8A%E5%BE%97%E6%A5%B5%E5%85%B6%E5%9B%B0%E9%9B%A3_%E8%A6%81%E8%A7%A3%E6%B1%BA%E5%BE%AE%E5%B0%8F%E7%9A%84%E7%86%B1%E9%87%8F__%E5%B0%B1%E9%9C%80%E8%A6%81%E5%B7%A8%E5%9E%8B%E6%95%A3%E7%86%B1%E6%9D%BF)
</td></tr>
</table>