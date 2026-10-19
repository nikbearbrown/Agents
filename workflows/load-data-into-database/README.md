# Load data into database

This folder contains the **Load data into database** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `lmChatOpenAi`, `manualTrigger`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`load-data-into-database.json`](load-data-into-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `pineconeApi`

**Entry nodes:** When clicking 'Test Workflow' button, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking 'Test Workflow' button | `manualTrigger` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Question & Answer | `agent` | Inspect parameters |
| Set Google Drive file URL | `set` | Inspect parameters |
| Google Drive | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Pinecone Vector Store1 | `vectorStorePinecone` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Google Drive → Pinecone Vector Store (`main`, output 0, input 0)
- Embeddings OpenAI → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Question & Answer (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Pinecone Vector Store1 (`ai_embedding`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- Pinecone Vector Store1 → Question & Answer (`ai_tool`, output 0, input 0)
- Set Google Drive file URL → Google Drive (`main`, output 0, input 0)
- When chat message received → Question & Answer (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking 'Test Workflow' button → Set Google Drive file URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0326_Manual_Stickynote_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0326_Manual_Stickynote_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
