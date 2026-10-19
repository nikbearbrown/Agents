# Default Error Handler

This folder contains the **Default Error Handler** workflow. Its executable nodes use `code`, `errorTrigger`, `gmail`, `if`, `n8n`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`default-error-handler.json`](default-error-handler.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `n8nApi`

**Entry nodes:** Error Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Error Trigger | `errorTrigger` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| get error handler | `n8n` | get |
| n8n \| update | `n8n` | update |
| set fields | `code` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| active && no error handler set && not this  handler workflow | `if` | Inspect parameters |

## Connection map

- n8n → active && no error handler set && not this  handler workflow (`main`, output 0, input 0)
- set fields → n8n \| update (`main`, output 0, input 0)
- Error Trigger → Gmail (`main`, output 0, input 0)
- Schedule Trigger → get error handler (`main`, output 0, input 0)
- get error handler → n8n (`main`, output 0, input 0)
- active && no error handler set && not this  handler workflow → set fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/0518_Error_Code_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/0518_Error_Code_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
