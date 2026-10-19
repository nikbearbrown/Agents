# Get Google Search Results (SERPs) for SEO Research

This folder contains the **Get Google Search Results (SERPs) for SEO Research** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `manualTrigger`, `noOp`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-google-search-results-serps-for-seo-research.json`](get-google-search-results-serps-for-seo-research.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `httpQueryAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| SERP results | `set` | Inspect parameters |
| Separate | `splitOut` | Inspect parameters |
| Title <> Empty | `filter` | Inspect parameters |
| Assign SERP #pos | `code` | Inspect parameters |
| GET SERP | `httpRequest` | POST |
| Connect to your own database -  | `noOp` | Inspect parameters |
| Set Keywords to get SERPs for | `set` | Inspect parameters |
| Connect to your own database2 | `noOp` | Inspect parameters |
| Assign SearchQuery | `set` | Inspect parameters |
| Split out Keywords | `splitOut` | Inspect parameters |

## Connection map

- GET SERP → SERP results (`main`, output 0, input 0)
- Separate → Title <> Empty (`main`, output 0, input 0)
- SERP results → Separate (`main`, output 0, input 0)
- Title <> Empty → Assign SearchQuery (`main`, output 0, input 0)
- Assign SERP #pos → Connect to your own database2 (`main`, output 0, input 0)
- Assign SearchQuery → Assign SERP #pos (`main`, output 0, input 0)
- Split out Keywords → GET SERP (`main`, output 0, input 0)
- Set Keywords to get SERPs for → Split out Keywords (`main`, output 0, input 0)
- Connect to your own database -  → Set Keywords to get SERPs for (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Connect to your own database -  (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0608_Splitout_Code_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0608_Splitout_Code_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
