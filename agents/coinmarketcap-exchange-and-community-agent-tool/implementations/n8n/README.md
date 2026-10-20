# CoinMarketCap_Exchange_and_Community_Agent_Tool

This folder contains the **CoinMarketCap_Exchange_and_Community_Agent_Tool** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`coinmarketcap-exchange-and-community-agent-tool.json`](coinmarketcap-exchange-and-community-agent-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| CoinMarketCap Exchange and Community Agent | `agent` | Inspect parameters |
| Exchange and Community Agent Brain | `lmChatOpenAi` | Inspect parameters |
| Exchange and Community Agent Memory | `memoryBufferWindow` | Inspect parameters |
| Exchange Map | `toolHttpRequest` | Inspect parameters |
| Exchange Info | `toolHttpRequest` | Inspect parameters |
| CMC 100 Index | `toolHttpRequest` | Inspect parameters |
| Fear and Greed Latest | `toolHttpRequest` | Inspect parameters |
| Exchange Assets | `toolHttpRequest` | Inspect parameters |

## Connection map

- Exchange Map → CoinMarketCap Exchange and Community Agent (`ai_tool`, output 0, input 0)
- CMC 100 Index → CoinMarketCap Exchange and Community Agent (`ai_tool`, output 0, input 0)
- Exchange Info → CoinMarketCap Exchange and Community Agent (`ai_tool`, output 0, input 0)
- Exchange Assets → CoinMarketCap Exchange and Community Agent (`ai_tool`, output 0, input 0)
- Fear and Greed Latest → CoinMarketCap Exchange and Community Agent (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → CoinMarketCap Exchange and Community Agent (`main`, output 0, input 0)
- Exchange and Community Agent Brain → CoinMarketCap Exchange and Community Agent (`ai_languageModel`, output 0, input 0)
- Exchange and Community Agent Memory → CoinMarketCap Exchange and Community Agent (`ai_memory`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1902_Stickynote_Executeworkflow_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1902_Stickynote_Executeworkflow_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
