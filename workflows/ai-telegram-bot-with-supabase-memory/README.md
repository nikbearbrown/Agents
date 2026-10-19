# AI Telegram Bot with Supabase memory

This folder contains the **AI Telegram Bot with Supabase memory** workflow. Its executable nodes use `httpRequest`, `if`, `merge`, `supabase`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-telegram-bot-with-supabase-memory.json`](ai-telegram-bot-with-supabase-memory.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `supabaseApi`, `telegramApi`

**Entry nodes:** Get New Message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get New Message | `telegramTrigger` | Inspect parameters |
| OPENAI - Create thread | `httpRequest` | POST |
| Create User | `supabase` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| OPENAI - Send message | `httpRequest` | POST |
| OPENAI - Run assistant | `httpRequest` | POST |
| OPENAI - Get messages | `httpRequest` | Inspect parameters |
| Send Message to User | `telegram` | Inspect parameters |
| If User exists | `if` | Inspect parameters |
| Find User | `supabase` | getAll |

## Connection map

- Merge → OPENAI - Send message (`main`, output 0, input 0)
- Find User → If User exists (`main`, output 0, input 0)
- Create User → Merge (`main`, output 0, input 1)
- If User exists → Merge (`main`, output 0, input 0)
- If User exists → OPENAI - Create thread (`main`, output 1, input 0)
- Get New Message → Find User (`main`, output 0, input 0)
- OPENAI - Get messages → Send Message to User (`main`, output 0, input 0)
- OPENAI - Send message → OPENAI - Run assistant (`main`, output 0, input 0)
- OPENAI - Create thread → Create User (`main`, output 0, input 0)
- OPENAI - Run assistant → OPENAI - Get messages (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0594_HTTP_Telegram_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0594_HTTP_Telegram_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
