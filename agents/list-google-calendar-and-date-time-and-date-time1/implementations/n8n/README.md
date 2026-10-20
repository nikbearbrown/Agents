# list google calendar and date time and date time1

This folder contains the **list google calendar and date time and date time1** workflow. Its executable nodes use `cron`, `dateTime`, `function`, `googleCalendar`, `if`, `merge`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-google-calendar-and-date-time-and-date-time1.json`](list-google-calendar-and-date-time-and-date-time1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `slackApi`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Calendar | `googleCalendar` | getAll |
| Function | `function` | Inspect parameters |
| Date & Time | `dateTime` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Date & Time1 | `dateTime` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Set1 | `set` | Inspect parameters |
| Date & Time2 | `dateTime` | Inspect parameters |
| Function1 | `function` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Cron | `cron` | Inspect parameters |

## Connection map

- IF → Set1 (`main`, output 0, input 0)
- Set → Merge (`main`, output 0, input 0)
- Cron → Google Calendar (`main`, output 0, input 0)
- Cron → Function (`main`, output 0, input 0)
- Set1 → Date & Time2 (`main`, output 0, input 0)
- Merge → IF (`main`, output 0, input 0)
- Function → Date & Time1 (`main`, output 0, input 0)
- Function1 → Slack (`main`, output 0, input 0)
- Date & Time → Set (`main`, output 0, input 0)
- Date & Time1 → Merge (`main`, output 0, input 1)
- Date & Time2 → Function1 (`main`, output 0, input 0)
- Google Calendar → Date & Time (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0109_Slack_Cron_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0109_Slack_Cron_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
