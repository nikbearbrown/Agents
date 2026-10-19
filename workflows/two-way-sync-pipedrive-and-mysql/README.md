# Two Way Sync Pipedrive and MySQL

This folder contains the **Two Way Sync Pipedrive and MySQL** workflow. Its executable nodes use `compareDatasets`, `dateTime`, `if`, `mySql`, `pipedrive`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`two-way-sync-pipedrive-and-mysql.json`](two-way-sync-pipedrive-and-mysql.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`, `pipedriveApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| MySQL | `mySql` | executeQuery |
| Pipedrive | `pipedrive` | person / getAll |
| Create Person | `pipedrive` | person |
| Create Contact | `mySql` | Inspect parameters |
| Date & Time | `dateTime` | Inspect parameters |
| Update Contact | `mySql` | executeQuery |
| Set Input2 | `set` | Inspect parameters |
| Set Input1 | `set` | Inspect parameters |
| Update Person | `pipedrive` | person / update |
| IF Data Changed | `if` | Inspect parameters |
| IF Updated On | `if` | Inspect parameters |
| Set | `set` | Inspect parameters |

## Connection map

- Set → Compare Datasets (`main`, output 0, input 1)
- MySQL → Compare Datasets (`main`, output 0, input 0)
- Pipedrive → Set (`main`, output 0, input 0)
- Set Input1 → Update Person (`main`, output 0, input 0)
- Set Input2 → Update Contact (`main`, output 0, input 0)
- Date & Time → IF Updated On (`main`, output 0, input 0)
- IF Updated On → Set Input1 (`main`, output 0, input 0)
- IF Updated On → Set Input2 (`main`, output 1, input 0)
- IF Data Changed → Date & Time (`main`, output 0, input 0)
- Compare Datasets → Create Person (`main`, output 0, input 0)
- Compare Datasets → IF Data Changed (`main`, output 2, input 0)
- Compare Datasets → Create Contact (`main`, output 3, input 0)
- Schedule Trigger → MySQL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1092_Datetime_Schedule_Sync_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1092_Datetime_Schedule_Sync_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
