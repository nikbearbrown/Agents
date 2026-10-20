# Telegram AI Langchain bot

This folder contains the **Telegram AI Langchain bot** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-ai-langchain-bot.json`](telegram-ai-langchain-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Execute Workflow Trigger, Listen for incoming events

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Correct errors | `telegram` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Listen for incoming events | `telegramTrigger` | Inspect parameters |
| Send back an image | `telegram` | sendPhoto |
| add response field | `set` | Inspect parameters |
| Dall-E 3 Tool | `toolWorkflow` | Inspect parameters |
| Generate image in Dall-E 3 | `httpRequest` | POST |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- AI Agent → Telegram (`main`, output 0, input 0)
- Telegram → Correct errors (`main`, output 1, input 0)
- Dall-E 3 Tool → AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Send back an image → add response field (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Execute Workflow Trigger → Generate image in Dall-E 3 (`main`, output 0, input 0)
- Generate image in Dall-E 3 → Send back an image (`main`, output 0, input 0)
- Listen for incoming events → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1687_HTTP_Telegram_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1687_HTTP_Telegram_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
