# Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini

This folder contains the **Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `googleSheets`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `markdown`, `outputParserStructured`, `set`, `splitOut`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`vision-based-ai-agent-scraper-with-google-sheets-scrapingbee-and-gemini.json`](vision-based-ai-agent-scraper-with-google-sheets-scrapingbee-and-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `googlePalmApi`

**Entry nodes:** When clicking ‘Test workflow’, HTML-Scraping Tool

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| ScrapingBee- Get page HTML | `httpRequest` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Google Sheets - Get list of URLs | `googleSheets` | Inspect parameters |
| Set fields | `set` | Inspect parameters |
| ScrapingBee - Get page screenshot | `httpRequest` | Inspect parameters |
| HTML-based Scraping Tool | `toolWorkflow` | Inspect parameters |
| Google Sheets - Create Rows | `googleSheets` | append |
| Vision-based Scraping Agent | `agent` | Inspect parameters |
| HTML-Scraping Tool | `executeWorkflowTrigger` | Inspect parameters |
| Set fields - from AI agent query | `set` | Inspect parameters |
| HTML to Markdown | `markdown` | Inspect parameters |

## Connection map

- Split Out → Google Sheets - Create Rows (`main`, output 0, input 0)
- Set fields → ScrapingBee - Get page screenshot (`main`, output 0, input 0)
- HTML-Scraping Tool → Set fields - from AI agent query (`main`, output 0, input 0)
- Google Gemini Chat Model → Vision-based Scraping Agent (`ai_languageModel`, output 0, input 0)
- HTML-based Scraping Tool → Vision-based Scraping Agent (`ai_tool`, output 0, input 0)
- Structured Output Parser → Vision-based Scraping Agent (`ai_outputParser`, output 0, input 0)
- ScrapingBee- Get page HTML → HTML to Markdown (`main`, output 0, input 0)
- Vision-based Scraping Agent → Split Out (`main`, output 0, input 0)
- Google Sheets - Get list of URLs → Set fields (`main`, output 0, input 0)
- Set fields - from AI agent query → ScrapingBee- Get page HTML (`main`, output 0, input 0)
- ScrapingBee - Get page screenshot → Vision-based Scraping Agent (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Google Sheets - Get list of URLs (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2041_Splitout_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2041_Splitout_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
