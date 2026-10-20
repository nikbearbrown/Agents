# http request and update google sheets and append google sheets

This folder contains the **http request and update google sheets and append google sheets** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `merge`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-update-google-sheets-and-append-google-sheets.json`](http-request-and-update-google-sheets-and-append-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Trigger - 08:00 am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter Fields | `set` | Inspect parameters |
| Final Outputs | `merge` | Inspect parameters |
| USD Query | `httpRequest` | Inspect parameters |
| Update Rate Sheet | `googleSheets` | update |
| Archive Rates | `googleSheets` | append |
| Format Output to JSON | `code` | Inspect parameters |
| Trigger - 08:00 am | `scheduleTrigger` | Inspect parameters |

## Connection map

- USD Query → Format Output to JSON (`main`, output 0, input 0)
- USD Query → Filter Fields (`main`, output 0, input 0)
- Filter Fields → Final Outputs (`main`, output 0, input 0)
- Final Outputs → Update Rate Sheet (`main`, output 0, input 0)
- Final Outputs → Archive Rates (`main`, output 0, input 0)
- Trigger - 08:00 am → USD Query (`main`, output 0, input 0)
- Format Output to JSON → Final Outputs (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0856_Code_Schedule_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0856_Code_Schedule_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
