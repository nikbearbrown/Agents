# webhook and get new accesstoken and receive schedule events

This folder contains the **webhook and get new accesstoken and receive schedule events** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `noOp`, `scheduleTrigger`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-get-new-accesstoken-and-receive-schedule-events.json`](webhook-and-get-new-accesstoken-and-receive-schedule-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| continue with valid token | `noOp` | Inspect parameters |
| get new accessToken | `httpRequest` | Inspect parameters |
| 2. set token in static data | `code` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| if token is valid | `if` | Inspect parameters |
| 1. initiate static data | `code` | Inspect parameters |

## Connection map

- Webhook → 1. initiate static data (`main`, output 0, input 0)
- Schedule Trigger → 1. initiate static data (`main`, output 0, input 0)
- if token is valid → continue with valid token (`main`, output 0, input 0)
- if token is valid → get new accessToken (`main`, output 1, input 0)
- get new accessToken → 2. set token in static data (`main`, output 0, input 0)
- 1. initiate static data → if token is valid (`main`, output 0, input 0)
- 2. set token in static data → continue with valid token (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0630_Code_Webhook_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0630_Code_Webhook_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
