# respond to webhook and respond with error and upload s3

This folder contains the **respond to webhook and respond with error and upload s3** workflow. Its executable nodes use `formTrigger`, `httpRequest`, `respondToWebhook`, `s3`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`respond-to-webhook-and-respond-with-error-and-upload-s3.json`](respond-to-webhook-and-respond-with-error-and-upload-s3.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `s3`

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Vivid Pop Explosion | `set` | Inspect parameters |
| AI Dystopia | `set` | Inspect parameters |
| Post-Analog Glitchscape | `set` | Inspect parameters |
| Neon Fauvism | `set` | Inspect parameters |
| None | `set` | Inspect parameters |
| Serve webpage | `respondToWebhook` | Inspect parameters |
| Respond with error | `respondToWebhook` | Inspect parameters |
| Upload image to S3 | `s3` | upload |
| Hyper-Surreal Escape | `set` | Inspect parameters |
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Call hugginface inference api | `httpRequest` | POST |
| Route by style | `switch` | Inspect parameters |

## Connection map

- None → Call hugginface inference api (`main`, output 0, input 0)
- AI Dystopia → Call hugginface inference api (`main`, output 0, input 0)
- Neon Fauvism → Call hugginface inference api (`main`, output 0, input 0)
- Route by style → Hyper-Surreal Escape (`main`, output 0, input 0)
- Route by style → Post-Analog Glitchscape (`main`, output 1, input 0)
- Route by style → AI Dystopia (`main`, output 2, input 0)
- Route by style → Neon Fauvism (`main`, output 3, input 0)
- Route by style → Vivid Pop Explosion (`main`, output 4, input 0)
- Route by style → None (`main`, output 5, input 0)
- n8n Form Trigger → Route by style (`main`, output 0, input 0)
- Upload image to S3 → Serve webpage (`main`, output 0, input 0)
- Upload image to S3 → Respond with error (`main`, output 1, input 0)
- Vivid Pop Explosion → Call hugginface inference api (`main`, output 0, input 0)
- Hyper-Surreal Escape → Call hugginface inference api (`main`, output 0, input 0)
- Post-Analog Glitchscape → Call hugginface inference api (`main`, output 0, input 0)
- Call hugginface inference api → Upload image to S3 (`main`, output 0, input 0)
- Call hugginface inference api → Respond with error (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/0576_Respondtowebhook_Form_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/0576_Respondtowebhook_Form_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `respond-to-webhook-and-respond-with-error-and-upload-s3-ebde10c6` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
