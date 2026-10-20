# http request and get all masked emails and create random masked email

This folder contains the **http request and get all masked emails and create random masked email** workflow. Its executable nodes use `html`, `httpRequest`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-get-all-masked-emails-and-create-random-masked-email.json`](http-request-and-get-all-masked-emails-and-create-random-masked-email.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `httpHeaderAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Session | `httpRequest` | Inspect parameters |
| get all masked emails | `httpRequest` | POST |
| create random masked email | `httpRequest` | POST |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| disabled | `httpRequest` | POST |
| delete | `httpRequest` | POST |
| gather masked email list | `set` | Inspect parameters |
| create html template | `html` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Switch → create random masked email (`main`, output 0, input 0)
- Switch → create random masked email (`main`, output 1, input 0)
- Switch → delete (`main`, output 2, input 0)
- Switch → disabled (`main`, output 3, input 0)
- Switch → get all masked emails (`main`, output 4, input 0)
- delete → get all masked emails (`main`, output 0, input 0)
- Session → Switch (`main`, output 0, input 0)
- Webhook → Session (`main`, output 0, input 0)
- Webhook → Session (`main`, output 1, input 0)
- disabled → get all masked emails (`main`, output 0, input 0)
- create html template → Respond to Webhook (`main`, output 0, input 0)
- get all masked emails → gather masked email list (`main`, output 0, input 0)
- gather masked email list → create html template (`main`, output 0, input 0)
- create random masked email → get all masked emails (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0591_Webhook_Respondtowebhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0591_Webhook_Respondtowebhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
