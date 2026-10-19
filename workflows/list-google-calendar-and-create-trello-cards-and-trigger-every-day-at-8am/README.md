# list google calendar and create trello cards and trigger every day at 8am

This folder contains the **list google calendar and create trello cards and trigger every day at 8am** workflow. Its executable nodes use `cron`, `function`, `googleCalendar`, `if`, `noOp`, `set`, `splitInBatches`, `trello`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-google-calendar-and-create-trello-cards-and-trigger-every-day-at-8am.json`](list-google-calendar-and-create-trello-cards-and-trigger-every-day-at-8am.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `trelloApi`

**Entry nodes:** Trigger Every Day at 8am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Start & End of day | `function` | Inspect parameters |
| Set Trello Card Details | `set` | Inspect parameters |
| Remove Recurring Tasks | `if` | Inspect parameters |
| Get Todays Events | `googleCalendar` | getAll |
| Split Events In Batches | `splitInBatches` | Inspect parameters |
| Create Trello Cards | `trello` | Inspect parameters |
| Delete Task | `noOp` | Inspect parameters |
| Trigger Every Day at 8am | `cron` | Inspect parameters |

## Connection map

- Get Todays Events → Split Events In Batches (`main`, output 0, input 0)
- Get Start & End of day → Get Todays Events (`main`, output 0, input 0)
- Remove Recurring Tasks → Delete Task (`main`, output 0, input 0)
- Remove Recurring Tasks → Create Trello Cards (`main`, output 1, input 0)
- Set Trello Card Details → Remove Recurring Tasks (`main`, output 0, input 0)
- Split Events In Batches → Set Trello Card Details (`main`, output 0, input 0)
- Split Events In Batches → Get Todays Events (`main`, output 0, input 0)
- Trigger Every Day at 8am → Get Start & End of day (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/0053_Trello_GoogleCalendar_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/0053_Trello_GoogleCalendar_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
