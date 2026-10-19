# Log errors and avoid sending too many emails

This folder contains the **Log errors and avoid sending too many emails** workflow. Its executable nodes use `code`, `emailSend`, `errorTrigger`, `executeWorkflow`, `executeWorkflowTrigger`, `if`, `manualTrigger`, `noOp`, `postgres`, `pushover`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`log-errors-and-avoid-sending-too-many-emails.json`](log-errors-and-avoid-sending-too-many-emails.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`, `pushoverApi`, `smtp`

**Entry nodes:** Error Trigger, Sometimes... just cleanup, See below to prepend this at your error handling

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Error Trigger | `errorTrigger` | Inspect parameters |
| Insert Log | `postgres` | Inspect parameters |
| Count for 5 minutes | `postgres` | executeQuery |
| Principal E-Mail | `emailSend` | Inspect parameters |
| Fallback E-Mail | `emailSend` | Inspect parameters |
| Push mobile notification | `pushover` | Inspect parameters |
| Truncate Log Database | `postgres` | deleteTable |
| Sometimes... just cleanup | `manualTrigger` | Inspect parameters |
| Call this Sample - Prepend to your error catcher | `executeWorkflow` | Inspect parameters |
| See below to prepend this at your error handling | `executeWorkflowTrigger` | Inspect parameters |
| If there is no logs in 5 minutes | `if` | Inspect parameters |
| CleanUp execution. See below if you will prepend this workflow | `code` | Inspect parameters |
| Insert your error handling logic after this | `noOp` | Inspect parameters |

## Connection map

- Insert Log → CleanUp execution. See below if you will prepend this workflow (`main`, output 0, input 0)
- Error Trigger → Insert Log (`main`, output 0, input 0)
- Error Trigger → Count for 5 minutes (`main`, output 0, input 0)
- Principal E-Mail → Fallback E-Mail (`main`, output 1, input 0)
- Count for 5 minutes → If there is no logs in 5 minutes (`main`, output 0, input 0)
- Sometimes... just cleanup → Truncate Log Database (`main`, output 0, input 0)
- If there is no logs in 5 minutes → Insert your error handling logic after this (`main`, output 0, input 0)
- If there is no logs in 5 minutes → CleanUp execution. See below if you will prepend this workflow (`main`, output 1, input 0)
- Call this Sample - Prepend to your error catcher → Principal E-Mail (`main`, output 0, input 0)
- Call this Sample - Prepend to your error catcher → Push mobile notification (`main`, output 0, input 0)
- See below to prepend this at your error handling → Insert Log (`main`, output 0, input 0)
- See below to prepend this at your error handling → Count for 5 minutes (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1777_Error_Postgres_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1777_Error_Postgres_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
