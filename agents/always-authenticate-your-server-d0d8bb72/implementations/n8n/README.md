# Always Authenticate Your Server!

This folder contains the **Always Authenticate Your Server!** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `httpRequest`, `mcpTrigger`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`always-authenticate-your-server-d0d8bb72.json`](always-authenticate-your-server-d0d8bb72.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When Executed by Another Workflow, Apify Youtube MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| Youtube Transcripts | `toolWorkflow` | Inspect parameters |
| Youtube Search | `toolWorkflow` | Inspect parameters |
| Apify Youtube Search | `httpRequest` | Inspect parameters |
| Simplify Search Results | `set` | Inspect parameters |
| Apify Youtube Transcripts | `httpRequest` | Inspect parameters |
| Simplify Transcript Results | `set` | Inspect parameters |
| Aggregate Search Results | `aggregate` | Inspect parameters |
| Aggregate Transcript Results | `aggregate` | Inspect parameters |
| Simplify Usage Metrics | `set` | Inspect parameters |
| Get Usage Limits | `httpRequest` | Inspect parameters |
| Usage Report | `toolWorkflow` | Inspect parameters |
| Get Usage Metrics | `httpRequest` | Inspect parameters |
| Apify Youtube MCP Server | `mcpTrigger` | Inspect parameters |

## Connection map

- Operation → Apify Youtube Search (`main`, output 0, input 0)
- Operation → Apify Youtube Transcripts (`main`, output 1, input 0)
- Operation → Get Usage Metrics (`main`, output 2, input 0)
- Usage Report → Apify Youtube MCP Server (`ai_tool`, output 0, input 0)
- Youtube Search → Apify Youtube MCP Server (`ai_tool`, output 0, input 0)
- Get Usage Limits → Simplify Usage Metrics (`main`, output 0, input 0)
- Get Usage Metrics → Get Usage Limits (`main`, output 0, input 0)
- Youtube Transcripts → Apify Youtube MCP Server (`ai_tool`, output 0, input 0)
- Apify Youtube Search → Simplify Search Results (`main`, output 0, input 0)
- Simplify Search Results → Aggregate Search Results (`main`, output 0, input 0)
- Apify Youtube Transcripts → Simplify Transcript Results (`main`, output 0, input 0)
- Simplify Transcript Results → Aggregate Transcript Results (`main`, output 0, input 0)
- When Executed by Another Workflow → Operation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0878_HTTP_Aggregate_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0878_HTTP_Aggregate_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
