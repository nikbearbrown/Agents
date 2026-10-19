# information edit image and resize edit image and multistep edit image 3d08a82e

This folder contains the **information edit image and resize edit image and multistep edit image 3d08a82e** workflow. Its executable nodes use `chainLlm`, `code`, `editImage`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `merge`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`information-edit-image-and-resize-edit-image-and-multistep-edit-image-3d08a82e.json`](information-edit-image-and-resize-edit-image-and-multistep-edit-image-3d08a82e.json): sanitized, inactive import copy with an overview sticky note.
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
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Get Info | `editImage` | information |
| Resize For AI | `editImage` | resize |
| Calculate Positioning | `code` | Inspect parameters |
| Apply Caption to Image | `editImage` | multiStep |
| Merge Image & Caption | `merge` | Inspect parameters |
| Merge Caption & Positions | `merge` | Inspect parameters |
| Get Image | `httpRequest` | Inspect parameters |
| Image Captioning Agent | `chainLlm` | Inspect parameters |

## Connection map

- Get Info → Merge Image & Caption (`main`, output 0, input 0)
- Get Image → Resize For AI (`main`, output 0, input 0)
- Get Image → Get Info (`main`, output 0, input 0)
- Resize For AI → Image Captioning Agent (`main`, output 0, input 0)
- Calculate Positioning → Merge Caption & Positions (`main`, output 0, input 1)
- Merge Image & Caption → Calculate Positioning (`main`, output 0, input 0)
- Merge Image & Caption → Merge Caption & Positions (`main`, output 0, input 0)
- Image Captioning Agent → Merge Image & Caption (`main`, output 0, input 1)
- Google Gemini Chat Model → Image Captioning Agent (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Image Captioning Agent (`ai_outputParser`, output 0, input 0)
- Merge Caption & Positions → Apply Caption to Image (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Image (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1423_Code_Editimage_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1423_Code_Editimage_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
