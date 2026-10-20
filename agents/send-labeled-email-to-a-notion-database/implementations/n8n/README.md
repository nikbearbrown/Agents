# Send labeled email to a Notion database

This folder contains the **Send labeled email to a Notion database** workflow. Its executable nodes use `dateTime`, `gmail`, `httpRequest`, `if`, `merge`, `noOp`, `notion`, `notionTrigger`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-labeled-email-to-a-notion-database.json`](send-labeled-email-to-a-notion-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `notionApi`

**Entry nodes:** On schedule, On updated database page

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On schedule | `scheduleTrigger` | Inspect parameters |
| Derive last request time | `dateTime` | subtractFromDate |
| Get emails from label and last request time | `gmail` | getAll |
| Create database page | `notion` | databasePage |
| Try get database page | `notion` | databasePage / getAll |
| If checked off | `if` | Inspect parameters |
| On updated database page | `notionTrigger` | Inspect parameters |
| Remove label from target email | `gmail` | removeLabels |
| Not yet checked off, do nothing | `noOp` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| If found, do nothing | `noOp` | Inspect parameters |
| If database page not found | `if` | Inspect parameters |
| Find my email address | `httpRequest` | Inspect parameters |

## Connection map

- Merge → If database page not found (`main`, output 0, input 0)
- On schedule → Derive last request time (`main`, output 0, input 0)
- If checked off → Remove label from target email (`main`, output 0, input 0)
- If checked off → Not yet checked off, do nothing (`main`, output 1, input 0)
- Find my email address → Create database page (`main`, output 0, input 0)
- Try get database page → Merge (`main`, output 0, input 1)
- Derive last request time → Get emails from label and last request time (`main`, output 0, input 0)
- On updated database page → If checked off (`main`, output 0, input 0)
- If database page not found → Find my email address (`main`, output 0, input 0)
- If database page not found → If found, do nothing (`main`, output 1, input 0)
- Get emails from label and last request time → Try get database page (`main`, output 0, input 0)
- Get emails from label and last request time → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0311_Datetime_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0311_Datetime_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
