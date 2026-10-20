# receive chat events and acuity support search api and results to items

This folder contains the **receive chat events and acuity support search api and results to items** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `splitOut`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-chat-events-and-acuity-support-search-api-and-results-to-items.json`](receive-chat-events-and-acuity-support-search-api-and-results-to-items.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received, KnowledgeBase Tool Subworkflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Acuity Support Search API | `httpRequest` | POST |
| Extract Relevant Fields | `set` | Inspect parameters |
| Results to Items | `splitOut` | Inspect parameters |
| Has Results? | `if` | Inspect parameters |
| Empty Response | `set` | Inspect parameters |
| Aggregate Response | `aggregate` | Inspect parameters |
| Knowledgebase Tool | `toolWorkflow` | Inspect parameters |
| AcuityScheduling Support Chatbot | `agent` | Inspect parameters |
| KnowledgeBase Tool Subworkflow | `executeWorkflowTrigger` | Inspect parameters |

## Connection map

- Has Results? → Results to Items (`main`, output 0, input 0)
- Has Results? → Empty Response (`main`, output 1, input 0)
- Simple Memory → AcuityScheduling Support Chatbot (`ai_memory`, output 0, input 0)
- Results to Items → Extract Relevant Fields (`main`, output 0, input 0)
- OpenAI Chat Model → AcuityScheduling Support Chatbot (`ai_languageModel`, output 0, input 0)
- Knowledgebase Tool → AcuityScheduling Support Chatbot (`ai_tool`, output 0, input 0)
- Extract Relevant Fields → Aggregate Response (`main`, output 0, input 0)
- Acuity Support Search API → Has Results? (`main`, output 0, input 0)
- When chat message received → AcuityScheduling Support Chatbot (`main`, output 0, input 0)
- KnowledgeBase Tool Subworkflow → Acuity Support Search API (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0840_Splitout_HTTP_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0840_Splitout_HTTP_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
