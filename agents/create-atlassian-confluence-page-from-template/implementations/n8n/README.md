# Create Atlassian Confluence page from template

This folder contains the **Create Atlassian Confluence page from template** workflow. Its executable nodes use `code`, `httpRequest`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-atlassian-confluence-page-from-template.json`](create-atlassian-confluence-page-from-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Confluence: Get template content | `httpRequest` | Inspect parameters |
| Confluence: Create page from template | `httpRequest` | POST |
| Set parameters | `set` | Inspect parameters |
| Replace placeholders in template body and title | `code` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Webhook → Set parameters (`main`, output 0, input 0)
- Set parameters → Confluence: Get template content (`main`, output 0, input 0)
- Confluence: Get template content → Replace placeholders in template body and title (`main`, output 0, input 0)
- Replace placeholders in template body and title → Confluence: Create page from template (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0559_HTTP_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0559_HTTP_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
