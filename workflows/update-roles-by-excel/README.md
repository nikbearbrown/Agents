# Update Roles by Excel

This folder contains the **Update Roles by Excel** workflow. Its executable nodes use `extractFromFile`, `httpRequest`, `manualTrigger`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`update-roles-by-excel.json`](update-roles-by-excel.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Extract from File | `extractFromFile` | xlsx |
| Merge | `merge` | Inspect parameters |
| Basic Variables | `set` | Inspect parameters |
| Zammad Univeral User Object | `set` | Inspect parameters |
| Download Excel | `httpRequest` | Inspect parameters |
| Find Zammad User by email | `httpRequest` | Inspect parameters |
| Update User Roles | `httpRequest` | PUT |

## Connection map

- Merge → Update User Roles (`main`, output 0, input 0)
- Download Excel → Extract from File (`main`, output 0, input 0)
- Basic Variables → Download Excel (`main`, output 0, input 0)
- Extract from File → Zammad Univeral User Object (`main`, output 0, input 0)
- Find Zammad User by email → Merge (`main`, output 0, input 0)
- Zammad Univeral User Object → Merge (`main`, output 0, input 1)
- Zammad Univeral User Object → Find Zammad User by email (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Basic Variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2022_Manual_Extractfromfile_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2022_Manual_Extractfromfile_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
