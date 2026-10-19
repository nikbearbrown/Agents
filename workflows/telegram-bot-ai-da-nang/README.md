# Telegram-bot AI Da Nang

This folder contains the **Telegram-bot AI Da Nang** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `googleSheets`, `lmChatOpenRouter`, `memoryBufferWindow`, `noOp`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-bot-ai-da-nang.json`](telegram-bot-ai-da-nang.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openRouterApi`, `telegramApi`

**Entry nodes:** telegramInput, n8nInput

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| SendTyping | `telegram` | sendChatAction |
| SetResponse | `set` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Schedule | `googleSheets` | Inspect parameters |
| ScheduleToMarkdown | `code` | Inspect parameters |
| ScheduleBot | `agent` | Inspect parameters |
| n8nChatSettings | `set` | Inspect parameters |
| telegramChatSettings | `set` | Inspect parameters |
| telegramInput | `telegramTrigger` | Inspect parameters |
| n8nInput | `chatTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| telegramResponse | `telegram` | Inspect parameters |
| n8nResponse | `noOp` | Inspect parameters |
| LLM | `lmChatOpenRouter` | Inspect parameters |
| Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- LLM → ScheduleBot (`ai_languageModel`, output 0, input 0)
- Memory → ScheduleBot (`ai_memory`, output 0, input 0)
- Switch → n8nResponse (`main`, output 0, input 0)
- Switch → telegramResponse (`main`, output 1, input 0)
- Schedule → ScheduleToMarkdown (`main`, output 0, input 0)
- Settings → Schedule (`main`, output 0, input 0)
- n8nInput → n8nChatSettings (`main`, output 0, input 0)
- SendTyping → telegramChatSettings (`main`, output 0, input 0)
- ScheduleBot → SetResponse (`main`, output 0, input 0)
- SetResponse → Switch (`main`, output 0, input 0)
- telegramInput → SendTyping (`main`, output 0, input 0)
- n8nChatSettings → Settings (`main`, output 0, input 0)
- ScheduleToMarkdown → ScheduleBot (`main`, output 0, input 0)
- telegramChatSettings → Settings (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1380_Telegram_Code_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1380_Telegram_Code_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
