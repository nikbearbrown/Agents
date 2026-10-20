# All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem

This folder contains the **All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem** workflow. Its executable nodes use `agent`, `aggregate`, `baserow`, `baserowTool`, `convertToFile`, `extractFromFile`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `memoryPostgresChat`, `merge`, `openAi`, `set`, `splitOut`, `switch`, `telegram`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`all-in-one-telegram-baserow-ai-assistant-voice-photo-save-notes-long-term-mem.json`](all-in-one-telegram-baserow-ai-assistant-voice-photo-save-notes-long-term-mem.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `baserowApi`, `openAiApi`, `postgres`, `telegramApi`

**Entry nodes:** Listen for Telegram Events

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Chat Response | `set` | Inspect parameters |
| Telegram Response | `telegram` | Inspect parameters |
| AI Tools Agent | `agent` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Get Audio File | `telegram` | file |
| Analyze Image | `openAi` | image / analyze |
| Transcribe Recording | `openAi` | audio / transcribe |
| Edit Fields | `set` | Inspect parameters |
| Convert to Image File | `convertToFile` | toBinary |
| Extract from File to Base64 | `extractFromFile` | binaryToPropery |
| Message Router | `switch` | Inspect parameters |
| Image Schema1 | `set` | Inspect parameters |
| caption | `splitOut` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Get Image | `telegram` | file |
| Edit Fields1 | `set` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Save Note Tool | `baserowTool` | create |
| Save Memory | `baserowTool` | create |
| Listen for Telegram Events | `webhook` | Inspect parameters |
| Validation | `set` | Inspect parameters |
| Check User & Chat ID | `if` | Inspect parameters |
| Error message | `telegram` | Inspect parameters |
| Baserow Retrieve Memories | `baserow` | Inspect parameters |
| Baserow Retrieve Notes | `baserow` | Inspect parameters |
| Window Memory (Easy Mode) | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Merge → Aggregate (`main`, output 0, input 0)
- Merge1 → Edit Fields1 (`main`, output 0, input 0)
- caption → Merge1 (`main`, output 0, input 0)
- Aggregate → AI Tools Agent (`main`, output 0, input 0)
- Get Image → Extract from File to Base64 (`main`, output 0, input 0)
- Validation → Check User & Chat ID (`main`, output 0, input 0)
- Edit Fields → Baserow Retrieve Memories (`main`, output 0, input 0)
- Edit Fields → Baserow Retrieve Notes (`main`, output 0, input 0)
- Save Memory → AI Tools Agent (`ai_tool`, output 0, input 0)
- gpt-4o-mini → AI Tools Agent (`ai_languageModel`, output 0, input 0)
- Edit Fields1 → Baserow Retrieve Memories (`main`, output 0, input 0)
- Edit Fields1 → Baserow Retrieve Notes (`main`, output 0, input 0)
- Analyze Image → Merge1 (`main`, output 0, input 1)
- Image Schema1 → Get Image (`main`, output 0, input 0)
- Image Schema1 → caption (`main`, output 0, input 0)
- AI Tools Agent → Telegram Response (`main`, output 0, input 0)
- AI Tools Agent → Chat Response (`main`, output 0, input 0)
- Get Audio File → Transcribe Recording (`main`, output 0, input 0)
- Message Router → Get Audio File (`main`, output 0, input 0)
- Message Router → Edit Fields (`main`, output 1, input 0)
- Message Router → Image Schema1 (`main`, output 2, input 0)
- Message Router → Error message (`main`, output 3, input 0)
- Save Note Tool → AI Tools Agent (`ai_tool`, output 0, input 0)
- Check User & Chat ID → Message Router (`main`, output 0, input 0)
- Check User & Chat ID → Error message (`main`, output 1, input 0)
- Postgres Chat Memory → AI Tools Agent (`ai_memory`, output 0, input 0)
- Transcribe Recording → Baserow Retrieve Memories (`main`, output 0, input 0)
- Transcribe Recording → Baserow Retrieve Notes (`main`, output 0, input 0)
- Convert to Image File → Analyze Image (`main`, output 0, input 0)
- Baserow Retrieve Notes → Merge (`main`, output 0, input 1)
- Baserow Retrieve Memories → Merge (`main`, output 0, input 0)
- Listen for Telegram Events → Validation (`main`, output 0, input 0)
- Extract from File to Base64 → Convert to Image File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1305_Telegram_Splitout_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1305_Telegram_Splitout_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
