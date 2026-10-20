# receive schedule events and list google calendar and only follow ups

This folder contains the **receive schedule events and list google calendar and only follow ups** workflow. Its executable nodes use `agent`, `filter`, `gmail`, `googleCalendar`, `googleCalendarTool`, `lmChatOpenAi`, `outputParserStructured`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-google-calendar-and-only-follow-ups.json`](receive-schedule-events-and-list-google-calendar-and-only-follow-ups.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Past Events | `googleCalendar` | getAll |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Flag to Follow Up | `set` | Inspect parameters |
| Only Follow Ups | `filter` | Inspect parameters |
| Get Emails Since | `gmail` | thread |
| Output | `outputParserStructured` | Inspect parameters |
| Availability | `googleCalendarTool` | calendar |
| Model | `lmChatOpenAi` | Inspect parameters |
| Meeting Availability Agent | `agent` | Inspect parameters |
| Generate Message | `set` | Inspect parameters |
| Meetings | `googleCalendarTool` | Inspect parameters |
| Model1 | `lmChatOpenAi` | Inspect parameters |
| Meeting Booking Agent | `agent` | Inspect parameters |
| Mark as Seen | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Send for Human Approval | `gmail` | sendAndWait |

## Connection map

- Model → Meeting Availability Agent (`ai_languageModel`, output 0, input 0)
- Model1 → Meeting Booking Agent (`ai_languageModel`, output 0, input 0)
- Output → Meeting Availability Agent (`ai_outputParser`, output 0, input 0)
- Meetings → Meeting Booking Agent (`ai_tool`, output 0, input 0)
- Availability → Meeting Availability Agent (`ai_tool`, output 0, input 0)
- Mark as Seen → Loop Over Items (`main`, output 0, input 0)
- Get Past Events → Mark as Seen (`main`, output 0, input 0)
- Loop Over Items → Only Follow Ups (`main`, output 0, input 0)
- Loop Over Items → Get Emails Since (`main`, output 1, input 0)
- Only Follow Ups → Meeting Availability Agent (`main`, output 0, input 0)
- Generate Message → Send for Human Approval (`main`, output 0, input 0)
- Get Emails Since → Flag to Follow Up (`main`, output 0, input 0)
- Schedule Trigger → Get Past Events (`main`, output 0, input 0)
- Flag to Follow Up → Loop Over Items (`main`, output 0, input 0)
- Send for Human Approval → Meeting Booking Agent (`main`, output 0, input 0)
- Meeting Availability Agent → Generate Message (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/0783_GoogleCalendar_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/0783_GoogleCalendar_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
