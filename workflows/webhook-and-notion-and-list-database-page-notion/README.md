# webhook and notion and list database page notion

This folder contains the **webhook and notion and list database page notion** workflow. Its executable nodes use `function`, `if`, `merge`, `notion`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-notion-and-list-database-page-notion.json`](webhook-and-notion-and-list-database-page-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `notionApi`

**Entry nodes:** Sign Up

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract Name and Email | `set` | Inspect parameters |
| Sign Up | `webhook` | Inspect parameters |
| If user exists | `if` | Inspect parameters |
| Create User | `notion` | databasePage |
| Query for User | `notion` | databasePage / getAll |
| Query Current Semester | `notion` | databasePage / getAll |
| Select Semester ID | `set` | Inspect parameters |
| Update Semester for User | `notion` | databasePage / update |
| Merge Semester ID | `merge` | Inspect parameters |
| Concatenate Semester IDs | `function` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Query User | `notion` | databasePage / getAll |

## Connection map

- Merge → If user exists (`main`, output 0, input 0)
- Sign Up → Extract Name and Email (`main`, output 0, input 0)
- Query User → Query Current Semester (`main`, output 0, input 0)
- Query User → Merge Semester ID (`main`, output 0, input 1)
- Create User → Query User (`main`, output 0, input 0)
- If user exists → Query User (`main`, output 0, input 0)
- If user exists → Create User (`main`, output 1, input 0)
- Query for User → Merge (`main`, output 0, input 1)
- Merge Semester ID → Concatenate Semester IDs (`main`, output 0, input 0)
- Select Semester ID → Merge Semester ID (`main`, output 0, input 0)
- Extract Name and Email → Merge (`main`, output 0, input 0)
- Extract Name and Email → Query for User (`main`, output 0, input 0)
- Query Current Semester → Select Semester ID (`main`, output 0, input 0)
- Concatenate Semester IDs → Update Semester for User (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Notion/0141_Notion_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Notion/0141_Notion_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
