# Append, lookup, update, and read data from a Google Sheets spreadsheet

This folder contains the **Append, lookup, update, and read data from a Google Sheets spreadsheet** workflow. Its executable nodes use `googleSheets`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`append-lookup-update-and-read-data-from-a-google-sheets-spreadsheet.json`](append-lookup-update-and-read-data-from-a-google-sheets-spreadsheet.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Google Sheets2 | `googleSheets` | update |
| Set1 | `set` | Inspect parameters |
| Google Sheets1 | `googleSheets` | lookup |
| Google Sheets | `googleSheets` | append |
| Google Sheets3 | `googleSheets` | Inspect parameters |
| Set | `set` | Inspect parameters |

## Connection map

- Set → Google Sheets (`main`, output 0, input 0)
- Set1 → Google Sheets2 (`main`, output 0, input 0)
- Google Sheets → Google Sheets1 (`main`, output 0, input 0)
- Google Sheets1 → Set1 (`main`, output 0, input 0)
- Google Sheets2 → Google Sheets3 (`main`, output 0, input 0)
- On clicking 'execute' → Set (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1062_Manual_GoogleSheets_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1062_Manual_GoogleSheets_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
