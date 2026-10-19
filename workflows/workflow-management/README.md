# Workflow management

This folder contains the **Workflow management** workflow. Its executable nodes use `airtable`, `cron`, `dropbox`, `function`, `httpRequest`, `if`, `manualTrigger`, `moveBinaryData`, `noOp`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-management.json`](workflow-management.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `dropboxApi`

**Entry nodes:** On clicking 'execute', Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Function | `function` | Inspect parameters |
| SplitInBatches | `splitInBatches` | Inspect parameters |
| IF | `if` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |
| Airtable | `airtable` | list |
| Airtable1 | `airtable` | update |
| Airtable2 | `airtable` | append |
| Set | `set` | Inspect parameters |
| Set1 | `set` | Inspect parameters |
| Get All Workflows | `httpRequest` | Inspect parameters |
| Prepare data | `function` | Inspect parameters |
| Prepare data1 | `function` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| Dropbox | `dropbox` | Inspect parameters |
| Get Workflow Details | `httpRequest` | Inspect parameters |
| Get file link | `httpRequest` | Inspect parameters |
| IF Airtable record exists? | `if` | Inspect parameters |

## Connection map

- IF → NoOp (`main`, output 0, input 0)
- IF → SplitInBatches (`main`, output 1, input 0)
- Set → Airtable1 (`main`, output 0, input 0)
- Cron → Get All Workflows (`main`, output 0, input 0)
- Set1 → Airtable2 (`main`, output 0, input 0)
- Dropbox → Get file link (`main`, output 0, input 0)
- Airtable → IF Airtable record exists? (`main`, output 0, input 0)
- Function → SplitInBatches (`main`, output 0, input 0)
- Airtable1 → IF (`main`, output 0, input 0)
- Airtable2 → IF (`main`, output 0, input 0)
- Prepare data → Set (`main`, output 0, input 0)
- Get file link → Airtable (`main`, output 0, input 0)
- Prepare data1 → Set1 (`main`, output 0, input 0)
- SplitInBatches → Get Workflow Details (`main`, output 0, input 0)
- Move Binary Data → Dropbox (`main`, output 0, input 0)
- Get All Workflows → Function (`main`, output 0, input 0)
- Get Workflow Details → Move Binary Data (`main`, output 0, input 0)
- On clicking 'execute' → Get All Workflows (`main`, output 0, input 0)
- IF Airtable record exists? → Prepare data (`main`, output 0, input 0)
- IF Airtable record exists? → Prepare data1 (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Dropbox/0969_Dropbox_Manual_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Dropbox/0969_Dropbox_Manual_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
