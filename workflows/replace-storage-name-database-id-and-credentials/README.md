# Replace Storage name, database ID and credentials.

This folder contains the **Replace Storage name, database ID and credentials.** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `merge`, `splitInBatches`, `supabase`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`replace-storage-name-database-id-and-credentials.json`](replace-storage-name-database-id-and-credentials.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `supabaseApi`

**Entry nodes:** When clicking ‘Test workflow’, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get All files | `httpRequest` | POST |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Extract Document PDF | `extractFromFile` | pdf |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Create File record2 | `supabase` | Inspect parameters |
| If | `if` | Inspect parameters |
| Get All Files | `supabase` | getAll |
| Download | `httpRequest` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Vector Store Tool1 | `toolVectorStore` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Insert into Supabase Vectorstore | `vectorStoreSupabase` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |

## Connection map

- If → Download (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- Merge → Create File record2 (`main`, output 0, input 0)
- Switch → Merge (`main`, output 0, input 0)
- Switch → Extract Document PDF (`main`, output 1, input 0)
- Download → Switch (`main`, output 0, input 0)
- Aggregate → Get All files (`main`, output 0, input 0)
- Get All Files → Aggregate (`main`, output 0, input 0)
- Get All files → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → If (`main`, output 1, input 0)
- Embeddings OpenAI → Insert into Supabase Vectorstore (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Vector Store Tool1 (`ai_languageModel`, output 0, input 0)
- Vector Store Tool1 → AI Agent (`ai_tool`, output 0, input 0)
- Create File record2 → Insert into Supabase Vectorstore (`main`, output 0, input 0)
- Default Data Loader → Insert into Supabase Vectorstore (`ai_document`, output 0, input 0)
- Extract Document PDF → Merge (`main`, output 0, input 1)
- Supabase Vector Store → Vector Store Tool1 (`ai_vectorStore`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Insert into Supabase Vectorstore → Loop Over Items (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Get All Files (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1246_Extractfromfile_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1246_Extractfromfile_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
