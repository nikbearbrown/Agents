# Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent

This folder contains the **Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent** workflow. Its executable nodes use `agent`, `function`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `mcpClient`, `mcpClientTool`, `memoryBufferWindow`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-web-data-with-bright-data-google-gemini-and-mcp-automated-ai-agent.json`](scrape-web-data-with-bright-data-google-gemini-and-mcp-automated-ai-agent.json): sanitized, inactive import copy with an overview sticky note.
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
| AI Agent | `agent` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| MCP Client list all tools for Bright Data | `mcpClient` | Inspect parameters |
| MCP Client List all tools | `mcpClientTool` | Inspect parameters |
| MCP Client Bright Data Web Scraper | `mcpClient` | executeTool |
| Webhook for web scraper | `httpRequest` | Inspect parameters |
| Set the URLs | `set` | Inspect parameters |
| MCP Client to Scrape as Markdown | `mcpClientTool` | executeTool |
| MCP Client to Scrape as HTML | `mcpClientTool` | executeTool |
| Google Gemini Chat Model for AI Agent | `lmChatGoogleGemini` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Webhook for Web Scraper AI Agent | `httpRequest` | Inspect parameters |
| Set the URL with the Webhook URL and data format | `set` | Inspect parameters |
| Create a binary data | `function` | Inspect parameters |
| Write the scraped content to disk | `readWriteFile` | write |

## Connection map

- AI Agent → Webhook for Web Scraper AI Agent (`main`, output 0, input 0)
- AI Agent → Create a binary data (`main`, output 0, input 0)
- Set the URLs → MCP Client Bright Data Web Scraper (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Create a binary data → Write the scraped content to disk (`main`, output 0, input 0)
- MCP Client List all tools → AI Agent (`ai_tool`, output 0, input 0)
- MCP Client to Scrape as HTML → AI Agent (`ai_tool`, output 0, input 0)
- MCP Client to Scrape as Markdown → AI Agent (`ai_tool`, output 0, input 0)
- When clicking ‘Test workflow’ → MCP Client list all tools for Bright Data (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set the URL with the Webhook URL and data format (`main`, output 0, input 0)
- MCP Client Bright Data Web Scraper → Webhook for web scraper (`main`, output 0, input 0)
- Google Gemini Chat Model for AI Agent → AI Agent (`ai_languageModel`, output 0, input 0)
- MCP Client list all tools for Bright Data → Set the URLs (`main`, output 0, input 0)
- Set the URL with the Webhook URL and data format → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1707_Manual_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1707_Manual_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
