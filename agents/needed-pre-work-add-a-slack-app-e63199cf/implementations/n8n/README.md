# Needed pre-work: Add a Slack App

This folder contains the **Needed pre-work: Add a Slack App** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`needed-pre-work-add-a-slack-app-e63199cf.json`](needed-pre-work-add-a-slack-app-e63199cf.json): sanitized, inactive import copy with an overview sticky note.
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
| Set me up | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Add to Google Sheets | `googleSheets` | appendOrUpdate |
| Hidden message to Slack to add feature details | `httpRequest` | POST |

## Connection map

- Switch → Add to Google Sheets (`main`, output 0, input 0)
- Webhook → Set me up (`main`, output 0, input 0)
- Set me up → Switch (`main`, output 0, input 0)
- Add to Google Sheets → Hidden message to Slack to add feature details (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0441_HTTP_GoogleSheets_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0441_HTTP_GoogleSheets_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
