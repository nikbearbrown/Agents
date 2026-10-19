# receive schedule events and get auth token and get latest requests

This folder contains the **receive schedule events and get auth token and get latest requests** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `keyValueStorage`, `merge`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-get-auth-token-and-get-latest-requests.json`](receive-schedule-events-and-get-auth-token-and-get-latest-requests.json): sanitized, inactive import copy with an overview sticky note.
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
| Get Auth Token | `httpRequest` | POST |
| Unprocessed Requests | `code` | Inspect parameters |
| Get Latest Requests | `httpRequest` | Inspect parameters |
| POST to n8n | `httpRequest` | POST |
| Merge | `merge` | Inspect parameters |
| Local Webhook Address | `set` | Inspect parameters |
| Latest Update Time | `code` | Inspect parameters |
| Store Auth Token | `keyValueStorage` | Inspect parameters |
| Store Last Processed | `keyValueStorage` | Inspect parameters |
| Retrieve Auth Token | `keyValueStorage` | read |
| Retrieve Last Processed | `keyValueStorage` | read |
| If Auth Token Exists | `if` | Inspect parameters |

## Connection map

- Merge → Unprocessed Requests (`main`, output 0, input 0)
- Get Auth Token → Store Auth Token (`main`, output 0, input 0)
- Schedule Trigger → Local Webhook Address (`main`, output 0, input 0)
- Schedule Trigger → Retrieve Last Processed (`main`, output 0, input 0)
- Store Auth Token → Get Latest Requests (`main`, output 0, input 0)
- Latest Update Time → Store Last Processed (`main`, output 0, input 0)
- Get Latest Requests → Merge (`main`, output 0, input 1)
- Retrieve Auth Token → If Auth Token Exists (`main`, output 0, input 0)
- If Auth Token Exists → Get Latest Requests (`main`, output 0, input 0)
- If Auth Token Exists → Get Auth Token (`main`, output 1, input 0)
- Store Last Processed → POST to n8n (`main`, output 0, input 0)
- Unprocessed Requests → Latest Update Time (`main`, output 0, input 0)
- Local Webhook Address → Retrieve Auth Token (`main`, output 0, input 0)
- Retrieve Last Processed → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0588_HTTP_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0588_HTTP_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
