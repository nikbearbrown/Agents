# News Monitoring Agent

This folder contains the **News Monitoring Agent** workflow. Its executable nodes use `agent`, `chatTrigger`, `convertToFile`, `dataTable`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `embeddingsHuggingFaceInference`, `executeWorkflow`, `extractFromFile`, `filter`, `httpRequest`, `lmChatGoogleGemini`, `lmChatOpenRouter`, `manualTrigger`, `memoryPostgresChat`, `merge`, `outputParserStructured`, `postgres`, `readWriteFile`, `removeDuplicates`, `scheduleTrigger`, `splitOut`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`news-monitoring-agent.json`](news-monitoring-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `huggingFaceApi`, `openRouterApi`, `postgres`, `qdrantApi`

**Entry nodes:** Schedule Trigger, When chat message received, When clicking ‘Execute workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| feedparser fetch | `httpRequest` | POST |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Healthcheck | `httpRequest` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Embeddings HuggingFace Inference | `embeddingsHuggingFaceInference` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Parse | `httpRequest` | POST |
| not null | `filter` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Merge2 | `merge` | Inspect parameters |
| FinBert | `httpRequest` | POST |
| Embeddings HuggingFace Inference4 | `embeddingsHuggingFaceInference` | Inspect parameters |
| View daily KPIs | `postgres` | executeQuery |
| Create Qdrant Collection | `httpRequest` | PUT |
| Write metrics | `postgres` | Inspect parameters |
| Create METRICS table | `postgres` | executeQuery |
| Get row(s) | `dataTable` | get |
| Upsert row(s) | `dataTable` | upsert |
| Split Out | `splitOut` | Inspect parameters |
| Default Data Loader2 | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter2 | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model4 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model5 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model6 | `lmChatGoogleGemini` | Inspect parameters |
| Metaprompt Agentv2 | `agent` | Inspect parameters |
| Metadata Agentv2 | `agent` | Inspect parameters |
| Default Data Loader3 | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter3 | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings Google Gemini1 | `embeddingsGoogleGemini` | Inspect parameters |
| Postgres Chat Memory1 | `memoryPostgresChat` | Inspect parameters |
| Google Gemini Chat Model7 | `lmChatGoogleGemini` | Inspect parameters |
| Qdrant Vector Store A | `vectorStoreQdrant` | Inspect parameters |
| Qdrant Vector Store B | `vectorStoreQdrant` | Inspect parameters |
| News Articles RAG A | `vectorStoreQdrant` | Inspect parameters |
| News Articles RAG B | `vectorStoreQdrant` | Inspect parameters |
| Embeddings Google Gemini2 | `embeddingsGoogleGemini` | Inspect parameters |
| Merge3 | `merge` | Inspect parameters |
| Structured Output Parser test1 | `outputParserStructured` | Inspect parameters |
| Structured Output Parser2 | `outputParserStructured` | Inspect parameters |
| Metaprompt Agentv | `agent` | Inspect parameters |
| Metadata Agentv | `agent` | Inspect parameters |
| Extract from File | `extractFromFile` | Inspect parameters |
| Merge5 | `merge` | Inspect parameters |
| Convert to File1 | `convertToFile` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Read/Write Files from Disk | `readWriteFile` | Inspect parameters |
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| OpenRouter Chat Model3 | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model4 | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model5 | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model6 | `lmChatOpenRouter` | Inspect parameters |
| RAG Agent3 | `agent` | Inspect parameters |
| Google Gemini Chat Model8 | `lmChatGoogleGemini` | Inspect parameters |
| News Articles RAG A2 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings HuggingFace Inference6 | `embeddingsHuggingFaceInference` | Inspect parameters |
| News Articles RAG A3 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings HuggingFace Inference7 | `embeddingsHuggingFaceInference` | Inspect parameters |
| Call rag grader | `executeWorkflow` | Inspect parameters |
| Merge6 | `merge` | Inspect parameters |
| Call rag grader1 | `executeWorkflow` | Inspect parameters |
| Merge4 | `merge` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings HuggingFace Inference8 | `embeddingsHuggingFaceInference` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Metadata structured output | `outputParserStructured` | Inspect parameters |
| Metaprompt structured output | `outputParserStructured` | Inspect parameters |
| Switch - A/B testing | `switch` | Inspect parameters |
| RAG Agent A | `agent` | Inspect parameters |
| RAG Agent B | `agent` | Inspect parameters |

## Connection map

- feedparser fetch → Upsert row(s) (`main`, output 0, input 0)
- feedparser fetch → Split Out (`main`, output 0, input 0)
- Schedule Trigger → Healthcheck (`main`, output 0, input 0)
- Schedule Trigger → Merge2 (`main`, output 0, input 3)
- Healthcheck → Get row(s) (`main`, output 0, input 0)
- Merge1 → Merge2 (`main`, output 0, input 0)
- Merge1 → Qdrant Vector Store A (`main`, output 0, input 0)
- Merge1 → Qdrant Vector Store B (`main`, output 0, input 0)
- Embeddings HuggingFace Inference → Qdrant Vector Store A (`ai_embedding`, output 0, input 0)
- Postgres Chat Memory → RAG Agent A (`ai_memory`, output 0, input 0)
- When chat message received → Metadata Agentv2 (`main`, output 0, input 0)
- When chat message received → Metaprompt Agentv2 (`main`, output 0, input 0)
- Parse → not null (`main`, output 0, input 0)
- not null → FinBert (`main`, output 0, input 0)
- not null → Merge1 (`main`, output 0, input 1)
- Remove Duplicates → Parse (`main`, output 0, input 0)
- Remove Duplicates → Merge2 (`main`, output 0, input 1)
- Merge2 → Write metrics (`main`, output 0, input 0)
- FinBert → Merge1 (`main`, output 0, input 0)
- Embeddings HuggingFace Inference4 → News Articles RAG A (`ai_embedding`, output 0, input 0)
- Get row(s) → feedparser fetch (`main`, output 0, input 0)
- Split Out → Remove Duplicates (`main`, output 0, input 0)
- Split Out → Merge2 (`main`, output 0, input 2)
- Recursive Character Text Splitter2 → Default Data Loader2 (`ai_textSplitter`, output 0, input 0)
- Default Data Loader2 → Qdrant Vector Store A (`ai_document`, output 0, input 0)
- Merge → Switch - A/B testing (`main`, output 0, input 0)
- Google Gemini Chat Model3 → RAG Agent A (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model4 → Metadata structured output (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model → Metadata Agentv2 (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model5 → Metaprompt Agentv2 (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model6 → Metaprompt structured output (`ai_languageModel`, output 0, input 0)
- Metaprompt Agentv2 → Merge (`main`, output 0, input 0)
- Metadata Agentv2 → Merge (`main`, output 0, input 1)
- Default Data Loader3 → Qdrant Vector Store B (`ai_document`, output 0, input 0)
- Recursive Character Text Splitter3 → Default Data Loader3 (`ai_textSplitter`, output 0, input 0)
- Embeddings Google Gemini1 → Qdrant Vector Store B (`ai_embedding`, output 0, input 0)
- Postgres Chat Memory1 → RAG Agent B (`ai_memory`, output 0, input 0)
- Google Gemini Chat Model7 → RAG Agent B (`ai_languageModel`, output 0, input 0)
- News Articles RAG A → RAG Agent A (`ai_tool`, output 0, input 0)
- News Articles RAG B → RAG Agent B (`ai_tool`, output 0, input 0)
- Embeddings Google Gemini2 → News Articles RAG B (`ai_embedding`, output 0, input 0)
- Merge3 → AI Agent (`main`, output 0, input 0)
- Structured Output Parser test1 → Metadata Agentv (`ai_outputParser`, output 0, input 0)
- Structured Output Parser2 → Metaprompt Agentv (`ai_outputParser`, output 0, input 0)
- Metaprompt Agentv → Merge3 (`main`, output 0, input 0)
- Metadata Agentv → Merge3 (`main`, output 0, input 1)
- Extract from File → RAG Agent3 (`main`, output 0, input 0)
- Extract from File → Metaprompt Agentv (`main`, output 0, input 0)
- Extract from File → Metadata Agentv (`main`, output 0, input 0)
- Extract from File → Merge5 (`main`, output 0, input 1)
- Extract from File → Merge6 (`main`, output 0, input 0)
- Merge5 → Call rag grader (`main`, output 0, input 0)
- Read/Write Files from Disk → Extract from File (`main`, output 0, input 0)
- When clicking ‘Execute workflow’ → Read/Write Files from Disk (`main`, output 0, input 0)
- OpenRouter Chat Model4 → Metaprompt Agentv (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model4 → Structured Output Parser2 (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model5 → Metadata Agentv (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model6 → Structured Output Parser test1 (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model8 → RAG Agent3 (`ai_languageModel`, output 0, input 0)
- RAG Agent3 → Merge6 (`main`, output 0, input 1)
- News Articles RAG A2 → RAG Agent3 (`ai_tool`, output 0, input 0)
- Embeddings HuggingFace Inference6 → News Articles RAG A2 (`ai_embedding`, output 0, input 0)
- Embeddings HuggingFace Inference7 → News Articles RAG A3 (`ai_embedding`, output 0, input 0)
- Call rag grader → Merge4 (`main`, output 0, input 0)
- Merge6 → Call rag grader1 (`main`, output 0, input 0)
- Call rag grader1 → Merge4 (`main`, output 0, input 1)
- Merge4 → Convert to File1 (`main`, output 0, input 0)
- Qdrant Vector Store → AI Agent (`ai_tool`, output 0, input 0)
- Embeddings HuggingFace Inference8 → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- AI Agent → Merge5 (`main`, output 0, input 0)
- OpenRouter Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Metadata structured output → Metadata Agentv2 (`ai_outputParser`, output 0, input 0)
- Metaprompt structured output → Metaprompt Agentv2 (`ai_outputParser`, output 0, input 0)
- Switch - A/B testing → RAG Agent A (`main`, output 0, input 0)
- Switch - A/B testing → RAG Agent B (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
