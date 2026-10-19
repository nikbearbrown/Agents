# Automated PDF to HTML Conversion

This folder contains the **Automated PDF to HTML Conversion** workflow. Its executable nodes use `code`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `if`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-pdf-to-html-conversion.json`](automated-pdf-to-html-conversion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Google Drive Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Google Drive | `googleDrive` | Inspect parameters |
| Convert to Binary File | `code` | Inspect parameters |

## Connection map

- If → HTTP Request (`main`, output 0, input 0)
- HTTP Request → Convert to Binary File (`main`, output 0, input 0)
- Google Drive Trigger → If (`main`, output 0, input 0)
- Convert to Binary File → Google Drive (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0934_HTTP_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0934_HTTP_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
