# 🌐🪛 AI Agent Chatbot with Jina.ai Webpage Scraper

This folder contains the **🌐🪛 AI Agent Chatbot with Jina.ai Webpage Scraper** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-agent-chatbot-with-jina-ai-webpage-scraper.json`](ai-agent-chatbot-with-jina-ai-webpage-scraper.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Jina.ai Web Scraping Agent | `agent` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Jina.ai Web Scraper Tool | `toolHttpRequest` | Inspect parameters |

## Connection map

- gpt-4o-mini → Jina.ai Web Scraping Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Jina.ai Web Scraping Agent (`ai_memory`, output 0, input 0)
- Jina.ai Web Scraper Tool → Jina.ai Web Scraping Agent (`ai_tool`, output 0, input 0)
- When chat message received → Jina.ai Web Scraping Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2009_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2009_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
