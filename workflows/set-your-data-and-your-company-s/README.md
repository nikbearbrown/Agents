# Set your data and your company's

This folder contains the **Set your data and your company's** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `filter`, `gmail`, `googleCalendarTool`, `httpRequest`, `hubspot`, `hubspotTrigger`, `if`, `lmChatOpenAi`, `markdown`, `outputParserStructured`, `set`, `splitOut`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`set-your-data-and-your-company-s.json`](set-your-data-and-your-company-s.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `hubspotDeveloperApi`, `hubspotOAuth2Api`, `openAiApi`

**Entry nodes:** Webhook, When Executed by Another Workflow, HubSpot Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Try Again | `set` | Inspect parameters |
| Success | `set` | Inspect parameters |
| Calendar Agent | `agent` | Inspect parameters |
| Create Event with Attendee | `googleCalendarTool` | Inspect parameters |
| Create Event | `googleCalendarTool` | Inspect parameters |
| Get Events | `googleCalendarTool` | getAll |
| Delete Event | `googleCalendarTool` | delete |
| Update Event | `googleCalendarTool` | update |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| calendarAgent | `toolWorkflow` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Get list of owners | `httpRequest` | Inspect parameters |
| Split Out owners | `splitOut` | Inspect parameters |
| Get current owner | `filter` | Inspect parameters |
| HubSpot Trigger | `hubspotTrigger` | Inspect parameters |
| Enter your company data here | `set` | Inspect parameters |
| If a contact is created | `if` | Inspect parameters |
| Get all info about the contact | `hubspot` | get |
| Write a personalized message | `agent` | Inspect parameters |
| Send the message | `gmail` | Inspect parameters |
| Set owner to contact | `hubspot` | Inspect parameters |
| Transforms markdown to HTML | `markdown` | Inspect parameters |
| OpenAI Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Webhook → Enter your company data here (`main`, output 0, input 0)
- Get Events → Calendar Agent (`ai_tool`, output 0, input 0)
- Create Event → Calendar Agent (`ai_tool`, output 0, input 0)
- Delete Event → Calendar Agent (`ai_tool`, output 0, input 0)
- OpenAI Model → Calendar Agent (`ai_languageModel`, output 0, input 0)
- Update Event → Calendar Agent (`ai_tool`, output 0, input 0)
- calendarAgent → Write a personalized message (`ai_tool`, output 0, input 0)
- Calendar Agent → Success (`main`, output 0, input 0)
- Calendar Agent → Try Again (`main`, output 1, input 0)
- HubSpot Trigger → Enter your company data here (`main`, output 0, input 0)
- Send the message → Set owner to contact (`main`, output 0, input 0)
- Split Out owners → Get current owner (`main`, output 0, input 0)
- Get current owner → If a contact is created (`main`, output 0, input 0)
- Get list of owners → Split Out owners (`main`, output 0, input 0)
- OpenAI Chat Model2 → Write a personalized message (`ai_languageModel`, output 0, input 0)
- If a contact is created → Get all info about the contact (`main`, output 0, input 0)
- Structured Output Parser → Write a personalized message (`ai_outputParser`, output 0, input 0)
- Create Event with Attendee → Calendar Agent (`ai_tool`, output 0, input 0)
- Transforms markdown to HTML → Send the message (`main`, output 0, input 0)
- Enter your company data here → Get list of owners (`main`, output 0, input 0)
- Write a personalized message → Transforms markdown to HTML (`main`, output 0, input 0)
- Get all info about the contact → Write a personalized message (`main`, output 0, input 0)
- When Executed by Another Workflow → Calendar Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hubspot/0920_HubSpot_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hubspot/0920_HubSpot_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
