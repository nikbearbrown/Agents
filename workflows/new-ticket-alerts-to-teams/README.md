# New Ticket Alerts to Teams

This folder contains the **New Ticket Alerts to Teams** workflow. Its executable nodes use `code`, `httpRequest`, `merge`, `microsoftTeams`, `redis`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`new-ticket-alerts-to-teams.json`](new-ticket-alerts-to-teams.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `microsoftTeamsOAuth2Api`, `redis`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Add Filterable Parameter | `code` | Inspect parameters |
| Query Database | `redis` | get |
| Filter Out Tickets that have already been sent | `merge` | Inspect parameters |
| Get New Tickets | `httpRequest` | Inspect parameters |
| Combine like Companies | `code` | Inspect parameters |
| Teams to Dispatch | `microsoftTeams` | chatMessage |
| Log in Redis | `redis` | set |

## Connection map

- Query Database → Filter Out Tickets that have already been sent (`main`, output 0, input 1)
- Get New Tickets → Query Database (`main`, output 0, input 0)
- Get New Tickets → Add Filterable Parameter (`main`, output 0, input 0)
- Schedule Trigger → Get New Tickets (`main`, output 0, input 0)
- Combine like Companies → Teams to Dispatch (`main`, output 0, input 0)
- Add Filterable Parameter → Filter Out Tickets that have already been sent (`main`, output 0, input 0)
- Filter Out Tickets that have already been sent → Combine like Companies (`main`, output 0, input 0)
- Filter Out Tickets that have already been sent → Log in Redis (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/1933_Redis_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/1933_Redis_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
