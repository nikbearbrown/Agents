# Extract expenses from emails and add to Google Sheet

This folder contains the **Extract expenses from emails and add to Google Sheet** workflow. Its executable nodes use `emailReadImap`, `googleSheets`, `if`, `mindee`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-expenses-from-emails-and-add-to-google-sheet.json`](extract-expenses-from-emails-and-add-to-google-sheet.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `imap`, `mindeeReceiptApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check subject | `if` | Inspect parameters |
| Setup Variables | `set` | Inspect parameters |
| Check for new emails | `emailReadImap` | Inspect parameters |
| Read Receipts | `mindee` | Inspect parameters |
| Set column data | `set` | Inspect parameters |
| Add to Google Sheet | `googleSheets` | append |

## Connection map

- Check subject → Read Receipts (`main`, output 0, input 0)
- Read Receipts → Set column data (`main`, output 0, input 0)
- Set column data → Add to Google Sheet (`main`, output 0, input 0)
- Setup Variables → Check subject (`main`, output 0, input 0)
- Check for new emails → Setup Variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/1188_GoogleSheets_Emailreadimap_Create.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/1188_GoogleSheets_Emailreadimap_Create.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
