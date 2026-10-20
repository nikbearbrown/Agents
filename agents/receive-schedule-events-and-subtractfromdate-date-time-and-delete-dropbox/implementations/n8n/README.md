# receive schedule events and subtractfromdate date time and delete dropbox

This folder contains the **receive schedule events and subtractfromdate date time and delete dropbox** workflow. Its executable nodes use `dateTime`, `dropbox`, `filter`, `if`, `merge`, `moveBinaryData`, `n8n`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-subtractfromdate-date-time-and-delete-dropbox.json`](receive-schedule-events-and-subtractfromdate-date-time-and-delete-dropbox.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropboxOAuth2Api`, `n8nApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| PURGE DAYS | `dateTime` | subtractFromDate |
| DELETE OLD BACKUPS | `dropbox` | delete |
| GET WORKFLOWS | `n8n` | Inspect parameters |
| MAKE JSON FILES | `moveBinaryData` | Inspect parameters |
| UPLOAD WORKFLOWS | `dropbox` | Inspect parameters |
| DESTINATION FOLDER | `set` | Inspect parameters |
| WAIT FOR MOVE TO FINISH | `merge` | Inspect parameters |
| GET CURRENT BACKUPS | `dropbox` | folder / list |
| IGNORE FOLDERS | `filter` | Inspect parameters |
| MOVE INTO OLD FOLDER | `dropbox` | move |
| LIST OLD BACKUPS | `dropbox` | folder / list |
| CHECK DATES | `if` | Inspect parameters |
| GET CURRENT DATE | `dateTime` | formatDate |

## Connection map

- PURGE DAYS → LIST OLD BACKUPS (`main`, output 0, input 0)
- CHECK DATES → DELETE OLD BACKUPS (`main`, output 0, input 0)
- GET WORKFLOWS → MAKE JSON FILES (`main`, output 0, input 0)
- IGNORE FOLDERS → MOVE INTO OLD FOLDER (`main`, output 0, input 0)
- MAKE JSON FILES → UPLOAD WORKFLOWS (`main`, output 0, input 0)
- GET CURRENT DATE → GET CURRENT BACKUPS (`main`, output 0, input 0)
- LIST OLD BACKUPS → CHECK DATES (`main`, output 0, input 0)
- Schedule Trigger → DESTINATION FOLDER (`main`, output 0, input 0)
- DESTINATION FOLDER → GET CURRENT DATE (`main`, output 0, input 0)
- DESTINATION FOLDER → WAIT FOR MOVE TO FINISH (`main`, output 0, input 1)
- DESTINATION FOLDER → PURGE DAYS (`main`, output 0, input 0)
- GET CURRENT BACKUPS → IGNORE FOLDERS (`main`, output 0, input 0)
- MOVE INTO OLD FOLDER → WAIT FOR MOVE TO FINISH (`main`, output 0, input 0)
- WAIT FOR MOVE TO FINISH → GET WORKFLOWS (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0396_Datetime_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0396_Datetime_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
