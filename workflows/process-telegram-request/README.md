# Process Telegram Request

This folder contains the **Process Telegram Request** workflow. Its executable nodes use `agent`, `baserowTool`, `gmailTool`, `googleCalendarTool`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`process-telegram-request.json`](process-telegram-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `baserowApi`, `gmailOAuth2`, `googleCalendarOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Listen for incoming events

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Calendar | `googleCalendarTool` | getAll |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Get Email | `gmailTool` | getAll |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Listen for incoming events | `telegramTrigger` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| If | `if` | Inspect parameters |
| Speech to Text | `openAi` | audio / transcribe |
| Voice or Text | `set` | Inspect parameters |
| Get Voice File | `telegram` | file |
| Angie, AI Assistant 👩🏻‍🏫 | `agent` | Inspect parameters |
| Tasks | `baserowTool` | Inspect parameters |
| Contacts | `baserowTool` | Inspect parameters |

## Connection map

- If → Get Voice File (`main`, output 0, input 0)
- If → Angie, AI Assistant 👩🏻‍🏫 (`main`, output 1, input 0)
- Tasks → Angie, AI Assistant 👩🏻‍🏫 (`ai_tool`, output 0, input 0)
- Contacts → Angie, AI Assistant 👩🏻‍🏫 (`ai_tool`, output 0, input 0)
- Get Email → Angie, AI Assistant 👩🏻‍🏫 (`ai_tool`, output 0, input 0)
- Voice or Text → If (`main`, output 0, input 0)
- Get Voice File → Speech to Text (`main`, output 0, input 0)
- Speech to Text → Angie, AI Assistant 👩🏻‍🏫 (`main`, output 0, input 0)
- Google Calendar → Angie, AI Assistant 👩🏻‍🏫 (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Angie, AI Assistant 👩🏻‍🏫 (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Angie, AI Assistant 👩🏻‍🏫 (`ai_memory`, output 0, input 0)
- Listen for incoming events → Voice or Text (`main`, output 0, input 0)
- Angie, AI Assistant 👩🏻‍🏫 → Telegram (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0599_Telegram_Gmailtool_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0599_Telegram_Gmailtool_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
