# Retry Execution Hourly

This folder contains the **Retry Execution Hourly** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `n8n`, `noOp`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`retry-execution-hourly.json`](retry-execution-hourly.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| n8n | `n8n` | execution |
| Log into n8n | `httpRequest` | POST |
| retry workflow automatically | `httpRequest` | POST |
| If | `if` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| login_details | `set` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- If → No Operation, do nothing (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- n8n → If (`main`, output 0, input 0)
- Log into n8n → n8n (`main`, output 0, input 0)
- execution_id → retry workflow automatically (`main`, output 0, input 0)
- login_details → Log into n8n (`main`, output 0, input 0)
- Loop Over Items → execution_id (`main`, output 1, input 0)
- Schedule Trigger → login_details (`main`, output 0, input 0)
- retry workflow automatically → Loop Over Items (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → login_details (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_source": 1, "missing_connection_target": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1524_Schedule_Manual_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1524_Schedule_Manual_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
