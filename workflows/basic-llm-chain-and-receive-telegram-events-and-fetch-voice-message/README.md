# basic llm chain and receive telegram events and fetch voice message

This folder contains the **basic llm chain and receive telegram events and fetch voice message** workflow. Its executable nodes use `chainLlm`, `lmChatOpenAi`, `openAi`, `outputParserStructured`, `set`, `switch`, `telegram`, `telegramTrigger`, `todoist`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`basic-llm-chain-and-receive-telegram-events-and-fetch-voice-message.json`](basic-llm-chain-and-receive-telegram-events-and-fetch-voice-message.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`, `todoistApi`

**Entry nodes:** Receive Telegram Messages

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Receive Telegram Messages | `telegramTrigger` | Inspect parameters |
| Voice or Text? | `switch` | Inspect parameters |
| Fetch Voice Message | `telegram` | file |
| Transcribe Voice to Text | `openAi` | audio / translate |
| Prepare for LLM | `set` | Inspect parameters |
| Extract Tasks | `outputParserStructured` | Inspect parameters |
| Create Todoist Tasks | `todoist` | Inspect parameters |
| Send Confirmation | `telegram` | Inspect parameters |

## Connection map

- Extract Tasks → Basic LLM Chain (`ai_outputParser`, output 0, input 0)
- Voice or Text? → Fetch Voice Message (`main`, output 0, input 0)
- Voice or Text? → Prepare for LLM (`main`, output 1, input 0)
- Basic LLM Chain → Create Todoist Tasks (`main`, output 0, input 0)
- Prepare for LLM → Basic LLM Chain (`main`, output 0, input 0)
- OpenAI Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Fetch Voice Message → Transcribe Voice to Text (`main`, output 0, input 0)
- Create Todoist Tasks → Send Confirmation (`main`, output 0, input 0)
- Transcribe Voice to Text → Basic LLM Chain (`main`, output 0, input 0)
- Receive Telegram Messages → Voice or Text? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0768_Telegram_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0768_Telegram_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
