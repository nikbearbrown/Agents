# 🔍 LinkedIn Jobs API – Parameter Guide

This folder contains the **🔍 LinkedIn Jobs API – Parameter Guide** workflow. Its executable nodes use `code`, `formTrigger`, `googleSheets`, `httpRequest`, `if`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-jobs-api-parameter-guide.json`](linkedin-jobs-api-parameter-guide.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** On form submission - Discover Jobs

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Snapshot Progress | `httpRequest` | Inspect parameters |
| On form submission - Discover Jobs | `formTrigger` | Inspect parameters |
| HTTP Request- Post API call to Bright Data | `httpRequest` | POST |
| Wait - Polling Bright Data | `wait` | Inspect parameters |
| If - Checking status of Snapshot - if data is ready or not | `if` | Inspect parameters |
| HTTP Request - Getting data from Bright Data | `httpRequest` | Inspect parameters |
| Code - Cleaning Up | `code` | Inspect parameters |
| Google Sheets - Adding All Job Posts | `googleSheets` | append |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- Edit Fields → HTTP Request- Post API call to Bright Data (`main`, output 0, input 0)
- Snapshot Progress → If - Checking status of Snapshot - if data is ready or not (`main`, output 0, input 0)
- Code - Cleaning Up → Google Sheets - Adding All Job Posts (`main`, output 0, input 0)
- Wait - Polling Bright Data → Snapshot Progress (`main`, output 0, input 0)
- On form submission - Discover Jobs → Edit Fields (`main`, output 0, input 0)
- HTTP Request- Post API call to Bright Data → Wait - Polling Bright Data (`main`, output 0, input 0)
- HTTP Request - Getting data from Bright Data → Code - Cleaning Up (`main`, output 0, input 0)
- If - Checking status of Snapshot - if data is ready or not → Wait - Polling Bright Data (`main`, output 0, input 0)
- If - Checking status of Snapshot - if data is ready or not → HTTP Request - Getting data from Bright Data (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0862_Wait_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0862_Wait_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
