# Image-to-3D

This folder contains the **Image-to-3D** workflow. Its executable nodes use `googleDrive`, `googleSheets`, `httpRequest`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`verified-image-to-3d.json`](verified-image-to-3d.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get status | `httpRequest` | Inspect parameters |
| Wait 60 sec. | `wait` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Completed? | `if` | Inspect parameters |
| Update result | `googleSheets` | update |
| Set data | `set` | Inspect parameters |
| Get new image | `googleSheets` | Inspect parameters |
| Create 3D Image | `httpRequest` | POST |
| Get Url 3D image | `httpRequest` | Inspect parameters |
| Get File 3D image | `httpRequest` | Inspect parameters |
| Upload 3D Image | `googleDrive` | Inspect parameters |

## Connection map

- Set data → Create 3D Image (`main`, output 0, input 0)
- Completed? → Get Url 3D image (`main`, output 0, input 0)
- Completed? → Wait 60 sec. (`main`, output 1, input 0)
- Get status → Completed? (`main`, output 0, input 0)
- Wait 60 sec. → Get status (`main`, output 0, input 0)
- Get new image → Set data (`main`, output 0, input 0)
- Create 3D Image → Wait 60 sec. (`main`, output 0, input 0)
- Upload 3D Image → Update result (`main`, output 0, input 0)
- Get Url 3D image → Get File 3D image (`main`, output 0, input 0)
- Get File 3D image → Upload 3D Image (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get new image (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1763_Wait_Schedule_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1763_Wait_Schedule_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
