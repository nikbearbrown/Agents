# default data loader and download google drive and receive chat events

This folder contains the **default data loader and download google drive and receive chat events** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `lmChatOpenAi`, `manualTrigger`, `outputParserStructured`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`default-data-loader-and-download-google-drive-and-receive-chat-events.json`](default-data-loader-and-download-google-drive-and-receive-chat-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `pineconeApi`

**Entry nodes:** When clicking "Execute Workflow", Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Set file URL in Google Drive | `set` | Inspect parameters |
| Add in metadata | `code` | Inspect parameters |
| Download file | `googleDrive` | download |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Prepare chunks | `code` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Set max chunks to send to model | `set` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Compose citations | `set` | Inspect parameters |
| Generate response | `set` | Inspect parameters |
| Answer the query based on chunks | `chainLlm` | Inspect parameters |
| Get top chunks matching query | `vectorStorePinecone` | Inspect parameters |
| Add to Pinecone vector store | `vectorStorePinecone` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |

## Connection map

- Chat Trigger → Set max chunks to send to model (`main`, output 0, input 0)
- Download file → Add in metadata (`main`, output 0, input 0)
- Prepare chunks → Answer the query based on chunks (`main`, output 0, input 0)
- Add in metadata → Add to Pinecone vector store (`main`, output 0, input 0)
- Compose citations → Generate response (`main`, output 0, input 0)
- Embeddings OpenAI → Add to Pinecone vector store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Answer the query based on chunks (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI2 → Get top chunks matching query (`ai_embedding`, output 0, input 0)
- Default Data Loader → Add to Pinecone vector store (`ai_document`, output 0, input 0)
- Structured Output Parser → Answer the query based on chunks (`ai_outputParser`, output 0, input 0)
- Set file URL in Google Drive → Download file (`main`, output 0, input 0)
- Get top chunks matching query → Prepare chunks (`main`, output 0, input 0)
- Set max chunks to send to model → Get top chunks matching query (`main`, output 0, input 0)
- Answer the query based on chunks → Compose citations (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Set file URL in Google Drive (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1376_Manual_GoogleDrive_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1376_Manual_GoogleDrive_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
