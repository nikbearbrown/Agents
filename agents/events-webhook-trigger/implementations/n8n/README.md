# Events Webhook Trigger

This folder contains the **Events Webhook Trigger** workflow. Its executable nodes use `aggregate`, `httpRequest`, `if`, `noOp`, `respondToWebhook`, `s3`, `set`, `slack`, `splitInBatches`, `splitOut`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`events-webhook-trigger.json`](events-webhook-trigger.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `s3`, `slackApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Parse Webhook | `set` | Inspect parameters |
| Close Modal Popup | `respondToWebhook` | Inspect parameters |
| Idea Selector Modal | `httpRequest` | POST |
| Route Message | `switch` | Inspect parameters |
| Route Message1 | `switch` | Inspect parameters |
| Create Folder | `httpRequest` | POST |
| Select Folder | `httpRequest` | POST |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Success Response | `set` | Inspect parameters |
| Check if uploaded successfully | `if` | Inspect parameters |
| move on to next | `noOp` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Route Action | `switch` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Failure Response | `set` | Inspect parameters |
| Respond to Slack Webhook - Success | `respondToWebhook` | Inspect parameters |
| Respond to Slack Webhook - No Action | `respondToWebhook` | Inspect parameters |
| Download File Binary | `httpRequest` | Inspect parameters |
| Upload to S3 Bucket | `s3` | upload |
| Post Image to Channel | `slack` | Inspect parameters |
| Split Out Files | `splitOut` | Inspect parameters |

## Connection map

- Webhook → Parse Webhook (`main`, output 0, input 0)
- Aggregate → Post Image to Channel (`main`, output 0, input 0)
- Route Action → Split Out Files (`main`, output 0, input 0)
- Parse Webhook → Route Message (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook - Success (`main`, output 0, input 0)
- Route Message → Respond to Slack Webhook - No Action (`main`, output 1, input 0)
- Route Message → Close Modal Popup (`main`, output 2, input 0)
- Route Message1 → Create Folder (`main`, output 0, input 0)
- Route Message1 → Select Folder (`main`, output 1, input 0)
- Loop Over Items → No Operation, do nothing (`main`, output 0, input 0)
- Loop Over Items → Download File Binary (`main`, output 1, input 0)
- Split Out Files → Loop Over Items (`main`, output 0, input 0)
- move on to next → Loop Over Items (`main`, output 0, input 0)
- Failure Response → move on to next (`main`, output 0, input 0)
- Success Response → move on to next (`main`, output 0, input 0)
- Close Modal Popup → Route Action (`main`, output 0, input 0)
- Upload to S3 Bucket → Check if uploaded successfully (`main`, output 0, input 0)
- Download File Binary → Upload to S3 Bucket (`main`, output 0, input 0)
- No Operation, do nothing → Aggregate (`main`, output 0, input 0)
- Check if uploaded successfully → Success Response (`main`, output 0, input 0)
- Check if uploaded successfully → Failure Response (`main`, output 1, input 0)
- Respond to Slack Webhook - Success → Idea Selector Modal (`main`, output 0, input 0)
- Respond to Slack Webhook - No Action → Route Message1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0650_Splitout_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0650_Splitout_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
