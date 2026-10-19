# Linear Project Status and End Date to Productboard feature Sync

This folder contains the **Linear Project Status and End Date to Productboard feature Sync** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `linearTrigger`, `merge`, `set`, `slack`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linear-project-status-and-end-date-to-productboard-feature-sync.json`](linear-project-status-and-end-date-to-productboard-feature-sync.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `linearApi`, `slackApi`

**Entry nodes:** Your Linear Project 2, Your Linear Project 1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| linear project id | `set` | Inspect parameters |
| get productboard feature id | `httpRequest` | Inspect parameters |
| update productboard status & timeframe | `httpRequest` | PATCH |
| map linear to productboard status | `set` | Inspect parameters |
| mapping | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| If | `if` | Inspect parameters |
| get productboard feature details | `httpRequest` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Your Linear Project 2 | `linearTrigger` | Inspect parameters |
| Your Linear Project 1 | `linearTrigger` | Inspect parameters |

## Connection map

- If → update productboard status & timeframe (`main`, output 0, input 0)
- Merge → Merge2 (`main`, output 0, input 0)
- Merge1 → map linear to productboard status (`main`, output 0, input 0)
- Merge1 → get productboard feature details (`main`, output 0, input 0)
- Merge2 → If (`main`, output 0, input 0)
- mapping → Merge (`main`, output 0, input 0)
- Split Out → Edit Fields (`main`, output 0, input 0)
- Edit Fields → Merge1 (`main`, output 0, input 1)
- linear project id → Merge1 (`main`, output 0, input 0)
- Your Linear Project 1 → get productboard feature id (`main`, output 0, input 0)
- Your Linear Project 1 → linear project id (`main`, output 0, input 0)
- Your Linear Project 2 → linear project id (`main`, output 0, input 0)
- Your Linear Project 2 → get productboard feature id (`main`, output 0, input 0)
- get productboard feature id → Split Out (`main`, output 0, input 0)
- get productboard feature details → Merge2 (`main`, output 0, input 1)
- map linear to productboard status → mapping (`main`, output 0, input 0)
- map linear to productboard status → Merge (`main`, output 0, input 1)
- update productboard status & timeframe → Slack (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0645_Splitout_Code_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0645_Splitout_Code_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
