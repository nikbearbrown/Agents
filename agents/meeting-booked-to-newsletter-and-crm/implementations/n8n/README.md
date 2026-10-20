# Meeting booked - to newsletter and CRM

This folder contains the **Meeting booked - to newsletter and CRM** workflow. Its executable nodes use `calTrigger`, `googleSheets`, `httpRequest`, `set`, `splitOut`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`meeting-booked-to-newsletter-and-crm.json`](meeting-booked-to-newsletter-and-crm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `calApi`, `googleSheetsOAuth2Api`, `telegramApi`

**Entry nodes:** on New Booking

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Attendees | `splitOut` | Inspect parameters |
| Add users | `googleSheets` | append |
| on New Booking | `calTrigger` | Inspect parameters |
| Add subscriber | `httpRequest` | POST |
| Set Attendee | `set` | Inspect parameters |
| notify in channel | `telegram` | Inspect parameters |
| set data | `set` | Inspect parameters |

## Connection map

- set data → Set Attendee (`main`, output 0, input 0)
- Add users → Add subscriber (`main`, output 0, input 0)
- Set Attendee → Add users (`main`, output 0, input 0)
- Add subscriber → notify in channel (`main`, output 0, input 0)
- on New Booking → Split Attendees (`main`, output 0, input 0)
- Split Attendees → set data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2018_Telegram_Cal_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2018_Telegram_Cal_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
