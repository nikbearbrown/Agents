# Independent "Async" Process

This folder contains the **Independent "Async" Process** workflow. Its executable nodes use `httpRequest`, `manualTrigger`, `respondToWebhook`, `set`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`independent-async-process.json`](independent-async-process.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’, Receive Input from External, Independent Process, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| HTTP Request - Initiate Independent Process | `httpRequest` | POST |
| HTTP Request - Resume Other Workflow Execution | `httpRequest` | POST |
| This Node Can Access Primary and Secondary | `set` | Inspect parameters |
| Set Primary Execution Context | `set` | Inspect parameters |
| Receive Input from External, Independent Process | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Simulate Event that Hits the 2nd Trigger/Flow | `httpRequest` | POST |
| Simulate some Consumed Service Time | `wait` | Inspect parameters |
| HTTP Request - Get A Random Joke | `httpRequest` | Inspect parameters |
| Demo "Trigger" Callback Setup | `set` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Wait → This Node Can Access Primary and Secondary (`main`, output 0, input 0)
- Webhook → Respond to Webhook (`main`, output 0, input 0)
- Respond to Webhook → Demo "Trigger" Callback Setup (`main`, output 0, input 0)
- Demo "Trigger" Callback Setup → HTTP Request - Get A Random Joke (`main`, output 0, input 0)
- Set Primary Execution Context → HTTP Request - Initiate Independent Process (`main`, output 0, input 0)
- HTTP Request - Get A Random Joke → Simulate some Consumed Service Time (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Primary Execution Context (`main`, output 0, input 0)
- Simulate some Consumed Service Time → Simulate Event that Hits the 2nd Trigger/Flow (`main`, output 0, input 0)
- HTTP Request - Initiate Independent Process → Wait (`main`, output 0, input 0)
- Receive Input from External, Independent Process → HTTP Request - Resume Other Workflow Execution (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0716_Wait_Webhook_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0716_Wait_Webhook_Process_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
