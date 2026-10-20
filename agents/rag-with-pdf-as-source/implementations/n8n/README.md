# RAG with PDF as source

This folder contains the **RAG with PDF as source** workflow. Its executable nodes use `agent`, `chainRetrievalQa`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `gmail`, `gmailTrigger`, `httpRequest`, `if`, `lmChatAnthropic`, `lmChatOpenAi`, `memoryBufferWindow`, `noOp`, `retrieverVectorStore`, `slack`, `textClassifier`, `textSplitterRecursiveCharacterTextSplitter`, `toolHttpRequest`, `vectorStorePinecone`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-with-pdf-as-source.json`](rag-with-pdf-as-source.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When chat message received, On new email to nathan's inbox, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Send message | `slack` | Inspect parameters |
| Execute JavaScript | `code` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Download PDF | `httpRequest` | Inspect parameters |
| PDFs to download | `noOp` | Inspect parameters |
| Read Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Get calendar availability | `toolHttpRequest` | POST |
| Appointment booking agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Insert into Pinecone vector store | `vectorStorePinecone` | Inspect parameters |
| Book appointment | `toolHttpRequest` | POST |
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Add automation label | `gmail` | addLabels |
| On new email to nathan's inbox | `gmailTrigger` | Inspect parameters |
| Add music label | `gmail` | addLabels |
| Assign label with AI | `textClassifier` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Whether email contains n8n | `if` | Inspect parameters |

## Connection map

- Webhook → Whether email contains n8n (`main`, output 0, input 0)
- Download PDF → Insert into Pinecone vector store (`main`, output 0, input 0)
- Book appointment → Appointment booking agent (`ai_tool`, output 0, input 0)
- PDFs to download → Download PDF (`main`, output 0, input 0)
- Embeddings OpenAI → Insert into Pinecone vector store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI2 → Read Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → Assign label with AI (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Insert into Pinecone vector store (`ai_document`, output 0, input 0)
- Anthropic Chat Model → Appointment booking agent (`ai_languageModel`, output 0, input 0)
- Assign label with AI → Add automation label (`main`, output 0, input 0)
- Assign label with AI → Add music label (`main`, output 1, input 0)
- Window Buffer Memory → Appointment booking agent (`ai_memory`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Get calendar availability → Appointment booking agent (`ai_tool`, output 0, input 0)
- Read Pinecone Vector Store → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- When chat message received → Question and Answer Chain (`main`, output 0, input 0)
- Whether email contains n8n → Execute JavaScript (`main`, output 0, input 0)
- Whether email contains n8n → Send message (`main`, output 0, input 0)
- On new email to nathan's inbox → Assign label with AI (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0548_Code_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0548_Code_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
