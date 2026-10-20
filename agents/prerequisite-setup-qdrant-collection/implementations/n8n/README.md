# Prerequisite: Setup Qdrant Collection

This folder contains the **Prerequisite: Setup Qdrant Collection** workflow. Its executable nodes use `aggregate`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflowTrigger`, `filter`, `httpRequest`, `if`, `manualTrigger`, `mcpTrigger`, `set`, `splitOut`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `toolWorkflow`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`prerequisite-setup-qdrant-collection.json`](prerequisite-setup-qdrant-collection.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `qdrantApi`

**Entry nodes:** Qdrant MCP Server, When Executed by Another Workflow, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Insert | `toolWorkflow` | Inspect parameters |
| Search | `toolWorkflow` | Inspect parameters |
| Recommend | `toolWorkflow` | Inspect parameters |
| Qdrant MCP Server | `mcpTrigger` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| Compare | `toolWorkflow` | Inspect parameters |
| Recommend API | `httpRequest` | POST |
| Get Embeddings | `httpRequest` | POST |
| Preferences to Items | `code` | Inspect parameters |
| Aggregate Embeddings | `aggregate` | Inspect parameters |
| Get Embeddings1 | `httpRequest` | POST |
| Aggregate Embeddings1 | `aggregate` | Inspect parameters |
| Group Search API | `httpRequest` | POST |
| Has Results? | `if` | Inspect parameters |
| Simplify Group Results | `set` | Inspect parameters |
| Empty Compare Response | `set` | Inspect parameters |
| Aggregate Compare Response | `aggregate` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Simplify Recommend Response | `set` | Inspect parameters |
| Get Insert Response | `set` | Inspect parameters |
| Get Search Response | `aggregate` | Inspect parameters |
| Insert Reviews | `vectorStoreQdrant` | Inspect parameters |
| Search Reviews | `vectorStoreQdrant` | Inspect parameters |
| Split Out Companies | `splitOut` | Inspect parameters |
| Filter By CompanyId | `filter` | Inspect parameters |
| Aggregate Recommend Response | `aggregate` | Inspect parameters |
| Has Results?1 | `if` | Inspect parameters |
| Empty Compare Response1 | `set` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| ListCompanies | `toolWorkflow` | Inspect parameters |
| List by Facet API | `httpRequest` | POST |
| Create Facet Index | `httpRequest` | PUT |
| Create Collection | `httpRequest` | PUT |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |

## Connection map

- Insert → Qdrant MCP Server (`ai_tool`, output 0, input 0)
- Search → Qdrant MCP Server (`ai_tool`, output 0, input 0)
- Compare → Qdrant MCP Server (`ai_tool`, output 0, input 0)
- Operation → List by Facet API (`main`, output 0, input 0)
- Operation → Insert Reviews (`main`, output 1, input 0)
- Operation → Search Reviews (`main`, output 2, input 0)
- Operation → Get Embeddings1 (`main`, output 3, input 0)
- Operation → Preferences to Items (`main`, output 4, input 0)
- Recommend → Qdrant MCP Server (`ai_tool`, output 0, input 0)
- Has Results? → Aggregate Compare Response (`main`, output 0, input 0)
- Has Results? → Empty Compare Response (`main`, output 1, input 0)
- Has Results?1 → Aggregate Recommend Response (`main`, output 0, input 0)
- Has Results?1 → Empty Compare Response1 (`main`, output 1, input 0)
- ListCompanies → Qdrant MCP Server (`ai_tool`, output 0, input 0)
- Recommend API → Simplify Recommend Response (`main`, output 0, input 0)
- Get Embeddings → Aggregate Embeddings (`main`, output 0, input 0)
- Insert Reviews → Get Insert Response (`main`, output 0, input 0)
- Search Reviews → Get Search Response (`main`, output 0, input 0)
- Get Embeddings1 → Aggregate Embeddings1 (`main`, output 0, input 0)
- Group Search API → Split Out Companies (`main`, output 0, input 0)
- Create Collection → Create Facet Index (`main`, output 0, input 0)
- Embeddings OpenAI → Insert Reviews (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI1 → Search Reviews (`ai_embedding`, output 0, input 0)
- Default Data Loader → Insert Reviews (`ai_document`, output 0, input 0)
- Filter By CompanyId → Has Results? (`main`, output 0, input 0)
- Split Out Companies → Simplify Group Results (`main`, output 0, input 0)
- Aggregate Embeddings → Recommend API (`main`, output 0, input 0)
- Preferences to Items → Get Embeddings (`main`, output 0, input 0)
- Aggregate Embeddings1 → Group Search API (`main`, output 0, input 0)
- Simplify Group Results → Filter By CompanyId (`main`, output 0, input 0)
- Simplify Recommend Response → Has Results?1 (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When Executed by Another Workflow → Operation (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Create Collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0877_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0877_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
