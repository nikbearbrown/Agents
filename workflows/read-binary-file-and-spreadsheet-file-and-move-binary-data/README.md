# read binary file and spreadsheet file and move binary data

This folder contains the **read binary file and spreadsheet file and move binary data** workflow. Its executable nodes use `manualTrigger`, `moveBinaryData`, `readBinaryFile`, `spreadsheetFile`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`read-binary-file-and-spreadsheet-file-and-move-binary-data.json`](read-binary-file-and-spreadsheet-file-and-move-binary-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Read Binary File | `readBinaryFile` | Inspect parameters |
| Spreadsheet File1 | `spreadsheetFile` | Inspect parameters |
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| Write Binary File | `writeBinaryFile` | Inspect parameters |

## Connection map

- Move Binary Data → Write Binary File (`main`, output 0, input 0)
- Read Binary File → Spreadsheet File1 (`main`, output 0, input 0)
- Spreadsheet File1 → Move Binary Data (`main`, output 0, input 0)
- On clicking 'execute' → Read Binary File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Readbinaryfile/0220_Readbinaryfile_Manual_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Readbinaryfile/0220_Readbinaryfile_Manual_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
