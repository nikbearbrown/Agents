# RAG

This folder contains the **RAG** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `lmChatGoogleGemini`, `lmChatOpenAi`, `memoryPostgresChat`, `set`, `supabase`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag.json`](rag.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `openAiApi`, `postgres`, `supabaseApi`

**Entry nodes:** File Created, File Updated, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Retrieve Documents | `toolVectorStore` | Inspect parameters |
| Download File | `googleDrive` | download |
| File Created | `googleDriveTrigger` | Inspect parameters |
| File Updated | `googleDriveTrigger` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Delete Old Doc Rows | `supabase` | delete |
| Set File ID | `set` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| RAG AI Agent | `agent` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Insert into Supabase Vectorstore | `vectorStoreSupabase` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Embeddings Google Gemini1 | `embeddingsGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |

## Connection map

- OpenAI Chat Model → RAG AI Agent (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Insert into Supabase Vectorstore (`ai_document`, output 0, input 0)
- Retrieve Documents → RAG AI Agent (`ai_tool`, output 0, input 0)
- Download File → Extract from File (`main`, output 0, input 0)
- File Created → Set File ID (`main`, output 0, input 0)
- File Updated → Set File ID (`main`, output 0, input 0)
- Postgres Chat Memory → RAG AI Agent (`ai_memory`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Delete Old Doc Rows → Download File (`main`, output 0, input 0)
- Set File ID → Delete Old Doc Rows (`main`, output 0, input 0)
- When chat message received → RAG AI Agent (`main`, output 0, input 0)
- Supabase Vector Store → Retrieve Documents (`ai_vectorStore`, output 0, input 0)
- Embeddings Google Gemini → Insert into Supabase Vectorstore (`ai_embedding`, output 0, input 0)
- Code → Insert into Supabase Vectorstore (`main`, output 0, input 0)
- Embeddings Google Gemini1 → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → Retrieve Documents (`ai_languageModel`, output 0, input 0)
- Extract from File → Code (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/renebell0/n8n-rag-agent/blob/448dab3450b4f57b5277bfadf8f75dfab2ea4eec/RAG.json](https://github.com/renebell0/n8n-rag-agent/blob/448dab3450b4f57b5277bfadf8f75dfab2ea4eec/RAG.json). License: **MIT**; preserve [the notice](../../licenses/renebell0--n8n-rag-agent.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
