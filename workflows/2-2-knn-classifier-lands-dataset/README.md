# [2/2] KNN classifier (lands dataset)

This folder contains the **[2/2] KNN classifier (lands dataset)** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `httpRequest`, `if`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`2-2-knn-classifier-lands-dataset.json`](2-2-knn-classifier-lands-dataset.json): sanitized, inactive import copy with an overview sticky note.
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
| Query Qdrant | `httpRequest` | POST |
| Majority Vote | `code` | Inspect parameters |
| Increase limitKNN | `set` | Inspect parameters |
| Propagate loop variables | `set` | Inspect parameters |
| Image Test URL | `set` | Inspect parameters |
| Return class | `set` | Inspect parameters |
| Check tie | `if` | Inspect parameters |
| Qdrant variables + embedding + KNN neigbours | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |

## Connection map

- Check tie → Increase limitKNN (`main`, output 0, input 0)
- Check tie → Return class (`main`, output 1, input 0)
- Embed image → Qdrant variables + embedding + KNN neigbours (`main`, output 0, input 0)
- Query Qdrant → Propagate loop variables (`main`, output 0, input 0)
- Majority Vote → Check tie (`main`, output 0, input 0)
- Image Test URL → Embed image (`main`, output 0, input 0)
- Increase limitKNN → Query Qdrant (`main`, output 0, input 0)
- Execute Workflow Trigger → Image Test URL (`main`, output 0, input 0)
- Propagate loop variables → Majority Vote (`main`, output 0, input 0)
- Qdrant variables + embedding + KNN neigbours → Query Qdrant (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1730_HTTP_Executeworkflow_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1730_HTTP_Executeworkflow_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
