# Shopify + Mautic

This folder contains the **Shopify + Mautic** workflow. Its executable nodes use `crypto`, `graphql`, `if`, `mautic`, `noOp`, `set`, `shopifyTrigger`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`shopify-mautic.json`](shopify-mautic.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `mauticOAuth2Api`, `shopifyAccessTokenApi`

**Entry nodes:** Shopify Trigger, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Shopify Trigger | `shopifyTrigger` | Inspect parameters |
| Accepts Marketing? | `if` | Inspect parameters |
| Accepts Marketing?1 | `if` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Add to confirmed segment | `mautic` | contactSegment |
| Remove from confirmed segment | `mautic` | contactSegment / remove |
| Webhook | `webhook` | Inspect parameters |
| Crypto | `crypto` | Inspect parameters |
| If | `if` | Inspect parameters |
| No Operation, do nothing1 | `noOp` | Inspect parameters |
| GraphQL | `graphql` | Inspect parameters |
| Marketing Consent - subscribed | `graphql` | Inspect parameters |
| Marketing Consent - unsubscribed | `graphql` | Inspect parameters |
| Mautic - Accepts Marketing? | `if` | Inspect parameters |
| Customer exists? | `if` | Inspect parameters |
| No Operation, do nothing2 | `noOp` | Inspect parameters |
| Set Shopify Subdomain | `set` | Inspect parameters |
| Search for Contact by Email | `mautic` | getAll |
| Contact exists? | `if` | Inspect parameters |
| Create a new contact | `mautic` | Inspect parameters |

## Connection map

- If → GraphQL (`main`, output 0, input 0)
- If → No Operation, do nothing1 (`main`, output 1, input 0)
- Crypto → If (`main`, output 0, input 0)
- GraphQL → Customer exists? (`main`, output 0, input 0)
- Webhook → Crypto (`main`, output 0, input 0)
- Webhook → Set Shopify Subdomain (`main`, output 0, input 0)
- Contact exists? → Accepts Marketing? (`main`, output 0, input 0)
- Contact exists? → Accepts Marketing?1 (`main`, output 1, input 0)
- Shopify Trigger → Search for Contact by Email (`main`, output 0, input 0)
- Customer exists? → Mautic - Accepts Marketing? (`main`, output 0, input 0)
- Customer exists? → No Operation, do nothing2 (`main`, output 1, input 0)
- Accepts Marketing? → Add to confirmed segment (`main`, output 0, input 0)
- Accepts Marketing? → Remove from confirmed segment (`main`, output 1, input 0)
- Accepts Marketing?1 → Create a new contact (`main`, output 0, input 0)
- Accepts Marketing?1 → No Operation, do nothing (`main`, output 1, input 0)
- Create a new contact → Add to confirmed segment (`main`, output 0, input 0)
- Mautic - Accepts Marketing? → Marketing Consent - subscribed (`main`, output 0, input 0)
- Mautic - Accepts Marketing? → Marketing Consent - unsubscribed (`main`, output 1, input 0)
- Search for Contact by Email → Contact exists? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/1526_Mautic_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/1526_Mautic_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
