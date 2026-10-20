# Shopify order UTM to Baserow

This folder contains the **Shopify order UTM to Baserow** workflow. Its executable nodes use `baserow`, `graphql`, `if`, `noOp`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`shopify-order-utm-to-baserow.json`](shopify-order-utm-to-baserow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `baserowApi`, `httpHeaderAuth`

**Entry nodes:** Every day at 00:00

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Baserow | `baserow` | create |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Set Shopify Subdomain | `set` | Inspect parameters |
| Get orders from Shopify | `graphql` | Inspect parameters |
| Every day at 00:00 | `scheduleTrigger` | Inspect parameters |
| Split Shopify data into n8n items | `splitOut` | Inspect parameters |
| Transform incoming data structure | `set` | Inspect parameters |
| Check if "Campaign" is present | `if` | Inspect parameters |

## Connection map

- Every day at 00:00 → Set Shopify Subdomain (`main`, output 0, input 0)
- Every day at 00:00 → Get orders from Shopify (`main`, output 0, input 0)
- Get orders from Shopify → Split Shopify data into n8n items (`main`, output 0, input 0)
- Check if "Campaign" is present → Baserow (`main`, output 0, input 0)
- Check if "Campaign" is present → No Operation, do nothing (`main`, output 1, input 0)
- Split Shopify data into n8n items → Transform incoming data structure (`main`, output 0, input 0)
- Transform incoming data structure → Check if "Campaign" is present (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1780_Splitout_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1780_Splitout_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
