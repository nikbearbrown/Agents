# [3/3] Anomaly detection tool (crops dataset)

This folder contains the **[3/3] Anomaly detection tool (crops dataset)** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `httpRequest`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`3-3-anomaly-detection-tool-crops-dataset.json`](3-3-anomaly-detection-tool-crops-dataset.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `qdrantApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embed image | `httpRequest` | POST |
| Get similarity of medoids | `httpRequest` | POST |
| Compare scores | `code` | Inspect parameters |
| Variables for medoids | `set` | Inspect parameters |
| Info About Crop Labeled Clusters | `set` | Inspect parameters |
| Total Points in Collection | `httpRequest` | POST |
| Each Crop Counts | `httpRequest` | POST |
| Image URL hardcode | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |

## Connection map

- Embed image → Get similarity of medoids (`main`, output 0, input 0)
- Each Crop Counts → Info About Crop Labeled Clusters (`main`, output 0, input 0)
- Image URL hardcode → Variables for medoids (`main`, output 0, input 0)
- Variables for medoids → Total Points in Collection (`main`, output 0, input 0)
- Execute Workflow Trigger → Image URL hardcode (`main`, output 0, input 0)
- Get similarity of medoids → Compare scores (`main`, output 0, input 0)
- Total Points in Collection → Each Crop Counts (`main`, output 0, input 0)
- Info About Crop Labeled Clusters → Embed image (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1462_HTTP_Executeworkflow_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1462_HTTP_Executeworkflow_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
