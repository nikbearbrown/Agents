# AutoQoutesV2_template

This folder contains the **AutoQoutesV2_template** workflow. Its executable nodes use `code`, `executeCommand`, `googleDrive`, `googleSheets`, `httpRequest`, `manualTrigger`, `readWriteFile`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`autoqoutesv2-template.json`](autoqoutesv2-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `youTubeOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Generate Image | `httpRequest` | POST |
| Get image | `httpRequest` | Inspect parameters |
| Update image background URL | `googleSheets` | update |
| Image-to-Video | `httpRequest` | POST |
| Wait image 2 min | `wait` | Inspect parameters |
| Wait video 5 min | `wait` | Inspect parameters |
| Get Video | `httpRequest` | Inspect parameters |
| Generate Audio | `httpRequest` | POST |
| Get data from Google Sheet | `googleSheets` | Inspect parameters |
| Update Sound background URL | `googleSheets` | update |
| Update video background URL | `googleSheets` | update |
| Upload Sound to Google Drive | `googleDrive` | Inspect parameters |
| Save Video Background Locally1 | `readWriteFile` | write |
| Get Binary Video Background | `httpRequest` | Inspect parameters |
| Save Music Background Locally1 | `readWriteFile` | write |
| Prepare Overlay Text (Quote & Author)1 | `code` | Inspect parameters |
| Generate Final Video Clip1 | `executeCommand` | Inspect parameters |
| Initiate YouTube Resumable Upload | `httpRequest` | POST |
| Read output file | `readWriteFile` | Inspect parameters |
| Upload Video to YouTube | `httpRequest` | PUT |
| Update Quote Upload Status | `googleSheets` | appendOrUpdate |

## Connection map

- Get Video → Get Binary Video Background (`main`, output 0, input 0)
- Get image → Update image background URL (`main`, output 0, input 0)
- Generate Audio → Upload Sound to Google Drive (`main`, output 0, input 0)
- Generate Audio → Save Music Background Locally1 (`main`, output 0, input 0)
- Generate Image → Wait image 2 min (`main`, output 0, input 0)
- Image-to-Video → Wait video 5 min (`main`, output 0, input 0)
- Read output file → Upload Video to YouTube (`main`, output 0, input 0)
- Wait image 2 min → Get image (`main`, output 0, input 0)
- Wait video 5 min → Get Video (`main`, output 0, input 0)
- Upload Video to YouTube → Update Quote Upload Status (`main`, output 0, input 0)
- Generate Final Video Clip1 → Initiate YouTube Resumable Upload (`main`, output 0, input 0)
- Get data from Google Sheet → Generate Image (`main`, output 0, input 0)
- Get Binary Video Background → Save Video Background Locally1 (`main`, output 0, input 0)
- Update image background URL → Image-to-Video (`main`, output 0, input 0)
- Update video background URL → Generate Audio (`main`, output 0, input 0)
- Upload Sound to Google Drive → Update Sound background URL (`main`, output 0, input 0)
- Save Music Background Locally1 → Prepare Overlay Text (Quote & Author)1 (`main`, output 0, input 0)
- Save Video Background Locally1 → Update video background URL (`main`, output 0, input 0)
- Initiate YouTube Resumable Upload → Read output file (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get data from Google Sheet (`main`, output 0, input 0)
- Prepare Overlay Text (Quote & Author)1 → Generate Final Video Clip1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1400_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1400_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
