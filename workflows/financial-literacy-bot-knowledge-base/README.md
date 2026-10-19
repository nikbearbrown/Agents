# Financial Literacy Bot - Knowledge Base

This folder contains the **Financial Literacy Bot - Knowledge Base** workflow. Its executable nodes use `documentDefaultDataLoader`, `embeddingsHuggingFaceInference`, `googleDrive`, `manualTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`financial-literacy-bot-knowledge-base.json`](financial-literacy-bot-knowledge-base.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `huggingFaceApi`, `pineconeApi`

**Entry nodes:** When clicking 'Execute workflow'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| When clicking 'Execute workflow' | `manualTrigger` | Inspect parameters |
| Embeddings HuggingFace Inference | `embeddingsHuggingFaceInference` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Search Knowledge Base Files | `googleDrive` | fileFolder |
| Download KB Files | `googleDrive` | download |

## Connection map

- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- When clicking 'Execute workflow' → Search Knowledge Base Files (`main`, output 0, input 0)
- Embeddings HuggingFace Inference → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Search Knowledge Base Files → Download KB Files (`main`, output 0, input 0)
- Download KB Files → Pinecone Vector Store (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
