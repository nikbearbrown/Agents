# receive pipedrive events and set item to only current product data and create product in stripe

This folder contains the **receive pipedrive events and set item to only current product data and create product in stripe** workflow. Its executable nodes use `functionItem`, `httpRequest`, `itemLists`, `merge`, `pipedriveTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-pipedrive-events-and-set-item-to-only-current-product-data-and-create-product-in-stripe.json`](receive-pipedrive-events-and-set-item-to-only-current-product-data-and-create-product-in-stripe.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `pipedriveApi`, `stripeApi`

**Entry nodes:** On product created

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On product created | `pipedriveTrigger` | Inspect parameters |
| Set item to only current product data | `functionItem` | Inspect parameters |
| Create product in Stripe | `httpRequest` | Inspect parameters |
| Add created product Id to data | `merge` | Inspect parameters |
| Keep only productId of created product | `set` | Inspect parameters |
| Create price records in Stripe | `httpRequest` | Inspect parameters |
| Split prices to seperate items | `itemLists` | Inspect parameters |

## Connection map

- On product created → Set item to only current product data (`main`, output 0, input 0)
- Create product in Stripe → Keep only productId of created product (`main`, output 0, input 0)
- Add created product Id to data → Split prices to seperate items (`main`, output 0, input 0)
- Split prices to seperate items → Create price records in Stripe (`main`, output 0, input 0)
- Set item to only current product data → Create product in Stripe (`main`, output 0, input 0)
- Set item to only current product data → Add created product Id to data (`main`, output 0, input 0)
- Keep only productId of created product → Add created product Id to data (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0247_Functionitem_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0247_Functionitem_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
