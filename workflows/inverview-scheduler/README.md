# Inverview Scheduler

This folder contains the **Inverview Scheduler** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `googleCalendar`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `noOp`, `outputParserStructured`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`inverview-scheduler.json`](inverview-scheduler.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `openAiApi`

**Entry nodes:** Get Availability, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory2 | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model4 | `lmChatOpenAi` | Inspect parameters |
| Run Get Availability | `toolWorkflow` | Inspect parameters |
| check day names | `toolWorkflow` | Inspect parameters |
| Convert Output to JSON | `agent` | Inspect parameters |
| Interview Scheduler | `agent` | Inspect parameters |
| If Final Output | `if` | Inspect parameters |
| Respond for More Info | `noOp` | Inspect parameters |
| Parse to JSON | `outputParserStructured` | Inspect parameters |
| Set Meeting with Google | `googleCalendar` | Inspect parameters |
| Final Response to User | `code` | Inspect parameters |
| Generate Interview Times | `code` | Inspect parameters |
| Check My Calendar | `googleCalendar` | getAll |
| Split Events into 30 min blocks | `code` | Inspect parameters |
| Add Blocked Field | `set` | Inspect parameters |
| Generate 30 Minute Timeslots | `code` | Inspect parameters |
| Combine My Calendar with All Slots | `merge` | Inspect parameters |
| Check if Calendar Blocked | `if` | Inspect parameters |
| Return string of all available times | `code` | Inspect parameters |
| Get Availability | `executeWorkflowTrigger` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |

## Connection map

- Parse to JSON → Convert Output to JSON (`ai_outputParser`, output 0, input 0)
- If Final Output → Convert Output to JSON (`main`, output 0, input 0)
- If Final Output → Respond for More Info (`main`, output 1, input 0)
- check day names → Interview Scheduler (`ai_tool`, output 0, input 0)
- Get Availability → Check My Calendar (`main`, output 0, input 0)
- Get Availability → Generate 30 Minute Timeslots (`main`, output 0, input 0)
- Add Blocked Field → Combine My Calendar with All Slots (`main`, output 0, input 0)
- Check My Calendar → Split Events into 30 min blocks (`main`, output 0, input 0)
- OpenAI Chat Model2 → Interview Scheduler (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model4 → Convert Output to JSON (`ai_languageModel`, output 0, input 0)
- Interview Scheduler → If Final Output (`main`, output 0, input 0)
- Run Get Availability → Interview Scheduler (`ai_tool`, output 0, input 0)
- Window Buffer Memory2 → Interview Scheduler (`ai_memory`, output 0, input 0)
- Convert Output to JSON → Set Meeting with Google (`main`, output 0, input 0)
- Set Meeting with Google → Final Response to User (`main`, output 0, input 0)
- Check if Calendar Blocked → Return string of all available times (`main`, output 0, input 0)
- When chat message received → Interview Scheduler (`main`, output 0, input 0)
- Generate 30 Minute Timeslots → Combine My Calendar with All Slots (`main`, output 0, input 1)
- Split Events into 30 min blocks → Add Blocked Field (`main`, output 0, input 0)
- Combine My Calendar with All Slots → Check if Calendar Blocked (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1813_Code_GoogleCalendar_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1813_Code_GoogleCalendar_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
