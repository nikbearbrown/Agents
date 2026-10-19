# Use Config Bot to setup your telegram details, like:

This folder contains the **Use Config Bot to setup your telegram details, like:** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `if`, `noOp`, `redis`, `set`, `splitInBatches`, `switch`, `telegram`, `telegramTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`use-config-bot-to-setup-your-telegram-details-like.json`](use-config-bot-to-setup-your-telegram-details-like.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `redis`, `telegramApi`

**Entry nodes:** Telegram-Bot

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| New User ? | `if` | Inspect parameters |
| Format | `code` | Inspect parameters |
| Bot-Fields | `set` | Inspect parameters |
| Create Topic (Chat Ticket) | `httpRequest` | Inspect parameters |
| Save Topic ID | `redis` | set |
| Get User Chat Topic | `redis` | get |
| Forward New Message | `httpRequest` | POST |
| IF No Topic Created | `if` | Inspect parameters |
| ReCreate Topic (Chat Ticket) | `httpRequest` | Inspect parameters |
| ReSave Topic ID | `redis` | set |
| Update User Data | `redis` | set |
| Save User Data | `redis` | set |
| Support Forum | `if` | Inspect parameters |
| From Ticket | `if` | Inspect parameters |
| Forward Support Reply To User | `httpRequest` | POST |
| IF Topic Created | `if` | Inspect parameters |
| Forward New Message to the recrated topic | `httpRequest` | POST |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Check User in Database | `redis` | keys |
| Send User Ticket Created Notification | `telegram` | Inspect parameters |
| Bot-Config | `set` | Inspect parameters |
| Telegram-Bot | `telegramTrigger` | Inspect parameters |
| 1st | `switch` | Inspect parameters |
| Split In Batches1 | `splitInBatches` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Format Users | `code` | Inspect parameters |
| Broadcast Channel Post into Users | `httpRequest` | POST |
| Set Blocked Member | `redis` | set |
| IF Verified Channel | `if` | Inspect parameters |
| Filter Blocked Users | `filter` | Inspect parameters |
| Retrieve all users in DB | `redis` | keys |

## Connection map

- 1st → Check User in Database (`main`, output 1, input 0)
- 1st → Support Forum (`main`, output 2, input 0)
- 1st → IF Verified Channel (`main`, output 3, input 0)
- Wait1 → Split In Batches1 (`main`, output 0, input 0)
- Format → Bot-Fields (`main`, output 0, input 0)
- Bot-Config → Format (`main`, output 0, input 0)
- Bot-Fields → 1st (`main`, output 0, input 0)
- New User ? → Save User Data (`main`, output 0, input 0)
- New User ? → Update User Data (`main`, output 1, input 0)
- From Ticket → Forward Support Reply To User (`main`, output 0, input 0)
- From Ticket → IF Topic Created (`main`, output 1, input 0)
- Format Users → Filter Blocked Users (`main`, output 0, input 0)
- Telegram-Bot → Bot-Config (`main`, output 0, input 0)
- Save Topic ID → Forward New Message (`main`, output 0, input 0)
- Support Forum → From Ticket (`main`, output 0, input 0)
- Save User Data → Create Topic (Chat Ticket) (`main`, output 0, input 0)
- ReSave Topic ID → Forward New Message to the recrated topic (`main`, output 0, input 0)
- IF Topic Created → Send User Ticket Created Notification (`main`, output 0, input 0)
- Update User Data → Get User Chat Topic (`main`, output 0, input 0)
- Split In Batches1 → Broadcast Channel Post into Users (`main`, output 0, input 0)
- Set Blocked Member → Split In Batches1 (`main`, output 0, input 0)
- Forward New Message → No Operation, do nothing (`main`, output 0, input 0)
- Forward New Message → IF No Topic Created (`main`, output 1, input 0)
- Get User Chat Topic → Forward New Message (`main`, output 0, input 0)
- IF No Topic Created → ReCreate Topic (Chat Ticket) (`main`, output 0, input 0)
- IF No Topic Created → No Operation, do nothing (`main`, output 1, input 0)
- IF Verified Channel → Retrieve all users in DB (`main`, output 0, input 0)
- IF Verified Channel → No Operation, do nothing (`main`, output 1, input 0)
- Filter Blocked Users → Split In Batches1 (`main`, output 0, input 0)
- Check User in Database → New User ? (`main`, output 0, input 0)
- Retrieve all users in DB → Format Users (`main`, output 0, input 0)
- Create Topic (Chat Ticket) → Save Topic ID (`main`, output 0, input 0)
- ReCreate Topic (Chat Ticket) → ReSave Topic ID (`main`, output 0, input 0)
- Forward Support Reply To User → No Operation, do nothing (`main`, output 0, input 0)
- Broadcast Channel Post into Users → Wait1 (`main`, output 0, input 0)
- Broadcast Channel Post into Users → Set Blocked Member (`main`, output 1, input 0)
- Send User Ticket Created Notification → No Operation, do nothing (`main`, output 0, input 0)
- Forward New Message to the recrated topic → No Operation, do nothing (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0383_Telegram_Wait_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0383_Telegram_Wait_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
