# Retrieve Customer Messages Data (Google Sheets Node ):

This folder contains the **Retrieve Customer Messages Data (Google Sheets Node ):** workflow. Its executable nodes use `filter`, `gmail`, `googleSheets`, `merge`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`retrieve-customer-messages-data-google-sheets-node.json`](retrieve-customer-messages-data-google-sheets-node.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter Status (Waiting for sending) | `filter` | Inspect parameters |
| Set data | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Retrieve Customer Messages Data | `googleSheets` | Inspect parameters |
| Update Message Status | `googleSheets` | update |
| Send a message (Gmail) | `gmail` | Inspect parameters |
| Merge fields | `merge` | Inspect parameters |

## Connection map

- Set data → Update Message Status (`main`, output 0, input 0)
- Merge fields → Set data (`main`, output 0, input 0)
- Schedule Trigger → Retrieve Customer Messages Data (`main`, output 0, input 0)
- Send a message (Gmail) → Merge fields (`main`, output 0, input 0)
- Retrieve Customer Messages Data → Filter Status (Waiting for sending) (`main`, output 0, input 0)
- Filter Status (Waiting for sending) → Merge fields (`main`, output 0, input 1)
- Filter Status (Waiting for sending) → Send a message (Gmail) (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0402_Schedule_Filter_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0402_Schedule_Filter_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
