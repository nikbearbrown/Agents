# FORECASTING

This folder contains the **FORECASTING** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `if`, `manualTrigger`, `merge`, `postgres`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`market-data-and-sentiment-forecast-review.json`](market-data-and-sentiment-forecast-review.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`, `smtp`

**Entry nodes:** When clicking ‘Execute workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Alpha Vantage Market Data | `httpRequest` | Inspect parameters |
| Configuration | `set` | Inspect parameters |
| FinBert | `httpRequest` | POST |
| Merge | `merge` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| Code2 | `code` | Inspect parameters |
| Execute a SQL query | `postgres` | executeQuery |
| Edit Fields | `set` | Inspect parameters |
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| Insert rows in a table | `postgres` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |
| Historical data | `code` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- Alpha Vantage Market Data → Merge (`main`, output 0, input 0)
- Configuration → FinBert (`main`, output 0, input 0)
- Configuration → Historical data (`main`, output 0, input 0)
- Configuration → Alpha Vantage Market Data (`main`, output 0, input 0)
- FinBert → Merge (`main`, output 0, input 2)
- Merge → Code1 (`main`, output 0, input 0)
- Code1 → If (`main`, output 0, input 0)
- If → Code2 (`main`, output 0, input 0)
- If → Edit Fields (`main`, output 1, input 0)
- Code2 → Insert rows in a table (`main`, output 0, input 0)
- Edit Fields → Send email (`main`, output 0, input 0)
- When clicking ‘Execute workflow’ → Code (`main`, output 0, input 0)
- Historical data → Merge (`main`, output 0, input 1)
- Code → Configuration (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
