# 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram

This folder contains the **🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `googleDocs`, `googleDocsTool`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `set`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-agent-chatbot-long-term-memory-note-storage-telegram.json`](ai-agent-chatbot-long-term-memory-note-storage-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Chat Response | `set` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Save Long Term Memories | `googleDocsTool` | update |
| Retrieve Long Term Memories | `googleDocs` | get |
| Telegram Response | `telegram` | Inspect parameters |
| DeepSeek-V3 Chat | `lmChatOpenAi` | Inspect parameters |
| AI Tools Agent | `agent` | Inspect parameters |
| Save Notes | `googleDocsTool` | update |
| Retrieve Notes | `googleDocs` | get |
| Aggregate | `aggregate` | Inspect parameters |
| Merge | `merge` | Inspect parameters |

## Connection map

- Merge → Aggregate (`main`, output 0, input 0)
- Aggregate → AI Tools Agent (`main`, output 0, input 0)
- Save Notes → AI Tools Agent (`ai_tool`, output 0, input 0)
- gpt-4o-mini → AI Tools Agent (`ai_languageModel`, output 0, input 0)
- AI Tools Agent → Telegram Response (`main`, output 0, input 0)
- AI Tools Agent → Chat Response (`main`, output 0, input 0)
- Retrieve Notes → Merge (`main`, output 0, input 1)
- Window Buffer Memory → AI Tools Agent (`ai_memory`, output 0, input 0)
- Save Long Term Memories → AI Tools Agent (`ai_tool`, output 0, input 0)
- When chat message received → Retrieve Long Term Memories (`main`, output 0, input 0)
- When chat message received → Retrieve Notes (`main`, output 0, input 0)
- Retrieve Long Term Memories → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2053_Telegram_Googledocs_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2053_Telegram_Googledocs_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
