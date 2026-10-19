# Discord MCP Server

This folder contains the **Discord MCP Server** workflow. Its executable nodes use `discordTool`, `httpRequestTool`, `mcpTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`discord-mcp-server.json`](discord-mcp-server.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`

**Entry nodes:** Discord MCP Server Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Send Discord Message to Channel | `discordTool` | message |
| Add Role To Member | `discordTool` | member / roleAdd |
| Remove Role from member | `discordTool` | member / roleRemove |
| Discord MCP Server Trigger | `mcpTrigger` | Inspect parameters |
| Get channels of server by server ID | `discordTool` | getAll |
| Get members of server by server ID | `discordTool` | member |
| Send DM and Wait for reply | `discordTool` | message / sendAndWait |
| Send to Channel and Wait for Reply | `discordTool` | message / sendAndWait |
| Send DM to User | `discordTool` | message |
| Get Discord Server IDs | `httpRequestTool` | Inspect parameters |

## Connection map

- Send DM to User → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Add Role To Member → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Get Discord Server IDs → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Remove Role from member → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Send DM and Wait for reply → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Send Discord Message to Channel → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Get members of server by server ID → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Send to Channel and Wait for Reply → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)
- Get channels of server by server ID → Discord MCP Server Trigger (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Discordtool/1913_Discordtool_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Discordtool/1913_Discordtool_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
