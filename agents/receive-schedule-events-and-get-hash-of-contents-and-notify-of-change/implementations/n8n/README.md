# receive schedule events and get hash of contents and notify of change

This folder contains the **receive schedule events and get hash of contents and notify of change** workflow. Its executable nodes use `crypto`, `gmail`, `googleDrive`, `googleSheets`, `html`, `httpRequest`, `markdown`, `removeDuplicates`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-get-hash-of-contents-and-notify-of-change.json`](receive-schedule-events-and-get-hash-of-contents-and-notify-of-change.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Hash of Contents | `crypto` | Inspect parameters |
| Notify of Change | `gmail` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Variables | `set` | Inspect parameters |
| Only New Hashes | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Log Record | `googleSheets` | append |
| Fetch Webpage | `httpRequest` | Inspect parameters |
| Extract Contents | `html` | extractHtmlContent |
| Take a Snapshot | `googleDrive` | createFromText |

## Connection map

- Markdown → Get Hash of Contents (`main`, output 0, input 0)
- Variables → Fetch Webpage (`main`, output 0, input 0)
- Log Record → Notify of Change (`main`, output 0, input 0)
- Fetch Webpage → Extract Contents (`main`, output 0, input 0)
- Only New Hashes → Take a Snapshot (`main`, output 0, input 0)
- Take a Snapshot → Log Record (`main`, output 0, input 0)
- Extract Contents → Markdown (`main`, output 0, input 0)
- Schedule Trigger → Variables (`main`, output 0, input 0)
- Get Hash of Contents → Only New Hashes (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0817_Schedule_Removeduplicates_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0817_Schedule_Removeduplicates_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
