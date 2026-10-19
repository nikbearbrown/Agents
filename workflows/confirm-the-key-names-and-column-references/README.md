# Confirm the key names and column references

This folder contains the **Confirm the key names and column references** workflow. Its executable nodes use `airtable`, `airtableTrigger`, `httpRequest`, `if`, `set`, `spreadsheetFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`confirm-the-key-names-and-column-references.json`](confirm-the-key-names-and-column-references.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`

**Entry nodes:** New Upload

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get File ID | `airtable` | get |
| Status Failed | `httpRequest` | PATCH |
| Status Uploaded | `httpRequest` | PATCH |
| Campaign is Not Empty | `if` | Inspect parameters |
| Campaign Not Empty | `set` | Inspect parameters |
| Campaign Not Empty1 | `set` | Inspect parameters |
| Read File | `spreadsheetFile` | Inspect parameters |
| Airtable Base IDs | `set` | Inspect parameters |
| Status Processing | `httpRequest` | PATCH |
| Download File | `httpRequest` | Inspect parameters |
| Create Records | `httpRequest` | POST |
| New Upload | `airtableTrigger` | Inspect parameters |

## Connection map

- Read File → Campaign is Not Empty (`main`, output 0, input 0)
- New Upload → Airtable Base IDs (`main`, output 0, input 0)
- Get File ID → Status Processing (`main`, output 0, input 0)
- Download File → Read File (`main`, output 0, input 0)
- Create Records → Status Uploaded (`main`, output 0, input 0)
- Create Records → Status Failed (`main`, output 1, input 0)
- Airtable Base IDs → Get File ID (`main`, output 0, input 0)
- Status Processing → Download File (`main`, output 0, input 0)
- Campaign Not Empty → Create Records (`main`, output 0, input 0)
- Campaign Not Empty1 → Create Records (`main`, output 0, input 0)
- Campaign is Not Empty → Campaign Not Empty (`main`, output 0, input 0)
- Campaign is Not Empty → Campaign Not Empty1 (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0394_HTTP_Spreadsheetfile_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0394_HTTP_Spreadsheetfile_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
