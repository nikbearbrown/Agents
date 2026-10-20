# list database page notion and notion and update database page notion

This folder contains the **list database page notion and notion and update database page notion** workflow. Its executable nodes use `function`, `if`, `merge`, `notion`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-database-page-notion-and-notion-and-update-database-page-notion.json`](list-database-page-notion-and-notion-and-update-database-page-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `notionApi`

**Entry nodes:** Team Creation

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Team Members | `function` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Query Current Semester | `notion` | databasePage / getAll |
| Select Semester ID and Projects Count | `set` | Inspect parameters |
| Use Default Name if Not Specified | `set` | Inspect parameters |
| Select Project Showcase ID | `set` | Inspect parameters |
| Get Project Name & Idea | `set` | Inspect parameters |
| Create Project | `notion` | databasePage |
| If user exists | `if` | Inspect parameters |
| Create User | `notion` | databasePage |
| Query for User | `notion` | databasePage / getAll |
| Merge1 | `merge` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Update Semester for User | `notion` | databasePage / update |
| Query User | `notion` | databasePage / getAll |
| Select Semester ID | `set` | Inspect parameters |
| Update Project Relation | `notion` | databasePage / update |
| Merge3 | `merge` | Inspect parameters |
| Concatenate SemesterIDs | `function` | Inspect parameters |
| Concatenate ProjectIDs | `function` | Inspect parameters |
| Merge4 | `merge` | Inspect parameters |
| Set Email | `set` | Inspect parameters |
| Team Creation | `webhook` | Inspect parameters |

## Connection map

- Merge → Use Default Name if Not Specified (`main`, output 0, input 0)
- Merge1 → If user exists (`main`, output 0, input 0)
- Merge2 → Concatenate SemesterIDs (`main`, output 0, input 0)
- Merge3 → Concatenate ProjectIDs (`main`, output 0, input 0)
- Merge4 → Query User (`main`, output 0, input 0)
- Set Email → Merge4 (`main`, output 0, input 1)
- Query User → Merge2 (`main`, output 0, input 1)
- Query User → Merge3 (`main`, output 0, input 0)
- Create User → Set Email (`main`, output 0, input 0)
- Team Creation → Get Project Name & Idea (`main`, output 0, input 0)
- Team Creation → Get Team Members (`main`, output 0, input 0)
- Team Creation → Query Current Semester (`main`, output 0, input 0)
- Create Project → Select Project Showcase ID (`main`, output 0, input 0)
- If user exists → Merge4 (`main`, output 0, input 0)
- If user exists → Create User (`main`, output 1, input 0)
- Query for User → Merge1 (`main`, output 0, input 1)
- Get Team Members → Query for User (`main`, output 0, input 0)
- Get Team Members → Merge1 (`main`, output 0, input 0)
- Select Semester ID → Merge2 (`main`, output 0, input 0)
- Concatenate ProjectIDs → Update Project Relation (`main`, output 0, input 0)
- Query Current Semester → Select Semester ID and Projects Count (`main`, output 0, input 0)
- Query Current Semester → Select Semester ID (`main`, output 0, input 0)
- Concatenate SemesterIDs → Update Semester for User (`main`, output 0, input 0)
- Get Project Name & Idea → Merge (`main`, output 0, input 1)
- Select Project Showcase ID → Merge3 (`main`, output 0, input 1)
- Use Default Name if Not Specified → Create Project (`main`, output 0, input 0)
- Select Semester ID and Projects Count → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Notion/0142_Notion_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Notion/0142_Notion_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
