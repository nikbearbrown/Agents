# Automating Betting Data Retrieval with TheOddsAPI and Airtable

This folder contains the **Automating Betting Data Retrieval with TheOddsAPI and Airtable** workflow. Its executable nodes use `airtable`, `httpRequest`, `merge`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automating-betting-data-retrieval-with-theoddsapi-and-airtable.json`](automating-betting-data-retrieval-with-theoddsapi-and-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`

**Entry nodes:** Morning Trigger To Pull Data At 7:00am, Evening Trigger To Pull Data At 11:00pm

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Morning Trigger To Pull Data At 7:00am | `scheduleTrigger` | Inspect parameters |
| Evening Trigger To Pull Data At 11:00pm | `scheduleTrigger` | Inspect parameters |
| Retrieve Data Of Upcoming Sport Events For The Day | `httpRequest` | Inspect parameters |
| Create Records Of Upcoming Events For The Day | `airtable` | create |
| Retrieve Sport Results Data At The End Of The Day | `httpRequest` | Inspect parameters |
| Combine Sport Results With Upcoming Events Records By Matching ID | `merge` | Inspect parameters |
| Update Table Records With Scores And Results For Sport Events | `airtable` | update |

## Connection map

- Morning Trigger To Pull Data At 7:00am → Retrieve Data Of Upcoming Sport Events For The Day (`main`, output 0, input 0)
- Evening Trigger To Pull Data At 11:00pm → Retrieve Sport Results Data At The End Of The Day (`main`, output 0, input 0)
- Retrieve Sport Results Data At The End Of The Day → Combine Sport Results With Upcoming Events Records By Matching ID (`main`, output 0, input 1)
- Retrieve Data Of Upcoming Sport Events For The Day → Combine Sport Results With Upcoming Events Records By Matching ID (`main`, output 0, input 0)
- Retrieve Data Of Upcoming Sport Events For The Day → Create Records Of Upcoming Events For The Day (`main`, output 0, input 0)
- Combine Sport Results With Upcoming Events Records By Matching ID → Update Table Records With Scores And Results For Sport Events (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1111_HTTP_Schedule_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1111_HTTP_Schedule_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
