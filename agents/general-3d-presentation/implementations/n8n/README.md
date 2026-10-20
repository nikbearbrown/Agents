# General 3D Presentation

This folder contains the **General 3D Presentation** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`general-3d-presentation.json`](general-3d-presentation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Prompt | `httpRequest` | POST |
| Midjourney Generator | `httpRequest` | Inspect parameters |
| GPT-4o Image Generator | `httpRequest` | POST |
| Generate Kling Video | `httpRequest` | POST |
| Get Video URL | `httpRequest` | Inspect parameters |
| Wait for Image Generation | `wait` | Inspect parameters |
| Check Generation Status | `if` | Inspect parameters |
| Get Image URL of Midjourney | `code` | Inspect parameters |
| Get Image URL of GPT-4o-image | `code` | Inspect parameters |
| Check Generation Status of GPT-4o | `if` | Inspect parameters |
| Check Video Generation Status | `if` | Inspect parameters |
| Wait for Video Generation | `wait` | Inspect parameters |
| Fetch Final Video URL | `code` | Inspect parameters |

## Connection map

- Prompt → Midjourney Generator (`main`, output 0, input 0)
- Get Video URL → Check Video Generation Status (`main`, output 0, input 0)
- Generate Kling Video → Get Video URL (`main`, output 0, input 0)
- Midjourney Generator → Check Generation Status (`main`, output 0, input 0)
- GPT-4o Image Generator → Get Image URL of GPT-4o-image (`main`, output 0, input 0)
- Check Generation Status → Get Image URL of Midjourney (`main`, output 0, input 0)
- Check Generation Status → Wait for Image Generation (`main`, output 1, input 0)
- Wait for Image Generation → Midjourney Generator (`main`, output 0, input 0)
- Wait for Video Generation → Get Video URL (`main`, output 0, input 0)
- Get Image URL of Midjourney → GPT-4o Image Generator (`main`, output 0, input 0)
- Check Video Generation Status → Fetch Final Video URL (`main`, output 0, input 0)
- Check Video Generation Status → Wait for Video Generation (`main`, output 1, input 0)
- Get Image URL of GPT-4o-image → Check Generation Status of GPT-4o (`main`, output 0, input 0)
- Check Generation Status of GPT-4o → GPT-4o Image Generator (`main`, output 0, input 0)
- Check Generation Status of GPT-4o → Generate Kling Video (`main`, output 1, input 0)
- When clicking ‘Test workflow’ → Prompt (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1992_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1992_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
