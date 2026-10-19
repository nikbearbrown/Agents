# Generate Graphic Wallpaper with Midjourney, GPT-4o-mini and Canvas APIs

This folder contains the **Generate Graphic Wallpaper with Midjourney, GPT-4o-mini and Canvas APIs** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `set`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-graphic-wallpaper-with-midjourney-gpt-4o-mini-and-canvas-apis.json`](generate-graphic-wallpaper-with-midjourney-gpt-4o-mini-and-canvas-apis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking Test workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Midjourney Generator | `httpRequest` | POST |
| When clicking Test workflow | `manualTrigger` | Inspect parameters |
| Get Prompt | `code` | Inspect parameters |
| Get Midjourney Task | `httpRequest` | Inspect parameters |
| Wait for Midjourney Generation | `wait` | Inspect parameters |
| Determine Whether the Image URL was Fetched | `if` | Inspect parameters |
| Check Image  Generation Status | `switch` | Inspect parameters |
| Design in Canvas | `httpRequest` | POST |
| Get Image Url | `set` | Inspect parameters |
| Gpt-4o-mini API | `httpRequest` | POST |
| Basic Params | `set` | Inspect parameters |

## Connection map

- Get Prompt → Midjourney Generator (`main`, output 0, input 0)
- Basic Params → Gpt-4o-mini API (`main`, output 0, input 0)
- Get Image Url → Design in Canvas (`main`, output 0, input 0)
- Gpt-4o-mini API → Get Prompt (`main`, output 0, input 0)
- Get Midjourney Task → Determine Whether the Image URL was Fetched (`main`, output 0, input 0)
- Midjourney Generator → Wait for Midjourney Generation (`main`, output 0, input 0)
- When clicking Test workflow → Basic Params (`main`, output 0, input 0)
- Check Image  Generation Status → Get Image Url (`main`, output 0, input 0)
- Wait for Midjourney Generation → Get Midjourney Task (`main`, output 0, input 0)
- Determine Whether the Image URL was Fetched → Check Image  Generation Status (`main`, output 0, input 0)
- Determine Whether the Image URL was Fetched → Wait for Midjourney Generation (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1917_Wait_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1917_Wait_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
