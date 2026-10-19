# photos to list and download google drive and resize edit image

This folder contains the **photos to list and download google drive and resize edit image** workflow. Its executable nodes use `chainLlm`, `editImage`, `googleDrive`, `lmChatGoogleGemini`, `manualTrigger`, `outputParserStructured`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`photos-to-list-and-download-google-drive-and-resize-edit-image.json`](photos-to-list-and-download-google-drive-and-resize-edit-image.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Photo URLs | `set` | Inspect parameters |
| Photos To List | `splitOut` | Inspect parameters |
| Download Photos | `googleDrive` | download |
| Resize For AI | `editImage` | resize |
| Passport Photo Validator | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Photo URLs → Photos To List (`main`, output 0, input 0)
- Resize For AI → Passport Photo Validator (`main`, output 0, input 0)
- Photos To List → Download Photos (`main`, output 0, input 0)
- Download Photos → Resize For AI (`main`, output 0, input 0)
- Google Gemini Chat Model → Passport Photo Validator (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Passport Photo Validator (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Photo URLs (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0579_Splitout_Editimage_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0579_Splitout_Editimage_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
