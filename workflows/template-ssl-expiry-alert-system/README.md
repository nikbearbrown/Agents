# Template - SSL Expiry Alert System

This folder contains the **Template - SSL Expiry Alert System** workflow. Its executable nodes use `Ntfy`, `gmail`, `googleSheets`, `httpRequest`, `scheduleTrigger`, `switch`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`template-ssl-expiry-alert-system.json`](template-ssl-expiry-alert-system.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `telegramApi`

**Entry nodes:** Weekly Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| URLs to Monitor | `googleSheets` | appendOrUpdate |
| Weekly Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch URLs | `googleSheets` | Inspect parameters |
| Check SSL | `httpRequest` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Send Alert Email2 | `gmail` | Inspect parameters |
| Send Alert Email4 | `gmail` | Inspect parameters |
| Send Alert Email6 | `gmail` | Inspect parameters |
| Ntfy4 | `Ntfy` | Inspect parameters |
| Send Alert Email1 | `gmail` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |

## Connection map

- Switch → Send Alert Email4 (`main`, output 0, input 0)
- Switch → Telegram (`main`, output 0, input 0)
- Switch → Send Alert Email2 (`main`, output 1, input 0)
- Switch → Send Alert Email1 (`main`, output 2, input 0)
- Switch → Send Alert Email6 (`main`, output 3, input 0)
- Switch → Ntfy4 (`main`, output 3, input 0)
- Check SSL → URLs to Monitor (`main`, output 0, input 0)
- Check SSL → Switch (`main`, output 0, input 0)
- Fetch URLs → Check SSL (`main`, output 0, input 0)
- Weekly Trigger → Fetch URLs (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1522_Telegram_Schedule_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1522_Telegram_Schedule_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
