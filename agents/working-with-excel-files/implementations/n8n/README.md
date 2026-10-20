# Working with Excel files

This folder contains the **Working with Excel files** workflow. Its executable nodes use `ftp`, `googleDrive`, `httpRequest`, `manualTrigger`, `microsoftOneDrive`, `readBinaryFile`, `set`, `spreadsheetFile`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`working-with-excel-files.json`](working-with-excel-files.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `microsoftOneDriveOAuth2Api`, `sftp`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Read Binary File | `readBinaryFile` | Inspect parameters |
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Write Binary File | `writeBinaryFile` | Inspect parameters |
| Download from Google Drive | `googleDrive` | download |
| Download from Microsoft OneDrive | `microsoftOneDrive` | download |
| Download Excel File | `httpRequest` | Inspect parameters |
| Work out Age | `set` | Inspect parameters |
| Upload to SFTP | `ftp` | upload |
| Upload to Google Drive | `googleDrive` | Inspect parameters |
| Upload to Microsoft OneDrive | `microsoftOneDrive` | Inspect parameters |
| Read Spreadsheet File | `spreadsheetFile` | Inspect parameters |
| Write Spreadsheet File | `spreadsheetFile` | toFile |

## Connection map

- Work out Age → Write Spreadsheet File (`main`, output 0, input 0)
- Read Binary File → Read Spreadsheet File (`main`, output 0, input 0)
- Download Excel File → Read Spreadsheet File (`main`, output 0, input 0)
- On clicking 'execute' → Read Binary File (`main`, output 0, input 0)
- On clicking 'execute' → Download Excel File (`main`, output 0, input 0)
- On clicking 'execute' → Download from Google Drive (`main`, output 0, input 0)
- On clicking 'execute' → Download from Microsoft OneDrive (`main`, output 0, input 0)
- Read Spreadsheet File → Work out Age (`main`, output 0, input 0)
- Write Spreadsheet File → Upload to SFTP (`main`, output 0, input 0)
- Write Spreadsheet File → Upload to Google Drive (`main`, output 0, input 0)
- Write Spreadsheet File → Write Binary File (`main`, output 0, input 0)
- Write Spreadsheet File → Upload to Microsoft OneDrive (`main`, output 0, input 0)
- Download from Google Drive → Read Spreadsheet File (`main`, output 0, input 0)
- Download from Microsoft OneDrive → Read Spreadsheet File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftonedrive/0276_Microsoftonedrive_Readbinaryfile_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftonedrive/0276_Microsoftonedrive_Readbinaryfile_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
