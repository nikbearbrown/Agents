# Post on X

This folder contains the **Post on X** workflow. Its executable nodes use `airtop`, `executeWorkflowTrigger`, `formTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`post-on-x.json`](post-on-x.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtopApi`

**Entry nodes:** When Executed by Another Workflow, On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create session | `airtop` | Inspect parameters |
| Create window | `airtop` | window |
| Type text | `airtop` | interaction / type |
| Click on Post | `airtop` | interaction |
| End session | `airtop` | terminate |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Parameters | `set` | Inspect parameters |

## Connection map

- Type text → Click on Post (`main`, output 0, input 0)
- Parameters → Create session (`main`, output 0, input 0)
- Click on Post → End session (`main`, output 0, input 0)
- Create window → Type text (`main`, output 0, input 0)
- Create session → Create window (`main`, output 0, input 0)
- On form submission → Parameters (`main`, output 0, input 0)
- When Executed by Another Workflow → Parameters (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1957_Form_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1957_Form_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
