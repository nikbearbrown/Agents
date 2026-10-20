# Blockchain DEX Screener Insights Agent

This folder contains the **Blockchain DEX Screener Insights Agent** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`blockchain-dex-screener-insights-agent.json`](blockchain-dex-screener-insights-agent.json): sanitized, inactive import copy with an overview sticky note.
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
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Blockchain DEX Screener Insights Agent | `agent` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Adds SessionId | `set` | Inspect parameters |
| DexScreener Latest Token Profiles | `toolHttpRequest` | Inspect parameters |
| DexScreener Latest Boosted Tokens | `toolHttpRequest` | Inspect parameters |
| DexScreener Top Token Boosts | `toolHttpRequest` | Inspect parameters |
| DexScreener Search Pairs | `toolHttpRequest` | Inspect parameters |
| DexScreener Check Orders Paid for Token | `toolHttpRequest` | Inspect parameters |
| DexScreener Get Pairs by Chain and Pair Address | `toolHttpRequest` | Inspect parameters |
| DexScreener Token Pools | `toolHttpRequest` | Inspect parameters |
| DexScreener Pairs by Token Address | `toolHttpRequest` | Inspect parameters |

## Connection map

- Adds SessionId → Blockchain DEX Screener Insights Agent (`main`, output 0, input 0)
- Telegram Trigger → Adds SessionId (`main`, output 0, input 0)
- OpenAI Chat Model → Blockchain DEX Screener Insights Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Blockchain DEX Screener Insights Agent (`ai_memory`, output 0, input 0)
- DexScreener Token Pools → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- DexScreener Search Pairs → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- When chat message received → Adds SessionId (`main`, output 0, input 0)
- DexScreener Top Token Boosts → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- DexScreener Latest Boosted Tokens → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- DexScreener Latest Token Profiles → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- DexScreener Pairs by Token Address → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- Blockchain DEX Screener Insights Agent → Telegram (`main`, output 0, input 0)
- DexScreener Check Orders Paid for Token → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)
- DexScreener Get Pairs by Chain and Pair Address → Blockchain DEX Screener Insights Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0340_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0340_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
