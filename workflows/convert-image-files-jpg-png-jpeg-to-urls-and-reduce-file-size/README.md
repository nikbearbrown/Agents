# Convert Image Files (JPG, PNG, JPEG) to URLs and Reduce File Size

This folder contains the **Convert Image Files (JPG, PNG, JPEG) to URLs and Reduce File Size** workflow. Its executable nodes use `httpRequest`, `noOp`, `openAi`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`convert-image-files-jpg-png-jpeg-to-urls-and-reduce-file-size.json`](convert-image-files-jpg-png-jpeg-to-urls-and-reduce-file-size.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Upload Img to ImgBB for URL | `httpRequest` | POST |
| ReSmush.it Image Optimisation | `httpRequest` | Inspect parameters |
| Store Optimised Image ImgBB | `httpRequest` | POST |
| Set image description | `set` | Inspect parameters |
| Generate Image | `openAi` | image |
| No Operation, do nothing | `noOp` | Inspect parameters |

## Connection map

- Generate Image → Upload Img to ImgBB for URL (`main`, output 0, input 0)
- Set image description → Generate Image (`main`, output 0, input 0)
- Store Optimised Image ImgBB → No Operation, do nothing (`main`, output 0, input 0)
- Upload Img to ImgBB for URL → ReSmush.it Image Optimisation (`main`, output 0, input 0)
- ReSmush.it Image Optimisation → Store Optimised Image ImgBB (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0622_HTTP_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0622_HTTP_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
