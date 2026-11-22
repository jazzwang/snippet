# Hermes Agent vs Grok Bot: Agent Memory Design Comparison

## 🔹 Hermes Agent Memory Architecture

### Four-Layer Design (四層結構設計)

```mermaid
graph TD
    L0[<b>L0 — Working Context (Session)</b><br/>• System prompt + injected memory<br/>• 會話內有效，凍結快照] --> L1
    L1[<b>L1 — Persistent Memory</b><br/>• MEMORY.md (2200 chars, ~800 tokens)<br/>• USER.md (1375 chars, ~500 tokens)<br/>• Stored in ~/.hermes/memories/] --> L15
    L15[<b>L1.5 — External Memory Plugins</b><br/>• Only 1 external Provider allowed<br/>• Examples: RetainDB, ByteRover, Honcho<br/>• Built-in memory always active] --> L2
    L2[<b>L2 — Session Search</b><br/>• SQLite FTS5 + LLM Summary<br/>• Cross-session retrieval]
    
    style L0 fill:#f9f,stroke:#333
    style L1 fill:#ff9,stroke:#333
    style L15 fill:#9cf,stroke:#333
    style L2 fill:#9f9,stroke:#333
```

### Core Features (核心特點)
- **File-Centric**: `MEMORY.md` (environment facts, learned content) and `USER.md` (user preferences) are core memory carriers
- **SQLite FTS5**: Full-text search across sessions with Lineage tracking (parent/child session tracking)
- **Session Snapshot**: Memory snapshot frozen at session start to avoid injecting unstable info in real-time
- **External Provider Limit**: Only 1 external Provider can be active simultaneously to avoid conflicts

---

## 🔹 Grok Bot Memory Architecture

### Bot-Centric Persistent Design

```mermaid
graph TD
    Bot[<b>Bot Instance</b><br/>• Independent memory & filesystem<br/>• Includes Routines (recurring tasks)<br/>• Session logs + preferences] --> MemoryRecords
    MemoryRecords[<b>Memory Records (Protobuf Schema)</b><br/>• scope + scope_key + folder<br/>• profile + logs map<br/>• versioned, timestamped]
    
    subgraph SharedComputer [<b>Shared Computer (One Cloud Machine)</b><br/>• All Bots share same cloud machine<br/>• Shared tools & execution environment]
        Computer1[Bot A]
        Computer2[Bot B]
        Computer3[Bot C]
    end
    
    subgraph Vault [<b>Vault Isolation</b><br/>• Secrets not stored in memory<br/>• Credentials & cards stored in Vault]
    
    style Bot fill:#f96,stroke:#333
    style SharedComputer fill:#9cf,stroke:#333
    style Vault fill:#ff9,stroke:#333
```

### Core Features (核心特點)
- **Bot as Unit**: Each Bot has independent memory, name, Avatar, title, and session records
- **Shared Computer**: All Bots share one cloud machine providing tools and execution environment
- **Protobuf Schema**: Memory records are structured with version control and timestamps
- **Autonomous Memory Management**: Bot decides what to remember; users can also ask it to remember/forget
- **Vault Isolation**: Sensitive data (logins, cards) not stored in memory, kept in Vault

---

## 📊 Key Differences Comparison

| Aspect | Hermes Agent | Grok Bot |
|--------|-------------|----------|
| **Memory Unit** | Files (MEMORY.md/USER.md) | Bot Instance |
| **Persistence Location** | Local ~/.hermes/ or custom path | Cloud machine |
| **Retrieval Mechanism** | SQLite FTS5 + Session search | Protobuf Schema + Gateway |
| **External Provider** | Supports 1 external Provider | Built-in, not open |
| **Model Switching** | Free LLM switching | Grok only |
| **Deployment** | Custom (Docker/SSH/local) | Cloud managed service |
| **Memory Visibility** | Editable files | Structured records |
| **Cross-Session** | L2 session search | Shared computer memory |

---

## 🎯 Design Philosophy Differences

### Hermes
- **File-Centric**: Emphasizes transparency, editability, and local self-hosting
- Users can directly read/edit memory files
- Supports plugin ecosystem (RetainDB, ByteRover, Supermemory, etc.)
- Suitable for users needing transparent control and self-management

### Grok Bot
- **Bot-Centric**: Emphasizes structured data and cloud management
- Each Bot is an independent entity with identity (name, avatar, title)
- Memory is structured and versioned, suitable for API integration
- Suitable for enterprise-grade, centralized management, and cloud collaboration scenarios

---

## 🏁 Conclusion

Both Hermes and Grok implement "memory" but with fundamentally different architectures:
- **Hermes** uses **files + SQLite FTS5** for session persistence
- **Grok** uses **Protobuf + cloud machine** for Bot identity persistence

The difference is most evident in:
1. **Control**: Hermes = local & transparent; Grok = managed & abstracted
2. **Flexibility**: Hermes = plugin ecosystem; Grok = built-in & unified
3. **Use Case**: Hermes = individual power users; Grok = enterprise teams
