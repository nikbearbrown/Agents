# 🔐 How to Get Your Product Hunt Token

This folder contains the **🔐 How to Get Your Product Hunt Token** workflow. Its executable nodes use `code`, `function`, `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`how-to-get-your-product-hunt-token.json`](how-to-get-your-product-hunt-token.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Daily Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Daily Trigger1 | `scheduleTrigger` | Inspect parameters |
| Set Date1 | `set` | Inspect parameters |
| Fetches today’s Product Hunt posts via API. | `httpRequest` | POST |
| Extracts Product Info | `code` | Inspect parameters |
| Resolve Website Redirection | `httpRequest` | Inspect parameters |
| Data  2 (website url) | `set` | Inspect parameters |
| Data 1 (product info) | `set` | Inspect parameters |
| Merge Data | `function` | Inspect parameters |
| Appends all details | `googleSheets` | appendOrUpdate |

## Connection map

- Set Date1 → Fetches today’s Product Hunt posts via API. (`main`, output 0, input 0)
- Merge Data → Appends all details (`main`, output 0, input 0)
- Daily Trigger1 → Set Date1 (`main`, output 0, input 0)
- Data  2 (website url) → Merge Data (`main`, output 0, input 0)
- Data 1 (product info) → Merge Data (`main`, output 0, input 0)
- Extracts Product Info → Resolve Website Redirection (`main`, output 0, input 0)
- Extracts Product Info → Data 1 (product info) (`main`, output 0, input 0)
- Resolve Website Redirection → Data  2 (website url) (`main`, output 0, input 0)
- Fetches today’s Product Hunt posts via API. → Extracts Product Info (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0863_Code_Schedule_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0863_Code_Schedule_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
