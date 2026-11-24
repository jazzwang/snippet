# Mem0 技術報告：記憶體分層架構與安裝部署指南

> **更新日期**: 2026-11-24  
> **來源**: [mem0ai/mem0](https://github.com/mem0ai/mem0)  
> **授權**: Apache 2.0

## 執行摘要

Mem0 是為 AI 助理和 AI 代理設計的記憶分層架構，提供個人化的 AI 互動能力。本報告詳細說明 Mem0 的安裝、測試與驗證流程，涵蓋三個主要部署模式：

1. **程式庫模式 (Library)** - 最快速的原型開發
2. **自我托管伺服器 (Self-Hosted Server)** - 完整伺服器架構
3. **雲端平台 (Cloud Platform)** - 零營運開銷的生產級解決方案

## 1. 系統要求與前置條件

### 1.1 通用要求

| 項目 | 版本要求 |
|------|----------|
| Python | 3.10 或更高版本 |
| Node.js | 18 或更高版本 |
| Docker | 20.10 或更高版本（自我托管模式） |
| LLM 提供者 | OpenAI API 或其他支援的 LLM |

### 1.2 推薦配置（混合搜尋最佳效能）

```bash
# 安裝 NLP 支援套件以提升混合搜尋效能
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
```

## 2. 安裝步驟

### 2.1 程式庫模式（Library Mode）

#### 2.1.1 Python SDK 安裝

```bash
pip install mem0ai

# 進階功能：啟用 BM25 關鍵字匹配和實體萃取
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
```

#### 2.1.2 Node.js SDK 安裝

```bash
npm install mem0ai
```

#### 2.1.3 環境變數設定

```bash
# 設定 OpenAI API 金鑰（預設模型）
export OPENAI_API_KEY="your-openai-api-key"

# 或使用其他 LLM 提供者
export MEM0_API_KEY="your-api-key"
```

### 2.2 自我托管伺服器（Self-Hosted Server）

#### 2.2.1 快速啟動（推薦方式）

```bash
cd server && make bootstrap
```

此命令會：
- 啟動完整的 Docker 堆疊
- 建立管理員帳戶
- 發出第一個 API 金鑰

#### 2.2.2 手動啟動（瀏覽器設定視窗）

```bash
cd server && docker compose up -d
```

然後在瀏覽器訪問 `http://localhost:3000` 完成設定。

#### 2.2.3 自訂環境變數

建立 `server/.env` 檔案：

```env
# LLM 提供者設定
OPENAI_API_KEY=your-openai-api-key

# JWT 金鑰（48 位元亂數）
JWT_SECRET=$(openssl rand -base64 48)

# 資料庫設定
POSTGRES_PASSWORD=your-postgres-password

# 可選：停用認證（僅供開發環境）
# AUTH_DISABLED=true
```

### 2.3 雲端平台（Cloud Platform）

1. 註冊帳戶：[app.mem0.ai](https://app.mem0.ai?utm_source=oss&utm_medium=readme)
2. 透過 SDK 或 API 金鑰整合記憶分層
3. 若使用托管的 Qdrant 向量，參閱 [平台遷移指南](https://docs.mem0.ai/migration/oss-to-platform)

### 2.4 CLI 工具

```bash
# 安裝 CLI
npm install -g @mem0/cli
# 或
pip install mem0-cli

# 初始化
mem0 init

# 以代理身份註冊（無需電子郵件）
mem0 init --agent --agent-caller claude-code

# 或作為人類擁有者
mem0 init --email your-email@example.com
```

## 3. 測試步驟

### 3.1 程式庫模式測試

#### 3.1.1 Python SDK 基本測試

```python
from openai import OpenAI
from mem0 import Memory

# 初始化
openai_client = OpenAI()
memory = Memory()

# 測試 1：新增記憶
user_id = "test_user_001"
message = {
    "role": "user",
    "content": "我偏好使用暗色模式和 Vim 的鍵盤快捷鍵"
}
memory.add(message, user_id=user_id)
print("✓ 記憶新增成功")

# 測試 2：搜尋記憶
results = memory.search(
    query="使用者偏好設定",
    filters={"user_id": user_id},
    top_k=3
)
if results.get("results"):
    print("✓ 記憶搜尋成功")
    for entry in results["results"]:
        print(f"  - {entry['memory']}")
else:
    print("✗ 搜尋無結果")

# 測試 3：對話流測試
def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # 1. 取得相關記憶
    relevant_memories = memory.search(
        query=message,
        filters={"user_id": user_id},
        top_k=3
    )
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])

    # 2. 建構系統提示詞
    system_prompt = f"""You are a helpful AI assistant. 
    Answer the question based on the user's query and their stored memories.
    
    User Memories:
    {memories_str}
    """
    
    # 3. 呼叫 LLM
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    response = openai_client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages
    )
    assistant_response = response.choices[0].message.content

    # 4. 新增對話到記憶
    messages.append({"role": "assistant", "content": assistant_response})
    memory.add(messages, user_id=user_id)

    return assistant_response

# 執行測試對話
test_message = "我喜歡深色主題"
response = chat_with_memories(test_message, user_id="test_user_001")
print(f"\nAI 回應: {response}")

# 驗證記憶已新增
validation_search = memory.search(
    query="深色主題",
    filters={"user_id": "test_user_001"},
    top_k=1
)
if validation_search.get("results"):
    print("✓ 記憶持久化驗證通過")
else:
    print("✗ 記憶持久化失敗")
```

#### 3.1.2 Node.js SDK 基本測試

```javascript
import { Mem0 } from 'mem0ai';
import OpenAI from 'openai';

const openai = new OpenAI();
const mem0 = new Mem0({ openai });

// 測試 1：新增記憶
const user_id = "test_user_001";
const result = await mem0.add([
  {
    role: "user",
    content: "我偏好使用暗色模式和 Vim 的鍵盤快捷鍵"
  }
], { userId: user_id });

console.log('✓ 記憶新增成功:', result);

// 測試 2：搜尋記憶
const searchResults = await mem0.search({
  query: "使用者偏好設定",
  filters: { userId: user_id },
  topK: 3
});

if (searchResults.results.length > 0) {
  console.log('✓ 記憶搜尋成功');
  searchResults.results.forEach(entry => {
    console.log(`  - ${entry.memory}`);
  });
} else {
  console.log('✗ 搜尋無結果');
}

// 測試 3：對話流
async function chatWithMemories(message, userId = "default_user") {
  // 1. 取得相關記憶
  const memories = await mem0.search({
    query: message,
    filters: { userId },
    topK: 3
  });
  const memoriesStr = memories.results.map(e => `- ${e.memory}`).join('\n');

  // 2. 呼叫 LLM
  const systemPrompt = `You are a helpful AI assistant. 
  Answer based on user's query and memories.
  
  User Memories:
  ${memoriesStr}`;
  
  const response = await openai.chat.completions.create({
    model: "gpt-5-mini",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: message }
    ]
  });
  const assistantResponse = response.choices[0].message.content;

  // 3. 新增對話
  await mem0.add([
    { role: "assistant", content: assistantResponse }
  ], { userId });

  return assistantResponse;
}

// 執行測試
const testResponse = await chatWithMemories("我喜歡深色主題", "test_user_001");
console.log('\nAI 回應:', testResponse);
```

### 3.2 自我托管伺服器測試

#### 3.2.1 API 端點測試

```bash
# 測試 API 連線
curl http://localhost:8888/docs

# 測試記憶新增（需先登入）
curl -X POST http://localhost:8888/api/v1/memories \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "我偏好暗色模式"}
    ]
  }'

# 測試記憶搜尋
curl -X POST http://localhost:8888/api/v1/memories/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "暗色模式",
    "filters": {"user_id": "test_user"}
  }'
```

#### 3.2.2 管理員命令測試

```bash
# 管理員新增記憶
mem0 add "我偏好暗色模式" --user-id test_user

# 搜尋記憶
mem0 search "暗色模式" --user-id test_user

# 列出所有記憶來源
mem0 sources

# 列出事件日誌
mem0 events --limit 10
```

## 4. 驗證步驟

### 4.1 功能驗證

#### 4.1.1 記憶存取驗證

```python
# 完整驗證流程
from mem0 import Memory

memory = Memory()

# 步驟 1：新增多筆記憶
test_memories = [
    "我偏好使用暗色模式",
    "使用 Vim 的鍵盤快捷鍵",
    "經常處理 Python 程式碼",
    "對效能優化有要求"
]

for memory_text in test_memories:
    memory.add({"role": "user", "content": memory_text}, user_id="validation_user")

print("✓ 新增 4 筆記憶")

# 步驟 2：驗證記憶數量
results = memory.search(
    query="使用者設定",
    filters={"user_id": "validation_user"},
    top_k=10
)
assert len(results.get("results", [])) == 4, "記憶數量不符"
print(f"✓ 記憶數量驗證通過：{len(results['results'])} 筆")

# 步驟 3：驗證記憶內容
for entry in results["results"]:
    assert "使用者設定" in entry.get("memory", ""), "記憶內容異常"
print("✓ 記憶內容驗證通過")
```

#### 4.1.2 對話上下文驗證

```python
def validate_dialogue_context():
    """驗證對話上下文保持能力"""
    memory = Memory()
    
    # 建立對話序列
    conversation_history = [
        {"role": "user", "content": "我偏好暗色模式"},
        {"role": "assistant", "content": "好的，我已經記錄您的偏好"},
        {"role": "user", "content": "設定介面為暗色模式"},
        {"role": "assistant", "content": "正在設定暗色模式介面"},
    ]
    
    # 新增對話到記憶
    memory.add(conversation_history, user_id="dialogue_user")
    print("✓ 對話序列新增成功")
    
    # 驗證記憶能正確萃取偏好資訊
    search_results = memory.search(
        query="暗色模式",
        filters={"user_id": "dialogue_user"},
        top_k=3
    )
    
    assert len(search_results["results"]) > 0, "未找到相關記憶"
    print("✓ 上下文驗證通過")
```

### 4.2 效能驗證

#### 4.2.1 搜尋效能測試

```python
import time

def benchmark_search():
    """搜尋效能測試"""
    memory = Memory()
    
    # 建立測試數據（100 筆記憶）
    test_memories = [
        f"使用者 {i} 偏好 {['暗色模式', '亮色模式', '混合模式'][i % 3]}" 
        for i in range(100)
    ]
    
    for mem in test_memories:
        memory.add({"role": "user", "content": mem}, user_id=f"user_{i % 10}")
    
    # 執行搜尋測試
    iterations = 10
    times = []
    
    for i in range(iterations):
        start_time = time.time()
        results = memory.search(
            query="使用者偏好設定",
            filters={"user_id": "user_0"},
            top_k=5
        )
        elapsed = time.time() - start_time
        times.append(elapsed)
        print(f"搜尋 #{i+1}: {elapsed:.4f} 秒")
    
    avg_time = sum(times) / len(times)
    print(f"\n平均搜尋時間: {avg_time:.4f} 秒")
    print(f"搜尋效能驗證通過 ✓" if avg_time < 2.0 else "搜尋效能警告 ⚠")
```

### 4.3 整合驗證

#### 4.3.1 CLI 整合驗證

```bash
# 1. 初始化 Mem0
mem0 init --agent --agent-caller test-agent

# 2. 新增記憶
mem0 add "測試記憶內容" --user-id validation_user
echo "✓ 記憶新增完成"

# 3. 搜尋記憶
mem0 search "測試記憶" --user-id validation_user
echo "✓ 記憶搜尋完成"

# 4. 檢查事件日誌
mem0 events --user-id validation_user
echo "✓ 事件日誌查詢完成"
```

#### 4.3.2 代理技能驗證

```bash
# 安裝 Mem0 代理技能
npx skills add https://github.com/mem0ai/mem0 --skill mem0

# 驗證技能已安裝
npx skills list | grep mem0

# 使用技能建立記憶
/mem0-integrate
# 或
/mem0-test-integration
```

## 5. 故障排除

### 5.1 常見問題

#### 5.1.1 記憶體存取失敗

**問題**: `MemoryError: Could not fetch embeddings`

**解決方案**:
```bash
# 確認 API 金鑰設定
echo $OPENAI_API_KEY  # 確認非空值

# 確認網路連線
curl https://api.openai.com/v1/models

# 檢查 API 限額
# 如需使用本地模型，設定：
export MEM0_LLM_PROVIDER="ollama"
export MEM0_LLM_MODEL="llama3"
```

#### 5.1.2 Docker 啟動失敗

**問題**: 自我托管伺服器無法啟動

**解決方案**:
```bash
# 確認 Docker 版本
docker --version  # 需要 20.10+

# 檢查 Docker 組態
docker compose -f server/docker-compose.yml config

# 手動檢查每個服務
docker compose up -d --no-deps mem0-api
docker compose up -d --no-deps postgres
docker compose up -d --no-deps neo4j
```

### 5.2 效能優化

```python
# 設定記憶預算
memory = Memory(
    max_memories=1000,  # 最大記憶數量
    embedding_model="text-embedding-3-small",  # 預設模型
    top_k=200  # 搜尋預算
)

# 使用混合搜尋提升準確率
results = memory.search(
    query="使用者設定",
    filters={"user_id": "user_001"},
    top_k=10,  # 限制返回數量
    similarity_threshold=0.5  # 相似度閾值
)
```

## 6. 最佳實踐

### 6.1 記憶管理

1. **定期清理過期記憶**
2. **設定記憶數量上限**
3. **使用適當的 filter 參數**

### 6.2 安全性

1. **不要將 API 金鑰存入程式碼中**
2. **使用環境變數或金鑰管理系統**
3. **啟用自我托管的認證機制**

### 6.3 監控

1. **記錄記憶新增/搜尋頻次**
2. **監控 API 回應時間**
3. **追蹤錯誤率**

## 7. 參考文獻

1. [Mem0 官方文件](https://docs.mem0.ai)
2. [Mem0 GitHub 倉庫](https://github.com/mem0ai/mem0)
3. [Mem0 研究論文](https://mem0.ai/research)
4. [Mem0 Discord 社區](https://mem0.dev/DiG)

## 8. 授權

本報告基於 Apache 2.0 授權的 Mem0 專案內容編寫。

*報告生成時間：2026-11-24*
