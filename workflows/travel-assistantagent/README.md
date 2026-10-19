# Travel AssistantAgent

This folder contains the **Travel AssistantAgent** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `lmChatGoogleGemini`, `memoryMongoDbChat`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreMongoDBAtlas`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`travel-assistantagent.json`](travel-assistantagent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `mongoDb`, `openAiApi`

**Entry nodes:** When chat message received, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| MongoDB Chat Memory | `memoryMongoDbChat` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| MongoDB Atlas Vector Store | `vectorStoreMongoDBAtlas` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| AI Traveling Planner Agent | `agent` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| MongoDB Atlas Vector Store1 | `vectorStoreMongoDBAtlas` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |

## Connection map

- Webhook → MongoDB Atlas Vector Store1 (`main`, output 0, input 0)
- Embeddings OpenAI → MongoDB Atlas Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI1 → MongoDB Atlas Vector Store1 (`ai_embedding`, output 0, input 0)
- Default Data Loader → MongoDB Atlas Vector Store1 (`ai_document`, output 0, input 0)
- MongoDB Chat Memory → AI Traveling Planner Agent (`ai_memory`, output 0, input 0)
- Google Gemini Chat Model → AI Traveling Planner Agent (`ai_languageModel`, output 0, input 0)
- MongoDB Atlas Vector Store → AI Traveling Planner Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Traveling Planner Agent (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2039_Stickynote_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2039_Stickynote_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
