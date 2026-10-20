# Convert image from jpg/png to webp

This folder contains the **Convert image from jpg/png to webp** workflow. Its executable nodes use `code`, `googleDrive`, `googleSheets`, `httpRequest`, `manualTrigger`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`convert-image-from-jpg-png-to-webp.json`](convert-image-from-jpg-png-to-webp.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set API KEY | `set` | Inspect parameters |
| Get images | `googleSheets` | Inspect parameters |
| Get extension | `code` | Inspect parameters |
| JPG or PNG? | `switch` | Inspect parameters |
| From JPG to WEBP | `httpRequest` | POST |
| PNG to WEBP | `httpRequest` | POST |
| Update Sheet | `googleSheets` | update |
| Get file image | `httpRequest` | Inspect parameters |
| Upload image | `googleDrive` | Inspect parameters |

## Connection map

- Get images → Get extension (`main`, output 0, input 0)
- JPG or PNG? → From JPG to WEBP (`main`, output 0, input 0)
- JPG or PNG? → From JPG to WEBP (`main`, output 1, input 0)
- JPG or PNG? → PNG to WEBP (`main`, output 2, input 0)
- PNG to WEBP → Update Sheet (`main`, output 0, input 0)
- Set API KEY → Get images (`main`, output 0, input 0)
- Update Sheet → Get file image (`main`, output 0, input 0)
- Get extension → JPG or PNG? (`main`, output 0, input 0)
- Get file image → Upload image (`main`, output 0, input 0)
- From JPG to WEBP → Update Sheet (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set API KEY (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1518_Code_Manual_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1518_Code_Manual_Process_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
