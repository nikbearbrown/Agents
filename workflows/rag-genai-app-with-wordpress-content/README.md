# RAG & GenAI App With WordPress Content

This folder contains the **RAG & GenAI App With WordPress Content** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `filter`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `memoryPostgresChat`, `merge`, `postgres`, `respondToWebhook`, `scheduleTrigger`, `set`, `splitInBatches`, `supabase`, `switch`, `textSplitterTokenSplitter`, `vectorStoreSupabase`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-genai-app-with-wordpress-content.json`](rag-genai-app-with-wordpress-content.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’, Every 30 seconds, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Set fields | `set` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader1 | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter1 | `textSplitterTokenSplitter` | Inspect parameters |
| Markdown1 | `markdown` | Inspect parameters |
| Postgres | `postgres` | executeQuery |
| Aggregate | `aggregate` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| Aggregate2 | `aggregate` | Inspect parameters |
| Wordpress - Get all posts | `wordpress` | getAll |
| Wordpress - Get all pages | `wordpress` | page / getAll |
| Set fields1 | `set` | Inspect parameters |
| Filter - Only published &  unprotected content | `filter` | Inspect parameters |
| HTML To Markdown | `markdown` | Inspect parameters |
| Supabase - Store workflow execution | `supabase` | Inspect parameters |
| Every 30 seconds | `scheduleTrigger` | Inspect parameters |
| Wordpress - Get posts modified after last workflow execution | `httpRequest` | Inspect parameters |
| Wordpress - Get posts modified after last workflow execution1 | `httpRequest` | Inspect parameters |
| Set fields2 | `set` | Inspect parameters |
| Filter - Only published and unprotected content | `filter` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Set fields3 | `set` | Inspect parameters |
| Set fields4 | `set` | Inspect parameters |
| Store documents on Supabase | `vectorStoreSupabase` | Inspect parameters |
| Store workflow execution id and timestamptz | `supabase` | Inspect parameters |
| Aggregate documents | `aggregate` | Inspect parameters |
| Postgres - Create documents table | `postgres` | executeQuery |
| Postgres - Create workflow execution history table | `postgres` | executeQuery |
| Merge Wordpress Posts and Pages | `merge` | Inspect parameters |
| Merge retrieved WordPress posts and pages | `merge` | Inspect parameters |
| Postgres - Filter on existing documents | `postgres` | executeQuery |
| Supabase - Delete row if documents exists | `supabase` | delete |
| Switch | `switch` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Supabase - Retrieve documents from chatinput | `vectorStoreSupabase` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |

## Connection map

- Switch → Supabase - Delete row if documents exists (`main`, output 0, input 0)
- Switch → Set fields4 (`main`, output 1, input 0)
- AI Agent → Respond to Webhook (`main`, output 0, input 0)
- Postgres → Wordpress - Get posts modified after last workflow execution (`main`, output 0, input 0)
- Postgres → Wordpress - Get posts modified after last workflow execution1 (`main`, output 0, input 0)
- Aggregate → Supabase - Store workflow execution (`main`, output 0, input 0)
- Markdown1 → Store documents on Supabase (`main`, output 0, input 0)
- Aggregate1 → Store workflow execution id and timestamptz (`main`, output 0, input 0)
- Aggregate2 → Set fields3 (`main`, output 0, input 0)
- Set fields → AI Agent (`main`, output 0, input 0)
- Set fields1 → Filter - Only published &  unprotected content (`main`, output 0, input 0)
- Set fields2 → Filter - Only published and unprotected content (`main`, output 0, input 0)
- Set fields3 → Loop Over Items (`main`, output 0, input 0)
- Set fields4 → Loop Over Items (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Loop Over Items → Markdown1 (`main`, output 0, input 0)
- Loop Over Items → Postgres - Filter on existing documents (`main`, output 1, input 0)
- Token Splitter1 → Default Data Loader1 (`ai_textSplitter`, output 0, input 0)
- Every 30 seconds → Postgres (`main`, output 0, input 0)
- HTML To Markdown → Supabase Vector Store (`main`, output 0, input 0)
- Embeddings OpenAI → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Supabase - Retrieve documents from chatinput (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Store documents on Supabase (`ai_embedding`, output 0, input 0)
- Aggregate documents → Set fields (`main`, output 0, input 0)
- Default Data Loader → Supabase Vector Store (`ai_document`, output 0, input 0)
- Default Data Loader1 → Store documents on Supabase (`ai_document`, output 0, input 0)
- Postgres Chat Memory → AI Agent (`ai_memory`, output 0, input 0)
- Supabase Vector Store → Aggregate (`main`, output 0, input 0)
- Wordpress - Get all pages → Merge Wordpress Posts and Pages (`main`, output 0, input 1)
- Wordpress - Get all posts → Merge Wordpress Posts and Pages (`main`, output 0, input 0)
- When chat message received → Supabase - Retrieve documents from chatinput (`main`, output 0, input 0)
- Store documents on Supabase → Aggregate1 (`main`, output 0, input 0)
- Merge Wordpress Posts and Pages → Set fields1 (`main`, output 0, input 0)
- Postgres - Create documents table → Postgres - Create workflow execution history table (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Wordpress - Get all posts (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Wordpress - Get all pages (`main`, output 0, input 0)
- Postgres - Filter on existing documents → Switch (`main`, output 0, input 0)
- Merge retrieved WordPress posts and pages → Set fields2 (`main`, output 0, input 0)
- Supabase - Delete row if documents exists → Aggregate2 (`main`, output 0, input 0)
- Supabase - Retrieve documents from chatinput → Aggregate documents (`main`, output 0, input 0)
- Filter - Only published &  unprotected content → HTML To Markdown (`main`, output 0, input 0)
- Filter - Only published and unprotected content → Loop Over Items (`main`, output 0, input 0)
- Wordpress - Get posts modified after last workflow execution → Merge retrieved WordPress posts and pages (`main`, output 0, input 0)
- Wordpress - Get posts modified after last workflow execution1 → Merge retrieved WordPress posts and pages (`main`, output 0, input 1)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1942_Postgres_Wordpress_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1942_Postgres_Wordpress_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
