# Upload attachments to Drive

This folder contains the **Upload attachments to Drive** workflow. Its executable nodes use `function`, `gmail`, `gmailTrigger`, `googleDrive`, `googleSheets`, `if`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`upload-attachments-to-drive.json`](upload-attachments-to-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Search For Folder | `googleDrive` | fileFolder |
| Create Month Folder | `googleDrive` | folder |
| Check If Folder Exists | `if` | Inspect parameters |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Gmail | `gmail` | get |
| Split Up Binary Data1 | `function` | Inspect parameters |
| YYYY/MM | `set` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Company Folder Exists | `if` | Inspect parameters |
| Create Company Folder | `googleDrive` | folder |
| Lookup in Sheets | `googleSheets` | Inspect parameters |
| Search Company Folder1 | `googleDrive` | fileFolder |
| Upload To Folder | `googleDrive` | Inspect parameters |

## Connection map

- Gmail → Split Up Binary Data1 (`main`, output 0, input 0)
- YYYY/MM → Search For Folder (`main`, output 0, input 0)
- Gmail Trigger → Lookup in Sheets (`main`, output 0, input 0)
- Loop Over Items → Upload To Folder (`main`, output 1, input 0)
- Lookup in Sheets → Search Company Folder1 (`main`, output 0, input 0)
- Upload To Folder → Loop Over Items (`main`, output 0, input 0)
- Search For Folder → Check If Folder Exists (`main`, output 0, input 0)
- Create Month Folder → Gmail (`main`, output 0, input 0)
- Company Folder Exists → YYYY/MM (`main`, output 0, input 0)
- Company Folder Exists → Create Company Folder (`main`, output 1, input 0)
- Create Company Folder → YYYY/MM (`main`, output 0, input 0)
- Split Up Binary Data1 → Loop Over Items (`main`, output 0, input 0)
- Check If Folder Exists → Gmail (`main`, output 0, input 0)
- Check If Folder Exists → Create Month Folder (`main`, output 1, input 0)
- Search Company Folder1 → Company Folder Exists (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/0837_GoogleSheets_Gmail_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/0837_GoogleSheets_Gmail_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
