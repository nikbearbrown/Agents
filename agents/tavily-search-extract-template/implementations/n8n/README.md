# 🔍🛠️ Tavily Search & Extract - Template

This folder contains the **🔍🛠️ Tavily Search & Extract - Template** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `httpRequest`, `lmChatOpenAi`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`tavily-search-extract-template.json`](tavily-search-extract-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Provide search topic via Chat window

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Tavily Search | `httpRequest` | POST |
| Tavily Extract | `httpRequest` | POST |
| Get Top Result | `set` | Inspect parameters |
| Tavily Extract Top Search | `httpRequest` | POST |
| Filter > 90% | `set` | Inspect parameters |
| Tavily Search Topic | `httpRequest` | POST |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Summarize Web Page Content | `chainLlm` | Inspect parameters |
| Tavily API Key | `set` | Inspect parameters |
| Provide search topic via Chat window | `chatTrigger` | Inspect parameters |

## Connection map

- Filter > 90% → Get Top Result (`main`, output 0, input 0)
- Get Top Result → Tavily Extract Top Search (`main`, output 0, input 0)
- Tavily API Key → Tavily Search Topic (`main`, output 0, input 0)
- OpenAI Chat Model → Summarize Web Page Content (`ai_languageModel`, output 0, input 0)
- Tavily Search Topic → Filter > 90% (`main`, output 0, input 0)
- Tavily Extract Top Search → Summarize Web Page Content (`main`, output 0, input 0)
- Provide search topic via Chat window → Tavily API Key (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1617_HTTP_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1617_HTTP_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
