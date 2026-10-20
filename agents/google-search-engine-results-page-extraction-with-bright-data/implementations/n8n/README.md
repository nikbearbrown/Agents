# Google Search Engine Results Page Extraction with Bright Data

This folder contains the **Google Search Engine Results Page Extraction with Bright Data** workflow. Its executable nodes use `agent`, `chainSummarization`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `set`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-search-engine-results-page-extraction-with-bright-data.json`](google-search-engine-results-page-extraction-with-bright-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Google Gemini Chat Model For Summarization | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Webhook HTTP Request | `toolHttpRequest` | POST |
| Google Search Data Extractor | `informationExtractor` | Inspect parameters |
| Perform Google Search Request | `httpRequest` | POST |
| Google Search Expert AI Agent | `agent` | Inspect parameters |
| Set Google Search Query | `set` | Inspect parameters |

## Connection map

- Summarization Chain → Google Search Expert AI Agent (`main`, output 0, input 0)
- Webhook HTTP Request → Google Search Expert AI Agent (`ai_tool`, output 0, input 0)
- Set Google Search Query → Perform Google Search Request (`main`, output 0, input 0)
- Google Gemini Chat Model → Google Search Data Extractor (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model1 → Google Search Expert AI Agent (`ai_languageModel`, output 0, input 0)
- Google Search Data Extractor → Summarization Chain (`main`, output 0, input 0)
- Perform Google Search Request → Google Search Data Extractor (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Google Search Query (`main`, output 0, input 0)
- Google Gemini Chat Model For Summarization → Summarization Chain (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1467_Manual_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1467_Manual_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
