# Portfolio Price Fetcher

This folder contains the **Portfolio Price Fetcher** workflow. Its executable nodes use `code`, `httpRequest`, `manualTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`portfolio-price-fetcher.json`](portfolio-price-fetcher.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Define Portfolio | `code` | Inspect parameters |
| Fetch Stock Prices | `httpRequest` | Inspect parameters |
| Calculate Metrics | `code` | Inspect parameters |
| Aggregate Summary | `code` | Inspect parameters |

## Connection map

- Manual Trigger → Define Portfolio (`main`, output 0, input 0)
- Define Portfolio → Fetch Stock Prices (`main`, output 0, input 0)
- Fetch Stock Prices → Calculate Metrics (`main`, output 0, input 0)
- Calculate Metrics → Aggregate Summary (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
