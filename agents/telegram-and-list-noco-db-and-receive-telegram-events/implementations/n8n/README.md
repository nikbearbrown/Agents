# telegram and list noco db and receive telegram events

This folder contains the **telegram and list noco db and receive telegram events** workflow. Its executable nodes use `function`, `httpRequest`, `if`, `merge`, `nocoDb`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-and-list-noco-db-and-receive-telegram-events.json`](telegram-and-list-noco-db-and-receive-telegram-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `nocoDb`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| chatID | `function` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| IF | `if` | Inspect parameters |
| msg_greet | `telegram` | Inspect parameters |
| msg_welcomeback | `telegram` | Inspect parameters |
| msg_help | `telegram` | Inspect parameters |
| msg_wrongcommand | `telegram` | Inspect parameters |
| New user? | `function` | Inspect parameters |
| CheckUser | `nocoDb` | getAll |
| LoadDictionary | `nocoDb` | getAll |
| botmessages | `function` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| HTTP AddUser | `httpRequest` | Inspect parameters |
| HTTP UpdateUser | `httpRequest` | Inspect parameters |
| AddUser | `nocoDb` | create |
| UpdateUser | `nocoDb` | update |

## Connection map

- IF → HTTP AddUser (`main`, output 0, input 0)
- IF → HTTP UpdateUser (`main`, output 1, input 0)
- Merge → Switch (`main`, output 0, input 0)
- Switch → New user? (`main`, output 0, input 0)
- Switch → msg_help (`main`, output 1, input 0)
- Switch → msg_wrongcommand (`main`, output 3, input 0)
- chatID → LoadDictionary (`main`, output 0, input 0)
- CheckUser → Merge (`main`, output 0, input 1)
- New user? → IF (`main`, output 0, input 0)
- botmessages → CheckUser (`main`, output 0, input 0)
- HTTP AddUser → msg_greet (`main`, output 0, input 0)
- LoadDictionary → botmessages (`main`, output 0, input 0)
- HTTP UpdateUser → msg_welcomeback (`main`, output 0, input 0)
- Telegram Trigger → chatID (`main`, output 0, input 0)
- Telegram Trigger → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Nocodb/0193_Nocodb_Telegram_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Nocodb/0193_Nocodb_Telegram_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
