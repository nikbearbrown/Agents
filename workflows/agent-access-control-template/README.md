# Agent Access Control Template

This folder contains the **Agent Access Control Template** workflow. Its executable nodes use `agent`, `airtable`, `code`, `executeWorkflowTrigger`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `telegram`, `telegramTrigger`, `toolCalculator`, `toolCode`, `toolHttpRequest`, `toolWikipedia`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`agent-access-control-template.json`](agent-access-control-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Trigger, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Check permissions | `code` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Set input | `set` | Inspect parameters |
| Get user permissions | `airtable` | search |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Simple Memory1 | `memoryBufferWindow` | Inspect parameters |
| Check permissions1 | `code` | Inspect parameters |
| list_granted_roles | `toolCode` | Inspect parameters |
| list_allowed_tools | `toolCode` | Inspect parameters |
| calculator | `toolCalculator` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| get_coordinates | `toolHttpRequest` | Inspect parameters |
| get_weather | `toolHttpRequest` | Inspect parameters |
| weather_agent | `toolWorkflow` | Inspect parameters |
| Weather Agent | `agent` | Inspect parameters |
| Unknown user | `if` | Inspect parameters |
| Reply: unknown user | `telegram` | Inspect parameters |
| Reply with results | `telegram` | Inspect parameters |
| Main Agent | `agent` | Inspect parameters |

## Connection map

- Settings → Weather Agent (`main`, output 0, input 0)
- Set input → Main Agent (`main`, output 0, input 0)
- Wikipedia → Main Agent (`ai_tool`, output 0, input 0)
- Main Agent → Reply with results (`main`, output 0, input 0)
- calculator → Check permissions (`ai_tool`, output 0, input 0)
- get_weather → Check permissions1 (`ai_tool`, output 0, input 0)
- Unknown user → Reply: unknown user (`main`, output 0, input 0)
- Unknown user → Set input (`main`, output 1, input 0)
- Simple Memory → Main Agent (`ai_memory`, output 0, input 0)
- weather_agent → Check permissions (`ai_tool`, output 0, input 0)
- Simple Memory1 → Weather Agent (`ai_memory`, output 0, input 0)
- get_coordinates → Check permissions1 (`ai_tool`, output 0, input 0)
- Telegram Trigger → Get user permissions (`main`, output 0, input 0)
- Check permissions → Main Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Main Agent (`ai_languageModel`, output 0, input 0)
- Check permissions1 → Weather Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model1 → Weather Agent (`ai_languageModel`, output 0, input 0)
- list_allowed_tools → Check permissions (`ai_tool`, output 0, input 0)
- list_granted_roles → Check permissions (`ai_tool`, output 0, input 0)
- Get user permissions → Unknown user (`main`, output 0, input 0)
- When Executed by Another Workflow → Settings (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1856_Telegram_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1856_Telegram_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
