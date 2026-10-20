# Simple indexing workflow using the Google Indexing API

This folder contains the **Simple indexing workflow using the Google Indexing API** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `stopAndError`, `wait`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`simple-indexing-workflow-using-the-google-indexing-api.json`](simple-indexing-workflow-using-the-google-indexing-api.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`

**Entry nodes:** When clicking "Execute Workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| loop | `splitInBatches` | Inspect parameters |
| sitemap_set | `httpRequest` | Inspect parameters |
| sitemap_convert | `xml` | Inspect parameters |
| sitemap_parse | `splitOut` | Inspect parameters |
| url_set | `set` | Inspect parameters |
| url_index | `httpRequest` | POST |
| index_check | `if` | Inspect parameters |
| wait | `wait` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |

## Connection map

- loop → url_index (`main`, output 0, input 0)
- wait → loop (`main`, output 0, input 0)
- url_set → loop (`main`, output 0, input 0)
- url_index → index_check (`main`, output 0, input 0)
- index_check → wait (`main`, output 0, input 0)
- index_check → Stop and Error (`main`, output 1, input 0)
- sitemap_set → sitemap_convert (`main`, output 0, input 0)
- sitemap_parse → url_set (`main`, output 0, input 0)
- sitemap_convert → sitemap_parse (`main`, output 0, input 0)
- Schedule Trigger → sitemap_set (`main`, output 0, input 0)
- When clicking "Execute Workflow" → sitemap_set (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0427_Stopanderror_Wait_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0427_Stopanderror_Wait_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
