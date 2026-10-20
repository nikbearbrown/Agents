# Setting Up a Workflow for "AI-Powered Children's English Storytelling on Telegram"

This folder contains the **Setting Up a Workflow for "AI-Powered Children's English Storytelling on Telegram"** workflow. Its executable nodes use `chainSummarization`, `lmChatOpenAi`, `openAi`, `scheduleTrigger`, `set`, `telegram`, `textSplitterRecursiveCharacterTextSplitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`setting-up-a-workflow-for-ai-powered-children-s-english-storytelling-on-telegram.json`](setting-up-a-workflow-for-ai-powered-children-s-english-storytelling-on-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Create a Prompt for DALL-E | `chainSummarization` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Create a story | `chainSummarization` | Inspect parameters |
| Generate Audio for the story | `openAi` | audio |
| Generate a Picture for the story | `openAi` | image |
| Send Story Text | `telegram` | Inspect parameters |
| Send Audio for the story | `telegram` | sendAudio |
| Send Story Picture | `telegram` | sendPhoto |
| Config | `set` | Inspect parameters |

## Connection map

- Config → Create a story (`main`, output 0, input 0)
- Create a story → Generate Audio for the story (`main`, output 0, input 0)
- Create a story → Create a Prompt for DALL-E (`main`, output 0, input 0)
- Create a story → Send Story Text (`main`, output 0, input 0)
- Schedule Trigger → Config (`main`, output 0, input 0)
- OpenAI Chat Model → Create a story (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Create a Prompt for DALL-E (`ai_languageModel`, output 0, input 0)
- Create a Prompt for DALL-E → Generate a Picture for the story (`main`, output 0, input 0)
- Generate Audio for the story → Send Audio for the story (`main`, output 0, input 0)
- Generate a Picture for the story → Send Story Picture (`main`, output 0, input 0)
- Recursive Character Text Splitter → Create a story (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0486_Schedule_Telegram_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0486_Schedule_Telegram_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
