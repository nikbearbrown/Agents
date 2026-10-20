# get last execution timestamp and set new last execution timestamp and get zendesk comments for tickets

This folder contains the **get last execution timestamp and set new last execution timestamp and get zendesk comments for tickets** workflow. Its executable nodes use `cron`, `functionItem`, `httpRequest`, `if`, `itemLists`, `merge`, `noOp`, `pipedrive`, `set`, `splitInBatches`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-last-execution-timestamp-and-set-new-last-execution-timestamp-and-get-zendesk-comments-for-tickets.json`](get-last-execution-timestamp-and-set-new-last-execution-timestamp-and-get-zendesk-comments-for-tickets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `pipedriveApi`, `zendeskApi`

**Entry nodes:** Every day at 09:00

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| NoOp | `noOp` | Inspect parameters |
| Get last execution timestamp | `functionItem` | Inspect parameters |
| Set new last execution timestamp | `functionItem` | Inspect parameters |
| Pipedrive person Id found | `if` | Inspect parameters |
| NoOp1 | `noOp` | Inspect parameters |
| Get Zendesk comments for tickets | `httpRequest` | Inspect parameters |
| Add comments to tickets | `merge` | Inspect parameters |
| Add Pipedrive person Id to Zendesk tickets | `merge` | Inspect parameters |
| Get tickets updated after last execution | `zendesk` | getAll |
| Channel is email | `if` | Inspect parameters |
| Rename fields and keep only needed fields | `set` | Inspect parameters |
| Search persons by email | `pipedrive` | person / search |
| Remove duplicates to make search efficient | `itemLists` | removeDuplicates |
| Set search email | `set` | Inspect parameters |
| Process commenst per ticket | `splitInBatches` | Inspect parameters |
| New comment | `if` | Inspect parameters |
| Split comments to seperate items | `itemLists` | Inspect parameters |
| Add comment as a note in Pipedrive | `pipedrive` | note |
| NoOp2 | `noOp` | Inspect parameters |
| Every day at 09:00 | `cron` | Inspect parameters |
| Done processing | `if` | Inspect parameters |

## Connection map

- New comment → Add comment as a note in Pipedrive (`main`, output 0, input 0)
- New comment → NoOp2 (`main`, output 1, input 0)
- Done processing → Set new last execution timestamp (`main`, output 0, input 0)
- Done processing → Process commenst per ticket (`main`, output 1, input 0)
- Channel is email → Set search email (`main`, output 0, input 0)
- Channel is email → Add Pipedrive person Id to Zendesk tickets (`main`, output 0, input 0)
- Channel is email → NoOp (`main`, output 1, input 0)
- Set search email → Remove duplicates to make search efficient (`main`, output 0, input 0)
- Every day at 09:00 → Get last execution timestamp (`main`, output 0, input 0)
- Add comments to tickets → Process commenst per ticket (`main`, output 0, input 0)
- Search persons by email → Rename fields and keep only needed fields (`main`, output 0, input 0)
- Pipedrive person Id found → Get Zendesk comments for tickets (`main`, output 0, input 0)
- Pipedrive person Id found → Add comments to tickets (`main`, output 0, input 0)
- Pipedrive person Id found → NoOp1 (`main`, output 1, input 0)
- Process commenst per ticket → Split comments to seperate items (`main`, output 0, input 0)
- Get last execution timestamp → Get tickets updated after last execution (`main`, output 0, input 0)
- Get Zendesk comments for tickets → Add comments to tickets (`main`, output 0, input 1)
- Split comments to seperate items → New comment (`main`, output 0, input 0)
- Add comment as a note in Pipedrive → Done processing (`main`, output 0, input 0)
- Get tickets updated after last execution → Channel is email (`main`, output 0, input 0)
- Rename fields and keep only needed fields → Add Pipedrive person Id to Zendesk tickets (`main`, output 0, input 1)
- Add Pipedrive person Id to Zendesk tickets → Pipedrive person Id found (`main`, output 0, input 0)
- Remove duplicates to make search efficient → Search persons by email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0267_Functionitem_Zendesk_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0267_Functionitem_Zendesk_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
