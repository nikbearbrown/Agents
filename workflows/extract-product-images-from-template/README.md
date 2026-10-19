# Extract Product Images from Template

This folder contains the **Extract Product Images from Template** workflow. Its executable nodes use `chainLlm`, `convertToFile`, `googleDrive`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `merge`, `openAi`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-product-images-from-template.json`](extract-product-images-from-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking 'Test workflow'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Read Image URLs | `googleSheets` | Inspect parameters |
| Download Images | `httpRequest` | Inspect parameters |
| Analyze Images | `openAi` | image / analyze |
| Product Photography Prompt | `chainLlm` | Inspect parameters |
| Send Image with Prompt to OpenAI | `httpRequest` | POST |
| Convert Base64 to File | `convertToFile` | toBinary |
| Upload to Drive | `googleDrive` | Inspect parameters |
| Insert Image URL in Table | `googleSheets` | update |
| When clicking 'Test workflow' | `manualTrigger` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Generate Image | `httpRequest` | POST |

## Connection map

- Merge → Send Image with Prompt to OpenAI (`main`, output 0, input 0)
- Analyze Images → Product Photography Prompt (`main`, output 0, input 0)
- Generate Image → Convert to File (`main`, output 0, input 0)
- Download Images → Analyze Images (`main`, output 0, input 0)
- Download Images → Merge (`main`, output 0, input 0)
- Read Image URLs → Download Images (`main`, output 0, input 0)
- Upload to Drive → Insert Image URL in Table (`main`, output 0, input 0)
- OpenAI Chat Model → Product Photography Prompt (`ai_languageModel`, output 0, input 0)
- Convert Base64 to File → Upload to Drive (`main`, output 0, input 0)
- Product Photography Prompt → Merge (`main`, output 0, input 1)
- When clicking 'Test workflow' → Read Image URLs (`main`, output 0, input 0)
- Send Image with Prompt to OpenAI → Convert Base64 to File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Converttofile/0889_Converttofile_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Converttofile/0889_Converttofile_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
