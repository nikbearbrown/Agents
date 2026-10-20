# webhook and function item and http request

This folder contains the **webhook and function item and http request** workflow. Its executable nodes use `functionItem`, `httpRequest`, `if`, `telegram`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-function-item-and-http-request.json`](webhook-and-function-item-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `telegramApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| SearchTorrent | `functionItem` | Inspect parameters |
| Start download | `httpRequest` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Torrent not found | `telegram` | Inspect parameters |
| Telegram1 | `telegram` | Inspect parameters |
| IF2 | `if` | Inspect parameters |
| Start download new token | `httpRequest` | Inspect parameters |

## Connection map

- IF → Start download (`main`, output 0, input 0)
- IF → Torrent not found (`main`, output 1, input 0)
- IF2 → Start download new token (`main`, output 0, input 0)
- IF2 → Telegram1 (`main`, output 1, input 0)
- Webhook → SearchTorrent (`main`, output 0, input 0)
- SearchTorrent → IF (`main`, output 0, input 0)
- Start download → IF2 (`main`, output 0, input 0)
- Start download new token → Telegram1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0146_Functionitem_Telegram_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0146_Functionitem_Telegram_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
