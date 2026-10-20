# Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration

This folder contains the **Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration** workflow. Its executable nodes use `chainRetrievalQa`, `documentDefaultDataLoader`, `embeddingsOllama`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `function`, `httpRequest`, `if`, `lmChatGoogleGemini`, `merge`, `noOp`, `respondToWebhook`, `retrieverVectorStore`, `set`, `splitOut`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`bitrix24-open-chanel-rag-chatbot-application-workflow-example-with-webhook-integration.json`](bitrix24-open-chanel-rag-chatbot-application-workflow-example-with-webhook-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Bitrix24 Handler, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Bitrix24 Handler | `webhook` | Inspect parameters |
| Credentials | `set` | Inspect parameters |
| Validate Token | `if` | Inspect parameters |
| Route Event | `switch` | Inspect parameters |
| Process Message | `function` | Inspect parameters |
| Process Join | `function` | Inspect parameters |
| Process Install | `function` | Inspect parameters |
| Register Bot | `httpRequest` | POST |
| Send Message | `httpRequest` | POST |
| Send Join Message | `httpRequest` | POST |
| Process Delete | `noOp` | Inspect parameters |
| Success Response | `respondToWebhook` | Inspect parameters |
| Error Response | `respondToWebhook` | Inspect parameters |
| Merge parameters for Subworkflow | `merge` | Inspect parameters |
| Get a list of available storages | `httpRequest` | POST |
| Get a list of List of Files and Folders | `httpRequest` | POST |
| Get a list of Folders files | `httpRequest` | POST |
| Download file | `httpRequest` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Split Out folder files and folders | `splitOut` | Inspect parameters |
| Filter for files | `filter` | Inspect parameters |
| Move files to Vector stored folder | `httpRequest` | POST |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings Ollama | `embeddingsOllama` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Prepare output parameters | `set` | Inspect parameters |
| Embeddings Ollama1 | `embeddingsOllama` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Execute subworkflow | `executeWorkflow` | Inspect parameters |

## Connection map

- Credentials → Validate Token (`main`, output 0, input 0)
- Credentials → Merge parameters for Subworkflow (`main`, output 0, input 1)
- Route Event → Process Message (`main`, output 0, input 0)
- Route Event → Process Join (`main`, output 1, input 0)
- Route Event → Process Install (`main`, output 2, input 0)
- Route Event → Process Delete (`main`, output 3, input 0)
- Process Join → Send Join Message (`main`, output 0, input 0)
- Register Bot → Success Response (`main`, output 0, input 0)
- Register Bot → Merge parameters for Subworkflow (`main`, output 0, input 0)
- Send Message → Success Response (`main`, output 0, input 0)
- Download file → Move files to Vector stored folder (`main`, output 0, input 0)
- Download file → Qdrant Vector Store (`main`, output 0, input 0)
- Process Delete → Success Response (`main`, output 0, input 0)
- Validate Token → Route Event (`main`, output 0, input 0)
- Validate Token → Error Response (`main`, output 1, input 0)
- Process Install → Register Bot (`main`, output 0, input 0)
- Process Message → Question and Answer Chain (`main`, output 0, input 0)
- Bitrix24 Handler → Credentials (`main`, output 0, input 0)
- Filter for files → Download file (`main`, output 0, input 0)
- Embeddings Ollama → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Send Join Message → Success Response (`main`, output 0, input 0)
- Embeddings Ollama1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Execute subworkflow → Success Response (`main`, output 0, input 0)
- Qdrant Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Execute Workflow Trigger → Get a list of available storages (`main`, output 0, input 0)
- Google Gemini Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Prepare output parameters → Send Message (`main`, output 0, input 0)
- Question and Answer Chain → Prepare output parameters (`main`, output 0, input 0)
- Get a list of Folders files → Split Out folder files and folders (`main`, output 0, input 0)
- Get a list of available storages → Get a list of List of Files and Folders (`main`, output 0, input 0)
- Merge parameters for Subworkflow → Execute subworkflow (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Split Out folder files and folders → Filter for files (`main`, output 0, input 0)
- Get a list of List of Files and Folders → Get a list of Folders files (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1355_Splitout_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1355_Splitout_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
