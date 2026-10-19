# list airtable and incr redis and webhook

This folder contains the **list airtable and incr redis and webhook** workflow. Its executable nodes use `airtable`, `function`, `if`, `redis`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-airtable-and-incr-redis-and-webhook.json`](list-airtable-and-incr-redis-and-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `httpHeaderAuth`, `redis`

**Entry nodes:** Webhook1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Airtable | `airtable` | list |
| Redis | `redis` | incr |
| Redis1 | `redis` | incr |
| Set1 | `set` | Inspect parameters |
| Webhook1 | `webhook` | Inspect parameters |
| Function | `function` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Set2 | `set` | Inspect parameters |
| Set3 | `set` | Inspect parameters |
| Per hour | `if` | Inspect parameters |
| Per minute | `if` | Inspect parameters |

## Connection map

- Set → Redis (`main`, output 0, input 0)
- Set2 → Redis1 (`main`, output 0, input 0)
- Redis → Per minute (`main`, output 0, input 0)
- Redis1 → Per hour (`main`, output 0, input 0)
- Airtable → Function (`main`, output 0, input 0)
- Per hour → Airtable (`main`, output 0, input 0)
- Per hour → Set1 (`main`, output 1, input 0)
- Webhook1 → Set (`main`, output 0, input 0)
- Per minute → Set2 (`main`, output 0, input 0)
- Per minute → Set3 (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0099_Webhook_Airtable_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0099_Webhook_Airtable_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
