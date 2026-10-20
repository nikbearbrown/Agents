# telegram and send assign alert and webhook

This folder contains the **telegram and send assign alert and webhook** workflow. Its executable nodes use `code`, `if`, `switch`, `telegram`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-and-send-assign-alert-and-webhook.json`](telegram-and-send-assign-alert-and-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `telegramApi`

**Entry nodes:** jira-webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| telegram account | `code` | Inspect parameters |
| check tg account exists | `if` | Inspect parameters |
| check type | `switch` | Inspect parameters |
| Send Update | `telegram` | Inspect parameters |
| Send Create | `telegram` | Inspect parameters |
| Send Assign Alert | `telegram` | Inspect parameters |
| check issue body, assignee and hook type | `if` | Inspect parameters |
| jira-webhook | `webhook` | Inspect parameters |

## Connection map

- check type → Send Create (`main`, output 0, input 0)
- check type → Send Update (`main`, output 1, input 0)
- check type → Send Assign Alert (`main`, output 2, input 0)
- jira-webhook → check issue body, assignee and hook type (`main`, output 0, input 0)
- telegram account → check tg account exists (`main`, output 0, input 0)
- check tg account exists → check type (`main`, output 0, input 0)
- check issue body, assignee and hook type → telegram account (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0683_Webhook_Telegram_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0683_Webhook_Telegram_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
