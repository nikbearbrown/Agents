# GoogleSheets MySQL Integration

This folder contains the **GoogleSheets MySQL Integration** workflow. Its executable nodes use `compareDatasets`, `googleSheets`, `if`, `manualTrigger`, `mySql`, `noOp`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`googlesheets-mysql-integration.json`](googlesheets-mysql-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `mySql`

**Entry nodes:** When clicking "Execute Workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Send Notifications | `noOp` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Google Sheet Data | `googleSheets` | Inspect parameters |
| SQL Get inquiries from Google | `mySql` | select |
| Add MySQL records | `mySql` | upsert |
| Rename GSheet variables | `set` | Inspect parameters |
| No reply too long? | `if` | Inspect parameters |
| DB Status assigned? | `if` | Inspect parameters |
| Update GSheet status | `googleSheets` | update |
| DB Status in sync? | `if` | Inspect parameters |
| Sync MySQL data | `mySql` | update |

## Connection map

- Compare Datasets → Add MySQL records (`main`, output 0, input 0)
- Compare Datasets → No reply too long? (`main`, output 1, input 0)
- Compare Datasets → DB Status assigned? (`main`, output 2, input 0)
- Compare Datasets → DB Status in sync? (`main`, output 3, input 0)
- Schedule Trigger → Google Sheet Data (`main`, output 0, input 0)
- Schedule Trigger → SQL Get inquiries from Google (`main`, output 0, input 0)
- Google Sheet Data → Rename GSheet variables (`main`, output 0, input 0)
- DB Status in sync? → Sync MySQL data (`main`, output 0, input 0)
- No reply too long? → Send Notifications (`main`, output 0, input 0)
- DB Status assigned? → Update GSheet status (`main`, output 0, input 0)
- Rename GSheet variables → Compare Datasets (`main`, output 0, input 0)
- SQL Get inquiries from Google → Compare Datasets (`main`, output 0, input 1)
- When clicking "Execute Workflow" → Google Sheet Data (`main`, output 0, input 0)
- When clicking "Execute Workflow" → SQL Get inquiries from Google (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1738_Schedule_Comparedatasets_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1738_Schedule_Comparedatasets_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
