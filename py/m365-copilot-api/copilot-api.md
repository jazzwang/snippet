# copilot-api

- Git Repo
  - https://github.com/OEvortex/copilot-api
- PyPI
  - https://pypi.org/project/copilot-api

## 2026-07-07

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Microsoft 365 Copilot - GPT-5
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
Are there python library to interact with M365 Copilot via websocket?
</td></tr><tr><td>A:</td><td>

## Python Library to interact with M365 Copilot via `websocket`

Short answer: **No official Python library currently exposes Microsoft 365 Copilot through a WebSocket chat interface.** Instead, Microsoft provides **REST-based Microsoft 365 Copilot APIs** and Python SDKs for them. [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/sdks/api-libraries), [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-overview)

### Official Python options

Microsoft's official Python SDKs are:
```bash
pip install microsoft-agents-m365copilot
```
or
```bash
pip install microsoft-agents-m365copilot-beta
```
These SDKs are part of the Microsoft 365 Copilot APIs and support Python. [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/sdks/api-libraries), [github.com](https://github.com/microsoft/Agents-M365Copilot/blob/main/python/README.md)

The SDKs work over HTTP/REST with Microsoft authentication, not WebSocket connections. [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/sdks/api-libraries), [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-overview)

### If you need streaming responses

There are a few possibilities:

1.  **Use Copilot APIs + HTTP streaming** (if the specific API supports it).
2.  **Build your own WebSocket gateway**:
        -   Python WebSocket server (`fastapi`, `websockets`)
        -   Backend calls Microsoft 365 Copilot APIs
        -   Stream results to clients over WebSocket

Architecture:
```
Browser/Web App
      |
   WebSocket
      |
Python Backend
      |
Microsoft 365 Copilot API
      |
  Microsoft 365 Data
```

### Unofficial libraries

There are community packages such as:
```bash
pip install copilot-api
```
which claim Microsoft Copilot integration and streaming support. However, they are **not Microsoft-supported**, may break without notice, and may not work with Microsoft 365 Copilot enterprise scenarios. [pypi.org](https://pypi.org/project/copilot-api/)

### Recommendation

For production and enterprise use:

-   Use **Microsoft 365 Copilot APIs**
-   Use the official SDK **`microsoft-agents-m365copilot`**
-   Implement WebSocket only in your own application layer if real-time browser communication is required. [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/sdks/api-libraries), [github.com](https://github.com/microsoft/Agents-M365Copilot/blob/main/python/README.md)

If your goal is specifically **"chat with M365 Copilot and receive tokens incrementally like OpenAI/Realtime APIs"**, I can show the current SDK pattern and whether the latest Copilot APIs expose streaming responses.
</td></tr>
</table>
