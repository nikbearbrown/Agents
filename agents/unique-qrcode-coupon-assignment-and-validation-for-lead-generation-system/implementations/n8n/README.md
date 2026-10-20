# Unique QRcode coupon assignment and validation for Lead Generation system

This folder contains the **Unique QRcode coupon assignment and validation for Lead Generation system** workflow. Its executable nodes use `emailSend`, `formTrigger`, `googleSheets`, `httpRequest`, `if`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`unique-qrcode-coupon-assignment-and-validation-for-lead-generation-system.json`](unique-qrcode-coupon-assignment-and-validation-for-lead-generation-system.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `smtp`

**Entry nodes:** Webhook, On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| If | `if` | Inspect parameters |
| Token SuiteCRM | `httpRequest` | Inspect parameters |
| Create Lead SuiteCRM | `httpRequest` | POST |
| On form submission | `formTrigger` | Inspect parameters |
| Duplicate Lead? | `googleSheets` | Inspect parameters |
| Form Fields | `set` | Inspect parameters |
| Get Coupon | `googleSheets` | Inspect parameters |
| Update Sheet | `googleSheets` | update |
| Is Duplicate? | `if` | Inspect parameters |
| Get QR | `httpRequest` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Update Lead | `httpRequest` | PATCH |
| Not used? | `if` | Inspect parameters |
| Coupon OK | `respondToWebhook` | Inspect parameters |
| No coupon | `respondToWebhook` | Inspect parameters |
| Coupon KO | `respondToWebhook` | Inspect parameters |
| Token SuiteCRM 1 | `httpRequest` | Inspect parameters |
| Set coupon | `set` | Inspect parameters |
| Get Lead | `googleSheets` | Inspect parameters |
| Update coupon used | `googleSheets` | update |

## Connection map

- If → Get Lead (`main`, output 0, input 0)
- If → No coupon (`main`, output 1, input 0)
- Get QR → Send Email (`main`, output 0, input 0)
- Webhook → Set coupon (`main`, output 0, input 0)
- Get Lead → Not used? (`main`, output 0, input 0)
- Not used? → Token SuiteCRM 1 (`main`, output 0, input 0)
- Not used? → Coupon KO (`main`, output 1, input 0)
- Get Coupon → Token SuiteCRM (`main`, output 0, input 0)
- Set coupon → If (`main`, output 0, input 0)
- Form Fields → Duplicate Lead? (`main`, output 0, input 0)
- Update Lead → Update coupon used (`main`, output 0, input 0)
- Update Sheet → Get QR (`main`, output 0, input 0)
- Is Duplicate? → Get Coupon (`main`, output 1, input 0)
- Token SuiteCRM → Create Lead SuiteCRM (`main`, output 0, input 0)
- Duplicate Lead? → Is Duplicate? (`main`, output 0, input 0)
- Token SuiteCRM 1 → Update Lead (`main`, output 0, input 0)
- On form submission → Form Fields (`main`, output 0, input 0)
- Update coupon used → Coupon OK (`main`, output 0, input 0)
- Create Lead SuiteCRM → Update Sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1855_Webhook_Respondtowebhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1855_Webhook_Respondtowebhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
