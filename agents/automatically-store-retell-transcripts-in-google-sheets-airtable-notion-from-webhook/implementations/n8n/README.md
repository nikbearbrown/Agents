# Automatically store Retell transcripts in Google Sheets/Airtable/Notion from webhook

This folder contains the **Automatically store Retell transcripts in Google Sheets/Airtable/Notion from webhook** workflow. Its executable nodes use `airtable`, `filter`, `googleSheets`, `notion`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automatically-store-retell-transcripts-in-google-sheets-airtable-notion-from-webhook.json`](automatically-store-retell-transcripts-in-google-sheets-airtable-notion-from-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googleSheetsOAuth2Api`, `notionApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Set fields to export | `set` | Inspect parameters |
| Save to Airtable | `airtable` | create |
| Save to Excel | `googleSheets` | append |
| Save to Notion | `notion` | databasePage |
| Filter - only call ended | `filter` | Inspect parameters |

## Connection map

- Webhook → Filter - only call ended (`main`, output 0, input 0)
- Set fields to export → Save to Excel (`main`, output 0, input 0)
- Set fields to export → Save to Airtable (`main`, output 0, input 0)
- Set fields to export → Save to Notion (`main`, output 0, input 0)
- Filter - only call ended → Set fields to export (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0845_Webhook_Filter_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0845_Webhook_Filter_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
