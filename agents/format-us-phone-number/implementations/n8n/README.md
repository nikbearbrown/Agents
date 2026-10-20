# Format US Phone Number

This folder contains the **Format US Phone Number** workflow. Its executable nodes use `executeWorkflowTrigger`, `if`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`format-us-phone-number.json`](format-us-phone-number.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Check if first digit is valid country code | `if` | Inspect parameters |
| Add valid country code | `set` | Inspect parameters |
| Strip phone number formatting | `set` | Inspect parameters |
| Check number of digits in phone number | `switch` | Inspect parameters |
| Format phone numbers | `set` | Inspect parameters |
| Clear invalid number | `set` | Inspect parameters |

## Connection map

- Clear invalid number → Format phone numbers (`main`, output 0, input 0)
- Add valid country code → Format phone numbers (`main`, output 0, input 0)
- Strip phone number formatting → Check number of digits in phone number (`main`, output 0, input 0)
- When Executed by Another Workflow → Strip phone number formatting (`main`, output 0, input 0)
- Check number of digits in phone number → Check if first digit is valid country code (`main`, output 0, input 0)
- Check number of digits in phone number → Add valid country code (`main`, output 1, input 0)
- Check number of digits in phone number → Clear invalid number (`main`, output 2, input 0)
- Check number of digits in phone number → Clear invalid number (`main`, output 3, input 0)
- Check if first digit is valid country code → Format phone numbers (`main`, output 0, input 0)
- Check if first digit is valid country code → Clear invalid number (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/1918_Executeworkflow_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/1918_Executeworkflow_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
