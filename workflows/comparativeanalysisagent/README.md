# ComparativeAnalysisAgent

This folder contains the **ComparativeAnalysisAgent** workflow. Its executable nodes use `aggregate`, `code`, `httpRequest`, `manualTrigger`, `merge`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`comparativeanalysisagent.json`](comparativeanalysisagent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Execute workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| Peer Company List | `code` | Inspect parameters |
| Subsector | `set` | Inspect parameters |
| Store Variables & Keys | `code` | Inspect parameters |
| Fetch Financial Overview | `httpRequest` | Inspect parameters |
| Fetch Financial Time Series | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Code in JavaScript | `code` | Inspect parameters |
| Loop - News | `splitInBatches` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Code in Python (Beta)1 | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| HTTP Request1 | `httpRequest` | Inspect parameters |
| Code in Python (Beta) | `code` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |

## Connection map

- When clicking ‘Execute workflow’ → Subsector (`main`, output 0, input 0)
- Subsector → Peer Company List (`main`, output 0, input 0)
- Peer Company List → Store Variables & Keys (`main`, output 0, input 0)
- Store Variables & Keys → Fetch Financial Overview (`main`, output 0, input 0)
- Store Variables & Keys → Fetch Financial Time Series (`main`, output 0, input 0)
- Store Variables & Keys → Loop - News (`main`, output 0, input 0)
- Store Variables & Keys → Loop Over Items (`main`, output 0, input 0)
- Fetch Financial Overview → Merge (`main`, output 0, input 0)
- Fetch Financial Time Series → Merge (`main`, output 0, input 1)
- Merge → Code in JavaScript (`main`, output 0, input 0)
- Loop - News → Aggregate1 (`main`, output 0, input 0)
- Loop - News → HTTP Request (`main`, output 1, input 0)
- HTTP Request → Code in Python (Beta)1 (`main`, output 0, input 0)
- Code in Python (Beta)1 → Loop - News (`main`, output 0, input 0)
- Loop Over Items → Aggregate (`main`, output 0, input 0)
- Loop Over Items → HTTP Request1 (`main`, output 1, input 0)
- HTTP Request1 → Code in Python (Beta) (`main`, output 0, input 0)
- Code in Python (Beta) → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
