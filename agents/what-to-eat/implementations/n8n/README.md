# What To Eat

This folder contains the **What To Eat** workflow. Its executable nodes use `cron`, `emailSend`, `function`, `httpRequest`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`what-to-eat.json`](what-to-eat.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Cron | `cron` | Inspect parameters |
| Search Criteria | `set` | Inspect parameters |
| Set Query Values | `function` | Inspect parameters |
| Set Recipe ID Values | `function` | Inspect parameters |
| Retrieve Recipe Counts | `httpRequest` | Inspect parameters |
| Retrieve Recipes | `httpRequest` | Inspect parameters |
| Set Counts | `set` | Inspect parameters |
| Send Recipes | `emailSend` | Inspect parameters |
| Create Email Body in HTML | `function` | Inspect parameters |

## Connection map

- Cron → Search Criteria (`main`, output 0, input 0)
- Set Counts → Set Recipe ID Values (`main`, output 0, input 0)
- Search Criteria → Set Query Values (`main`, output 0, input 0)
- Retrieve Recipes → Create Email Body in HTML (`main`, output 0, input 0)
- Set Query Values → Retrieve Recipe Counts (`main`, output 0, input 0)
- Set Recipe ID Values → Retrieve Recipes (`main`, output 0, input 0)
- Retrieve Recipe Counts → Set Counts (`main`, output 0, input 0)
- Create Email Body in HTML → Send Recipes (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0084_HTTP_Cron_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0084_HTTP_Cron_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
