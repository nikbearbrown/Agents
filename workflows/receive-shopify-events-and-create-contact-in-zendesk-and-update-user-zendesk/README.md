# receive shopify events and create contact in zendesk and update user zendesk

This folder contains the **receive shopify events and create contact in zendesk and update user zendesk** workflow. Its executable nodes use `if`, `merge`, `noOp`, `set`, `shopifyTrigger`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-shopify-events-and-create-contact-in-zendesk-and-update-user-zendesk.json`](receive-shopify-events-and-create-contact-in-zendesk-and-update-user-zendesk.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `shopifyApi`, `zendeskApi`

**Entry nodes:** On customer updated

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Keep only UserId and email | `set` | Inspect parameters |
| User exists in Zendesk | `if` | Inspect parameters |
| Add Zendesk contact Id to Shopify data | `merge` | Inspect parameters |
| On customer updated | `shopifyTrigger` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |
| Contact data is modified | `if` | Inspect parameters |
| Create contact in Zendesk | `zendesk` | user |
| Update contact in Zendesk | `zendesk` | user / update |
| Search contact by email adress | `zendesk` | user / search |

## Connection map

- On customer updated → Add Zendesk contact Id to Shopify data (`main`, output 0, input 0)
- On customer updated → Search contact by email adress (`main`, output 0, input 0)
- User exists in Zendesk → Contact data is modified (`main`, output 0, input 0)
- User exists in Zendesk → Create contact in Zendesk (`main`, output 1, input 0)
- Contact data is modified → Update contact in Zendesk (`main`, output 0, input 0)
- Contact data is modified → NoOp (`main`, output 1, input 0)
- Keep only UserId and email → Add Zendesk contact Id to Shopify data (`main`, output 0, input 1)
- Search contact by email adress → Keep only UserId and email (`main`, output 0, input 0)
- Add Zendesk contact Id to Shopify data → User exists in Zendesk (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0268_Shopify_Zendesk_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Shopify/0268_Shopify_Zendesk_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
