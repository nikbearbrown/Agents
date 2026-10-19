# get portfolio from sheets and fetch live prices and call groq api

This folder contains the **get portfolio from sheets and fetch live prices and call groq api** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `manualTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-portfolio-from-sheets-and-fetch-live-prices-and-call-groq-api.json`](get-portfolio-from-sheets-and-fetch-live-prices-and-call-groq-api.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Get Portfolio from Sheets | `googleSheets` | Inspect parameters |
| Fetch Live Prices | `httpRequest` | Inspect parameters |
| Calculate Advanced Risk | `code` | Inspect parameters |
| Prepare for LLM | `code` | Inspect parameters |
| Call Groq API | `httpRequest` | POST |
| Format Report | `code` | Inspect parameters |
| Log to Sheets | `googleSheets` | append |

## Connection map

- Manual Trigger → Get Portfolio from Sheets (`main`, output 0, input 0)
- Get Portfolio from Sheets → Fetch Live Prices (`main`, output 0, input 0)
- Fetch Live Prices → Calculate Advanced Risk (`main`, output 0, input 0)
- Calculate Advanced Risk → Prepare for LLM (`main`, output 0, input 0)
- Prepare for LLM → Call Groq API (`main`, output 0, input 0)
- Call Groq API → Format Report (`main`, output 0, input 0)
- Format Report → Log to Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
