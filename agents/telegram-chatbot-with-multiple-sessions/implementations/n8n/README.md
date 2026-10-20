# Telegram ChatBot with multiple sessions

This folder contains the **Telegram ChatBot with multiple sessions** workflow. Its executable nodes use `agent`, `chainLlm`, `chainSummarization`, `code`, `googleSheets`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-chatbot-with-multiple-sessions.json`](telegram-chatbot-with-multiple-sessions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Get message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Get message | `telegramTrigger` | Inspect parameters |
| Command or text? | `switch` | Inspect parameters |
| Get session | `googleSheets` | Inspect parameters |
| Disable previous session | `googleSheets` | update |
| Set new session | `googleSheets` | append |
| Session activated | `telegram` | Inspect parameters |
| Send response | `telegram` | Inspect parameters |
| Update database | `googleSheets` | append |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Get message1 | `set` | Inspect parameters |
| Set to expire | `googleSheets` | update |
| Exist? | `if` | Inspect parameters |
| OK | `telegram` | Inspect parameters |
| KO | `telegram` | Inspect parameters |
| Trim resume | `code` | Inspect parameters |
| Get session1 | `googleSheets` | Inspect parameters |
| Prompt + Resume | `code` | Inspect parameters |
| Send summary | `telegram` | Inspect parameters |
| Get message2 | `set` | Inspect parameters |
| Trim question | `code` | Inspect parameters |
| Set new current session | `googleSheets` | update |
| Response + Text | `googleSheets` | Inspect parameters |
| fullText | `code` | Inspect parameters |
| Send answer | `telegram` | Inspect parameters |
| Send current session | `telegram` | Inspect parameters |
| Telegram Chatbot | `agent` | Inspect parameters |

## Connection map

- Exist? → KO (`main`, output 0, input 0)
- Exist? → OK (`main`, output 1, input 0)
- fullText → Basic LLM Chain (`main`, output 0, input 0)
- Get message → Get session (`main`, output 0, input 0)
- Get session → Command or text? (`main`, output 0, input 0)
- Trim resume → Set to expire (`main`, output 0, input 0)
- Get message1 → Trim resume (`main`, output 0, input 0)
- Get message2 → Trim question (`main`, output 0, input 0)
- Get session1 → Prompt + Resume (`main`, output 0, input 0)
- Send response → Update database (`main`, output 0, input 0)
- Set to expire → Set new current session (`main`, output 0, input 0)
- Simple Memory → Telegram Chatbot (`ai_memory`, output 0, input 0)
- Trim question → Response + Text (`main`, output 0, input 0)
- Basic LLM Chain → Send answer (`main`, output 0, input 0)
- Prompt + Resume → Summarization Chain (`main`, output 0, input 0)
- Response + Text → fullText (`main`, output 0, input 0)
- Set new session → Session activated (`main`, output 0, input 0)
- Command or text? → Disable previous session (`main`, output 0, input 0)
- Command or text? → Send current session (`main`, output 1, input 0)
- Command or text? → Get message1 (`main`, output 2, input 0)
- Command or text? → Get session1 (`main`, output 3, input 0)
- Command or text? → Get message2 (`main`, output 4, input 0)
- Command or text? → Telegram Chatbot (`main`, output 5, input 0)
- Telegram Chatbot → Send response (`main`, output 0, input 0)
- OpenAI Chat Model → Telegram Chatbot (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Summarization Chain (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Summarization Chain → Send summary (`main`, output 0, input 0)
- Set new current session → Exist? (`main`, output 0, input 0)
- Disable previous session → Set new session (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1244_Telegram_GoogleSheets_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1244_Telegram_GoogleSheets_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
