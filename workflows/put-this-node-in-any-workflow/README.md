# Put this node in any workflow.

This folder contains the **Put this node in any workflow.** workflow. Its executable nodes use `agent`, `chainRetrievalQa`, `embeddingsOpenAi`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `n8n`, `noOp`, `respondToWebhook`, `retrieverVectorStore`, `scheduleTrigger`, `splitInBatches`, `switch`, `toolHttpRequest`, `vectorStoreInMemory`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`put-this-node-in-any-workflow.json`](put-this-node-in-any-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’, POST /workflow/magic/position/id, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| In-Memory Vector Store | `vectorStoreInMemory` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Dummy Node | `noOp` | Inspect parameters |
| Dummy Node (1) | `noOp` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Dummy Node (2) | `noOp` | Inspect parameters |
| Dummy Node (3) | `noOp` | Inspect parameters |
| Dummy Node (4) | `noOp` | Inspect parameters |
| Dummy Node (5) | `noOp` | Inspect parameters |
| Dummy Node (6) | `noOp` | Inspect parameters |
| Dummy Node (7) | `noOp` | Inspect parameters |
| Dummy Node (8) | `noOp` | Inspect parameters |
| Dummy Node (9) | `noOp` | Inspect parameters |
| Dummy Tool | `toolHttpRequest` | Inspect parameters |
| Dummy Tool (1) | `toolHttpRequest` | Inspect parameters |
| OpenAI Chat Model (1) | `lmChatOpenAi` | Inspect parameters |
| Update n8n Workflow | `n8n` | update |
| Magic Positioning IA2S | `httpRequest` | POST |
| POST /workflow/magic/position/id | `webhook` | Inspect parameters |
| Get n8n Workflow | `n8n` | get |
| Simple Webhook Response | `respondToWebhook` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Magic Positioning | `httpRequest` | POST |

## Connection map

- IF → Dummy Node (`main`, output 0, input 0)
- IF → AI Agent (`main`, output 1, input 0)
- Switch → Dummy Node (6) (`main`, output 0, input 0)
- Switch → Dummy Node (7) (`main`, output 1, input 0)
- Switch → Dummy Node (8) (`main`, output 2, input 0)
- Switch → Dummy Node (9) (`main`, output 3, input 0)
- Switch → Question and Answer Chain (`main`, output 4, input 0)
- Dummy Node → Dummy Node (1) (`main`, output 0, input 0)
- Dummy Node → Dummy Node (3) (`main`, output 0, input 0)
- Dummy Tool → AI Agent (`ai_tool`, output 0, input 0)
- Dummy Node (1) → Loop Over Items (`main`, output 0, input 0)
- Dummy Node (2) → Switch (`main`, output 0, input 0)
- Dummy Node (3) → Dummy Node (4) (`main`, output 0, input 0)
- Dummy Node (5) → Loop Over Items (`main`, output 0, input 0)
- Dummy Tool (1) → AI Agent (`ai_tool`, output 0, input 0)
- Loop Over Items → Dummy Node (2) (`main`, output 0, input 0)
- Loop Over Items → Dummy Node (5) (`main`, output 1, input 0)
- Get n8n Workflow → Magic Positioning IA2S (`main`, output 0, input 0)
- Schedule Trigger → IF (`main`, output 0, input 0)
- Embeddings OpenAI → In-Memory Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Update n8n Workflow → Simple Webhook Response (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- OpenAI Chat Model (1) → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- In-Memory Vector Store → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Magic Positioning IA2S → Update n8n Workflow (`main`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- POST /workflow/magic/position/id → Get n8n Workflow (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → IF (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0672_Webhook_Schedule_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0672_Webhook_Schedule_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
