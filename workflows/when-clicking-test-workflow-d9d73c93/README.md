# When clicking "Test workflow"

This folder contains the **When clicking "Test workflow"** workflow. Its executable nodes use `agent`, `extractFromFile`, `filter`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`when-clicking-test-workflow-d9d73c93.json`](when-clicking-test-workflow-d9d73c93.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpQueryAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Get image from unsplash2 | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Get image from unsplash3 | `httpRequest` | Inspect parameters |
| Transform to base | `extractFromFile` | binaryToPropery |
| Call Gemini API1 | `httpRequest` | POST |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| AI Agent2 | `agent` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Get image from unsplash4 | `httpRequest` | Inspect parameters |
| Get PDF file | `httpRequest` | Inspect parameters |
| Get image from unsplash | `httpRequest` | Inspect parameters |
| Call Gemini API with PDF | `httpRequest` | POST |
| Call Gemini API with Image | `httpRequest` | POST |
| Transform to base64 (image) | `extractFromFile` | binaryToPropery |
| Transform to base64 (pdf) | `extractFromFile` | binaryToPropery |
| Define Multiple Image URLs | `set` | Inspect parameters |
| Split Out to multiple items | `splitOut` | Inspect parameters |
| Define URLs And Prompts | `set` | Inspect parameters |
| Filter (optional) | `filter` | Inspect parameters |

## Connection map

- AI Agent → Loop Over Items (`main`, output 0, input 0)
- Split Out → Filter (optional) (`main`, output 0, input 0)
- Get PDF file → Transform to base64 (pdf) (`main`, output 0, input 0)
- Loop Over Items → AI Agent (`main`, output 1, input 0)
- Filter (optional) → Get image from unsplash2 (`main`, output 0, input 0)
- Transform to base → Call Gemini API1 (`main`, output 0, input 0)
- Define URLs And Prompts → Split Out (`main`, output 0, input 0)
- Get image from unsplash → Transform to base64 (image) (`main`, output 0, input 0)
- Get image from unsplash2 → Loop Over Items (`main`, output 0, input 0)
- Get image from unsplash3 → Transform to base (`main`, output 0, input 0)
- Get image from unsplash4 → AI Agent2 (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model1 → AI Agent2 (`ai_languageModel`, output 0, input 0)
- Transform to base64 (pdf) → Call Gemini API with PDF (`main`, output 0, input 0)
- Define Multiple Image URLs → Split Out to multiple items (`main`, output 0, input 0)
- Split Out to multiple items → Get image from unsplash3 (`main`, output 0, input 0)
- Transform to base64 (image) → Call Gemini API with Image (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Define URLs And Prompts (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Define Multiple Image URLs (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get PDF file (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get image from unsplash (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get image from unsplash4 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0772_Splitout_Filter_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0772_Splitout_Filter_Process_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
