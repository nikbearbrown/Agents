# OpenAI Personal Shopper with RAG and WooCommerce

This folder contains the **OpenAI Personal Shopper with RAG and WooCommerce** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `set`, `textSplitterTokenSplitter`, `toolCalculator`, `toolVectorStore`, `vectorStoreQdrant`, `wooCommerceTool`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`openai-personal-shopper-with-rag-and-woocommerce.json`](openai-personal-shopper-with-rag-and-woocommerce.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`, `wooCommerceApi`

**Entry nodes:** When chat message received, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| RAG | `toolVectorStore` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| personal_shopper | `wooCommerceTool` | getAll |
| Information Extractor | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Google Drive2 | `googleDrive` | fileFolder |
| Google Drive1 | `googleDrive` | download |
| Embeddings OpenAI3 | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader2 | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter1 | `textSplitterTokenSplitter` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- RAG → AI Agent (`ai_tool`, output 0, input 0)
- Calculator → AI Agent (`ai_tool`, output 0, input 0)
- Edit Fields → Information Extractor (`main`, output 0, input 0)
- HTTP Request → Google Drive2 (`main`, output 0, input 0)
- Google Drive1 → Qdrant Vector Store1 (`main`, output 0, input 0)
- Google Drive2 → Google Drive1 (`main`, output 0, input 0)
- Token Splitter1 → Default Data Loader2 (`ai_textSplitter`, output 0, input 0)
- personal_shopper → AI Agent (`ai_tool`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI3 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → RAG (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Information Extractor (`ai_languageModel`, output 0, input 0)
- Qdrant Vector Store → RAG (`ai_vectorStore`, output 0, input 0)
- Default Data Loader2 → Qdrant Vector Store1 (`ai_document`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Information Extractor → AI Agent (`main`, output 0, input 0)
- When chat message received → Edit Fields (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → HTTP Request (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Woocommercetool/1857_Woocommercetool_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Woocommercetool/1857_Woocommercetool_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
