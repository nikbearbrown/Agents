# Always Authenticate Your Server!

This folder contains the **Always Authenticate Your Server!** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `httpRequest`, `if`, `mcpTrigger`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`always-authenticate-your-server-db28c8ed.json`](always-authenticate-your-server-db28c8ed.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** When Executed by Another Workflow, Paycaptain MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| Paycaptain MCP Server | `mcpTrigger` | Inspect parameters |
| Update Employee | `toolWorkflow` | Inspect parameters |
| Get Employee | `toolWorkflow` | Inspect parameters |
| Get Employees | `httpRequest` | Inspect parameters |
| Search Employees | `toolWorkflow` | Inspect parameters |
| Log Call | `googleSheets` | append |
| Filter Matches | `filter` | Inspect parameters |
| Aggregate Search Results | `aggregate` | Inspect parameters |
| Get Employees1 | `httpRequest` | Inspect parameters |
| Filter Matching ID | `filter` | Inspect parameters |
| Strip Sensitive Fields1 | `set` | Inspect parameters |
| Strip Sensitive Fields | `set` | Inspect parameters |
| Update Employee1 | `httpRequest` | POST |
| Valid Fields Only | `set` | Inspect parameters |
| Has Valid Request? | `if` | Inspect parameters |
| Get Error Response | `set` | Inspect parameters |
| Get Success Response | `set` | Inspect parameters |
| Aggregate Get Response | `aggregate` | Inspect parameters |

## Connection map

- Log Call → Operation (`main`, output 0, input 0)
- Operation → Get Employees (`main`, output 0, input 0)
- Operation → Get Employees1 (`main`, output 1, input 0)
- Operation → Valid Fields Only (`main`, output 2, input 0)
- Get Employee → Paycaptain MCP Server (`ai_tool`, output 0, input 0)
- Get Employees → Filter Matches (`main`, output 0, input 0)
- Filter Matches → Strip Sensitive Fields (`main`, output 0, input 0)
- Get Employees1 → Filter Matching ID (`main`, output 0, input 0)
- Update Employee → Paycaptain MCP Server (`ai_tool`, output 0, input 0)
- Search Employees → Paycaptain MCP Server (`ai_tool`, output 0, input 0)
- Update Employee1 → Get Success Response (`main`, output 0, input 0)
- Valid Fields Only → Has Valid Request? (`main`, output 0, input 0)
- Filter Matching ID → Strip Sensitive Fields1 (`main`, output 0, input 0)
- Has Valid Request? → Update Employee1 (`main`, output 0, input 0)
- Has Valid Request? → Get Error Response (`main`, output 1, input 0)
- Strip Sensitive Fields → Aggregate Search Results (`main`, output 0, input 0)
- Strip Sensitive Fields1 → Aggregate Get Response (`main`, output 0, input 0)
- When Executed by Another Workflow → Log Call (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0879_Filter_HTTP_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0879_Filter_HTTP_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
