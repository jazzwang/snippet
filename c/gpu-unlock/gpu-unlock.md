# GPU Unlock 技術報告

> **解鎖 NVIDIA GeForce RTX 20/30/40 系列 Tensor Core 全速效能**

## 一、專案簡介

NVIDIA GeForce 顯卡針對 FP16、BF16 和 TF32 數學運算（搭配 FP32 累加）的 Tensor Core 效能進行了限制，使其僅能發揮一半的運算速度。這項限制主要用於區分消費級與專業級（A 系列/數據中心）顯卡的市場定位。

**gpu-unlock** 是一個 Linux 內核模組，能在系統啟動時於 NVIDIA 驅動載入之前解鎖這些限制，讓您的 GeForce RTX 顯卡發揮完整效能，無需修改 VBIOS 或打補丁的驅動程式。

---

## 二、支援的 GPU 型號

| 世代 | 型號 | 狀態 |
|------|------|------|
| **Ampere (RTX 30 系列)** | RTX 3050, 3060, 3060 Ti, 3070, 3070 Ti, 3080, 3080 Ti, 3090, 3090 Ti, RTX 3070/3080 筆記型 GPU | 穩定，100+ 用戶回報 |
| **Ada Lovelace (RTX 40 系列)** | RTX 4060, 4060 Ti, 4070, 4070 SUPER, 4070 Ti, 4070 Ti SUPER, 4080, 4080 SUPER, 4090, 4090 D, RTX 4050/4060 筆記型 GPU | 實驗性 |
| **Turing (RTX 20 系列)** | RTX 2060, 2060 SUPER, 2070, 2070 SUPER, 2080, 2080 SUPER, 2080 Ti, Titan RTX | 實驗性 |
| **Blackwell (RTX 50 系列)** | - | 不支援 |

> **筆記型電腦注意事項**：筆記型電腦只有在獨顯從未完全關機的情況下才能保持解鎖。許多筆記型電腦會在閒置時關機，這會靜默地重置解鎖狀態。可嘗試以 `options nvidia NVreg_DynamicPowerManagement=0x00` 加入 `/etc/modprobe.d/` 來關閉動態電源管理，但效果因型號而異。

---

## 三、效能提升

### 3.1 理論峰值運算能力（FP32 累加）

| 型號 | 解鎖前 | 解鎖後 | 提升 |
|------|--------|--------|------|
| RTX 3060 12GB | 27 TFLOPS | 51 TFLOPS | +87% |
| RTX 3060 Ti | 37 TFLOPS | 68 TFLOPS | +82% |
| RTX 3070 | 40 TFLOPS | 72 TFLOPS | +81% |
| RTX 3080 10GB | 65 TFLOPS | 113 TFLOPS | +73% |
| RTX 3090 | 75 TFLOPS | 125 TFLOPS | +65% |
| RTX 3090 Ti (450W) | 88 TFLOPS | 157 TFLOPS | +80% |
| RTX 4070 Ti | 81 TFLOPS | 150 TFLOPS | +84% |
| RTX 4080 | 104 TFLOPS | 193 TFLOPS | +87% |
| RTX 4090 | 165 TFLOPS | 329 TFLOPS | +100%（峰值 MMA 速率） |

> 註：RTX 4090 在標準功率限制下會在 Tensor Core 耗盡前先用完電力，因此大型 GEMM 運算的實際增益低於理論峰值。

### 3.2 實際工作負載效能提升

| 工作負載 | 典型加速比 |
|----------|-----------|
| LLM 提示詞處理（FP16/BF16 或 AWQ/GPTQ），使用 vLLM、PyTorch、Transformers | +25–55% |
| 第一個 Token 生成時間 | 降低 25–30% |
| LoRA 與完整微調（BF16） | +25–50% |
| 圖像生成（SDXL、SD 1.5、Krea、ComfyUI 中的 DiT 模型），FP16/BF16 | +30–55% |
| 影片生成（Wan 2.2），BF16 運算 | +15–20% |
| FlashAttention / SDPA 核心 | +50–60% |
| llama.cpp / Ollama（量化 GGUF） | 0–15%（主要體現在長上下文） |
| LLM 解碼 / Token 生成（記憶體綁定） | 無變化 |
| INT8、FP8 與 INT4 模型 | 無變化 |
| 遊戲與 FP32 CUDA | 無變化 |

