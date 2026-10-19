# Mycroft News Intelligence Agent

This folder contains the **Mycroft News Intelligence Agent** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `manualTrigger`, `merge`, `postgres`, `set`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-news-intelligence-agent.json`](mycroft-news-intelligence-agent.json): sanitized, inactive import copy with an overview sticky note.
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
| Company List | `code` | Inspect parameters |
| Build Query | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| normalizenewsapi | `code` | Inspect parameters |
| NewsApiKey | `httpRequest` | Inspect parameters |
| When clicking ‘Execute workflow’ | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| XML | `xml` | Inspect parameters |
| ProcessNewData | `code` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| HTTP Request1 | `httpRequest` | POST |
| RiskCalculator | `code` | Inspect parameters |
| Insert rows in a table | `postgres` | Inspect parameters |
| Alert Generator Code Node | `code` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |
| DailyGeneratorCode | `code` | Inspect parameters |

## Connection map

- Company List → Build Query (`main`, output 0, input 0)
- Build Query → HTTP Request (`main`, output 0, input 0)
- Build Query → NewsApiKey (`main`, output 0, input 0)
- normalizenewsapi → Merge (`main`, output 0, input 0)
- NewsApiKey → ProcessNewData (`main`, output 0, input 0)
- HTTP Request → XML (`main`, output 0, input 0)
- Merge → HTTP Request1 (`main`, output 0, input 0)
- XML → Edit Fields (`main`, output 0, input 0)
- When clicking ‘Execute workflow’ → Company List (`main`, output 0, input 0)
- ProcessNewData → normalizenewsapi (`main`, output 0, input 0)
- Edit Fields → Merge (`main`, output 0, input 1)
- HTTP Request1 → RiskCalculator (`main`, output 0, input 0)
- RiskCalculator → Insert rows in a table (`main`, output 0, input 0)
- Insert rows in a table → Alert Generator Code Node (`main`, output 0, input 0)
- Alert Generator Code Node → Send email (`main`, output 0, input 0)
- Send email → DailyGeneratorCode (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
