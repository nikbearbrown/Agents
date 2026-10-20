# Stock Q&A Workflow

This folder contains the **Stock Q&A Workflow** workflow. Its executable nodes use `chainRetrievalQa`, `documentBinaryInputLoader`, `embeddingsOpenAi`, `googleDrive`, `lmChatOpenAi`, `manualChatTrigger`, `manualTrigger`, `respondToWebhook`, `retrieverVectorStore`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`stock-q-a-workflow.json`](stock-q-a-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `qdrantApi`

**Entry nodes:** On new manual Chat Message, Webhook1, When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| On new manual Chat Message | `manualChatTrigger` | Inspect parameters |
| Retrieval QA Chain | `chainRetrievalQa` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Webhook1 | `webhook` | Inspect parameters |
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Google Drive | `googleDrive` | download |
| Binary to Document | `documentBinaryInputLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Webhook1 → Retrieval QA Chain (`main`, output 0, input 0)
- Google Drive → Qdrant Vector Store (`main`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Retrieval QA Chain (`ai_languageModel`, output 0, input 0)
- Binary to Document → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Retrieval QA Chain → Respond to Webhook (`main`, output 0, input 0)
- Qdrant Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Retrieval QA Chain (`ai_retriever`, output 0, input 0)
- On new manual Chat Message → Retrieval QA Chain (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Google Drive (`main`, output 0, input 0)
- Recursive Character Text Splitter → Binary to Document (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1255_Webhook_Respondtowebhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1255_Webhook_Respondtowebhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
