# Streamline Your Zoom Meetings with Secure, Automated Stripe Payments

This folder contains the **Streamline Your Zoom Meetings with Secure, Automated Stripe Payments** workflow. Its executable nodes use `formTrigger`, `gmail`, `googleSheets`, `httpRequest`, `if`, `noOp`, `set`, `stripeTrigger`, `zoom`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`streamline-your-zoom-meetings-with-secure-automated-stripe-payments.json`](streamline-your-zoom-meetings-with-secure-automated-stripe-payments.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `stripeApi`, `zoomOAuth2Api`

**Entry nodes:** Creation Form, On payment

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create Zoom meeting | `zoom` | Inspect parameters |
| Create Stripe Product | `httpRequest` | POST |
| Config | `set` | Inspect parameters |
| Send email to teacher | `gmail` | Inspect parameters |
| Create participant list | `googleSheets` | create |
| Add participant to list | `googleSheets` | append |
| Send confirmation to participant | `gmail` | Inspect parameters |
| Notify teacher | `gmail` | Inspect parameters |
| Create payment link | `httpRequest` | POST |
| Format participant | `set` | Inspect parameters |
| Format event | `set` | Inspect parameters |
| Store event | `googleSheets` | append |
| Creation Form | `formTrigger` | Inspect parameters |
| On payment | `stripeTrigger` | Inspect parameters |
| if is creation flow | `if` | Inspect parameters |
| the end | `noOp` | Inspect parameters |

## Connection map

- Config → if is creation flow (`main`, output 0, input 0)
- On payment → Config (`main`, output 0, input 0)
- Format event → Store event (`main`, output 0, input 0)
- Creation Form → Config (`main`, output 0, input 0)
- Notify teacher → the end (`main`, output 0, input 0)
- Format participant → Add participant to list (`main`, output 0, input 0)
- Create Zoom meeting → Create Stripe Product (`main`, output 0, input 0)
- Create payment link → Create participant list (`main`, output 0, input 0)
- Create payment link → Format event (`main`, output 0, input 0)
- if is creation flow → Create Zoom meeting (`main`, output 0, input 0)
- if is creation flow → Format participant (`main`, output 1, input 0)
- Create Stripe Product → Create payment link (`main`, output 0, input 0)
- Add participant to list → Send confirmation to participant (`main`, output 0, input 0)
- Create participant list → Send email to teacher (`main`, output 0, input 0)
- Send confirmation to participant → Notify teacher (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0739_HTTP_Form_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0739_HTTP_Form_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
