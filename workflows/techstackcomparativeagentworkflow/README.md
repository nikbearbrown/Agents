# TechStackComparativeAgentWorkflow

This folder contains the **TechStackComparativeAgentWorkflow** workflow. Its executable nodes use `code`, `convertToFile`, `httpRequest`, `if`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`techstackcomparativeagentworkflow.json`](techstackcomparativeagentworkflow.json): sanitized, inactive import copy with an overview sticky note.
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
| Validate Input | `if` | Inspect parameters |
| Prepare Variables | `set` | Inspect parameters |
| GitHub: Get Repos | `httpRequest` | Inspect parameters |
| Batch Repos (Top 5) | `splitInBatches` | Inspect parameters |
| GitHub: Get Languages | `httpRequest` | Inspect parameters |
| Aggregate Repo Data | `set` | Inspect parameters |
| arXiv: Search Papers | `httpRequest` | Inspect parameters |
| Error: Invalid Input | `set` | Inspect parameters |
| Parse arXiv XML | `code` | Inspect parameters |
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| set | `set` | Inspect parameters |
| set1 | `set` | Inspect parameters |
| Convert to File | `convertToFile` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |

## Connection map

- Validate Input → Prepare Variables (`main`, output 0, input 0)
- Validate Input → Error: Invalid Input (`main`, output 1, input 0)
- Prepare Variables → GitHub: Get Repos (`main`, output 0, input 0)
- Prepare Variables → arXiv: Search Papers (`main`, output 0, input 0)
- GitHub: Get Repos → Edit Fields2 (`main`, output 0, input 0)
- Batch Repos (Top 5) → GitHub: Get Languages (`main`, output 0, input 0)
- Batch Repos (Top 5) → Aggregate Repo Data (`main`, output 0, input 0)
- GitHub: Get Languages → Aggregate Repo Data (`main`, output 0, input 0)
- Aggregate Repo Data → Batch Repos (Top 5) (`main`, output 0, input 0)
- Aggregate Repo Data → Edit Fields (`main`, output 0, input 0)
- arXiv: Search Papers → Parse arXiv XML (`main`, output 0, input 0)
- Parse arXiv XML → Edit Fields1 (`main`, output 0, input 0)
- When clicking ‘Execute workflow’ → set1 (`main`, output 0, input 0)
- Split Out → Validate Input (`main`, output 0, input 0)
- set → Split Out (`main`, output 0, input 0)
- set1 → set (`main`, output 0, input 0)
- Edit Fields → Code (`main`, output 0, input 0)
- Edit Fields1 → Code (`main`, output 0, input 0)
- Code → Convert to File (`main`, output 0, input 0)
- Edit Fields2 → Batch Repos (Top 5) (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
