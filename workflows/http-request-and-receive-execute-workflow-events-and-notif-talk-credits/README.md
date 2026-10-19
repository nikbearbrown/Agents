# http request and receive execute workflow events and notif talk credits

This folder contains the **http request and receive execute workflow events and notif talk credits** workflow. Its executable nodes use `executeWorkflowTrigger`, `httpRequest`, `if`, `sendInBlue`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-receive-execute-workflow-events-and-notif-talk-credits.json`](http-request-and-receive-execute-workflow-events-and-notif-talk-credits.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Tally Forms Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Token SuiteCRM | `httpRequest` | Inspect parameters |
| CaptainMail | `httpRequest` | Inspect parameters |
| If mail ok | `if` | Inspect parameters |
| If Credits OK | `if` | Inspect parameters |
| Tally Forms Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Notif Talk credits | `httpRequest` | Inspect parameters |
| Notif Talk bad email | `httpRequest` | Inspect parameters |
| Create Lead SuiteCRM | `httpRequest` | POST |
| Notif Talk Lead created | `httpRequest` | Inspect parameters |
| Brevo Create Contact | `sendInBlue` | contact |

## Connection map

- If mail ok → Notif Talk bad email (`main`, output 0, input 0)
- If mail ok → Token SuiteCRM (`main`, output 1, input 0)
- CaptainMail → If Credits OK (`main`, output 0, input 0)
- If Credits OK → Notif Talk credits (`main`, output 0, input 0)
- If Credits OK → If mail ok (`main`, output 1, input 0)
- Token SuiteCRM → Create Lead SuiteCRM (`main`, output 0, input 0)
- Notif Talk credits → If mail ok (`main`, output 0, input 0)
- Tally Forms Trigger → CaptainMail (`main`, output 0, input 0)
- Brevo Create Contact → Notif Talk Lead created (`main`, output 0, input 0)
- Create Lead SuiteCRM → Brevo Create Contact (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0505_HTTP_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0505_HTTP_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
