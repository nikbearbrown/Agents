# Baserow markdown to html

This folder contains the **Baserow markdown to html** workflow. Its executable nodes use `baserow`, `if`, `markdown`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`baserow-markdown-to-html.json`](baserow-markdown-to-html.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `baserowApi`

**Entry nodes:** Baserow sync video description

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get single record from baserow | `baserow` | get |
| Update single record in baserow | `baserow` | update |
| Update all records in baserow | `baserow` | update |
| Check if it's 1 record or all records - Baserow | `if` | Inspect parameters |
| Get all records from baserow | `baserow` | Inspect parameters |
| Baserow sync video description | `webhook` | Inspect parameters |
| Convert markdown to HTML (single) | `markdown` | Inspect parameters |
| Convert markdown to HTML (all records) | `markdown` | Inspect parameters |

## Connection map

- Get all records from baserow → Convert markdown to HTML (all records) (`main`, output 0, input 0)
- Baserow sync video description → Check if it's 1 record or all records - Baserow (`main`, output 0, input 0)
- Get single record from baserow → Convert markdown to HTML (single) (`main`, output 0, input 0)
- Convert markdown to HTML (single) → Update single record in baserow (`main`, output 0, input 0)
- Convert markdown to HTML (all records) → Update all records in baserow (`main`, output 0, input 0)
- Check if it's 1 record or all records - Baserow → Get single record from baserow (`main`, output 0, input 0)
- Check if it's 1 record or all records - Baserow → Get all records from baserow (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Baserow/1822_Baserow_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Baserow/1822_Baserow_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
