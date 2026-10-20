# Way 1 - We call the subworklow for each file in the specified folder

This folder contains the **Way 1 - We call the subworklow for each file in the specified folder** workflow. Its executable nodes use `dropbox`, `executeWorkflow`, `merge`, `nocoDb`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`way-1-we-call-the-subworklow-for-each-file-in-the-specified-folder.json`](way-1-we-call-the-subworklow-for-each-file-in-the-specified-folder.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropboxOAuth2Api`, `nocoDbApiToken`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Dropbox - List watched folder | `dropbox` | folder / list |
| Switch File vs Folder | `switch` | Inspect parameters |
| Switch File vs Folder1 | `switch` | Inspect parameters |
| NocoDB - Get know files to exclude | `nocoDb` | getAll |
| Merge - Keep only new items | `merge` | Inspect parameters |
| Just a quick answer to Dropbox - webhook validation | `respondToWebhook` | Inspect parameters |
| Respond to Dropbox in less than 10sec | `respondToWebhook` | Inspect parameters |
| Dropbox get files | `dropbox` | folder / list |
| NocoDB - Add this file in the table | `nocoDb` | create |
| set_folder A | `set` | Inspect parameters |
| set_folder to watch B | `set` | Inspect parameters |
| Execute Workflow - what i want to do for this folder/file A | `executeWorkflow` | Inspect parameters |
| Execute Workflow - Something to do for new files | `executeWorkflow` | Inspect parameters |

## Connection map

- Webhook → Respond to Dropbox in less than 10sec (`main`, output 0, input 0)
- Webhook → Just a quick answer to Dropbox - webhook validation (`main`, output 1, input 0)
- set_folder A → Dropbox get files (`main`, output 0, input 0)
- Dropbox get files → Switch File vs Folder1 (`main`, output 0, input 0)
- Switch File vs Folder → Merge - Keep only new items (`main`, output 0, input 0)
- set_folder to watch B → Dropbox - List watched folder (`main`, output 0, input 0)
- set_folder to watch B → NocoDB - Get know files to exclude (`main`, output 0, input 0)
- Switch File vs Folder1 → Execute Workflow - what i want to do for this folder/file A (`main`, output 0, input 0)
- Merge - Keep only new items → NocoDB - Add this file in the table (`main`, output 0, input 0)
- Dropbox - List watched folder → Switch File vs Folder (`main`, output 0, input 0)
- NocoDB - Get know files to exclude → Merge - Keep only new items (`main`, output 0, input 1)
- NocoDB - Add this file in the table → Execute Workflow - Something to do for new files (`main`, output 0, input 0)
- Respond to Dropbox in less than 10sec → set_folder A (`main`, output 0, input 0)
- Respond to Dropbox in less than 10sec → set_folder to watch B (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0802_Webhook_Nocodb_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0802_Webhook_Nocodb_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
