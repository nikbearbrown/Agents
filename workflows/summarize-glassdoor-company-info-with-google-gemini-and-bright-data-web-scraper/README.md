# Summarize Glassdoor Company Info with Google Gemini and Bright Data Web Scraper

This folder contains the **Summarize Glassdoor Company Info with Google Gemini and Bright Data Web Scraper** workflow. Its executable nodes use `chainSummarization`, `documentDefaultDataLoader`, `httpRequest`, `if`, `lmChatGoogleGemini`, `manualTrigger`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`summarize-glassdoor-company-info-with-google-gemini-and-bright-data-web-scraper.json`](summarize-glassdoor-company-info-with-google-gemini-and-bright-data-web-scraper.json): sanitized, inactive import copy with an overview sticky note.
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
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Snapshot Id | `set` | Inspect parameters |
| Check Snapshot Status | `httpRequest` | Inspect parameters |
| Download the Snapshot Response | `httpRequest` | Inspect parameters |
| Wait for 30 seconds | `wait` | Inspect parameters |
| Summarization of Glassdoor Response | `chainSummarization` | Inspect parameters |
| Configure Webhook Notification | `httpRequest` | Inspect parameters |
| HTTP Request to Glassdoor | `httpRequest` | POST |

## Connection map

- If → Download the Snapshot Response (`main`, output 0, input 0)
- If → Wait for 30 seconds (`main`, output 1, input 0)
- Set Snapshot Id → Check Snapshot Status (`main`, output 0, input 0)
- Default Data Loader → Summarization of Glassdoor Response (`ai_document`, output 0, input 0)
- Wait for 30 seconds → Check Snapshot Status (`main`, output 0, input 0)
- Check Snapshot Status → If (`main`, output 0, input 0)
- Google Gemini Chat Model → Summarization of Glassdoor Response (`ai_languageModel`, output 0, input 0)
- HTTP Request to Glassdoor → Set Snapshot Id (`main`, output 0, input 0)
- Download the Snapshot Response → Summarization of Glassdoor Response (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → HTTP Request to Glassdoor (`main`, output 0, input 0)
- Summarization of Glassdoor Response → Configure Webhook Notification (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1676_Manual_Wait_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1676_Manual_Wait_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
