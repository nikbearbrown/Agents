# Clone n8n Workflows between Instances using n8n API

This folder contains the **Clone n8n Workflows between Instances using n8n API** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `manualTrigger`, `merge`, `n8n`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clone-n8n-workflows-between-instances-using-n8n-api.json`](clone-n8n-workflows-between-instances-using-n8n-api.json): sanitized, inactive import copy with an overview sticky note.
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
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| GET - Workflows | `n8n` | Inspect parameters |
| CREATE - Workflow | `n8n` | create |
| n8n - GET - Projects | `httpRequest` | Inspect parameters |
| SET Project ID | `set` | Inspect parameters |
| PUT - Workflow in Project | `httpRequest` | PUT |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| GET - Destination Workflows | `n8n` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Split Out Workflows | `splitOut` | Inspect parameters |
| Split Out Workflows1 | `splitOut` | Inspect parameters |
| Merge Workflows | `merge` | Inspect parameters |
| Split Out Projects | `splitOut` | Inspect parameters |
| Filter Project | `filter` | Inspect parameters |

## Connection map

- Code → Loop Over Items (`main`, output 0, input 0)
- Filter Project → SET Project ID (`main`, output 0, input 0)
- SET Project ID → PUT - Workflow in Project (`main`, output 0, input 0)
- GET - Workflows → Split Out Workflows (`main`, output 0, input 0)
- Loop Over Items → CREATE - Workflow (`main`, output 1, input 0)
- Merge Workflows → Code (`main`, output 0, input 0)
- CREATE - Workflow → n8n - GET - Projects (`main`, output 0, input 0)
- Split Out Projects → Filter Project (`main`, output 0, input 0)
- Split Out Workflows → Merge Workflows (`main`, output 0, input 0)
- Split Out Workflows1 → Merge Workflows (`main`, output 0, input 1)
- n8n - GET - Projects → Split Out Projects (`main`, output 0, input 0)
- PUT - Workflow in Project → Loop Over Items (`main`, output 0, input 0)
- GET - Destination Workflows → Split Out Workflows1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → GET - Workflows (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → GET - Destination Workflows (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2025_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2025_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
