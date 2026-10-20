# Validate Seatable Webhooks with HMAC SHA256 Authentication

This folder contains the **Validate Seatable Webhooks with HMAC SHA256 Authentication** workflow. Its executable nodes use `crypto`, `if`, `noOp`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`validate-seatable-webhooks-with-hmac-sha256-authentication.json`](validate-seatable-webhooks-with-hmac-sha256-authentication.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Seatable Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| 200 | `respondToWebhook` | Inspect parameters |
| 403 | `respondToWebhook` | Inspect parameters |
| Calculate sha256 | `crypto` | Inspect parameters |
| Seatable Webhook | `webhook` | Inspect parameters |
| Add nodes for processing | `noOp` | Inspect parameters |
| hash matches | `if` | Inspect parameters |

## Connection map

- hash matches → 200 (`main`, output 0, input 0)
- hash matches → Add nodes for processing (`main`, output 0, input 0)
- hash matches → 403 (`main`, output 1, input 0)
- Calculate sha256 → hash matches (`main`, output 0, input 0)
- Seatable Webhook → Calculate sha256 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1740_Webhook_Respondtowebhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1740_Webhook_Respondtowebhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
