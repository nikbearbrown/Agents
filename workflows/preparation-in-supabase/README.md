# PREPARATION (in Supabase)

This folder contains the **PREPARATION (in Supabase)** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `lmChatOpenAi`, `retrieverVectorStore`, `set`, `supabase`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`preparation-in-supabase.json`](preparation-in-supabase.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Recursive Character Text Splitter1 | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Customize Response | `set` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Retrieve by Query | `vectorStoreSupabase` | Inspect parameters |
| Embeddings OpenAI Retrieval | `embeddingsOpenAi` | Inspect parameters |
| Embeddings OpenAI Insertion | `embeddingsOpenAi` | Inspect parameters |
| Placeholder (File/Content to Upsert) | `set` | Inspect parameters |
| Embeddings OpenAI Upserting | `embeddingsOpenAi` | Inspect parameters |
| Insert Documents | `vectorStoreSupabase` | Inspect parameters |
| Retrieve Rows from Table | `supabase` | getAll |
| Update Documents | `vectorStoreSupabase` | Inspect parameters |

## Connection map

- Google Drive → Insert Documents (`main`, output 0, input 0)
- OpenAI Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Retrieve by Query → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Default Data Loader → Insert Documents (`ai_document`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Question and Answer Chain → Customize Response (`main`, output 0, input 0)
- When chat message received → Question and Answer Chain (`main`, output 0, input 0)
- Embeddings OpenAI Insertion → Insert Documents (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI Retrieval → Retrieve by Query (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI Upserting → Update Documents (`ai_embedding`, output 0, input 0)
- Recursive Character Text Splitter1 → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Placeholder (File/Content to Upsert) → Update Documents (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Supabase/0564_Supabase_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Supabase/0564_Supabase_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
