# My workflow 4

This folder contains the **My workflow 4** workflow. Its executable nodes use `code`, `httpRequest`, `manualTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`github-get-repos-and-github-get-languages-and-arxiv-search-papers.json`](github-get-repos-and-github-get-languages-and-arxiv-search-papers.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Prepare Variables | `set` | Inspect parameters |
| GitHub: Get Repos | `httpRequest` | Inspect parameters |
| Batch Repos | `splitInBatches` | Inspect parameters |
| GitHub: Get Languages | `httpRequest` | Inspect parameters |
| Aggregate Repo Data | `set` | Inspect parameters |
| arXiv: Search Papers | `httpRequest` | Inspect parameters |
| Parse arXiv XML | `code` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Input: Companies | `set` | Inspect parameters |
| Format Language Data | `set` | Inspect parameters |
| Format Research Data | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Code2 | `code` | Inspect parameters |
| Code3 | `code` | Inspect parameters |
| Code4 | `code` | Inspect parameters |
| Code5 | `code` | Inspect parameters |

## Connection map

- Prepare Variables → GitHub: Get Repos (`main`, output 0, input 0)
- Prepare Variables → arXiv: Search Papers (`main`, output 0, input 0)
- GitHub: Get Repos → Code3 (`main`, output 0, input 0)
- Batch Repos → GitHub: Get Languages (`main`, output 0, input 0)
- Batch Repos → Aggregate Repo Data (`main`, output 0, input 0)
- Batch Repos → Code5 (`main`, output 1, input 0)
- GitHub: Get Languages → Format Language Data (`main`, output 0, input 0)
- Format Language Data → Code4 (`main`, output 0, input 0)
- Aggregate Repo Data → Batch Repos (`main`, output 0, input 0)
- arXiv: Search Papers → Parse arXiv XML (`main`, output 0, input 0)
- Parse arXiv XML → Format Research Data (`main`, output 0, input 0)
- Format Research Data → Code5 (`main`, output 0, input 0)
- Manual Trigger → Input: Companies (`main`, output 0, input 0)
- Input: Companies → Code (`main`, output 0, input 0)
- Code → Prepare Variables (`main`, output 0, input 0)
- Code1 → Batch Repos (`main`, output 0, input 0)
- Code3 → Code1 (`main`, output 0, input 0)
- Code5 → Code2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
