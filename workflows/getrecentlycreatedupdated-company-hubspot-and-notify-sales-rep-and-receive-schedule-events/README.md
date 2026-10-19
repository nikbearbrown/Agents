# getrecentlycreatedupdated company hubspot and notify sales rep and receive schedule events

This folder contains the **getrecentlycreatedupdated company hubspot and notify sales rep and receive schedule events** workflow. Its executable nodes use `filter`, `hubspot`, `scheduleTrigger`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`getrecentlycreatedupdated-company-hubspot-and-notify-sales-rep-and-receive-schedule-events.json`](getrecentlycreatedupdated-company-hubspot-and-notify-sales-rep-and-receive-schedule-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`, `slackOAuth2Api`

**Entry nodes:** Trigger every 5 minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get leads created last 5 minutes | `hubspot` | company / getRecentlyCreatedUpdated |
| Notify sales rep | `slack` | Inspect parameters |
| Trigger every 5 minutes | `scheduleTrigger` | Inspect parameters |
| Keep the ones that make more than $5M in revenue | `filter` | Inspect parameters |

## Connection map

- Trigger every 5 minutes → Get leads created last 5 minutes (`main`, output 0, input 0)
- Get leads created last 5 minutes → Keep the ones that make more than $5M in revenue (`main`, output 0, input 0)
- Keep the ones that make more than $5M in revenue → Notify sales rep (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0432_Schedule_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0432_Schedule_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
