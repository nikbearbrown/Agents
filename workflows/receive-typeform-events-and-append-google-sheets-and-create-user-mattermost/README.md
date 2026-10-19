# receive typeform events and append google sheets and create user mattermost

This folder contains the **receive typeform events and append google sheets and create user mattermost** workflow. Its executable nodes use `function`, `gmail`, `googleCalendar`, `googleSheets`, `mattermost`, `merge`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-typeform-events-and-append-google-sheets-and-create-user-mattermost.json`](receive-typeform-events-and-append-google-sheets-and-create-user-mattermost.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `googleSheetsOAuth2Api`, `mattermostApi`, `typeformApi`

**Entry nodes:** Attendee Registrations

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Attendee Registrations | `typeformTrigger` | Inspect parameters |
| Add to Sheets | `googleSheets` | append |
| Create Account | `mattermost` | user / create |
| Add to team | `mattermost` | user / invite |
| Array to Rows | `function` | Inspect parameters |
| Get Session Details | `googleSheets` | Inspect parameters |
| Merge Data | `merge` | Inspect parameters |
| Add to channels | `mattermost` | channel / addUser |
| Add to Event | `googleCalendar` | update |
| Welcome Email | `gmail` | message |

## Connection map

- Merge Data → Add to channels (`main`, output 0, input 0)
- Add to team → Array to Rows (`main`, output 0, input 0)
- Add to Event → Welcome Email (`main`, output 0, input 0)
- Add to Sheets → Create Account (`main`, output 0, input 0)
- Array to Rows → Merge Data (`main`, output 0, input 0)
- Create Account → Add to team (`main`, output 0, input 0)
- Add to channels → Add to Event (`main`, output 0, input 0)
- Get Session Details → Merge Data (`main`, output 0, input 1)
- Attendee Registrations → Add to Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/1116_GoogleCalendar_GoogleSheets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/1116_GoogleCalendar_GoogleSheets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
