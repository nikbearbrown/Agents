# Simple Conversion of Emails into HTML Webpages

This folder contains the **Simple Conversion of Emails into HTML Webpages** workflow. Its executable nodes use `emailReadImap`, `httpRequest`, `telegram`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`simple-conversion-of-emails-into-html-webpages.json`](simple-conversion-of-emails-into-html-webpages.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Github Gist | `httpRequest` | POST |
| Wait | `wait` | Inspect parameters |
| Telegram ‌ | `telegram` | deleteMessage |
| Github Gist ‌ | `httpRequest` | DELETE |

## Connection map

- Wait → Github Gist ‌ (`main`, output 0, input 0)
- Telegram → Wait (`main`, output 0, input 0)
- Github Gist → Telegram (`main`, output 0, input 0)
- Github Gist ‌ → Telegram ‌ (`main`, output 0, input 0)
- Email Trigger (IMAP) → Github Gist (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0398_Telegram_Wait_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0398_Telegram_Wait_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
