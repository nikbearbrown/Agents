# Local chatbot with retrieval augmented generation (RAG) Gemini

This folder contains the **Local chatbot with retrieval augmented generation (RAG) Gemini** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOllama`, `formTrigger`, `httpRequest`, `lmChatGoogleGemini`, `memoryBufferWindow`, `merge`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`local-chatbot-with-retrieval-augmented-generation-rag-gemini.json`](local-chatbot-with-retrieval-augmented-generation-rag-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `ollamaApi`, `qdrantApi`

**Entry nodes:** When chat message received, On form submission1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings Ollama | `embeddingsOllama` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| On form submission1 | `formTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| Simple Memory1 | `memoryBufferWindow` | Inspect parameters |
| Embeddings Ollama2 | `embeddingsOllama` | Inspect parameters |
| Qdrant Vector Store2 | `vectorStoreQdrant` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Merge | `merge` | Inspect parameters |

## Connection map

- Embeddings Ollama → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- When chat message received → AI Agent1 (`main`, output 0, input 0)
- When chat message received → Merge (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- On form submission1 → Qdrant Vector Store (`main`, output 0, input 0)
- Simple Memory1 → AI Agent1 (`ai_memory`, output 0, input 0)
- Qdrant Vector Store2 → AI Agent1 (`ai_tool`, output 0, input 0)
- Embeddings Ollama2 → Qdrant Vector Store2 (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → AI Agent1 (`ai_languageModel`, output 0, input 0)
- AI Agent1 → Merge (`main`, output 0, input 1)
- Merge → HTTP Request (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/algonacci/rag-evaluation/blob/5a0256acc2f538259f7ec60a71f6991a0365fb41/sumber.json](https://github.com/algonacci/rag-evaluation/blob/5a0256acc2f538259f7ec60a71f6991a0365fb41/sumber.json). License: **MIT**; preserve [the notice](../../licenses/algonacci--rag-evaluation.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
