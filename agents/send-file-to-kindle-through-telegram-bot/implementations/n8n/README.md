# send file to kindle through telegram bot

This folder contains the **send file to kindle through telegram bot** workflow. Its executable nodes use `code`, `if`, `microsoftOutlook`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-file-to-kindle-through-telegram-bot.json`](send-file-to-kindle-through-telegram-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** receive file message from telegram bot

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| receive file message from telegram bot | `telegramTrigger` | Inspect parameters |
| check if there is a file in the message | `if` | Inspect parameters |
| reply to warn that file is missing | `telegram` | Inspect parameters |
| rename file to as attachment out email | `code` | Inspect parameters |
| send email with the file as attchament to kindle | `microsoftOutlook` | Inspect parameters |
| reply to telegram chat that the file has been sent successfully | `telegram` | Inspect parameters |

## Connection map

- receive file message from telegram bot → check if there is a file in the message (`main`, output 0, input 0)
- rename file to as attachment out email → send email with the file as attchament to kindle (`main`, output 0, input 0)
- check if there is a file in the message → rename file to as attachment out email (`main`, output 0, input 0)
- check if there is a file in the message → reply to warn that file is missing (`main`, output 1, input 0)
- send email with the file as attchament to kindle → reply to telegram chat that the file has been sent successfully (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftoutlook/1944_Microsoftoutlook_Telegram_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftoutlook/1944_Microsoftoutlook_Telegram_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
