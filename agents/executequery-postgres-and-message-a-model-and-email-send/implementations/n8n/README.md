# My workflow 4

This folder contains the **My workflow 4** workflow. Its executable nodes use `code`, `emailSend`, `googleGemini`, `manualTrigger`, `postgres`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`executequery-postgres-and-message-a-model-and-email-send.json`](executequery-postgres-and-message-a-model-and-email-send.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `postgres`, `smtp`

**Entry nodes:** When clicking ‘Execute workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Execute a SQL query | `postgres` | executeQuery |
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| Execute a SQL query1 | `postgres` | executeQuery |
| Execute a SQL query2 | `postgres` | executeQuery |
| Collect User Requirements | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Message a model | `googleGemini` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |

## Connection map

- When clicking ‘Execute workflow’ → Collect User Requirements (`main`, output 0, input 0)
- Collect User Requirements → Execute a SQL query2 (`main`, output 0, input 0)
- Execute a SQL query2 → Code (`main`, output 0, input 0)
- Code → Message a model (`main`, output 0, input 0)
- Message a model → Code1 (`main`, output 0, input 0)
- Code1 → Send email (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
