# receive execute workflow events and n8n and http request

This folder contains the **receive execute workflow events and n8n and http request** workflow. Its executable nodes use `code`, `executeWorkflow`, `executeWorkflowTrigger`, `github`, `httpRequest`, `if`, `manualTrigger`, `merge`, `n8n`, `noOp`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-execute-workflow-events-and-n8n-and-http-request.json`](receive-execute-workflow-events-and-n8n-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** On clicking 'execute', Execute Workflow Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| Return | `set` | Inspect parameters |
| Get File | `httpRequest` | Inspect parameters |
| If file too large | `if` | Inspect parameters |
| Merge Items | `merge` | Inspect parameters |
| isDiffOrNew | `code` | Inspect parameters |
| Check Status | `switch` | Inspect parameters |
| Same file - Do nothing | `noOp` | Inspect parameters |
| File is different | `noOp` | Inspect parameters |
| File is new | `noOp` | Inspect parameters |
| Create new file | `github` | file |
| Edit existing file | `github` | file / edit |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Create sub path | `set` | Inspect parameters |
| Starting Message | `slack` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Completed Notification | `slack` | Inspect parameters |
| Failed Flows | `slack` | Inspect parameters |
| Get file data | `github` | file / get |
| Config | `set` | Inspect parameters |

## Connection map

- n8n → Loop Over Items (`main`, output 0, input 0)
- Config → Get file data (`main`, output 0, input 0)
- Config → Merge Items (`main`, output 0, input 1)
- Get File → Merge Items (`main`, output 0, input 0)
- File is new → Create new file (`main`, output 0, input 0)
- Merge Items → isDiffOrNew (`main`, output 0, input 0)
- isDiffOrNew → Create sub path (`main`, output 0, input 0)
- Check Status → Same file - Do nothing (`main`, output 0, input 0)
- Check Status → File is different (`main`, output 1, input 0)
- Check Status → File is new (`main`, output 2, input 0)
- Failed Flows → Loop Over Items (`main`, output 0, input 0)
- Get file data → If file too large (`main`, output 0, input 0)
- Create new file → Return (`main`, output 0, input 0)
- Create sub path → Check Status (`main`, output 0, input 0)
- Loop Over Items → Completed Notification (`main`, output 0, input 0)
- Loop Over Items → Execute Workflow (`main`, output 1, input 0)
- Execute Workflow → Loop Over Items (`main`, output 0, input 0)
- Execute Workflow → Failed Flows (`main`, output 1, input 0)
- Schedule Trigger → Starting Message (`main`, output 0, input 0)
- Starting Message → n8n (`main`, output 0, input 0)
- File is different → Edit existing file (`main`, output 0, input 0)
- If file too large → Get File (`main`, output 0, input 0)
- If file too large → Merge Items (`main`, output 1, input 0)
- Edit existing file → Return (`main`, output 0, input 0)
- On clicking 'execute' → Starting Message (`main`, output 0, input 0)
- Same file - Do nothing → Return (`main`, output 0, input 0)
- Execute Workflow Trigger → Config (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0182_Code_GitHub_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0182_Code_GitHub_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
