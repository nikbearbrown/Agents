# Very often your data is not in the right format to insert in a node. you can use the set node to fix it.

This folder contains the **Very often your data is not in the right format to insert in a node. you can use the set node to fix it.** workflow. Its executable nodes use `googleSheets`, `manualTrigger`, `n8nTrainingCustomerDatastore`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`very-often-your-data-is-not-in-the-right-format-to-insert-in-a-node-you-can-use-the-set-node-to-fix-it.json`](very-often-your-data-is-not-in-the-right-format-to-insert-in-a-node-you-can-use-the-set-node-to-fix-it.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Create or Update record in Google Sheet | `googleSheets` | upsert |
| Set - Prepare fields | `set` | Inspect parameters |
| Customer Datastore - Generate some data | `n8nTrainingCustomerDatastore` | getAllPeople |

## Connection map

- Set - Prepare fields → Create or Update record in Google Sheet (`main`, output 0, input 0)
- On clicking 'execute' → Customer Datastore - Generate some data (`main`, output 0, input 0)
- Customer Datastore - Generate some data → Set - Prepare fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0233_Manual_N8Ntrainingcustomerdatastore_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0233_Manual_N8Ntrainingcustomerdatastore_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
