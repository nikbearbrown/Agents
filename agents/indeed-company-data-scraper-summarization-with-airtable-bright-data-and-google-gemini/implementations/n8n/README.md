# Indeed Company Data Scraper & Summarization with Airtable, Bright Data and Google Gemini

This folder contains the **Indeed Company Data Scraper & Summarization with Airtable, Bright Data and Google Gemini** workflow. Its executable nodes use `agent`, `airtable`, `chainLlm`, `chainSummarization`, `httpRequest`, `if`, `lmChatGoogleGemini`, `manualTrigger`, `markdown`, `set`, `splitInBatches`, `toolHttpRequest`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`indeed-company-data-scraper-summarization-with-airtable-bright-data-and-google-gemini.json`](indeed-company-data-scraper-summarization-with-airtable-bright-data-and-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googlePalmApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model For Summarization | `lmChatGoogleGemini` | Inspect parameters |
| Webhook HTTP Request | `toolHttpRequest` | POST |
| Perform Indeed Web Request | `httpRequest` | POST |
| Indeed Expert AI Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Markdown to Textual Data Extractor | `chainLlm` | Inspect parameters |
| Convert Markdown to HTML | `markdown` | Inspect parameters |
| Initiate a Webhook Notification for Markdown to HTML Response | `httpRequest` | Inspect parameters |
| Set Bright Data Zone | `set` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Airtable | `airtable` | search |
| If Link field is not empty | `if` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Indeed Summarizer | `chainSummarization` | Inspect parameters |
| Google Gemini Chat Model for AI Agent | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Wait → If Link field is not empty (`main`, output 0, input 0)
- Airtable → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Wait (`main`, output 1, input 0)
- Indeed Summarizer → Indeed Expert AI Agent (`main`, output 0, input 0)
- Set Bright Data Zone → Airtable (`main`, output 0, input 0)
- Webhook HTTP Request → Indeed Expert AI Agent (`ai_tool`, output 0, input 0)
- Indeed Expert AI Agent → Loop Over Items (`main`, output 0, input 0)
- Convert Markdown to HTML → Initiate a Webhook Notification for Markdown to HTML Response (`main`, output 0, input 0)
- Google Gemini Chat Model → Markdown to Textual Data Extractor (`ai_languageModel`, output 0, input 0)
- If Link field is not empty → Perform Indeed Web Request (`main`, output 0, input 0)
- Perform Indeed Web Request → Markdown to Textual Data Extractor (`main`, output 0, input 0)
- Perform Indeed Web Request → Convert Markdown to HTML (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Bright Data Zone (`main`, output 0, input 0)
- Markdown to Textual Data Extractor → Indeed Summarizer (`main`, output 0, input 0)
- Google Gemini Chat Model for AI Agent → Indeed Expert AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model For Summarization → Indeed Summarizer (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1508_Wait_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1508_Wait_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
