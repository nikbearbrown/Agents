# Transform Image to Lego Style Using Line and Dall-E

This folder contains the **Transform Image to Lego Style Using Line and Dall-E** workflow. Its executable nodes use `httpRequest`, `openAi`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`transform-image-to-lego-style-using-line-and-dall-e.json`](transform-image-to-lego-style-using-line-and-dall-e.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Receive a Line Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Receive a Line Webhook | `webhook` | Inspect parameters |
| Receive Line Messages | `httpRequest` | Inspect parameters |
| Creating an Image using Dall-E | `openAi` | image |
| Creating a Prompt for Dall-E (Lego Style) | `openAi` | image / analyze |
| Send Back an Image through Line | `httpRequest` | POST |

## Connection map

- Receive Line Messages → Creating a Prompt for Dall-E (Lego Style) (`main`, output 0, input 0)
- Receive a Line Webhook → Receive Line Messages (`main`, output 0, input 0)
- Creating an Image using Dall-E → Send Back an Image through Line (`main`, output 0, input 0)
- Creating a Prompt for Dall-E (Lego Style) → Creating an Image using Dall-E (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1700_HTTP_Webhook_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1700_HTTP_Webhook_Process_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
