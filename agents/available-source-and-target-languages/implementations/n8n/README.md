# Available source and target languages`*`:

This folder contains the **Available source and target languages`*`:** workflow. Its executable nodes use `filter`, `googleDrive`, `httpRequest`, `if`, `manualTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`available-source-and-target-languages.json`](available-source-and-target-languages.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Run manually

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Run manually | `manualTrigger` | Inspect parameters |
| Get files from specified folder | `googleDrive` | fileFolder |
| Use only PDF documents | `filter` | Inspect parameters |
| Download files | `googleDrive` | download |
| Send translate request | `httpRequest` | POST |
| Check translation status | `httpRequest` | POST |
| Wait a bit | `wait` | Inspect parameters |
| file translated? | `if` | Inspect parameters |
| Wait between documents | `wait` | Inspect parameters |
| Get translated document from deepL | `httpRequest` | POST |
| Uplad to original folder | `googleDrive` | Inspect parameters |
| ⚙️ config | `set` | Inspect parameters |

## Connection map

- Wait a bit → file translated? (`main`, output 0, input 0)
- Run manually → ⚙️ config (`main`, output 0, input 0)
- ⚙️ config → Get files from specified folder (`main`, output 0, input 0)
- Download files → Send translate request (`main`, output 0, input 0)
- file translated? → Wait between documents (`main`, output 0, input 0)
- file translated? → Check translation status (`main`, output 1, input 0)
- Send translate request → Check translation status (`main`, output 0, input 0)
- Use only PDF documents → Download files (`main`, output 0, input 0)
- Wait between documents → Get translated document from deepL (`main`, output 0, input 0)
- Check translation status → Wait a bit (`main`, output 0, input 0)
- Get files from specified folder → Use only PDF documents (`main`, output 0, input 0)
- Get translated document from deepL → Uplad to original folder (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 5}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0466_Wait_Filter_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0466_Wait_Filter_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
