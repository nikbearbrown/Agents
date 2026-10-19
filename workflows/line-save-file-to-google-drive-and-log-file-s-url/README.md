# Line Save File to Google Drive and Log File's URL

This folder contains the **Line Save File to Google Drive and Log File's URL** workflow. Its executable nodes use `code`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `merge`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`line-save-file-to-google-drive-and-log-file-s-url.json`](line-save-file-to-google-drive-and-log-file-s-url.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** LINE Webhook Listener

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Config | `googleSheets` | Inspect parameters |
| Create Date Folder | `googleDrive` | folder |
| Set Date Folder ID | `code` | Inspect parameters |
| Create File Type Folder | `googleDrive` | folder |
| Upload File to Google Drive | `googleDrive` | Inspect parameters |
| Determine Folder Info | `code` | Inspect parameters |
| Search Date Folder | `googleDrive` | fileFolder |
| Merge Event and Config Data | `merge` | Inspect parameters |
| Check Existing Date Folder | `if` | Inspect parameters |
| Check Existing File Type Folder | `if` | Inspect parameters |
| Merge Final Parent Folder Data | `merge` | Inspect parameters |
| Search File Type Folder | `googleDrive` | fileFolder |
| Set File Type Folder ID | `code` | Inspect parameters |
| Configure Final Parent Folder ID | `code` | Inspect parameters |
| Process Event and Config Data | `code` | Inspect parameters |
| Get File Binary Content | `httpRequest` | Inspect parameters |
| Log File Details to Google Sheet | `googleSheets` | append |
| Check Reply Enabled Flag | `if` | Inspect parameters |
| Check if Store by Date is Enabled | `if` | Inspect parameters |
| Check if Store by File Type is Enabled | `if` | Inspect parameters |
| LINE Webhook Listener | `webhook` | Inspect parameters |
| Send LINE Reply Message | `httpRequest` | POST |
| Validate File Type | `code` | Inspect parameters |

## Connection map

- Get Config → Merge Event and Config Data (`main`, output 0, input 1)
- Create Date Folder → Set Date Folder ID (`main`, output 0, input 0)
- Search Date Folder → Check Existing Date Folder (`main`, output 0, input 0)
- Set Date Folder ID → Search File Type Folder (`main`, output 0, input 0)
- Set Date Folder ID → Merge Final Parent Folder Data (`main`, output 0, input 0)
- Validate File Type → Upload File to Google Drive (`main`, output 0, input 0)
- Determine Folder Info → Search Date Folder (`main`, output 0, input 0)
- LINE Webhook Listener → Merge Event and Config Data (`main`, output 0, input 0)
- LINE Webhook Listener → Get Config (`main`, output 0, input 0)
- Create File Type Folder → Set File Type Folder ID (`main`, output 0, input 0)
- Get File Binary Content → Validate File Type (`main`, output 0, input 0)
- Search File Type Folder → Check Existing File Type Folder (`main`, output 0, input 0)
- Set File Type Folder ID → Merge Final Parent Folder Data (`main`, output 0, input 1)
- Check Reply Enabled Flag → Send LINE Reply Message (`main`, output 0, input 0)
- Check Existing Date Folder → Set Date Folder ID (`main`, output 0, input 0)
- Check Existing Date Folder → Check if Store by Date is Enabled (`main`, output 1, input 0)
- Merge Event and Config Data → Process Event and Config Data (`main`, output 0, input 0)
- Upload File to Google Drive → Log File Details to Google Sheet (`main`, output 0, input 0)
- Process Event and Config Data → Determine Folder Info (`main`, output 0, input 0)
- Merge Final Parent Folder Data → Configure Final Parent Folder ID (`main`, output 0, input 0)
- Check Existing File Type Folder → Set File Type Folder ID (`main`, output 0, input 0)
- Check Existing File Type Folder → Check if Store by File Type is Enabled (`main`, output 1, input 0)
- Configure Final Parent Folder ID → Get File Binary Content (`main`, output 0, input 0)
- Log File Details to Google Sheet → Check Reply Enabled Flag (`main`, output 0, input 0)
- Check if Store by Date is Enabled → Create Date Folder (`main`, output 0, input 0)
- Check if Store by Date is Enabled → Set Date Folder ID (`main`, output 1, input 0)
- Check if Store by File Type is Enabled → Create File Type Folder (`main`, output 0, input 0)
- Check if Store by File Type is Enabled → Set File Type Folder ID (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1924_Code_Webhook_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1924_Code_Webhook_Export_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
