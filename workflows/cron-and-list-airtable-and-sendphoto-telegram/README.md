# cron and list airtable and sendphoto telegram

This folder contains the **cron and list airtable and sendphoto telegram** workflow. Its executable nodes use `airtable`, `cron`, `httpRequest`, `if`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cron-and-list-airtable-and-sendphoto-telegram.json`](cron-and-list-airtable-and-sendphoto-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `telegramApi`

**Entry nodes:** Cron, Telegram Trigger - people join bot

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Cron | `cron` | Inspect parameters |
| Airtable2 | `airtable` | list |
| Set | `set` | Inspect parameters |
| Recipe Photo | `telegram` | sendPhoto |
| Recipe URL | `telegram` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Airtable | `airtable` | list |
| Airtable1 | `airtable` | append |
| Telegram Recipe Image | `telegram` | sendPhoto |
| Telegram Recipe URL | `telegram` | Inspect parameters |
| Set1 | `set` | Inspect parameters |
| Get recipes from API | `httpRequest` | Inspect parameters |
| Get recipes | `httpRequest` | Inspect parameters |
| Telegram Trigger - people join bot | `telegramTrigger` | Inspect parameters |
| Telegram - Welcome Message | `telegram` | Inspect parameters |

## Connection map

- IF → Set1 (`main`, output 0, input 0)
- Set → Get recipes from API (`main`, output 0, input 0)
- Cron → Airtable2 (`main`, output 0, input 0)
- Set1 → Airtable1 (`main`, output 0, input 0)
- Airtable → IF (`main`, output 0, input 0)
- Airtable2 → Set (`main`, output 0, input 0)
- Get recipes → Telegram Recipe Image (`main`, output 0, input 0)
- Recipe Photo → Recipe URL (`main`, output 0, input 0)
- Get recipes from API → Recipe Photo (`main`, output 0, input 0)
- Telegram Recipe Image → Telegram Recipe URL (`main`, output 0, input 0)
- Telegram - Welcome Message → Get recipes (`main`, output 0, input 0)
- Telegram Trigger - people join bot → Airtable (`main`, output 0, input 0)
- Telegram Trigger - people join bot → Telegram - Welcome Message (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1654_HTTP_Telegram_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1654_HTTP_Telegram_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
