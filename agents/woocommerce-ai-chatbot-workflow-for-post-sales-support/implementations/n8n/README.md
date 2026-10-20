# WooCommerce AI Chatbot Workflow for Post-Sales Support

This folder contains the **WooCommerce AI Chatbot Workflow for Post-Sales Support** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflowTrigger`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `set`, `telegramTool`, `textSplitterTokenSplitter`, `toolCalculator`, `toolVectorStore`, `toolWorkflow`, `vectorStoreQdrant`, `wooCommerceTool`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`woocommerce-ai-chatbot-workflow-for-post-sales-support.json`](woocommerce-ai-chatbot-workflow-for-post-sales-support.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpBasicAuth`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`, `telegramApi`, `wooCommerceApi`

**Entry nodes:** When chat message received, When clicking ‘Test workflow’, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| get_order | `wooCommerceTool` | order / get |
| get_orders | `wooCommerceTool` | order / getAll |
| get_user | `wooCommerceTool` | customer / getAll |
| Calculator | `toolCalculator` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Create collection | `httpRequest` | POST |
| Refresh collection | `httpRequest` | POST |
| Get folder | `googleDrive` | fileFolder |
| Download Files | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| ToS | `toolVectorStore` | Inspect parameters |
| get_tracking | `toolWorkflow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Post-Sales Agent | `agent` | Inspect parameters |
| human_assistence | `telegramTool` | Inspect parameters |
| Get tracking | `httpRequest` | Inspect parameters |
| Set tracking code | `set` | Inspect parameters |
| GPT 4o-mini | `lmChatOpenAi` | Inspect parameters |

## Connection map

- ToS → Post-Sales Agent (`ai_tool`, output 0, input 0)
- get_user → Post-Sales Agent (`ai_tool`, output 0, input 0)
- get_order → Post-Sales Agent (`ai_tool`, output 0, input 0)
- Calculator → Post-Sales Agent (`ai_tool`, output 0, input 0)
- Get folder → Download Files (`main`, output 0, input 0)
- get_orders → Post-Sales Agent (`ai_tool`, output 0, input 0)
- GPT 4o-mini → Post-Sales Agent (`ai_languageModel`, output 0, input 0)
- Get tracking → Set tracking code (`main`, output 0, input 0)
- get_tracking → Post-Sales Agent (`ai_tool`, output 0, input 0)
- Simple Memory → Post-Sales Agent (`ai_memory`, output 0, input 0)
- Download Files → Qdrant Vector Store1 (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- human_assistence → Post-Sales Agent (`ai_tool`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → ToS (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Refresh collection → Get folder (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store1 (`ai_document`, output 0, input 0)
- Qdrant Vector Store → ToS (`ai_vectorStore`, output 0, input 0)
- When chat message received → Post-Sales Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Get tracking (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Create collection (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegramtool/1575_Telegramtool_Woocommercetool_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegramtool/1575_Telegramtool_Woocommercetool_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
