# Clone this spreadsheet

This folder contains the **Clone this spreadsheet** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clone-this-spreadsheet.json`](clone-this-spreadsheet.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `shopifyAccessTokenApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Orders | `httpRequest` | Inspect parameters |
| Extract page_info  | `code` | Inspect parameters |
| Merge Loop items | `code` | Inspect parameters |
| List Orders | `splitOut` | Inspect parameters |
| Google Sheets | `googleSheets` | appendOrUpdate |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Assign page_info parameter | `set` | Inspect parameters |
| Check page_info existence | `if` | Inspect parameters |

## Connection map

- Get Orders → Check page_info existence (`main`, output 0, input 0)
- List Orders → Google Sheets (`main`, output 0, input 0)
- Merge Loop items → List Orders (`main`, output 0, input 0)
- Schedule Trigger → Get Orders (`main`, output 0, input 0)
- Extract page_info  → Assign page_info parameter (`main`, output 0, input 0)
- Check page_info existence → Merge Loop items (`main`, output 0, input 0)
- Check page_info existence → Extract page_info  (`main`, output 1, input 0)
- Assign page_info parameter → Get Orders (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Orders (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0792_Splitout_Code_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0792_Splitout_Code_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
