# api to check existing merge request and create new merge request and api to close existing merge request

This folder contains the **api to check existing merge request and create new merge request and api to close existing merge request** workflow. Its executable nodes use `httpRequest`, `if`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`api-to-check-existing-merge-request-and-create-new-merge-request-and-api-to-close-existing-merge-request.json`](api-to-check-existing-merge-request-and-create-new-merge-request-and-api-to-close-existing-merge-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| API to Check existing merge request | `httpRequest` | Inspect parameters |
| Is Exists | `if` | Inspect parameters |
| Create New Merge Request | `httpRequest` | POST |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| API to CLOSE existing Merge Request | `httpRequest` | PUT |
| Add Custom Notes To Merge Request | `httpRequest` | POST |
| 30 secs wait to approve merge request and pipeline to finish1 | `wait` | Inspect parameters |
| Merge When Pipeline Succeeds | `httpRequest` | PUT |
| setValueForMerge | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Is Exists → Create New Merge Request (`main`, output 0, input 0)
- Is Exists → Loop Over Items (`main`, output 1, input 0)
- Loop Over Items → API to Check existing merge request (`main`, output 0, input 0)
- Loop Over Items → API to CLOSE existing Merge Request (`main`, output 1, input 0)
- Schedule Trigger → API to Check existing merge request (`main`, output 0, input 0)
- setValueForMerge → Merge When Pipeline Succeeds (`main`, output 0, input 0)
- Create New Merge Request → Add Custom Notes To Merge Request (`main`, output 0, input 0)
- Add Custom Notes To Merge Request → 30 secs wait to approve merge request and pipeline to finish1 (`main`, output 0, input 0)
- API to CLOSE existing Merge Request → Loop Over Items (`main`, output 0, input 0)
- API to Check existing merge request → Is Exists (`main`, output 0, input 0)
- 30 secs wait to approve merge request and pipeline to finish1 → setValueForMerge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0717_HTTP_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0717_HTTP_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
