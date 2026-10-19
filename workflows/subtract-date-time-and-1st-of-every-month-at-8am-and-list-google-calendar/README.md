# subtract date time and 1st of every month at 8am and list google calendar

This folder contains the **subtract date time and 1st of every month at 8am and list google calendar** workflow. Its executable nodes use `code`, `cron`, `dateTime`, `emailSend`, `googleCalendar`, `merge`, `noOp`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`subtract-date-time-and-1st-of-every-month-at-8am-and-list-google-calendar.json`](subtract-date-time-and-1st-of-every-month-at-8am-and-list-google-calendar.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `smtp`

**Entry nodes:** 1st of Every month at 8am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Previous Month | `dateTime` | subtract |
| 1st of Every month at 8am | `cron` | Inspect parameters |
| Check Summary for Illness or Holiday | `switch` | Inspect parameters |
| Holiday | `noOp` | Inspect parameters |
| Illness | `noOp` | Inspect parameters |
| Filter Holiday Days | `set` | Inspect parameters |
| Filter Illness Days | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Get previous months events | `googleCalendar` | getAll |
| Send email to payroll | `emailSend` | Inspect parameters |
| Combine Holiday Counts | `code` | Inspect parameters |
| Combine Illness Counts | `code` | Inspect parameters |
| Build the message to send | `code` | Inspect parameters |

## Connection map

- Merge → Build the message to send (`main`, output 0, input 0)
- Holiday → Filter Holiday Days (`main`, output 0, input 0)
- Illness → Filter Illness Days (`main`, output 0, input 0)
- Previous Month → Get previous months events (`main`, output 0, input 0)
- Filter Holiday Days → Combine Holiday Counts (`main`, output 0, input 0)
- Filter Illness Days → Combine Illness Counts (`main`, output 0, input 0)
- Combine Holiday Counts → Merge (`main`, output 0, input 0)
- Combine Illness Counts → Merge (`main`, output 0, input 1)
- 1st of Every month at 8am → Previous Month (`main`, output 0, input 0)
- Build the message to send → Send email to payroll (`main`, output 0, input 0)
- Get previous months events → Check Summary for Illness or Holiday (`main`, output 0, input 0)
- Check Summary for Illness or Holiday → Holiday (`main`, output 0, input 0)
- Check Summary for Illness or Holiday → Illness (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0168_Datetime_GoogleCalendar_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0168_Datetime_GoogleCalendar_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
