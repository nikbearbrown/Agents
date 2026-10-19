# Always Authenticate Your Server!

This folder contains the **Always Authenticate Your Server!** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `github`, `httpRequest`, `mcpTrigger`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`always-authenticate-your-server-865df2b4.json`](always-authenticate-your-server-865df2b4.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`

**Entry nodes:** When Executed by Another Workflow, Github MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| Github MCP Server | `mcpTrigger` | Inspect parameters |
| Get Latest Issues | `toolWorkflow` | Inspect parameters |
| Add Issue Comment | `toolWorkflow` | Inspect parameters |
| Simplify Issues | `set` | Inspect parameters |
| Aggregate Results | `aggregate` | Inspect parameters |
| Get Issue Comments | `toolWorkflow` | Inspect parameters |
| Get Comments | `httpRequest` | Inspect parameters |
| Simplify Comments | `set` | Inspect parameters |
| Aggregate Comments | `aggregate` | Inspect parameters |
| Get Many Issues | `github` | repository |
| Get Single Issue | `github` | get |
| Create Comment | `github` | createComment |
| Get Response | `set` | Inspect parameters |

## Connection map

- Operation → Get Many Issues (`main`, output 0, input 0)
- Operation → Get Single Issue (`main`, output 1, input 0)
- Operation → Create Comment (`main`, output 2, input 0)
- Get Comments → Simplify Comments (`main`, output 0, input 0)
- Create Comment → Get Response (`main`, output 0, input 0)
- Get Many Issues → Simplify Issues (`main`, output 0, input 0)
- Simplify Issues → Aggregate Results (`main`, output 0, input 0)
- Get Single Issue → Get Comments (`main`, output 0, input 0)
- Add Issue Comment → Github MCP Server (`ai_tool`, output 0, input 0)
- Get Latest Issues → Github MCP Server (`ai_tool`, output 0, input 0)
- Simplify Comments → Aggregate Comments (`main`, output 0, input 0)
- Get Issue Comments → Github MCP Server (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → Operation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/0876_GitHub_Aggregate_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/0876_GitHub_Aggregate_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
