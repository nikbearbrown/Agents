# Flux Dev Image Generation Fal.ai

This folder contains the **Flux Dev Image Generation Fal.ai** workflow. Its executable nodes use `googleDrive`, `httpRequest`, `if`, `manualTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`flux-dev-image-generation-fal-ai.json`](flux-dev-image-generation-fal-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Fal Flux | `httpRequest` | POST |
| Get Image Result URL | `httpRequest` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| Google Drive | `googleDrive` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Wait 3 Sec | `wait` | Inspect parameters |
| Check Status | `httpRequest` | Inspect parameters |
| Completed? | `if` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- Fal Flux → Wait 3 Sec (`main`, output 0, input 0)
- Completed? → Get Image Result URL (`main`, output 0, input 0)
- Completed? → Wait 3 Sec (`main`, output 1, input 0)
- Wait 3 Sec → Check Status (`main`, output 0, input 0)
- Edit Fields → Fal Flux (`main`, output 0, input 0)
- Check Status → Completed? (`main`, output 0, input 0)
- Download Image → Google Drive (`main`, output 0, input 0)
- Get Image Result URL → Download Image (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1931_Wait_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1931_Wait_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
