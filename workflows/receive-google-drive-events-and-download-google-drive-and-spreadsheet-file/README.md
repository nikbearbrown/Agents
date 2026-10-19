# receive google drive events and download google drive and spreadsheet file

This folder contains the **receive google drive events and download google drive and spreadsheet file** workflow. Its executable nodes use `googleDrive`, `googleDriveTrigger`, `if`, `merge`, `pipedrive`, `set`, `spreadsheetFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-google-drive-events-and-download-google-drive-and-spreadsheet-file.json`](receive-google-drive-events-and-download-google-drive-and-spreadsheet-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `pipedriveApi`

**Entry nodes:** Google Drive Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| Google Drive | `googleDrive` | download |
| Spreadsheet File | `spreadsheetFile` | Inspect parameters |
| Pipedrive | `pipedrive` | lead / getAll |
| Pipedrive1 | `pipedrive` | person / get |
| IF | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Create Organization | `pipedrive` | organization |
| Create Person | `pipedrive` | person |
| Create Lead | `pipedrive` | lead |
| Create Note | `pipedrive` | note |

## Connection map

- IF → Pipedrive1 (`main`, output 0, input 0)
- Set → Create Organization (`main`, output 0, input 0)
- Merge → Set (`main`, output 0, input 0)
- Pipedrive → IF (`main`, output 0, input 0)
- Pipedrive1 → Merge (`main`, output 0, input 1)
- Create Lead → Create Note (`main`, output 0, input 0)
- Google Drive → Spreadsheet File (`main`, output 0, input 0)
- Create Person → Create Lead (`main`, output 0, input 0)
- Spreadsheet File → Pipedrive (`main`, output 0, input 0)
- Spreadsheet File → Merge (`main`, output 0, input 0)
- Create Organization → Create Person (`main`, output 0, input 0)
- Google Drive Trigger → Google Drive (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Pipedrive/0251_Pipedrive_Spreadsheetfile_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Pipedrive/0251_Pipedrive_Spreadsheetfile_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
