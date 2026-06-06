# mcpvault

- Git Repo
  - https://github.com/bitbonsai/mcpvault
- Website
  - https://mcpvault.org
  
## 2026-06-06

- 緣起：因為[研究別人怎麼用 Obsidian 當第二大腦](https://github.com/mathruffian-dot/claude-code-lazy-packs/blob/master/03-%E5%BB%BA%E7%AB%8B%E7%AC%AC%E4%BA%8C%E5%A4%A7%E8%85%A6-Obsidian.md)。所以看一下範例 Agent Skill.md 裡寫到的 Obsidian 的 MCP Server。
- 研究：
  - 支援跟 OpenCode 整合
  > **OpenCode** \- Copy this to `~/.config/opencode/opencode.json`
  > ```json
  >  {
  >  "mcp": {
  >      "obsidian": {
  >      "type": "local",
  >      "command": \[
  >          "npx",
  >          "@bitbonsai/mcpvault@latest",
  >          "/path/to/your/vault/"
  >      \],
  >      "enabled": true
  >      }
  >  }
  >  }
  >  ```
  >
  >  Replace `/path/to/your/vault` with your actual Obsidian vault path.