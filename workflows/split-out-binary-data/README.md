# split out binary data

This folder contains the **split out binary data** workflow. Its executable nodes use `code`, `formTrigger`, `googleDrive`, `if`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`split-out-binary-data.json`](split-out-binary-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Get Folder Name | `set` | Inspect parameters |
| Search specific folder | `googleDrive` | fileFolder |
| Folder found ? | `if` | Inspect parameters |
| Create Folder | `googleDrive` | folder |
| Upload Files | `googleDrive` | Inspect parameters |
| Prepare Files for Upload | `code` | Inspect parameters |
| Prepare Files for New Folder | `code` | Inspect parameters |
| Upload to New Folder | `googleDrive` | Inspect parameters |

## Connection map

- Create Folder → Prepare Files for New Folder (`main`, output 0, input 0)
- Folder found ? → Prepare Files for Upload (`main`, output 0, input 0)
- Folder found ? → Create Folder (`main`, output 1, input 0)
- Get Folder Name → Search specific folder (`main`, output 0, input 0)
- On form submission → Get Folder Name (`main`, output 0, input 0)
- Search specific folder → Folder found ? (`main`, output 0, input 0)
- Prepare Files for Upload → Upload Files (`main`, output 0, input 0)
- Prepare Files for New Folder → Upload to New Folder (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0733_Form_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0733_Form_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
