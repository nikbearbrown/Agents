# Search console REPORTS

This folder contains the **Search console REPORTS** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-console-reports.json`](search-console-reports.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `googleOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Split Out2 | `splitOut` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |
| date | `httpRequest` | POST |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Set your domain | `set` | Inspect parameters |
| Get query Report | `httpRequest` | POST |
| Get Page Report | `httpRequest` | POST |
| Update queries to Sheets | `googleSheets` | appendOrUpdate |
| Update Pages to Sheets  | `googleSheets` | appendOrUpdate |
| Update date report to sheets | `googleSheets` | appendOrUpdate |

## Connection map

- date → Split Out2 (`main`, output 0, input 0)
- Split Out → Edit Fields (`main`, output 0, input 0)
- Split Out1 → Edit Fields1 (`main`, output 0, input 0)
- Split Out2 → Edit Fields2 (`main`, output 0, input 0)
- Edit Fields → Update queries to Sheets (`main`, output 0, input 0)
- Edit Fields1 → Update Pages to Sheets  (`main`, output 0, input 0)
- Edit Fields2 → Update date report to sheets (`main`, output 0, input 0)
- Get Page Report → Split Out1 (`main`, output 0, input 0)
- Set your domain → Get query Report (`main`, output 0, input 0)
- Set your domain → Get Page Report (`main`, output 0, input 0)
- Set your domain → date (`main`, output 0, input 0)
- Get query Report → Split Out (`main`, output 0, input 0)
- Schedule Trigger → Set your domain (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0657_Splitout_Schedule_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0657_Splitout_Schedule_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
