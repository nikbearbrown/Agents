# It structures the script for direct use with the Hugging Face text-to-speech model.

This folder contains the **It structures the script for direct use with the Hugging Face text-to-speech model.** workflow. Its executable nodes use `aggregate`, `chainLlm`, `filter`, `html`, `httpRequest`, `if`, `limit`, `lmChatGoogleGemini`, `manualTrigger`, `outputParserStructured`, `splitOut`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`it-structures-the-script-for-direct-use-with-the-hugging-face-text-to-speech-model.json`](it-structures-the-script-for-direct-use-with-the-hugging-face-text-to-speech-model.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `huggingFaceApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Extract News Block | `html` | extractHtmlContent |
| Extract News Content | `html` | extractHtmlContent |
| Aggregate | `aggregate` | Inspect parameters |
| Fetch BBC News Detail | `httpRequest` | Inspect parameters |
| Extract Detail | `html` | extractHtmlContent |
| Filter Empty Detail | `filter` | Inspect parameters |
| If script exists | `if` | Inspect parameters |
| Basic Podcast LLM Chain | `chainLlm` | Inspect parameters |
| Gemini | `lmChatGoogleGemini` | Inspect parameters |
| Output Parser | `outputParserStructured` | Inspect parameters |
| News Classifier | `textClassifier` | Inspect parameters |
| Fetch BBC News Page | `httpRequest` | Inspect parameters |
| Limit 10 Items | `limit` | Inspect parameters |
| Hugging Face Text-to-Speech. | `httpRequest` | POST |

## Connection map

- Gemini → News Classifier (`ai_languageModel`, output 0, input 0)
- Gemini → Basic Podcast LLM Chain (`ai_languageModel`, output 0, input 0)
- Aggregate → Basic Podcast LLM Chain (`main`, output 0, input 0)
- Split Out → Extract News Content (`main`, output 0, input 0)
- Output Parser → Basic Podcast LLM Chain (`ai_outputParser`, output 0, input 0)
- Extract Detail → Filter Empty Detail (`main`, output 0, input 0)
- Limit 10 Items → News Classifier (`main`, output 0, input 0)
- News Classifier → Fetch BBC News Detail (`main`, output 0, input 0)
- If script exists → Hugging Face Text-to-Speech. (`main`, output 0, input 0)
- Extract News Block → Split Out (`main`, output 0, input 0)
- Fetch BBC News Page → Extract News Block (`main`, output 0, input 0)
- Filter Empty Detail → Aggregate (`main`, output 0, input 0)
- Extract News Content → Limit 10 Items (`main`, output 0, input 0)
- Fetch BBC News Detail → Extract Detail (`main`, output 0, input 0)
- Basic Podcast LLM Chain → If script exists (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Fetch BBC News Page (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0731_Splitout_Limit_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0731_Splitout_Limit_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
