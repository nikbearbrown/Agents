# Generate Leads with Google Maps - AlexK1919

This folder contains the **Generate Leads with Google Maps - AlexK1919** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `httpRequest`, `if`, `limit`, `manualTrigger`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `stopAndError`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-leads-with-google-maps-alexk1919.json`](generate-leads-with-google-maps-alexk1919.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** When clicking "Execute Workflow", Run workflow every hours, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Run workflow every hours | `scheduleTrigger` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Check Max Retries1 | `if` | Inspect parameters |
| Stop and Error1 | `stopAndError` | Inspect parameters |
| GMaps API | `httpRequest` | POST |
| Update Status to Success | `googleSheets` | update |
| Add rows in Google Sheets | `googleSheets` | appendOrUpdate |
| Set Row Number | `set` | Inspect parameters |
| Set Zip | `set` | Inspect parameters |
| Set Place ID | `set` | Inspect parameters |
| Exponential Backoff | `code` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Check Max Retries | `if` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Exponential Backoff1 | `code` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| GS - Get Subcategory | `googleSheets` | Inspect parameters |
| Subcategory | `set` | Inspect parameters |
| GS - Get Zip Codes | `googleSheets` | Inspect parameters |
| Place Array | `code` | Inspect parameters |
| Loop Zips | `splitInBatches` | Inspect parameters |
| Loop Subcats | `splitInBatches` | Inspect parameters |
| GS - Get Status | `googleSheets` | Inspect parameters |
| Check Max Retries2 | `if` | Inspect parameters |
| Stop and Error2 | `stopAndError` | Inspect parameters |
| Exponential Backoff2 | `code` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Zips | `set` | Inspect parameters |
| Filter Zips | `filter` | Inspect parameters |
| Filter Subcategories | `filter` | Inspect parameters |
| If Empty | `if` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |

## Connection map

- Wait → Check Max Retries1 (`main`, output 0, input 0)
- Zips → Filter Zips (`main`, output 0, input 0)
- Limit → Loop Zips (`main`, output 0, input 0)
- Wait1 → Check Max Retries (`main`, output 0, input 0)
- Wait2 → Check Max Retries2 (`main`, output 0, input 0)
- Set Zip → GMaps API (`main`, output 0, input 0)
- If Empty → Loop Subcats (`main`, output 0, input 0)
- If Empty → Place Array (`main`, output 1, input 0)
- Settings → GS - Get Zip Codes (`main`, output 0, input 0)
- GMaps API → If Empty (`main`, output 0, input 0)
- Loop Zips → GS - Get Subcategory (`main`, output 1, input 0)
- Split Out → Limit (`main`, output 0, input 0)
- Filter Zips → Set Row Number (`main`, output 0, input 0)
- Place Array → Set Place ID (`main`, output 0, input 0)
- Subcategory → Loop Subcats (`main`, output 0, input 0)
- Loop Subcats → Loop Zips (`main`, output 0, input 0)
- Loop Subcats → Set Zip (`main`, output 1, input 0)
- Set Place ID → Remove Duplicates (`main`, output 0, input 0)
- Set Row Number → Split Out (`main`, output 0, input 0)
- GS - Get Status → Update Status to Success (`main`, output 0, input 0)
- GS - Get Status → Exponential Backoff2 (`main`, output 1, input 0)
- Check Max Retries → Stop and Error (`main`, output 0, input 0)
- Check Max Retries → Update Status to Success (`main`, output 1, input 0)
- Remove Duplicates → Add rows in Google Sheets (`main`, output 0, input 0)
- Check Max Retries1 → Stop and Error1 (`main`, output 0, input 0)
- Check Max Retries1 → Add rows in Google Sheets (`main`, output 1, input 0)
- Check Max Retries2 → Stop and Error2 (`main`, output 0, input 0)
- GS - Get Zip Codes → Zips (`main`, output 0, input 0)
- Exponential Backoff → Wait (`main`, output 0, input 0)
- Exponential Backoff1 → Wait1 (`main`, output 0, input 0)
- Exponential Backoff2 → Wait2 (`main`, output 0, input 0)
- Filter Subcategories → Subcategory (`main`, output 0, input 0)
- GS - Get Subcategory → Filter Subcategories (`main`, output 0, input 0)
- Execute Workflow Trigger → Settings (`main`, output 0, input 0)
- Run workflow every hours → Settings (`main`, output 0, input 0)
- Update Status to Success → Loop Subcats (`main`, output 0, input 0)
- Update Status to Success → Exponential Backoff1 (`main`, output 1, input 0)
- Add rows in Google Sheets → GS - Get Status (`main`, output 0, input 0)
- Add rows in Google Sheets → Exponential Backoff (`main`, output 1, input 0)
- When clicking "Execute Workflow" → Settings (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1823_Stopanderror_Wait_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1823_Stopanderror_Wait_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
