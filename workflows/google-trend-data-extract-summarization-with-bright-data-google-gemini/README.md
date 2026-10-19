# Google Trend Data Extract, Summarization with Bright Data & Google Gemini

This folder contains the **Google Trend Data Extract, Summarization with Bright Data & Google Gemini** workflow. Its executable nodes use `chainLlm`, `chainSummarization`, `function`, `gmail`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-trend-data-extract-summarization-with-bright-data-google-gemini.json`](google-trend-data-extract-summarization-with-bright-data-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Markdown to Textual Data Extractor | `chainLlm` | Inspect parameters |
| Set URL and Bright Data Zone | `set` | Inspect parameters |
| Initiate a Webhook Notification for Markdown to Textual Data Extraction | `httpRequest` | Inspect parameters |
| Google Gemini Chat Model for Data Extract | `lmChatGoogleGemini` | Inspect parameters |
| Perform Bright Data Web Request | `httpRequest` | POST |
| Create a binary data | `function` | Inspect parameters |
| Structured Data Extractor | `informationExtractor` | Inspect parameters |
| Summarize Google Trends | `chainSummarization` | Inspect parameters |
| Initiate a Webhook Notification for Summarization | `httpRequest` | Inspect parameters |
| Write the file to disk | `readWriteFile` | write |
| Google Gemini Chat Model for Summarization | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model for Structured Data Extract | `lmChatGoogleGemini` | Inspect parameters |
| Send Summary to Gmail | `gmail` | Inspect parameters |

## Connection map

- Create a binary data → Write the file to disk (`main`, output 0, input 0)
- Summarize Google Trends → Initiate a Webhook Notification for Summarization (`main`, output 0, input 0)
- Summarize Google Trends → Send Summary to Gmail (`main`, output 0, input 0)
- Structured Data Extractor → Create a binary data (`main`, output 0, input 0)
- Structured Data Extractor → Summarize Google Trends (`main`, output 0, input 0)
- Set URL and Bright Data Zone → Perform Bright Data Web Request (`main`, output 0, input 0)
- Perform Bright Data Web Request → Markdown to Textual Data Extractor (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set URL and Bright Data Zone (`main`, output 0, input 0)
- Markdown to Textual Data Extractor → Initiate a Webhook Notification for Markdown to Textual Data Extraction (`main`, output 0, input 0)
- Markdown to Textual Data Extractor → Structured Data Extractor (`main`, output 0, input 0)
- Google Gemini Chat Model for Data Extract → Markdown to Textual Data Extractor (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model for Summarization → Summarize Google Trends (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model for Structured Data Extract → Structured Data Extractor (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1235_Manual_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1235_Manual_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
