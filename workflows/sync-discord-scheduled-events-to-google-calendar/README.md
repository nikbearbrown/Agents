# Sync Discord scheduled events to Google Calendar

This folder contains the **Sync Discord scheduled events to Google Calendar** workflow. Its executable nodes use `googleCalendar`, `httpRequest`, `if`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sync-discord-scheduled-events-to-google-calendar.json`](sync-discord-scheduled-events-to-google-calendar.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** On schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| List scheduled events from Discord | `httpRequest` | Inspect parameters |
| On schedule | `scheduleTrigger` | Inspect parameters |
| Update event details | `googleCalendar` | update |
| Create event | `googleCalendar` | Inspect parameters |
| Get events | `googleCalendar` | get |
| Create or update? | `if` | Inspect parameters |
| Configure | `set` | Inspect parameters |

## Connection map

- Configure → List scheduled events from Discord (`main`, output 0, input 0)
- Get events → Create or update? (`main`, output 0, input 0)
- On schedule → Configure (`main`, output 0, input 0)
- Create or update? → Update event details (`main`, output 0, input 0)
- Create or update? → Create event (`main`, output 1, input 0)
- List scheduled events from Discord → Get events (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0313_HTTP_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0313_HTTP_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
