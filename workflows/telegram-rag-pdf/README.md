# Telegram RAG pdf

This folder contains the **Telegram RAG pdf** workflow. Its executable nodes use `chainRetrievalQa`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `if`, `limit`, `lmChatGroq`, `retrieverVectorStore`, `stopAndError`, `telegram`, `telegramTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-rag-pdf.json`](telegram-rag-pdf.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`, `openAiApi`, `pineconeApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Pinecone Vector Store1 | `vectorStorePinecone` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Check If is a document | `if` | Inspect parameters |
| Change to application/pdf | `code` | Inspect parameters |
| Telegram get File | `telegram` | file |
| Embeddings | `embeddingsOpenAi` | Inspect parameters |
| Telegram Response | `telegram` | Inspect parameters |
| Telegram Response about Database | `telegram` | Inspect parameters |
| Stop and Error1 | `stopAndError` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Limit to 1 | `limit` | Inspect parameters |

## Connection map

- Embeddings → Pinecone Vector Store1 (`ai_embedding`, output 0, input 0)
- Limit to 1 → Telegram Response about Database (`main`, output 0, input 0)
- Groq Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Telegram Trigger → Check If is a document (`main`, output 0, input 0)
- Embeddings OpenAI → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Telegram Response → Stop and Error (`main`, output 1, input 0)
- Telegram get File → Change to application/pdf (`main`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- Pinecone Vector Store → Limit to 1 (`main`, output 0, input 0)
- Check If is a document → Telegram get File (`main`, output 0, input 0)
- Check If is a document → Question and Answer Chain (`main`, output 1, input 0)
- Pinecone Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Change to application/pdf → Pinecone Vector Store (`main`, output 0, input 0)
- Question and Answer Chain → Telegram Response (`main`, output 0, input 0)
- Telegram Response about Database → Stop and Error1 (`main`, output 1, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1689_Stopanderror_Telegram_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1689_Stopanderror_Telegram_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
