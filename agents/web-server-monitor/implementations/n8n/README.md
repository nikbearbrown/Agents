# Web Server Monitor.

This folder contains the **Web Server Monitor.** workflow. Its executable nodes use `gmail`, `googleSheets`, `httpRequest`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`web-server-monitor.json`](web-server-monitor.json): sanitized, inactive import copy with an overview sticky note.
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
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Server-Monitor | `googleSheets` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Server_Status_Alive | `googleSheets` | append |
| Gmail | `gmail` | Inspect parameters |
| Server_Status_Down | `googleSheets` | append |

## Connection map

- Gmail → Server_Status_Down (`main`, output 0, input 0)
- HTTP Request → Server_Status_Alive (`main`, output 0, input 0)
- HTTP Request → Gmail (`main`, output 1, input 0)
- Server-Monitor → HTTP Request (`main`, output 0, input 0)
- Schedule Trigger → Server-Monitor (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1952_Schedule_HTTP_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1952_Schedule_HTTP_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
