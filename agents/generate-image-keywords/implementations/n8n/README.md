# Generate Image Keywords

This folder contains the **Generate Image Keywords** workflow. Its executable nodes use `documentDefaultDataLoader`, `editImage`, `embeddingsOpenAi`, `googleDrive`, `manualTrigger`, `merge`, `openAi`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreInMemory`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-image-keywords.json`](generate-image-keywords.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Google Drive | `googleDrive` | download |
| Get Color Information | `editImage` | information |
| Resize Image | `editImage` | resize |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Combine Image Analysis | `merge` | Inspect parameters |
| Document for Embedding | `set` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| In-Memory Vector Store | `vectorStoreInMemory` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Search for Image | `vectorStoreInMemory` | Inspect parameters |
| Get Image Keywords | `openAi` | image / analyze |

## Connection map

- Google Drive → Get Color Information (`main`, output 0, input 0)
- Google Drive → Resize Image (`main`, output 0, input 0)
- Resize Image → Get Image Keywords (`main`, output 0, input 0)
- Embeddings OpenAI → In-Memory Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI1 → Search for Image (`ai_embedding`, output 0, input 0)
- Get Image Keywords → Combine Image Analysis (`main`, output 0, input 1)
- Default Data Loader → In-Memory Vector Store (`ai_document`, output 0, input 0)
- Get Color Information → Combine Image Analysis (`main`, output 0, input 0)
- Combine Image Analysis → Document for Embedding (`main`, output 0, input 0)
- Document for Embedding → In-Memory Vector Store (`main`, output 0, input 0)
- When clicking "Test workflow" → Google Drive (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0541_Manual_Stickynote_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0541_Manual_Stickynote_Update_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
