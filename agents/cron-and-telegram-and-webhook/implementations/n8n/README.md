# cron and telegram and webhook

This folder contains the **cron and telegram and webhook** workflow. Its executable nodes use `cron`, `manualTrigger`, `mySql`, `telegram`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cron-and-telegram-and-webhook.json`](cron-and-telegram-and-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`, `telegramApi`

**Entry nodes:** On clicking 'execute', Cron, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Telegram1 | `telegram` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| limparPacoteCliente1 | `mySql` | executeQuery |
| limpaPacoteCliente0 | `mySql` | executeQuery |

## Connection map

- Cron → limpaPacoteCliente0 (`main`, output 0, input 0)
- Cron → limparPacoteCliente1 (`main`, output 0, input 0)
- Webhook → limpaPacoteCliente0 (`main`, output 0, input 0)
- Webhook → limparPacoteCliente1 (`main`, output 0, input 0)
- limpaPacoteCliente0 → Telegram (`main`, output 0, input 0)
- limparPacoteCliente1 → Telegram1 (`main`, output 0, input 0)
- On clicking 'execute' → limpaPacoteCliente0 (`main`, output 0, input 0)
- On clicking 'execute' → limparPacoteCliente1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0140_Telegram_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0140_Telegram_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
