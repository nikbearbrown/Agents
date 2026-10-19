# AI News & Sentiment Agent

This folder contains the **AI News & Sentiment Agent** workflow. Its executable nodes use `airtable`, `code`, `emailSend`, `filter`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-news-sentiment-agent.json`](ai-news-sentiment-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `smtp`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Edit Fields | `set` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Create a record | `airtable` | create |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |
| Filter | `filter` | Inspect parameters |

## Connection map

- Edit Fields → HTTP Request (`main`, output 0, input 0)
- HTTP Request → Split Out (`main`, output 0, input 0)
- Split Out → Code (`main`, output 0, input 0)
- Code → Create a record (`main`, output 0, input 0)
- Schedule Trigger → Edit Fields (`main`, output 0, input 0)
- Create a record → Filter (`main`, output 0, input 0)
- Filter → Send email (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
