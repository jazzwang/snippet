# Wllama 技術報告

## 概述

**Wllama** 是一個用於 [llama.cpp](https://github.com/ggerganov/llama.cpp) 的 WebAssembly 綁定，讓使用者能在瀏覽器端直接運行大型語言模型 (LLM)，無需後端伺服器或 GPU。

### 主要功能

- 🔌 OpenAI 相容 API（完全類型化的內建支援）
- 🚀 WebGPU 支援（自動分層到 GPU 加速）
- 🔥 多模態支援（圖片和音訊檔案輸入）
- 🎤 語音支援：文字轉語音、語音轉文字和即時語音
- 🔧 工具呼叫（Tool calling）支援
- 💻 直接在瀏覽器端進行推論（使用 WebAssembly SIMD），無需後端或 GPU
- 📦 無運行時依賴（可嵌入到專案中）
- 🔄 可自動切換單線程和多線程模式（基於瀏覽器支援）
- ⚡ 推論在 Worker 中執行，不阻塞 UI 渲染

## 系統需求

- 現代瀏覽器（Chrome、Firefox、Safari）
- WebAssembly 支援
- 可選：WebGPU 支援（V3.1+）
- Docker（如需自行編譯 WASM 二元檔）

## 安裝步驟

### 方法一：使用 npm 套件（推薦）

```bash
npm i @wllama/wllama
```

### 方法二：從 Git 倉庫安裝（含自製 WASM）

```bash
# 建議以 Git submodule 形式加入
git submodule add https://github.com/ngxson/wllama.git wllama
git submodule update --init --recursive

# 進入 wllama 目錄並安裝相依套件
cd wllama
npm ci
```

## 基本使用

### 在 React/TypeScript 專案中使用

```typescript
import { Wllama } from '@wllama/wllama';

// 設定 WASM 檔案路徑
const CONFIG_PATHS = {
  default: './esm/wasm/wllama.wasm',
};

// 建立 Wllama 實例（會自動切換單線程/多線程模式）
const wllama = new Wllama(CONFIG_PATHS);
```

### 載入模型

```typescript
// 從 Hugging Face 載入模型
const response = await wllama.loadModelFromHF(
  { repo: 'ggml-org/models', file: 'tinyllamas/stories260K.gguf' },
  { progressCallback: ({ loaded, total }) => console.log(`下載中... ${Math.round((loaded / total) * 100)}%`) }
);
```

### 基本對話完成（Chat Completion）

```typescript
const response = await wllama.createChatCompletion({
  messages: [{ role: 'user', content: '你好，請問台灣的首都是哪裡？' }],
  max_tokens: 50,
  temperature: 0.5,
  top_k: 40,
  top_p: 0.9,
});

console.log(response.choices[0].message.content);
```

### 串流輸出（Streaming）

```typescript
const stream = await wllama.createChatCompletion({
  messages: [{ role: 'user', content: '請用繁體中文寫一首詩' }],
  max_tokens: 100,
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0].delta.content ?? '');
}
```

## 進階功能

### 語音功能（Speech）

需要使用支援音訊的模型（如 [LFM3-Omni](https://huggingface.co/ggerml-org/LFM3-Omni-2B-GGUF)）。

#### 文字轉語音（Text to Speech）

```typescript
// 產生 WAV 檔案
const { audio, sample_rate } = await wllama.createSpeech({
  input: '你好，這是文字轉語音的範例',
  voice: 'female',
});

// 以串流方式取得音訊區塊
const { audio, sample_rate } = await wllama.createSpeech({
  input: '你好',
  voice: 'male',
  stream: true,
});

for await (const chunk of audio) {
  console.log(chunk); // 可即時播放
}
```

#### 語音轉文字（Transcription）

```typescript
const { text } = await wllama.createTranscription({
  file: await audioFile.arrayBuffer(),
  language: 'zh-TW', // 台灣繁體中文
});

console.log(text);
```

### 即時語音會話（Realtime Session）

```typescript
const session = await wllama.createRealtimeSession();
await session.send({ type: 'session.update', session: { type: 'transcription' } });

// 傳送單聲道浮點樣本
await session.appendAudio(samples);
await session.send({ type: 'input_audio_buffer.commit' });

// 接收事件
for await (const event of session.events()) {
  if (event.type === 'conversation.item.input_audio_transcription.delta') {
    console.log(event.delta);
  } else if (event.type === 'conversation.item.input_audio_transcription.completed') {
    break;
  }
}
await session.close();
```

### 工具呼叫（Tool Calling）

```typescript
const tools = [
  {
    type: 'function',
    function: {
      name: 'get_weather',
      description: '取得指定城市的當前天氣狀況',
      parameters: {
        type: 'object',
        properties: {
          city: { type: 'string', description: '城市名稱' },
        },
        required: ['city'],
      },
    },
  },
];

const messages = [{ role: 'user', content: '今天東京的天氣如何？' }];

const response = await wllama.createChatCompletion({
  messages,
  tools,
  tool_choice: 'auto',
  max_tokens: 256,
});

const choice = response.choices[0];
if (choice.finish_reason === 'tool_calls') {
  const toolCall = choice.message.tool_calls[0];
  const args = JSON.parse(toolCall.function.arguments);
  const result = { condition: '雨天', temperature_celsius: 21 };

  // 將工具結果回饋給模型
  messages.push(choice.message);
  messages.push({
    role: 'tool',
    tool_call_id: toolCall.id,
    content: JSON.stringify(result),
  });

  const final = await wllama.createChatCompletion({ messages, max_tokens: 256 });
  console.log(final.choices[0].message.content);
}
```

### 多模態輸入（Multimodal）

```typescript
// 載入模型與 mmproj
await wllama.loadModelFromHF({
  repo: 'user/model-GGUF',
  quant: 'Q4_K_M',
  mmprojQuant: 'Q8_0',
});

// 將圖片作為 ArrayBuffer 與文字一同傳送
const imageData = await fetch('./photo.jpg').then(r => r.arrayBuffer());

const response = await wllama.createChatCompletion({
  messages: [
    {
      role: 'user',
      content: [
        { type: 'image', data: imageData },
        { type: 'text', text: '請描述這張圖片的內容' },
      ],
    },
  ],
  max_tokens: 512,
});
```

### WebGPU 加速（V3.1+）

V3.1 會自動啟用 WebGPU 支援。預設所有層都會 offload 到 GPU。如果模型過大無法放入 VRAM，可手動調整 `n_gpu_layers`：

```typescript
await wllama.loadModel(files, {
  n_gpu_layers: 4, // 4 層 offload 到 GPU；設為 0 則禁用 GPU 推論
});
```

### 嵌入式模型載入（Embeddings）

```typescript
// 載入時啟用 embeddings 支援
await wllama.loadModelFromHF(
  { repo: 'user/model', file: 'model-Q4_K_M.gguf' },
  { embeddings: true }
);

const response = await wllama.createEmbedding({
  input: '快速奔跑的狐狸',
});

console.log(response.data[0].embedding); // float[] 向量
```

## 模型準備

### 模型分割（Split Model）

由於 ArrayBuffer 大小限制為 2GB，大於 2GB 的模型需要分割：

```bash
# 使用 llama-gguf-split 將模型分割為 512MB 的區塊
./llama-gguf-split --split-max-size 512M ./my_model.gguf ./my_model
```

輸出檔案如 `-00001-of-00003.gguf`、`-00002-of-00003.gguf` 等。

然後在載入時指定第一個檔案，wllama 會自動載入所有區塊：

```typescript
const wllama = new Wllama(CONFIG_PATHS, {
  parallelDownloads: 5, // 最大並行下載檔案數（預設 3）
});

await wllama.loadModelFromHF({
  repo: 'ngxson/tinyllama_split_test',
  file: 'stories15M-q8_0-00001-of-00003.gguf',
});
```

### 量化建議

建議使用 **Q4、Q5 或 Q6** 量化，在效能、檔案大小與品質之間取得平衡。避免使用 IQ（需配合 imatrix），可能會導致推論速度慢且品質較差。

## 自編譯 WASM

如需自行編譯 WASM 二元檔，可使用以下指令：

```bash
# 重要：需要安裝 Docker Compose

# 以 Git submodule 形式複製倉庫
git clone --recurse-submodules https://github.com/ngxson/wllama.git
cd wllama

# 可選：更新到最新的上游版本（不穩定）
# git submodule update --remote --merge

# 安裝相依套件
npm i

# 首先編譯 llama.cpp 為 WASM
npm run build:wasm

# 然後編譯 ES Module
npm run build
```

## 自訂日誌（Custom Logger）

### 抑制除錯訊息

```typescript
import { Wllama, LoggerWithoutDebug } from '@wllama/wllama';

const wllama = new Wllama(pathConfig, {
  logger: LoggerWithoutDebug,
});
```

### 添加表情符號前綴

```typescript
const wllama = new Wllama(pathConfig, {
  logger: {
    debug: (...args) => console.debug('🔧', ...args),
    log: (...args) => console.log('ℹ️', ...args),
    warn: (...args) => console.warn('⚠️', ...args),
    error: (...args) => console.error('☠️', ...args),
  },
});
```

## 測試與驗證

### 1. 基本功能測試

```typescript
// 測試對話完成
const response = await wllama.createChatCompletion({
  messages: [{ role: 'user', content: '你好，世界' }],
  max_tokens: 30,
});

// 驗證回應格式
if (response.choices && response.choices.length > 0) {
  console.log('✓ 對話完成 API 運作正常');
  console.log('回應:', response.choices[0].message.content);
} else {
  throw new Error('對話完成 API 回應格式錯誤');
}
```

### 2. 模型載入測試

```typescript
try {
  await wllama.loadModelFromHF(
    { repo: 'ggml-org/models', file: 'tinyllamas/stories260K.gguf' }
  );
  console.log('✓ 模型載入成功');
  
  // 檢查模型資訊
  const contextInfo = wllama.getLoadedContextInfo();
  console.log('模型資訊:', {
    n_ctx: contextInfo.n_ctx,
    has_audio_input: contextInfo.has_audio_input,
    has_audio_output: contextInfo.has_audio_output,
    has_live_asr: contextInfo.has_live_asr,
    audio_voices: contextInfo.audio_voices,
  });
} catch (error) {
  console.error('✗ 模型載入失敗:', error);
  throw error;
}
```

### 3. 串流輸出測試

```typescript
let receivedText = '';
const stream = await wllama.createChatCompletion({
  messages: [{ role: 'user', content: '請用繁體中文寫一首短詩' }],
  max_tokens: 50,
  stream: true,
});

try {
  for await (const chunk of stream) {
    receivedText += chunk.choices[0].delta.content ?? '';
  }
  
  if (receivedText.trim().length > 0) {
    console.log('✓ 串流輸出測試通過');
    console.log('收到的文字:', receivedText);
  } else {
    throw new Error('串流輸出未收到任何內容');
  }
} catch (error) {
  console.error('✗ 串流輸出測試失敗:', error);
  throw error;
}
```

### 4. WebGPU 加速測試（V3.1+）

```typescript
try {
  await wllama.setCompat('default', 'firefox_safari');
  
  await wllama.loadModel(files, {
    n_gpu_layers: 4,
  });
  
  const contextInfo = wllama.getLoadedContextInfo();
  console.log('WebGPU 狀態:', {
    gpu_available: contextInfo.gpu_available,
    n_gpu_layers: contextInfo.n_gpu_layers,
  });
  
  console.log('✓ WebGPU 加速測試通過');
} catch (error) {
  console.error('✗ WebGPU 加速測試失敗:', error);
}
```

### 5. 工具呼叫測試

```typescript
const tools = [
  {
    type: 'function',
    function: {
      name: 'test_function',
      description: '測試功能',
      parameters: {
        type: 'object',
        properties: { value: { type: 'number' } },
        required: ['value'],
      },
    },
  },
];

const response = await wllama.createChatCompletion({
  messages: [{ role: 'user', content: '請呼叫 test_function，參數 value 設為 42' }],
  tools,
  tool_choice: 'auto',
});

if (response.choices[0].finish_reason === 'tool_calls') {
  console.log('✓ 工具呼叫測試通過');
  console.log('工具呼叫:', response.choices[0].message.tool_calls[0]);
} else {
  console.log('模型未呼叫工具，回應:', response.choices[0].message.content);
}
```

## 性能最佳化

### 1. 模型量選擇

| 量化等級 | 效能 | 檔案大小 | 品質 | 推薦使用 |
|---------|------|---------|------|---------|
| Q4_K_M  | ⭐⭐⭐⭐ | 中等 | ⭐⭐⭐⭐ | 一般用途 |
| Q5_K_M  | ⭐⭐⭐  | 較中等 | ⭐⭐⭐⭐⭐ | 高品質需求 |
| Q6_K    | ⭐⭐⭐⭐ | 較大   | ⭐⭐⭐⭐⭐ | 追求最佳品質 |

### 2. 並行下載設定

```typescript
const wllama = new Wllama(CONFIG_PATHS, {
  parallelDownloads: 5, // 增加並行下載數以加速大型模型
});
```

### 3. WebGPU 層數調整

如果模型過大無法完全放入 GPU，可調整 `n_gpu_layers`：

```typescript
await wllama.loadModel(files, {
  n_gpu_layers: 8, // 根據 VRAM 大小調整，預設所有層都會 offload
});
```

## 已知限制

1. **多線程模式**：啟用多線程需在伺服端添加 `Cross-Origin-Embedder-Policy` 和 `Cross-Origin-Opener-Policy` 標頭
2. **檔案大小限制**：最大 2GB（ArrayBuffer 限制），大於 2GB 的模型需分割
3. **WebGPU 相容性**：目前主要支援 Chrome，Firefox 需手動啟用旗標
4. **Tokenizer API**：已移除，如需支援請提 issue

## 參考資源

- [官方文件](https://github.ngxson.com/wllama/docs/)
- [Hugging Face Demo](https://huggingface.co/spaces/ngxson/wllama)
- [V3.0 升級指南](./guides/intro-v3.md)
- [V3.1 WebGPU 支援](./guides/intro-v3.1.md)
- [llama.cpp 主倉庫](https://github.com/ggerganov/llama.cpp)

*最後更新：2024 年*
