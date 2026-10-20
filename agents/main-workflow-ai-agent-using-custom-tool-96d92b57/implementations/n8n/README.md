# Main workflow: AI agent using custom tool

This folder contains the **Main workflow: AI agent using custom tool** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `executeWorkflowTrigger`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`main-workflow-ai-agent-using-custom-tool-96d92b57.json`](main-workflow-ai-agent-using-custom-tool-96d92b57.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Work out activity type and number of people1 | `informationExtractor` | Inspect parameters |
| Call the API | `httpRequest` | Inspect parameters |
| Activity Tool | `toolWorkflow` | Inspect parameters |
| Set 'response' value | `set` | Inspect parameters |
| Combine | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- Combine → Set 'response' value (`main`, output 0, input 0)
- Call the API → Combine (`main`, output 0, input 0)
- Activity Tool → AI Agent (`ai_tool`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Work out activity type and number of people1 (`ai_languageModel`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Work out activity type and number of people1 (`main`, output 0, input 0)
- Work out activity type and number of people1 → Call the API (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0405_HTTP_Executeworkflow_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0405_HTTP_Executeworkflow_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
