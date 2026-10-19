# google sheets and tofile spreadsheet file and dropbox

This folder contains the **google sheets and tofile spreadsheet file and dropbox** workflow. Its executable nodes use `dropbox`, `googleSheets`, `interval`, `spreadsheetFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-sheets-and-tofile-spreadsheet-file-and-dropbox.json`](google-sheets-and-tofile-spreadsheet-file-and-dropbox.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropboxApi`, `googleApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Read Sheet | `googleSheets` | Inspect parameters |
| Convert to XLS | `spreadsheetFile` | toFile |
| Upload Dropbox | `dropbox` | Inspect parameters |
| Trigger all 15 min | `interval` | Inspect parameters |

## Connection map

- Read Sheet → Convert to XLS (`main`, output 0, input 0)
- Convert to XLS → Upload Dropbox (`main`, output 0, input 0)
- Trigger all 15 min → Read Sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/0082_GoogleSheets_Interval_Process_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/0082_GoogleSheets_Interval_Process_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
