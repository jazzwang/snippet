# OpenSSF Scorecard

- Website
  - https://scorecard.dev/
- Git Repo:
  - https://github.com/ossf/scorecard

## 2025-01-05

- 緣起：根據研究[1]，單 2024 年就有 450 萬假 Star [2]。
  - [1] https://arxiv.org/pdf/2412.13459
- 文末「對開源從業者的啟示」，提到 OpenSSF Scorecard 可以拿來評估開源專案的「品質」
  - [2] https://mp.weixin.qq.com/s/R_3Wou6dKlSFjikW8q52JQ
- 文中提到檢測假星星的 `StarScout` 工具
  - [3] https://github.com/hehao98/StarScout

> GitHub 星數並不屬於可靠的質量訊號，請勿將其用於高風險決策，至少不應單獨使用。
> 研究人員表示，儘管不可能在此類決策中完全忽略星數的影響，但也請務必參考並評估其他訊號。
> 例如，從業者可以考慮能夠反映開源元件採用水平的其他安全相關和基於活動的訊號，
> 包括<mark>開源安全基金會（OpenSSF）記分卡</mark>。

- 仔細讀了一下 README，OpenSSF Scorecard 原本名稱是 Security Scorecard，
  所以衡量的指標多半跟 Security 有關。