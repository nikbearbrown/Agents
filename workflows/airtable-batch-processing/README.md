# ↔️ Airtable Batch Processing

This folder contains the **↔️ Airtable Batch Processing** workflow. Its executable nodes use `aggregate`, `code`, `debugHelper`, `executeWorkflow`, `executeWorkflowTrigger`, `httpRequest`, `if`, `manualTrigger`, `merge`, `set`, `splitInBatches`, `splitOut`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`airtable-batch-processing.json`](airtable-batch-processing.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`

**Entry nodes:** When clicking ‘Test workflow’, Airtable Subprocess

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| upsert | `httpRequest` | PATCH |
| random data | `debugHelper` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| batch 10 | `splitInBatches` | Inspect parameters |
| Airtable Subprocess | `executeWorkflowTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| insert | `httpRequest` | POST |
| rate limit? | `if` | Inspect parameters |
| Wait 0.2s to prevent rate limits | `wait` | Inspect parameters |
| retry request | `merge` | Inspect parameters |
| rate limit?1 | `if` | Inspect parameters |
| retry request1 | `merge` | Inspect parameters |
| rate limit?2 | `if` | Inspect parameters |
| retry request2 | `merge` | Inspect parameters |
| Aggregate3 | `aggregate` | Inspect parameters |
| Edit Fields4 | `set` | Inspect parameters |
| Aggregate2 | `aggregate` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| update | `httpRequest` | PATCH |
| Airtable Batch | `executeWorkflow` | Inspect parameters |
| Set Fields | `set` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Wait 5s2 | `wait` | Inspect parameters |
| Wait 5s | `wait` | Inspect parameters |
| Wait 5s1 | `wait` | Inspect parameters |
| return merged output | `code` | Inspect parameters |

## Connection map

- Switch → Edit Fields4 (`main`, output 0, input 0)
- Switch → Edit Fields1 (`main`, output 1, input 0)
- Switch → Edit Fields2 (`main`, output 2, input 0)
- insert → rate limit?1 (`main`, output 0, input 0)
- update → rate limit?2 (`main`, output 0, input 0)
- upsert → rate limit? (`main`, output 0, input 0)
- Wait 5s → retry request (`main`, output 0, input 1)
- Wait 5s1 → retry request1 (`main`, output 0, input 1)
- Wait 5s2 → retry request2 (`main`, output 0, input 1)
- batch 10 → return merged output (`main`, output 0, input 0)
- batch 10 → Switch (`main`, output 1, input 0)
- Aggregate → Airtable Batch (`main`, output 0, input 0)
- Split Out → batch 10 (`main`, output 0, input 0)
- Aggregate1 → upsert (`main`, output 0, input 0)
- Aggregate1 → retry request (`main`, output 0, input 0)
- Aggregate2 → insert (`main`, output 0, input 0)
- Aggregate2 → retry request1 (`main`, output 0, input 0)
- Aggregate3 → update (`main`, output 0, input 0)
- Aggregate3 → retry request2 (`main`, output 0, input 0)
- Set Fields → Aggregate (`main`, output 0, input 0)
- rate limit? → Wait 5s (`main`, output 0, input 0)
- rate limit? → Wait 0.2s to prevent rate limits (`main`, output 1, input 0)
- Edit Fields1 → Aggregate1 (`main`, output 0, input 0)
- Edit Fields2 → Aggregate2 (`main`, output 0, input 0)
- Edit Fields4 → Aggregate3 (`main`, output 0, input 0)
- rate limit?1 → Wait 5s1 (`main`, output 0, input 0)
- rate limit?1 → Wait 0.2s to prevent rate limits (`main`, output 1, input 0)
- rate limit?2 → Wait 5s2 (`main`, output 0, input 0)
- rate limit?2 → Wait 0.2s to prevent rate limits (`main`, output 1, input 0)
- retry request → upsert (`main`, output 0, input 0)
- retry request1 → insert (`main`, output 0, input 0)
- retry request2 → update (`main`, output 0, input 0)
- Airtable Subprocess → Split Out (`main`, output 0, input 0)
- Wait 0.2s to prevent rate limits → batch 10 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → random data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0091_Wait_Splitout_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0091_Wait_Splitout_Process_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
