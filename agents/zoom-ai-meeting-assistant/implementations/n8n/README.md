# Zoom AI Meeting Assistant

This folder contains the **Zoom AI Meeting Assistant** workflow. Its executable nodes use `agent`, `clickUp`, `code`, `emailSend`, `executeWorkflowTrigger`, `extractFromFile`, `filter`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `microsoftOutlookTool`, `openAi`, `set`, `splitInBatches`, `splitOut`, `stopAndError`, `toolWorkflow`, `zoom`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`zoom-ai-meeting-assistant.json`](zoom-ai-meeting-assistant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clickUpOAuth2Api`, `microsoftOutlookOAuth2Api`, `openAiApi`, `smtp`, `zoomOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| No Recording/Transcript available | `stopAndError` | Inspect parameters |
| Zoom: Get data of last meeting | `zoom` | getAll |
| Filter transcript URL | `set` | Inspect parameters |
| Filter: Only 1 item | `splitInBatches` | Inspect parameters |
| Zoom: Get transcript file | `httpRequest` | Inspect parameters |
| Extract text from transcript file | `extractFromFile` | text |
| Format transcript text | `set` | Inspect parameters |
| Zoom: Get participants data | `httpRequest` | Inspect parameters |
| Create meeting summary | `openAi` | Inspect parameters |
| Sort for mail delivery | `set` | Inspect parameters |
| Format to html | `code` | Inspect parameters |
| Send meeting summary | `emailSend` | Inspect parameters |
| Create tasks | `toolWorkflow` | Inspect parameters |
| Create tasks and follow-up call | `agent` | Inspect parameters |
| Create follow-up call | `microsoftOutlookTool` | event / create |
| Filter: Last 24 hours | `filter` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| ClickUp | `clickUp` | Inspect parameters |
| Zoom: Get transcripts data | `httpRequest` | Inspect parameters |

## Connection map

- Split Out → ClickUp (`main`, output 0, input 0)
- Create tasks → Create tasks and follow-up call (`ai_tool`, output 0, input 0)
- Format to html → Send meeting summary (`main`, output 0, input 0)
- OpenAI Chat Model → Create tasks and follow-up call (`ai_languageModel`, output 0, input 0)
- Filter: Only 1 item → Filter: Only 1 item (`main`, output 0, input 0)
- Filter: Only 1 item → Zoom: Get transcript file (`main`, output 1, input 0)
- Create follow-up call → Create tasks and follow-up call (`ai_tool`, output 0, input 0)
- Filter transcript URL → Filter: Only 1 item (`main`, output 0, input 0)
- Filter: Last 24 hours → Zoom: Get transcripts data (`main`, output 0, input 0)
- Create meeting summary → Sort for mail delivery (`main`, output 0, input 0)
- Create meeting summary → Create tasks and follow-up call (`main`, output 0, input 0)
- Format transcript text → Zoom: Get participants data (`main`, output 0, input 0)
- Sort for mail delivery → Format to html (`main`, output 0, input 0)
- Execute Workflow Trigger → Split Out (`main`, output 0, input 0)
- Zoom: Get transcript file → Extract text from transcript file (`main`, output 0, input 0)
- Zoom: Get transcripts data → Filter transcript URL (`main`, output 0, input 0)
- Zoom: Get transcripts data → No Recording/Transcript available (`main`, output 1, input 0)
- Zoom: Get participants data → Create meeting summary (`main`, output 0, input 0)
- Zoom: Get data of last meeting → Filter: Last 24 hours (`main`, output 0, input 0)
- Extract text from transcript file → Format transcript text (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Zoom: Get data of last meeting (`main`, output 0, input 0)

## Verification and provenance

Selected from 8 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1785_Stopanderror_Clickup_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1785_Stopanderror_Clickup_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
