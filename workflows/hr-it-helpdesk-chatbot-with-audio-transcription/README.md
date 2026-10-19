# HR & IT Helpdesk Chatbot with Audio Transcription

This folder contains the **HR & IT Helpdesk Chatbot with Audio Transcription** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryPostgresChat`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStorePGVector`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hr-it-helpdesk-chatbot-with-audio-transcription.json`](hr-it-helpdesk-chatbot-with-audio-transcription.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| Create HR Policies | `vectorStorePGVector` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Verify Message Type | `switch` | Inspect parameters |
| OpenAI | `openAi` | audio / transcribe |
| Telegram1 | `telegram` | file |
| Unsupported Message Type | `telegram` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Answer questions with a vector store | `toolVectorStore` | Inspect parameters |
| Postgres PGVector Store | `vectorStorePGVector` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- OpenAI → AI Agent (`main`, output 0, input 0)
- AI Agent → Telegram (`main`, output 0, input 0)
- Telegram1 → OpenAI (`main`, output 0, input 0)
- Edit Fields → AI Agent (`main`, output 0, input 0)
- HTTP Request → Extract from File (`main`, output 0, input 0)
- Telegram Trigger → Verify Message Type (`main`, output 0, input 0)
- Embeddings OpenAI → Create HR Policies (`ai_embedding`, output 0, input 0)
- Extract from File → Create HR Policies (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Postgres PGVector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → Answer questions with a vector store (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Create HR Policies (`ai_document`, output 0, input 0)
- Verify Message Type → Edit Fields (`main`, output 0, input 0)
- Verify Message Type → Telegram1 (`main`, output 1, input 0)
- Verify Message Type → Unsupported Message Type (`main`, output 2, input 0)
- Postgres Chat Memory → AI Agent (`ai_memory`, output 0, input 0)
- Postgres PGVector Store → Answer questions with a vector store (`ai_vectorStore`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → HTTP Request (`main`, output 0, input 0)
- Answer questions with a vector store → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2038_Telegram_Extractfromfile_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2038_Telegram_Extractfromfile_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
