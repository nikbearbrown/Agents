# Motion-illustration Workflow Generated with Midjourney and Kling API

This folder contains the **Motion-illustration Workflow Generated with Midjourney and Kling API** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`motion-illustration-workflow-generated-with-midjourney-and-kling-api.json`](motion-illustration-workflow-generated-with-midjourney-and-kling-api.json): sanitized, inactive import copy with an overview sticky note.
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
| Kling Video Generator | `httpRequest` | POST |
| Get Video | `httpRequest` | Inspect parameters |
| Get Image | `code` | Inspect parameters |
| Basic Prompt | `httpRequest` | POST |
| Get Data Status | `if` | Inspect parameters |
| Wait for Image Generation | `wait` | Inspect parameters |
| Midjourney Image Generator | `httpRequest` | Inspect parameters |
| Wait for Video Generation | `wait` | Inspect parameters |
| Get Final Video URL | `code` | Inspect parameters |
| Verify Data Status | `if` | Inspect parameters |

## Connection map

- Get Image → Kling Video Generator (`main`, output 0, input 0)
- Get Video → Verify Data Status (`main`, output 0, input 0)
- Basic Prompt → Midjourney Image Generator (`main`, output 0, input 0)
- Get Data Status → Get Image (`main`, output 0, input 0)
- Get Data Status → Wait for Image Generation (`main`, output 1, input 0)
- Verify Data Status → Get Final Video URL (`main`, output 0, input 0)
- Verify Data Status → Wait for Video Generation (`main`, output 1, input 0)
- Kling Video Generator → Get Video (`main`, output 0, input 0)
- Wait for Image Generation → Midjourney Image Generator (`main`, output 0, input 0)
- Wait for Video Generation → Get Video (`main`, output 0, input 0)
- Midjourney Image Generator → Get Data Status (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Basic Prompt (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1484_Wait_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1484_Wait_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
