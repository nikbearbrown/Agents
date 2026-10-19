# RAG AI Agent with Milvus and Cohere

This folder contains the **RAG AI Agent with Milvus and Cohere** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsCohere`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreMilvus`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-ai-agent-with-milvus-and-cohere.json`](rag-ai-agent-with-milvus-and-cohere.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `cohereApi`, `googleDriveOAuth2Api`, `milvusApi`, `openAiApi`

**Entry nodes:** When chat message received, Watch New Files

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Embeddings Cohere | `embeddingsCohere` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Watch New Files | `googleDriveTrigger` | Inspect parameters |
| Download New | `googleDrive` | download |
| Insert into Milvus | `vectorStoreMilvus` | Inspect parameters |
| RAG Agent | `agent` | Inspect parameters |
| Retrieve from Milvus | `vectorStoreMilvus` | Inspect parameters |
| OpenAI 4o | `lmChatOpenAi` | Inspect parameters |
| Memory | `memoryBufferWindow` | Inspect parameters |
| Cohere embeddings | `embeddingsCohere` | Inspect parameters |
| Set Chunks | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |

## Connection map

- Memory → RAG Agent (`ai_memory`, output 0, input 0)
- OpenAI 4o → RAG Agent (`ai_languageModel`, output 0, input 0)
- Set Chunks → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Download New → Extract from File (`main`, output 0, input 0)
- Watch New Files → Download New (`main`, output 0, input 0)
- Cohere embeddings → Retrieve from Milvus (`ai_embedding`, output 0, input 0)
- Embeddings Cohere → Insert into Milvus (`ai_embedding`, output 0, input 0)
- Extract from File → Insert into Milvus (`main`, output 0, input 0)
- Default Data Loader → Insert into Milvus (`ai_document`, output 0, input 0)
- Retrieve from Milvus → RAG Agent (`ai_tool`, output 0, input 0)
- When chat message received → RAG Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0741_Extractfromfile_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0741_Extractfromfile_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
