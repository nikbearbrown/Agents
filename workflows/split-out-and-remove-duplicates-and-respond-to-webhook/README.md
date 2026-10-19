# split out and remove duplicates and respond to webhook

This folder contains the **split out and remove duplicates and respond to webhook** workflow. Its executable nodes use `httpRequest`, `if`, `removeDuplicates`, `respondToWebhook`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`split-out-and-remove-duplicates-and-respond-to-webhook.json`](split-out-and-remove-duplicates-and-respond-to-webhook.json): sanitized, inactive import copy with an overview sticky note.
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
| Split Out | `splitOut` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Get the website data | `httpRequest` | Inspect parameters |
| Extract the emails found | `set` | Inspect parameters |
| If contains email | `if` | Inspect parameters |

## Connection map

- Webhook → Get the website data (`main`, output 0, input 0)
- Split Out → If contains email (`main`, output 0, input 0)
- If contains email → Remove Duplicates (`main`, output 0, input 0)
- Remove Duplicates → Respond to Webhook (`main`, output 0, input 0)
- Get the website data → Extract the emails found (`main`, output 0, input 0)
- Extract the emails found → Split Out (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0434_Splitout_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0434_Splitout_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
