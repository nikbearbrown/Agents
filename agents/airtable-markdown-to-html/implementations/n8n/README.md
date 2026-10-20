# Airtable markdown to html

This folder contains the **Airtable markdown to html** workflow. Its executable nodes use `airtable`, `if`, `markdown`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`airtable-markdown-to-html.json`](airtable-markdown-to-html.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`

**Entry nodes:** Airtable sync video description

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check if it's 1 record or all records - Airtable | `if` | Inspect parameters |
| Get single record from airtable | `airtable` | get |
| Convert markdown to HTML1 | `markdown` | Inspect parameters |
| Convert markdown to HTML2 | `markdown` | Inspect parameters |
| Update single record in airtable | `airtable` | update |
| Update all records in airtable | `airtable` | update |
| Get all records from airtable | `airtable` | search |
| Airtable sync video description | `webhook` | Inspect parameters |

## Connection map

- Convert markdown to HTML1 → Update single record in airtable (`main`, output 0, input 0)
- Convert markdown to HTML2 → Update all records in airtable (`main`, output 0, input 0)
- Get all records from airtable → Convert markdown to HTML2 (`main`, output 0, input 0)
- Airtable sync video description → Check if it's 1 record or all records - Airtable (`main`, output 0, input 0)
- Get single record from airtable → Convert markdown to HTML1 (`main`, output 0, input 0)
- Check if it's 1 record or all records - Airtable → Get single record from airtable (`main`, output 0, input 0)
- Check if it's 1 record or all records - Airtable → Get all records from airtable (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Markdown/1540_Markdown_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Markdown/1540_Markdown_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
