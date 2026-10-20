# Find a different ideal buyer:

This folder contains the **Find a different ideal buyer:** workflow. Its executable nodes use `httpRequest`, `if`, `itemLists`, `merge`, `pipedrive`, `pipedriveTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`find-a-different-ideal-buyer.json`](find-a-different-ideal-buyer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpQueryAuth`, `pipedriveApi`

**Entry nodes:** Pipedrive Trigger - New Company Created

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| list people | `itemLists` | Inspect parameters |
| Pipedrive - Enrich Organization | `pipedrive` | organization / update |
| Pipedrive - Add Person | `pipedrive` | person |
| Datagma - Enrich Company | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| If lead is Ideal Buyer | `if` | Inspect parameters |
| Datagma - Find Emails | `httpRequest` | Inspect parameters |
| Prepare Data Before Merge | `set` | Inspect parameters |
| Pipedrive Trigger - New Company Created | `pipedriveTrigger` | Inspect parameters |

## Connection map

- Merge → Pipedrive - Add Person (`main`, output 0, input 0)
- list people → If lead is Ideal Buyer (`main`, output 0, input 0)
- list people → Merge (`main`, output 0, input 1)
- Datagma - Find Emails → Prepare Data Before Merge (`main`, output 0, input 0)
- If lead is Ideal Buyer → Datagma - Find Emails (`main`, output 0, input 0)
- Datagma - Enrich Company → list people (`main`, output 0, input 0)
- Datagma - Enrich Company → Pipedrive - Enrich Organization (`main`, output 0, input 0)
- Prepare Data Before Merge → Merge (`main`, output 0, input 0)
- Pipedrive Trigger - New Company Created → Datagma - Enrich Company (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Pipedrive/0249_Pipedrive_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Pipedrive/0249_Pipedrive_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
