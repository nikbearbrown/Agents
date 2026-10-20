# http request and receive google calendar events and filter out myself

This folder contains the **http request and receive google calendar events and filter out myself** workflow. Its executable nodes use `aggregate`, `filter`, `gmail`, `googleCalendarTrigger`, `httpRequest`, `if`, `markdown`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-receive-google-calendar-events-and-filter-out-myself.json`](http-request-and-receive-google-calendar-events-and-filter-out-myself.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Google Calendar Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Research Company | `httpRequest` | Inspect parameters |
| Research Person | `httpRequest` | Inspect parameters |
| Google Calendar Trigger | `googleCalendarTrigger` | Inspect parameters |
| Filter Out Myself | `filter` | Inspect parameters |
| Split Out Attendees | `splitOut` | Inspect parameters |
| For Each Attendee | `splitInBatches` | Inspect parameters |
| Is Company Email? | `if` | Inspect parameters |
| Combine All Research | `aggregate` | Inspect parameters |
| Collect Fields | `set` | Inspect parameters |
| Write HTML | `markdown` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Send Report | `gmail` | Inspect parameters |
| Person Prompt | `set` | Inspect parameters |
| Company Prompt | `set` | Inspect parameters |

## Connection map

- Write HTML → Send Report (`main`, output 0, input 0)
- Edit Fields → Split Out Attendees (`main`, output 0, input 0)
- Person Prompt → Research Person (`main`, output 0, input 0)
- Collect Fields → For Each Attendee (`main`, output 0, input 0)
- Company Prompt → Research Company (`main`, output 0, input 0)
- Research Person → Collect Fields (`main`, output 0, input 0)
- Research Company → Person Prompt (`main`, output 0, input 0)
- Filter Out Myself → For Each Attendee (`main`, output 0, input 0)
- For Each Attendee → Combine All Research (`main`, output 0, input 0)
- For Each Attendee → Is Company Email? (`main`, output 1, input 0)
- Is Company Email? → Company Prompt (`main`, output 0, input 0)
- Is Company Email? → Person Prompt (`main`, output 1, input 0)
- Split Out Attendees → Filter Out Myself (`main`, output 0, input 0)
- Combine All Research → Write HTML (`main`, output 0, input 0)
- Google Calendar Trigger → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0899_Splitout_GoogleCalendar_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0899_Splitout_GoogleCalendar_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
