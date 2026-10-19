# Trigger workflow every 48 hours

This folder contains the **Trigger workflow every 48 hours** workflow. Its executable nodes use `cron`, `filter`, `httpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`trigger-workflow-every-48-hours.json`](trigger-workflow-every-48-hours.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** Runs every 48hrs

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter | `filter` | Inspect parameters |
| List Snapshots for a Droplet | `httpRequest` | Inspect parameters |
| List All Droplets | `httpRequest` | Inspect parameters |
| Delete a Snapshot | `httpRequest` | Inspect parameters |
| Droplet Actions snapshot (n8n.optimus01.co.za) | `httpRequest` | Inspect parameters |
| Runs every 48hrs | `cron` | Inspect parameters |

## Connection map

- Filter → Delete a Snapshot (`main`, output 0, input 0)
- Runs every 48hrs → List All Droplets (`main`, output 0, input 0)
- Delete a Snapshot → Droplet Actions snapshot (n8n.optimus01.co.za) (`main`, output 0, input 0)
- List All Droplets → List Snapshots for a Droplet (`main`, output 0, input 0)
- List Snapshots for a Droplet → Filter (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0611_HTTP_Filter_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0611_HTTP_Filter_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
