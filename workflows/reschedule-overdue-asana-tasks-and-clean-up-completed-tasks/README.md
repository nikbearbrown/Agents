# Reschedule overdue Asana tasks and clean up completed tasks

This folder contains the **Reschedule overdue Asana tasks and clean up completed tasks** workflow. Its executable nodes use `asana`, `if`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`reschedule-overdue-asana-tasks-and-clean-up-completed-tasks.json`](reschedule-overdue-asana-tasks-and-clean-up-completed-tasks.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `asanaApi`

**Entry nodes:** Everyday at 7am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Everyday at 7am | `scheduleTrigger` | Inspect parameters |
| Get user tasks | `asana` | getAll |
| Get task infos | `asana` | get |
| Task is open? | `if` | Inspect parameters |
| Due date in the past? | `if` | Inspect parameters |
| Set due date to Today | `asana` | update |
| Clean up task | `asana` | delete |

## Connection map

- Task is open? → Due date in the past? (`main`, output 0, input 0)
- Task is open? → Clean up task (`main`, output 1, input 0)
- Get task infos → Task is open? (`main`, output 0, input 0)
- Get user tasks → Get task infos (`main`, output 0, input 0)
- Everyday at 7am → Get user tasks (`main`, output 0, input 0)
- Due date in the past? → Set due date to Today (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1629_Schedule_Stickynote_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1629_Schedule_Stickynote_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
