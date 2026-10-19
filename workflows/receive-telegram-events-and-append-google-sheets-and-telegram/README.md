# receive telegram events and append google sheets and telegram

This folder contains the **receive telegram events and append google sheets and telegram** workflow. Its executable nodes use `code`, `googleSheets`, `if`, `telegram`, `telegramTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-append-google-sheets-and-telegram.json`](receive-telegram-events-and-append-google-sheets-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| Deep Work | `wait` | Inspect parameters |
| Break | `wait` | Inspect parameters |
| Initiate Static Data | `code` | Inspect parameters |
| Increment Count | `code` | Inspect parameters |
| Record Deep Work | `googleSheets` | append |
| Record Long Break | `googleSheets` | append |
| Instructions Message | `telegram` | Inspect parameters |
| start or stop? | `if` | Inspect parameters |
| Long Break Notification | `telegram` | Inspect parameters |
| Clear Variables1 | `code` | Inspect parameters |
| Clear Variables2 | `code` | Inspect parameters |
| < 4 Cycles | `if` | Inspect parameters |
| Short Break Notification | `telegram` | Inspect parameters |
| Back to Work Notification | `telegram` | Inspect parameters |
| Start Cycle Notification | `telegram` | Inspect parameters |
| End of Session Notification | `telegram` | Inspect parameters |

## Connection map

- If → start or stop? (`main`, output 0, input 0)
- If → Instructions Message (`main`, output 1, input 0)
- Break → Increment Count (`main`, output 0, input 0)
- Deep Work → Short Break Notification (`main`, output 0, input 0)
- < 4 Cycles → Long Break Notification (`main`, output 0, input 0)
- < 4 Cycles → Start Cycle Notification (`main`, output 1, input 0)
- start or stop? → Start Cycle Notification (`main`, output 0, input 0)
- start or stop? → End of Session Notification (`main`, output 1, input 0)
- Increment Count → Back to Work Notification (`main`, output 0, input 0)
- Telegram Trigger → If (`main`, output 0, input 0)
- Long Break Notification → Clear Variables2 (`main`, output 0, input 0)
- Long Break Notification → Record Long Break (`main`, output 0, input 0)
- Short Break Notification → Break (`main`, output 0, input 0)
- Start Cycle Notification → Deep Work (`main`, output 0, input 0)
- Back to Work Notification → < 4 Cycles (`main`, output 0, input 0)
- Back to Work Notification → Record Deep Work (`main`, output 0, input 0)
- End of Session Notification → Clear Variables1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0807_Telegram_Wait_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0807_Telegram_Wait_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
