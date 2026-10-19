# receive chat events and qdrant vector store and retrieval qa chain

This folder contains the **receive chat events and qdrant vector store and retrieval qa chain** workflow. Its executable nodes use `chainRetrievalQa`, `chatTrigger`, `embeddingsOllama`, `httpRequest`, `lmChatGoogleGemini`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-chat-events-and-qdrant-vector-store-and-retrieval-qa-chain.json`](receive-chat-events-and-qdrant-vector-store-and-retrieval-qa-chain.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Embeddings Ollama | `embeddingsOllama` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Retrieval QA Chain | `chainRetrievalQa` | Inspect parameters |
| RAG Evaluation Webhook | `httpRequest` | POST |

## Connection map

- When chat message received → Retrieval QA Chain (`main`, output 0, input 0)
- Google Gemini Chat Model → Retrieval QA Chain (`ai_languageModel`, output 0, input 0)
- Embeddings Ollama → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Qdrant Vector Store → Retrieval QA Chain (`ai_retriever`, output 0, input 0)
- Retrieval QA Chain → RAG Evaluation Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/algonacci/rag-evaluation/blob/5a0256acc2f538259f7ec60a71f6991a0365fb41/anjay.json](https://github.com/algonacci/rag-evaluation/blob/5a0256acc2f538259f7ec60a71f6991a0365fb41/anjay.json). License: **MIT**; preserve [the notice](../../licenses/algonacci--rag-evaluation.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
