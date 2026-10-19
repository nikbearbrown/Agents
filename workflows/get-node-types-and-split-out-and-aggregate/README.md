# get node types and split out and aggregate

This folder contains the **get node types and split out and aggregate** workflow. Its executable nodes use `aggregate`, `code`, `httpRequest`, `if`, `manualTrigger`, `n8n`, `set`, `splitOut`, `summarize`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-node-types-and-split-out-and-aggregate.json`](get-node-types-and-split-out-and-aggregate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| get node types | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| If | `if` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| extract name and latest version | `code` | Inspect parameters |
| Summarize | `summarize` | Inspect parameters |
| get all workflows | `n8n` | Inspect parameters |
| prettify output | `set` | Inspect parameters |
| instance base url | `set` | Inspect parameters |
| get single workflow | `n8n` | get |
| node names that needs update | `set` | Inspect parameters |

## Connection map

- If → node names that needs update (`main`, output 0, input 0)
- Aggregate → get all workflows (`main`, output 0, input 0)
- Split Out → If (`main`, output 0, input 0)
- Summarize → prettify output (`main`, output 0, input 0)
- get node types → extract name and latest version (`main`, output 0, input 0)
- get all workflows → get single workflow (`main`, output 0, input 0)
- instance base url → get node types (`main`, output 0, input 0)
- get single workflow → Split Out (`main`, output 0, input 0)
- node names that needs update → Summarize (`main`, output 0, input 0)
- extract name and latest version → Aggregate (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → instance base url (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0512_Splitout_Code_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0512_Splitout_Code_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
