# receive schedule events and get all emails in the last day and get thread gmail

This folder contains the **receive schedule events and get all emails in the last day and get thread gmail** workflow. Its executable nodes use `filter`, `gmail`, `itemLists`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-get-all-emails-in-the-last-day-and-get-thread-gmail.json`](receive-schedule-events-and-get-all-emails-in-the-last-day-and-get-thread-gmail.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** At midnight every work day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| At midnight every work day | `scheduleTrigger` | Inspect parameters |
| Get all emails in the last day | `gmail` | thread |
| Get the thread of each email | `gmail` | thread / get |
| Keep only starred emails in inbox | `filter` | Inspect parameters |
| for each message in the thread | `itemLists` | Inspect parameters |
| Archive message (remove from inbox) | `gmail` | removeLabels |
| Archive thread  (remove from inbox) | `gmail` | thread / removeLabels |

## Connection map

- At midnight every work day → Get all emails in the last day (`main`, output 0, input 0)
- Get the thread of each email → Keep only starred emails in inbox (`main`, output 0, input 0)
- Get all emails in the last day → Get the thread of each email (`main`, output 0, input 0)
- for each message in the thread → Archive message (remove from inbox) (`main`, output 0, input 0)
- Keep only starred emails in inbox → Archive thread  (remove from inbox) (`main`, output 0, input 0)
- Keep only starred emails in inbox → for each message in the thread (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0443_Schedule_Filter_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0443_Schedule_Filter_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
