# Coinmarketcap Price Agent

This folder contains the **Coinmarketcap Price Agent** workflow. Its executable nodes use `agent`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`coinmarketcap-price-agent.json`](coinmarketcap-price-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Send Message | `telegram` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Telegram Trigger1 | `telegramTrigger` | Inspect parameters |
| CoinMarketCap Price Agent | `agent` | Inspect parameters |
| Adds SessionId | `set` | Inspect parameters |
| CoinMarketCap Price | `toolHttpRequest` | Inspect parameters |

## Connection map

- Adds SessionId → CoinMarketCap Price Agent (`main`, output 0, input 0)
- OpenAI Chat Model → CoinMarketCap Price Agent (`ai_languageModel`, output 0, input 0)
- Telegram Trigger1 → Adds SessionId (`main`, output 0, input 0)
- CoinMarketCap Price → CoinMarketCap Price Agent (`ai_tool`, output 0, input 0)
- Window Buffer Memory → CoinMarketCap Price Agent (`ai_memory`, output 0, input 0)
- CoinMarketCap Price Agent → Telegram Send Message (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1450_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1450_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
