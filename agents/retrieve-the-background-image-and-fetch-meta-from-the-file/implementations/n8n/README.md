# Retrieve the Background Image and fetch Meta from the File

This folder contains the **Retrieve the Background Image and fetch Meta from the File** workflow. Its executable nodes use `code`, `editImage`, `httpRequest`, `manualTrigger`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`retrieve-the-background-image-and-fetch-meta-from-the-file.json`](retrieve-the-background-image-and-fetch-meta-from-the-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Get Meta BG | `editImage` | information |
| Nest Top Meta | `set` | Inspect parameters |
| Nest Bg Meta | `set` | Inspect parameters |
| Calculate Center | `code` | Inspect parameters |
| Get Logo for the Watermark | `httpRequest` | Inspect parameters |
| Get the Image for Background | `httpRequest` | Inspect parameters |
| Wait for both Images and merge Binary in one Item | `merge` | Inspect parameters |
| Rename Image Binary Top Image | `code` | Inspect parameters |
| Rename Image Binary Background Image | `code` | Inspect parameters |
| Get Meta Top | `editImage` | information |
| Let "top" overlay "bg" | `editImage` | composite |

## Connection map

- Get Meta BG → Nest Bg Meta (`main`, output 0, input 0)
- Get Meta Top → Nest Top Meta (`main`, output 0, input 0)
- Nest Bg Meta → Rename Image Binary Background Image (`main`, output 0, input 0)
- Nest Top Meta → Rename Image Binary Top Image (`main`, output 0, input 0)
- Calculate Center → Let "top" overlay "bg" (`main`, output 0, input 0)
- Get Logo for the Watermark → Get Meta Top (`main`, output 0, input 0)
- Get the Image for Background → Get Meta BG (`main`, output 0, input 0)
- Rename Image Binary Top Image → Wait for both Images and merge Binary in one Item (`main`, output 0, input 1)
- When clicking "Test workflow" → Get the Image for Background (`main`, output 0, input 0)
- When clicking "Test workflow" → Get Logo for the Watermark (`main`, output 0, input 0)
- Rename Image Binary Background Image → Wait for both Images and merge Binary in one Item (`main`, output 0, input 0)
- Wait for both Images and merge Binary in one Item → Calculate Center (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0598_Code_Editimage_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0598_Code_Editimage_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
