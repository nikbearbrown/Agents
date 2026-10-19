# Luma AI Dream Machine - Simple v1 - AK

This folder contains the **Luma AI Dream Machine - Simple v1 - AK** workflow. Its executable nodes use `airtable`, `code`, `executionData`, `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`luma-ai-dream-machine-simple-v1-ak.json`](luma-ai-dream-machine-simple-v1-ak.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Text 2 Video | `httpRequest` | POST |
| RANDOM Camera Motion | `code` | Inspect parameters |
| Global SETTINGS | `set` | Inspect parameters |
| ADD Video Info | `airtable` | create |
| Execution Data | `executionData` | Inspect parameters |

## Connection map

- Text 2 Video → Execution Data (`main`, output 0, input 0)
- Execution Data → ADD Video Info (`main`, output 0, input 0)
- Global SETTINGS → RANDOM Camera Motion (`main`, output 0, input 0)
- RANDOM Camera Motion → Text 2 Video (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Global SETTINGS (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0753_Code_Executiondata_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0753_Code_Executiondata_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
