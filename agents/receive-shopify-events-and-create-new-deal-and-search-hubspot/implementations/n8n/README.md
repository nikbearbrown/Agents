# receive shopify events and create new deal and search hubspot

This folder contains the **receive shopify events and create new deal and search hubspot** workflow. Its executable nodes use `hubspot`, `if`, `merge`, `noOp`, `set`, `shopifyTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-shopify-events-and-create-new-deal-and-search-hubspot.json`](receive-shopify-events-and-create-new-deal-and-search-hubspot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`, `shopifyApi`

**Entry nodes:** On order updated

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On order updated | `shopifyTrigger` | Inspect parameters |
| Keep only userId | `set` | Inspect parameters |
| New Order, deal not found | `if` | Inspect parameters |
| Do Nothing | `noOp` | Inspect parameters |
| Create new deal | `hubspot` | Inspect parameters |
| Find if order already exists as deal | `hubspot` | search |
| Add Hubspot userId to data | `merge` | Inspect parameters |
| Create or update contact | `hubspot` | contact |

## Connection map

- Keep only userId → Add Hubspot userId to data (`main`, output 0, input 1)
- On order updated → Add Hubspot userId to data (`main`, output 0, input 0)
- On order updated → Create or update contact (`main`, output 0, input 0)
- Create or update contact → Keep only userId (`main`, output 0, input 0)
- New Order, deal not found → Create new deal (`main`, output 0, input 0)
- New Order, deal not found → Do Nothing (`main`, output 1, input 0)
- Add Hubspot userId to data → Find if order already exists as deal (`main`, output 0, input 0)
- Find if order already exists as deal → New Order, deal not found (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0265_Shopify_HubSpot_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0265_Shopify_HubSpot_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
