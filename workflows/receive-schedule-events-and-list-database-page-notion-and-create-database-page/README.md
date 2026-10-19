# receive schedule events and list database page notion and create database page

This folder contains the **receive schedule events and list database page notion and create database page** workflow. Its executable nodes use `dateTime`, `httpRequest`, `if`, `itemLists`, `merge`, `notion`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-database-page-notion-and-create-database-page.json`](receive-schedule-events-and-list-database-page-notion-and-create-database-page.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `oAuth2Api`

**Entry nodes:** On schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On schedule | `scheduleTrigger` | Inspect parameters |
| Try get database page | `notion` | databasePage / getAll |
| Merge | `merge` | Inspect parameters |
| If database page not found | `if` | Inspect parameters |
| Create database page | `notion` | databasePage |
| Update database page | `notion` | databasePage / update |
| X days into the future | `dateTime` | addToDate |
| Split out items | `itemLists` | Inspect parameters |
| Get Outlook Calendar events | `httpRequest` | Inspect parameters |

## Connection map

- Merge → If database page not found (`main`, output 0, input 0)
- On schedule → X days into the future (`main`, output 0, input 0)
- Split out items → Merge (`main`, output 0, input 0)
- Split out items → Try get database page (`main`, output 0, input 0)
- Try get database page → Merge (`main`, output 0, input 1)
- X days into the future → Get Outlook Calendar events (`main`, output 0, input 0)
- If database page not found → Create database page (`main`, output 0, input 0)
- If database page not found → Update database page (`main`, output 1, input 0)
- Get Outlook Calendar events → Split out items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0316_Datetime_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0316_Datetime_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
