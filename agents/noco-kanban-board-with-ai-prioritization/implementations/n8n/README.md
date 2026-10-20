# Noco Kanban Board with AI Prioritization

This folder contains the **Noco Kanban Board with AI Prioritization** workflow. Its executable nodes use `agent`, `aggregate`, `emailSend`, `formTrigger`, `if`, `lmChatOpenAi`, `manualTrigger`, `noOp`, `nocoDb`, `outputParserStructured`, `scheduleTrigger`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`noco-kanban-board-with-ai-prioritization.json`](noco-kanban-board-with-ai-prioritization.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `nocoDbApiToken`, `openAiApi`, `slackOAuth2Api`, `smtp`

**Entry nodes:** Incident Form, When clicking ‘Test workflow’, Check status every day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Incident Form | `formTrigger` | Inspect parameters |
| Assign Category | `agent` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Structure Output Todoist Ready1 | `outputParserStructured` | Inspect parameters |
| Get incident definitions | `nocoDb` | getAll |
| Insert Incident | `nocoDb` | create |
| Aggregate for AI parsing | `aggregate` | Inspect parameters |
| On schedule or during flow | `noOp` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Task is not picked up after expected response | `if` | Inspect parameters |
| Send email to client | `emailSend` | Inspect parameters |
| Check status every day | `scheduleTrigger` | Inspect parameters |
| Send email to asignee | `emailSend` | Inspect parameters |
| Get Unpicked Tasks | `nocoDb` | getAll |
| Get Unfinished Tasks | `nocoDb` | getAll |
| Task is not complete in expected time | `if` | Inspect parameters |
| Send email to client1 | `emailSend` | Inspect parameters |
| If there is asignee email | `if` | Inspect parameters |
| If there is assignee slack | `if` | Inspect parameters |
| Slack to assignee | `slack` | Inspect parameters |
| Send another email to asignee | `emailSend` | Inspect parameters |
| Format for Noco | `set` | Inspect parameters |

## Connection map

- Incident Form → Get incident definitions (`main`, output 0, input 0)
- Assign Category → Format for Noco (`main`, output 0, input 0)
- Format for Noco → Insert Incident (`main`, output 0, input 0)
- Insert Incident → On schedule or during flow (`main`, output 0, input 0)
- Get Unpicked Tasks → Task is not picked up after expected response (`main`, output 0, input 0)
- OpenAI Chat Model1 → Assign Category (`ai_languageModel`, output 0, input 0)
- Get Unfinished Tasks → Task is not complete in expected time (`main`, output 0, input 0)
- Check status every day → On schedule or during flow (`main`, output 0, input 0)
- Aggregate for AI parsing → Assign Category (`main`, output 0, input 0)
- Get incident definitions → Aggregate for AI parsing (`main`, output 0, input 0)
- If there is asignee email → Send email to asignee (`main`, output 0, input 0)
- If there is assignee slack → Slack to assignee (`main`, output 0, input 0)
- If there is assignee slack → Send another email to asignee (`main`, output 1, input 0)
- On schedule or during flow → Get Unpicked Tasks (`main`, output 0, input 0)
- On schedule or during flow → Get Unfinished Tasks (`main`, output 0, input 0)
- Structure Output Todoist Ready1 → Assign Category (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → On schedule or during flow (`main`, output 0, input 0)
- Task is not complete in expected time → Send email to client1 (`main`, output 0, input 0)
- Task is not complete in expected time → If there is assignee slack (`main`, output 1, input 0)
- Task is not picked up after expected response → Send email to client (`main`, output 0, input 0)
- Task is not picked up after expected response → If there is asignee email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1418_Schedule_Nocodb_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1418_Schedule_Nocodb_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
