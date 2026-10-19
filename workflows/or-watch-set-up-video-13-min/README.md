# ... or watch set up video [13 min]

This folder contains the **... or watch set up video [13 min]** workflow. Its executable nodes use `agent`, `chatTrigger`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryPostgresChat`, `openAi`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`or-watch-set-up-video-13-min.json`](or-watch-set-up-video-13-min.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpQueryAuth`, `openAiApi`, `postgres`

**Entry nodes:** When chat message received, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| get_channel_details | `toolWorkflow` | Inspect parameters |
| get_video_description | `toolWorkflow` | Inspect parameters |
| get_list_of_videos | `toolWorkflow` | Inspect parameters |
| get_list_of_comments | `toolWorkflow` | Inspect parameters |
| search | `toolWorkflow` | Inspect parameters |
| analyze_thumbnail | `toolWorkflow` | Inspect parameters |
| video_transcription | `toolWorkflow` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Get Comments | `httpRequest` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Get Channel Details | `httpRequest` | Inspect parameters |
| Get Video Description | `httpRequest` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Run Query | `httpRequest` | Inspect parameters |
| Get Videos by Channel | `httpRequest` | Inspect parameters |
| Response | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Get Video Transcription | `httpRequest` | POST |
| OpenAI | `openAi` | image / analyze |

## Connection map

- OpenAI → Response (`main`, output 0, input 0)
- Switch → Get Channel Details (`main`, output 0, input 0)
- Switch → Get Video Description (`main`, output 1, input 0)
- Switch → Get Comments (`main`, output 2, input 0)
- Switch → Run Query (`main`, output 3, input 0)
- Switch → Get Videos by Channel (`main`, output 4, input 0)
- Switch → OpenAI (`main`, output 5, input 0)
- Switch → Get Video Transcription (`main`, output 6, input 0)
- search → AI Agent (`ai_tool`, output 0, input 0)
- Run Query → Response (`main`, output 0, input 0)
- Edit Fields → Response (`main`, output 0, input 0)
- Get Comments → Edit Fields (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- analyze_thumbnail → AI Agent (`ai_tool`, output 0, input 0)
- get_list_of_videos → AI Agent (`ai_tool`, output 0, input 0)
- Get Channel Details → Response (`main`, output 0, input 0)
- get_channel_details → AI Agent (`ai_tool`, output 0, input 0)
- video_transcription → AI Agent (`ai_tool`, output 0, input 0)
- Postgres Chat Memory → AI Agent (`ai_memory`, output 0, input 0)
- get_list_of_comments → AI Agent (`ai_tool`, output 0, input 0)
- Get Video Description → Response (`main`, output 0, input 0)
- Get Videos by Channel → Response (`main`, output 0, input 0)
- get_video_description → AI Agent (`ai_tool`, output 0, input 0)
- Get Video Transcription → Response (`main`, output 0, input 0)
- Execute Workflow Trigger → Switch (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1440_HTTP_Executeworkflow_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1440_HTTP_Executeworkflow_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
