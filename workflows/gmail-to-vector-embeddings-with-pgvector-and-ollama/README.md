# Gmail to Vector Embeddings with PGVector and Ollama

This folder contains the **Gmail to Vector Embeddings with PGVector and Ollama** workflow. Its executable nodes use `code`, `documentDefaultDataLoader`, `embeddingsOllama`, `gmail`, `gmailTrigger`, `if`, `manualTrigger`, `noOp`, `postgres`, `set`, `splitInBatches`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePGVector`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`gmail-to-vector-embeddings-with-pgvector-and-ollama.json`](gmail-to-vector-embeddings-with-pgvector-and-ollama.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Gmail Trigger, Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings Ollama | `embeddingsOllama` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Was manually triggered? | `if` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Set before and after dates | `set` | Inspect parameters |
| Extract email fields | `set` | Inspect parameters |
| Store structured | `postgres` | upsert |
| Store vectorized | `vectorStorePGVector` | Inspect parameters |
| Create the table | `postgres` | executeQuery |
| Explode interval into weeks | `code` | Inspect parameters |
| Get a batch of messages | `gmail` | getAll |

## Connection map

- Split Out → Loop Over Items (`main`, output 0, input 0)
- Gmail Trigger → Extract email fields (`main`, output 0, input 0)
- Manual Trigger → Create the table (`main`, output 0, input 0)
- Loop Over Items → Set before and after dates (`main`, output 1, input 0)
- Create the table → Explode interval into weeks (`main`, output 0, input 0)
- Store structured → Store vectorized (`main`, output 0, input 0)
- Store structured → Loop Over Items (`main`, output 1, input 0)
- Store vectorized → Was manually triggered? (`main`, output 0, input 0)
- Embeddings Ollama → Store vectorized (`ai_embedding`, output 0, input 0)
- Default Data Loader → Store vectorized (`ai_document`, output 0, input 0)
- Extract email fields → Store structured (`main`, output 0, input 0)
- Get a batch of messages → Extract email fields (`main`, output 0, input 0)
- Was manually triggered? → No Operation, do nothing (`main`, output 0, input 0)
- Was manually triggered? → Loop Over Items (`main`, output 1, input 0)
- Set before and after dates → Get a batch of messages (`main`, output 0, input 0)
- Explode interval into weeks → Split Out (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1783_Splitout_Postgres_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1783_Splitout_Postgres_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
