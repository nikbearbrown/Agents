# sendandwait telegram and set redis and get redis

This folder contains the **sendandwait telegram and set redis and get redis** workflow. Its executable nodes use `agent`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `if`, `informationExtractor`, `lmChatOpenAi`, `memoryManager`, `memoryRedisChat`, `redis`, `switch`, `telegram`, `telegramTrigger`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sendandwait-telegram-and-set-redis-and-get-redis.json`](sendandwait-telegram-and-set-redis-and-get-redis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `redis`, `telegramApi`

**Entry nodes:** Handoff Subworkflow, Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Human Handoff using Send and Wait | `telegram` | sendAndWait |
| Set Interaction to Bot | `redis` | set |
| Set Interaction to Human | `redis` | set |
| Get Interaction State | `redis` | get |
| Model | `lmChatOpenAi` | Inspect parameters |
| Memory | `memoryRedisChat` | Inspect parameters |
| Handoff Subworkflow | `executeWorkflowTrigger` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Send Response | `telegram` | Inspect parameters |
| Switch Interaction | `switch` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| With Defaults | `code` | Inspect parameters |
| Has All Criteria? | `if` | Inspect parameters |
| Onboarding Agent | `agent` | Inspect parameters |
| Get Onboarding Chat History | `redis` | get |
| After Sales Agent | `agent` | Inspect parameters |
| Memory1 | `memoryRedisChat` | Inspect parameters |
| Model1 | `lmChatOpenAi` | Inspect parameters |
| Handoff Tool | `toolWorkflow` | Inspect parameters |
| Handoff Subworkflow1 | `executeWorkflow` | Inspect parameters |
| Send Response2 | `telegram` | Inspect parameters |
| Memory2 | `memoryRedisChat` | Inspect parameters |
| Update Agent Memory | `memoryManager` | Inspect parameters |
| Send Response3 | `telegram` | Inspect parameters |
| Get Canned Response | `telegram` | Inspect parameters |
| Notify user | `telegram` | Inspect parameters |
| Memory3 | `memoryRedisChat` | Inspect parameters |
| Update Agent Memory1 | `memoryManager` | Inspect parameters |
| Continue Conversation | `telegram` | Inspect parameters |

## Connection map

- Model → Onboarding Agent (`ai_languageModel`, output 0, input 0)
- Memory → Onboarding Agent (`ai_memory`, output 0, input 0)
- Model1 → After Sales Agent (`ai_languageModel`, output 0, input 0)
- Memory1 → After Sales Agent (`ai_memory`, output 0, input 0)
- Memory2 → Update Agent Memory (`ai_memory`, output 0, input 0)
- Memory3 → Update Agent Memory1 (`ai_memory`, output 0, input 0)
- Notify user → Set Interaction to Human (`main`, output 0, input 0)
- Handoff Tool → After Sales Agent (`ai_tool`, output 0, input 0)
- Send Response → Update Agent Memory1 (`main`, output 0, input 0)
- With Defaults → Has All Criteria? (`main`, output 0, input 0)
- Onboarding Agent → Get Onboarding Chat History (`main`, output 0, input 0)
- Telegram Trigger → Get Interaction State (`main`, output 0, input 0)
- After Sales Agent → Send Response3 (`main`, output 0, input 0)
- Has All Criteria? → Handoff Subworkflow1 (`main`, output 0, input 0)
- Has All Criteria? → Continue Conversation (`main`, output 1, input 0)
- OpenAI Chat Model → Information Extractor (`ai_languageModel`, output 0, input 0)
- Switch Interaction → Get Canned Response (`main`, output 0, input 0)
- Switch Interaction → After Sales Agent (`main`, output 1, input 0)
- Switch Interaction → Onboarding Agent (`main`, output 2, input 0)
- Handoff Subworkflow → Notify user (`main`, output 0, input 0)
- Update Agent Memory → Send Response2 (`main`, output 0, input 0)
- Handoff Subworkflow1 → Send Response (`main`, output 0, input 0)
- Get Interaction State → Switch Interaction (`main`, output 0, input 0)
- Information Extractor → With Defaults (`main`, output 0, input 0)
- Set Interaction to Bot → Update Agent Memory (`main`, output 0, input 0)
- Set Interaction to Human → Human Handoff using Send and Wait (`main`, output 0, input 0)
- Get Onboarding Chat History → Information Extractor (`main`, output 0, input 0)
- Human Handoff using Send and Wait → Set Interaction to Bot (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0815_Telegram_Code_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0815_Telegram_Code_Update_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
