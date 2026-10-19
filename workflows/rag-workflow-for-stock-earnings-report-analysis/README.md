# RAG Workflow For Stock Earnings Report Analysis

This folder contains the **RAG Workflow For Stock Earnings Report Analysis** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `googleDocs`, `googleDrive`, `googleSheets`, `lmChatGoogleGemini`, `lmChatOpenAi`, `manualTrigger`, `splitInBatches`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-workflow-for-stock-earnings-report-analysis.json`](rag-workflow-for-stock-earnings-report-analysis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `openAiApi`, `pineconeApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Vector Store Tool | `toolVectorStore` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Pinecone Vector Store (Retrieval) | `vectorStorePinecone` | Inspect parameters |
| Save Report to Google Docs | `googleDocs` | update |
| Embeddings Google Gemini (retrieval) | `embeddingsGoogleGemini` | Inspect parameters |
| List Of Files To Load (Google Sheets) | `googleSheets` | Inspect parameters |
| Download File From Google Drive | `googleDrive` | download |

## Connection map

- AI Agent → Save Report to Google Docs (`main`, output 0, input 0)
- Loop Over Items → Download File From Google Drive (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Vector Store Tool → AI Agent (`ai_tool`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- Pinecone Vector Store → Loop Over Items (`main`, output 0, input 0)
- Embeddings Google Gemini → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model1 → Vector Store Tool (`ai_languageModel`, output 0, input 0)
- Download File From Google Drive → Pinecone Vector Store (`main`, output 0, input 0)
- Pinecone Vector Store (Retrieval) → Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → AI Agent (`main`, output 0, input 0)
- Embeddings Google Gemini (retrieval) → Pinecone Vector Store (Retrieval) (`ai_embedding`, output 0, input 0)
- List Of Files To Load (Google Sheets) → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/1858_Googledocs_Manual_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/1858_Googledocs_Manual_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
