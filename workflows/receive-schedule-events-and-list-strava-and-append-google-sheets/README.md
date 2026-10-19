# receive schedule events and list strava and append google sheets

This folder contains the **receive schedule events and list strava and append google sheets** workflow. Its executable nodes use `code`, `googleSheets`, `limit`, `removeDuplicates`, `scheduleTrigger`, `set`, `sort`, `strava`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-strava-and-append-google-sheets.json`](receive-schedule-events-and-list-strava-and-append-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Strava | `strava` | getAll |
| Code | `code` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| strava_last | `set` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| activities | `googleSheets` | Inspect parameters |
| sort_saved | `sort` | Inspect parameters |
| last_saved | `limit` | Inspect parameters |
| saved_last | `set` | Inspect parameters |
| sort_strava | `sort` | Inspect parameters |
| last_strava | `limit` | Inspect parameters |
| sort_results | `sort` | Inspect parameters |

## Connection map

- Code → sort_results (`main`, output 0, input 0)
- Strava → sort_strava (`main`, output 0, input 0)
- activities → sort_saved (`main`, output 0, input 0)
- last_saved → saved_last (`main`, output 0, input 0)
- saved_last → Strava (`main`, output 0, input 0)
- sort_saved → last_saved (`main`, output 0, input 0)
- last_strava → strava_last (`main`, output 0, input 0)
- sort_strava → Remove Duplicates (`main`, output 0, input 0)
- strava_last → Code (`main`, output 0, input 0)
- sort_results → Google Sheets (`main`, output 0, input 0)
- Schedule Trigger → activities (`main`, output 0, input 0)
- Remove Duplicates → last_strava (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0675_Limit_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0675_Limit_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
