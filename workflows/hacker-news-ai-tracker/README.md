# Hacker News AI Tracker

This folder contains the **Hacker News AI Tracker** workflow. Its executable nodes use `code`, `executeWorkflow`, `executeWorkflowTrigger`, `httpRequest`, `manualTrigger`, `merge`, `scheduleTrigger`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hacker-news-ai-tracker.json`](hacker-news-ai-tracker.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger, Manual Trigger, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Get Day Ago Unix Time | `code` | Inspect parameters |
| WatchList | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Loop Over Entities | `splitInBatches` | Inspect parameters |
| Entity Term Pair | `code` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Call 'HackerNews' | `executeWorkflow` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Get Metrics | `code` | Inspect parameters |
| Code in Python | `code` | Inspect parameters |

## Connection map

- Schedule Trigger → Get Day Ago Unix Time (`main`, output 0, input 0)
- Schedule Trigger → WatchList (`main`, output 0, input 0)
- Manual Trigger → Get Day Ago Unix Time (`main`, output 0, input 0)
- Manual Trigger → WatchList (`main`, output 0, input 0)
- Get Day Ago Unix Time → Merge (`main`, output 0, input 0)
- WatchList → Merge (`main`, output 0, input 1)
- Merge → Loop Over Entities (`main`, output 0, input 0)
- HTTP Request → Merge1 (`main`, output 0, input 0)
- Loop Over Entities → Code in Python (`main`, output 0, input 0)
- Loop Over Entities → Entity Term Pair (`main`, output 1, input 0)
- Entity Term Pair → Call 'HackerNews' (`main`, output 0, input 0)
- When Executed by Another Workflow → HTTP Request (`main`, output 0, input 0)
- When Executed by Another Workflow → Merge1 (`main`, output 0, input 1)
- Call 'HackerNews' → Get Metrics (`main`, output 0, input 0)
- Get Metrics → Loop Over Entities (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
