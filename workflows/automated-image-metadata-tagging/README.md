# Automated Image Metadata Tagging

This folder contains the **Automated Image Metadata Tagging** workflow. Its executable nodes use `code`, `convertToFile`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `merge`, `openAi`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-image-metadata-tagging.json`](automated-image-metadata-tagging.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** Trigger: New file added to Google Drive Folder

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract from File | `extractFromFile` | binaryToPropery |
| Convert to File | `convertToFile` | toBinary |
| Analyze Image Content | `openAi` | image / analyze |
| Download Image File | `googleDrive` | download |
| Trigger: New file added to Google Drive Folder | `googleDriveTrigger` | Inspect parameters |
| Write Metadata to Base64 Code | `code` | Inspect parameters |
| Update Image File | `googleDrive` | update |
| Merge Metadata and Base64 Code | `merge` | Inspect parameters |

## Connection map

- Convert to File → Update Image File (`main`, output 0, input 0)
- Extract from File → Merge Metadata and Base64 Code (`main`, output 0, input 1)
- Download Image File → Analyze Image Content (`main`, output 0, input 0)
- Download Image File → Extract from File (`main`, output 0, input 0)
- Analyze Image Content → Merge Metadata and Base64 Code (`main`, output 0, input 0)
- Write Metadata to Base64 Code → Convert to File (`main`, output 0, input 0)
- Merge Metadata and Base64 Code → Write Metadata to Base64 Code (`main`, output 0, input 0)
- Trigger: New file added to Google Drive Folder → Download Image File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1761_Code_Extractfromfile_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1761_Code_Extractfromfile_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
