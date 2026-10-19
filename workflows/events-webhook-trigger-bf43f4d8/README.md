# Events Webhook Trigger

This folder contains the **Events Webhook Trigger** workflow. Its executable nodes use `executeWorkflow`, `httpRequest`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`events-webhook-trigger-bf43f4d8.json`](events-webhook-trigger-bf43f4d8.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Parse Webhook | `set` | Inspect parameters |
| Qualys Create Report | `executeWorkflow` | Inspect parameters |
| Required Report Variables | `set` | Inspect parameters |
| Qualys Start Vulnerability Scan | `executeWorkflow` | Inspect parameters |
| Scan Report Task Modal | `httpRequest` | POST |
| Vuln Scan Modal | `httpRequest` | POST |
| Route Message | `switch` | Inspect parameters |
| Required Scan Variables | `set` | Inspect parameters |
| Route Submission | `switch` | Inspect parameters |
| Close Modal Popup | `respondToWebhook` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Slack Webhook - Vulnerability | `respondToWebhook` | Inspect parameters |
| Respond to Slack Webhook - Report | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → Parse Webhook (`main`, output 0, input 0)
- Parse Webhook → Route Message (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook - Vulnerability (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook - Report (`main`, output 1, input 0)
- Route Message → Close Modal Popup (`main`, output 2, input 0)
- Route Submission → Required Scan Variables (`main`, output 0, input 0)
- Route Submission → Required Report Variables (`main`, output 1, input 0)
- Close Modal Popup → Route Submission (`main`, output 0, input 0)
- Required Scan Variables → Qualys Start Vulnerability Scan (`main`, output 0, input 0)
- Required Report Variables → Qualys Create Report (`main`, output 0, input 0)
- Respond to Slack Webhook - Report → Scan Report Task Modal (`main`, output 0, input 0)
- Respond to Slack Webhook - Vulnerability → Vuln Scan Modal (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0619_Webhook_Respondtowebhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0619_Webhook_Respondtowebhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
