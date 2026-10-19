# airflow dag_run

This folder contains the **airflow dag_run** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `httpRequest`, `if`, `set`, `stopAndError`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`airflow-dag-run.json`](airflow-dag-run.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`

**Entry nodes:** in data

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Airflow: dag_run | `httpRequest` | POST |
| Airflow: dag_run - state | `httpRequest` | Inspect parameters |
| count | `code` | Inspect parameters |
| dag run fail | `stopAndError` | Inspect parameters |
| if state == queued | `if` | Inspect parameters |
| dag run wait too long | `stopAndError` | Inspect parameters |
| Airflow: dag_run - get result | `httpRequest` | Inspect parameters |
| Switch: state | `switch` | Inspect parameters |
| in data | `executeWorkflowTrigger` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| If count > wait_time | `if` | Inspect parameters |
| airflow-api | `set` | Inspect parameters |

## Connection map

- Wait → Airflow: dag_run - state (`main`, output 0, input 0)
- count → If count > wait_time (`main`, output 0, input 0)
- in data → airflow-api (`main`, output 0, input 0)
- airflow-api → Airflow: dag_run (`main`, output 0, input 0)
- Switch: state → Airflow: dag_run - get result (`main`, output 0, input 0)
- Switch: state → count (`main`, output 1, input 0)
- Switch: state → count (`main`, output 2, input 0)
- Switch: state → dag run fail (`main`, output 3, input 0)
- Airflow: dag_run → if state == queued (`main`, output 0, input 0)
- if state == queued → Wait (`main`, output 0, input 0)
- if state == queued → dag run fail (`main`, output 1, input 0)
- If count > wait_time → dag run wait too long (`main`, output 0, input 0)
- If count > wait_time → Wait (`main`, output 1, input 0)
- Airflow: dag_run - state → Switch: state (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1768_Stopanderror_Wait_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1768_Stopanderror_Wait_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
