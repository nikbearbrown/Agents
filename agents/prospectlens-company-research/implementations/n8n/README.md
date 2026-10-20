# ProspectLens company research

This folder contains the **ProspectLens company research** workflow. Its executable nodes use `filter`, `googleSheets`, `httpRequest`, `manualTrigger`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`prospectlens-company-research.json`](prospectlens-company-research.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Save company data into Sheets | `googleSheets` | update |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| ProspectLens API call | `httpRequest` | Inspect parameters |
| Get all rows from Sheets | `googleSheets` | Inspect parameters |

## Connection map

- Filter → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → ProspectLens API call (`main`, output 1, input 0)
- ProspectLens API call → Save company data into Sheets (`main`, output 0, input 0)
- ProspectLens API call → Loop Over Items (`main`, output 1, input 0)
- Get all rows from Sheets → Filter (`main`, output 0, input 0)
- Save company data into Sheets → Loop Over Items (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all rows from Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/2006_Filter_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/2006_Filter_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
