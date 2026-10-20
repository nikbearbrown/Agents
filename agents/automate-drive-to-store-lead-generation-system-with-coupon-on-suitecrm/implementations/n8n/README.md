# Automate Drive-To-Store Lead Generation System (with coupon) on SuiteCRM

This folder contains the **Automate Drive-To-Store Lead Generation System (with coupon) on SuiteCRM** workflow. Its executable nodes use `formTrigger`, `googleSheets`, `httpRequest`, `if`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-drive-to-store-lead-generation-system-with-coupon-on-suitecrm.json`](automate-drive-to-store-lead-generation-system-with-coupon-on-suitecrm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** Webhook, On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Token SuiteCRM | `httpRequest` | Inspect parameters |
| Create Lead SuiteCRM | `httpRequest` | POST |
| Webhook | `webhook` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Duplicate Lead? | `googleSheets` | Inspect parameters |
| Form Fields | `set` | Inspect parameters |
| Get Coupon | `googleSheets` | Inspect parameters |
| Respond OK | `respondToWebhook` | Inspect parameters |
| Respond KO | `respondToWebhook` | Inspect parameters |
| Is Duplicate? | `if` | Inspect parameters |
| Update Lead | `googleSheets` | update |

## Connection map

- Get Coupon → Token SuiteCRM (`main`, output 0, input 0)
- Form Fields → Duplicate Lead? (`main`, output 0, input 0)
- Is Duplicate? → Get Coupon (`main`, output 1, input 0)
- Token SuiteCRM → Create Lead SuiteCRM (`main`, output 0, input 0)
- Duplicate Lead? → Is Duplicate? (`main`, output 0, input 0)
- On form submission → Form Fields (`main`, output 0, input 0)
- Create Lead SuiteCRM → Update Lead (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0722_Webhook_Respondtowebhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0722_Webhook_Respondtowebhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
