# Get all scaleway server info copy

This folder contains the **Get all scaleway server info copy** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `respondToWebhook`, `set`, `splitInBatches`, `splitOut`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-all-scaleway-server-info-copy.json`](get-all-scaleway-server-info-copy.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Code | `code` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Code search Tags | `code` | Inspect parameters |
| Code search Name | `code` | Inspect parameters |
| Code search public_ip | `code` | Inspect parameters |
| Code search zone | `code` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond Error | `respondToWebhook` | Inspect parameters |
| Respond to Webhook1 | `respondToWebhook` | Inspect parameters |
| Respond to Webhook2 | `respondToWebhook` | Inspect parameters |
| Respond to Webhook3 | `respondToWebhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Get Scalway Machines | `httpRequest` | POST |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Respond to Webhook4 | `respondToWebhook` | Inspect parameters |
| Get scw instance by zone | `httpRequest` | Inspect parameters |
| Loop Over Zone Instance | `splitInBatches` | Inspect parameters |
| Get scw baremetal by zone | `httpRequest` | Inspect parameters |
| Split Out ZONE_INSTANCE | `splitOut` | Inspect parameters |
| If ZONE_BAREMETAL in ZONE_INSTANCE | `if` | Inspect parameters |

## Connection map

- Code → Switch (`main`, output 0, input 0)
- Switch → Code search Tags (`main`, output 0, input 0)
- Switch → Code search Name (`main`, output 1, input 0)
- Switch → Code search public_ip (`main`, output 2, input 0)
- Switch → Code search zone (`main`, output 3, input 0)
- Switch → Respond to Webhook4 (`main`, output 4, input 0)
- Switch → Respond Error (`main`, output 5, input 0)
- Webhook → Edit Fields (`main`, output 0, input 0)
- Edit Fields → Split Out ZONE_INSTANCE (`main`, output 0, input 0)
- Code search Name → Respond to Webhook1 (`main`, output 0, input 0)
- Code search Tags → Respond to Webhook (`main`, output 0, input 0)
- Code search zone → Respond to Webhook3 (`main`, output 0, input 0)
- Get Scalway Machines → Loop Over Items (`main`, output 0, input 0)
- Code search public_ip → Respond to Webhook2 (`main`, output 0, input 0)
- Loop Over Zone Instance → Code (`main`, output 0, input 0)
- Loop Over Zone Instance → Get scw instance by zone (`main`, output 1, input 0)
- Split Out ZONE_INSTANCE → Loop Over Zone Instance (`main`, output 0, input 0)
- Get scw instance by zone → If ZONE_BAREMETAL in ZONE_INSTANCE (`main`, output 0, input 0)
- Get scw baremetal by zone → Loop Over Zone Instance (`main`, output 0, input 0)
- If ZONE_BAREMETAL in ZONE_INSTANCE → Get scw baremetal by zone (`main`, output 0, input 0)
- If ZONE_BAREMETAL in ZONE_INSTANCE → Loop Over Zone Instance (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1946_Splitout_Webhook_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1946_Splitout_Webhook_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
