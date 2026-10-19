# write binary file and read binary file and http request

This folder contains the **write binary file and read binary file and http request** workflow. Its executable nodes use `cron`, `function`, `functionItem`, `httpRequest`, `manualTrigger`, `moveBinaryData`, `readBinaryFile`, `set`, `telegram`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`write-binary-file-and-read-binary-file-and-http-request.json`](write-binary-file-and-read-binary-file-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `telegramApi`

**Entry nodes:** On clicking 'execute', Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Write Binary File | `writeBinaryFile` | Inspect parameters |
| Read Binary File | `readBinaryFile` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Binary to json | `moveBinaryData` | Inspect parameters |
| Json to binary | `moveBinaryData` | Inspect parameters |
| Set new update time | `functionItem` | Inspect parameters |
| Split into baches | `function` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| Config | `set` | Inspect parameters |

## Connection map

- Cron → Read Binary File (`main`, output 0, input 0)
- HTTP Request → Split into baches (`main`, output 0, input 0)
- HTTP Request → Set new update time (`main`, output 0, input 0)
- Binary to json → HTTP Request (`main`, output 0, input 0)
- Json to binary → Write Binary File (`main`, output 0, input 0)
- Read Binary File → Binary to json (`main`, output 0, input 0)
- Split into baches → Telegram (`main`, output 0, input 0)
- Set new update time → Json to binary (`main`, output 0, input 0)
- On clicking 'execute' → Read Binary File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0158_Telegram_Functionitem_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0158_Telegram_Functionitem_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
