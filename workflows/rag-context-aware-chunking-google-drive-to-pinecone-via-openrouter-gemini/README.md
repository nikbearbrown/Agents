# RAG:Context-Aware Chunking \| Google Drive to Pinecone via OpenRouter & Gemini

This folder contains the **RAG:Context-Aware Chunking \| Google Drive to Pinecone via OpenRouter & Gemini** workflow. Its executable nodes use `agent`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `extractFromFile`, `googleDrive`, `lmChatOpenRouter`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-gemini.json`](rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `openRouterApi`, `pineconeApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Get Document From Google Drive | `googleDrive` | download |
| Extract Text Data From Google Document | `extractFromFile` | text |
| Split Document Text Into Sections | `code` | Inspect parameters |
| Prepare Sections For Looping | `splitOut` | Inspect parameters |
| AI Agent - Prepare Context | `agent` | Inspect parameters |
| Concatenate the context and section text | `set` | Inspect parameters |

## Connection map

- Loop Over Items → AI Agent - Prepare Context (`main`, output 1, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- OpenRouter Chat Model → AI Agent - Prepare Context (`ai_languageModel`, output 0, input 0)
- Pinecone Vector Store → Loop Over Items (`main`, output 0, input 0)
- Embeddings Google Gemini → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- AI Agent - Prepare Context → Concatenate the context and section text (`main`, output 0, input 0)
- Prepare Sections For Looping → Loop Over Items (`main`, output 0, input 0)
- Get Document From Google Drive → Extract Text Data From Google Document (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Split Document Text Into Sections → Prepare Sections For Looping (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Document From Google Drive (`main`, output 0, input 0)
- Extract Text Data From Google Document → Split Document Text Into Sections (`main`, output 0, input 0)
- Concatenate the context and section text → Pinecone Vector Store (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1627_Splitout_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1627_Splitout_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
