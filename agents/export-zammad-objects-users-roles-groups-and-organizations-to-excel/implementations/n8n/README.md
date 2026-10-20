# Export Zammad Objects Users, Roles, Groups and Organizations to Excel

This folder contains the **Export Zammad Objects Users, Roles, Groups and Organizations to Excel** workflow. Its executable nodes use `convertToFile`, `httpRequest`, `if`, `manualTrigger`, `set`, `zammad`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`export-zammad-objects-users-roles-groups-and-organizations-to-excel.json`](export-zammad-objects-users-roles-groups-and-organizations-to-excel.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `zammadTokenAuthApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Zammad Univeral User Object | `set` | Inspect parameters |
| Zammad Univeral Organization Object | `set` | Inspect parameters |
| Zammad Univeral Role Object | `set` | Inspect parameters |
| Get all Organizations | `zammad` | organization / getAll |
| Get all Roles | `httpRequest` | Inspect parameters |
| Convert to Excel Organizations | `convertToFile` | xlsx |
| Convert to Excel Roles | `convertToFile` | xlsx |
| Convert to Excel Users | `convertToFile` | xlsx |
| Get all Users | `zammad` | getAll |
| Zammad Univeral Group Object | `set` | Inspect parameters |
| Get all Groups | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| Basic Variables | `set` | Inspect parameters |
| Convert to Excel Groups | `convertToFile` | xlsx |
| Filter Groups if needed | `if` | Inspect parameters |
| Filter Roles if needed | `if` | Inspect parameters |
| Filter Organizations if needed | `if` | Inspect parameters |

## Connection map

- If → Convert to Excel Users (`main`, output 0, input 0)
- Get all Roles → Zammad Univeral Role Object (`main`, output 0, input 0)
- Get all Users → Zammad Univeral User Object (`main`, output 0, input 0)
- Get all Groups → Zammad Univeral Group Object (`main`, output 0, input 0)
- Basic Variables → Get all Roles (`main`, output 0, input 0)
- Basic Variables → Get all Groups (`main`, output 0, input 0)
- Get all Organizations → Zammad Univeral Organization Object (`main`, output 0, input 0)
- Filter Roles if needed → Convert to Excel Roles (`main`, output 0, input 0)
- Filter Groups if needed → Convert to Excel Groups (`main`, output 0, input 0)
- Zammad Univeral Role Object → Filter Roles if needed (`main`, output 0, input 0)
- Zammad Univeral User Object → If (`main`, output 0, input 0)
- Zammad Univeral Group Object → Filter Groups if needed (`main`, output 0, input 0)
- Filter Organizations if needed → Convert to Excel Organizations (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all Users (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Basic Variables (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all Organizations (`main`, output 0, input 0)
- Zammad Univeral Organization Object → Filter Organizations if needed (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1503_Manual_HTTP_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1503_Manual_HTTP_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
