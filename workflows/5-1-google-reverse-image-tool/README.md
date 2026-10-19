# 5.1 Google Reverse Image Tool

This folder contains the **5.1 Google Reverse Image Tool** workflow. Its executable nodes use `agent`, `airtable`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `openAi`, `outputParserStructured`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`5-1-google-reverse-image-tool.json`](5-1-google-reverse-image-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`, `openAiApi`, `serpApi`

**Entry nodes:** When clicking "Test workflow", Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Get Applicable Rows | `airtable` | search |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Fallback Response | `set` | Inspect parameters |
| SERP Google Reverse Image API | `httpRequest` | Inspect parameters |
| Reverse Image Search Response | `set` | Inspect parameters |
| Reverse Image Search Tool | `toolWorkflow` | Inspect parameters |
| Firecrawl Scrape API | `httpRequest` | POST |
| Scrape Success? | `if` | Inspect parameters |
| Firecrawl Scrape Success Response | `set` | Inspect parameters |
| Firecrawl scrape Error Response | `set` | Inspect parameters |
| Firecrawl Web Scaper Tool | `toolWorkflow` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Enrich Product Rows | `airtable` | update |
| Analyse Image | `openAi` | image / analyze |
| Object Identifier Agent | `agent` | Inspect parameters |
| Actions Router | `switch` | Inspect parameters |

## Connection map

- Edit Fields → Actions Router (`main`, output 0, input 0)
- Analyse Image → Object Identifier Agent (`main`, output 0, input 0)
- Actions Router → SERP Google Reverse Image API (`main`, output 0, input 0)
- Actions Router → Firecrawl Scrape API (`main`, output 1, input 0)
- Actions Router → Fallback Response (`main`, output 2, input 0)
- Scrape Success? → Firecrawl Scrape Success Response (`main`, output 0, input 0)
- Scrape Success? → Firecrawl scrape Error Response (`main`, output 1, input 0)
- OpenAI Chat Model1 → Object Identifier Agent (`ai_languageModel`, output 0, input 0)
- Get Applicable Rows → Analyse Image (`main`, output 0, input 0)
- Firecrawl Scrape API → Scrape Success? (`main`, output 0, input 0)
- Object Identifier Agent → Enrich Product Rows (`main`, output 0, input 0)
- Execute Workflow Trigger → Edit Fields (`main`, output 0, input 0)
- Structured Output Parser → Object Identifier Agent (`ai_outputParser`, output 0, input 0)
- Firecrawl Web Scaper Tool → Object Identifier Agent (`ai_tool`, output 0, input 0)
- Reverse Image Search Tool → Object Identifier Agent (`ai_tool`, output 0, input 0)
- SERP Google Reverse Image API → Reverse Image Search Response (`main`, output 0, input 0)
- When clicking "Test workflow" → Get Applicable Rows (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0531_Manual_HTTP_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0531_Manual_HTTP_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
