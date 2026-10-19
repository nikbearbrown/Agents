# Structured Bulk Data Extract with Bright Data Web Scraper

This folder contains the **Structured Bulk Data Extract with Bright Data Web Scraper** workflow. Its executable nodes use `aggregate`, `function`, `httpRequest`, `if`, `manualTrigger`, `readWriteFile`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`structured-bulk-data-extract-with-bright-data-web-scraper.json`](structured-bulk-data-extract-with-bright-data-web-scraper.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Snapshot Id | `set` | Inspect parameters |
| Download Snapshot | `httpRequest` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Check on the errors | `if` | Inspect parameters |
| Check Snapshot Status | `httpRequest` | Inspect parameters |
| Initiate a Webhook Notification | `httpRequest` | Inspect parameters |
| Aggregate JSON Response | `aggregate` | Inspect parameters |
| Set Dataset Id, Request URL | `set` | Inspect parameters |
| Create a binary data | `function` | Inspect parameters |
| Write the file to disk | `readWriteFile` | write |
| HTTP Request to the specified URL | `httpRequest` | POST |

## Connection map

- If → Check on the errors (`main`, output 0, input 0)
- If → Wait (`main`, output 1, input 0)
- Wait → Check Snapshot Status (`main`, output 0, input 0)
- Set Snapshot Id → Check Snapshot Status (`main`, output 0, input 0)
- Download Snapshot → Aggregate JSON Response (`main`, output 0, input 0)
- Check on the errors → Download Snapshot (`main`, output 0, input 0)
- Create a binary data → Write the file to disk (`main`, output 0, input 0)
- Check Snapshot Status → If (`main`, output 0, input 0)
- Aggregate JSON Response → Initiate a Webhook Notification (`main`, output 0, input 0)
- Aggregate JSON Response → Create a binary data (`main`, output 0, input 0)
- Set Dataset Id, Request URL → HTTP Request to the specified URL (`main`, output 0, input 0)
- HTTP Request to the specified URL → Set Snapshot Id (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Dataset Id, Request URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1579_Wait_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1579_Wait_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
