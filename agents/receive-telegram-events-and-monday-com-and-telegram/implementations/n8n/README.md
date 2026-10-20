# receive telegram events and monday com and telegram

This folder contains the **receive telegram events and monday com and telegram** workflow. Its executable nodes use `freshdesk`, `if`, `mondayCom`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-monday-com-and-telegram.json`](receive-telegram-events-and-monday-com-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `freshdeskApi`, `mondayComApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Monday.com | `mondayCom` | boardItem |
| Monday.com1 | `mondayCom` | boardItem |
| Telegram | `telegram` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| Freshdesk | `freshdesk` | Inspect parameters |
| Freshdesk1 | `freshdesk` | Inspect parameters |
| Telegram1 | `telegram` | Inspect parameters |

## Connection map

- IF1 → Freshdesk (`main`, output 0, input 0)
- IF1 → Freshdesk1 (`main`, output 1, input 0)
- Telegram → Monday.com (`main`, output 0, input 0)
- Freshdesk → Telegram (`main`, output 0, input 0)
- Telegram1 → Monday.com1 (`main`, output 0, input 0)
- Freshdesk1 → Telegram1 (`main`, output 0, input 0)
- Telegram Trigger → IF1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0885_Telegram_Mondaycom_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0885_Telegram_Mondaycom_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
