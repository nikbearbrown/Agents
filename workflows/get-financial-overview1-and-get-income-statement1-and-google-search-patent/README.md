# My workflow

This folder contains the **My workflow** workflow. Its executable nodes use `code`, `httpRequest`, `manualTrigger`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-financial-overview1-and-get-income-statement1-and-google-search-patent.json`](get-financial-overview1-and-get-income-statement1-and-google-search-patent.json): sanitized, inactive import copy with an overview sticky note.
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
| Code in Python (Beta) | `code` | Inspect parameters |
| Company Input | `set` | Inspect parameters |
| Get Financial Overview1 | `httpRequest` | Inspect parameters |
| Get Income Statement1 | `httpRequest` | Inspect parameters |
| Process Company Data1 | `code` | Inspect parameters |
| Google Search Patent | `httpRequest` | Inspect parameters |
| Process Patent Data1 | `code` | Inspect parameters |
| Process Financial Data1 | `code` | Inspect parameters |
| Generate Analysis1 | `code` | Inspect parameters |
| Generate Final Report1 | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |

## Connection map

- When clicking ‘Execute workflow’ → Company Input (`main`, output 0, input 0)
- Company Input → Get Financial Overview1 (`main`, output 0, input 0)
- Company Input → Get Income Statement1 (`main`, output 0, input 0)
- Get Financial Overview1 → Process Company Data1 (`main`, output 0, input 0)
- Get Income Statement1 → Process Financial Data1 (`main`, output 0, input 0)
- Process Company Data1 → Google Search Patent (`main`, output 0, input 0)
- Google Search Patent → Process Patent Data1 (`main`, output 0, input 0)
- Process Patent Data1 → Merge (`main`, output 0, input 0)
- Process Financial Data1 → Merge (`main`, output 0, input 1)
- Generate Analysis1 → Generate Final Report1 (`main`, output 0, input 0)
- Generate Final Report1 → Code in Python (Beta) (`main`, output 0, input 0)
- Merge → Generate Analysis1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
