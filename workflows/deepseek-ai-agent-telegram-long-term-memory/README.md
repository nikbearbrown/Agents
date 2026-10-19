# 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠

This folder contains the **🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠** workflow. Its executable nodes use `agent`, `chatTrigger`, `googleDocs`, `googleDocsTool`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `set`, `switch`, `telegram`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`deepseek-ai-agent-telegram-long-term-memory.json`](deepseek-ai-agent-telegram-long-term-memory.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Listen for Telegram Events, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check User & Chat ID | `if` | Inspect parameters |
| Error message | `telegram` | Inspect parameters |
| Listen for Telegram Events | `webhook` | Inspect parameters |
| Validation | `set` | Inspect parameters |
| Message Router | `switch` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Telegram Response | `telegram` | Inspect parameters |
| Save Long Term Memories | `googleDocsTool` | update |
| Retrieve Long Term Memories | `googleDocs` | get |
| Response Error message | `telegram` | Inspect parameters |
| DeepSeek-R1 Reasoning | `lmChatOpenAi` | Inspect parameters |
| DeepSeek-V3 Chat | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Merge → AI Agent (`main`, output 0, input 0)
- AI Agent → Telegram Response (`main`, output 0, input 0)
- AI Agent → Response Error message (`main`, output 1, input 0)
- Validation → Check User & Chat ID (`main`, output 0, input 0)
- Message Router → Merge (`main`, output 1, input 0)
- Message Router → Retrieve Long Term Memories (`main`, output 1, input 0)
- Message Router → Error message (`main`, output 3, input 0)
- DeepSeek-V3 Chat → AI Agent (`ai_languageModel`, output 0, input 0)
- Check User & Chat ID → Message Router (`main`, output 0, input 0)
- Check User & Chat ID → Error message (`main`, output 1, input 0)
- Save Long Term Memories → AI Agent (`ai_tool`, output 0, input 0)
- Listen for Telegram Events → Validation (`main`, output 0, input 0)
- Retrieve Long Term Memories → Merge (`main`, output 0, input 1)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2044_Telegram_Googledocs_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2044_Telegram_Googledocs_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
