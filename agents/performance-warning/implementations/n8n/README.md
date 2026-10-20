# 🚨 PERFORMANCE WARNING!

This folder contains the **🚨 PERFORMANCE WARNING!** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `convertToFile`, `editImage`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `openAi`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`performance-warning.json`](performance-warning.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Capture Frames | `code` | Inspect parameters |
| Split Out Frames | `splitOut` | Inspect parameters |
| Download Video | `httpRequest` | Inspect parameters |
| Convert to Binary | `convertToFile` | toBinary |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Combine Script | `aggregate` | Inspect parameters |
| Upload to GDrive | `googleDrive` | Inspect parameters |
| Stay Within Service Limits | `wait` | Inspect parameters |
| For Every 15 Frames | `splitInBatches` | Inspect parameters |
| Resize Frame | `editImage` | resize |
| Aggregate Frames | `aggregate` | Inspect parameters |
| Use Text-to-Speech | `openAi` | audio |
| Generate Narration Script | `chainLlm` | Inspect parameters |

## Connection map

- Resize Frame → Aggregate Frames (`main`, output 0, input 0)
- Capture Frames → Split Out Frames (`main`, output 0, input 0)
- Combine Script → Use Text-to-Speech (`main`, output 0, input 0)
- Download Video → Capture Frames (`main`, output 0, input 0)
- Aggregate Frames → Generate Narration Script (`main`, output 0, input 0)
- Split Out Frames → For Every 15 Frames (`main`, output 0, input 0)
- Convert to Binary → Resize Frame (`main`, output 0, input 0)
- OpenAI Chat Model → Generate Narration Script (`ai_languageModel`, output 0, input 0)
- Use Text-to-Speech → Upload to GDrive (`main`, output 0, input 0)
- For Every 15 Frames → Combine Script (`main`, output 0, input 0)
- For Every 15 Frames → Convert to Binary (`main`, output 1, input 0)
- Generate Narration Script → Stay Within Service Limits (`main`, output 0, input 0)
- Stay Within Service Limits → For Every 15 Frames (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Download Video (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0603_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0603_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
