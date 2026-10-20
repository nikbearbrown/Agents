# [1/3 - anomaly detection] [1/2 - KNN classification] Batch upload dataset to Qdrant (crops dataset)

This folder contains the **[1/3 - anomaly detection] [1/2 - KNN classification] Batch upload dataset to Qdrant (crops dataset)** workflow. Its executable nodes use `code`, `filter`, `googleCloudStorage`, `httpRequest`, `if`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`1-3-anomaly-detection-1-2-knn-classification-batch-upload-dataset-to-qdrant-crops-dataset.json`](1-3-anomaly-detection-1-2-knn-classification-batch-upload-dataset-to-qdrant-crops-dataset.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCloudStorageOAuth2Api`, `httpHeaderAuth`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Cloud Storage | `googleCloudStorage` | object |
| Get fields for Qdrant | `set` | Inspect parameters |
| Qdrant cluster variables | `set` | Inspect parameters |
| Embed crop image | `httpRequest` | POST |
| Create Qdrant Collection | `httpRequest` | PUT |
| Check Qdrant Collection Existence | `httpRequest` | Inspect parameters |
| Batches in the API's format | `set` | Inspect parameters |
| Batch Upload to Qdrant | `httpRequest` | PUT |
| Split in batches, generate uuids for Qdrant points | `code` | Inspect parameters |
| If collection exists | `if` | Inspect parameters |
| Payload index on crop_name | `httpRequest` | PUT |
| Filtering out tomato to test anomalies | `filter` | Inspect parameters |

## Connection map

- Embed crop image → Batch Upload to Qdrant (`main`, output 0, input 0)
- Google Cloud Storage → Get fields for Qdrant (`main`, output 0, input 0)
- If collection exists → Google Cloud Storage (`main`, output 0, input 0)
- If collection exists → Create Qdrant Collection (`main`, output 1, input 0)
- Get fields for Qdrant → Filtering out tomato to test anomalies (`main`, output 0, input 0)
- Create Qdrant Collection → Payload index on crop_name (`main`, output 0, input 0)
- Qdrant cluster variables → Check Qdrant Collection Existence (`main`, output 0, input 0)
- Payload index on crop_name → Google Cloud Storage (`main`, output 0, input 0)
- Batches in the API's format → Embed crop image (`main`, output 0, input 0)
- Check Qdrant Collection Existence → If collection exists (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Qdrant cluster variables (`main`, output 0, input 0)
- Filtering out tomato to test anomalies → Split in batches, generate uuids for Qdrant points (`main`, output 0, input 0)
- Split in batches, generate uuids for Qdrant points → Batches in the API's format (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1728_Code_Filter_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1728_Code_Filter_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
