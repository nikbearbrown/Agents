# Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool

This folder contains the **Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `markdown`, `outputParserStructured`, `set`, `splitInBatches`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`enrich-company-data-from-google-sheet-with-openai-agent-and-scraper-tool.json`](enrich-company-data-from-google-sheet-with-openai-agent-and-scraper-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `openAiApi`

**Entry nodes:** Tool called from Agent, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Get rows from Google Sheet | `googleSheets` | Inspect parameters |
| Call n8n workflow  : Scrape companies homepage content | `toolWorkflow` | Inspect parameters |
| Update Company's Row on Google Sheet | `googleSheets` | update |
| ScrapingBee : Scrape company's homepage data  | `httpRequest` | Inspect parameters |
| Tool called from Agent | `executeWorkflowTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Set company url | `set` | Inspect parameters |
| HTML to Markdown | `markdown` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Webhook → Get rows from Google Sheet (`main`, output 0, input 0)
- AI Agent → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Update Company's Row on Google Sheet (`main`, output 0, input 0)
- Loop Over Items → AI Agent (`main`, output 1, input 0)
- Set company url → ScrapingBee : Scrape company's homepage data  (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Tool called from Agent → Set company url (`main`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Get rows from Google Sheet → Loop Over Items (`main`, output 0, input 0)
- ScrapingBee : Scrape company's homepage data  → HTML to Markdown (`main`, output 0, input 0)
- Call n8n workflow  : Scrape companies homepage content → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1694_Webhook_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1694_Webhook_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
