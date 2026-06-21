# Microcks

- Git Repo
  - https://github.com/microcks/microcks
- Website
  - https://microcks.io/

> The open source, cloud native tool for API Mocking and Testing. Microcks is a Cloud Native Computing Foundation incubating project 🚀

## 2026-06-21

- 緣起：
  - 從 Swagger (OpenAPI, `RESTful`) 到 AsyncAPI (`Event-driven`)，想知道有沒有簡單生成 petstore 的 Kafka 後端程式
  - 在與 Google Search AI Mode 對談時，有提到 Microcks

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
AsyncAPI 有類似 petstore 的範例嗎？
</td></tr><tr><td>A:</td><td>

## AsyncAPI 對應的 PetStore 範例

有的，AsyncAPI 官方與微服務社群（如 [Microcks.io](https://microcks.io/)）最常拿來當作標準教學與測試的範例，正是 AsyncAPI 版的 Petstore。 [1, 2]
在非同步（Event-Driven）的場景下，Petstore 範例通常會被轉換為 「當寵物商店有新訂單、或有新寵物上架時發送事件」 的架構。 [3]
以下為你提供 AsyncAPI v3.0 最新標準 的 Petstore 完整範本（以 Kafka 為基礎，內含 `Pet` 與 `Order` 的事件宣告）： [1, 2]

### 📄 Petstore AsyncAPI v3.0 範本 (`petstore-asyncapi.yaml`)

```yaml
asyncapi: 3.0.0info:
  title: Petstore Asynchronous Stream API
  version: 1.0.0description: 寵物商店非同步 API，定義 Pet/Order 的 Kafka 事件。
servers:
  dev-kafka:
    host: localhost:9092protocol: kafka
# ... (Channels and Components defined below)
```

*(上述 YAML 內容展示了 Kafka 基礎結構，詳細的 `channels` 與 `components` 定義可參考 [Microcks 範例網站](https://microcks.io/documentation/tutorials/first-asyncapi-mock/))*\* [1, 2]

### 💡 AsyncAPI 與 OpenAPI 的核心差異

1.  channels 與 operations：非同步架構，明確定義發送 (`send`) 或訂閱 (`receive`) 的主題。
2.  相容的 schema：Data model 完全沿用。
3.  多協定支援：`servers` 區塊可定義 Kafka、AMQP、MQTT 等協定。 [1, 3, 4, 5, 6]

### 🛠️ 實作建議

1.  [AsyncAPI Studio](https://studio.asyncapi.com/)：線上直接渲染視覺化文件。
2.  Microcks 網站：自動模擬 Kafka Broker，進行測試。 [1, 2, 7, 8]

[1] [https://microcks.io](https://microcks.io/documentation/tutorials/first-asyncapi-mock/)
[2] [https://microcks.io](https://microcks.io/documentation/tutorials/first-asyncapi-mock/)
[3] [https://mokapi.io](https://mokapi.io/resources/blogs/mock-api-based-on-openapi-asyncapi)
[4] [https://www.asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest)
[5] [https://medium.com](https://medium.com/@santhoshziyam/define-rest-apis-using-asyncapi-specification-a4e779ee58bf)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=28ifyPXoe-Y)
[7] [https://medium.com](https://medium.com/@jack43581996/asyncapi-%E5%85%A5%E9%96%80%E7%AD%86%E8%A8%98-122ae469b6b0)
[8] [https://www.asyncapi.com](https://www.asyncapi.com/docs/tools/generator/asyncapi-document)

</td></tr>
</table>

> [!NOTE]
> 從 [Your 1st AsyncAPI on Kafka mock](https://microcks.io/documentation/tutorials/first-asyncapi-mock/) 的說明文件內容，可以找到 PetStore 的範例 YAML [petstore-1.0.0-asyncapi.yaml](https://microcks.io/documentation/tutorials/petstore-1.0.0-asyncapi.yaml)

- 直接用線上的 [AsyncAPI Studio](https://studio.asyncapi.com/) 來看這個PetStore 的範例 YAML [petstore-1.0.0-asyncapi.yaml](https://microcks.io/documentation/tutorials/petstore-1.0.0-asyncapi.yaml)