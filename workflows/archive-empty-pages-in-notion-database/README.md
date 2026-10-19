# Archive empty pages in Notion Database

This folder contains the **Archive empty pages in Notion Database** workflow. Its executable nodes use `cron`, `function`, `if`, `notion`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`archive-empty-pages-in-notion-database.json`](archive-empty-pages-in-notion-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`

**Entry nodes:** Every day @ 2am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get All Databases | `notion` | database / getAll |
| Get All Database Pages | `notion` | databasePage / getAll |
| Get Page Blocks | `notion` | block / getAll |
| Process Blocks | `function` | Inspect parameters |
| SplitInBatches | `splitInBatches` | Inspect parameters |
| Check for empty properties | `function` | Inspect parameters |
| Archive Page | `notion` | archive |
| If toDelete | `if` | Inspect parameters |
| If Empty Properties | `if` | Inspect parameters |
| Every day @ 2am | `cron` | Inspect parameters |

## Connection map

- If toDelete → Archive Page (`main`, output 0, input 0)
- Process Blocks → If toDelete (`main`, output 0, input 0)
- Process Blocks → SplitInBatches (`main`, output 0, input 0)
- SplitInBatches → Get Page Blocks (`main`, output 0, input 0)
- Every day @ 2am → Get All Databases (`main`, output 0, input 0)
- Get Page Blocks → Process Blocks (`main`, output 0, input 0)
- Get All Databases → Get All Database Pages (`main`, output 0, input 0)
- If Empty Properties → SplitInBatches (`main`, output 0, input 0)
- Get All Database Pages → Check for empty properties (`main`, output 0, input 0)
- Check for empty properties → If Empty Properties (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitinbatches/0070_Splitinbatches_Notion_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitinbatches/0070_Splitinbatches_Notion_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
