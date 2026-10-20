# Slack Modal Interface

This folder contains the **Slack Modal Interface** workflow. Its executable nodes use `httpRequest`, `if`, `limit`, `respondToWebhook`, `serviceNow`, `set`, `slack`, `sort`, `splitInBatches`, `summarize`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`slack-modal-interface.json`](slack-modal-interface.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `serviceNowBasicApi`, `slackApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Parse Webhook | `set` | Inspect parameters |
| Close Modal Popup | `respondToWebhook` | Inspect parameters |
| Route Message | `switch` | Inspect parameters |
| ServiceNow Modal | `httpRequest` | POST |
| Webhook | `webhook` | Inspect parameters |
| Send 200 | `respondToWebhook` | Inspect parameters |
| ServiceNow | `serviceNow` | incident / getAll |
| Channel - Notify User no Incidents Matched | `slack` | Inspect parameters |
| DM - Notify User no Incidents Matched | `slack` | Inspect parameters |
| Were Incidents Found? | `if` | Inspect parameters |
| No Matches - Was a Channel Selected? | `if` | Inspect parameters |
| Sort by Most Recent | `sort` | Inspect parameters |
| Retain First 5 Incidents | `limit` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Format Incident Details | `set` | Inspect parameters |
| Format Slack Message | `set` | Inspect parameters |
| Concatenate Incident Details | `summarize` | Inspect parameters |
| DM - Send Matching Incidents | `slack` | Inspect parameters |
| Channel - Send Matching Incidents | `slack` | Inspect parameters |
| Was a Channel Selected? | `if` | Inspect parameters |
| Respond to Slack Webhook | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → Parse Webhook (`main`, output 0, input 0)
- ServiceNow → Were Incidents Found? (`main`, output 0, input 0)
- Parse Webhook → Route Message (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook (`main`, output 0, input 0)
- Route Message → Close Modal Popup (`main`, output 1, input 0)
- Route Message → Send 200 (`main`, output 2, input 0)
- Loop Over Items → Concatenate Incident Details (`main`, output 0, input 0)
- Loop Over Items → Format Incident Details (`main`, output 1, input 0)
- Close Modal Popup → ServiceNow (`main`, output 0, input 0)
- Sort by Most Recent → Retain First 5 Incidents (`main`, output 0, input 0)
- Format Slack Message → Was a Channel Selected? (`main`, output 0, input 0)
- Were Incidents Found? → Sort by Most Recent (`main`, output 0, input 0)
- Were Incidents Found? → No Matches - Was a Channel Selected? (`main`, output 1, input 0)
- Format Incident Details → Loop Over Items (`main`, output 0, input 0)
- Was a Channel Selected? → Channel - Send Matching Incidents (`main`, output 0, input 0)
- Was a Channel Selected? → DM - Send Matching Incidents (`main`, output 1, input 0)
- Respond to Slack Webhook → ServiceNow Modal (`main`, output 0, input 0)
- Retain First 5 Incidents → Loop Over Items (`main`, output 0, input 0)
- Concatenate Incident Details → Format Slack Message (`main`, output 0, input 0)
- No Matches - Was a Channel Selected? → Channel - Notify User no Incidents Matched (`main`, output 0, input 0)
- No Matches - Was a Channel Selected? → DM - Notify User no Incidents Matched (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0685_Limit_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0685_Limit_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
