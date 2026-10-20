# Generate Exam Questions

This folder contains the **Generate Exam Questions** workflow. Its executable nodes use `agent`, `chainLlm`, `chainRetrievalQa`, `code`, `convertToFile`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDocs`, `googleSheets`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `outputParserItemList`, `outputParserStructured`, `retrieverVectorStore`, `splitInBatches`, `textSplitterTokenSplitter`, `toolVectorStore`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-exam-questions.json`](generate-exam-questions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Create collection | `httpRequest` | PUT |
| Refresh collection | `httpRequest` | POST |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Converto di MD | `code` | Inspect parameters |
| Get Doc | `googleDocs` | get |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Item List Output Parser | `outputParserItemList` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Item List Output Parser1 | `outputParserItemList` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Qdrant Vector Store2 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| RAG | `toolVectorStore` | Inspect parameters |
| Google Gemini Chat Model4 | `lmChatGoogleGemini` | Inspect parameters |
| Open questions | `chainLlm` | Inspect parameters |
| Closed questions | `chainLlm` | Inspect parameters |
| Answer questions | `chainRetrievalQa` | Inspect parameters |
| Answer and create options | `agent` | Inspect parameters |
| Write open | `googleSheets` | append |
| Write closed | `googleSheets` | append |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |

## Connection map

- RAG → Answer and create options (`ai_tool`, output 0, input 0)
- Get Doc → Converto di MD (`main`, output 0, input 0)
- Write open → Loop Over Items (`main`, output 0, input 0)
- Write closed → Loop Over Items1 (`main`, output 0, input 0)
- Converto di MD → Closed questions (`main`, output 0, input 0)
- Converto di MD → Convert to File (`main`, output 0, input 0)
- Converto di MD → Open questions (`main`, output 0, input 0)
- Open questions → Loop Over Items (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Convert to File → Qdrant Vector Store (`main`, output 0, input 0)
- Loop Over Items → Answer questions (`main`, output 1, input 0)
- Answer questions → Write open (`main`, output 0, input 0)
- Closed questions → Loop Over Items1 (`main`, output 0, input 0)
- Loop Over Items1 → Answer and create options (`main`, output 1, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Qdrant Vector Store2 (`ai_embedding`, output 0, input 0)
- Refresh collection → Get Doc (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Qdrant Vector Store2 → RAG (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Answer questions (`ai_retriever`, output 0, input 0)
- Item List Output Parser → Open questions (`ai_outputParser`, output 0, input 0)
- Google Gemini Chat Model → Open questions (`ai_languageModel`, output 0, input 0)
- Item List Output Parser1 → Closed questions (`ai_outputParser`, output 0, input 0)
- Structured Output Parser → Answer and create options (`ai_outputParser`, output 0, input 0)
- Answer and create options → Write closed (`main`, output 0, input 0)
- Google Gemini Chat Model1 → Answer questions (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Closed questions (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model3 → Answer and create options (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model4 → RAG (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/1134_Googledocs_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/1134_Googledocs_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
