# MCP Client with Brave and Telegram

This folder contains the **MCP Client with Brave and Telegram** workflow. Its executable nodes use `code`, `if`, `mcpClient`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mcp-client-with-brave-and-telegram.json`](mcp-client-with-brave-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mcpClientApi`, `telegramApi`

**Entry nodes:** Get Message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| List Brave Tools | `mcpClient` | Inspect parameters |
| Exec Brave tool | `mcpClient` | executeTool |
| Clean query | `code` | Inspect parameters |
| Send message | `telegram` | Inspect parameters |
| Get Message | `telegramTrigger` | Inspect parameters |
| Search with Brave? | `if` | Inspect parameters |
| Get Text | `set` | Inspect parameters |

## Connection map

- Get Text → Clean query (`main`, output 0, input 0)
- Clean query → List Brave Tools (`main`, output 0, input 0)
- Get Message → Search with Brave? (`main`, output 0, input 0)
- Exec Brave tool → Send message (`main`, output 0, input 0)
- List Brave Tools → Exec Brave tool (`main`, output 0, input 0)
- Search with Brave? → Get Text (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1001_Telegram_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1001_Telegram_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
