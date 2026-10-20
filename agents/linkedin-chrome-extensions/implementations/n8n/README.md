# Linkedin Chrome Extensions

This folder contains the **Linkedin Chrome Extensions** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `limit`, `manualTrigger`, `merge`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-chrome-extensions.json`](linkedin-chrome-extensions.json): sanitized, inactive import copy with an overview sticky note.
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
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Set extension IDs var | `code` | Inspect parameters |
| Load already processed items | `googleSheets` | Inspect parameters |
| Exclude processed items | `merge` | Inspect parameters |
| SERP Request | `httpRequest` | Inspect parameters |
| Upsert to Google Sheets | `googleSheets` | appendOrUpdate |

## Connection map

- Limit → Loop Over Items (`main`, output 0, input 0)
- SERP Request → Upsert to Google Sheets (`main`, output 0, input 0)
- Loop Over Items → SERP Request (`main`, output 1, input 0)
- Set extension IDs var → Exclude processed items (`main`, output 0, input 0)
- Exclude processed items → Limit (`main`, output 0, input 0)
- Upsert to Google Sheets → Loop Over Items (`main`, output 0, input 0)
- Load already processed items → Exclude processed items (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Set extension IDs var (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Load already processed items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1483_Limit_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1483_Limit_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
