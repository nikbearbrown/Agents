# Investor agent - part 2

This folder contains the **Investor agent - part 2** workflow. Its executable nodes use `code`, `manualTrigger`, `postgres`, `rssFeedRead`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`investor-agent-part-2.json`](investor-agent-part-2.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`

**Entry nodes:** When clicking ‘Execute workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| RSS Read | `rssFeedRead` | Inspect parameters |
| Extract Funding Deals | `code` | Inspect parameters |
| Insert or update rows in a table | `postgres` | upsert |
| extract investor | `code` | Inspect parameters |
| Execute a SQL query | `postgres` | executeQuery |
| Build Investor Links | `code` | Inspect parameters |
| Insert or update rows in a table1 | `postgres` | upsert |
| Execute a SQL query1 | `postgres` | executeQuery |

## Connection map

- When clicking ‘Execute workflow’ → RSS Read (`main`, output 0, input 0)
- RSS Read → Extract Funding Deals (`main`, output 0, input 0)
- Extract Funding Deals → Insert or update rows in a table (`main`, output 0, input 0)
- Extract Funding Deals → extract investor (`main`, output 0, input 0)
- extract investor → Build Investor Links (`main`, output 0, input 0)
- Build Investor Links → Insert or update rows in a table1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
