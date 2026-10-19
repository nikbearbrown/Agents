# 🧹 Archive (delete) duplicate items from a Notion database

This folder contains the **🧹 Archive (delete) duplicate items from a Notion database** workflow. Its executable nodes use `aggregate`, `code`, `notion`, `notionTrigger`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`archive-delete-duplicate-items-from-a-notion-database.json`](archive-delete-duplicate-items-from-a-notion-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Every day, When a page is added to the database

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Every day | `scheduleTrigger` | Inspect parameters |
| Get pages from database | `notion` | databasePage / getAll |
| Aggregate all items | `aggregate` | Inspect parameters |
| Format items properly | `set` | Inspect parameters |
| Filter duplicates | `code` | Inspect parameters |
| Archive pages | `notion` | archive |
| When a page is added to the database | `notionTrigger` | Inspect parameters |

## Connection map

- Every day → Get pages from database (`main`, output 0, input 0)
- Filter duplicates → Archive pages (`main`, output 0, input 0)
- Aggregate all items → Filter duplicates (`main`, output 0, input 0)
- Format items properly → Aggregate all items (`main`, output 0, input 0)
- Get pages from database → Format items properly (`main`, output 0, input 0)
- When a page is added to the database → Get pages from database (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1317_Code_Schedule_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1317_Code_Schedule_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
