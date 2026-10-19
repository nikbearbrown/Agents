# RAG on living data

This folder contains the **RAG on living data** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `limit`, `lmChatOpenAi`, `noOp`, `notion`, `notionTrigger`, `retrieverVectorStore`, `scheduleTrigger`, `splitInBatches`, `summarize`, `supabase`, `textSplitterTokenSplitter`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-on-living-data.json`](rag-on-living-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `openAiApi`, `supabaseApi`

**Entry nodes:** When chat message received, Schedule Trigger, Notion Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Limit1 | `limit` | Inspect parameters |
| Delete old embeddings if exist | `supabase` | delete |
| Get page blocks | `notion` | block / getAll |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Input Reference | `noOp` | Inspect parameters |
| Notion Trigger | `notionTrigger` | Inspect parameters |
| Get updated pages | `notion` | databasePage / getAll |
| Supabase Vector Store1 | `vectorStoreSupabase` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Concatenate to single string | `summarize` | Inspect parameters |

## Connection map

- Limit → Get page blocks (`main`, output 0, input 0)
- Limit1 → Loop Over Items (`main`, output 0, input 0)
- Notion Trigger → Input Reference (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Get page blocks → Concatenate to single string (`main`, output 0, input 0)
- Input Reference → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Delete old embeddings if exist (`main`, output 1, input 0)
- Schedule Trigger → Get updated pages (`main`, output 0, input 0)
- Embeddings OpenAI → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI → Supabase Vector Store1 (`ai_embedding`, output 0, input 0)
- Get updated pages → Input Reference (`main`, output 0, input 0)
- OpenAI Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Supabase Vector Store (`ai_document`, output 0, input 0)
- Supabase Vector Store → Limit1 (`main`, output 0, input 0)
- Supabase Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- When chat message received → Question and Answer Chain (`main`, output 0, input 0)
- Concatenate to single string → Supabase Vector Store (`main`, output 0, input 0)
- Delete old embeddings if exist → Limit (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1527_Limit_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1527_Limit_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
