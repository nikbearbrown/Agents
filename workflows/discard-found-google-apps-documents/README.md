# Discard found Google Apps documents

This folder contains the **Discard found Google Apps documents** workflow. Its executable nodes use `code`, `filter`, `googleDrive`, `googleDriveTrigger`, `if`, `noOp`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`discard-found-google-apps-documents.json`](discard-found-google-apps-documents.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`

**Entry nodes:** Google Drive Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Config | `set` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Deduplicate Keep First | `code` | Inspect parameters |
| Deduplicate Keep Last | `code` | Inspect parameters |
| Send Duplicates to Trash | `googleDrive` | deleteFile |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Is Flagged | `if` | Inspect parameters |
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| Drop Google Apps files | `filter` | Inspect parameters |
| Working Folder | `googleDrive` | fileFolder |
| Google Drive | `googleDrive` | update |
| Keep First/Last | `switch` | Inspect parameters |
| Trash/Flag Duplicates | `switch` | Inspect parameters |

## Connection map

- Config → Working Folder (`main`, output 0, input 0)
- Filter → Trash/Flag Duplicates (`main`, output 0, input 0)
- Is Flagged → No Operation, do nothing (`main`, output 0, input 0)
- Is Flagged → Google Drive (`main`, output 1, input 0)
- Edit Fields → Filter (`main`, output 0, input 0)
- Working Folder → Drop Google Apps files (`main`, output 0, input 0)
- Keep First/Last → Deduplicate Keep Last (`main`, output 0, input 0)
- Keep First/Last → Deduplicate Keep First (`main`, output 1, input 0)
- Google Drive Trigger → Config (`main`, output 0, input 0)
- Deduplicate Keep Last → Edit Fields (`main`, output 0, input 0)
- Trash/Flag Duplicates → Send Duplicates to Trash (`main`, output 0, input 0)
- Trash/Flag Duplicates → Is Flagged (`main`, output 1, input 0)
- Deduplicate Keep First → Edit Fields (`main`, output 0, input 0)
- Drop Google Apps files → Keep First/Last (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0848_Code_Filter_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0848_Code_Filter_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
