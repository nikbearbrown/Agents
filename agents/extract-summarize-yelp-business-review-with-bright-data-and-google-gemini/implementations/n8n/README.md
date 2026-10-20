# Extract & Summarize Yelp Business Review with Bright Data and Google Gemini

This folder contains the **Extract & Summarize Yelp Business Review with Bright Data and Google Gemini** workflow. Its executable nodes use `chainLlm`, `chainSummarization`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `merge`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-summarize-yelp-business-review-with-bright-data-and-google-gemini.json`](extract-summarize-yelp-business-review-with-bright-data-and-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
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
| Set Yelp URL with the Bright Data Zone | `set` | Inspect parameters |
| HTTP Request to fetch the Yelp Business Reviews | `httpRequest` | POST |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Webhook Notifier for the merged response | `httpRequest` | Inspect parameters |
| Google Gemini Chat Model for Summarization | `lmChatGoogleGemini` | Inspect parameters |
| Structured Data Extractor | `chainLlm` | Inspect parameters |

## Connection map

- Merge → Webhook Notifier for the merged response (`main`, output 0, input 0)
- Summarization Chain → Merge (`main`, output 0, input 1)
- Google Gemini Chat Model → Structured Data Extractor (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Structured Data Extractor (`ai_outputParser`, output 0, input 0)
- Structured Data Extractor → Summarization Chain (`main`, output 0, input 0)
- Structured Data Extractor → Merge (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Yelp URL with the Bright Data Zone (`main`, output 0, input 0)
- Set Yelp URL with the Bright Data Zone → HTTP Request to fetch the Yelp Business Reviews (`main`, output 0, input 0)
- Google Gemini Chat Model for Summarization → Summarization Chain (`ai_languageModel`, output 0, input 0)
- HTTP Request to fetch the Yelp Business Reviews → Structured Data Extractor (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1821_Manual_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1821_Manual_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
