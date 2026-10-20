# Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls

This folder contains the **Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls** workflow. Its executable nodes use `convertToFile`, `extractFromFile`, `filter`, `formTrigger`, `lmChatOpenAi`, `noOp`, `set`, `summarize`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-ai-ready-llms-txt-files-from-screaming-frog-website-crawls.json`](generate-ai-ready-llms-txt-files-from-screaming-frog-website-crawls.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Form - Screaming frog internal_html.csv upload

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set useful fields | `set` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Filter URLs | `filter` | Inspect parameters |
| Summarize - Concatenate | `summarize` | Inspect parameters |
| Set Fields - llms.txt Content | `set` | Inspect parameters |
| upload file anywhere | `noOp` | Inspect parameters |
| Set Field - llms.txt Row | `set` | Inspect parameters |
| Form - Screaming frog internal_html.csv upload | `formTrigger` | Inspect parameters |
| Extract data from Screaming Frog file | `extractFromFile` | xls |
| Generate llms.txt file | `convertToFile` | toText |

## Connection map

- Filter URLs → Text Classifier (`main`, output 0, input 0)
- Text Classifier → Set Field - llms.txt Row (`main`, output 0, input 0)
- Text Classifier → No Operation, do nothing (`main`, output 1, input 0)
- OpenAI Chat Model → Text Classifier (`ai_languageModel`, output 0, input 0)
- Set useful fields → Filter URLs (`main`, output 0, input 0)
- Summarize - Concatenate → Set Fields - llms.txt Content (`main`, output 0, input 0)
- Set Field - llms.txt Row → Summarize - Concatenate (`main`, output 0, input 0)
- Set Fields - llms.txt Content → Generate llms.txt file (`main`, output 0, input 0)
- Extract data from Screaming Frog file → Set useful fields (`main`, output 0, input 0)
- Form - Screaming frog internal_html.csv upload → Extract data from Screaming Frog file (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1791_Filter_Summarize_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1791_Filter_Summarize_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
