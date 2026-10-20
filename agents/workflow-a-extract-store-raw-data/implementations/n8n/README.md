# Workflow A — Extract & Store Raw Data

This folder contains the **Workflow A — Extract & Store Raw Data** workflow. Its executable nodes use `code`, `executeWorkflow`, `httpRequest`, `if`, `postgres`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-a-extract-store-raw-data.json`](workflow-a-extract-store-raw-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch TechCrunch | `httpRequest` | Inspect parameters |
| Fetch VentureBeat | `httpRequest` | Inspect parameters |
| Fetch HackerNews | `httpRequest` | Inspect parameters |
| Fetch ArXiv | `httpRequest` | Inspect parameters |
| Fetch Reddit | `httpRequest` | Inspect parameters |
| Parse TechCrunch | `code` | Inspect parameters |
| Parse VentureBeat | `code` | Inspect parameters |
| Parse HackerNews | `code` | Inspect parameters |
| Parse ArXiv | `code` | Inspect parameters |
| Parse Reddit | `code` | Inspect parameters |
| Store TechCrunch | `postgres` | executeQuery |
| Store VentureBeat | `postgres` | executeQuery |
| Store HackerNews | `postgres` | executeQuery |
| Store ArXiv | `postgres` | executeQuery |
| Store Reddit | `postgres` | executeQuery |
| Verify — Count Stored Items | `postgres` | executeQuery |
| Check — New Items Exist? | `if` | Inspect parameters |
| Trigger — Start Workflow B | `executeWorkflow` | Inspect parameters |
| Log — Skip | `code` | Inspect parameters |

## Connection map

- Schedule Trigger → Fetch TechCrunch (`main`, output 0, input 0)
- Schedule Trigger → Fetch VentureBeat (`main`, output 0, input 0)
- Schedule Trigger → Fetch HackerNews (`main`, output 0, input 0)
- Schedule Trigger → Fetch ArXiv (`main`, output 0, input 0)
- Schedule Trigger → Fetch Reddit (`main`, output 0, input 0)
- Fetch TechCrunch → Parse TechCrunch (`main`, output 0, input 0)
- Fetch VentureBeat → Parse VentureBeat (`main`, output 0, input 0)
- Fetch HackerNews → Parse HackerNews (`main`, output 0, input 0)
- Fetch ArXiv → Parse ArXiv (`main`, output 0, input 0)
- Fetch Reddit → Parse Reddit (`main`, output 0, input 0)
- Parse TechCrunch → Store TechCrunch (`main`, output 0, input 0)
- Parse VentureBeat → Store VentureBeat (`main`, output 0, input 0)
- Parse HackerNews → Store HackerNews (`main`, output 0, input 0)
- Parse ArXiv → Store ArXiv (`main`, output 0, input 0)
- Parse Reddit → Store Reddit (`main`, output 0, input 0)
- Store TechCrunch → Verify — Count Stored Items (`main`, output 0, input 0)
- Store VentureBeat → Verify — Count Stored Items (`main`, output 0, input 0)
- Store HackerNews → Verify — Count Stored Items (`main`, output 0, input 0)
- Store ArXiv → Verify — Count Stored Items (`main`, output 0, input 0)
- Store Reddit → Verify — Count Stored Items (`main`, output 0, input 0)
- Verify — Count Stored Items → Check — New Items Exist? (`main`, output 0, input 0)
- Check — New Items Exist? → Trigger — Start Workflow B (`main`, output 0, input 0)
- Check — New Items Exist? → Log — Skip (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
