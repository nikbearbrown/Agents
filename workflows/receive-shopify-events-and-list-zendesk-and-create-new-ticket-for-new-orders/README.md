# receive shopify events and list zendesk and create new ticket for new orders

This folder contains the **receive shopify events and list zendesk and create new ticket for new orders** workflow. Its executable nodes use `if`, `merge`, `noOp`, `set`, `shopifyTrigger`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-shopify-events-and-list-zendesk-and-create-new-ticket-for-new-orders.json`](receive-shopify-events-and-list-zendesk-and-create-new-ticket-for-new-orders.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `shopifyApi`, `zendeskApi`

**Entry nodes:** On order updated

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On order updated | `shopifyTrigger` | Inspect parameters |
| Order exists in Zendesk | `if` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |
| Find if order already has a ticket in Zendesk | `zendesk` | getAll |
| Keep only ticket Id | `set` | Inspect parameters |
| Add ticket info to order data | `merge` | Inspect parameters |
| Create new ticket for new orders | `zendesk` | Inspect parameters |

## Connection map

- On order updated → Find if order already has a ticket in Zendesk (`main`, output 0, input 0)
- On order updated → Add ticket info to order data (`main`, output 0, input 0)
- Keep only ticket Id → Add ticket info to order data (`main`, output 0, input 1)
- Order exists in Zendesk → NoOp (`main`, output 0, input 0)
- Order exists in Zendesk → Create new ticket for new orders (`main`, output 1, input 0)
- Add ticket info to order data → Order exists in Zendesk (`main`, output 0, input 0)
- Find if order already has a ticket in Zendesk → Keep only ticket Id (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0269_Shopify_Zendesk_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0269_Shopify_Zendesk_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
