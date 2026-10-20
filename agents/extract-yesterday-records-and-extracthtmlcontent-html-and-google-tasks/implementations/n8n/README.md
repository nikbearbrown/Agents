# extract yesterday records and extracthtmlcontent html and google tasks

This folder contains the **extract yesterday records and extracthtmlcontent html and google tasks** workflow. Its executable nodes use `googleSheets`, `googleTasks`, `html`, `httpRequest`, `if`, `manualTrigger`, `merge`, `openAi`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-yesterday-records-and-extracthtmlcontent-html-and-google-tasks.json`](extract-yesterday-records-and-extracthtmlcontent-html-and-google-tasks.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| If | `if` | Inspect parameters |
| Extract Yesterday Records | `httpRequest` | Inspect parameters |
| Extract HTML Blocks | `html` | extractHtmlContent |
| Parse Blocks | `html` | extractHtmlContent |
| Google Tasks | `googleTasks` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Classification Agent | `openAi` | Inspect parameters |
| Collect Answer | `set` | Inspect parameters |
| Record Sustainability Procedures | `googleSheets` | append |
| Edit Links | `set` | Inspect parameters |

## Connection map

- If → Record Sustainability Procedures (`main`, output 0, input 0)
- If → Google Tasks (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- Merge → If (`main`, output 0, input 0)
- Edit Links → Loop Over Items (`main`, output 0, input 0)
- Google Tasks → Loop Over Items (`main`, output 0, input 0)
- Parse Blocks → Edit Links (`main`, output 0, input 0)
- Collect Answer → Merge (`main`, output 0, input 1)
- Loop Over Items → Classification Agent (`main`, output 1, input 0)
- Loop Over Items → Merge (`main`, output 1, input 0)
- Extract HTML Blocks → Parse Blocks (`main`, output 0, input 0)
- Classification Agent → Collect Answer (`main`, output 0, input 0)
- Extract Yesterday Records → Extract HTML Blocks (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Extract Yesterday Records (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletasks/0881_Googletasks_HTTP_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletasks/0881_Googletasks_HTTP_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
