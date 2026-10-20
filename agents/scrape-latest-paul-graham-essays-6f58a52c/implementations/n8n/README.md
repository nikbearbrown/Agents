# Scrape latest Paul Graham essays

This folder contains the **Scrape latest Paul Graham essays** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `html`, `httpRequest`, `limit`, `lmChatOpenAi`, `manualTrigger`, `retrieverVectorStore`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreMilvus`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-latest-paul-graham-essays-6f58a52c.json`](scrape-latest-paul-graham-essays-6f58a52c.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking "Execute Workflow", When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Fetch Essay List | `httpRequest` | Inspect parameters |
| Extract essay names | `html` | extractHtmlContent |
| Split out into items | `splitOut` | Inspect parameters |
| Fetch essay texts | `httpRequest` | Inspect parameters |
| Limit to first 3 | `limit` | Inspect parameters |
| Extract Text Only | `html` | extractHtmlContent |
| When chat message received | `chatTrigger` | Inspect parameters |
| Milvus Vector Store | `vectorStoreMilvus` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Milvus Vector Store1 | `vectorStoreMilvus` | Inspect parameters |
| Q&A Chain to Retrieve from Milvus and Answer Question | `chainRetrievalQa` | Inspect parameters |
| Milvus Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |

## Connection map

- Fetch Essay List → Extract essay names (`main`, output 0, input 0)
- Limit to first 3 → Fetch essay texts (`main`, output 0, input 0)
- Embeddings OpenAI → Milvus Vector Store (`ai_embedding`, output 0, input 0)
- Extract Text Only → Milvus Vector Store (`main`, output 0, input 0)
- Fetch essay texts → Extract Text Only (`main`, output 0, input 0)
- OpenAI Chat Model → Q&A Chain to Retrieve from Milvus and Answer Question (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Milvus Vector Store1 (`ai_embedding`, output 0, input 0)
- Default Data Loader → Milvus Vector Store (`ai_document`, output 0, input 0)
- Extract essay names → Split out into items (`main`, output 0, input 0)
- Milvus Vector Store1 → Milvus Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Split out into items → Limit to first 3 (`main`, output 0, input 0)
- When chat message received → Q&A Chain to Retrieve from Milvus and Answer Question (`main`, output 0, input 0)
- Milvus Vector Store Retriever → Q&A Chain to Retrieve from Milvus and Answer Question (`ai_retriever`, output 0, input 0)
- When clicking "Execute Workflow" → Fetch Essay List (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0860_Splitout_Limit_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0860_Splitout_Limit_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
