# 🚨 Change your Base ID and Table ID here!

This folder contains the **🚨 Change your Base ID and Table ID here!** workflow. Its executable nodes use `aggregate`, `airtable`, `code`, `filter`, `form`, `formTrigger`, `httpRequest`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`change-your-base-id-and-table-id-here.json`](change-your-base-id-and-table-id-here.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`

**Entry nodes:** On form submission, On form submission1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Base Schema | `airtable` | base / getSchema |
| On form submission | `formTrigger` | Inspect parameters |
| Filter Unsupported FieldTypes | `filter` | Inspect parameters |
| Combine Fields | `aggregate` | Inspect parameters |
| Render Form | `form` | Inspect parameters |
| Files To List | `code` | Inspect parameters |
| Fields to List | `splitOut` | Inspect parameters |
| Covert to n8n Form Fields | `code` | Inspect parameters |
| Filter Table | `filter` | Inspect parameters |
| Baserow List Fields | `httpRequest` | Inspect parameters |
| Covert to n8n Form Fields1 | `code` | Inspect parameters |
| Combine Fields1 | `aggregate` | Inspect parameters |
| Filter Unsupported FieldTypes1 | `filter` | Inspect parameters |
| Render Form1 | `form` | Inspect parameters |
| Baserow Create Row | `httpRequest` | POST |
| On form submission1 | `formTrigger` | Inspect parameters |
| Files To List1 | `code` | Inspect parameters |
| Baserow Upload File | `httpRequest` | POST |
| Baserow Update Row | `httpRequest` | PATCH |
| Group By FieldName | `code` | Inspect parameters |
| Update Airtable Row | `httpRequest` | POST |
| Prep Data for Insert1 | `code` | Inspect parameters |
| Prep Data for Insert | `code` | Inspect parameters |
| Airtable Create Record | `airtable` | create |
| Show Completion! | `form` | completion |
| Show Completion!1 | `form` | completion |

## Connection map

- Render Form → Prep Data for Insert (`main`, output 0, input 0)
- Filter Table → Fields to List (`main`, output 0, input 0)
- Render Form1 → Prep Data for Insert1 (`main`, output 0, input 0)
- Files To List → Update Airtable Row (`main`, output 0, input 0)
- Combine Fields → Render Form (`main`, output 0, input 0)
- Fields to List → Covert to n8n Form Fields (`main`, output 0, input 0)
- Files To List1 → Baserow Upload File (`main`, output 0, input 0)
- Combine Fields1 → Render Form1 (`main`, output 0, input 0)
- Get Base Schema → Filter Table (`main`, output 0, input 0)
- Baserow Create Row → Files To List1 (`main`, output 0, input 0)
- Baserow Update Row → Show Completion! (`main`, output 0, input 0)
- Group By FieldName → Baserow Update Row (`main`, output 0, input 0)
- On form submission → Get Base Schema (`main`, output 0, input 0)
- Baserow List Fields → Covert to n8n Form Fields1 (`main`, output 0, input 0)
- Baserow Upload File → Group By FieldName (`main`, output 0, input 0)
- On form submission1 → Baserow List Fields (`main`, output 0, input 0)
- Update Airtable Row → Show Completion!1 (`main`, output 0, input 0)
- Prep Data for Insert → Airtable Create Record (`main`, output 0, input 0)
- Prep Data for Insert1 → Baserow Create Row (`main`, output 0, input 0)
- Airtable Create Record → Files To List (`main`, output 0, input 0)
- Covert to n8n Form Fields → Filter Unsupported FieldTypes (`main`, output 0, input 0)
- Covert to n8n Form Fields1 → Filter Unsupported FieldTypes1 (`main`, output 0, input 0)
- Filter Unsupported FieldTypes → Combine Fields (`main`, output 0, input 0)
- Filter Unsupported FieldTypes1 → Combine Fields1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0654_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0654_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
