# Telegram AI-bot

This folder contains the **Telegram AI-bot** workflow. Its executable nodes use `merge`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-ai-bot.json`](telegram-ai-bot.json): sanitized, inactive import copy with an overview sticky note.
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
| CheckCommand | `switch` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Chat_mode | `openAi` | chat |
| Greeting | `openAi` | chat |
| Text reply | `telegram` | Inspect parameters |
| Send Typing action | `telegram` | sendChatAction |
| Merge | `merge` | Inspect parameters |
| Create an image | `openAi` | image |
| Send error message | `telegram` | Inspect parameters |
| Send image | `telegram` | sendPhoto |
| PreProcessing | `set` | Inspect parameters |

## Connection map

- Merge → CheckCommand (`main`, output 0, input 0)
- Greeting → Text reply (`main`, output 0, input 0)
- Settings → Send Typing action (`main`, output 0, input 0)
- Settings → Merge (`main`, output 0, input 0)
- Chat_mode → Text reply (`main`, output 0, input 0)
- CheckCommand → Chat_mode (`main`, output 0, input 0)
- CheckCommand → Greeting (`main`, output 1, input 0)
- CheckCommand → Create an image (`main`, output 2, input 0)
- CheckCommand → Send error message (`main`, output 3, input 0)
- PreProcessing → Settings (`main`, output 0, input 0)
- Create an image → Send image (`main`, output 0, input 0)
- Telegram Trigger → PreProcessing (`main`, output 0, input 0)
- Send Typing action → Merge (`main`, output 0, input 1)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/1685_Openai_Telegram_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/1685_Openai_Telegram_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
