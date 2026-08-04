# Kimi K3 in C

- Git Repo
  - https://github.com/FareedKhan-dev/kimi-k3-in-c

## 2026-08-03

- 印象是從 LinkedIn 貼文看到的，雖然討論中有人提到每秒個位數的 token 回應速度太慢，但原貼文認為這個實作的價值不在於「快」，而在於「可行」。因為照傳統的方式，受限於 GPU RAM 需求，無法在單一地端 PC 或 Latop 直接跑 Kimi K3 模型，但這個實作辦到了，而且是用 8 GB RAM 就可以跑。當然缺點就是「慢」，因為資料要從 SSD 搬到記憶體，有一點類似 SWAP 把硬碟拿來當記憶體用的概念。