# Realtime Text-to-Speech and Speech-to-Text

## 2024-12-13

- 緣起：
  - Siri 帶動了語音秘書/助理的風潮
  - 曾經看過幾個 Demo，都蠻有趣的，這一個 https://demo.ultravox.ai/ 的中文表現還蠻好的。當然需要更多 Benchmark 跟測試。

### Ultravox

- https://demo.ultravox.ai/
- 公開的模型：
  - Github: https://github.com/fixie-ai/ultravox
  - huggingface: https://huggingface.co/fixie-ai/ultravox-v0_4
- 付費 API
  - https://www.ultravox.ai/

## 2024-12-15

- 2024-02-27: TTS Arena: Benchmarking Text-to-Speech Models in the Wild
  - https://huggingface.co/blog/arena-tts

## 2024-12-16

以下是根據提供的搜索結果整理的比較列表，使用 Markdown 格式：

| 模型名稱 | Git Repo | 支持語言 | 即時/串流支持 | 語音轉文字支持 | 文字轉語音支持 |
|----------|----------|----------|----------------|-----------------|-----------------|
| Ultravox | [Repo](https://github.com/fixie-ai/ultravox) | 英語、西班牙語、德語、法語、意大利語、葡萄牙語 | 是 | 是 | 是 |
| Mimic3 | [Repo](https://github.com/MycroftAI/mimic3) | 英語、西班牙語、德語、南非荷蘭語、孟加拉語、荷蘭語 | 是 | - | 是 |
| LLaMA | [Repo](https://github.com/OpenT2S/LlamaVoice) | 英語、德語、法語、意大利語、葡萄牙語、印地語、西班牙語、泰語 | 是 | 是 | 是 |
| Meta Spirit LM | [Repo](https://github.com/facebookresearch/spiritlm) | - | 是 | 是 | 是 |
| WhisperSpeech | [Repo](https://github.com/nitaiaharoni1/whisper-speech-to-text) | 英語、波蘭語 | 否 | 是 | 是 |
| Mini-Omni | [Repo](https://github.com/gpt-omni/mini-omni) | 英語 | 是 | 是 | 是 |
| MolMolAI | [Repo](https://github.com/allenai/molmo) | - | - | - | - |
| MetaVoice | [Repo](https://github.com/metavoiceio/metavoice-src) | 英語 | 是 | 是 | 是 |
| OpenVoice | [Repo](https://github.com/myshell-ai/OpenVoice) | 英語、西班牙語、法語、中文、日語、韓語 | 是 | 是 | 是 |
| XTTS | [Repo](https://github.com/coqui-ai/TTS) | 英語、西班牙語、法語、德語、意大利語、葡萄牙語、波蘭語、土耳其語、俄語、荷蘭語、捷克語、阿拉伯語、中文、日語 | 是 | 否 | 是 |
| Mozilla TTS | [Repo](https://github.com/mozilla/TTS) | 英語、西班牙語、法語、德語 | 是 | 是 | 是 |
| Coqui TTS | [Repo](https://github.com/Edresson/Coqui-TTS) | 英語、德語、法語、西班牙語、意大利語、葡萄牙語、波蘭語、土耳其語、俄語、荷蘭語、捷克語、阿拉伯語、中文、日語、匈牙利語、韓語 | 是 | 是 | 是 |
| MeloTTS | [Repo](https://github.com/myshell-ai/MeloTTS) | 英語（美國、英國、印度、澳大利亞）、西班牙語、法語、中文（混合英語）、日語、韓語 | 是 | 否 | 是 |
| Parler-TTS | [Repo](https://github.com/huggingface/parler-tts) | 英語、印地語、孟加拉語、泰米爾語、泰盧固語、馬拉地語 | 是 | 否 | 是 |
| TortoiseTTS | [Repo](https://github.com/neonbjb/tortoise-tts) | - | 否 | - | 是 |
| StyleTTS | [Repo](https://github.com/yl4579/StyleTTS2) | 英語 | 是 | - | 是 |

請注意，某些模型的資訊可能不完整，因為搜索結果中沒有提供相關數據。標記為"-"的項目表示資訊不明確或未提供。

Citations:
[1] https://github.com/meta-llama/llama/compare/main...markasoftware:llama-cpu:main
[2] https://github.com/mozilla/TTS
[3] https://github.com/fixie-ai/ultravox-client-sdk-android
[4] https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mimic-tts/mimic-3
[5] https://encord.com/blog/spirit-lm-meta-ai/
[6] https://huggingface.co/gpt-omni/mini-omni
[7] https://github.com/allenai/molmo?tab=readme-ov-file
[8] https://github.com/metavoiceio/MetaVoiceLive
[9] https://github.com/ValyrianTech/OpenVoice_server
[10] https://github.com/coqui-ai/TTS/blob/dev/docs/source/models/xtts.md
[11] https://docs.coqui.ai/en/latest/models/xtts.html
[12] https://huggingface.co/dron3flyv3r/MeloTTS-GLaDOS/blob/main/README.md
[13] https://github.com/inferless/Parler-tts-streaming
[14] https://github.com/neonbjb/tortoise-tts
[15] https://github.com/IIEleven11/StyleTTS2FineTune
[16] https://github.com/fixie-ai/ultravox
[17] https://www.ultravox.ai
[18] https://www.marktechpost.com/2024/11/13/fixie-ai-introduces-ultravox-v0-4-1-a-family-of-open-speech-models-trained-specifically-for-enabling-real-time-conversation-with-llms-and-an-open-weight-alternative-to-gpt-4o-realtime/
[19] https://zguyun.com/blog/github-open-source-ai-voice-cloning-projects/
[20] https://www.reddit.com/r/Python/comments/vnzl5y/mimic_3_released_mycrofts_privacyfocused_neural/
[21] https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mimic-tts/mimic-3
[22] https://voicebot.ai/2022/06/29/mycroft-ai-launches-mimic-3-neural-text-to-speech-platform/
[23] https://github.com/OpenT2S/LlamaVoice
[24] https://www.aimodels.fyi/models/huggingFace/llama-31-8b-instruct-meta-llama
[25] https://arxiv.org/html/2409.06666v1
[26] https://github.com/facebookresearch/spiritlm
[27] https://ai.gopubby.com/meta-spirit-lm-a-complete-guide-to-multimodal-ai-for-text-and-speech-generation-ed0af74bc950?gi=3dc33ad56ed3
[28] https://encord.com/blog/spirit-lm-meta-ai/
[29] https://github.com/nitaiaharoni1/whisper-speech-to-text
[30] https://dataloop.ai/library/model/whisperspeech_whisperspeech/
[31] https://picovoice.ai/blog/whisper-speech-to-text-for-real-time-transcription/
[32] https://www.collabora.com/news-and-blog/blog/2023/09/13/whisperspeech-exploring-new-horizons-in-text-to-speech-technology/
[33] https://huggingface.co/gpt-omni/mini-omni
[34] https://huggingface.co/gpt-omni/mini-omni/blob/main/README.md
[35] https://neurohive.io/en/state-of-the-art/mini-omni-open-source-model-for-real-time-speech-interaction/
[36] https://github.com/allenai/molmo?tab=readme-ov-file
[37] https://github.com/metavoiceio/metavoice-src
[38] https://huggingface.co/metavoiceio/metavoice-1B-v0.1/blob/main/README.md
[39] https://huggingface.co/metavoiceio/metavoice-1B-v0.1/discussions/8
[40] https://blog.unrealspeech.com/metavoice-1b/
[41] https://github.com/myshell-ai/OpenVoice
[42] https://www.segmind.com/models/openvoice
[43] https://github.com/PolyAI-LDN/pheme
[44] https://poly.ai/blog/introducing-pheme-a-new-speech-generation-model-from-polyai/
[45] https://huggingface.co/papers/2401.02839
[46] https://github.com/coqui-ai/TTS/blob/dev/docs/source/models/xtts.md
[47] https://huggingface.co/coqui/XTTS-v1
[48] https://www.baseten.co/blog/streaming-real-time-text-to-speech-with-xtts-v2/
[49] https://github.com/mozilla/TTS
[50] https://www.restack.io/p/voice-synthesis-answer-mozilla-tts-cat-ai
[51] https://www.restack.io/p/mozilla-tts-python-answer
[52] https://rasa.com/blog/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/
[53] https://github.com/Edresson/Coqui-TTS
[54] https://docs.coqui.ai/en/dev/models/xtts.html
[55] https://zaka.ai/real-time-voice-imitation-clone-any-voice-with-aistep-by-step-guide/
[56] https://cran.r-project.org/web/packages/text2speech/vignettes/coqui-tts.html
[57] https://ulife.ai/stories/complete-guide-to-text-to-speech-with-coqui-tts
[58] https://github.com/myshell-ai/MeloTTS
[59] https://www.makayis.co/melotts-your-multi-lingual-text-to-speech-solution/
[60] https://github.com/huggingface/parler-tts
[61] https://www.marktechpost.com/2024/12/06/ai4bharat-and-hugging-face-released-indic-parler-tts-a-multimodal-text-to-speech-technology-for-multilingual-inclusivity-and-bridging-indias-linguistic-digital-divide/
[62] https://github.com/inferless/Parler-tts-streaming
[63] https://github.com/neonbjb/tortoise-tts
[64] https://github.com/neonbjb/tortoise-tts/discussions/605
[65] https://docs.coqui.ai/en/latest/models/tortoise.html
[66] https://github.com/yl4579/StyleTTS
[67] https://modal.com/blog/open-source-tts

## 2025-05-30

- Read from https://www.linkedin.com/feed/update/urn:li:activity:7333847125232914433/
  - 語音Demo：https://resemble-ai.github.io/chatterbox_demopage/
  - Github 專案：https://github.com/resemble-ai/chatterbox
