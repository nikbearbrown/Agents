# 🙋‍♀️What's the difference?

This folder contains the **🙋‍♀️What's the difference?** workflow. Its executable nodes use `agent`, `chatTrigger`, `compression`, `documentDefaultDataLoader`, `embeddingsMistralCloud`, `executeWorkflowTrigger`, `extractFromFile`, `filter`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `set`, `splitInBatches`, `splitOut`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `toolWorkflow`, `vectorStoreQdrant`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`what-s-the-difference.json`](what-s-the-difference.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mistralCloudApi`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Embeddings Mistral Cloud | `embeddingsMistralCloud` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Get Tax Code Zip File | `httpRequest` | Inspect parameters |
| Extract Zip Files | `compression` | Inspect parameters |
| Files as Items | `splitOut` | Inspect parameters |
| Extract PDF Contents | `extractFromFile` | pdf |
| Extract From Chapter | `set` | Inspect parameters |
| Map To Sections | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Get Mistral Embeddings | `httpRequest` | POST |
| Content Chunking @ 50k Chars | `set` | Inspect parameters |
| Split Out Chunks | `splitOut` | Inspect parameters |
| For Each Section... | `splitInBatches` | Inspect parameters |
| Sections To List | `splitOut` | Inspect parameters |
| Only Valid Sections | `filter` | Inspect parameters |
| Use Qdrant Search API1 | `httpRequest` | POST |
| Use Qdrant Scroll API | `httpRequest` | POST |
| Get Search Response | `set` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Window Buffer Memory1 | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| 1sec | `wait` | Inspect parameters |
| Ask Tool | `toolWorkflow` | Inspect parameters |
| Search Tool | `toolWorkflow` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Get Ask Response | `set` | Inspect parameters |

## Connection map

- 1sec → For Each Section... (`main`, output 0, input 0)
- Switch → Get Mistral Embeddings (`main`, output 0, input 0)
- Switch → Use Qdrant Scroll API (`main`, output 1, input 0)
- Ask Tool → AI Agent (`ai_tool`, output 0, input 0)
- Search Tool → AI Agent (`ai_tool`, output 0, input 0)
- Files as Items → Extract PDF Contents (`main`, output 0, input 0)
- Map To Sections → Sections To List (`main`, output 0, input 0)
- Sections To List → Only Valid Sections (`main`, output 0, input 0)
- Split Out Chunks → Qdrant Vector Store (`main`, output 0, input 0)
- Extract Zip Files → Files as Items (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- For Each Section... → Content Chunking @ 50k Chars (`main`, output 1, input 0)
- Only Valid Sections → For Each Section... (`main`, output 0, input 0)
- Qdrant Vector Store → 1sec (`main`, output 0, input 0)
- Extract From Chapter → Map To Sections (`main`, output 0, input 0)
- Extract PDF Contents → Extract From Chapter (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Get Tax Code Zip File → Extract Zip Files (`main`, output 0, input 0)
- Use Qdrant Scroll API → Get Search Response (`main`, output 0, input 0)
- Window Buffer Memory1 → When chat message received (`ai_memory`, output 0, input 0)
- Get Mistral Embeddings → Use Qdrant Search API1 (`main`, output 0, input 0)
- Use Qdrant Search API1 → Get Ask Response (`main`, output 0, input 0)
- Embeddings Mistral Cloud → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Execute Workflow Trigger → Switch (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Content Chunking @ 50k Chars → Split Out Chunks (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Tax Code Zip File (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0538_Wait_Splitout_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0538_Wait_Splitout_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
