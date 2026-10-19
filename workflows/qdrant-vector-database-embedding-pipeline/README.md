# Qdrant Vector Database Embedding Pipeline

This folder contains the **Qdrant Vector Database Embedding Pipeline** workflow. Its executable nodes use `documentDefaultDataLoader`, `embeddingsOpenAi`, `ftp`, `manualTrigger`, `splitInBatches`, `textSplitterCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`qdrant-vector-database-embedding-pipeline.json`](qdrant-vector-database-embedding-pipeline.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ftp`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Character Text Splitter | `textSplitterCharacterTextSplitter` | Inspect parameters |
| List all the files | `ftp` | list |
| Loop over one item | `splitInBatches` | Inspect parameters |
| Downloading item | `ftp` | Inspect parameters |

## Connection map

- Downloading item → Qdrant Vector Store (`main`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- List all the files → Loop over one item (`main`, output 0, input 0)
- Loop over one item → Downloading item (`main`, output 1, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store → List all the files (`main`, output 0, input 0)
- Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → List all the files (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1776_Manual_Ftp_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1776_Manual_Ftp_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
