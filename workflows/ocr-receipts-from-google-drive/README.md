# OCR receipts from Google Drive

This folder contains the **OCR receipts from Google Drive** workflow. Its executable nodes use `code`, `googleDrive`, `googleDriveTrigger`, `googleSheets`, `httpRequest`, `manualTrigger`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ocr-receipts-from-google-drive.json`](ocr-receipts-from-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’, On new file in Google Drive

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OCR recognize | `httpRequest` | POST |
| Unserialize response JSON | `code` | Inspect parameters |
| On new file in Google Drive | `googleDriveTrigger` | Inspect parameters |
| Load files from Google Drive folder | `googleDrive` | fileFolder |
| Filter processed files | `merge` | Inspect parameters |
| Download file for OCR | `googleDrive` | download |
| Save OCR result into Sheets | `googleSheets` | appendOrUpdate |
| Get already processed rows from Sheets | `googleSheets` | Inspect parameters |

## Connection map

- OCR recognize → Unserialize response JSON (`main`, output 0, input 0)
- Download file for OCR → OCR recognize (`main`, output 0, input 0)
- Filter processed files → Download file for OCR (`main`, output 0, input 0)
- Unserialize response JSON → Save OCR result into Sheets (`main`, output 0, input 0)
- On new file in Google Drive → Get already processed rows from Sheets (`main`, output 0, input 0)
- On new file in Google Drive → Load files from Google Drive folder (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Load files from Google Drive folder (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get already processed rows from Sheets (`main`, output 0, input 0)
- Load files from Google Drive folder → Filter processed files (`main`, output 0, input 1)
- Get already processed rows from Sheets → Filter processed files (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1839_Code_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1839_Code_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
