# get Google Drive folders

This folder contains the **get Google Drive folders** workflow. Its executable nodes use `code`, `filter`, `googleDrive`, `if`, `itemLists`, `merge`, `moveBinaryData`, `n8n`, `scheduleTrigger`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-google-drive-folders.json`](get-google-drive-folders.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `n8nApi`

**Entry nodes:** Schedule Trigger, Schedule Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| IGNORE FILES | `filter` | Inspect parameters |
| Create n8n_backups | `googleDrive` | folder |
| Create n8n_old | `googleDrive` | folder |
| GET CURRENT FOLDER | `googleDrive` | fileFolder |
| Code | `code` | Inspect parameters |
| If n8n_old | `if` | Inspect parameters |
| If1 n8n_backups | `if` | Inspect parameters |
| GET CURRENT FOLDER CREATES | `googleDrive` | fileFolder |
| Merge mensage | `merge` | Inspect parameters |
| GET CURRENT BACKUPS1 | `googleDrive` | fileFolder |
| MOVE INTO OLD FOLDER | `googleDrive` | move |
| UPLOAD WORKFLOWS | `googleDrive` | Inspect parameters |
| Item Lists | `itemLists` | Inspect parameters |
| Split In Batches2 | `splitInBatches` | Inspect parameters |
| Split In Batches | `splitInBatches` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| LIST OLD BACKUPS | `googleDrive` | fileFolder |
| DELETE OLD BACKUP | `googleDrive` | deleteFile |
| Item Lists old | `itemLists` | Inspect parameters |
| Split In Batches old | `splitInBatches` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |

## Connection map

- n8n → Move Binary Data (`main`, output 0, input 0)
- Code → If n8n_old (`main`, output 0, input 0)
- Code → If1 n8n_backups (`main`, output 0, input 0)
- If n8n_old → Create n8n_old (`main`, output 0, input 0)
- If n8n_old → Merge mensage (`main`, output 1, input 1)
- Item Lists → Split In Batches2 (`main`, output 0, input 0)
- IGNORE FILES → GET CURRENT BACKUPS1 (`main`, output 0, input 0)
- IGNORE FILES → n8n (`main`, output 0, input 0)
- Merge mensage → GET CURRENT FOLDER CREATES (`main`, output 0, input 0)
- Create n8n_old → GET CURRENT FOLDER (`main`, output 0, input 0)
- Item Lists old → Split In Batches old (`main`, output 0, input 0)
- If1 n8n_backups → Create n8n_backups (`main`, output 0, input 0)
- If1 n8n_backups → Merge mensage (`main`, output 1, input 0)
- LIST OLD BACKUPS → Item Lists old (`main`, output 0, input 0)
- Move Binary Data → Split In Batches (`main`, output 0, input 0)
- Schedule Trigger → GET CURRENT FOLDER (`main`, output 0, input 0)
- Split In Batches → UPLOAD WORKFLOWS (`main`, output 0, input 0)
- UPLOAD WORKFLOWS → Split In Batches (`main`, output 0, input 0)
- DELETE OLD BACKUP → Split In Batches old (`main`, output 0, input 0)
- Split In Batches2 → MOVE INTO OLD FOLDER (`main`, output 0, input 0)
- Create n8n_backups → GET CURRENT FOLDER (`main`, output 0, input 0)
- GET CURRENT FOLDER → Code (`main`, output 0, input 0)
- GET CURRENT BACKUPS1 → Item Lists (`main`, output 0, input 0)
- MOVE INTO OLD FOLDER → Split In Batches2 (`main`, output 0, input 0)
- Split In Batches old → DELETE OLD BACKUP (`main`, output 0, input 0)
- GET CURRENT FOLDER CREATES → IGNORE FILES (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0605_Code_Itemlists_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0605_Code_Itemlists_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
