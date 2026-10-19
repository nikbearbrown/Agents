# Main Function to Receive and Send Telegram Messages

This folder contains the **Main Function to Receive and Send Telegram Messages** workflow. Its executable nodes use `agent`, `googleTasksTool`, `lmChatOpenAi`, `mcpClientTool`, `mcpTrigger`, `memoryBufferWindow`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`main-function-to-receive-and-send-telegram-messages.json`](main-function-to-receive-and-send-telegram-messages.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleTasksOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Incoming Message, MCP Server Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Incoming Message | `telegramTrigger` | Inspect parameters |
| MCP Server Trigger | `mcpTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| MCP Client | `mcpClientTool` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| chatInput | `set` | Inspect parameters |
| create_todays_task | `googleTasksTool` | Inspect parameters |
| chatOutput | `set` | Inspect parameters |
| sendMessage | `telegram` | Inspect parameters |
| create_upcoming_task | `googleTasksTool` | Inspect parameters |
| complete_task | `googleTasksTool` | update |
| get_todays_tasks | `googleTasksTool` | getAll |
| get_upcoming_tasks | `googleTasksTool` | getAll |
| Switch | `switch` | Inspect parameters |
| audio_id | `set` | Inspect parameters |
| download_audio | `telegram` | file |
| transcribeAudio | `openAi` | audio / transcribe |
| audioInput | `set` | Inspect parameters |

## Connection map

- Switch → audio_id (`main`, output 0, input 0)
- Switch → chatInput (`main`, output 1, input 0)
- AI Agent → chatOutput (`main`, output 0, input 0)
- audio_id → download_audio (`main`, output 0, input 0)
- chatInput → AI Agent (`main`, output 0, input 0)
- MCP Client → AI Agent (`ai_tool`, output 0, input 0)
- audioInput → AI Agent (`main`, output 0, input 0)
- chatOutput → sendMessage (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- complete_task → MCP Server Trigger (`ai_tool`, output 0, input 0)
- download_audio → transcribeAudio (`main`, output 0, input 0)
- transcribeAudio → audioInput (`main`, output 0, input 0)
- Incoming Message → Switch (`main`, output 0, input 0)
- get_todays_tasks → MCP Server Trigger (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- create_todays_task → MCP Server Trigger (`ai_tool`, output 0, input 0)
- get_upcoming_tasks → MCP Server Trigger (`ai_tool`, output 0, input 0)
- create_upcoming_task → MCP Server Trigger (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0882_Telegram_Googletaskstool_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0882_Telegram_Googletaskstool_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
