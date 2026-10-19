# Always Authenticate Your Server!

This folder contains the **Always Authenticate Your Server!** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `mcpTrigger`, `switch`, `toolCode`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`always-authenticate-your-server-4f28d5b3.json`](always-authenticate-your-server-4f28d5b3.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When Executed by Another Workflow, SQLite MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| SQLite MCP Server | `mcpTrigger` | Inspect parameters |
| CreateRecord | `code` | Inspect parameters |
| UpdateRecord | `code` | Inspect parameters |
| ReadRecords | `code` | Inspect parameters |
| DescribeTables | `toolCode` | Inspect parameters |
| ListTables | `toolCode` | Inspect parameters |
| CreateRecords | `toolWorkflow` | Inspect parameters |
| UpdateRows | `toolWorkflow` | Inspect parameters |
| ReadRows | `toolWorkflow` | Inspect parameters |

## Connection map

- ReadRows → SQLite MCP Server (`ai_tool`, output 0, input 0)
- Operation → ReadRecords (`main`, output 0, input 0)
- Operation → CreateRecord (`main`, output 1, input 0)
- Operation → UpdateRecord (`main`, output 2, input 0)
- ListTables → SQLite MCP Server (`ai_tool`, output 0, input 0)
- UpdateRows → SQLite MCP Server (`ai_tool`, output 0, input 0)
- CreateRecords → SQLite MCP Server (`ai_tool`, output 0, input 0)
- DescribeTables → SQLite MCP Server (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → Operation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0874_Stickynote_Executeworkflow_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0874_Stickynote_Executeworkflow_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
