# Translate Telegram audio messages with AI (55 supported languages) v1

This folder contains the **Translate Telegram audio messages with AI (55 supported languages) v1** workflow. Its executable nodes use `chainLlm`, `lmChatOpenAi`, `openAi`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`translate-telegram-audio-messages-with-ai-55-supported-languages-v1.json`](translate-telegram-audio-messages-with-ai-55-supported-languages-v1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Text reply | `telegram` | Inspect parameters |
| Telegram1 | `telegram` | file |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Input Error Handling | `set` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Auto-detect and translate | `chainLlm` | Inspect parameters |
| Audio reply | `telegram` | sendAudio |
| OpenAI2 | `openAi` | audio / transcribe |
| OpenAI | `openAi` | audio |

## Connection map

- OpenAI → Audio reply (`main`, output 0, input 0)
- OpenAI2 → Auto-detect and translate (`main`, output 0, input 0)
- Settings → Input Error Handling (`main`, output 0, input 0)
- Telegram1 → OpenAI2 (`main`, output 0, input 0)
- Telegram Trigger → Settings (`main`, output 0, input 0)
- OpenAI Chat Model → Auto-detect and translate (`ai_languageModel`, output 0, input 0)
- Input Error Handling → Telegram1 (`main`, output 0, input 0)
- Auto-detect and translate → Text reply (`main`, output 0, input 0)
- Auto-detect and translate → OpenAI (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1701_Telegram_Stickynote_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1701_Telegram_Stickynote_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
