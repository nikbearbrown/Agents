# ✨😃Automated Workflow Backups to Google Drive

This folder contains the **✨😃Automated Workflow Backups to Google Drive** workflow. Its executable nodes use `code`, `convertToFile`, `googleDrive`, `limit`, `manualTrigger`, `n8n`, `noOp`, `scheduleTrigger`, `set`, `splitInBatches`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-workflow-backups-to-google-drive.json`](automated-workflow-backups-to-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `n8nApi`, `telegramApi`

**Entry nodes:** On clicking 'execute', Every Day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Every Day | `scheduleTrigger` | Inspect parameters |
| Create Folder with DateTime Stamp | `googleDrive` | folder |
| Get DateTIme | `set` | Inspect parameters |
| Get Workflows | `n8n` | Inspect parameters |
| Limit to 200 | `limit` | Inspect parameters |
| Convert Workflow to JSON File | `convertToFile` | toJson |
| Save JSON File to Google Drive Folder | `googleDrive` | Inspect parameters |
| Execute Once | `noOp` | Inspect parameters |
| Search Folder Names | `googleDrive` | fileFolder |
| Delete Folders | `googleDrive` | folder / deleteFolder |
| Complete Message | `telegram` | Inspect parameters |
| Find Folders to Delete | `code` | Inspect parameters |

## Connection map

- Every Day → Get DateTIme (`main`, output 0, input 0)
- Execute Once → Search Folder Names (`main`, output 0, input 0)
- Execute Once → Complete Message (`main`, output 0, input 0)
- Get DateTIme → Create Folder with DateTime Stamp (`main`, output 0, input 0)
- Limit to 200 → Loop Over Items (`main`, output 0, input 0)
- Get Workflows → Limit to 200 (`main`, output 0, input 0)
- Loop Over Items → Execute Once (`main`, output 0, input 0)
- Loop Over Items → Convert Workflow to JSON File (`main`, output 1, input 0)
- Search Folder Names → Find Folders to Delete (`main`, output 0, input 0)
- On clicking 'execute' → Get DateTIme (`main`, output 0, input 0)
- Find Folders to Delete → Delete Folders (`main`, output 0, input 0)
- Convert Workflow to JSON File → Save JSON File to Google Drive Folder (`main`, output 0, input 0)
- Create Folder with DateTime Stamp → Get Workflows (`main`, output 0, input 0)
- Save JSON File to Google Drive Folder → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1940_Telegram_Limit_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1940_Telegram_Limit_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
