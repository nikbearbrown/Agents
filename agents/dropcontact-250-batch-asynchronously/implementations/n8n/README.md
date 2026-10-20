# DROPCONTACT 250 BATCH ASYNCHRONOUSLY

This folder contains the **DROPCONTACT 250 BATCH ASYNCHRONOUSLY** workflow. Its executable nodes use `aggregate`, `code`, `httpRequest`, `postgres`, `scheduleTrigger`, `slack`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dropcontact-250-batch-asynchronously.json`](dropcontact-250-batch-asynchronously.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropcontactApi`, `postgres`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Aggregate | `aggregate` | Inspect parameters |
| PROFILES QUERY | `postgres` | executeQuery |
| BULK DROPCONTACT REQUESTS | `httpRequest` | POST |
| Loop Over Items2 | `splitInBatches` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Postgres | `postgres` | update |
| BULK DROPCONTACT DOWNLOAD | `httpRequest` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| DATA TRANSFORMATION | `code` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Wait2 → BULK DROPCONTACT DOWNLOAD (`main`, output 0, input 0)
- Postgres → Loop Over Items2 (`main`, output 0, input 0)
- Aggregate → DATA TRANSFORMATION (`main`, output 0, input 0)
- Split Out → Postgres (`main`, output 0, input 0)
- PROFILES QUERY → Loop Over Items2 (`main`, output 0, input 0)
- Loop Over Items2 → Aggregate (`main`, output 1, input 0)
- Schedule Trigger → PROFILES QUERY (`main`, output 0, input 0)
- DATA TRANSFORMATION → BULK DROPCONTACT REQUESTS (`main`, output 0, input 0)
- BULK DROPCONTACT DOWNLOAD → Split Out (`main`, output 0, input 0)
- BULK DROPCONTACT DOWNLOAD → Slack (`main`, output 1, input 0)
- BULK DROPCONTACT REQUESTS → Wait2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0498_Wait_Splitout_Process_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0498_Wait_Splitout_Process_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
