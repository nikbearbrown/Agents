# AI Lead Generation & Enrichment (Outscraper + Gemini)

This folder contains the **AI Lead Generation & Enrichment (Outscraper + Gemini)** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-lead-generation-enrichment-outscraper-gemini.json`](ai-lead-generation-enrichment-outscraper-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`, `queryAuth`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Outscraper API | `httpRequest` | POST |
| Split Into Items | `splitOut` | Inspect parameters |
| Extract Lead Data | `set` | Inspect parameters |
| Gemini - Qualify Lead | `httpRequest` | POST |
| Parse AI Response | `code` | Inspect parameters |
| Gemini - Personalize Message | `httpRequest` | POST |
| Prepare Final Output | `code` | Inspect parameters |
| Google Sheets | `googleSheets` | appendOrUpdate |

## Connection map

- Schedule Trigger → Outscraper API (`main`, output 0, input 0)
- Outscraper API → Split Into Items (`main`, output 0, input 0)
- Split Into Items → Extract Lead Data (`main`, output 0, input 0)
- Extract Lead Data → Gemini - Qualify Lead (`main`, output 0, input 0)
- Gemini - Qualify Lead → Parse AI Response (`main`, output 0, input 0)
- Parse AI Response → Gemini - Personalize Message (`main`, output 0, input 0)
- Gemini - Personalize Message → Prepare Final Output (`main`, output 0, input 0)
- Prepare Final Output → Google Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/skadaai/awesome-n8n-templates/blob/4eabc190bf6fac4073e3e1dcaabf0f72897770eb/leadgen.json](https://github.com/skadaai/awesome-n8n-templates/blob/4eabc190bf6fac4073e3e1dcaabf0f72897770eb/leadgen.json). License: **MIT**; preserve [the notice](../../licenses/skadaai--awesome-n8n-templates.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
