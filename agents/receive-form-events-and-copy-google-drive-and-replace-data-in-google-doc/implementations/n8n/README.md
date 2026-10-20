# receive form events and copy google drive and replace data in google doc

This folder contains the **receive form events and copy google drive and replace data in google doc** workflow. Its executable nodes use `code`, `formTrigger`, `googleDrive`, `httpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-form-events-and-copy-google-drive-and-replace-data-in-google-doc.json`](receive-form-events-and-copy-google-drive-and-replace-data-in-google-doc.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `googleDriveOAuth2Api`

**Entry nodes:** Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Form | `formTrigger` | Inspect parameters |
| Copy template file | `googleDrive` | copy |
| Format form data | `code` | Inspect parameters |
| Format form data to Google Doc API | `code` | Inspect parameters |
| Replace data in Google Doc | `httpRequest` | POST |

## Connection map

- Form → Copy template file (`main`, output 0, input 0)
- Format form data → Format form data to Google Doc API (`main`, output 0, input 0)
- Copy template file → Format form data (`main`, output 0, input 0)
- Format form data to Google Doc API → Replace data in Google Doc (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0784_Code_Form_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0784_Code_Form_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
