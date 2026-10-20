# pinecone vector store and receive chat events and download google drive

This folder contains the **pinecone vector store and receive chat events and download google drive** workflow. Its executable nodes use `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pinecone-vector-store-and-receive-chat-events-and-download-google-drive.json`](pinecone-vector-store-and-receive-chat-events-and-download-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `pineconeApi`

**Entry nodes:** When clicking "Execute Workflow", When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Set file URL in Google Drive | `set` | Inspect parameters |
| Download file | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Set max chunks to send to model | `set` | Inspect parameters |
| Get top chunks matching query | `vectorStorePinecone` | Inspect parameters |
| Prepare chunks | `code` | Inspect parameters |
| Answer the query based on chunks | `informationExtractor` | Inspect parameters |
| Compose citations | `set` | Inspect parameters |
| Generate response | `set` | Inspect parameters |

## Connection map

- Download file → Pinecone Vector Store (`main`, output 0, input 0)
- Prepare chunks → Answer the query based on chunks (`main`, output 0, input 0)
- Compose citations → Generate response (`main`, output 0, input 0)
- Embeddings OpenAI → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Get top chunks matching query (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → Answer the query based on chunks (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- When chat message received → Set max chunks to send to model (`main`, output 0, input 0)
- Set file URL in Google Drive → Download file (`main`, output 0, input 0)
- Get top chunks matching query → Prepare chunks (`main`, output 0, input 0)
- Set max chunks to send to model → Get top chunks matching query (`main`, output 0, input 0)
- Answer the query based on chunks → Compose citations (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Set file URL in Google Drive (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0458_Manual_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0458_Manual_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
