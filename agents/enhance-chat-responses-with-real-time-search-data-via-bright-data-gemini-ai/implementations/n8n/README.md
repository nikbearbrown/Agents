# Enhance Chat Responses with Real-Time Search Data via Bright Data & Gemini AI

This folder contains the **Enhance Chat Responses with Real-Time Search Data via Bright Data & Gemini AI** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatGoogleGemini`, `manualTrigger`, `mcpClient`, `mcpClientTool`, `memoryBufferWindow`, `set`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`enhance-chat-responses-with-real-time-search-data-via-bright-data-gemini-ai.json`](enhance-chat-responses-with-real-time-search-data-via-bright-data-gemini-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `mcpClientApi`

**Entry nodes:** When chat message received, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| MCP Client list all tools for Bright Data | `mcpClient` | Inspect parameters |
| MCP Client Bright Data Search Tool | `mcpClient` | executeTool |
| Set search query | `set` | Inspect parameters |
| Google Search Engine for Bright Data | `mcpClientTool` | executeTool |
| Bing Search Engine for Bright Data | `mcpClientTool` | executeTool |
| MCP Client List all tools | `mcpClientTool` | Inspect parameters |
| HTTP Request for Webhook Notification | `toolHttpRequest` | POST |
| Yandex Search Engine for Bright Data | `mcpClientTool` | executeTool |

## Connection map

- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Set search query → MCP Client Bright Data Search Tool (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- MCP Client List all tools → AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → MCP Client list all tools for Bright Data (`main`, output 0, input 0)
- Bing Search Engine for Bright Data → AI Agent (`ai_tool`, output 0, input 0)
- Google Search Engine for Bright Data → AI Agent (`ai_tool`, output 0, input 0)
- Yandex Search Engine for Bright Data → AI Agent (`ai_tool`, output 0, input 0)
- HTTP Request for Webhook Notification → AI Agent (`ai_tool`, output 0, input 0)
- MCP Client list all tools for Bright Data → Set search query (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1183_Manual_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1183_Manual_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
