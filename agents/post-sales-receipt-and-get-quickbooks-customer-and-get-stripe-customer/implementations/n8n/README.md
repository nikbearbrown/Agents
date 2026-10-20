# post sales receipt and get quickbooks customer and get stripe customer

This folder contains the **post sales receipt and get quickbooks customer and get stripe customer** workflow. Its executable nodes use `httpRequest`, `if`, `merge`, `quickbooks`, `stripe`, `stripeTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`post-sales-receipt-and-get-quickbooks-customer-and-get-stripe-customer.json`](post-sales-receipt-and-get-quickbooks-customer-and-get-stripe-customer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpCustomAuth`, `quickBooksOAuth2Api`, `stripeApi`

**Entry nodes:** New Payment

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| POST Sales Receipt | `httpRequest` | POST |
| GET Quickbooks Customer | `httpRequest` | Inspect parameters |
| Get Stripe Customer | `stripe` | customer |
| New Payment | `stripeTrigger` | Inspect parameters |
| If Customer Exists | `if` | Inspect parameters |
| Use Stripe Customer | `merge` | Inspect parameters |
| Create QuickBooks Customer | `quickbooks` | create |
| Merge Stripe and QuickBooks Data | `merge` | Inspect parameters |
| Merge Payment and QuickBooks Customer | `merge` | Inspect parameters |
| POST Sales Receipt To QuickBooks | `httpRequest` | POST |

## Connection map

- New Payment → Get Stripe Customer (`main`, output 0, input 0)
- New Payment → Merge Stripe and QuickBooks Data (`main`, output 0, input 0)
- New Payment → Merge Payment and QuickBooks Customer (`main`, output 0, input 0)
- If Customer Exists → Merge Stripe and QuickBooks Data (`main`, output 0, input 2)
- If Customer Exists → Use Stripe Customer (`main`, output 1, input 0)
- Get Stripe Customer → GET Quickbooks Customer (`main`, output 0, input 0)
- Get Stripe Customer → Use Stripe Customer (`main`, output 0, input 1)
- Use Stripe Customer → Create QuickBooks Customer (`main`, output 0, input 0)
- GET Quickbooks Customer → If Customer Exists (`main`, output 0, input 0)
- GET Quickbooks Customer → Merge Stripe and QuickBooks Data (`main`, output 0, input 1)
- Create QuickBooks Customer → Merge Payment and QuickBooks Customer (`main`, output 0, input 1)
- Merge Stripe and QuickBooks Data → POST Sales Receipt (`main`, output 0, input 0)
- Merge Payment and QuickBooks Customer → POST Sales Receipt To QuickBooks (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0707_HTTP_Stripe_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0707_HTTP_Stripe_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
