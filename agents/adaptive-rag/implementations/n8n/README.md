# Adaptive RAG

This folder contains the **Adaptive RAG** workflow. Its executable nodes use `agent`, `chatTrigger`, `embeddingsGoogleGemini`, `executeWorkflowTrigger`, `lmChatGoogleGemini`, `memoryBufferWindow`, `respondToWebhook`, `set`, `summarize`, `switch`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`adaptive-rag.json`](adaptive-rag.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `qdrantApi`

**Entry nodes:** Chat, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Query Classification | `agent` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Factual Strategy - Focus on Precision | `agent` | Inspect parameters |
| Analytical Strategy - Comprehensive Coverage | `agent` | Inspect parameters |
| Opinion Strategy - Diverse Perspectives | `agent` | Inspect parameters |
| Contextual Strategy - User Context Integration | `agent` | Inspect parameters |
| Chat | `chatTrigger` | Inspect parameters |
| Factual Prompt and Output | `set` | Inspect parameters |
| Contextual Prompt and Output | `set` | Inspect parameters |
| Opinion Prompt and Output | `set` | Inspect parameters |
| Analytical Prompt and Output | `set` | Inspect parameters |
| Gemini Classification | `lmChatGoogleGemini` | Inspect parameters |
| Gemini Factual | `lmChatGoogleGemini` | Inspect parameters |
| Gemini Analytical | `lmChatGoogleGemini` | Inspect parameters |
| Chat Buffer Memory Analytical | `memoryBufferWindow` | Inspect parameters |
| Chat Buffer Memory Factual | `memoryBufferWindow` | Inspect parameters |
| Gemini Opinion | `lmChatGoogleGemini` | Inspect parameters |
| Chat Buffer Memory Opinion | `memoryBufferWindow` | Inspect parameters |
| Gemini Contextual | `lmChatGoogleGemini` | Inspect parameters |
| Chat Buffer Memory Contextual | `memoryBufferWindow` | Inspect parameters |
| Embeddings | `embeddingsGoogleGemini` | Inspect parameters |
| Concatenate Context | `summarize` | Inspect parameters |
| Retrieve Documents from Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Set Prompt and Output | `set` | Inspect parameters |
| Gemini Answer | `lmChatGoogleGemini` | Inspect parameters |
| Answer | `agent` | Inspect parameters |
| Chat Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Combined Fields | `set` | Inspect parameters |

## Connection map

- Chat → Combined Fields (`main`, output 0, input 0)
- Answer → Respond to Webhook (`main`, output 0, input 0)
- Switch → Factual Strategy - Focus on Precision (`main`, output 0, input 0)
- Switch → Analytical Strategy - Comprehensive Coverage (`main`, output 1, input 0)
- Switch → Opinion Strategy - Diverse Perspectives (`main`, output 2, input 0)
- Switch → Contextual Strategy - User Context Integration (`main`, output 3, input 0)
- Embeddings → Retrieve Documents from Vector Store (`ai_embedding`, output 0, input 0)
- Gemini Answer → Answer (`ai_languageModel`, output 0, input 0)
- Gemini Factual → Factual Strategy - Focus on Precision (`ai_languageModel`, output 0, input 0)
- Gemini Opinion → Opinion Strategy - Diverse Perspectives (`ai_languageModel`, output 0, input 0)
- Combined Fields → Query Classification (`main`, output 0, input 0)
- Gemini Analytical → Analytical Strategy - Comprehensive Coverage (`ai_languageModel`, output 0, input 0)
- Gemini Contextual → Contextual Strategy - User Context Integration (`ai_languageModel`, output 0, input 0)
- Chat Buffer Memory → Answer (`ai_memory`, output 0, input 0)
- Concatenate Context → Answer (`main`, output 0, input 0)
- Query Classification → Switch (`main`, output 0, input 0)
- Gemini Classification → Query Classification (`ai_languageModel`, output 0, input 0)
- Set Prompt and Output → Retrieve Documents from Vector Store (`main`, output 0, input 0)
- Factual Prompt and Output → Set Prompt and Output (`main`, output 0, input 0)
- Opinion Prompt and Output → Set Prompt and Output (`main`, output 0, input 0)
- Chat Buffer Memory Factual → Factual Strategy - Focus on Precision (`ai_memory`, output 0, input 0)
- Chat Buffer Memory Opinion → Opinion Strategy - Diverse Perspectives (`ai_memory`, output 0, input 0)
- Analytical Prompt and Output → Set Prompt and Output (`main`, output 0, input 0)
- Contextual Prompt and Output → Set Prompt and Output (`main`, output 0, input 0)
- Chat Buffer Memory Analytical → Analytical Strategy - Comprehensive Coverage (`ai_memory`, output 0, input 0)
- Chat Buffer Memory Contextual → Contextual Strategy - User Context Integration (`ai_memory`, output 0, input 0)
- When Executed by Another Workflow → Combined Fields (`main`, output 0, input 0)
- Retrieve Documents from Vector Store → Concatenate Context (`main`, output 0, input 0)
- Factual Strategy - Focus on Precision → Factual Prompt and Output (`main`, output 0, input 0)
- Opinion Strategy - Diverse Perspectives → Opinion Prompt and Output (`main`, output 0, input 0)
- Analytical Strategy - Comprehensive Coverage → Analytical Prompt and Output (`main`, output 0, input 0)
- Contextual Strategy - User Context Integration → Contextual Prompt and Output (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Summarize/1829_Summarize_Respondtowebhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Summarize/1829_Summarize_Respondtowebhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
