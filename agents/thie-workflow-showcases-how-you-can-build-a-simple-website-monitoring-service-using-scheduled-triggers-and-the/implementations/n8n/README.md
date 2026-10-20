# Thie workflow showcases how you can build a simple website monitoring service using Scheduled Triggers and the HTTP Requests node.

This folder contains the **Thie workflow showcases how you can build a simple website monitoring service using Scheduled Triggers and the HTTP Requests node.** workflow. Its executable nodes use `gmail`, `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`thie-workflow-showcases-how-you-can-build-a-simple-website-monitoring-service-using-scheduled-triggers-and-the.json`](thie-workflow-showcases-how-you-can-build-a-simple-website-monitoring-service-using-scheduled-triggers-and-the.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `slackApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Calculate Status | `set` | Inspect parameters |
| Get Sites | `googleSheets` | Inspect parameters |
| Send Chat Alert | `slack` | Inspect parameters |
| Send Email Alert | `gmail` | Inspect parameters |
| Log Uptime Event | `googleSheets` | append |
| Update Site Status | `googleSheets` | appendOrUpdate |
| Perform Site Test | `httpRequest` | Inspect parameters |
| For Each Site... | `splitInBatches` | Inspect parameters |
| Status Router | `switch` | Inspect parameters |

## Connection map

- Get Sites → For Each Site... (`main`, output 0, input 0)
- Status Router → Log Uptime Event (`main`, output 0, input 0)
- Status Router → Send Email Alert (`main`, output 1, input 0)
- Status Router → Log Uptime Event (`main`, output 1, input 0)
- Status Router → Log Uptime Event (`main`, output 2, input 0)
- Status Router → Send Email Alert (`main`, output 2, input 0)
- Status Router → Send Email Alert (`main`, output 3, input 0)
- Status Router → Log Uptime Event (`main`, output 3, input 0)
- Calculate Status → Status Router (`main`, output 0, input 0)
- For Each Site... → Perform Site Test (`main`, output 1, input 0)
- Log Uptime Event → Update Site Status (`main`, output 0, input 0)
- Schedule Trigger → Get Sites (`main`, output 0, input 0)
- Send Email Alert → Send Chat Alert (`main`, output 0, input 0)
- Perform Site Test → Calculate Status (`main`, output 0, input 0)
- Update Site Status → For Each Site... (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0529_Schedule_Slack_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0529_Schedule_Slack_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
