# Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

This folder contains the **Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflowTrigger`, `extractFromFile`, `github`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `merge`, `set`, `splitOut`, `textSplitterTokenSplitter`, `toolWorkflow`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai.json`](building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’, When chat message received, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| GitHub | `github` | file / get |
| Extract from File | `extractFromFile` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Call n8n Workflow Tool | `toolWorkflow` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Embedding Recommendation Request with Open AI | `httpRequest` | POST |
| Embedding Anti-Recommendation Request with Open AI | `httpRequest` | POST |
| Extracting Embedding | `set` | Inspect parameters |
| Extracting Embedding1 | `set` | Inspect parameters |
| Calling Qdrant Recommendation API | `httpRequest` | POST |
| Retrieving Recommended Movies Meta Data | `httpRequest` | POST |
| Selecting Fields Relevant for Agent | `set` | Inspect parameters |

## Connection map

- Merge → Calling Qdrant Recommendation API (`main`, output 0, input 0)
- GitHub → Extract from File (`main`, output 0, input 0)
- Merge1 → Selecting Fields Relevant for Agent (`main`, output 0, input 0)
- Split Out → Merge1 (`main`, output 0, input 1)
- Split Out1 → Merge1 (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Extract from File → Qdrant Vector Store (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Extracting Embedding → Merge (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Extracting Embedding1 → Merge (`main`, output 0, input 1)
- Call n8n Workflow Tool → AI Agent (`ai_tool`, output 0, input 0)
- Execute Workflow Trigger → Embedding Recommendation Request with Open AI (`main`, output 0, input 0)
- Execute Workflow Trigger → Embedding Anti-Recommendation Request with Open AI (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Calling Qdrant Recommendation API → Retrieving Recommended Movies Meta Data (`main`, output 0, input 0)
- Calling Qdrant Recommendation API → Split Out1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → GitHub (`main`, output 0, input 0)
- Selecting Fields Relevant for Agent → Aggregate (`main`, output 0, input 0)
- Retrieving Recommended Movies Meta Data → Split Out (`main`, output 0, input 0)
- Embedding Recommendation Request with Open AI → Extracting Embedding (`main`, output 0, input 0)
- Embedding Anti-Recommendation Request with Open AI → Extracting Embedding1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1798_Splitout_GitHub_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1798_Splitout_GitHub_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
