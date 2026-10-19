# Prevent concurrent workflow runs using Redis

This folder contains the **Prevent concurrent workflow runs using Redis** workflow. Its executable nodes use `executeWorkflow`, `executeWorkflowTrigger`, `if`, `manualTrigger`, `noOp`, `redis`, `set`, `stopAndError`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`prevent-concurrent-workflow-runs-using-redis.json`](prevent-concurrent-workflow-runs-using-redis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `redis`

**Entry nodes:** When Executed by Another Workflow, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| Is Workflow Active | `executeWorkflow` | Inspect parameters |
| Set Workflow Active | `executeWorkflow` | Inspect parameters |
| Set Workflow Finished | `executeWorkflow` | Inspect parameters |
| Get Key | `redis` | get |
| Set Key | `redis` | set |
| UnSet Key | `redis` | delete |
| Set Timeout | `set` | Inspect parameters |
| set continue | `set` | Inspect parameters |
| If | `if` | Inspect parameters |
| Is Workflow Active1 | `executeWorkflow` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Set Workflow Active1 | `executeWorkflow` | Inspect parameters |
| Set Workflow Finished1 | `executeWorkflow` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Is Workflow Active2 | `executeWorkflow` | Inspect parameters |
| Stop and Error1 | `stopAndError` | Inspect parameters |
| Set Workflow Finished2 | `executeWorkflow` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| Wait3 | `wait` | Inspect parameters |
| Set Workflow "started" | `executeWorkflow` | Inspect parameters |
| Set Workflow "finishing" | `executeWorkflow` | Inspect parameters |
| Set Workflow "loading" | `executeWorkflow` | Inspect parameters |
| Is Workflow Active3 | `executeWorkflow` | Inspect parameters |
| Switch1 | `switch` | Inspect parameters |

## Connection map

- If → Set Workflow Active1 (`main`, output 0, input 0)
- If → Stop and Error (`main`, output 1, input 0)
- If1 → Set Workflow "started" (`main`, output 0, input 0)
- If1 → Stop and Error1 (`main`, output 1, input 0)
- Wait → Set Workflow Finished1 (`main`, output 0, input 0)
- Wait1 → Set Workflow "loading" (`main`, output 0, input 0)
- Wait2 → Set Workflow "finishing" (`main`, output 0, input 0)
- Wait3 → Set Workflow Finished2 (`main`, output 0, input 0)
- Switch → Get Key (`main`, output 0, input 0)
- Switch → Set Key (`main`, output 1, input 0)
- Switch → UnSet Key (`main`, output 2, input 0)
- Set Key → set continue (`main`, output 0, input 0)
- UnSet Key → set continue (`main`, output 0, input 0)
- Set Timeout → Switch (`main`, output 0, input 0)
- Is Workflow Active → If2 (`main`, output 0, input 0)
- Is Workflow Active1 → If (`main`, output 0, input 0)
- Is Workflow Active2 → If1 (`main`, output 0, input 0)
- Is Workflow Active3 → Switch1 (`main`, output 0, input 0)
- Set Workflow Active1 → No Operation, do nothing (`main`, output 0, input 0)
- Set Workflow "loading" → Wait2 (`main`, output 0, input 0)
- Set Workflow "started" → Wait1 (`main`, output 0, input 0)
- No Operation, do nothing → Wait (`main`, output 0, input 0)
- Set Workflow "finishing" → Wait3 (`main`, output 0, input 0)
- When Executed by Another Workflow → Set Timeout (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0925_Stopanderror_Wait_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0925_Stopanderror_Wait_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
