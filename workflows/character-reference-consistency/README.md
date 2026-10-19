# 3D Figurine Orthographic Views with Midjourney and GPT-4o-Image API

This folder contains the **3D Figurine Orthographic Views with Midjourney and GPT-4o-Image API** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`character-reference-consistency.json`](character-reference-consistency.json): sanitized, inactive import copy with an overview sticky note.
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
| Midjourney Generator | `httpRequest` | POST |
| Get Midjourney URL | `httpRequest` | Inspect parameters |
| Verify URL Acquisition | `if` | Inspect parameters |
| Wait for Generation | `wait` | Inspect parameters |
| Get Random Image URL | `code` | Inspect parameters |
| Generation 3-view Image with GPT-4o-Image | `httpRequest` | POST |
| Check if the URL is obtained | `if` | Inspect parameters |
| Get Final Output | `code` | Inspect parameters |
| Get Image | `code` | Inspect parameters |

## Connection map

- Get Image → Check if the URL is obtained (`main`, output 0, input 0)
- Get Midjourney URL → Verify URL Acquisition (`main`, output 0, input 0)
- Wait for Generation → Get Midjourney URL (`main`, output 0, input 0)
- Get Random Image URL → Generation 3-view Image with GPT-4o-Image (`main`, output 0, input 0)
- Midjourney Generator → Get Midjourney URL (`main`, output 0, input 0)
- Verify URL Acquisition → Get Random Image URL (`main`, output 0, input 0)
- Verify URL Acquisition → Wait for Generation (`main`, output 1, input 0)
- Check if the URL is obtained → Generation 3-view Image with GPT-4o-Image (`main`, output 0, input 0)
- Check if the URL is obtained → Get Final Output (`main`, output 1, input 0)
- When clicking ‘Test workflow’ → Midjourney Generator (`main`, output 0, input 0)
- Generation 3-view Image with GPT-4o-Image → Get Image (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1238_Manual_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1238_Manual_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
