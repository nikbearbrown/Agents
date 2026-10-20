# fetch source image and split out results only and filter score 0 9

This folder contains the **fetch source image and split out results only and filter score 0 9** workflow. Its executable nodes use `editImage`, `elasticsearch`, `filter`, `httpRequest`, `manualTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-source-image-and-split-out-results-only-and-filter-score-0-9.json`](fetch-source-image-and-split-out-results-only-and-filter-score-0-9.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `cloudflareApi`, `elasticsearchApi`, `httpQueryAuth`

**Entry nodes:** When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Fetch Source Image | `httpRequest` | Inspect parameters |
| Split Out Results Only | `splitOut` | Inspect parameters |
| Filter Score >= 0.9 | `filter` | Inspect parameters |
| Crop Object From Image | `editImage` | crop |
| Set Variables | `set` | Inspect parameters |
| Use Detr-Resnet-50 Object Classification | `httpRequest` | POST |
| Upload to Cloudinary | `httpRequest` | POST |
| Create Docs In Elasticsearch | `elasticsearch` | create |
| Fetch Source Image Again | `httpRequest` | Inspect parameters |

## Connection map

- Set Variables → Fetch Source Image (`main`, output 0, input 0)
- Fetch Source Image → Use Detr-Resnet-50 Object Classification (`main`, output 0, input 0)
- Filter Score >= 0.9 → Fetch Source Image Again (`main`, output 0, input 0)
- Upload to Cloudinary → Create Docs In Elasticsearch (`main`, output 0, input 0)
- Crop Object From Image → Upload to Cloudinary (`main`, output 0, input 0)
- Split Out Results Only → Filter Score >= 0.9 (`main`, output 0, input 0)
- Fetch Source Image Again → Crop Object From Image (`main`, output 0, input 0)
- When clicking "Test workflow" → Set Variables (`main`, output 0, input 0)
- Use Detr-Resnet-50 Object Classification → Split Out Results Only (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1425_Splitout_Elasticsearch_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1425_Splitout_Elasticsearch_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
