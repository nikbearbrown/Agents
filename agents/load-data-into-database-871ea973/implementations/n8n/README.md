# Load data into database

This folder contains the **Load data into database** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `lmChatOpenAi`, `manualTrigger`, `retrieverVectorStore`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`load-data-into-database-871ea973.json`](load-data-into-database-871ea973.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `pineconeApi`

**Entry nodes:** When clicking 'Chat' button below, When clicking 'Test Workflow' button

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive | `googleDrive` | download |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Read Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Insert into Pinecone vector store | `vectorStorePinecone` | Inspect parameters |
| When clicking 'Chat' button below | `chatTrigger` | Inspect parameters |
| When clicking 'Test Workflow' button | `manualTrigger` | Inspect parameters |
| Set Google Drive file URL | `set` | Inspect parameters |

## Connection map

- Google Drive → Insert into Pinecone vector store (`main`, output 0, input 0)
- Embeddings OpenAI → Insert into Pinecone vector store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI2 → Read Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Default Data Loader → Insert into Pinecone vector store (`ai_document`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Set Google Drive file URL → Google Drive (`main`, output 0, input 0)
- Read Pinecone Vector Store → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking 'Chat' button below → Question and Answer Chain (`main`, output 0, input 0)
- When clicking 'Test Workflow' button → Set Google Drive file URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1319_Manual_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1319_Manual_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
