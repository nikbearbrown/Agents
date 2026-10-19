# Parents smart bot

This folder contains the **Parents smart bot** workflow. Its executable nodes use `agent`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `toolCalculator`, `toolHttpRequest`, `toolWikipedia`, `toolWorkflow`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`parents-smart-bot.json`](parents-smart-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `qdrantApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Ultimate Assistant | `agent` | Inspect parameters |
| Email Agent | `toolWorkflow` | Inspect parameters |
| Contact Agent | `toolWorkflow` | Inspect parameters |
| Content Creator Agent | `toolWorkflow` | Inspect parameters |
| Tavily | `toolHttpRequest` | POST |
| Calendar Agent | `toolWorkflow` | Inspect parameters |
| Download File | `telegram` | file |
| Transcribe | `openAi` | audio / transcribe |
| Calculator1 | `toolCalculator` | Inspect parameters |
| Set 'Text'1 | `set` | Inspect parameters |
| Switch1 | `switch` | Inspect parameters |
| Response1 | `telegram` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Download File1 | `telegram` | file |
| Code | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |

## Connection map

- Email Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Contact Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Content Creator Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Tavily → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Calendar Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Ultimate Assistant → Response1 (`main`, output 0, input 0)
- Download File → Transcribe (`main`, output 0, input 0)
- Transcribe → Ultimate Assistant (`main`, output 0, input 0)
- Calculator1 → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Set 'Text'1 → If (`main`, output 0, input 0)
- Switch1 → Download File (`main`, output 0, input 0)
- Switch1 → Set 'Text'1 (`main`, output 1, input 0)
- Switch1 → Download File1 (`main`, output 2, input 0)
- Wikipedia → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- OpenAI Chat Model → Ultimate Assistant (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Qdrant Vector Store1 → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Window Buffer Memory → Ultimate Assistant (`ai_memory`, output 0, input 0)
- Qdrant Vector Store → Edit Fields1 (`main`, output 0, input 0)
- Telegram Trigger → Switch1 (`main`, output 0, input 0)
- Download File1 → Code (`main`, output 0, input 0)
- Code → Qdrant Vector Store (`main`, output 0, input 0)
- Code → Ultimate Assistant (`main`, output 1, input 0)
- If → Edit Fields (`main`, output 0, input 0)
- If → Ultimate Assistant (`main`, output 1, input 0)
- Edit Fields → Qdrant Vector Store (`main`, output 0, input 0)
- Edit Fields1 → Ultimate Assistant (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1596_Telegram_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1596_Telegram_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
