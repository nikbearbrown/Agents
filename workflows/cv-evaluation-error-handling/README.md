# CV Evaluation - Error Handling

This folder contains the **CV Evaluation - Error Handling** workflow. Its executable nodes use `code`, `errorTrigger`, `gmail`, `html`, `if`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cv-evaluation-error-handling.json`](cv-evaluation-error-handling.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** Error Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Error Trigger | `errorTrigger` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Config | `set` | Inspect parameters |
| Constants | `set` | Inspect parameters |
| If | `if` | Inspect parameters |
| HTML for Execution Error | `html` | Inspect parameters |
| HTML for Trigger Error | `html` | Inspect parameters |
| KeepEitherOfHTMLs | `merge` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- If → HTML for Execution Error (`main`, output 0, input 0)
- If → HTML for Trigger Error (`main`, output 1, input 0)
- Merge → Gmail (`main`, output 0, input 0)
- Config → Constants (`main`, output 0, input 0)
- Constants → Merge (`main`, output 0, input 1)
- Constants → If (`main`, output 0, input 0)
- Error Trigger → Config (`main`, output 0, input 0)
- KeepEitherOfHTMLs → Merge (`main`, output 0, input 0)
- HTML for Trigger Error → KeepEitherOfHTMLs (`main`, output 0, input 1)
- HTML for Execution Error → KeepEitherOfHTMLs (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1991_Error_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1991_Error_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
