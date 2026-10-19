# Template for Kids' Story in Arabic

This folder contains the **Template for Kids' Story in Arabic** workflow. Its executable nodes use `chainSummarization`, `lmChatOpenAi`, `openAi`, `scheduleTrigger`, `telegram`, `textSplitterRecursiveCharacterTextSplitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`template-for-kids-story-in-arabic.json`](template-for-kids-story-in-arabic.json): sanitized, inactive import copy with an overview sticky note.
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
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Create a Prompt for DALL-E | `chainSummarization` | Inspect parameters |
| Generate an Image for the Story | `openAi` | image |
| Generate Audio for the Story | `openAi` | audio |
| Send the Story To Channel | `telegram` | Inspect parameters |
| Send Image to the Channel | `telegram` | sendPhoto |
| Translate the Story to Arabic | `chainSummarization` | Inspect parameters |
| Send Audio to the Channel | `telegram` | sendAudio |
| Create a Story for Kids | `chainSummarization` | Inspect parameters |

## Connection map

- Schedule Trigger → Create a Story for Kids (`main`, output 0, input 0)
- OpenAI Chat Model → Create a Story for Kids (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Translate the Story to Arabic (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Create a Prompt for DALL-E (`ai_languageModel`, output 0, input 0)
- Create a Story for Kids → Translate the Story to Arabic (`main`, output 0, input 0)
- Create a Story for Kids → Create a Prompt for DALL-E (`main`, output 0, input 0)
- Create a Prompt for DALL-E → Generate an Image for the Story (`main`, output 0, input 0)
- Generate Audio for the Story → Send Audio to the Channel (`main`, output 0, input 0)
- Translate the Story to Arabic → Send the Story To Channel (`main`, output 0, input 0)
- Translate the Story to Arabic → Generate Audio for the Story (`main`, output 0, input 0)
- Generate an Image for the Story → Send Image to the Channel (`main`, output 0, input 0)
- Recursive Character Text Splitter → Create a Story for Kids (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0487_Schedule_Telegram_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0487_Schedule_Telegram_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
