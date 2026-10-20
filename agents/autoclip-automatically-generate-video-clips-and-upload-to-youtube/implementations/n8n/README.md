# AutoClip – Automatically Generate Video Clips and Upload to YouTube

This folder contains the **AutoClip – Automatically Generate Video Clips and Upload to YouTube** workflow. Its executable nodes use `code`, `executeCommand`, `googleDrive`, `googleSheets`, `httpRequest`, `manualTrigger`, `merge`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`autoclip-automatically-generate-video-clips-and-upload-to-youtube.json`](autoclip-automatically-generate-video-clips-and-upload-to-youtube.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `youTubeOAuth2Api`

**Entry nodes:** Start AutoClip Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start AutoClip Workflow | `manualTrigger` | Inspect parameters |
| Retrieve Video Background Data | `googleSheets` | append |
| Retrieve Quote Data | `googleSheets` | Inspect parameters |
| List Video Background Files | `googleDrive` | fileFolder |
| Configure Music Background Folder ID | `set` | Inspect parameters |
| List Music Background Files | `googleDrive` | fileFolder |
| Retrieve Music Background Data | `googleSheets` | append |
| Merge File Selection Data | `merge` | Inspect parameters |
| Select Random Video, Music & Quote | `code` | Inspect parameters |
| Download Selected Video Background | `googleDrive` | download |
| Download Selected Music Background | `googleDrive` | download |
| Save Video Background Locally | `readWriteFile` | write |
| Save Music Background Locally | `readWriteFile` | write |
| Prepare Overlay Text (Quote & Author) | `code` | Inspect parameters |
| Generate Final Video Clip | `executeCommand` | Inspect parameters |
| Initiate YouTube Resumable Upload | `httpRequest` | POST |
| Read output file | `readWriteFile` | Inspect parameters |
| Upload Video to YouTube | `httpRequest` | PUT |
| Update Quote Upload Status | `googleSheets` | appendOrUpdate |
| Mark Background as Used | `googleSheets` | appendOrUpdate |

## Connection map

- Read output file → Upload Video to YouTube (`main`, output 0, input 0)
- Retrieve Quote Data → Merge File Selection Data (`main`, output 0, input 0)
- Start AutoClip Workflow → Retrieve Quote Data (`main`, output 0, input 0)
- Start AutoClip Workflow → List Video Background Files (`main`, output 0, input 0)
- Start AutoClip Workflow → Configure Music Background Folder ID (`main`, output 0, input 0)
- Upload Video to YouTube → Update Quote Upload Status (`main`, output 0, input 0)
- Generate Final Video Clip → Initiate YouTube Resumable Upload (`main`, output 0, input 0)
- Merge File Selection Data → Select Random Video, Music & Quote (`main`, output 0, input 0)
- Update Quote Upload Status → Mark Background as Used (`main`, output 0, input 0)
- List Music Background Files → Retrieve Music Background Data (`main`, output 0, input 0)
- List Video Background Files → Retrieve Video Background Data (`main`, output 0, input 0)
- Save Music Background Locally → Prepare Overlay Text (Quote & Author) (`main`, output 0, input 0)
- Save Video Background Locally → Download Selected Music Background (`main`, output 0, input 0)
- Retrieve Music Background Data → Merge File Selection Data (`main`, output 0, input 2)
- Retrieve Video Background Data → Merge File Selection Data (`main`, output 0, input 1)
- Initiate YouTube Resumable Upload → Read output file (`main`, output 0, input 0)
- Download Selected Music Background → Save Music Background Locally (`main`, output 0, input 0)
- Download Selected Video Background → Save Video Background Locally (`main`, output 0, input 0)
- Select Random Video, Music & Quote → Download Selected Video Background (`main`, output 0, input 0)
- Configure Music Background Folder ID → List Music Background Files (`main`, output 0, input 0)
- Prepare Overlay Text (Quote & Author) → Generate Final Video Clip (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1864_Code_Executecommand_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1864_Code_Executecommand_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
