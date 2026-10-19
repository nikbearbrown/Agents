# create database page and list database page notion and update database page notion

This folder contains the **create database page and list database page notion and update database page notion** workflow. Its executable nodes use `function`, `githubTrigger`, `if`, `notion`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-database-page-and-list-database-page-notion-and-update-database-page-notion.json`](create-database-page-and-list-database-page-notion-and-update-database-page-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `notionApi`

**Entry nodes:** Trigger on issues

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create database page | `notion` | databasePage |
| Find database page | `notion` | databasePage / getAll |
| Switch | `switch` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Edit issue | `notion` | databasePage / update |
| Delete issue | `notion` | archive |
| Create custom Notion filters | `function` | Inspect parameters |
| Close issue | `notion` | databasePage / update |
| Reopen issue | `notion` | databasePage / update |
| Trigger on issues | `githubTrigger` | Inspect parameters |

## Connection map

- IF → Create database page (`main`, output 0, input 0)
- IF → Create custom Notion filters (`main`, output 1, input 0)
- Switch → Edit issue (`main`, output 0, input 0)
- Switch → Delete issue (`main`, output 1, input 0)
- Switch → Close issue (`main`, output 2, input 0)
- Switch → Reopen issue (`main`, output 3, input 0)
- Trigger on issues → IF (`main`, output 0, input 0)
- Find database page → Switch (`main`, output 0, input 0)
- Create custom Notion filters → Find database page (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/0264_GitHub_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/0264_GitHub_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
