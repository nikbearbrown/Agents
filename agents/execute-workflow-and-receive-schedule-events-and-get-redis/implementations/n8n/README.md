# execute workflow and receive schedule events and get redis

This folder contains the **execute workflow and receive schedule events and get redis** workflow. Its executable nodes use `executeWorkflow`, `filter`, `if`, `manualTrigger`, `noOp`, `redis`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`execute-workflow-and-receive-schedule-events-and-get-redis.json`](execute-workflow-and-receive-schedule-events-and-get-redis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `redis`

**Entry nodes:** Schedule Trigger, When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Status | `redis` | get |
| Set Running | `redis` | set |
| Set Idle | `redis` | set |
| Continue if Idle | `filter` | Inspect parameters |
| Redis Key exists | `if` | Inspect parameters |
| No Operation | `noOp` | Inspect parameters |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Reset to Idle | `redis` | set |

## Connection map

- Get Status → Redis Key exists (`main`, output 0, input 0)
- Set Running → Execute Workflow (`main`, output 0, input 0)
- No Operation → Set Running (`main`, output 0, input 0)
- Continue if Idle → Set Running (`main`, output 0, input 0)
- Execute Workflow → Set Idle (`main`, output 0, input 0)
- Redis Key exists → Continue if Idle (`main`, output 0, input 0)
- Redis Key exists → No Operation (`main`, output 1, input 0)
- Schedule Trigger → Get Status (`main`, output 0, input 0)
- When clicking "Test workflow" → Reset to Idle (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/0497_Redis_Schedule_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/0497_Redis_Schedule_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
