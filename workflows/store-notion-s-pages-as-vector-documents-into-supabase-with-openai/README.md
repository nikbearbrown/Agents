# Store Notion's Pages as Vector Documents into Supabase with OpenAI

This folder contains the **Store Notion's Pages as Vector Documents into Supabase with OpenAI** workflow. Its executable nodes use `documentDefaultDataLoader`, `embeddingsOpenAi`, `filter`, `notion`, `notionTrigger`, `summarize`, `textSplitterTokenSplitter`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`store-notion-s-pages-as-vector-documents-into-supabase-with-openai.json`](store-notion-s-pages-as-vector-documents-into-supabase-with-openai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Notion - Page Added Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Notion - Page Added Trigger | `notionTrigger` | Inspect parameters |
| Notion - Retrieve Page Content | `notion` | block / getAll |
| Filter Non-Text Content | `filter` | Inspect parameters |
| Summarize - Concatenate Notion's blocks content | `summarize` | Inspect parameters |
| Create metadata and load content | `documentDefaultDataLoader` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |

## Connection map

- Token Splitter → Create metadata and load content (`ai_textSplitter`, output 0, input 0)
- Embeddings OpenAI → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- Filter Non-Text Content → Summarize - Concatenate Notion's blocks content (`main`, output 0, input 0)
- Notion - Page Added Trigger → Notion - Retrieve Page Content (`main`, output 0, input 0)
- Notion - Retrieve Page Content → Filter Non-Text Content (`main`, output 0, input 0)
- Create metadata and load content → Supabase Vector Store (`ai_document`, output 0, input 0)
- Summarize - Concatenate Notion's blocks content → Supabase Vector Store (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1414_Filter_Summarize_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1414_Filter_Summarize_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
