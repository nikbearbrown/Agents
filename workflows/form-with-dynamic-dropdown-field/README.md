# Form with Dynamic Dropdown Field

This folder contains the **Form with Dynamic Dropdown Field** workflow. Its executable nodes use `code`, `executeWorkflow`, `formTrigger`, `googleSheets`, `googleSheetsTrigger`, `n8n`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`form-with-dynamic-dropdown-field.json`](form-with-dynamic-dropdown-field.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `n8nApi`

**Entry nodes:** On form submission, Google Sheets Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| n8n \| get wf | `n8n` | get |
| n8n \| update | `n8n` | update |
| On form submission | `formTrigger` | Inspect parameters |
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Write JSON | `code` | Inspect parameters |
| Replace values | `set` | Inspect parameters |
| Get all values | `googleSheets` | Inspect parameters |
| Format to 'values' | `set` | Inspect parameters |

## Connection map

- Write JSON → n8n \| get wf (`main`, output 0, input 0)
- n8n \| get wf → Replace values (`main`, output 0, input 0)
- Get all values → Format to 'values' (`main`, output 0, input 0)
- Replace values → n8n \| update (`main`, output 0, input 0)
- Format to 'values' → Write JSON (`main`, output 0, input 0)
- On form submission → Execute Workflow (`main`, output 0, input 0)
- Google Sheets Trigger → Get all values (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1630_Code_Form_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1630_Code_Form_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
