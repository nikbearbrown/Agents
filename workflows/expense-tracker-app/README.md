# Expense Tracker App

This folder contains the **Expense Tracker App** workflow. Its executable nodes use `airtable`, `httpRequest`, `mindee`, `set`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`expense-tracker-app.json`](expense-tracker-app.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `mindeeReceiptApi`, `typeformApi`

**Entry nodes:** Get Receipt

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Receipt | `typeformTrigger` | Inspect parameters |
| Get Image | `httpRequest` | Inspect parameters |
| Extract Information | `mindee` | Inspect parameters |
| Set Information | `set` | Inspect parameters |
| Store Information | `airtable` | append |

## Connection map

- Get Image → Extract Information (`main`, output 0, input 0)
- Get Receipt → Get Image (`main`, output 0, input 0)
- Set Information → Store Information (`main`, output 0, input 0)
- Extract Information → Set Information (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1030_HTTP_Typeform_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1030_HTTP_Typeform_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
