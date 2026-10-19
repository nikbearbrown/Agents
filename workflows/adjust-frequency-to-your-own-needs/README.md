# Adjust frequency to your own needs

This folder contains the **Adjust frequency to your own needs** workflow. Its executable nodes use `code`, `filter`, `googleSheets`, `httpRequest`, `if`, `itemLists`, `manualTrigger`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`adjust-frequency-to-your-own-needs.json`](adjust-frequency-to-your-own-needs.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `serpApi`

**Entry nodes:** When clicking "Execute Workflow", Run workflow every hours

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Extract next start value | `code` | Inspect parameters |
| Merge all values from SERPAPI | `code` | Inspect parameters |
| Transform data in the right format | `code` | Inspect parameters |
| Add rows in Google Sheets | `googleSheets` | appendOrUpdate |
| SERPAPI - Scrape Google Maps URL | `httpRequest` | Inspect parameters |
| Remove duplicate items | `itemLists` | removeDuplicates |
| Split out items | `itemLists` | Inspect parameters |
| Remove empty values | `filter` | Inspect parameters |
| Google Sheets - Get searches  to scrap | `googleSheets` | Inspect parameters |
| Extract keyword and location from URL | `set` | Inspect parameters |
| Run workflow every hours | `scheduleTrigger` | Inspect parameters |
| Update Status to Success | `googleSheets` | update |
| Update Status to Error | `googleSheets` | update |
| Continue IF Loop is complete | `if` | Inspect parameters |

## Connection map

- Split out items → Remove empty values (`main`, output 0, input 0)
- Remove empty values → Transform data in the right format (`main`, output 0, input 0)
- Remove duplicate items → Add rows in Google Sheets (`main`, output 0, input 0)
- Extract next start value → Continue IF Loop is complete (`main`, output 0, input 0)
- Run workflow every hours → Google Sheets - Get searches  to scrap (`main`, output 0, input 0)
- Add rows in Google Sheets → Update Status to Success (`main`, output 0, input 0)
- Continue IF Loop is complete → SERPAPI - Scrape Google Maps URL (`main`, output 0, input 0)
- Continue IF Loop is complete → Merge all values from SERPAPI (`main`, output 1, input 0)
- Merge all values from SERPAPI → Split out items (`main`, output 0, input 0)
- SERPAPI - Scrape Google Maps URL → Extract next start value (`main`, output 0, input 0)
- SERPAPI - Scrape Google Maps URL → Update Status to Error (`main`, output 1, input 0)
- When clicking "Execute Workflow" → Google Sheets - Get searches  to scrap (`main`, output 0, input 0)
- Transform data in the right format → Remove duplicate items (`main`, output 0, input 0)
- Extract keyword and location from URL → SERPAPI - Scrape Google Maps URL (`main`, output 0, input 0)
- Google Sheets - Get searches  to scrap → Extract keyword and location from URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0391_Code_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0391_Code_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
