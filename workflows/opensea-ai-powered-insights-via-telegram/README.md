# OpenSea AI-Powered Insights via Telegram

This folder contains the **OpenSea AI-Powered Insights via Telegram** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`opensea-ai-powered-insights-via-telegram.json`](opensea-ai-powered-insights-via-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** When chat message received, Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Adds SessionId | `set` | Inspect parameters |
| Opensea Supervisor Brain | `lmChatOpenAi` | Inspect parameters |
| Opensea Supervisor Memory | `memoryBufferWindow` | Inspect parameters |
| OpenSea Analytics Agent Tool | `toolWorkflow` | Inspect parameters |
| OpenSea NFT Agent Tool | `toolWorkflow` | Inspect parameters |
| OpenSea Marketplace Agent Tool | `toolWorkflow` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| OpenSea AI-Powered Insights Agent | `agent` | Inspect parameters |

## Connection map

- Adds SessionId → OpenSea AI-Powered Insights Agent (`main`, output 0, input 0)
- Telegram Trigger → Adds SessionId (`main`, output 0, input 0)
- OpenSea NFT Agent Tool → OpenSea AI-Powered Insights Agent (`ai_tool`, output 0, input 0)
- Opensea Supervisor Brain → OpenSea AI-Powered Insights Agent (`ai_languageModel`, output 0, input 0)
- Opensea Supervisor Memory → OpenSea AI-Powered Insights Agent (`ai_memory`, output 0, input 0)
- When chat message received → OpenSea AI-Powered Insights Agent (`main`, output 0, input 0)
- OpenSea Analytics Agent Tool → OpenSea AI-Powered Insights Agent (`ai_tool`, output 0, input 0)
- OpenSea Marketplace Agent Tool → OpenSea AI-Powered Insights Agent (`ai_tool`, output 0, input 0)
- OpenSea AI-Powered Insights Agent → Telegram (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2004_Telegram_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2004_Telegram_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
