# Events Webhook Trigger

This folder contains the **Events Webhook Trigger** workflow. Its executable nodes use `executeWorkflow`, `httpRequest`, `if`, `merge`, `noOp`, `openAi`, `respondToWebhook`, `set`, `slack`, `switch`, `venafiTlsProtectCloud`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`events-webhook-trigger-8e718da6.json`](events-webhook-trigger-8e718da6.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `slackApi`, `venafiTlsProtectCloudApi`, `virusTotalApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Venafi TLS Protect Cloud | `venafiTlsProtectCloud` | Inspect parameters |
| Parse Webhook | `set` | Inspect parameters |
| Close Modal Popup | `respondToWebhook` | Inspect parameters |
| Respond to Slack Webhook - Vulnerability | `respondToWebhook` | Inspect parameters |
| Venafi Request Certificate | `httpRequest` | POST |
| Extract Fields | `set` | Inspect parameters |
| Get Slack User ID | `set` | Inspect parameters |
| Translate Slack User ID to Email | `executeWorkflow` | Inspect parameters |
| VirusTotal HTTP Request | `httpRequest` | GET |
| Summarize output to save on tokens | `set` | Inspect parameters |
| Auto Issue Certificate Based on 0 Malicious Reports | `if` | Inspect parameters |
| Auto Issue Certificate | `noOp` | Inspect parameters |
| Generate Report For Manual Approval | `noOp` | Inspect parameters |
| Get Slack Team ID | `set` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Merge User and Team Data | `merge` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Merge Requestor and VT Data | `merge` | Inspect parameters |
| Send Auto Generated Confirmation | `slack` | Inspect parameters |
| Send Message Request for Manual Approval | `slack` | Inspect parameters |
| Route Message | `switch` | Inspect parameters |
| Venafi TLS Protect Cloud1 | `venafiTlsProtectCloud` | Inspect parameters |
| Send Auto Generated Confirmation1 | `slack` | Inspect parameters |
| Manual Issue Certificate | `noOp` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to webhook success | `respondToWebhook` | Inspect parameters |

## Connection map

- OpenAI → Send Message Request for Manual Approval (`main`, output 0, input 0)
- Webhook → Parse Webhook (`main`, output 0, input 0)
- Parse Webhook → Route Message (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook - Vulnerability (`main`, output 0, input 0)
- Route Message → Close Modal Popup (`main`, output 1, input 0)
- Route Message → Respond to webhook success (`main`, output 2, input 0)
- Extract Fields → VirusTotal HTTP Request (`main`, output 0, input 0)
- Execute Workflow → Merge User and Team Data (`main`, output 0, input 1)
- Close Modal Popup → Extract Fields (`main`, output 0, input 0)
- Close Modal Popup → Get Slack User ID (`main`, output 0, input 0)
- Close Modal Popup → Get Slack Team ID (`main`, output 0, input 0)
- Get Slack Team ID → Execute Workflow (`main`, output 0, input 0)
- Get Slack User ID → Translate Slack User ID to Email (`main`, output 0, input 0)
- Auto Issue Certificate → Venafi TLS Protect Cloud (`main`, output 0, input 0)
- VirusTotal HTTP Request → Summarize output to save on tokens (`main`, output 0, input 0)
- Manual Issue Certificate → Venafi TLS Protect Cloud1 (`main`, output 0, input 0)
- Merge User and Team Data → Merge Requestor and VT Data (`main`, output 0, input 1)
- Venafi TLS Protect Cloud → Send Auto Generated Confirmation (`main`, output 0, input 0)
- Venafi TLS Protect Cloud1 → Send Auto Generated Confirmation1 (`main`, output 0, input 0)
- Respond to webhook success → Manual Issue Certificate (`main`, output 0, input 0)
- Merge Requestor and VT Data → Auto Issue Certificate Based on 0 Malicious Reports (`main`, output 0, input 0)
- Translate Slack User ID to Email → Merge User and Team Data (`main`, output 0, input 0)
- Summarize output to save on tokens → Merge Requestor and VT Data (`main`, output 0, input 0)
- Generate Report For Manual Approval → OpenAI (`main`, output 0, input 0)
- Respond to Slack Webhook - Vulnerability → Venafi Request Certificate (`main`, output 0, input 0)
- Auto Issue Certificate Based on 0 Malicious Reports → Auto Issue Certificate (`main`, output 0, input 0)
- Auto Issue Certificate Based on 0 Malicious Reports → Generate Report For Manual Approval (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0581_Webhook_Slack_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0581_Webhook_Slack_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
