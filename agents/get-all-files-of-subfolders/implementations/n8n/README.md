# Get all files of subfolders

This folder contains the **Get all files of subfolders** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `if`, `manualTrigger`, `nextCloud`, `noOp`, `set`, `splitInBatches`, `stopAndError`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-all-files-of-subfolders.json`](get-all-files-of-subfolders.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `nextCloudApi`

**Entry nodes:** When clicking "Execute Workflow", Webhook, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Whether type is file | `if` | Inspect parameters |
| Set new path for subfolder | `set` | Inspect parameters |
| Set new path for file | `code` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Set folder-paths for from and to | `set` | Inspect parameters |
| Create to folder if necessary | `nextCloud` | folder |
| Get all folders/files in from-folder | `nextCloud` | folder / list |
| Loop over files and folders | `splitInBatches` | Inspect parameters |
| Consolidate all files and folders found | `noOp` | Inspect parameters |
| Create subfolder in to-folder | `nextCloud` | folder |
| Get all folders/files in found subfolder | `nextCloud` | folder / list |
| Whether there is are more files or subfolders found | `if` | Inspect parameters |
| Consolidate all found files | `code` | Inspect parameters |
| Loop Over all files | `splitInBatches` | Inspect parameters |
| Move file to destination | `nextCloud` | move |
| Delete from-folder | `nextCloud` | folder / delete |
| Set paths | `set` | Inspect parameters |
| Whether the request is valid | `if` | Inspect parameters |
| Stop and Error: request not valid | `stopAndError` | Inspect parameters |
| Whether the request is valid1 | `if` | Inspect parameters |
| Stop and Error: request not valid1 | `stopAndError` | Inspect parameters |

## Connection map

- Webhook → Whether the request is valid (`main`, output 0, input 0)
- Set paths → Set folder-paths for from and to (`main`, output 0, input 0)
- Loop Over all files → Delete from-folder (`main`, output 0, input 0)
- Loop Over all files → Move file to destination (`main`, output 1, input 0)
- Whether type is file → Consolidate all files and folders found (`main`, output 0, input 0)
- Whether type is file → Set new path for subfolder (`main`, output 1, input 0)
- Set new path for file → Loop Over all files (`main`, output 0, input 0)
- Execute Workflow Trigger → Whether the request is valid1 (`main`, output 0, input 0)
- Move file to destination → Loop Over all files (`main`, output 0, input 0)
- Set new path for subfolder → Create subfolder in to-folder (`main`, output 0, input 0)
- Consolidate all found files → Set new path for file (`main`, output 0, input 0)
- Loop over files and folders → Whether type is file (`main`, output 1, input 0)
- Whether the request is valid → Set folder-paths for from and to (`main`, output 0, input 0)
- Whether the request is valid → Stop and Error: request not valid (`main`, output 1, input 0)
- Create subfolder in to-folder → Get all folders/files in found subfolder (`main`, output 0, input 0)
- Create to folder if necessary → Get all folders/files in from-folder (`main`, output 0, input 0)
- Whether the request is valid1 → Set folder-paths for from and to (`main`, output 0, input 0)
- Whether the request is valid1 → Stop and Error: request not valid1 (`main`, output 1, input 0)
- Set folder-paths for from and to → Create to folder if necessary (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Set paths (`main`, output 0, input 0)
- Get all folders/files in from-folder → Loop over files and folders (`main`, output 0, input 0)
- Consolidate all files and folders found → Whether there is are more files or subfolders found (`main`, output 0, input 0)
- Get all folders/files in found subfolder → Consolidate all files and folders found (`main`, output 0, input 0)
- Whether there is are more files or subfolders found → Consolidate all found files (`main`, output 0, input 0)
- Whether there is are more files or subfolders found → Loop over files and folders (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0333_Stopanderror_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0333_Stopanderror_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
