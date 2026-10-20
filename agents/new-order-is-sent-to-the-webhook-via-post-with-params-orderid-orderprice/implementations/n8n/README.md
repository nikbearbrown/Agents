# New order is sent to the Webhook via POST with params {orderID, orderPrice}

This folder contains the **New order is sent to the Webhook via POST with params {orderID, orderPrice}** workflow. Its executable nodes use `airtable`, `code`, `gmail`, `html`, `scheduleTrigger`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`new-order-is-sent-to-the-webhook-via-post-with-params-orderid-orderprice.json`](new-order-is-sent-to-the-webhook-via-post-with-params-orderid-orderprice.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`

**Entry nodes:** Everyday at 7PM, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Everyday at 7PM | `scheduleTrigger` | Inspect parameters |
| Airtable Get Today's Orders | `airtable` | search |
| Yesterday Date | `code` | Inspect parameters |
| HTML | `html` | Inspect parameters |
| Set Order Fields | `set` | Inspect parameters |
| Send to Gmail | `gmail` | Inspect parameters |
| Store Order | `airtable` | create |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- HTML → Send to Gmail (`main`, output 0, input 0)
- Webhook → Set Order Fields (`main`, output 0, input 0)
- Yesterday Date → Airtable Get Today's Orders (`main`, output 0, input 0)
- Everyday at 7PM → Yesterday Date (`main`, output 0, input 0)
- Set Order Fields → Store Order (`main`, output 0, input 0)
- Airtable Get Today's Orders → HTML (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0571_Code_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0571_Code_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
