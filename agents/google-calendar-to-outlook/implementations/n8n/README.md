# Google calendar to Outlook

This folder contains the **Google calendar to Outlook** workflow. Its executable nodes use `googleCalendarTrigger`, `merge`, `microsoftOutlook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-calendar-to-outlook.json`](google-calendar-to-outlook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `microsoftOutlookOAuth2Api`

**Entry nodes:** Incoming Event Trigger, Cancel Event Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Merge | `merge` | Inspect parameters |
| Incoming Event Trigger | `googleCalendarTrigger` | Inspect parameters |
| Cancel Event Trigger | `googleCalendarTrigger` | Inspect parameters |
| Create Outlook Event | `microsoftOutlook` | event / create |
| Get Event to Cancel | `microsoftOutlook` | event |
| Delete Event | `microsoftOutlook` | event / delete |
| Send E-mail with details | `microsoftOutlook` | Inspect parameters |

## Connection map

- Merge → Send E-mail with details (`main`, output 0, input 0)
- Delete Event → Merge (`main`, output 0, input 1)
- Get Event to Cancel → Delete Event (`main`, output 0, input 0)
- Get Event to Cancel → Merge (`main`, output 0, input 0)
- Cancel Event Trigger → Get Event to Cancel (`main`, output 0, input 0)
- Incoming Event Trigger → Create Outlook Event (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftoutlook/1870_Microsoftoutlook_GoogleCalendar_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftoutlook/1870_Microsoftoutlook_GoogleCalendar_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
