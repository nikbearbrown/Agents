# On User created event in Intercom

This folder contains the **On User created event in Intercom** workflow. Its executable nodes use `code`, `httpRequest`, `intercom`, `noOp`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`on-user-created-event-in-intercom.json`](on-user-created-event-in-intercom.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `intercomApi`

**Entry nodes:** On Webhook event from Intercom

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Could not find user | `noOp` | Inspect parameters |
| On Webhook event from Intercom | `webhook` | Inspect parameters |
| set key fields | `set` | Inspect parameters |
| Update data in Intercom | `httpRequest` | PUT |
| Other event | `noOp` | Inspect parameters |
| Intercom | `intercom` | update |
| massage data | `code` | Inspect parameters |
| On user created | `switch` | Inspect parameters |
| Enrich user from ExactBuyer | `httpRequest` | Inspect parameters |

## Connection map

- massage data → Update data in Intercom (`main`, output 0, input 0)
- set key fields → Enrich user from ExactBuyer (`main`, output 0, input 0)
- On user created → set key fields (`main`, output 0, input 0)
- On user created → Other event (`main`, output 1, input 0)
- Enrich user from ExactBuyer → massage data (`main`, output 0, input 0)
- Enrich user from ExactBuyer → Could not find user (`main`, output 1, input 0)
- On Webhook event from Intercom → On user created (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Intercom/0413_Intercom_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Intercom/0413_Intercom_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
