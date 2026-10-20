# [n8n] - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices

This folder contains the **[n8n] - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `if`, `noOp`, `scheduleTrigger`, `set`, `shopify`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-shopify-orders-to-d365-business-central-sales-orders-sales-invoices.json`](n8n-shopify-orders-to-d365-business-central-sales-orders-sales-invoices.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `oAuth2Api`, `shopifyAccessTokenApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| GetFufillmentOrders | `httpRequest` | Inspect parameters |
| Shopify | `shopify` | getAll |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| New Customer? | `if` | Inspect parameters |
| Lookup Customers | `httpRequest` | Inspect parameters |
| SelectFields | `set` | Inspect parameters |
| orderPreprocessing | `code` | Inspect parameters |
| Create Customer | `httpRequest` | POST |
| Set Business Central Customer Id | `set` | Inspect parameters |
| Create Order Lines | `httpRequest` | POST |
| End | `noOp` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| DELETE Sales Order | `httpRequest` | DELETE |
| D365 BC Environment Settings | `set` | Inspect parameters |
| Create Sales Order | `httpRequest` | POST |
| Set Lines Invoice | `set` | Inspect parameters |
| Set Lines SO | `set` | Inspect parameters |
| Split Out Invoice | `splitOut` | Inspect parameters |
| Create Invoice Lines | `httpRequest` | POST |
| Filter | `filter` | Inspect parameters |
| Create Sales Invoice | `httpRequest` | POST |
| End1 | `noOp` | Inspect parameters |
| Sales Invoice | `set` | Inspect parameters |
| Lookup Sales Order | `httpRequest` | Inspect parameters |
| Sales Order Mapping | `set` | Inspect parameters |
| New SO? | `if` | Inspect parameters |
| Lookup Sales Invoice | `httpRequest` | Inspect parameters |
| New Invoice? | `if` | Inspect parameters |
| POS? | `if` | Inspect parameters |
| DELETE Sales Invoice | `httpRequest` | DELETE |

## Connection map

- POS? → Lookup Sales Invoice (`main`, output 0, input 0)
- POS? → Lookup Sales Order (`main`, output 1, input 0)
- Filter → GetFufillmentOrders (`main`, output 0, input 0)
- New SO? → Sales Order Mapping (`main`, output 0, input 0)
- Shopify → Filter (`main`, output 0, input 0)
- Split Out → Create Order Lines (`main`, output 0, input 0)
- New Invoice? → Sales Invoice (`main`, output 0, input 0)
- SelectFields → orderPreprocessing (`main`, output 0, input 0)
- Set Lines SO → Split Out (`main`, output 0, input 0)
- New Customer? → Create Customer (`main`, output 0, input 0)
- New Customer? → Loop Over Items (`main`, output 1, input 0)
- Sales Invoice → Create Sales Invoice (`main`, output 0, input 0)
- Create Customer → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Set Business Central Customer Id (`main`, output 0, input 0)
- Loop Over Items → Lookup Customers (`main`, output 1, input 0)
- Lookup Customers → New Customer? (`main`, output 0, input 0)
- Schedule Trigger → D365 BC Environment Settings (`main`, output 0, input 0)
- Set Lines Invoice → Split Out Invoice (`main`, output 0, input 0)
- Split Out Invoice → Create Invoice Lines (`main`, output 0, input 0)
- Create Order Lines → End (`main`, output 0, input 0)
- Create Order Lines → DELETE Sales Order (`main`, output 1, input 0)
- Create Sales Order → Set Lines SO (`main`, output 0, input 0)
- Lookup Sales Order → New SO? (`main`, output 0, input 0)
- orderPreprocessing → Loop Over Items (`main`, output 0, input 0)
- GetFufillmentOrders → SelectFields (`main`, output 0, input 0)
- Sales Order Mapping → Create Sales Order (`main`, output 0, input 0)
- Create Invoice Lines → End1 (`main`, output 0, input 0)
- Create Invoice Lines → DELETE Sales Invoice (`main`, output 1, input 0)
- Create Sales Invoice → Set Lines Invoice (`main`, output 0, input 0)
- Lookup Sales Invoice → New Invoice? (`main`, output 0, input 0)
- D365 BC Environment Settings → Shopify (`main`, output 0, input 0)
- Set Business Central Customer Id → POS? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1560_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1560_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
