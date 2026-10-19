# telegram and transcribe audio open ai and receive gmail events

This folder contains the **telegram and transcribe audio open ai and receive gmail events** workflow. Its executable nodes use `chainLlm`, `gmail`, `gmailTrigger`, `if`, `lmChatOpenAi`, `openAi`, `outputParserStructured`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-and-transcribe-audio-open-ai-and-receive-gmail-events.json`](telegram-and-transcribe-audio-open-ai-and-receive-gmail-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`, `telegramApi`

**Entry nodes:** New Email Received, Telegram Bot Message Received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Text Email | `telegram` | Inspect parameters |
| OpenAI | `openAi` | audio / transcribe |
| New Email Received | `gmailTrigger` | Inspect parameters |
| In the Inbox? | `if` | Inspect parameters |
| Needs a response? | `if` | Inspect parameters |
| Telegram Bot Message Received | `telegramTrigger` | Inspect parameters |
| It needs to be an audio message + a reply! | `telegram` | Inspect parameters |
| Get Audio File | `telegram` | file |
| Create Email Draft | `gmail` | draft |
| Direct to Draft | `telegram` | Inspect parameters |
| Does Email Need a Response? | `chainLlm` | Inspect parameters |
| Is Type Audio Message + Reply? | `if` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Write Polished Reply | `chainLlm` | Inspect parameters |
| Set Chat ID | `set` | Inspect parameters |

## Connection map

- OpenAI → Write Polished Reply (`main`, output 0, input 0)
- Set Chat ID → Text Email (`main`, output 0, input 0)
- In the Inbox? → Does Email Need a Response? (`main`, output 0, input 0)
- Get Audio File → OpenAI (`main`, output 0, input 0)
- Needs a response? → Set Chat ID (`main`, output 0, input 0)
- OpenAI Chat Model → Does Email Need a Response? (`ai_languageModel`, output 0, input 0)
- Create Email Draft → Direct to Draft (`main`, output 0, input 0)
- New Email Received → In the Inbox? (`main`, output 0, input 0)
- OpenAI Chat Model1 → Write Polished Reply (`ai_languageModel`, output 0, input 0)
- Write Polished Reply → Create Email Draft (`main`, output 0, input 0)
- Structured Output Parser → Does Email Need a Response? (`ai_outputParser`, output 0, input 0)
- Does Email Need a Response? → Needs a response? (`main`, output 0, input 0)
- Telegram Bot Message Received → Is Type Audio Message + Reply? (`main`, output 0, input 0)
- Is Type Audio Message + Reply? → Get Audio File (`main`, output 0, input 0)
- Is Type Audio Message + Reply? → It needs to be an audio message + a reply! (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0916_Telegram_Gmail_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0916_Telegram_Gmail_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
