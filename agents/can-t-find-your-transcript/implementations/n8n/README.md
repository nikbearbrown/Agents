# 💡 Can't find your transcript?

This folder contains the **💡 Can't find your transcript?** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `extractFromFile`, `googleCalendar`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `outputParserStructured`, `set`, `splitOut`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`can-t-find-your-transcript.json`](can-t-find-your-transcript.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `googleDriveOAuth2Api`, `googleOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking "Test workflow", Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Get Meeting ConferenceRecords | `httpRequest` | Inspect parameters |
| Get Meeting Transcript Location | `httpRequest` | Inspect parameters |
| Get Transcript File | `googleDrive` | download |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| PDF Loader | `extractFromFile` | pdf |
| Get Calendar Event | `googleCalendar` | get |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Response | `set` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Fallback Response | `set` | Inspect parameters |
| Actions Router | `switch` | Inspect parameters |
| Get Attendees | `set` | Inspect parameters |
| Attendees List | `splitOut` | Inspect parameters |
| Add Attendee to Invite | `googleCalendar` | update |
| Create Calendar Event1 | `googleCalendar` | Inspect parameters |
| Schedule Meeting | `toolWorkflow` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- PDF Loader → AI Agent (`main`, output 0, input 0)
- Edit Fields → Actions Router (`main`, output 0, input 0)
- Get Attendees → Attendees List (`main`, output 0, input 0)
- Actions Router → Create Calendar Event1 (`main`, output 0, input 0)
- Actions Router → Fallback Response (`main`, output 1, input 0)
- Attendees List → Add Attendee to Invite (`main`, output 0, input 0)
- Schedule Meeting → AI Agent (`ai_tool`, output 0, input 0)
- Get Calendar Event → Get Meeting ConferenceRecords (`main`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- Get Transcript File → PDF Loader (`main`, output 0, input 0)
- Add Attendee to Invite → Response (`main`, output 0, input 0)
- Create Calendar Event1 → Get Attendees (`main`, output 0, input 0)
- Execute Workflow Trigger → Edit Fields (`main`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Get Meeting ConferenceRecords → Get Meeting Transcript Location (`main`, output 0, input 0)
- When clicking "Test workflow" → Get Calendar Event (`main`, output 0, input 0)
- Get Meeting Transcript Location → Get Transcript File (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0530_Splitout_GoogleCalendar_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0530_Splitout_GoogleCalendar_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
