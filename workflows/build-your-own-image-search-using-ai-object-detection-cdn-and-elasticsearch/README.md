# build your own image search using ai object detection cdn and elasticsearch

This folder contains the **build your own image search using ai object detection cdn and elasticsearch** workflow. Its executable nodes use `code`, `editImage`, `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch.json`](build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Variables | `set` | Inspect parameters |
| Get Test Image | `httpRequest` | Inspect parameters |
| Gemini 2.0 Object Detection | `httpRequest` | POST |
| Scale Normalised Coords | `code` | Inspect parameters |
| Draw Bounding Boxes | `editImage` | multiStep |
| Get Image Info | `editImage` | information |

## Connection map

- Get Variables → Scale Normalised Coords (`main`, output 0, input 0)
- Get Image Info → Gemini 2.0 Object Detection (`main`, output 0, input 0)
- Get Test Image → Get Image Info (`main`, output 0, input 0)
- Scale Normalised Coords → Draw Bounding Boxes (`main`, output 0, input 0)
- Gemini 2.0 Object Detection → Get Variables (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Test Image (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0665_Code_Editimage_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0665_Code_Editimage_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
