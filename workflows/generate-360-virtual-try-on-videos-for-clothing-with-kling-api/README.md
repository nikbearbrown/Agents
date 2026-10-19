# Generate 360° Virtual Try-on Videos for Clothing with Kling API

This folder contains the **Generate 360° Virtual Try-on Videos for Clothing with Kling API** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `set`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-360-virtual-try-on-videos-for-clothing-with-kling-api.json`](generate-360-virtual-try-on-videos-for-clothing-with-kling-api.json): sanitized, inactive import copy with an overview sticky note.
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
| Kling Virtual Try-On Task | `httpRequest` | POST |
| Switch | `switch` | Inspect parameters |
| Get Kling Video Task | `httpRequest` | Inspect parameters |
| Generate kling video | `httpRequest` | POST |
| Preset Parameters | `set` | Inspect parameters |
| Get Kling Virtual Try-On Task | `httpRequest` | Inspect parameters |
| Check Data Status | `if` | Inspect parameters |
| Wait for Image Generation | `wait` | Inspect parameters |
| Wait for Video Generation | `wait` | Inspect parameters |
| Check Video Data Status | `switch` | Inspect parameters |
| Get Video Data Status | `if` | Inspect parameters |
| Get Final Video URL | `set` | Inspect parameters |

## Connection map

- Switch → Generate kling video (`main`, output 0, input 0)
- Check Data Status → Switch (`main`, output 0, input 0)
- Check Data Status → Wait for Image Generation (`main`, output 1, input 0)
- Preset Parameters → Kling Virtual Try-On Task (`main`, output 0, input 0)
- Generate kling video → Wait for Video Generation (`main`, output 0, input 0)
- Get Kling Video Task → Get Video Data Status (`main`, output 0, input 0)
- Get Video Data Status → Check Video Data Status (`main`, output 0, input 0)
- Get Video Data Status → Wait for Video Generation (`main`, output 1, input 0)
- Check Video Data Status → Get Final Video URL (`main`, output 0, input 0)
- Kling Virtual Try-On Task → Wait for Image Generation (`main`, output 0, input 0)
- Wait for Image Generation → Get Kling Virtual Try-On Task (`main`, output 0, input 0)
- Wait for Video Generation → Get Kling Video Task (`main`, output 0, input 0)
- Get Kling Virtual Try-On Task → Check Data Status (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Preset Parameters (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2013_Manual_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2013_Manual_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
