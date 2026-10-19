# LinkedIn Web Scraping with Bright Data MCP Server & Google Gemini

This folder contains the **LinkedIn Web Scraping with Bright Data MCP Server & Google Gemini** workflow. Its executable nodes use `aggregate`, `code`, `function`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `mcpClient`, `merge`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-web-scraping-with-bright-data-mcp-server-google-gemini.json`](linkedin-web-scraping-with-bright-data-mcp-server-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `mcpClientApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set the URLs | `set` | Inspect parameters |
| Bright Data MCP Client For LinkedIn Person | `mcpClient` | executeTool |
| List all tools for Bright Data | `mcpClient` | Inspect parameters |
| Bright Data MCP Client For LinkedIn Company | `mcpClient` | executeTool |
| Set the LinkedIn Company URL | `set` | Inspect parameters |
| Webhook for LinkedIn Company Web Scraper | `httpRequest` | Inspect parameters |
| LinkedIn Data Extractor | `informationExtractor` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| List all available tools for Bright Data | `mcpClient` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Create a binary data for LinkedIn person info extract | `function` | Inspect parameters |
| Write the LinkedIn person info to disk | `readWriteFile` | write |
| Create a binary data for LinkedIn company info extract | `function` | Inspect parameters |
| Write the LinkedIn company info to disk | `readWriteFile` | write |
| Webhook for LinkedIn Person Web Scraper | `httpRequest` | Inspect parameters |

## Connection map

- Code → Merge (`main`, output 0, input 0)
- Merge → Aggregate (`main`, output 0, input 0)
- Aggregate → Webhook for LinkedIn Company Web Scraper (`main`, output 0, input 0)
- Aggregate → Create a binary data for LinkedIn company info extract (`main`, output 0, input 0)
- Set the URLs → Bright Data MCP Client For LinkedIn Person (`main`, output 0, input 0)
- LinkedIn Data Extractor → Merge (`main`, output 0, input 1)
- Google Gemini Chat Model → LinkedIn Data Extractor (`ai_languageModel`, output 0, input 0)
- Set the LinkedIn Company URL → Bright Data MCP Client For LinkedIn Company (`main`, output 0, input 0)
- List all tools for Bright Data → Set the LinkedIn Company URL (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → List all available tools for Bright Data (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → List all tools for Bright Data (`main`, output 0, input 0)
- List all available tools for Bright Data → Set the URLs (`main`, output 0, input 0)
- Bright Data MCP Client For LinkedIn Person → Webhook for LinkedIn Person Web Scraper (`main`, output 0, input 0)
- Bright Data MCP Client For LinkedIn Person → Create a binary data for LinkedIn person info extract (`main`, output 0, input 0)
- Bright Data MCP Client For LinkedIn Company → Code (`main`, output 0, input 0)
- Bright Data MCP Client For LinkedIn Company → LinkedIn Data Extractor (`main`, output 0, input 0)
- Create a binary data for LinkedIn person info extract → Write the LinkedIn person info to disk (`main`, output 0, input 0)
- Create a binary data for LinkedIn company info extract → Write the LinkedIn company info to disk (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1402_Code_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1402_Code_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
