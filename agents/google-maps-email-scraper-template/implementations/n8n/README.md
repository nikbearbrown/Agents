# Google Maps Email Scraper Template

This folder contains the **Google Maps Email Scraper Template** workflow. Its executable nodes use `aggregate`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `httpRequest`, `manualTrigger`, `removeDuplicates`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-maps-email-scraper-template.json`](google-maps-email-scraper-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Starts scraper workflow, Run workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Remove Duplicate URLs | `removeDuplicates` | Inspect parameters |
| Loop over queries | `splitInBatches` | Inspect parameters |
| Search Google Maps with query | `httpRequest` | Inspect parameters |
| Scrape URLs from results | `code` | Inspect parameters |
| Filter irrelevant URLs | `filter` | Inspect parameters |
| Request web page for URL | `httpRequest` | Inspect parameters |
| Loop over URLs | `splitInBatches` | Inspect parameters |
| Loop over pages | `splitInBatches` | Inspect parameters |
| Scrape emails from page | `code` | Inspect parameters |
| Aggregate arrays of emails | `aggregate` | Inspect parameters |
| Split out into default data structure | `splitOut` | Inspect parameters |
| Remove duplicate emails | `removeDuplicates` | Inspect parameters |
| Filter irrelevant emails | `filter` | Inspect parameters |
| Save emails to Google Sheet | `googleSheets` | append |
| Starts scraper workflow | `executeWorkflowTrigger` | Inspect parameters |
| Run workflow | `manualTrigger` | Inspect parameters |
| Wait between executions | `wait` | Inspect parameters |
| Execute scraper for query | `executeWorkflow` | Inspect parameters |

## Connection map

- Run workflow → Loop over queries (`main`, output 0, input 0)
- Loop over URLs → Loop over pages (`main`, output 0, input 0)
- Loop over URLs → Request web page for URL (`main`, output 1, input 0)
- Loop over pages → Aggregate arrays of emails (`main`, output 0, input 0)
- Loop over pages → Scrape emails from page (`main`, output 1, input 0)
- Loop over queries → Execute scraper for query (`main`, output 1, input 0)
- Remove Duplicate URLs → Loop over URLs (`main`, output 0, input 0)
- Filter irrelevant URLs → Remove Duplicate URLs (`main`, output 0, input 0)
- Remove duplicate emails → Filter irrelevant emails (`main`, output 0, input 0)
- Scrape emails from page → Loop over pages (`main`, output 0, input 0)
- Starts scraper workflow → Search Google Maps with query (`main`, output 0, input 0)
- Wait between executions → Loop over queries (`main`, output 0, input 0)
- Filter irrelevant emails → Save emails to Google Sheet (`main`, output 0, input 0)
- Request web page for URL → Loop over URLs (`main`, output 0, input 0)
- Scrape URLs from results → Filter irrelevant URLs (`main`, output 0, input 0)
- Execute scraper for query → Wait between executions (`main`, output 0, input 0)
- Aggregate arrays of emails → Split out into default data structure (`main`, output 0, input 0)
- Search Google Maps with query → Scrape URLs from results (`main`, output 0, input 0)
- Split out into default data structure → Remove duplicate emails (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0639_Wait_Splitout_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0639_Wait_Splitout_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
