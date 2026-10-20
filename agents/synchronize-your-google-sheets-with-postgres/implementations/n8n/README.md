# Synchronize your Google Sheets with Postgres

This folder contains the **Synchronize your Google Sheets with Postgres** workflow. Its executable nodes use `compareDatasets`, `googleSheets`, `postgres`, `scheduleTrigger`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`synchronize-your-google-sheets-with-postgres.json`](synchronize-your-google-sheets-with-postgres.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Split Out Relevant Fields | `splitOut` | Inspect parameters |
| Retrieve Sheets Data | `googleSheets` | Inspect parameters |
| Select Rows in Postgres | `postgres` | select |
| Insert Rows | `postgres` | Inspect parameters |
| Update Rows | `postgres` | update |

## Connection map

- Compare Datasets → Insert Rows (`main`, output 0, input 0)
- Compare Datasets → Update Rows (`main`, output 2, input 0)
- Schedule Trigger → Retrieve Sheets Data (`main`, output 0, input 0)
- Schedule Trigger → Select Rows in Postgres (`main`, output 0, input 0)
- Retrieve Sheets Data → Split Out Relevant Fields (`main`, output 0, input 0)
- Select Rows in Postgres → Compare Datasets (`main`, output 0, input 1)
- Split Out Relevant Fields → Compare Datasets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1998_Splitout_Postgres_Sync_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1998_Splitout_Postgres_Sync_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
