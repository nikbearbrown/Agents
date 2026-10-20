# TEMPLATES

This folder contains the **TEMPLATES** workflow. Its executable nodes use `code`, `convertToFile`, `httpRequest`, `manualTrigger`, `merge`, `mondayCom`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`split-out-and-get-boarditem-monday-com-and-http-request.json`](split-out-and-get-boarditem-monday-com-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mondayComApi`, `mondayComOAuth2Api`

**Entry nodes:** When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| PULL SUBITEMS | `code` | Inspect parameters |
| SPLIT SUBITEMS | `splitOut` | Inspect parameters |
| GET EACH SUBITEM | `mondayCom` | boardItem / get |
| MONDAY UPLOAD | `httpRequest` | POST |
| Convert to File | `convertToFile` | toJson |
| Merge | `merge` | Inspect parameters |
| PULL LINKEDPULSE | `mondayCom` | boardItem / get |
| GET ITEM | `mondayCom` | boardItem / get |
| GET LINKEDPULSES | `code` | Inspect parameters |
| GET BOARD RELATION | `code` | Inspect parameters |
| COLUMN BY NAME | `code` | Inspect parameters |
| COLUMN BY ID | `code` | Inspect parameters |
| SPLIT LINKED PULSES | `splitOut` | Inspect parameters |

## Connection map

- Merge → MONDAY UPLOAD (`main`, output 0, input 0)
- GET ITEM → GET BOARD RELATION (`main`, output 0, input 0)
- GET ITEM → PULL SUBITEMS (`main`, output 0, input 0)
- GET ITEM → Convert to File (`main`, output 0, input 0)
- GET ITEM → Merge (`main`, output 0, input 0)
- GET ITEM → COLUMN BY NAME (`main`, output 0, input 0)
- GET ITEM → COLUMN BY ID (`main`, output 0, input 0)
- PULL SUBITEMS → SPLIT SUBITEMS (`main`, output 0, input 0)
- SPLIT SUBITEMS → GET EACH SUBITEM (`main`, output 0, input 0)
- Convert to File → Merge (`main`, output 0, input 1)
- GET LINKEDPULSES → SPLIT LINKED PULSES (`main`, output 0, input 0)
- GET BOARD RELATION → GET LINKEDPULSES (`main`, output 0, input 0)
- SPLIT LINKED PULSES → PULL LINKEDPULSE (`main`, output 0, input 0)
- When clicking "Test workflow" → GET ITEM (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1553_Mondaycom_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1553_Mondaycom_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
