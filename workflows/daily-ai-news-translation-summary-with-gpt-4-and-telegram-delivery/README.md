# Daily AI News Translation & Summary with GPT-4 and Telegram Delivery

This folder contains the **Daily AI News Translation & Summary with GPT-4 and Telegram Delivery** workflow. Its executable nodes use `agent`, `httpRequest`, `lmChatOpenAi`, `merge`, `scheduleTrigger`, `set`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`daily-ai-news-translation-summary-with-gpt-4-and-telegram-delivery.json`](daily-ai-news-translation-summary-with-gpt-4-and-telegram-delivery.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Trigger at 8am daily

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Trigger at 8am daily | `scheduleTrigger` | Inspect parameters |
| Fetch GNews articles | `httpRequest` | Inspect parameters |
| Fetch NewsAPI articles | `httpRequest` | Inspect parameters |
| GNews: Map to articles | `set` | Inspect parameters |
| NewsAPI: Map to articles | `set` | Inspect parameters |
| Merge GNews & NewsAPI | `merge` | Inspect parameters |
| AI summarizer & translator | `agent` | Inspect parameters |
| GPT-4.1 Model | `lmChatOpenAi` | Inspect parameters |
| Send summary to Telegram | `telegram` | Inspect parameters |

## Connection map

- GPT-4.1 Model → AI summarizer & translator (`ai_languageModel`, output 0, input 0)
- Fetch GNews articles → GNews: Map to articles (`main`, output 0, input 0)
- Trigger at 8am daily → Fetch GNews articles (`main`, output 0, input 0)
- Trigger at 8am daily → Fetch NewsAPI articles (`main`, output 0, input 0)
- Merge GNews & NewsAPI → AI summarizer & translator (`main`, output 0, input 0)
- Fetch NewsAPI articles → NewsAPI: Map to articles (`main`, output 0, input 0)
- GNews: Map to articles → Merge GNews & NewsAPI (`main`, output 0, input 0)
- NewsAPI: Map to articles → Merge GNews & NewsAPI (`main`, output 0, input 1)
- AI summarizer & translator → Send summary to Telegram (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0970_HTTP_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0970_HTTP_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
