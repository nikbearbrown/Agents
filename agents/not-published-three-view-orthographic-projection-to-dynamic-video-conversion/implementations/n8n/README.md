# (Not published) Three-View Orthographic Projection to Dynamic Video Conversion

This folder contains the **(Not published) Three-View Orthographic Projection to Dynamic Video Conversion** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`not-published-three-view-orthographic-projection-to-dynamic-video-conversion.json`](not-published-three-view-orthographic-projection-to-dynamic-video-conversion.json): sanitized, inactive import copy with an overview sticky note.
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
| Generate Kling Video | `httpRequest` | POST |
| Get Kling Video | `httpRequest` | Inspect parameters |
| Verify Task Status | `if` | Inspect parameters |
| Get Final Video | `code` | Inspect parameters |
| GPT-4o Generator: Front View | `httpRequest` | POST |
| GPT-4o Generator: Side View | `httpRequest` | POST |
| Get Image URL of Front Image | `code` | Inspect parameters |
| Get Image URL of Side Image | `code` | Inspect parameters |
| Verify Generation Status of Front View | `if` | Inspect parameters |
| Verify Generation Status of Side View | `if` | Inspect parameters |
| Wait for Video Generation | `wait` | Inspect parameters |
| Basic Params | `set` | Inspect parameters |

## Connection map

- Basic Params → GPT-4o Generator: Front View (`main`, output 0, input 0)
- Get Kling Video → Verify Task Status (`main`, output 0, input 0)
- Verify Task Status → Get Final Video (`main`, output 0, input 0)
- Verify Task Status → Wait for Video Generation (`main`, output 1, input 0)
- Generate Kling Video → Get Kling Video (`main`, output 0, input 0)
- Wait for Video Generation → Get Kling Video (`main`, output 0, input 0)
- GPT-4o Generator: Side View → Get Image URL of Side Image (`main`, output 0, input 0)
- Get Image URL of Side Image → Verify Generation Status of Side View (`main`, output 0, input 0)
- GPT-4o Generator: Front View → Get Image URL of Front Image (`main`, output 0, input 0)
- Get Image URL of Front Image → Verify Generation Status of Front View (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Basic Params (`main`, output 0, input 0)
- Verify Generation Status of Side View → GPT-4o Generator: Side View (`main`, output 0, input 0)
- Verify Generation Status of Side View → Generate Kling Video (`main`, output 1, input 0)
- Verify Generation Status of Front View → GPT-4o Generator: Front View (`main`, output 0, input 0)
- Verify Generation Status of Front View → GPT-4o Generator: Side View (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1532_Manual_Wait_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1532_Manual_Wait_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
