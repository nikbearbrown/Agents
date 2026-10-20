# 🏢 Company Decision Maker Discovery

This folder contains the **🏢 Company Decision Maker Discovery** workflow. Its executable nodes use `code`, `filter`, `googleSheets`, `googleSheetsTrigger`, `httpRequest`, `if`, `merge`, `openAi`, `scheduleTrigger`, `slack`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`company-decision-maker-discovery.json`](company-decision-maker-discovery.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Google Sheets Trigger, Weekly Report Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| Apollo Organization Enrichment | `httpRequest` | Inspect parameters |
| Create Apollo People Search URL | `code` | Inspect parameters |
| Loop Over Items (1000 per Batch) | `splitInBatches` | Inspect parameters |
| Apollo Find Decision Makers | `httpRequest` | POST |
| Add Contacts | `googleSheets` | appendOrUpdate |
| Apollo Enrich Decision Makers | `httpRequest` | POST |
| Create Apollo People Enrichment Payload | `code` | Inspect parameters |
| Enrich Contacts | `googleSheets` | appendOrUpdate |
| Loop Over Items For Bulk Enrichment (10 per batch) | `splitInBatches` | Inspect parameters |
| Determine Contact's Department | `openAi` | Inspect parameters |
| Apollo Organization Search | `httpRequest` | POST |
| Add Company Website | `googleSheets` | appendOrUpdate |
| Approve Company Website | `slack` | sendAndWait |
| Add Company Details | `googleSheets` | appendOrUpdate |
| Select Unprocessed Companies | `filter` | Inspect parameters |
| Is Domain Already Provided? | `if` | Inspect parameters |
| Summarize Core Business | `openAi` | Inspect parameters |
| Split Out Batched Decision Maker Response | `splitOut` | Inspect parameters |
| Split Out Batched Enrichment Response | `splitOut` | Inspect parameters |
| Send Weekly Report | `slack` | Inspect parameters |
| Retrieve Verified Leads | `googleSheets` | Inspect parameters |
| Derive Past Week's Lead Gen. Metrics | `code` | Inspect parameters |
| Weekly Report Trigger | `scheduleTrigger` | Inspect parameters |
| Merge Rows Which Now All Contain Domains | `merge` | Inspect parameters |

## Connection map

- Add Contacts → Loop Over Items For Bulk Enrichment (10 per batch) (`main`, output 0, input 0)
- Add Company Details → Loop Over Items (1000 per Batch) (`main`, output 0, input 0)
- Add Company Website → Approve Company Website (`main`, output 0, input 0)
- Add Company Website → Merge Rows Which Now All Contain Domains (`main`, output 0, input 0)
- Google Sheets Trigger → Select Unprocessed Companies (`main`, output 0, input 0)
- Weekly Report Trigger → Retrieve Verified Leads (`main`, output 0, input 0)
- Retrieve Verified Leads → Derive Past Week's Lead Gen. Metrics (`main`, output 0, input 0)
- Summarize Core Business → Add Company Details (`main`, output 0, input 0)
- Apollo Organization Search → Add Company Website (`main`, output 0, input 0)
- Apollo Find Decision Makers → Loop Over Items (1000 per Batch) (`main`, output 0, input 0)
- Is Domain Already Provided? → Merge Rows Which Now All Contain Domains (`main`, output 0, input 1)
- Is Domain Already Provided? → Apollo Organization Search (`main`, output 1, input 0)
- Select Unprocessed Companies → Is Domain Already Provided? (`main`, output 0, input 0)
- Apollo Enrich Decision Makers → Loop Over Items For Bulk Enrichment (10 per batch) (`main`, output 0, input 0)
- Apollo Organization Enrichment → Summarize Core Business (`main`, output 0, input 0)
- Determine Contact's Department → Add Contacts (`main`, output 0, input 0)
- Create Apollo People Search URL → Apollo Find Decision Makers (`main`, output 0, input 0)
- Loop Over Items (1000 per Batch) → Split Out Batched Decision Maker Response (`main`, output 0, input 0)
- Loop Over Items (1000 per Batch) → Create Apollo People Search URL (`main`, output 1, input 0)
- Derive Past Week's Lead Gen. Metrics → Send Weekly Report (`main`, output 0, input 0)
- Split Out Batched Enrichment Response → Enrich Contacts (`main`, output 0, input 0)
- Create Apollo People Enrichment Payload → Apollo Enrich Decision Makers (`main`, output 0, input 0)
- Merge Rows Which Now All Contain Domains → Apollo Organization Enrichment (`main`, output 0, input 0)
- Split Out Batched Decision Maker Response → Determine Contact's Department (`main`, output 0, input 0)
- Loop Over Items For Bulk Enrichment (10 per batch) → Split Out Batched Enrichment Response (`main`, output 0, input 0)
- Loop Over Items For Bulk Enrichment (10 per batch) → Create Apollo People Enrichment Payload (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0902_Splitout_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0902_Splitout_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
