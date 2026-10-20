# n8napi-check-workflow-which-model-is-using

This folder contains the **n8napi-check-workflow-which-model-is-using** workflow. Its executable nodes use `filter`, `googleSheets`, `manualTrigger`, `n8n`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8napi-check-workflow-which-model-is-using.json`](n8napi-check-workflow-which-model-is-using.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Edit Fields-set_model_data | `set` | Inspect parameters |
| Google Sheets-Clear Sheet Data | `googleSheets` | clear |
| n8n-get all workflow | `n8n` | Inspect parameters |
| Filter-get workflow contain modelid | `filter` | Inspect parameters |
| Split Out-nodes | `splitOut` | Inspect parameters |
| Filter-node contain modelId | `filter` | Inspect parameters |
| Google Sheets-Save node and workflow data | `googleSheets` | append |

## Connection map

- Loop Over Items → Split Out-nodes (`main`, output 1, input 0)
- Split Out-nodes → Filter-node contain modelId (`main`, output 0, input 0)
- n8n-get all workflow → Filter-get workflow contain modelid (`main`, output 0, input 0)
- n8n-get all workflow → Google Sheets-Clear Sheet Data (`main`, output 0, input 0)
- Edit Fields-set_model_data → Google Sheets-Save node and workflow data (`main`, output 0, input 0)
- Filter-node contain modelId → Edit Fields-set_model_data (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → n8n-get all workflow (`main`, output 0, input 0)
- Filter-get workflow contain modelid → Loop Over Items (`main`, output 0, input 0)
- Google Sheets-Save node and workflow data → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1499_Splitout_Filter_Monitor_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1499_Splitout_Filter_Monitor_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
