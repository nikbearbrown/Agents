# http request and filter

This folder contains the **http request and filter** workflow. Its executable nodes use `filter`, `httpRequest`, `if`, `manualTrigger`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-filter.json`](http-request-and-filter.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set Loop | `set` | Inspect parameters |
| If | `if` | Inspect parameters |
| User ID | `set` | Inspect parameters |
| Collections | `httpRequest` | Inspect parameters |
| Loop Discount | `set` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Select Collection | `filter` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Get Articles | `httpRequest` | Inspect parameters |
| Merge 100+ | `merge` | Inspect parameters |

## Connection map

- If → Get Articles (`main`, output 0, input 0)
- If → Loop Discount (`main`, output 0, input 0)
- Filter → Edit Fields (`main`, output 0, input 0)
- User ID → Collections (`main`, output 0, input 0)
- Set Loop → If (`main`, output 0, input 0)
- Merge 100+ → Filter (`main`, output 0, input 0)
- Collections → Select Collection (`main`, output 0, input 0)
- Get Articles → Merge 100+ (`main`, output 0, input 0)
- Loop Discount → If (`main`, output 0, input 0)
- Select Collection → Set Loop (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → User ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0589_Manual_Filter_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0589_Manual_Filter_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
