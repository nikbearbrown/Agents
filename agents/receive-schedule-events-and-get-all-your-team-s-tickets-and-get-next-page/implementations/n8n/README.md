# receive schedule events and get all your team s tickets and get next page

This folder contains the **receive schedule events and get all your team s tickets and get next page** workflow. Its executable nodes use `code`, `googleSheets`, `graphql`, `if`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-get-all-your-team-s-tickets-and-get-next-page.json`](receive-schedule-events-and-get-all-your-team-s-tickets-and-get-next-page.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Every day at 06:00

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Every day at 06:00 | `scheduleTrigger` | Inspect parameters |
| Get all your team's tickets | `graphql` | Inspect parameters |
| if has next page | `if` | Inspect parameters |
| Get end cursor | `set` | Inspect parameters |
| Get next page | `graphql` | Inspect parameters |
| Split out the tickets | `splitOut` | Inspect parameters |
| Set custom fields | `set` | Inspect parameters |
| Write tickets to Sheets | `googleSheets` | appendOrUpdate |
| Flatten object to have simple fields to filter by | `code` | Inspect parameters |

## Connection map

- Get next page → if has next page (`main`, output 0, input 0)
- Get next page → Split out the tickets (`main`, output 0, input 0)
- Get end cursor → Get next page (`main`, output 0, input 0)
- if has next page → Get end cursor (`main`, output 0, input 0)
- Set custom fields → Flatten object to have simple fields to filter by (`main`, output 0, input 0)
- Every day at 06:00 → Get all your team's tickets (`main`, output 0, input 0)
- Split out the tickets → Set custom fields (`main`, output 0, input 0)
- Get all your team's tickets → Split out the tickets (`main`, output 0, input 0)
- Get all your team's tickets → if has next page (`main`, output 0, input 0)
- Flatten object to have simple fields to filter by → Write tickets to Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0445_Splitout_Code_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0445_Splitout_Code_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
