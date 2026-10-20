# receive telegram events and send next question and telegram

This folder contains the **receive telegram events and send next question and telegram** workflow. Its executable nodes use `agent`, `executionData`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryManager`, `memoryRedisChat`, `redis`, `set`, `switch`, `telegram`, `telegramTrigger`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-send-next-question-and-telegram.json`](receive-telegram-events-and-send-next-question-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `redis`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Send Next Question | `telegram` | Inspect parameters |
| Send Response | `telegram` | Inspect parameters |
| Has No Record? | `if` | Inspect parameters |
| Is Survey Continue? | `if` | Inspect parameters |
| Get State2 | `redis` | get |
| Get Columns1 | `googleSheets` | Inspect parameters |
| Set Variables1 | `set` | Inspect parameters |
| Message Type1 | `switch` | Inspect parameters |
| Get Command1 | `set` | Inspect parameters |
| Bot Actions1 | `switch` | Inspect parameters |
| Memory3 | `memoryRedisChat` | Inspect parameters |
| Get Survey State1 | `set` | Inspect parameters |
| Reset Agent Memory1 | `memoryManager` | Inspect parameters |
| Memory4 | `memoryRedisChat` | Inspect parameters |
| Start Session1 | `redis` | set |
| Get State3 | `redis` | get |
| Increment Index1 | `redis` | set |
| Interview Agent1 | `agent` | Inspect parameters |
| Get Record1 | `googleSheets` | Inspect parameters |
| Append Responses1 | `set` | Inspect parameters |
| Update Answer2 | `httpRequest` | PUT |
| Get Last Bot Message1 | `redis` | get |
| Update Answer3 | `httpRequest` | PUT |
| Model2 | `lmChatOpenAi` | Inspect parameters |
| Model3 | `lmChatOpenAi` | Inspect parameters |
| Should Follow Up?1 | `textClassifier` | Inspect parameters |
| Execution Data2 | `executionData` | Inspect parameters |
| Create Record2 | `googleSheets` | appendOrUpdate |
| Send Start | `telegram` | Inspect parameters |
| Send Start1 | `telegram` | Inspect parameters |
| Completed Survey | `telegram` | Inspect parameters |
| Create Record1 | `googleSheets` | appendOrUpdate |

## Connection map

- Model2 → Interview Agent1 (`ai_languageModel`, output 0, input 0)
- Model3 → Should Follow Up?1 (`ai_languageModel`, output 0, input 0)
- Memory3 → Reset Agent Memory1 (`ai_memory`, output 0, input 0)
- Memory4 → Interview Agent1 (`ai_memory`, output 0, input 0)
- Get State2 → Message Type1 (`main`, output 0, input 0)
- Get State3 → Get Columns1 (`main`, output 0, input 0)
- Get Record1 → Has No Record? (`main`, output 0, input 0)
- Bot Actions1 → Create Record1 (`main`, output 0, input 0)
- Bot Actions1 → Get State3 (`main`, output 1, input 0)
- Bot Actions1 → Send Start1 (`main`, output 2, input 0)
- Get Columns1 → Get Survey State1 (`main`, output 0, input 0)
- Get Command1 → Bot Actions1 (`main`, output 0, input 0)
- Message Type1 → Get Command1 (`main`, output 0, input 0)
- Message Type1 → Get Record1 (`main`, output 1, input 0)
- Create Record1 → Start Session1 (`main`, output 0, input 0)
- Create Record2 → Get State3 (`main`, output 0, input 0)
- Has No Record? → Create Record2 (`main`, output 0, input 0)
- Has No Record? → Get Last Bot Message1 (`main`, output 1, input 0)
- Set Variables1 → Execution Data2 (`main`, output 0, input 0)
- Start Session1 → Send Start (`main`, output 0, input 0)
- Update Answer2 → Send Response (`main`, output 0, input 0)
- Update Answer3 → Get State3 (`main`, output 0, input 0)
- Execution Data2 → Get State2 (`main`, output 0, input 0)
- Increment Index1 → Is Survey Continue? (`main`, output 0, input 0)
- Interview Agent1 → Update Answer2 (`main`, output 0, input 0)
- Telegram Trigger → Set Variables1 (`main`, output 0, input 0)
- Append Responses1 → Should Follow Up?1 (`main`, output 0, input 0)
- Get Survey State1 → Increment Index1 (`main`, output 0, input 0)
- Should Follow Up?1 → Update Answer3 (`main`, output 0, input 0)
- Should Follow Up?1 → Interview Agent1 (`main`, output 1, input 0)
- Is Survey Continue? → Reset Agent Memory1 (`main`, output 0, input 0)
- Is Survey Continue? → Completed Survey (`main`, output 1, input 0)
- Reset Agent Memory1 → Send Next Question (`main`, output 0, input 0)
- Get Last Bot Message1 → Append Responses1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0782_Telegram_Redis_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0782_Telegram_Redis_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
