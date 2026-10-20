# 💻 Schedule workflow activity time

This folder contains the **💻 Schedule workflow activity time** workflow. Its executable nodes use `merge`, `n8n`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`schedule-workflow-activity-time.json`](schedule-workflow-activity-time.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** Activate at 08:00 daily, Deactivate at 20:00 daily

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| n8n Activate | `n8n` | activate |
| n8n Deactivate | `n8n` | deactivate |
| Workflow ID | `set` | Inspect parameters |
| Merge in Workflow ID for deactivation | `merge` | Inspect parameters |
| Merge in Workflow ID for activation | `merge` | Inspect parameters |
| Activate at 08:00 daily | `scheduleTrigger` | Inspect parameters |
| Deactivate at 20:00 daily | `scheduleTrigger` | Inspect parameters |

## Connection map

- Workflow ID → Merge in Workflow ID for activation (`main`, output 0, input 1)
- Workflow ID → Merge in Workflow ID for deactivation (`main`, output 0, input 0)
- Activate at 08:00 daily → Workflow ID (`main`, output 0, input 0)
- Activate at 08:00 daily → Merge in Workflow ID for activation (`main`, output 0, input 0)
- Deactivate at 20:00 daily → Workflow ID (`main`, output 0, input 0)
- Deactivate at 20:00 daily → Merge in Workflow ID for deactivation (`main`, output 0, input 1)
- Merge in Workflow ID for activation → n8n Activate (`main`, output 0, input 0)
- Merge in Workflow ID for deactivation → n8n Deactivate (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1820_Schedule_N8N_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1820_Schedule_N8N_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
