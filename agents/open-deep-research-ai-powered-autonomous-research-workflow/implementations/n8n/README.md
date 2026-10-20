# Open Deep Research - AI-Powered Autonomous Research Workflow

This folder contains the **Open Deep Research - AI-Powered Autonomous Research Workflow** workflow. Its executable nodes use `agent`, `chainLlm`, `chatTrigger`, `code`, `httpRequest`, `lmChatOpenRouter`, `memoryBufferWindow`, `splitInBatches`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`open-deep-research-ai-powered-autonomous-research-workflow.json`](open-deep-research-ai-powered-autonomous-research-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openRouterApi`

**Entry nodes:** Chat Message Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Chat Message Trigger | `chatTrigger` | Inspect parameters |
| Generate Search Queries using LLM | `chainLlm` | Inspect parameters |
| LLM Response Provider (OpenRouter) | `lmChatOpenRouter` | Inspect parameters |
| Parse and Chunk JSON Data | `code` | Inspect parameters |
| Perform SerpAPI Search Request | `httpRequest` | Inspect parameters |
| Perform Jina AI Analysis Request | `httpRequest` | Inspect parameters |
| Format SerpAPI Organic Results | `code` | Inspect parameters |
| Extract Relevant Context via LLM | `agent` | Inspect parameters |
| Generate Comprehensive Research Report | `agent` | Inspect parameters |
| Split Data for SerpAPI Batching | `splitInBatches` | Inspect parameters |
| Split Data for Jina AI Batching | `splitInBatches` | Inspect parameters |
| LLM Memory Buffer (Input Context) | `memoryBufferWindow` | Inspect parameters |
| LLM Memory Buffer (Report Context) | `memoryBufferWindow` | Inspect parameters |
| Fetch Wikipedia Information | `toolWikipedia` | Inspect parameters |

## Connection map

- Chat Message Trigger → Generate Search Queries using LLM (`main`, output 0, input 0)
- Parse and Chunk JSON Data → Split Data for SerpAPI Batching (`main`, output 0, input 0)
- Fetch Wikipedia Information → Generate Comprehensive Research Report (`ai_tool`, output 0, input 0)
- Format SerpAPI Organic Results → Split Data for Jina AI Batching (`main`, output 0, input 0)
- Perform SerpAPI Search Request → Split Data for SerpAPI Batching (`main`, output 0, input 0)
- Split Data for Jina AI Batching → Extract Relevant Context via LLM (`main`, output 0, input 0)
- Split Data for Jina AI Batching → Perform Jina AI Analysis Request (`main`, output 1, input 0)
- Split Data for SerpAPI Batching → Format SerpAPI Organic Results (`main`, output 0, input 0)
- Split Data for SerpAPI Batching → Perform SerpAPI Search Request (`main`, output 1, input 0)
- Extract Relevant Context via LLM → Generate Comprehensive Research Report (`main`, output 0, input 0)
- Perform Jina AI Analysis Request → Split Data for Jina AI Batching (`main`, output 0, input 0)
- Generate Search Queries using LLM → Parse and Chunk JSON Data (`main`, output 0, input 0)
- LLM Memory Buffer (Input Context) → Extract Relevant Context via LLM (`ai_memory`, output 0, input 0)
- LLM Memory Buffer (Report Context) → Generate Comprehensive Research Report (`ai_memory`, output 0, input 0)
- LLM Response Provider (OpenRouter) → Generate Search Queries using LLM (`ai_languageModel`, output 0, input 0)
- LLM Response Provider (OpenRouter) → Extract Relevant Context via LLM (`ai_languageModel`, output 0, input 0)
- LLM Response Provider (OpenRouter) → Generate Comprehensive Research Report (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1747_HTTP_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1747_HTTP_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