> 輸出結果在解鎖前後完全相同；僅速度有所提升。這些數字來自用戶回報的 [相容性報告](https://github.com/Zagitta/gpu-unlock/issues)，您可以在其中查看完整的基準測試細節並發布您的報告。

---

## 四、安裝步驟

### 步驟 1：下載並安裝套件

```bash
git clone https://github.com/Zagitta/gpu-unlock
cd gpu-unlock
make install
```

執行 `make install` 會自動偵測您的發行版並選擇對應的安裝方式：

- **Arch Linux**：`make install-arch`（使用 makepkg）
- **Debian/Ubuntu/Mint**：`make install-deb`（使用 apt-get 建立依賴）
- **Fedora/RHEL/CentOS**：`make install-rpm`（使用 dnf）

如需手動建立套件，可執行 `make deb`、`make rpm` 或 `make arch`，套件將分別產出於 `build/deb`、`build/rpm` 或 `build/arch`。

### 步驟 2：加入 Kernel Command Line

套件安裝後，必須將 `gpu_unlock.targets=all` 加入您的啟動列（kernel command line）。請依照您的啟動管理員選擇對應方式：

#### **GRUB (Debian/Ubuntu/Mint)**

```bash
sudo nano /etc/default/grub
```

在 `GRUB_CMDLINE_LINUX_DEFAULT` 參數中加入 `gpu_unlock.targets=all`，例如：

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash gpu_unlock.targets=all"
```

儲存後執行：

```bash
sudo update-grub
```

#### **GRUB (Arch/CachyOS)**

同上編輯 `/etc/default/grub`，然後執行：

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

#### **Fedora/RHEL**

```bash
sudo grubby --update-kernel=ALL --args="gpu_unlock.targets=all"
```

#### **systemd-boot**

在 `/boot/loader/entries/` 下的啟動條目中加入 `gpu_unlock.targets=all` 到 `options` 行。

#### **UKI / 自動產生的啟動記錄**

在 `/etc/kernel/cmdline` 中加入該參數並重新產生您的啟動影像/條目（例如 `sudo mkinitcpio -P` 用於 mkinitcpio UKI）。

> **註**：您也可以指定特定的 PCI 裝置 ID：
> - `gpu_unlock.targets=0000:21:00.0`（僅解鎖此卡）
> - `gpu_unlock.targets=0000:21:00.0,0000:22:00.0`（解鎖多個卡，逗號分隔）
>
> 裝置 ID 格式與 `lspci -D` 輸出相同（十六進位數字大小寫皆可）。

---

## 五、測試與驗證步驟

### 步驟 1：確認模組已載入並執行解鎖

重新啟動系統後，檢查日誌：

```bash
journalctl -k -b | grep gpu_unlock
```

您應該會看到類似以下的輸出：

```
gpu_unlock: unlocked 0000:21:00.0 (RTX 3080)
gpu_unlock: SS0=0x88888888 (full BF16 rate), SS1=0x8 (IMLA4)
gpu_unlock: performed FLR before nvidia driver bind
```

### 步驟 2：確認 GPU 驅動資訊

檢查 NVIDIA 驅動是否正確綁定：

```bash
lspci -nnk -s 0000:[ID]:00.0
```

或簡化版：

```bash
lspci -nnk
```

確認 NVIDIA 驅動已正常載入，且您的顯卡顯示為 NVIDIA 裝置。

### 步驟 3：測試 Tensor Core 效能

#### 方法 A：使用 GPU-Z 或 nvidia-smi

```bash
nvidia-smi --query-compute-caps=all --format=csv
```

確認 Tensor Core 相關參數是否已啟用。

#### 方法 B：執行基準測試

可使用以下工具驗證效能提升：

1. **TensorFlow / PyTorch FP16 測試**

```python
import torch
import time

torch.cuda.set_device(0)
torch.cuda.empty_cache()

# 建立大型矩陣
N = 8192
A = torch.randn(N, N, device='cuda', dtype=torch.bfloat16)
B = torch.randn(N, N, device='cuda', dtype=torch.bfloat16)

# 測試矩阵乘法
start = time.time()
for _ in range(10):
    C = torch.matmul(A, B)
end = time.time()

print(f"BF16 Matrix Multiply: {(end - start) * 10:.2f} seconds for 10 iterations")
```

2. **使用 vLLM 測試 LLM 提示詞處理**

```bash
vllm serve MODEL_NAME --tensor-parallel-size 1 --dtype bfloat16
```

比較解鎖前後處理相同提示詞的時間，應可觀察到 25–55% 的加速。

3. **使用 Ollama 測試**

```bash
ollama run llama3:8b
```

測試長上下文生成，應可觀察到明顯加速。

### 步驟 4：檢查日誌與問題排查

如果解鎖失敗，請檢查詳細日誌：

```bash
journalctl -k -b --all | grep gpu_unlock
dmesg | grep -i nvidia
dmesg | grep -i gpu_unlock
```

常見問題：

- **模組載入失敗**：檢查 `/var/log/kern.log` 或 `dmesg` 是否有模組載入錯誤
- **顯示卡一瞬間變黑**：這是正常的，因為解鎖模組會在顯示卡被 NVIDIA 驅動綁定之前重置顯示卡
- **筆記型電腦閒置後失效**：檢查是否需要在 `/etc/modprobe.d/` 中加入動態電源管理設定

---

## 六、停用與移除

### 臨時停用（單次啟動）

使用 GRUB 編輯器（如 `grub-editenv`）或直接使用 GRUB 啟動畫面，移除 `gpu_unlock.targets=all` 參數。

### 永久停用

1. **從啟動列移除參數**

   - **GRUB (Debian/Ubuntu/Mint)**：編輯 `/etc/default/grub`，移除 `gpu_unlock.targets=all`，然後執行 `sudo update-grub`
   - **Fedora/RHEL**：執行 `sudo grubby --update-kernel=ALL --remove-args="gpu_unlock.targets=all"`

2. **移除套件**

```bash
make uninstall
```

這將移除模組和 initramfs 中的相關設定。

### 手動停用（一次性的啟動）

在 GRUB 啟動選單中直接移除參數，適合快速測試。

---

## 七、常見問題（FAQ）

### Q：這是一個網站、代幣或安裝程式嗎？

A：沒有。這是 GPU Unlock 的唯一原始來源。任何網站、代幣、安裝程式或其他形式都與此專案或開發者無關。

### Q：這依賴於特定的驅動版本嗎？我看到有 `610.43.03` 的 pinned。

A：不，驅動程式僅用於提取解鎖所依賴的韌體（firmware）。實際運行時使用任何 NVIDIA 驅動都可以。

### Q：Windows 支援嗎？

A：開發者不使用 Windows，因此不維護 Windows 版本。但有一個第三方移植版本：[Windows-GPU-UNLOCK](https://github.com/impacifist/Windows-GPU-UNLOCK)。Windows 安裝程式在網路上流通，但強烈建議非常謹慎地使用。

### Q：Blackwell (RTX 50) 系列支援嗎？

A：目前不支援，也不太可能支援。

### Q：為什麼 NVIDIA 要限制我的 GPU 效能？

A：市場區隔策略，他們希望企業購買專業版顯卡以獲得這些完整效能，以顯著更高的價格出售。

### Q：這會損壞我的 GPU 嗎？

A：極不可能。這只是解鎖 NVIDIA 為了區分數據中心和專業顯卡而設定的小限制。GPU 可能會因進行更多運算而略微升溫，但標準的降頻和電源管理機制仍然完好，會自動降頻。

### Q：如何協助開發者？

A：請考慮 [贊助](#support-me) 以購買更多 GPU 用於測試。

---

## 八、支援開發者

感謝您的支援，讓開發者能購買更多 GPU 用於測試與改進：

- [GitHub Sponsor](https://github.com/sponsors/Zagitta)
- [Buy Me a Coffee](https://buymeacoffee.com/zagitta)
- **Ethereum**: `0xf4eee937937f92038D70B16AbD7736D8a53a1c5c`
- **Bitcoin**: `bc1qwpkwp70fn76z3s4kg2l9y3j4kst95twcznuugf`
- **Solana**: `8Rih6HY7V4LcdjYHz4iSffT4fTniqw5CACaBigSVxNYu`

---

## 九、工作原理

`gpu-unlock` 是一個 Linux 內核模組，結合了 cmpunlocker 的 V67/PLM 技術與 UEFI 方法的啟動時機。

**運作流程**：

1. 在系統啟動時，模組在 initramfs 中載入，於 NVIDIA 驅動綁定顯卡之前執行解鎖
2. 寫入速度選擇器（SS0 `0x88888888`，選擇全速 BF16 速率，以及 4 位 SS1 `0x8` IMLA4）
3. 執行 FLR（Firmware Level Reset）
4. 在未經修改的 NVIDIA 驅動綁定顯卡之前完成所有操作
5. 此模組既非 UEFI 應用程式，也非 patched NVIDIA 驅動

**Initramfs 配置**：

- **mkinitcpio**：`/etc/mkinitcpio.conf.d/zz-gpu-unlock.conf` 將 `gpu_unlock` 置於 `nvidia` 之前
- **initramfs-tools**：`/usr/share/initramfs-tools/modules.d/gpu-unlock.conf`
- **dracut**：`/usr/lib/dracut/dracut.conf.d/gpu-unlock.conf`

模組僅在啟動列加入 `gpu_unlock.targets=` 參數時才會執行任何操作。

---

## 十、參考資源

- [專案官方網站](https://github.com/Zagitta/gpu-unlock)
- [相容性回報](https://github.com/Zagitta/gpu-unlock/issues)
- [Windows 移植版本](https://github.com/impacifist/Windows-GPU-UNLOCK)
- [專案源碼](https://github.com/Zagitta/gpu-unlock/tree/main/kernel/gpu_unlock)

---

*報告撰寫日期：2024*  
*基於 [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) 官方文檔整理*
