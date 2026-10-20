# Job Finder

This folder contains the **Job Finder** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `manualTrigger`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`job-finder.json`](job-finder.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Search for open jobs | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- When clicking ‘Test workflow’ → Search for open jobs (`main`, output 0, input 0)
- Search for open jobs → Code (`main`, output 0, input 0)
- Schedule Trigger → Search for open jobs (`main`, output 0, input 0)
- Code → Send Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/t0mer/Applyfy/blob/b0679d64719ca44a88d33825ea8e0debdc0c822b/flow.json](https://github.com/t0mer/Applyfy/blob/b0679d64719ca44a88d33825ea8e0debdc0c822b/flow.json). License: **Apache-2.0**; preserve [the notice](../../../../licenses/t0mer--Applyfy.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
