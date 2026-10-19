# Funding Intelligence Agent

This folder contains the **Funding Intelligence Agent** workflow. Its executable nodes use `code`, `emailSend`, `googleSheets`, `html`, `httpRequest`, `merge`, `postgres`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`funding-intelligence-agent.json`](funding-intelligence-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpBasicAuth`, `httpHeaderAuth`, `postgres`, `smtp`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Zyte_TechCrunch_Scraper | `httpRequest` | POST |
| HTML | `html` | extractHtmlContent |
| Zyte_VentureBeat | `httpRequest` | POST |
| Decode_VB | `code` | Inspect parameters |
| Decode_TC | `code` | Inspect parameters |
| HTML1 | `html` | extractHtmlContent |
| Merge | `merge` | Inspect parameters |
| Filter and split VB | `code` | Inspect parameters |
| Filter and split tech_crunch | `code` | Inspect parameters |
| Filter_Funding_Keywords | `code` | Inspect parameters |
| Classify_Industry | `code` | Inspect parameters |
| Execute a SQL query | `postgres` | executeQuery |
| Insert rows in a table | `postgres` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |
| Append row in sheet | `googleSheets` | append |

## Connection map

- Schedule Trigger → Zyte_TechCrunch_Scraper (`main`, output 0, input 0)
- Schedule Trigger → Zyte_VentureBeat (`main`, output 0, input 0)
- Zyte_TechCrunch_Scraper → Decode_TC (`main`, output 0, input 0)
- HTML → Filter and split tech_crunch (`main`, output 0, input 0)
- Zyte_VentureBeat → Decode_VB (`main`, output 0, input 0)
- Decode_TC → HTML (`main`, output 0, input 0)
- Decode_VB → HTML1 (`main`, output 0, input 0)
- HTML1 → Filter and split VB (`main`, output 0, input 0)
- Filter and split VB → Merge (`main`, output 0, input 0)
- Filter and split tech_crunch → Merge (`main`, output 0, input 1)
- Merge → Filter_Funding_Keywords (`main`, output 0, input 0)
- Filter_Funding_Keywords → Classify_Industry (`main`, output 0, input 0)
- Classify_Industry → Insert rows in a table (`main`, output 0, input 0)
- Insert rows in a table → Append row in sheet (`main`, output 0, input 0)
- Insert rows in a table → Send email (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
