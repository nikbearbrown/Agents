# item lists and piloterr get recent fundraise serie a and piloterr get recent fundraise serie b

This folder contains the **item lists and piloterr get recent fundraise serie a and piloterr get recent fundraise serie b** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `itemLists`, `merge`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`item-lists-and-piloterr-get-recent-fundraise-serie-a-and-piloterr-get-recent-fundraise-serie-b.json`](item-lists-and-piloterr-get-recent-fundraise-serie-a-and-piloterr-get-recent-fundraise-serie-b.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Schedule Trigger - Run Workflow Every Day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split results | `itemLists` | Inspect parameters |
| Piloterr - Get Recent Fundraise - Serie A | `httpRequest` | Inspect parameters |
| Piloterr - Get Recent Fundraise - Serie B | `httpRequest` | Inspect parameters |
| Google Sheets | `googleSheets` | appendOrUpdate |
| Piloterr - Get Recent Fundraise - Seed | `httpRequest` | Inspect parameters |
| Prepare data | `set` | Inspect parameters |
| Piloterr - Enrich company | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Schedule Trigger - Run Workflow Every Day | `scheduleTrigger` | Inspect parameters |
| Prepare data before importing to Gsheets | `set` | Inspect parameters |
| Get Linkedin URL from object | `code` | Inspect parameters |

## Connection map

- Merge → Google Sheets (`main`, output 0, input 0)
- Prepare data → Piloterr - Enrich company (`main`, output 0, input 0)
- Prepare data → Merge (`main`, output 0, input 0)
- Split results → Prepare data (`main`, output 0, input 0)
- Piloterr - Enrich company → Get Linkedin URL from object (`main`, output 0, input 0)
- Get Linkedin URL from object → Prepare data before importing to Gsheets (`main`, output 0, input 0)
- Piloterr - Get Recent Fundraise - Seed → Split results (`main`, output 0, input 0)
- Prepare data before importing to Gsheets → Merge (`main`, output 0, input 1)
- Piloterr - Get Recent Fundraise - Serie A → Split results (`main`, output 0, input 0)
- Piloterr - Get Recent Fundraise - Serie B → Split results (`main`, output 0, input 0)
- Schedule Trigger - Run Workflow Every Day → Piloterr - Get Recent Fundraise - Serie A (`main`, output 0, input 0)
- Schedule Trigger - Run Workflow Every Day → Piloterr - Get Recent Fundraise - Serie B (`main`, output 0, input 0)
- Schedule Trigger - Run Workflow Every Day → Piloterr - Get Recent Fundraise - Seed (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0397_Code_Schedule_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0397_Code_Schedule_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
