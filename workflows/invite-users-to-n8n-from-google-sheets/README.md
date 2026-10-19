# Invite users to n8n from Google sheets

This folder contains the **Invite users to n8n from Google sheets** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `manualTrigger`, `merge`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`invite-users-to-n8n-from-google-sheets.json`](invite-users-to-n8n-from-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`, `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get all Users | `httpRequest` | Inspect parameters |
| Get all rows | `googleSheets` | Inspect parameters |
| Get non-users | `merge` | Inspect parameters |
| Invite Users | `httpRequest` | POST |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Create users list | `set` | Inspect parameters |
| Combine all paginated results | `code` | Inspect parameters |

## Connection map

- Edit Fields → Get all rows (`main`, output 0, input 0)
- Edit Fields → Get all Users (`main`, output 0, input 0)
- Get all rows → Get non-users (`main`, output 0, input 0)
- Get all Users → Combine all paginated results (`main`, output 0, input 0)
- Get non-users → Create users list (`main`, output 0, input 0)
- Schedule Trigger → Edit Fields (`main`, output 0, input 0)
- Create users list → Invite Users (`main`, output 0, input 0)
- Combine all paginated results → Get non-users (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0794_Code_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0794_Code_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
