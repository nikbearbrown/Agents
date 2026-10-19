# n8n update

This folder contains the **n8n update** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `merge`, `scheduleTrigger`, `set`, `ssh`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-update.json`](n8n-update.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `sshPassword`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Pull n8n Image | `ssh` | Inspect parameters |
| docker compose pull | `ssh` | Inspect parameters |
| check n8n installed version | `ssh` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| docker compose up | `ssh` | Inspect parameters |
| Set Default variable | `set` | Inspect parameters |
| Github HTTP Request | `httpRequest` | Inspect parameters |
| Merge Results | `merge` | Inspect parameters |
| Edit Version String | `set` | Inspect parameters |
| Comapre Two Input | `if` | Inspect parameters |
| Telegram Notif | `telegram` | Inspect parameters |
| Telegram Approve | `telegram` | sendAndWait |
| Telegram Notif1 | `telegram` | Inspect parameters |

## Connection map

- Merge Results → Comapre Two Input (`main`, output 0, input 0)
- Pull n8n Image → docker compose pull (`main`, output 0, input 0)
- Telegram Notif1 → Comapre Two Input (`main`, output 0, input 0)
- Schedule Trigger → Set Default variable (`main`, output 0, input 0)
- Telegram Approve → Pull n8n Image (`main`, output 0, input 0)
- Comapre Two Input → Telegram Notif (`main`, output 0, input 0)
- Comapre Two Input → Telegram Approve (`main`, output 1, input 0)
- docker compose up → Telegram Notif1 (`main`, output 0, input 0)
- Edit Version String → Merge Results (`main`, output 0, input 1)
- Github HTTP Request → Edit Version String (`main`, output 0, input 0)
- docker compose pull → docker compose up (`main`, output 0, input 0)
- Set Default variable → check n8n installed version (`main`, output 0, input 0)
- Set Default variable → Github HTTP Request (`main`, output 0, input 0)
- check n8n installed version → Merge Results (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Default variable (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1595_Telegram_Schedule_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1595_Telegram_Schedule_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
