# MONDAY GET FULL ITEM

This folder contains the **MONDAY GET FULL ITEM** workflow. Its executable nodes use `aggregate`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `merge`, `mondayCom`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`monday-get-full-item.json`](monday-get-full-item.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mondayComApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| GET ALL COLUMNS | `code` | Inspect parameters |
| GET ALL RELATIONS | `code` | Inspect parameters |
| PULL LINKEDPULSE1 | `mondayCom` | boardItem / get |
| GET LINKEDPULSES1 | `code` | Inspect parameters |
| SPLIT LINKED PULSES1 | `splitOut` | Inspect parameters |
| SPLIT SUBITEMS1 | `splitOut` | Inspect parameters |
| GET EACH SUBITEM1 | `mondayCom` | boardItem / get |
| GET ALL COLUMNS1 | `code` | Inspect parameters |
| GET ALL COLUMNS2 | `code` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| PULL SUBITEMS | `code` | Inspect parameters |
| GET ITEM | `mondayCom` | boardItem / get |
| GET ALL COLUMNS3 | `code` | Inspect parameters |
| Merge4 | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- Merge → Merge1 (`main`, output 0, input 1)
- Merge2 → Merge1 (`main`, output 0, input 0)
- Merge4 → Aggregate (`main`, output 0, input 0)
- GET ITEM → GET ALL COLUMNS (`main`, output 0, input 0)
- GET ITEM → GET ALL COLUMNS2 (`main`, output 0, input 0)
- GET ITEM → PULL SUBITEMS (`main`, output 0, input 0)
- Aggregate → Merge (`main`, output 0, input 0)
- Aggregate1 → Merge (`main`, output 0, input 1)
- Edit Fields → Execute Workflow (`main`, output 0, input 0)
- PULL SUBITEMS → SPLIT SUBITEMS1 (`main`, output 0, input 0)
- GET ALL COLUMNS → GET ALL RELATIONS (`main`, output 0, input 0)
- GET ALL COLUMNS → Merge2 (`main`, output 0, input 0)
- SPLIT SUBITEMS1 → GET EACH SUBITEM1 (`main`, output 0, input 0)
- GET ALL COLUMNS1 → Aggregate1 (`main`, output 0, input 0)
- GET ALL COLUMNS2 → Merge2 (`main`, output 0, input 1)
- GET ALL COLUMNS3 → Merge4 (`main`, output 0, input 1)
- GET ALL RELATIONS → GET LINKEDPULSES1 (`main`, output 0, input 0)
- GET ALL RELATIONS → Merge4 (`main`, output 0, input 0)
- GET EACH SUBITEM1 → GET ALL COLUMNS1 (`main`, output 0, input 0)
- GET LINKEDPULSES1 → SPLIT LINKED PULSES1 (`main`, output 0, input 0)
- PULL LINKEDPULSE1 → GET ALL COLUMNS3 (`main`, output 0, input 0)
- SPLIT LINKED PULSES1 → PULL LINKEDPULSE1 (`main`, output 0, input 0)
- Execute Workflow Trigger → GET ITEM (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1781_Mondaycom_Splitout_Import_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1781_Mondaycom_Splitout_Import_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
