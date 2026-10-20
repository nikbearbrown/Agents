# telegram and receive telegram events and sendphoto telegram

This folder contains the **telegram and receive telegram events and sendphoto telegram** workflow. Its executable nodes use `executeCommand`, `function`, `httpRequest`, `if`, `merge`, `readBinaryFile`, `set`, `spreadsheetFile`, `switch`, `telegram`, `telegramTrigger`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-and-receive-telegram-events-and-sendphoto-telegram.json`](telegram-and-receive-telegram-events-and-sendphoto-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Switch | `switch` | Inspect parameters |
| msg_greet | `telegram` | Inspect parameters |
| msg_wrongcommand | `telegram` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| msg_getweather | `telegram` | sendPhoto |
| City List | `function` | Inspect parameters |
| Convert API response | `function` | Inspect parameters |
| Get weather data | `httpRequest` | Inspect parameters |
| Spreadsheet File | `spreadsheetFile` | toFile |
| Write csv | `writeBinaryFile` | Inspect parameters |
| Filename | `set` | Inspect parameters |
| msg_errorAPI | `telegram` | Inspect parameters |
| Any errors API? | `if` | Inspect parameters |
| msg_errorR | `telegram` | Inspect parameters |
| Read Binary File | `readBinaryFile` | Inspect parameters |
| R successful? | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| msg_pleasewait | `telegram` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Run R script | `executeCommand` | Inspect parameters |

## Connection map

- Merge → msg_wrongcommand (`main`, output 0, input 0)
- Merge1 → msg_greet (`main`, output 0, input 0)
- Merge2 → Filename (`main`, output 0, input 0)
- Switch → Merge1 (`main`, output 0, input 0)
- Switch → msg_pleasewait (`main`, output 1, input 0)
- Switch → Merge2 (`main`, output 1, input 0)
- Switch → Merge (`main`, output 3, input 0)
- Filename → City List (`main`, output 0, input 0)
- City List → Get weather data (`main`, output 0, input 0)
- Write csv → Run R script (`main`, output 0, input 0)
- Run R script → R successful? (`main`, output 0, input 0)
- R successful? → Read Binary File (`main`, output 0, input 0)
- R successful? → msg_errorR (`main`, output 1, input 0)
- msg_pleasewait → Merge2 (`main`, output 0, input 1)
- Any errors API? → msg_errorAPI (`main`, output 0, input 0)
- Any errors API? → Convert API response (`main`, output 1, input 0)
- Get weather data → Any errors API? (`main`, output 0, input 0)
- Read Binary File → msg_getweather (`main`, output 0, input 0)
- Spreadsheet File → Write csv (`main`, output 0, input 0)
- Telegram Trigger → Switch (`main`, output 0, input 0)
- Convert API response → Spreadsheet File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0201_Telegram_Executecommand_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0201_Telegram_Executecommand_Process_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
