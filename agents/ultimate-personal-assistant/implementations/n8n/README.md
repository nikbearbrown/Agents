# Ultimate Personal Assistant

This folder contains the **Ultimate Personal Assistant** workflow. Its executable nodes use `agent`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`, `toolCalculator`, `toolHttpRequest`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ultimate-personal-assistant.json`](ultimate-personal-assistant.json): sanitized, inactive import copy with an overview sticky note.
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
| Ultimate Assistant | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Email Agent | `toolWorkflow` | Inspect parameters |
| Contact Agent | `toolWorkflow` | Inspect parameters |
| Content Creator Agent | `toolWorkflow` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Tavily | `toolHttpRequest` | POST |
| Calculator | `toolCalculator` | Inspect parameters |
| Calendar Agent | `toolWorkflow` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Set 'Text' | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Response | `telegram` | Inspect parameters |
| Download File | `telegram` | file |
| Transcribe | `openAi` | audio / transcribe |

## Connection map

- OpenAI Chat Model → Ultimate Assistant (`ai_languageModel`, output 0, input 0)
- Email Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Contact Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Content Creator Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Window Buffer Memory → Ultimate Assistant (`ai_memory`, output 0, input 0)
- Tavily → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Calculator → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Calendar Agent → Ultimate Assistant (`ai_tool`, output 0, input 0)
- Telegram Trigger → Switch (`main`, output 0, input 0)
- Switch → Download File (`main`, output 0, input 0)
- Switch → Set 'Text' (`main`, output 1, input 0)
- Set 'Text' → Ultimate Assistant (`main`, output 0, input 0)
- Ultimate Assistant → Response (`main`, output 0, input 0)
- Download File → Transcribe (`main`, output 0, input 0)
- Transcribe → Ultimate Assistant (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1712_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1712_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
