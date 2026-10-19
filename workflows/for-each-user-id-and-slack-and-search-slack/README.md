# for each user id and slack and search slack

This folder contains the **for each user id and slack and search slack** workflow. Its executable nodes use `agent`, `code`, `filter`, `googleCalendar`, `if`, `lmChatOpenAi`, `outputParserStructured`, `scheduleTrigger`, `set`, `slack`, `splitOut`, `toolSerpApi`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`for-each-user-id-and-slack-and-search-slack.json`](for-each-user-id-and-slack-and-search-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| For Each User ID... | `splitOut` | Inspect parameters |
| Get User | `slack` | user |
| Search for Invite Requests | `slack` | search |
| Get Existing Invite EventID | `code` | Inspect parameters |
| Should Create Event? | `if` | Inspect parameters |
| Create Event | `googleCalendar` | Inspect parameters |
| Get Invite Reactions | `slack` | reaction / get |
| Get Invite Replies | `slack` | channel / replies |
| Extract Invite Reactions | `splitOut` | Inspect parameters |
| Get Old EventId | `set` | Inspect parameters |
| Add Attendee to Event | `googleCalendar` | update |
| Get Event Details | `googleCalendar` | get |
| Is Attending | `filter` | Inspect parameters |
| Get User Email | `set` | Inspect parameters |
| Should Add Attendee? | `if` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| SerpAPI | `toolSerpApi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Reply Invite with EventId | `slack` | Inspect parameters |
| Calendar Event Booking Agent | `agent` | Inspect parameters |

## Connection map

- SerpAPI → Calendar Event Booking Agent (`ai_tool`, output 0, input 0)
- Get User → Should Add Attendee? (`main`, output 0, input 0)
- Wikipedia → Calendar Event Booking Agent (`ai_tool`, output 0, input 0)
- Create Event → Reply Invite with EventId (`main`, output 0, input 0)
- Is Attending → For Each User ID... (`main`, output 0, input 0)
- Get User Email → Add Attendee to Event (`main`, output 0, input 0)
- Get Old EventId → Get Event Details (`main`, output 0, input 0)
- Schedule Trigger → Search for Invite Requests (`main`, output 0, input 0)
- Get Event Details → Get Invite Reactions (`main`, output 0, input 0)
- OpenAI Chat Model → Calendar Event Booking Agent (`ai_languageModel`, output 0, input 0)
- Get Invite Replies → Get Existing Invite EventID (`main`, output 0, input 0)
- For Each User ID... → Get User (`main`, output 0, input 0)
- Get Invite Reactions → Extract Invite Reactions (`main`, output 0, input 0)
- Should Add Attendee? → Get User Email (`main`, output 0, input 0)
- Should Create Event? → Calendar Event Booking Agent (`main`, output 0, input 0)
- Should Create Event? → Get Old EventId (`main`, output 1, input 0)
- Extract Invite Reactions → Is Attending (`main`, output 0, input 0)
- Structured Output Parser → Calendar Event Booking Agent (`ai_outputParser`, output 0, input 0)
- Search for Invite Requests → Get Invite Replies (`main`, output 0, input 0)
- Get Existing Invite EventID → Should Create Event? (`main`, output 0, input 0)
- Calendar Event Booking Agent → Create Event (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0528_Splitout_GoogleCalendar_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0528_Splitout_GoogleCalendar_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
