# Create Animated Stories using GPT-4o-mini, Midjourney, Kling and Creatomate API

This folder contains the **Create Animated Stories using GPT-4o-mini, Midjourney, Kling and Creatomate API** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `set`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-animated-stories-using-gpt-4o-mini-midjourney-kling-and-creatomate-api.json`](create-animated-stories-using-gpt-4o-mini-midjourney-kling-and-creatomate-api.json): sanitized, inactive import copy with an overview sticky note.
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
| output1 | `set` | Inspect parameters |
| output2 | `set` | Inspect parameters |
| Get Prompt | `code` | Inspect parameters |
| Basic Params | `set` | Inspect parameters |
| Get Task ID of the First Image | `set` | Inspect parameters |
| Midjourney Generator of the First Image | `httpRequest` | POST |
| Wait for the First Image Generation | `wait` | Inspect parameters |
| Verify the first image generation status | `if` | Inspect parameters |
| Get the First Image URL | `set` | Inspect parameters |
| Midjourney Generator of the Second Image | `httpRequest` | POST |
| Midjourney Generator of the Third Image | `httpRequest` | POST |
| Get the First Image Generation Status | `switch` | Inspect parameters |
| Get the Second Image Generation Status | `switch` | Inspect parameters |
| Get the Third Image Generation Status | `switch` | Inspect parameters |
| Get the Second Image URL | `set` | Inspect parameters |
| Get the Third Image URL | `set` | Inspect parameters |
| Wait for the Second Image Generation | `wait` | Inspect parameters |
| Get Task of the First Image | `httpRequest` | Inspect parameters |
| Get Task of the Second Image | `httpRequest` | Inspect parameters |
| Verify the second image generation status | `if` | Inspect parameters |
| Verify the third image generation status | `if` | Inspect parameters |
| Get Task of the Third Image | `httpRequest` | Inspect parameters |
| Wait for the Third Image Generation | `wait` | Inspect parameters |
| Get three Image URLs | `set` | Inspect parameters |
| Generate the First Video | `httpRequest` | POST |
| Generate the Second Video | `httpRequest` | POST |
| Generate the Third Video | `httpRequest` | POST |
| Final Video Combination | `httpRequest` | POST |
| Get the Third Video URL | `set` | Inspect parameters |
| Get Video Task IDs | `set` | Inspect parameters |
| Get the First Video Task | `httpRequest` | Inspect parameters |
| Verify the First Video Generation | `if` | Inspect parameters |
| Verify the Second Video Generation | `if` | Inspect parameters |
| Verify the Third Video Generation | `if` | Inspect parameters |
| Wait for Video Generation for at Least 4 min | `wait` | Inspect parameters |
| Wait for the First Video Generation | `wait` | Inspect parameters |
| Wait for the Second Video Generation | `wait` | Inspect parameters |
| Wait for the Third Video Generation | `wait` | Inspect parameters |
| Get the First Video Generation | `switch` | Inspect parameters |
| Get the Second Video Generation | `switch` | Inspect parameters |
| Get the Third Video Generation | `switch` | Inspect parameters |
| Get the Second Video Task | `httpRequest` | Inspect parameters |
| Get the Third Video Task | `httpRequest` | Inspect parameters |
| When clicking Test workflow | `manualTrigger` | Inspect parameters |
| GPT-4o-mini Generate Image Scenario Prompt | `httpRequest` | POST |

## Connection map

- output1 → Get the Second Video Task (`main`, output 0, input 0)
- output2 → Get the Third Video Task (`main`, output 0, input 0)
- Get Prompt → Midjourney Generator of the First Image (`main`, output 0, input 0)
- Basic Params → GPT-4o-mini Generate Image Scenario Prompt (`main`, output 0, input 0)
- Get Video Task IDs → Wait for Video Generation for at Least 4 min (`main`, output 0, input 0)
- Get three Image URLs → Generate the First Video (`main`, output 0, input 0)
- Get the First Image URL → Midjourney Generator of the Second Image (`main`, output 0, input 0)
- Get the Third Image URL → Get three Image URLs (`main`, output 0, input 0)
- Get the Third Video URL → Final Video Combination (`main`, output 0, input 0)
- Generate the First Video → Generate the Second Video (`main`, output 0, input 0)
- Generate the Third Video → Get Video Task IDs (`main`, output 0, input 0)
- Get the First Video Task → Verify the First Video Generation (`main`, output 0, input 0)
- Get the Second Image URL → Midjourney Generator of the Third Image (`main`, output 0, input 0)
- Get the Third Video Task → Verify the Third Video Generation (`main`, output 0, input 0)
- Generate the Second Video → Generate the Third Video (`main`, output 0, input 0)
- Get the Second Video Task → Verify the Second Video Generation (`main`, output 0, input 0)
- Get Task of the First Image → Verify the first image generation status (`main`, output 0, input 0)
- Get Task of the Third Image → Verify the third image generation status (`main`, output 0, input 0)
- When clicking Test workflow → Basic Params (`main`, output 0, input 0)
- Get Task of the Second Image → Verify the second image generation status (`main`, output 0, input 0)
- Get Task ID of the First Image → Wait for the First Image Generation (`main`, output 0, input 0)
- Get the First Video Generation → output1 (`main`, output 0, input 0)
- Get the Third Video Generation → Get the Third Video URL (`main`, output 0, input 0)
- Get the Second Video Generation → output2 (`main`, output 0, input 0)
- Verify the First Video Generation → Get the First Video Generation (`main`, output 0, input 0)
- Verify the First Video Generation → Wait for the First Video Generation (`main`, output 1, input 0)
- Verify the Third Video Generation → Get the Third Video Generation (`main`, output 0, input 0)
- Verify the Third Video Generation → Wait for the Third Video Generation (`main`, output 1, input 0)
- Verify the Second Video Generation → Get the Second Video Generation (`main`, output 0, input 0)
- Verify the Second Video Generation → Wait for the Second Video Generation (`main`, output 1, input 0)
- Wait for the First Image Generation → Get Task of the First Image (`main`, output 0, input 0)
- Wait for the First Video Generation → Get the First Video Task (`main`, output 0, input 0)
- Wait for the Third Image Generation → Get Task of the Third Image (`main`, output 0, input 0)
- Wait for the Third Video Generation → Get the Third Video Task (`main`, output 0, input 0)
- Wait for the Second Image Generation → Get Task of the Second Image (`main`, output 0, input 0)
- Wait for the Second Video Generation → Get the Second Video Task (`main`, output 0, input 0)
- Get the First Image Generation Status → Get the First Image URL (`main`, output 0, input 0)
- Get the Third Image Generation Status → Get the Third Image URL (`main`, output 0, input 0)
- Get the Second Image Generation Status → Get the Second Image URL (`main`, output 0, input 0)
- Midjourney Generator of the First Image → Get Task ID of the First Image (`main`, output 0, input 0)
- Midjourney Generator of the Third Image → Wait for the Third Image Generation (`main`, output 0, input 0)
- Midjourney Generator of the Second Image → Wait for the Second Image Generation (`main`, output 0, input 0)
- Verify the first image generation status → Get the First Image Generation Status (`main`, output 0, input 0)
- Verify the first image generation status → Wait for the First Image Generation (`main`, output 1, input 0)
- Verify the third image generation status → Get the Third Image Generation Status (`main`, output 0, input 0)
- Verify the third image generation status → Wait for the Third Image Generation (`main`, output 1, input 0)
- Verify the second image generation status → Get the Second Image Generation Status (`main`, output 0, input 0)
- Verify the second image generation status → Wait for the Second Image Generation (`main`, output 1, input 0)
- GPT-4o-mini Generate Image Scenario Prompt → Get Prompt (`main`, output 0, input 0)
- Wait for Video Generation for at Least 4 min → Get the First Video Task (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1395_Wait_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1395_Wait_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
