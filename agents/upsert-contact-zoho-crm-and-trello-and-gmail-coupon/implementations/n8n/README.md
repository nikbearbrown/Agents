# upsert contact zoho crm and trello and gmail coupon

This folder contains the **upsert contact zoho crm and trello and gmail coupon** workflow. Its executable nodes use `gmail`, `harvest`, `if`, `mailchimp`, `set`, `shopifyTrigger`, `trello`, `zohoCrm`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`upsert-contact-zoho-crm-and-trello-and-gmail-coupon.json`](upsert-contact-zoho-crm-and-trello-and-gmail-coupon.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `harvestApi`, `mailchimpApi`, `shopifyApi`, `trelloApi`, `zohoOAuth2Api`

**Entry nodes:** order created

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Zoho | `zohoCrm` | contact / upsert |
| Trello | `trello` | Inspect parameters |
| Set fields | `set` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Gmail - coupon | `gmail` | message |
| Gmail - thankyou | `gmail` | message |
| Mailchimp | `mailchimp` | memberTag |
| order created | `shopifyTrigger` | Inspect parameters |
| Harvest | `harvest` | invoice / create |

## Connection map

- IF → Gmail - coupon (`main`, output 0, input 0)
- IF → Gmail - thankyou (`main`, output 1, input 0)
- Harvest → Trello (`main`, output 0, input 0)
- Set fields → Harvest (`main`, output 0, input 0)
- Set fields → IF (`main`, output 0, input 0)
- Set fields → Zoho (`main`, output 0, input 0)
- order created → Set fields (`main`, output 0, input 0)
- Gmail - coupon → Mailchimp (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Zohocrm/0086_Zohocrm_Trello_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Zohocrm/0086_Zohocrm_Trello_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
