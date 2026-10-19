# [2/3] Set up medoids (2 types) for anomaly detection (crops dataset)

This folder contains the **[2/3] Set up medoids (2 types) for anomaly detection (crops dataset)** workflow. Its executable nodes use `code`, `httpRequest`, `manualTrigger`, `merge`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`2-3-set-up-medoids-2-types-for-anomaly-detection-crops-dataset.json`](2-3-set-up-medoids-2-types-for-anomaly-detection-crops-dataset.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Total Points in Collection | `httpRequest` | POST |
| Cluster Distance Matrix | `httpRequest` | POST |
| Scipy Sparse Matrix | `code` | Inspect parameters |
| Set medoid id | `httpRequest` | POST |
| Get Medoid Vector | `httpRequest` | POST |
| Prepare for Searching Threshold | `set` | Inspect parameters |
| Searching Score | `httpRequest` | POST |
| Threshold Score | `set` | Inspect parameters |
| Set medoid threshold score | `httpRequest` | POST |
| Split Out1 | `splitOut` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Textual (visual) crop descriptions | `set` | Inspect parameters |
| Embed text | `httpRequest` | POST |
| Get Medoid by Text | `httpRequest` | POST |
| Set text medoid id | `httpRequest` | POST |
| Prepare for Searching Threshold1 | `set` | Inspect parameters |
| Threshold Score1 | `set` | Inspect parameters |
| Searching Text Medoid Score | `httpRequest` | POST |
| Medoids Variables | `set` | Inspect parameters |
| Text Medoids Variables | `set` | Inspect parameters |
| Qdrant cluster variables | `set` | Inspect parameters |
| Info About Crop Clusters | `set` | Inspect parameters |
| Crop Counts | `httpRequest` | POST |
| Split Out | `splitOut` | Inspect parameters |
| Set text medoid threshold score | `httpRequest` | POST |

## Connection map

- Merge → Embed text (`main`, output 0, input 0)
- Split Out → Cluster Distance Matrix (`main`, output 0, input 0)
- Split Out → Merge (`main`, output 0, input 0)
- Embed text → Get Medoid by Text (`main`, output 0, input 0)
- Split Out1 → Merge (`main`, output 0, input 1)
- Crop Counts → Info About Crop Clusters (`main`, output 0, input 0)
- Searching Score → Threshold Score (`main`, output 0, input 0)
- Threshold Score → Set medoid threshold score (`main`, output 0, input 0)
- Threshold Score1 → Set text medoid threshold score (`main`, output 0, input 0)
- Get Medoid Vector → Prepare for Searching Threshold (`main`, output 0, input 0)
- Medoids Variables → Total Points in Collection (`main`, output 0, input 0)
- Get Medoid by Text → Set text medoid id (`main`, output 0, input 0)
- Get Medoid by Text → Prepare for Searching Threshold1 (`main`, output 0, input 0)
- Scipy Sparse Matrix → Set medoid id (`main`, output 0, input 0)
- Scipy Sparse Matrix → Get Medoid Vector (`main`, output 0, input 0)
- Text Medoids Variables → Textual (visual) crop descriptions (`main`, output 0, input 0)
- Cluster Distance Matrix → Scipy Sparse Matrix (`main`, output 0, input 0)
- Info About Crop Clusters → Split Out (`main`, output 0, input 0)
- Qdrant cluster variables → Medoids Variables (`main`, output 0, input 0)
- Qdrant cluster variables → Text Medoids Variables (`main`, output 0, input 0)
- Total Points in Collection → Crop Counts (`main`, output 0, input 0)
- Searching Text Medoid Score → Threshold Score1 (`main`, output 0, input 0)
- Prepare for Searching Threshold → Searching Score (`main`, output 0, input 0)
- Prepare for Searching Threshold1 → Searching Text Medoid Score (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Qdrant cluster variables (`main`, output 0, input 0)
- Textual (visual) crop descriptions → Split Out1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1915_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1915_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
