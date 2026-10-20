# http request and filter leads by company criteria and clearbit

This folder contains the **http request and filter leads by company criteria and clearbit** workflow. Its executable nodes use `clearbit`, `filter`, `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-filter-leads-by-company-criteria-and-clearbit.json`](http-request-and-filter-leads-by-company-criteria-and-clearbit.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clearbitApi`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Leads | `httpRequest` | Inspect parameters |
| Filter Leads by company criteria | `filter` | Inspect parameters |
| Enrich company | `clearbit` | Inspect parameters |
| Setup | `set` | Inspect parameters |
| Get all Leedfeeder accounts | `httpRequest` | Inspect parameters |
| Only for wanted accounts | `filter` | Inspect parameters |
| Split out accounts | `splitOut` | Inspect parameters |
| Split Out Leads | `splitOut` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Filter leads by engagement | `filter` | Inspect parameters |
| Save leads to Google Sheets | `googleSheets` | appendOrUpdate |

## Connection map

- Setup → Get all Leedfeeder accounts (`main`, output 0, input 0)
- Get Leads → Split Out Leads (`main`, output 0, input 0)
- Enrich company → Filter Leads by company criteria (`main`, output 0, input 0)
- Split Out Leads → Filter leads by engagement (`main`, output 0, input 0)
- Schedule Trigger → Setup (`main`, output 0, input 0)
- Split out accounts → Only for wanted accounts (`main`, output 0, input 0)
- Only for wanted accounts → Get Leads (`main`, output 0, input 0)
- Filter leads by engagement → Enrich company (`main`, output 0, input 0)
- Get all Leedfeeder accounts → Split out accounts (`main`, output 0, input 0)
- Filter Leads by company criteria → Save leads to Google Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0418_Splitout_Filter_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0418_Splitout_Filter_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
