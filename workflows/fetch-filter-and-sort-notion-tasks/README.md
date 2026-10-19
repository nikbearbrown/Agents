# Fetch, filter and sort notion tasks

This folder contains the **Fetch, filter and sort notion tasks** workflow. Its executable nodes use `aggregate`, `emailSend`, `filter`, `html`, `if`, `manualTrigger`, `merge`, `notion`, `pushover`, `scheduleTrigger`, `set`, `sort`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-filter-and-sort-notion-tasks.json`](fetch-filter-and-sort-notion-tasks.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `pushoverApi`, `smtp`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Notion | `notion` | databasePage / getAll |
| Sort by closest deadline | `sort` | Inspect parameters |
| Filter for deadline | `filter` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| HTML | `html` | Inspect parameters |
| Aggregate due to tasks | `aggregate` | Inspect parameters |
| Aggregate overdue tasks | `aggregate` | Inspect parameters |
| Pushover | `pushover` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| If deadline is overdue | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| HTML for Task | `html` | Inspect parameters |
| HTML due to List | `html` | Inspect parameters |
| HTML overdue List | `html` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge groups | `merge` | Inspect parameters |
| Set Workflow vars | `set` | Inspect parameters |

## Connection map

- HTML → Send Email (`main`, output 0, input 0)
- HTML → Pushover (`main`, output 0, input 0)
- Merge → If deadline is overdue (`main`, output 0, input 0)
- Notion → Filter for deadline (`main`, output 0, input 0)
- Aggregate → HTML (`main`, output 0, input 0)
- Merge groups → Aggregate (`main`, output 0, input 0)
- HTML for Task → Merge (`main`, output 0, input 1)
- HTML due to List → Merge groups (`main`, output 0, input 1)
- Schedule Trigger → Set Workflow vars (`main`, output 0, input 0)
- HTML overdue List → Merge groups (`main`, output 0, input 0)
- Set Workflow vars → Notion (`main`, output 0, input 0)
- Filter for deadline → Sort by closest deadline (`main`, output 0, input 0)
- Aggregate due to tasks → HTML due to List (`main`, output 0, input 0)
- If deadline is overdue → Aggregate overdue tasks (`main`, output 0, input 0)
- If deadline is overdue → Aggregate due to tasks (`main`, output 1, input 0)
- Aggregate overdue tasks → HTML overdue List (`main`, output 0, input 0)
- Sort by closest deadline → HTML for Task (`main`, output 0, input 0)
- Sort by closest deadline → Merge (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Workflow vars (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0572_Filter_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0572_Filter_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
