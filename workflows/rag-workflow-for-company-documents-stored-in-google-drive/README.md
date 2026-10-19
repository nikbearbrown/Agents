# RAG Workflow For Company Documents stored in Google Drive

This folder contains the **RAG Workflow For Company Documents stored in Google Drive** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `googleDrive`, `googleDriveTrigger`, `lmChatGoogleGemini`, `memoryBufferWindow`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-workflow-for-company-documents-stored-in-google-drive.json`](rag-workflow-for-company-documents-stored-in-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `pineconeApi`

**Entry nodes:** Google Drive File Updated, Google Drive File Created, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Vector Store Tool | `toolVectorStore` | Inspect parameters |
| Pinecone Vector Store (Retrieval) | `vectorStorePinecone` | Inspect parameters |
| Embeddings Google Gemini (retrieval) | `embeddingsGoogleGemini` | Inspect parameters |
| Download File From Google Drive | `googleDrive` | download |
| Google Drive File Updated | `googleDriveTrigger` | Inspect parameters |
| Google Drive File Created | `googleDriveTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model (retrieval) | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Vector Store Tool → AI Agent (`ai_tool`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Embeddings Google Gemini → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Drive File Created → Download File From Google Drive (`main`, output 0, input 0)
- Google Drive File Updated → Download File From Google Drive (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Download File From Google Drive → Pinecone Vector Store (`main`, output 0, input 0)
- Pinecone Vector Store (Retrieval) → Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Embeddings Google Gemini (retrieval) → Pinecone Vector Store (Retrieval) (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model (retrieval) → Vector Store Tool (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1626_Stickynote_GoogleDrive_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1626_Stickynote_GoogleDrive_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
