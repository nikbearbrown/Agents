# Syncro Status Update Clockify

This folder contains the **Syncro Status Update Clockify** workflow. Its executable nodes use `clockify`, `httpRequest`, `if`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`syncro-status-update-clockify.json`](syncro-status-update-clockify.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clockifyApi`, `httpHeaderAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Clockify | `clockify` | getAll |
| HTTP Request | `httpRequest` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| Clockify1 | `clockify` | getAll |
| HTTP Request1 | `httpRequest` | Inspect parameters |

## Connection map

- IF1 → Clockify (`main`, output 0, input 0)
- IF1 → Clockify1 (`main`, output 1, input 0)
- Webhook → IF1 (`main`, output 0, input 0)
- Clockify → HTTP Request (`main`, output 0, input 0)
- Clockify1 → HTTP Request1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1064_HTTP_Clockify_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1064_HTTP_Clockify_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
