# Basic PDF Digital Sign Service

This folder contains the **Basic PDF Digital Sign Service** workflow. Its executable nodes use `code`, `convertToFile`, `if`, `readWriteFile`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`basic-pdf-digital-sign-service.json`](basic-pdf-digital-sign-service.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** API POST Endpoint, API GET Endpoint

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Validate Key Gen Params | `code` | Inspect parameters |
| Validate PDF Sign Params | `code` | Inspect parameters |
| Validate PDF Upload | `code` | Inspect parameters |
| Validate Key Upload | `code` | Inspect parameters |
| Generate Keys | `code` | Inspect parameters |
| Sign PDF | `code` | Inspect parameters |
| Prepare Success Response | `set` | Inspect parameters |
| Switch Operation | `switch` | Inspect parameters |
| Switch Upload Type | `switch` | Inspect parameters |
| Prepare input params | `set` | Inspect parameters |
| set file path | `set` | Inspect parameters |
| Convert PDF to File | `convertToFile` | toBinary |
| Write PDF File to Disk | `readWriteFile` | write |
| Read PDF File from Disk | `readWriteFile` | Inspect parameters |
| Convert PFX to File | `convertToFile` | toBinary |
| Write PFX File to Disk | `readWriteFile` | write |
| Read PFX File from Disk | `readWriteFile` | Inspect parameters |
| Check PDF file is OK | `set` | Inspect parameters |
| Check PFX file is OK | `set` | Inspect parameters |
| check success | `if` | Inspect parameters |
| set downlowd file info | `set` | Inspect parameters |
| Read download file from Disk | `readWriteFile` | Inspect parameters |
| API POST Endpoint | `webhook` | Inspect parameters |
| API GET Endpoint | `webhook` | Inspect parameters |
| POST Success Response | `respondToWebhook` | Inspect parameters |
| POST Error Response | `respondToWebhook` | Inspect parameters |
| GET Respond to Webhook | `respondToWebhook` | Inspect parameters |

## Connection map

- Sign PDF → check success (`main`, output 0, input 0)
- Generate Keys → check success (`main`, output 0, input 0)
- check success → Prepare Success Response (`main`, output 0, input 0)
- check success → POST Error Response (`main`, output 1, input 0)
- set file path → Switch Operation (`main`, output 0, input 0)
- API GET Endpoint → set file path (`main`, output 0, input 0)
- Switch Operation → Prepare input params (`main`, output 0, input 0)
- Switch Operation → Validate Key Gen Params (`main`, output 1, input 0)
- Switch Operation → Validate PDF Sign Params (`main`, output 2, input 0)
- Switch Operation → set downlowd file info (`main`, output 3, input 0)
- API POST Endpoint → set file path (`main`, output 0, input 0)
- Switch Upload Type → Validate PDF Upload (`main`, output 0, input 0)
- Switch Upload Type → Validate Key Upload (`main`, output 1, input 0)
- Convert PDF to File → Write PDF File to Disk (`main`, output 0, input 0)
- Convert PFX to File → Write PFX File to Disk (`main`, output 0, input 0)
- Validate Key Upload → Convert PFX to File (`main`, output 0, input 0)
- Validate PDF Upload → Convert PDF to File (`main`, output 0, input 0)
- Check PDF file is OK → check success (`main`, output 0, input 0)
- Check PFX file is OK → check success (`main`, output 0, input 0)
- Prepare input params → Switch Upload Type (`main`, output 0, input 0)
- Write PDF File to Disk → Read PDF File from Disk (`main`, output 0, input 0)
- Write PFX File to Disk → Read PFX File from Disk (`main`, output 0, input 0)
- set downlowd file info → Read download file from Disk (`main`, output 0, input 0)
- Read PDF File from Disk → Check PDF file is OK (`main`, output 0, input 0)
- Read PFX File from Disk → Check PFX file is OK (`main`, output 0, input 0)
- Validate Key Gen Params → Generate Keys (`main`, output 0, input 0)
- Prepare Success Response → POST Success Response (`main`, output 0, input 0)
- Validate PDF Sign Params → Sign PDF (`main`, output 0, input 0)
- Read download file from Disk → GET Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1722_Webhook_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1722_Webhook_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
