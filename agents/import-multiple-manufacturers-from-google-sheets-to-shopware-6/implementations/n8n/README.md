# Import multiple Manufacturers from Google Sheets to Shopware 6

This folder contains the **Import multiple Manufacturers from Google Sheets to Shopware 6** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `if`, `manualTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`import-multiple-manufacturers-from-google-sheets-to-shopware-6.json`](import-multiple-manufacturers-from-google-sheets-to-shopware-6.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `oAuth2Api`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Create Import Request Body | `code` | Inspect parameters |
| Upload Manufacturer Logo | `httpRequest` | POST |
| Import Manufacturer | `httpRequest` | POST |
| Loop Over Manufacturers | `splitInBatches` | Inspect parameters |
| Get Manufacturer from Google Sheet | `googleSheets` | Inspect parameters |
| If has Logo | `if` | Inspect parameters |

## Connection map

- Settings → Get Manufacturer from Google Sheet (`main`, output 0, input 0)
- If has Logo → Upload Manufacturer Logo (`main`, output 0, input 0)
- If has Logo → Loop Over Manufacturers (`main`, output 1, input 0)
- Import Manufacturer → If has Logo (`main`, output 0, input 0)
- Loop Over Manufacturers → Import Manufacturer (`main`, output 1, input 0)
- Upload Manufacturer Logo → Loop Over Manufacturers (`main`, output 0, input 0)
- Create Import Request Body → Loop Over Manufacturers (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Settings (`main`, output 0, input 0)
- Get Manufacturer from Google Sheet → Create Import Request Body (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2011_Code_Manual_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2011_Code_Manual_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
