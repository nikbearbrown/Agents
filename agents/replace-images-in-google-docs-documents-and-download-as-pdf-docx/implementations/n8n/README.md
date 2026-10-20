# Replace Images in Google Docs Documents and Download as PDF/Docx

This folder contains the **Replace Images in Google Docs Documents and Download as PDF/Docx** workflow. Its executable nodes use `googleDrive`, `httpRequest`, `manualTrigger`, `noOp`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`replace-images-in-google-docs-documents-and-download-as-pdf-docx.json`](replace-images-in-google-docs-documents-and-download-as-pdf-docx.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Find Image ID in Docx | `httpRequest` | Inspect parameters |
| Make file shareable publically (optional) | `googleDrive` | share |
| Image URL | `set` | Inspect parameters |
| Find & Copy Docx Template | `googleDrive` | copy |
| Own datasource | `noOp` | Inspect parameters |
| Replace Image in Docx | `httpRequest` | POST |
| Download File - Docx | `googleDrive` | download |
| Download File - PDF | `googleDrive` | download |

## Connection map

- Image URL → Find & Copy Docx Template (`main`, output 0, input 0)
- Own datasource → Image URL (`main`, output 0, input 0)
- Download File - Docx → Download File - PDF (`main`, output 0, input 0)
- Find Image ID in Docx → Replace Image in Docx (`main`, output 0, input 0)
- Replace Image in Docx → Make file shareable publically (optional) (`main`, output 0, input 0)
- Find & Copy Docx Template → Find Image ID in Docx (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Own datasource (`main`, output 0, input 0)
- Make file shareable publically (optional) → Download File - Docx (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0617_Manual_Noop_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0617_Manual_Noop_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
