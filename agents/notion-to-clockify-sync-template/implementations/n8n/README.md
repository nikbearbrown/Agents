# Notion to Clockify Sync Template

This folder contains the **Notion to Clockify Sync Template** workflow. Its executable nodes use `clockify`, `compareDatasets`, `httpRequest`, `if`, `limit`, `merge`, `noOp`, `notion`, `scheduleTrigger`, `set`, `stopAndError`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`notion-to-clockify-sync-template.json`](notion-to-clockify-sync-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clockifyApi`, `notionApi`

**Entry nodes:** Webhook, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get first workspace ID | `clockify` | workspace |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Structure output | `noOp` | Inspect parameters |
| Map values | `set` | Inspect parameters |
| Map values1 | `set` | Inspect parameters |
| No Operation | `noOp` | Inspect parameters |
| Get active Clients from Notion | `notion` | databasePage / getAll |
| Get active Clients from Clockify | `clockify` | client / getAll |
| If unmapped in Notion | `if` | Inspect parameters |
| Set new values | `set` | Inspect parameters |
| Update Client in Clockify | `clockify` | client / update |
| Get archived Client from Notion | `notion` | databasePage / getAll |
| Create Client in Clockify | `clockify` | client |
| Store Clockify ID in Notion | `notion` | databasePage / update |
| Remove Client from Clockify | `clockify` | client / delete |
| Merge | `merge` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Get active Projects from Notion | `notion` | databasePage / getAll |
| Get active Projects from Clockify | `clockify` | getAll |
| Update Project in Clockify | `httpRequest` | PUT |
| Get completed Project from Notion | `notion` | databasePage / getAll |
| Create Project in Clockify | `httpRequest` | POST |
| Remove Project from Clockify | `clockify` | client / delete |
| Structure output1 | `noOp` | Inspect parameters |
| No Operation1 | `noOp` | Inspect parameters |
| Map values2 | `set` | Inspect parameters |
| Map values3 | `set` | Inspect parameters |
| Compare Datasets1 | `compareDatasets` | Inspect parameters |
| If unmapped in Notion1 | `if` | Inspect parameters |
| Set new values1 | `set` | Inspect parameters |
| Store Clockify ID in Notion1 | `notion` | databasePage / update |
| Stop and Error1 | `stopAndError` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| No Operation, do nothing2 | `noOp` | Inspect parameters |
| Get active Tasks from Notion | `notion` | databasePage / getAll |
| Get active Tasks from Clockify | `clockify` | task / getAll |
| Update Task in Clockify | `clockify` | task / update |
| Get completed Task from Notion | `notion` | databasePage / getAll |
| Create Task in Clockify | `clockify` | task |
| Remove Task from Clockify | `clockify` | task / delete |
| Structure output2 | `noOp` | Inspect parameters |
| No Operation2 | `noOp` | Inspect parameters |
| Map values4 | `set` | Inspect parameters |
| Map values5 | `set` | Inspect parameters |
| Get active Projects from Clockify1 | `clockify` | getAll |
| Compare Datasets2 | `compareDatasets` | Inspect parameters |
| If unmapped in Notion2 | `if` | Inspect parameters |
| Set new values2 | `set` | Inspect parameters |
| Store Clockify ID in Notion2 | `notion` | databasePage / update |
| Stop and Error2 | `stopAndError` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Limit1 | `limit` | Inspect parameters |

## Connection map

- Limit → No Operation1 (`main`, output 0, input 0)
- Merge → Limit (`main`, output 0, input 0)
- Limit1 → No Operation2 (`main`, output 0, input 0)
- Merge1 → Limit1 (`main`, output 0, input 0)
- Globals → No Operation (`main`, output 0, input 0)
- Webhook → Get first workspace ID (`main`, output 0, input 0)
- Map values → Compare Datasets (`main`, output 0, input 0)
- Map values1 → Compare Datasets (`main`, output 0, input 1)
- Map values2 → Compare Datasets1 (`main`, output 0, input 0)
- Map values3 → Compare Datasets1 (`main`, output 0, input 1)
- Map values4 → Compare Datasets2 (`main`, output 0, input 0)
- Map values5 → Compare Datasets2 (`main`, output 0, input 1)
- No Operation → Get active Clients from Notion (`main`, output 0, input 0)
- No Operation → Get active Clients from Clockify (`main`, output 0, input 0)
- No Operation1 → Get active Projects from Notion (`main`, output 0, input 0)
- No Operation1 → Get active Projects from Clockify (`main`, output 0, input 0)
- No Operation2 → Get active Projects from Clockify1 (`main`, output 0, input 0)
- No Operation2 → Get active Tasks from Notion (`main`, output 0, input 0)
- Set new values → Update Client in Clockify (`main`, output 0, input 0)
- Set new values1 → Update Project in Clockify (`main`, output 0, input 0)
- Set new values2 → Update Task in Clockify (`main`, output 0, input 0)
- Compare Datasets → If unmapped in Notion (`main`, output 0, input 0)
- Compare Datasets → Structure output (`main`, output 1, input 0)
- Compare Datasets → Update Client in Clockify (`main`, output 2, input 0)
- Compare Datasets → Get archived Client from Notion (`main`, output 3, input 0)
- Schedule Trigger → Get first workspace ID (`main`, output 0, input 0)
- Structure output → Merge (`main`, output 0, input 1)
- Compare Datasets1 → If unmapped in Notion1 (`main`, output 0, input 0)
- Compare Datasets1 → Structure output1 (`main`, output 1, input 0)
- Compare Datasets1 → Update Project in Clockify (`main`, output 2, input 0)
- Compare Datasets1 → Get completed Project from Notion (`main`, output 3, input 0)
- Compare Datasets2 → If unmapped in Notion2 (`main`, output 0, input 0)
- Compare Datasets2 → Structure output2 (`main`, output 1, input 0)
- Compare Datasets2 → Update Task in Clockify (`main`, output 2, input 0)
- Compare Datasets2 → Get completed Task from Notion (`main`, output 3, input 0)
- Structure output1 → Merge1 (`main`, output 0, input 1)
- If unmapped in Notion → Create Client in Clockify (`main`, output 0, input 0)
- If unmapped in Notion → Update Client in Clockify (`main`, output 1, input 0)
- Get first workspace ID → Globals (`main`, output 0, input 0)
- If unmapped in Notion1 → Create Project in Clockify (`main`, output 0, input 0)
- If unmapped in Notion1 → Update Project in Clockify (`main`, output 1, input 0)
- If unmapped in Notion2 → Create Task in Clockify (`main`, output 0, input 0)
- If unmapped in Notion2 → Update Task in Clockify (`main`, output 1, input 0)
- Create Task in Clockify → Store Clockify ID in Notion2 (`main`, output 0, input 0)
- No Operation, do nothing → Merge (`main`, output 0, input 0)
- Create Client in Clockify → Store Clockify ID in Notion (`main`, output 0, input 0)
- No Operation, do nothing2 → Merge1 (`main`, output 0, input 0)
- Remove Task from Clockify → Stop and Error2 (`main`, output 0, input 0)
- Update Client in Clockify → Merge (`main`, output 0, input 2)
- Create Project in Clockify → Store Clockify ID in Notion1 (`main`, output 0, input 0)
- Update Project in Clockify → Merge1 (`main`, output 0, input 2)
- Remove Client from Clockify → Stop and Error (`main`, output 0, input 0)
- Store Clockify ID in Notion → No Operation, do nothing (`main`, output 0, input 0)
- Store Clockify ID in Notion → Remove Client from Clockify (`main`, output 1, input 0)
- Get active Tasks from Notion → Map values4 (`main`, output 0, input 0)
- Remove Project from Clockify → Stop and Error1 (`main`, output 0, input 0)
- Store Clockify ID in Notion1 → No Operation, do nothing2 (`main`, output 0, input 0)
- Store Clockify ID in Notion1 → Remove Project from Clockify (`main`, output 1, input 0)
- Store Clockify ID in Notion2 → Remove Task from Clockify (`main`, output 1, input 0)
- Get active Clients from Notion → Map values (`main`, output 0, input 0)
- Get active Tasks from Clockify → Map values5 (`main`, output 0, input 0)
- Get completed Task from Notion → Set new values2 (`main`, output 0, input 0)
- Get active Projects from Notion → Map values2 (`main`, output 0, input 0)
- Get archived Client from Notion → Set new values (`main`, output 0, input 0)
- Get active Clients from Clockify → Map values1 (`main`, output 0, input 0)
- Get active Projects from Clockify → Map values3 (`main`, output 0, input 0)
- Get completed Project from Notion → Set new values1 (`main`, output 0, input 0)
- Get active Projects from Clockify1 → Get active Tasks from Clockify (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1498_Stopanderror_Limit_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1498_Stopanderror_Limit_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
