# Scenario 1 - AI Agent

This folder contains the **Scenario 1 - AI Agent** workflow. Its executable nodes use `agent`, `airtable`, `airtableTool`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `scheduleTrigger`, `set`, `splitInBatches`, `switch`, `telegram`, `telegramTrigger`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scenario-1-ai-agent.json`](scenario-1-ai-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Trigger, Workflow Input Trigger, Webhook, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Get Chart | `toolWorkflow` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Send Analysis | `telegram` | Inspect parameters |
| Workflow Input Trigger | `executeWorkflowTrigger` | Inspect parameters |
| response | `set` | Inspect parameters |
| Download Chart | `httpRequest` | Inspect parameters |
| Get Chart URL | `httpRequest` | POST |
| Send Chart | `telegram` | sendPhoto |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Transcribe | `openAi` | audio / transcribe |
| Download File | `telegram` | file |
| Set Text | `set` | Inspect parameters |
| Set Values | `set` | Inspect parameters |
| Technical Analysis | `openAi` | image / analyze |
| Webhook | `webhook` | Inspect parameters |
| Set Text1 | `set` | Inspect parameters |
| Save Ticker | `airtableTool` | create |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Run Agent | `httpRequest` | POST |
| Get tokens | `airtable` | search |

## Connection map

- Switch → Download File (`main`, output 0, input 0)
- Switch → Set Text (`main`, output 1, input 0)
- Webhook → Set Text1 (`main`, output 0, input 0)
- AI Agent → Send Analysis (`main`, output 0, input 0)
- Set Text → AI Agent (`main`, output 0, input 0)
- Get Chart → AI Agent (`ai_tool`, output 0, input 0)
- Run Agent → Loop Over Items (`main`, output 0, input 0)
- Set Text1 → AI Agent (`main`, output 0, input 0)
- Get tokens → Loop Over Items (`main`, output 0, input 0)
- Send Chart → response (`main`, output 0, input 0)
- Set Values → Get Chart URL (`main`, output 0, input 0)
- Transcribe → AI Agent (`main`, output 0, input 0)
- Save Ticker → AI Agent (`ai_tool`, output 0, input 0)
- Download File → Transcribe (`main`, output 0, input 0)
- Get Chart URL → Download Chart (`main`, output 0, input 0)
- Download Chart → Technical Analysis (`main`, output 0, input 0)
- Loop Over Items → Run Agent (`main`, output 1, input 0)
- Schedule Trigger → Get tokens (`main`, output 0, input 0)
- Telegram Trigger → Switch (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Technical Analysis → Send Chart (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Workflow Input Trigger → Set Values (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0769_Telegram_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0769_Telegram_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
