# Personal Assistant MCP server

This folder contains the **Personal Assistant MCP server** workflow. Its executable nodes use `agent`, `chatTrigger`, `gmailTool`, `googleCalendarTool`, `googleSheetsTool`, `lmChatGoogleGemini`, `mcpClientTool`, `mcpTrigger`, `memoryBufferWindow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`personal-assistant-mcp-server.json`](personal-assistant-mcp-server.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`

**Entry nodes:** When chat message received, MCP Server Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| MCP Server Trigger | `mcpTrigger` | Inspect parameters |
| MCP Client | `mcpClientTool` | Inspect parameters |
| Create event | `googleCalendarTool` | Inspect parameters |
| Update event | `googleCalendarTool` | update |
| Draft email | `gmailTool` | draft |
| Personal Assistant | `agent` | Inspect parameters |
| Add new row | `googleSheetsTool` | append |
| Find row | `googleSheetsTool` | Inspect parameters |
| Update row | `googleSheetsTool` | update |
| Find emails | `gmailTool` | getAll |
| Find single event | `googleCalendarTool` | get |
| Find multiple events | `googleCalendarTool` | getAll |

## Connection map

- Find row → MCP Server Trigger (`ai_tool`, output 0, input 0)
- MCP Client → Personal Assistant (`ai_tool`, output 0, input 0)
- Update row → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Add new row → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Draft email → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Find emails → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Create event → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Update event → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Simple Memory → Personal Assistant (`ai_memory`, output 0, input 0)
- Find single event → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Find multiple events → MCP Server Trigger (`ai_tool`, output 0, input 0)
- Google Gemini Chat Model → Personal Assistant (`ai_languageModel`, output 0, input 0)
- When chat message received → Personal Assistant (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1534_Stickynote_Googlecalendartool_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1534_Stickynote_Googlecalendartool_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
