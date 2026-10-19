# 💡Criteria For Follow Up Candidates

This folder contains the **💡Criteria For Follow Up Candidates** workflow. Its executable nodes use `agent`, `airtable`, `chainLlm`, `lmChatOpenAi`, `outputParserAutofixing`, `outputParserStructured`, `scheduleTrigger`, `switch`, `toolHttpRequest`, `twilio`, `twilioTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`criteria-for-follow-up-candidates.json`](criteria-for-follow-up-candidates.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `calApi`, `httpHeaderAuth`, `openAiApi`, `twilioApi`

**Entry nodes:** Twilio Trigger, Every 24hrs

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Twilio Trigger | `twilioTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Find Follow-Up Candidates | `airtable` | search |
| Send Follow Up Message | `twilio` | Inspect parameters |
| Update Follow-Up Count and Date | `airtable` | update |
| Create/Update Session | `airtable` | update |
| Get Existing Chat Session | `airtable` | search |
| Every 24hrs | `scheduleTrigger` | Inspect parameters |
| Send Reply | `twilio` | Inspect parameters |
| Send Confirmation | `twilio` | Inspect parameters |
| User Request STOP | `airtable` | update |
| Check For Command  Words | `switch` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Generate Follow Up Message | `chainLlm` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Get Availability | `toolHttpRequest` | Inspect parameters |
| Get Existing Booking | `toolHttpRequest` | Inspect parameters |
| Find Existing Booking | `toolHttpRequest` | Inspect parameters |
| Reschedule Booking | `toolHttpRequest` | POST |
| Cancel Booking | `toolHttpRequest` | POST |
| Create a Booking | `toolHttpRequest` | POST |
| Appointment Scheduling Agent1 | `agent` | Inspect parameters |

## Connection map

- Every 24hrs → Find Follow-Up Candidates (`main`, output 0, input 0)
- Cancel Booking → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- Twilio Trigger → Check For Command  Words (`main`, output 0, input 0)
- Create a Booking → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- Get Availability → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- User Request STOP → Send Confirmation (`main`, output 0, input 0)
- OpenAI Chat Model1 → Generate Follow Up Message (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Appointment Scheduling Agent1 (`ai_languageModel`, output 0, input 0)
- Reschedule Booking → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- Get Existing Booking → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- Create/Update Session → Send Reply (`main`, output 0, input 0)
- Find Existing Booking → Appointment Scheduling Agent1 (`ai_tool`, output 0, input 0)
- Check For Command  Words → User Request STOP (`main`, output 0, input 0)
- Check For Command  Words → Get Existing Chat Session (`main`, output 1, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Appointment Scheduling Agent1 (`ai_outputParser`, output 0, input 0)
- Find Follow-Up Candidates → Generate Follow Up Message (`main`, output 0, input 0)
- Get Existing Chat Session → Appointment Scheduling Agent1 (`main`, output 0, input 0)
- Generate Follow Up Message → Update Follow-Up Count and Date (`main`, output 0, input 0)
- Appointment Scheduling Agent1 → Create/Update Session (`main`, output 0, input 0)
- Update Follow-Up Count and Date → Send Follow Up Message (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 9}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0539_Schedule_Twilio_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0539_Schedule_Twilio_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
