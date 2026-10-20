# Scrape Trustpilot Reviews to Google Sheets

This folder contains the **Scrape Trustpilot Reviews to Google Sheets** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `manualTrigger`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-trustpilot-reviews-to-google-sheets.json`](scrape-trustpilot-reviews-to-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get reviews | `httpRequest` | Inspect parameters |
| Global | `set` | Inspect parameters |
| Parse reviews | `code` | Inspect parameters |
| HelpfulCrowd edits | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| General edits | `set` | Inspect parameters |
| General sheet | `googleSheets` | appendOrUpdate |
| HelpfulCrowd Sheets | `googleSheets` | appendOrUpdate |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Global → Get reviews (`main`, output 0, input 0)
- Split Out → HelpfulCrowd edits (`main`, output 0, input 0)
- Split Out → General edits (`main`, output 0, input 0)
- Get reviews → Parse reviews (`main`, output 0, input 0)
- General edits → General sheet (`main`, output 0, input 0)
- Parse reviews → Split Out (`main`, output 0, input 0)
- Schedule Trigger → Global (`main`, output 0, input 0)
- HelpfulCrowd edits → HelpfulCrowd Sheets (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Global (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1412_Splitout_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1412_Splitout_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
