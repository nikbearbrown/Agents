# append google sheets tool and receive form events and completion form

This folder contains the **append google sheets tool and receive form events and completion form** workflow. Its executable nodes use `code`, `extractFromFile`, `filter`, `form`, `formTrigger`, `gmail`, `googleSheets`, `googleSheetsTool`, `informationExtractor`, `scheduleTrigger`, `set`, `summarize`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`append-google-sheets-tool-and-receive-form-events-and-completion-form.json`](append-google-sheets-tool-and-receive-form-events-and-completion-form.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`

**Entry nodes:** On form submission, Every End of Month

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Client Usage Log | `googleSheetsTool` | append |
| Logging Attributes | `set` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Custom LLM Subnode | `code` | Inspect parameters |
| Display JSON Document | `form` | completion |
| Filter Last Month | `filter` | Inspect parameters |
| Get Client Logs | `googleSheets` | Inspect parameters |
| Calculate Totals | `summarize` | Inspect parameters |
| Every End of Month | `scheduleTrigger` | Inspect parameters |
| Send Invoice | `gmail` | Inspect parameters |
| Parse PDF Upload | `extractFromFile` | pdf |
| Extract Resume Data | `informationExtractor` | Inspect parameters |

## Connection map

- Get Client Logs → Filter Last Month (`main`, output 0, input 0)
- Calculate Totals → Send Invoice (`main`, output 0, input 0)
- Client Usage Log → Custom LLM Subnode (`ai_tool`, output 0, input 0)
- Parse PDF Upload → Logging Attributes (`main`, output 0, input 0)
- Filter Last Month → Calculate Totals (`main`, output 0, input 0)
- Custom LLM Subnode → Extract Resume Data (`ai_languageModel`, output 0, input 0)
- Every End of Month → Get Client Logs (`main`, output 0, input 0)
- Logging Attributes → Extract Resume Data (`main`, output 0, input 0)
- On form submission → Parse PDF Upload (`main`, output 0, input 0)
- Extract Resume Data → Display JSON Document (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0830_Filter_Summarize_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0830_Filter_Summarize_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
