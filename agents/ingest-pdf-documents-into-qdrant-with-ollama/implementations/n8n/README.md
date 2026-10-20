# qdrant

This folder contains the **qdrant** workflow. Its executable nodes use `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsOllama`, `extractFromFile`, `if`, `splitOut`, `textSplitterTokenSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ingest-pdf-documents-into-qdrant-with-ollama.json`](ingest-pdf-documents-into-qdrant-with-ollama.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`, `qdrantApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings Ollama | `embeddingsOllama` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| IF: PDF | `if` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| Split Out | `splitOut` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- When chat message received → IF: PDF (`main`, output 0, input 0)
- Embeddings Ollama → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- IF: PDF → Extract from File (`main`, output 0, input 0)
- Extract from File → Split Out (`main`, output 0, input 0)
- Split Out → Code (`main`, output 0, input 0)
- Code → Qdrant Vector Store (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/ums11/indproject/blob/a6989aaa94e1557def997c801537378470dc382b/qdrant.json](https://github.com/ums11/indproject/blob/a6989aaa94e1557def997c801537378470dc382b/qdrant.json). License: **MIT**; preserve [the notice](../../../../licenses/ums11--indproject.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
