# Import Productboard Notes, Companies and Features into Snowflake

This folder contains the **Import Productboard Notes, Companies and Features into Snowflake** workflow. Its executable nodes use `httpRequest`, `scheduleTrigger`, `set`, `slack`, `snowflake`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`import-productboard-notes-companies-and-features-into-snowflake.json`](import-productboard-notes-companies-and-features-into-snowflake.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `slackApi`, `snowflake`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual mapping feature | `set` | Inspect parameters |
| get productboard companies | `httpRequest` | Inspect parameters |
| Manual mapping companies | `set` | Inspect parameters |
| get productboard notes | `httpRequest` | Inspect parameters |
| Manual mapping notes | `set` | Inspect parameters |
| Split features | `splitOut` | Inspect parameters |
| Split companies | `splitOut` | Inspect parameters |
| Split notes | `splitOut` | Inspect parameters |
| Split features in notes | `splitOut` | Inspect parameters |
| Combine Feature ID + Note ID | `set` | Inspect parameters |
| get productboard features | `httpRequest` | Inspect parameters |
| Update Productboard Notes | `snowflake` | Inspect parameters |
| Empty Table Productboard Notes | `snowflake` | executeQuery |
| [CREATE] PRODUCTBOARD_NOTES | `snowflake` | executeQuery |
| [CREATE] PRODUCTBOARD_COMPANIES | `snowflake` | executeQuery |
| Update Productboard Companies | `snowflake` | Inspect parameters |
| Manual mapping companies db | `set` | Inspect parameters |
| Manual mapping notes db | `set` | Inspect parameters |
| Empty Table Productboard Companies | `snowflake` | executeQuery |
| [CREATE] PRODUCTBOARD_NOTES_FEATURES | `snowflake` | executeQuery |
| Manual mapping feature note IDs db | `set` | Inspect parameters |
| Update Productboard Note and Feature IDs | `snowflake` | Inspect parameters |
| Empty Table Productboard Note and Feature IDs | `snowflake` | executeQuery |
| Loop Over Items notes | `splitInBatches` | Inspect parameters |
| Loop Over Items features notes | `splitInBatches` | Inspect parameters |
| [CREATE] PRODUCTBOARD_FEATURES | `snowflake` | executeQuery |
| Empty Table Productboard Features | `snowflake` | executeQuery |
| Loop Over Items features | `splitInBatches` | Inspect parameters |
| Manual mapping features db | `set` | Inspect parameters |
| Update Productboard Features | `snowflake` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Count Notes Last 7 days and Unprocessed | `snowflake` | executeQuery |

## Connection map

- Split notes → Manual mapping notes (`main`, output 0, input 0)
- Split notes → Split features in notes (`main`, output 0, input 0)
- Split notes → Count Notes Last 7 days and Unprocessed (`main`, output 0, input 0)
- Split features → Manual mapping feature (`main`, output 0, input 0)
- Split companies → Manual mapping companies (`main`, output 0, input 0)
- Schedule Trigger → Empty Table Productboard Features (`main`, output 0, input 0)
- Manual mapping notes → Loop Over Items notes (`main`, output 0, input 0)
- Loop Over Items notes → Manual mapping notes db (`main`, output 1, input 0)
- Manual mapping feature → Loop Over Items features (`main`, output 0, input 0)
- get productboard notes → Split notes (`main`, output 0, input 0)
- Manual mapping notes db → Update Productboard Notes (`main`, output 0, input 0)
- Split features in notes → Combine Feature ID + Note ID (`main`, output 0, input 0)
- Loop Over Items features → Empty Table Productboard Companies (`main`, output 0, input 0)
- Loop Over Items features → Manual mapping features db (`main`, output 1, input 0)
- Manual mapping companies → Manual mapping companies db (`main`, output 0, input 0)
- Update Productboard Notes → Loop Over Items notes (`main`, output 0, input 0)
- get productboard features → Split features (`main`, output 0, input 0)
- Manual mapping features db → Update Productboard Features (`main`, output 0, input 0)
- get productboard companies → Split companies (`main`, output 0, input 0)
- Manual mapping companies db → Update Productboard Companies (`main`, output 0, input 0)
- Combine Feature ID + Note ID → Loop Over Items features notes (`main`, output 0, input 0)
- Update Productboard Features → Loop Over Items features (`main`, output 0, input 0)
- Update Productboard Companies → Empty Table Productboard Note and Feature IDs (`main`, output 0, input 0)
- Empty Table Productboard Notes → get productboard notes (`main`, output 0, input 0)
- Loop Over Items features notes → Manual mapping feature note IDs db (`main`, output 1, input 0)
- Empty Table Productboard Features → get productboard features (`main`, output 0, input 0)
- Empty Table Productboard Companies → get productboard companies (`main`, output 0, input 0)
- Manual mapping feature note IDs db → Update Productboard Note and Feature IDs (`main`, output 0, input 0)
- Count Notes Last 7 days and Unprocessed → Slack (`main`, output 0, input 0)
- Update Productboard Note and Feature IDs → Loop Over Items features notes (`main`, output 0, input 0)
- Empty Table Productboard Note and Feature IDs → Empty Table Productboard Notes (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0643_Splitout_Snowflake_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0643_Splitout_Snowflake_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
