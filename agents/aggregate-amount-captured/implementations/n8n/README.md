# ``Aggregate `amount_captured` ``

This folder contains the **``Aggregate `amount_captured` ``** workflow. Its executable nodes use `code`, `httpRequest`, `hubspot`, `if`, `itemLists`, `merge`, `noOp`, `scheduleTrigger`, `set`, `stripe`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`aggregate-amount-captured.json`](aggregate-amount-captured.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`, `stripeApi`

**Entry nodes:** On schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If charge has customer | `if` | Inspect parameters |
| Get customer | `stripe` | customer |
| On schedule | `scheduleTrigger` | Inspect parameters |
| Remove duplicate customers | `itemLists` | removeDuplicates |
| Aggregate `amount_captured` | `itemLists` | aggregateItems |
| Aggregate totals | `code` | Inspect parameters |
| Create or update customer | `hubspot` | contact |
| Merge data | `merge` | Inspect parameters |
| Get all charges | `stripe` | charge / getAll |
| Get HubSpot field | `httpRequest` | Inspect parameters |
| Create field in HubSpot | `httpRequest` | POST |
| Configure | `set` | Inspect parameters |
| Skip field checking | `if` | Inspect parameters |
| Do nothing | `noOp` | Inspect parameters |
| If field exists | `if` | Inspect parameters |

## Connection map

- Configure → Skip field checking (`main`, output 0, input 0)
- Merge data → Aggregate totals (`main`, output 0, input 0)
- On schedule → Configure (`main`, output 0, input 0)
- Get customer → Merge data (`main`, output 0, input 0)
- Get all charges → If charge has customer (`main`, output 0, input 0)
- Get all charges → Merge data (`main`, output 0, input 1)
- If field exists → Get all charges (`main`, output 0, input 0)
- If field exists → Create field in HubSpot (`main`, output 1, input 0)
- Aggregate totals → Create or update customer (`main`, output 0, input 0)
- Get HubSpot field → If field exists (`main`, output 0, input 0)
- Skip field checking → Get all charges (`main`, output 0, input 0)
- Skip field checking → Get HubSpot field (`main`, output 1, input 0)
- If charge has customer → Remove duplicate customers (`main`, output 0, input 0)
- If charge has customer → Aggregate `amount_captured` (`main`, output 0, input 0)
- If charge has customer → Do nothing (`main`, output 1, input 0)
- Create field in HubSpot → Get all charges (`main`, output 0, input 0)
- Remove duplicate customers → Get customer (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0288_Code_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0288_Code_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
