# On new Stripe Invoice Payment update Hubspot and notify the team in Slack

This folder contains the **On new Stripe Invoice Payment update Hubspot and notify the team in Slack** workflow. Its executable nodes use `hubspot`, `if`, `slack`, `stripeTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`on-new-stripe-invoice-payment-update-hubspot-and-notify-the-team-in-slack.json`](on-new-stripe-invoice-payment-update-hubspot-and-notify-the-team-in-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotApi`, `hubspotOAuth2Api`, `slackApi`, `stripeApi`

**Entry nodes:** When Invoice Paid

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Invoice Paid | `stripeTrigger` | Inspect parameters |
| Update Deal to Paid | `hubspot` | update |
| Find Deal based on PO Number | `hubspot` | search |
| If no PO Number | `if` | Inspect parameters |
| If no deal found for PO | `if` | Inspect parameters |
| Send invoice paid message | `slack` | Inspect parameters |
| Send no PO Message | `slack` | Inspect parameters |
| Send Deal not found message | `slack` | Inspect parameters |

## Connection map

- If no PO Number → Send no PO Message (`main`, output 0, input 0)
- If no PO Number → Find Deal based on PO Number (`main`, output 1, input 0)
- When Invoice Paid → If no PO Number (`main`, output 0, input 0)
- Update Deal to Paid → Send invoice paid message (`main`, output 0, input 0)
- If no deal found for PO → Send Deal not found message (`main`, output 0, input 0)
- If no deal found for PO → Update Deal to Paid (`main`, output 1, input 0)
- Find Deal based on PO Number → If no deal found for PO (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0008_Slack_Stripe_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0008_Slack_Stripe_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
