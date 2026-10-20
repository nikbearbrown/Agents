# Finance Literacy Bot - Chatbot w/ Memory

This folder contains the **Finance Literacy Bot - Chatbot w/ Memory** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `embeddingsHuggingFaceInference`, `httpRequest`, `lmChatGroq`, `memoryBufferWindow`, `postgres`, `respondToWebhook`, `set`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`finance-literacy-bot-chatbot-w-memory.json`](finance-literacy-bot-chatbot-w-memory.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`, `httpHeaderAuth`, `huggingFaceApi`, `pineconeApi`, `postgres`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings HuggingFace Inference1 | `embeddingsHuggingFaceInference` | Inspect parameters |
| Fetch User History | `postgres` | executeQuery |
| Code in JavaScript | `code` | Inspect parameters |
| Parse Gap Analysis | `set` | Inspect parameters |
| Groq - Gap Analysis | `httpRequest` | POST |
| Update DB - User Interactions | `postgres` | Inspect parameters |
| Update DB - User Knowledge Profile | `postgres` | executeQuery |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- When chat message received → Fetch User History (`main`, output 0, input 0)
- Groq Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Pinecone Vector Store → AI Agent (`ai_tool`, output 0, input 0)
- Embeddings HuggingFace Inference1 → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Fetch User History → Code in JavaScript (`main`, output 0, input 0)
- Code in JavaScript → Groq - Gap Analysis (`main`, output 0, input 0)
- Parse Gap Analysis → AI Agent (`main`, output 0, input 0)
- Groq - Gap Analysis → Parse Gap Analysis (`main`, output 0, input 0)
- AI Agent → Respond to Webhook (`main`, output 0, input 0)
- AI Agent → Update DB - User Knowledge Profile (`main`, output 0, input 0)
- AI Agent → Update DB - User Interactions (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
