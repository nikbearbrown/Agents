# CalcsLive Demo Workflow Template

This folder contains the **CalcsLive Demo Workflow Template** workflow. Its executable nodes use `calcsLive`, `gmail`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`calcslive-demo-workflow-template.json`](calcslive-demo-workflow-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `calcsLiveApi`, `gmailOAuth2`

**Entry nodes:** When clicking 'Execute workflow'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking 'Execute workflow' | `manualTrigger` | Inspect parameters |
| Cylinder Calcs: (D, h) => (A, V) | `calcsLive` | Inspect parameters |
| Speed Calc: (d, t) => v | `calcsLive` | Inspect parameters |
| Mass Calc: (ρ, V) => m | `calcsLive` | Inspect parameters |
| Fields: (d, t) | `set` | Inspect parameters |
| Send Email | `gmail` | Inspect parameters |

## Connection map

- When clicking 'Execute workflow' → Fields: (d, t) (`main`, output 0, input 0)
- When clicking 'Execute workflow' → Cylinder Calcs: (D, h) => (A, V) (`main`, output 0, input 0)
- Mass Calc: (ρ, V) => m → Send Email (`main`, output 0, input 0)
- Fields: (d, t) → Speed Calc: (d, t) => v (`main`, output 0, input 0)
- Cylinder Calcs: (D, h) => (A, V) → Mass Calc: (ρ, V) => m (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calcslive/2058_Calcslive_Engineering_Calculations_Manual.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calcslive/2058_Calcslive_Engineering_Calculations_Manual.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
