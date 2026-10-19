# receive local file events and read write file and default data loader

This folder contains the **receive local file events and read write file and default data loader** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsMistralCloud`, `httpRequest`, `if`, `lmChatMistralCloud`, `localFileTrigger`, `manualTrigger`, `readWriteFile`, `retrieverVectorStore`, `set`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-local-file-events-and-read-write-file-and-default-data-loader.json`](receive-local-file-events-and-read-write-file-and-default-data-loader.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mistralCloudApi`, `qdrantApi`

**Entry nodes:** Local File Trigger, When clicking "Test workflow", Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Local File Trigger | `localFileTrigger` | Inspect parameters |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Read File | `readWriteFile` | Inspect parameters |
| Embeddings Mistral Cloud | `embeddingsMistralCloud` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Prepare Embedding Document | `set` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Mistral Cloud Chat Model | `lmChatMistralCloud` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Embeddings Mistral Cloud1 | `embeddingsMistralCloud` | Inspect parameters |
| Remap for File_Added Flow | `set` | Inspect parameters |
| Search For Existing Point | `httpRequest` | POST |
| Has Existing Point? | `if` | Inspect parameters |
| Delete Existing Point | `httpRequest` | POST |
| Search For Existing Point1 | `httpRequest` | POST |
| Has Existing Point?1 | `if` | Inspect parameters |
| Delete Existing Point1 | `httpRequest` | POST |
| Handle File Event | `switch` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |

## Connection map

- Read File → Prepare Embedding Document (`main`, output 0, input 0)
- Chat Trigger → Question and Answer Chain (`main`, output 0, input 0)
- Set Variables → Handle File Event (`main`, output 0, input 0)
- Handle File Event → Search For Existing Point (`main`, output 0, input 0)
- Handle File Event → Search For Existing Point1 (`main`, output 1, input 0)
- Handle File Event → Read File (`main`, output 2, input 0)
- Local File Trigger → Set Variables (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Has Existing Point? → Delete Existing Point1 (`main`, output 0, input 0)
- Has Existing Point?1 → Delete Existing Point (`main`, output 0, input 0)
- Qdrant Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Delete Existing Point → Remap for File_Added Flow (`main`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Embeddings Mistral Cloud → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Mistral Cloud Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Embeddings Mistral Cloud1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Remap for File_Added Flow → Read File (`main`, output 0, input 0)
- Search For Existing Point → Has Existing Point? (`main`, output 0, input 0)
- Prepare Embedding Document → Qdrant Vector Store (`main`, output 0, input 0)
- Search For Existing Point1 → Has Existing Point?1 (`main`, output 0, input 0)
- When clicking "Test workflow" → Set Variables (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Localfile/0535_Localfile_Manual_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Localfile/0535_Localfile_Manual_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
