# Wait for file do be processed

This folder contains the **Wait for file do be processed** workflow. Its executable nodes use `dropbox`, `executeWorkflowTrigger`, `httpRequest`, `manualTrigger`, `merge`, `set`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`wait-for-file-do-be-processed.json`](wait-for-file-do-be-processed.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropboxOAuth2Api`, `httpCustomAuth`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Create Asset | `httpRequest` | POST |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Adobe API Query | `set` | Inspect parameters |
| Load a test pdf file | `dropbox` | download |
| Query + File | `merge` | Inspect parameters |
| Query + File + Asset information | `merge` | Inspect parameters |
| Process Query | `httpRequest` | POST |
| Wait 5 second | `wait` | Inspect parameters |
| Try to download the result | `httpRequest` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Forward response to origin workflow | `set` | Inspect parameters |
| Authenticartion (get token) | `httpRequest` | POST |
| Upload PDF File (asset) | `httpRequest` | PUT |

## Connection map

- Switch → Wait 5 second (`main`, output 0, input 0)
- Switch → Forward response to origin workflow (`main`, output 1, input 0)
- Switch → Forward response to origin workflow (`main`, output 2, input 0)
- Create Asset → Query + File + Asset information (`main`, output 0, input 1)
- Query + File → Authenticartion (get token) (`main`, output 0, input 0)
- Query + File → Query + File + Asset information (`main`, output 0, input 0)
- Process Query → Wait 5 second (`main`, output 0, input 0)
- Wait 5 second → Try to download the result (`main`, output 0, input 0)
- Adobe API Query → Query + File (`main`, output 0, input 0)
- Load a test pdf file → Query + File (`main`, output 0, input 1)
- Upload PDF File (asset) → Process Query (`main`, output 0, input 0)
- Execute Workflow Trigger → Authenticartion (get token) (`main`, output 0, input 0)
- Execute Workflow Trigger → Query + File + Asset information (`main`, output 0, input 0)
- Try to download the result → Switch (`main`, output 0, input 0)
- Authenticartion (get token) → Create Asset (`main`, output 0, input 0)
- Query + File + Asset information → Upload PDF File (asset) (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Load a test pdf file (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Adobe API Query (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0582_Wait_Dropbox_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0582_Wait_Dropbox_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
