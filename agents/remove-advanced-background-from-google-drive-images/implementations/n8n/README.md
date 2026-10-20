# Remove Advanced Background from Google Drive Images

This folder contains the **Remove Advanced Background from Google Drive Images** workflow. Its executable nodes use `editImage`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `if`, `merge`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`remove-advanced-background-from-google-drive-images.json`](remove-advanced-background-from-google-drive-images.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`

**Entry nodes:** Watch for new images

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Config | `set` | Inspect parameters |
| remove background | `httpRequest` | POST |
| Split Out | `splitOut` | Inspect parameters |
| Upload Picture to Google Drive | `googleDrive` | Inspect parameters |
| remove background fixed size | `httpRequest` | POST |
| Merge | `merge` | Inspect parameters |
| Upload Picture to Google Drive1 | `googleDrive` | Inspect parameters |
| Download Image | `googleDrive` | download |
| Get Image Size | `editImage` | information |
| Watch for new images | `googleDriveTrigger` | Inspect parameters |
| check which output size method is used | `if` | Inspect parameters |
| loop all over your images | `splitInBatches` | Inspect parameters |

## Connection map

- Merge → loop all over your images (`main`, output 0, input 0)
- Config → Merge (`main`, output 0, input 1)
- Split Out → Merge (`main`, output 0, input 0)
- Download Image → Get Image Size (`main`, output 0, input 0)
- Get Image Size → Split Out (`main`, output 0, input 0)
- remove background → Upload Picture to Google Drive1 (`main`, output 0, input 0)
- Watch for new images → Download Image (`main`, output 0, input 0)
- Watch for new images → Config (`main`, output 0, input 0)
- loop all over your images → check which output size method is used (`main`, output 1, input 0)
- remove background fixed size → Upload Picture to Google Drive (`main`, output 0, input 0)
- Upload Picture to Google Drive → loop all over your images (`main`, output 0, input 0)
- Upload Picture to Google Drive1 → loop all over your images (`main`, output 0, input 0)
- check which output size method is used → remove background fixed size (`main`, output 0, input 0)
- check which output size method is used → remove background (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1943_Splitout_Editimage_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1943_Splitout_Editimage_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
