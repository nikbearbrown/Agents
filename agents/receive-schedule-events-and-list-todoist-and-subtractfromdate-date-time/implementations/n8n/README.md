# receive schedule events and list todoist and subtractfromdate date time

This folder contains the **receive schedule events and list todoist and subtractfromdate date time** workflow. Its executable nodes use `crypto`, `dateTime`, `filter`, `httpRequest`, `if`, `itemLists`, `scheduleTrigger`, `set`, `todoist`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-todoist-and-subtractfromdate-date-time.json`](receive-schedule-events-and-list-todoist-and-subtractfromdate-date-time.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `todoistApi`

**Entry nodes:** at 5am, every 5 min

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| if after unsnooze date | `if` | Inspect parameters |
| at 5am | `scheduleTrigger` | Inspect parameters |
| every 5 min | `scheduleTrigger` | Inspect parameters |
| Get snoozed tasks | `todoist` | getAll |
| if task is not a subtask | `if` | Inspect parameters |
| If task has due date | `if` | Inspect parameters |
| Get date to unsnooze | `dateTime` | subtractFromDate |
| Get inbox tasks to snooze | `todoist` | getAll |
| Set inbox project id | `set` | Inspect parameters |
| If not same project | `filter` | Inspect parameters |
| Set args to move | `set` | Inspect parameters |
| Generate unique uuid for move | `crypto` | Inspect parameters |
| Merge all items into a list | `itemLists` | concatenateItems |
| Move the tasks | `httpRequest` | POST |
| Set snoozed project id | `set` | Inspect parameters |

## Connection map

- at 5am → Get snoozed tasks (`main`, output 0, input 0)
- every 5 min → Get inbox tasks to snooze (`main`, output 0, input 0)
- Set args to move → Generate unique uuid for move (`main`, output 0, input 0)
- Get snoozed tasks → if task is not a subtask (`main`, output 0, input 0)
- If not same project → Set args to move (`main`, output 0, input 0)
- Get date to unsnooze → if after unsnooze date (`main`, output 0, input 0)
- If task has due date → Get date to unsnooze (`main`, output 0, input 0)
- Set inbox project id → If not same project (`main`, output 0, input 0)
- Set snoozed project id → If not same project (`main`, output 0, input 0)
- if after unsnooze date → Set inbox project id (`main`, output 0, input 0)
- if after unsnooze date → Set snoozed project id (`main`, output 1, input 0)
- if task is not a subtask → If task has due date (`main`, output 0, input 0)
- Get inbox tasks to snooze → if task is not a subtask (`main`, output 0, input 0)
- Merge all items into a list → Move the tasks (`main`, output 0, input 0)
- Generate unique uuid for move → Merge all items into a list (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0444_Datetime_Todoist_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0444_Datetime_Todoist_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
