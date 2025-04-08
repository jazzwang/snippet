# Anthropic - Claude

- Get API Key
  - https://console.anthropic.com/settings/keys

## Anthropic Prompt Generator

- https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator
- Colab
  - https://colab.research.google.com/drive/1SoAajN8CBYTl79VyTwxtxncfCWlHlyy9

## 2025-04-08

- ( 2025-04-08 12:25:52 )
- 紀錄最近針對 Databricks 可以使用 Claude 新聞的相關研究。
- 2025-03-26: [Announcing Anthropic Claude 3.7 Sonnet is natively available in Databricks](https://www.databricks.com/blog/anthropic-claude-37-sonnet-now-natively-available-databricks)
- 大致上，從 Pricing 的視角，感覺 Databricks, Amazon Bedrock, Google Vertex AI 都是 Anthropic Claude 的「二房東」。畢竟 Claude 是商用模型，因此不太可能分享給多個平台對手。就商業模式來看，應該是走類似 [`OpenRouter`](https://openrouter.ai/) 的模式。
- [Amazon Bedrock API](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock)
> Anthropic’s Claude models are now generally available through Amazon Bedrock.
  - https://aws.amazon.com/bedrock/claude/
  - https://aws.amazon.com/bedrock/pricing/
- [Vertex AI API](https://docs.anthropic.com/en/api/claude-on-vertex-ai)
> Anthropic’s Claude models are now generally available through Vertex AI.
- [OpenAI SDK compatibility (beta)](https://docs.anthropic.com/en/api/openai-sdk)
  - 原本想確認一下 Claude 是否 OpenAI API compatible，看起來應該是有。
- [Client SDKs](https://docs.anthropic.com/en/api/client-sdks)
> We provide libraries in Python and TypeScript that make it easier to work with the Anthropic API.
- 我應該只有先註冊了 Anthropic 並產生了 API Key 但並沒有綁定信用卡，所以沒辦法用。Pricing 頁面並沒有免費的額度。
  - https://www.anthropic.com/pricing#anthropic-api