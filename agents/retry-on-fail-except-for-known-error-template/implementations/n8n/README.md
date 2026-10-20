# Retry on fail except for known error Template

This folder contains the **Retry on fail except for known error Template** workflow. Its executable nodes use `if`, `manualTrigger`, `noOp`, `set`, `stopAndError`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`retry-on-fail-except-for-known-error-template.json`](retry-on-fail-except-for-known-error-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Retry limit reached | `stopAndError` | Inspect parameters |
| Set tries | `set` | Inspect parameters |
| Update tries | `set` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Catch known error | `if` | Inspect parameters |
| Replace Me | `noOp` | Inspect parameters |
| Success | `noOp` | Inspect parameters |
| Known Error | `noOp` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| If tries left | `if` | Inspect parameters |

## Connection map

- Wait → Update tries (`main`, output 0, input 0)
- Set tries → Replace Me (`main`, output 0, input 0)
- Replace Me → Success (`main`, output 0, input 0)
- Replace Me → Catch known error (`main`, output 1, input 0)
- Update tries → If tries left (`main`, output 0, input 0)
- If tries left → Set tries (`main`, output 0, input 0)
- If tries left → Retry limit reached (`main`, output 1, input 0)
- Manual Trigger → Set tries (`main`, output 0, input 0)
- Catch known error → Known Error (`main`, output 0, input 0)
- Catch known error → Wait (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1963_Stopanderror_Wait_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1963_Stopanderror_Wait_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
