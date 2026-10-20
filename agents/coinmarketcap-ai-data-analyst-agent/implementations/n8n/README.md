# CoinMarketCap_AI_Data_Analyst_Agent

This folder contains the **CoinMarketCap_AI_Data_Analyst_Agent** workflow. Its executable nodes use `agent`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`coinmarketcap-ai-data-analyst-agent.json`](coinmarketcap-ai-data-analyst-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Input

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Send Message | `telegram` | Inspect parameters |
| Adds SessionId | `set` | Inspect parameters |
| CoinMarketCap AI Data Analyst Agent | `agent` | Inspect parameters |
| CoinMarketCap Agent Brain | `lmChatOpenAi` | Inspect parameters |
| CoinMarketCap Memory | `memoryBufferWindow` | Inspect parameters |
| CoinMarketCap Crypto Agent Tool | `toolWorkflow` | Inspect parameters |
| CoinMarketCap Exchange and Community Agent Tool | `toolWorkflow` | Inspect parameters |
| CoinMarketCap DEXScan Agent Tool | `toolWorkflow` | Inspect parameters |
| Telegram Input | `telegramTrigger` | Inspect parameters |

## Connection map

- Adds SessionId → CoinMarketCap AI Data Analyst Agent (`main`, output 0, input 0)
- Telegram Input → Adds SessionId (`main`, output 0, input 0)
- CoinMarketCap Memory → CoinMarketCap AI Data Analyst Agent (`ai_memory`, output 0, input 0)
- CoinMarketCap Agent Brain → CoinMarketCap AI Data Analyst Agent (`ai_languageModel`, output 0, input 0)
- CoinMarketCap Crypto Agent Tool → CoinMarketCap AI Data Analyst Agent (`ai_tool`, output 0, input 0)
- CoinMarketCap DEXScan Agent Tool → CoinMarketCap AI Data Analyst Agent (`ai_tool`, output 0, input 0)
- CoinMarketCap AI Data Analyst Agent → Telegram Send Message (`main`, output 0, input 0)
- CoinMarketCap Exchange and Community Agent Tool → CoinMarketCap AI Data Analyst Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1916_Telegram_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1916_Telegram_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
