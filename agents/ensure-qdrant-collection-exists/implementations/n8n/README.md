# 🚨Ensure Qdrant collection exists!

This folder contains the **🚨Ensure Qdrant collection exists!** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsMistralCloud`, `executeWorkflowTrigger`, `html`, `httpRequest`, `lmChatMistralCloud`, `manualTrigger`, `merge`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `toolWorkflow`, `vectorStoreQdrant`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ensure-qdrant-collection-exists.json`](ensure-qdrant-collection-exists.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mistralCloudApi`, `qdrantApi`

**Entry nodes:** When clicking "Test workflow", Chat Trigger, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Get This Week's Menu | `httpRequest` | Inspect parameters |
| Extract Available Courses | `code` | Inspect parameters |
| Extract Server Data | `html` | extractHtmlContent |
| Get Course Metadata | `set` | Inspect parameters |
| Get Recipe | `httpRequest` | Inspect parameters |
| Embeddings Mistral Cloud | `embeddingsMistralCloud` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Merge Course & Recipe | `merge` | Inspect parameters |
| Prepare Documents | `set` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Extract Recipe Details | `html` | extractHtmlContent |
| Qdrant Recommend API | `toolWorkflow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Mistral Cloud Chat Model | `lmChatMistralCloud` | Inspect parameters |
| Get Tool Response | `set` | Inspect parameters |
| Wait for Rate Limits | `wait` | Inspect parameters |
| Get Mistral Embeddings | `httpRequest` | POST |
| Use Qdrant Recommend API | `httpRequest` | POST |
| Get Recipes From DB | `code` | Inspect parameters |
| Save Recipes to DB | `code` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |

## Connection map

- Get Recipe → Extract Recipe Details (`main`, output 0, input 0)
- Chat Trigger → AI Agent (`main`, output 0, input 0)
- Prepare Documents → Qdrant Vector Store (`main`, output 0, input 0)
- Prepare Documents → Save Recipes to DB (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Extract Server Data → Extract Available Courses (`main`, output 0, input 0)
- Get Course Metadata → Merge Course & Recipe (`main`, output 0, input 0)
- Get Recipes From DB → Get Tool Response (`main`, output 0, input 0)
- Get This Week's Menu → Extract Server Data (`main`, output 0, input 0)
- Qdrant Recommend API → AI Agent (`ai_tool`, output 0, input 0)
- Wait for Rate Limits → Get Mistral Embeddings (`main`, output 0, input 0)
- Merge Course & Recipe → Prepare Documents (`main`, output 0, input 0)
- Extract Recipe Details → Merge Course & Recipe (`main`, output 0, input 1)
- Get Mistral Embeddings → Use Qdrant Recommend API (`main`, output 0, input 0)
- Embeddings Mistral Cloud → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Execute Workflow Trigger → Wait for Rate Limits (`main`, output 0, input 0)
- Mistral Cloud Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Use Qdrant Recommend API → Get Recipes From DB (`main`, output 0, input 0)
- Extract Available Courses → Get Course Metadata (`main`, output 0, input 0)
- Extract Available Courses → Get Recipe (`main`, output 0, input 0)
- When clicking "Test workflow" → Get This Week's Menu (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0533_Wait_Code_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0533_Wait_Code_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
