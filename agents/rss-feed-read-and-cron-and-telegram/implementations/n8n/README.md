# rss feed read and cron and telegram

This folder contains the **rss feed read and cron and telegram** workflow. Its executable nodes use `cron`, `function`, `if`, `rssFeedRead`, `splitInBatches`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rss-feed-read-and-cron-and-telegram.json`](rss-feed-read-and-cron-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `telegramApi`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| RSS Feed Read | `rssFeedRead` | Inspect parameters |
| SplitInBatches | `splitInBatches` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| only get new RSS | `function` | Inspect parameters |
| Telegram_IT | `telegram` | Inspect parameters |
| Telegram_Security | `telegram` | Inspect parameters |
| RSS Source | `function` | Inspect parameters |
| Telegram_M365 | `telegram` | Inspect parameters |
| IF-2 | `if` | Inspect parameters |
| IF-1 | `if` | Inspect parameters |
| Clear Function | `function` | Inspect parameters |

## Connection map

- Cron → RSS Source (`main`, output 0, input 0)
- IF-1 → Telegram_M365 (`main`, output 0, input 0)
- IF-1 → IF-2 (`main`, output 1, input 0)
- IF-2 → Telegram_Security (`main`, output 0, input 0)
- IF-2 → Telegram_IT (`main`, output 1, input 0)
- RSS Source → SplitInBatches (`main`, output 0, input 0)
- RSS Feed Read → SplitInBatches (`main`, output 0, input 0)
- RSS Feed Read → only get new RSS (`main`, output 0, input 0)
- SplitInBatches → RSS Feed Read (`main`, output 0, input 0)
- only get new RSS → IF-1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/0188_Rssfeedread_Telegram_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/0188_Rssfeedread_Telegram_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
