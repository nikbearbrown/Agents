# Payment Detials are Selected

This folder contains the **Payment Detials are Selected** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `set`, `switch`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`payment-detials-are-selected.json`](payment-detials-are-selected.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Event Capture Type | `switch` | Inspect parameters |
| Get Order Details | `httpRequest` | Inspect parameters |
| Email Data | `set` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| getJSON | `httpRequest` | Inspect parameters |
| Event Capture Type1 | `switch` | Inspect parameters |
| Conver to File | `code` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |

## Connection map

- Wait → Event Capture Type (`main`, output 0, input 0)
- Webhook → Wait (`main`, output 0, input 0)
- getJSON → Conver to File (`main`, output 0, input 0)
- Email Data → Event Capture Type1 (`main`, output 0, input 0)
- Conver to File → Send Email (`main`, output 0, input 0)
- Get Order Details → Email Data (`main`, output 0, input 0)
- Event Capture Type → Get Order Details (`main`, output 0, input 0)
- Event Capture Type1 → getJSON (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0888_Wait_Code_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0888_Wait_Code_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
