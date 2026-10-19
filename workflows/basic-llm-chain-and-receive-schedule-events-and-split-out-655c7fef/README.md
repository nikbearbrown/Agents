# basic llm chain and receive schedule events and split out 655c7fef

This folder contains the **basic llm chain and receive schedule events and split out 655c7fef** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `html`, `httpRequest`, `lmChatGoogleGemini`, `merge`, `scheduleTrigger`, `set`, `splitOut`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`basic-llm-chain-and-receive-schedule-events-and-split-out-655c7fef.json`](basic-llm-chain-and-receive-schedule-events-and-split-out-655c7fef.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `telegramApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| CreateYearsList | `code` | Inspect parameters |
| CleanUpYearList | `set` | Inspect parameters |
| SplitOutYearList | `splitOut` | Inspect parameters |
| GetFrontPage | `httpRequest` | Inspect parameters |
| ExtractDetails | `html` | extractHtmlContent |
| GetHeadlines | `set` | Inspect parameters |
| GetDate | `set` | Inspect parameters |
| MergeHeadlinesDate | `merge` | Inspect parameters |
| SingleJson | `aggregate` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |

## Connection map

- GetDate → MergeHeadlinesDate (`main`, output 0, input 1)
- SingleJson → Basic LLM Chain (`main`, output 0, input 0)
- GetFrontPage → ExtractDetails (`main`, output 0, input 0)
- GetHeadlines → MergeHeadlinesDate (`main`, output 0, input 0)
- ExtractDetails → GetHeadlines (`main`, output 0, input 0)
- ExtractDetails → GetDate (`main`, output 0, input 0)
- Basic LLM Chain → Telegram (`main`, output 0, input 0)
- CleanUpYearList → SplitOutYearList (`main`, output 0, input 0)
- CreateYearsList → CleanUpYearList (`main`, output 0, input 0)
- Schedule Trigger → CreateYearsList (`main`, output 0, input 0)
- SplitOutYearList → GetFrontPage (`main`, output 0, input 0)
- MergeHeadlinesDate → SingleJson (`main`, output 0, input 0)
- Google Gemini Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1490_Telegram_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1490_Telegram_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
