# crypto market alert system with binance and telegram integration

This folder contains the **crypto market alert system with binance and telegram integration** workflow. Its executable nodes use `aggregate`, `code`, `function`, `httpRequest`, `scheduleTrigger`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`crypto-market-alert-system-with-binance-and-telegram-integration.json`](crypto-market-alert-system-with-binance-and-telegram-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Send Telegram Message | `telegram` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Binance 24h Price Change | `httpRequest` | Inspect parameters |
| Filter by 10% Change rate | `function` | Inspect parameters |
| Split By 1K chars | `code` | Inspect parameters |

## Connection map

- Aggregate → Split By 1K chars (`main`, output 0, input 0)
- Schedule Trigger → Binance 24h Price Change (`main`, output 0, input 0)
- Split By 1K chars → Send Telegram Message (`main`, output 0, input 0)
- Binance 24h Price Change → Filter by 10% Change rate (`main`, output 0, input 0)
- Filter by 10% Change rate → Aggregate (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0381_Telegram_Code_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0381_Telegram_Code_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
