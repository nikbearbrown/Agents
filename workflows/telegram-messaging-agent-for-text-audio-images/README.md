# 🤖 Telegram Messaging Agent for Text/Audio/Images

This folder contains the **🤖 Telegram Messaging Agent for Text/Audio/Images** workflow. Its executable nodes use `convertToFile`, `extractFromFile`, `httpRequest`, `if`, `lmChatOpenAi`, `openAi`, `set`, `switch`, `telegram`, `textClassifier`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-messaging-agent-for-text-audio-images.json`](telegram-messaging-agent-for-text-audio-images.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Listen for Telegram Events

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check User & Chat ID | `if` | Inspect parameters |
| Error message | `telegram` | Inspect parameters |
| Listen for Telegram Events | `webhook` | Inspect parameters |
| Set Webhook Test URL | `httpRequest` | Inspect parameters |
| Get Telegram Webhook Info | `httpRequest` | Inspect parameters |
| Image Schema | `set` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Get Audio File | `telegram` | file |
| Get Image | `telegram` | file |
| Analyze Image | `openAi` | image / analyze |
| Transcribe Recording | `openAi` | audio / transcribe |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| Test Webhook Status | `telegram` | Inspect parameters |
| Production Webhook Status | `telegram` | Inspect parameters |
| Set Webhook Production URL | `httpRequest` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Audio Task Message | `telegram` | Inspect parameters |
| Audio Other Message | `telegram` | Inspect parameters |
| Text Task Message | `telegram` | Inspect parameters |
| Text Other Message | `telegram` | Inspect parameters |
| Image Message | `telegram` | Inspect parameters |
| Convert to Image File | `convertToFile` | toBinary |
| Extract from File to Base64 | `extractFromFile` | binaryToPropery |
| Text Classifier Audio | `textClassifier` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| Telegram Token & Webhooks | `set` | Inspect parameters |
| Get Webhook Status | `telegram` | Inspect parameters |
| Validation | `set` | Inspect parameters |
| Message Router | `switch` | Inspect parameters |

## Connection map

- Get Image → Extract from File to Base64 (`main`, output 0, input 0)
- Validation → Check User & Chat ID (`main`, output 0, input 0)
- Edit Fields → Text Classifier (`main`, output 0, input 0)
- gpt-4o-mini → Text Classifier Audio (`ai_languageModel`, output 0, input 0)
- Image Schema → Get Image (`main`, output 0, input 0)
- gpt-4o-mini1 → Text Classifier (`ai_languageModel`, output 0, input 0)
- Analyze Image → Image Message (`main`, output 0, input 0)
- Get Audio File → Transcribe Recording (`main`, output 0, input 0)
- Message Router → Get Audio File (`main`, output 0, input 0)
- Message Router → Edit Fields (`main`, output 1, input 0)
- Message Router → Image Schema (`main`, output 2, input 0)
- Message Router → Error message (`main`, output 3, input 0)
- Text Classifier → Text Task Message (`main`, output 0, input 0)
- Text Classifier → Text Other Message (`main`, output 1, input 0)
- Check User & Chat ID → Message Router (`main`, output 0, input 0)
- Check User & Chat ID → Error message (`main`, output 1, input 0)
- Set Webhook Test URL → Test Webhook Status (`main`, output 0, input 0)
- Transcribe Recording → Text Classifier Audio (`main`, output 0, input 0)
- Convert to Image File → Analyze Image (`main`, output 0, input 0)
- Text Classifier Audio → Audio Task Message (`main`, output 0, input 0)
- Text Classifier Audio → Audio Other Message (`main`, output 1, input 0)
- Get Telegram Webhook Info → Get Webhook Status (`main`, output 0, input 0)
- Telegram Token & Webhooks → Set Webhook Production URL (`main`, output 0, input 0)
- Telegram Token & Webhooks → Set Webhook Test URL (`main`, output 0, input 0)
- Telegram Token & Webhooks → Get Telegram Webhook Info (`main`, output 0, input 0)
- Listen for Telegram Events → Validation (`main`, output 0, input 0)
- Set Webhook Production URL → Production Webhook Status (`main`, output 0, input 0)
- Extract from File to Base64 → Convert to Image File (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2051_Telegram_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2051_Telegram_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
