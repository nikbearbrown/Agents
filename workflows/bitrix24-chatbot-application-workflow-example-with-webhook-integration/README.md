# Bitrix24 Chatbot Application Workflow example with Webhook Integration

This folder contains the **Bitrix24 Chatbot Application Workflow example with Webhook Integration** workflow. Its executable nodes use `function`, `httpRequest`, `if`, `noOp`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`bitrix24-chatbot-application-workflow-example-with-webhook-integration.json`](bitrix24-chatbot-application-workflow-example-with-webhook-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Bitrix24 Handler

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Bitrix24 Handler | `webhook` | Inspect parameters |
| Credentials | `set` | Inspect parameters |
| Validate Token | `if` | Inspect parameters |
| Route Event | `switch` | Inspect parameters |
| Process Message | `function` | Inspect parameters |
| Process Join | `function` | Inspect parameters |
| Process Install | `function` | Inspect parameters |
| Register Bot | `httpRequest` | POST |
| Send Message | `httpRequest` | POST |
| Send Join Message | `httpRequest` | POST |
| Process Delete | `noOp` | Inspect parameters |
| Success Response | `respondToWebhook` | Inspect parameters |
| Error Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Credentials → Validate Token (`main`, output 0, input 0)
- Route Event → Process Message (`main`, output 0, input 0)
- Route Event → Process Join (`main`, output 1, input 0)
- Route Event → Process Install (`main`, output 2, input 0)
- Route Event → Process Delete (`main`, output 3, input 0)
- Process Join → Send Join Message (`main`, output 0, input 0)
- Register Bot → Success Response (`main`, output 0, input 0)
- Send Message → Success Response (`main`, output 0, input 0)
- Process Delete → Success Response (`main`, output 0, input 0)
- Validate Token → Route Event (`main`, output 0, input 0)
- Validate Token → Error Response (`main`, output 1, input 0)
- Process Install → Register Bot (`main`, output 0, input 0)
- Process Message → Send Message (`main`, output 0, input 0)
- Bitrix24 Handler → Credentials (`main`, output 0, input 0)
- Send Join Message → Success Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1354_HTTP_Respondtowebhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1354_HTTP_Respondtowebhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
