# http request and split out and filter owned projects

This folder contains the **http request and split out and filter owned projects** workflow. Its executable nodes use `code`, `filter`, `form`, `formTrigger`, `httpRequest`, `if`, `limit`, `n8n`, `removeDuplicates`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-split-out-and-filter-owned-projects.json`](http-request-and-split-out-and-filter-owned-projects.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| set credentials | `set` | Inspect parameters |
| login n8n | `httpRequest` | POST |
| get tags | `httpRequest` | Inspect parameters |
| my-projects | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| filter owned projects | `filter` | Inspect parameters |
| Get folders | `httpRequest` | Inspect parameters |
| Split Out2 | `splitOut` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| get workflows | `n8n` | Inspect parameters |
| Move workflow to folder | `httpRequest` | PATCH |
| Normalize names | `set` | Inspect parameters |
| Limit1 | `limit` | Inspect parameters |
| Create folders | `httpRequest` | POST |
| set folder name + id | `set` | Inspect parameters |
| set folder name + id1 | `set` | Inspect parameters |
| set global | `set` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Code | `code` | Inspect parameters |
| If no folder | `if` | Inspect parameters |
| If folder exists | `if` | Inspect parameters |
| set name | `set` | Inspect parameters |
| end import | `form` | completion |
| pass all items | `set` | Inspect parameters |
| select tags to move | `form` | Inspect parameters |
| extract name from form | `set` | Inspect parameters |
| Split Out the tags | `splitOut` | Inspect parameters |
| tags to string | `set` | Inspect parameters |

## Connection map

- Code → select tags to move (`main`, output 0, input 0)
- Filter → Limit1 (`main`, output 0, input 0)
- Limit1 → If folder exists (`main`, output 0, input 0)
- get tags → tags to string (`main`, output 0, input 0)
- set name → Create folders (`main`, output 0, input 0)
- Split Out → filter owned projects (`main`, output 0, input 0)
- login n8n → my-projects (`main`, output 0, input 0)
- Split Out2 → Normalize names (`main`, output 0, input 0)
- set global → get workflows (`main`, output 0, input 0)
- Edit Fields → set name (`main`, output 0, input 0)
- Get folders → If no folder (`main`, output 0, input 0)
- my-projects → Split Out (`main`, output 0, input 0)
- If no folder → Split Out2 (`main`, output 0, input 0)
- If no folder → Edit Fields (`main`, output 1, input 0)
- get workflows → Move workflow to folder (`main`, output 0, input 0)
- Create folders → set folder name + id (`main`, output 0, input 0)
- pass all items → end import (`main`, output 0, input 0)
- tags to string → Code (`main`, output 0, input 0)
- Loop Over Items → pass all items (`main`, output 0, input 0)
- Loop Over Items → Get folders (`main`, output 1, input 0)
- Normalize names → Remove Duplicates (`main`, output 0, input 0)
- set credentials → login n8n (`main`, output 0, input 0)
- If folder exists → set folder name + id1 (`main`, output 0, input 0)
- If folder exists → set name (`main`, output 1, input 0)
- Remove Duplicates → Filter (`main`, output 0, input 0)
- On form submission → set credentials (`main`, output 0, input 0)
- Split Out the tags → extract name from form (`main`, output 0, input 0)
- select tags to move → Split Out the tags (`main`, output 0, input 0)
- set folder name + id → set global (`main`, output 0, input 0)
- filter owned projects → get tags (`main`, output 0, input 0)
- set folder name + id1 → set global (`main`, output 0, input 0)
- extract name from form → Loop Over Items (`main`, output 0, input 0)
- Move workflow to folder → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0832_Splitout_Limit_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0832_Splitout_Limit_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
