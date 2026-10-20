# Calendar_scheduling

This folder contains the **Calendar_scheduling** workflow. Its executable nodes use `agent`, `chainLlm`, `executeWorkflowTrigger`, `filter`, `gmail`, `gmailTrigger`, `googleCalendar`, `if`, `itemLists`, `lmChatOpenAi`, `outputParserStructured`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`calendar-scheduling.json`](calendar-scheduling.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `openAiApi`

**Entry nodes:** Gmail Trigger, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Chat OpenAI | `lmChatOpenAi` | Inspect parameters |
| Workflow Tool | `toolWorkflow` | Inspect parameters |
| Chat OpenAI1 | `lmChatOpenAi` | Inspect parameters |
| Google Calendar | `googleCalendar` | getAll |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Format response | `itemLists` | concatenateItems |
| Stringify Response | `set` | Inspect parameters |
| Extract start, end and name | `set` | Inspect parameters |
| Filter only confirmed and with set time | `filter` | Inspect parameters |
| Is appointment request | `if` | Inspect parameters |
| Classify appointment | `chainLlm` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Sort | `itemLists` | sort |
| Mark as read | `gmail` | markAsRead |
| Send Reply | `gmail` | reply |
| Agent | `agent` | Inspect parameters |

## Connection map

- Sort → Format response (`main`, output 0, input 0)
- Agent → Send Reply (`main`, output 0, input 0)
- Agent → Mark as read (`main`, output 0, input 0)
- Chat OpenAI → Classify appointment (`ai_languageModel`, output 0, input 0)
- Chat OpenAI1 → Agent (`ai_languageModel`, output 0, input 0)
- Gmail Trigger → Classify appointment (`main`, output 0, input 0)
- Workflow Tool → Agent (`ai_tool`, output 0, input 0)
- Format response → Stringify Response (`main`, output 0, input 0)
- Google Calendar → Filter only confirmed and with set time (`main`, output 0, input 0)
- Classify appointment → Is appointment request (`main`, output 0, input 0)
- Is appointment request → Agent (`main`, output 0, input 0)
- Execute Workflow Trigger → Google Calendar (`main`, output 0, input 0)
- Structured Output Parser → Classify appointment (`ai_outputParser`, output 0, input 0)
- Extract start, end and name → Sort (`main`, output 0, input 0)
- Filter only confirmed and with set time → Extract start, end and name (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/1668_GoogleCalendar_Filter_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlecalendar/1668_GoogleCalendar_Filter_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
