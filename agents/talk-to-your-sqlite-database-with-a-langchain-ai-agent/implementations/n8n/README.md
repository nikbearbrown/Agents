# talk to your sqlite database with a langchain ai agent

This folder contains the **talk to your sqlite database with a langchain ai agent** workflow. Its executable nodes use `agent`, `chatTrigger`, `executeWorkflow`, `executeWorkflowTrigger`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`talk-to-your-sqlite-database-with-a-langchain-ai-agent.json`](talk-to-your-sqlite-database-with-a-langchain-ai-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`

**Entry nodes:** Execute "Generate a chart" tool, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Execute "Generate a chart" tool | `executeWorkflowTrigger` | Inspect parameters |
| OpenAI - Generate Chart definition with Structured Output | `httpRequest` | POST |
| Set response | `set` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Set Text output | `set` | Inspect parameters |
| Set Text + Chart output | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model Classifier | `lmChatOpenAi` | Inspect parameters |
| Text Classifier - Chart required? | `textClassifier` | Inspect parameters |
| User question + Agent initial response | `set` | Inspect parameters |
| Information Extractor - User question | `informationExtractor` | Inspect parameters |

## Connection map

- AI Agent → Text Classifier - Chart required? (`main`, output 0, input 0)
- Execute Workflow → Set Text + Chart output (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model → Information Extractor - User question (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- When chat message received → Information Extractor - User question (`main`, output 0, input 0)
- OpenAI Chat Model Classifier → Text Classifier - Chart required? (`ai_languageModel`, output 0, input 0)
- Execute "Generate a chart" tool → OpenAI - Generate Chart definition with Structured Output (`main`, output 0, input 0)
- Text Classifier - Chart required? → User question + Agent initial response (`main`, output 0, input 0)
- Text Classifier - Chart required? → Set Text output (`main`, output 1, input 0)
- Information Extractor - User question → AI Agent (`main`, output 0, input 0)
- User question + Agent initial response → Execute Workflow (`main`, output 0, input 0)
- OpenAI - Generate Chart definition with Structured Output → Set response (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0636_HTTP_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0636_HTTP_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
