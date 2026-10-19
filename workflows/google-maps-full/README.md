# Google Maps FULL

This folder contains the **Google Maps FULL** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `executeWorkflowTrigger`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `toolSerpApi`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-maps-full.json`](google-maps-full.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `serpApi`

**Entry nodes:** Trigger - When User Sends Message, Trigger - On Subworkflow Start

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Trigger - When User Sends Message | `chatTrigger` | Inspect parameters |
| AI Agent - Lead Collection | `agent` | Inspect parameters |
| GPT-4o - Generate & Process Requests | `lmChatOpenAi` | Inspect parameters |
| Memory - Track Recent Context | `memoryBufferWindow` | Inspect parameters |
| Tool - Scrape Google Maps Business Data | `toolWorkflow` | Inspect parameters |
| Fallback - Enrich with Google Search | `toolSerpApi` | Inspect parameters |
| Tool - Crawl Business Website | `toolWorkflow` | Inspect parameters |
| Trigger - On Subworkflow Start | `executeWorkflowTrigger` | Inspect parameters |
| Scrape Google Maps (via Apify) | `httpRequest` | POST |
| Save Extracted Data to Google Sheets | `googleSheets` | append |
| Aggregate Business Listings | `aggregate` | Inspect parameters |
| Scrape Website Content (via Apify) | `httpRequest` | POST |
| Save Website Data to Google Sheets | `googleSheets` | append |
| Aggregate Website Content | `aggregate` | Inspect parameters |

## Connection map

- Memory - Track Recent Context → AI Agent - Lead Collection (`ai_memory`, output 0, input 0)
- Tool - Crawl Business Website → AI Agent - Lead Collection (`ai_tool`, output 0, input 0)
- Scrape Google Maps (via Apify) → Save Extracted Data to Google Sheets (`main`, output 0, input 0)
- Trigger - On Subworkflow Start → Scrape Google Maps (via Apify) (`main`, output 0, input 0)
- Trigger - When User Sends Message → AI Agent - Lead Collection (`main`, output 0, input 0)
- Save Website Data to Google Sheets → Aggregate Website Content (`main`, output 0, input 0)
- Scrape Website Content (via Apify) → Save Website Data to Google Sheets (`main`, output 0, input 0)
- Fallback - Enrich with Google Search → AI Agent - Lead Collection (`ai_tool`, output 0, input 0)
- GPT-4o - Generate & Process Requests → AI Agent - Lead Collection (`ai_languageModel`, output 0, input 0)
- Save Extracted Data to Google Sheets → Aggregate Business Listings (`main`, output 0, input 0)
- Tool - Scrape Google Maps Business Data → AI Agent - Lead Collection (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1964_HTTP_Aggregate_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1964_HTTP_Aggregate_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
