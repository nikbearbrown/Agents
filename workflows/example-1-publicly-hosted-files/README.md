# Example 1. Publicly Hosted Files

This folder contains the **Example 1. Publicly Hosted Files** workflow. Its executable nodes use `googleDrive`, `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`example-1-publicly-hosted-files.json`](example-1-publicly-hosted-files.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `mistralCloudApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Mistral Upload | `httpRequest` | POST |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Mistral Signed URL | `httpRequest` | Inspect parameters |
| Import PDF | `googleDrive` | download |
| Import Image | `googleDrive` | download |
| Mistral Upload1 | `httpRequest` | POST |
| Mistral Signed URL1 | `httpRequest` | Inspect parameters |
| Mistral DOC OCR | `httpRequest` | POST |
| Mistral IMAGE OCR | `httpRequest` | POST |
| Document URL | `set` | Inspect parameters |
| Image URL | `set` | Inspect parameters |
| Mistral DOC OCR1 | `httpRequest` | POST |
| Mistral IMAGE OCR1 | `httpRequest` | POST |
| Document URL1 | `set` | Inspect parameters |
| Document Understanding | `httpRequest` | POST |
| Image URL1 | `set` | Inspect parameters |
| Document Mis-Understanding? | `httpRequest` | POST |

## Connection map

- Image URL → Mistral IMAGE OCR1 (`main`, output 0, input 0)
- Image URL1 → Document Mis-Understanding? (`main`, output 0, input 0)
- Import PDF → Mistral Upload (`main`, output 0, input 0)
- Document URL → Mistral DOC OCR1 (`main`, output 0, input 0)
- Import Image → Mistral Upload1 (`main`, output 0, input 0)
- Document URL1 → Document Understanding (`main`, output 0, input 0)
- Mistral Upload → Mistral Signed URL (`main`, output 0, input 0)
- Mistral Upload1 → Mistral Signed URL1 (`main`, output 0, input 0)
- Mistral Signed URL → Mistral DOC OCR (`main`, output 0, input 0)
- Mistral Signed URL1 → Mistral IMAGE OCR (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Document URL (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Image URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0778_HTTP_Stickynote_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0778_HTTP_Stickynote_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
