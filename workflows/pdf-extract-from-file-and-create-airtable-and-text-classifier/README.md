# pdf extract from file and create airtable and text classifier

This folder contains the **pdf extract from file and create airtable and text classifier** workflow. Its executable nodes use `airtable`, `chainLlm`, `extractFromFile`, `form`, `formTrigger`, `function`, `httpRequest`, `lmChatGoogleGemini`, `outputParserStructured`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pdf-extract-from-file-and-create-airtable-and-text-classifier.json`](pdf-extract-from-file-and-create-airtable-and-text-classifier.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googlePalmApi`

**Entry nodes:** Step 1 of 2 - Upload Document

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract from File | `extractFromFile` | pdf |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Save to Airtable | `airtable` | create |
| Classify Document | `textClassifier` | Inspect parameters |
| Upload File to Record | `httpRequest` | POST |
| Application Suitability Agent | `chainLlm` | Inspect parameters |
| File Upload Retry | `form` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Step 1 of 2 - Upload Document | `formTrigger` | Inspect parameters |
| Split Files | `function` | Inspect parameters |

## Connection map

- Extract from File → Classify Document (`main`, output 0, input 0)
- Structured Output Parser → Application Suitability Agent (`ai_outputParser`, output 0, input 0)
- Save to Airtable → Upload File to Record (`main`, output 0, input 0)
- Classify Document → Application Suitability Agent (`main`, output 0, input 0)
- Classify Document → File Upload Retry (`main`, output 1, input 0)
- Application Suitability Agent → Save to Airtable (`main`, output 0, input 0)
- File Upload Retry → Split Files (`main`, output 0, input 0)
- Google Gemini Chat Model1 → Classify Document (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model → Application Suitability Agent (`ai_languageModel`, output 0, input 0)
- Step 1 of 2 - Upload Document → Split Files (`main`, output 0, input 0)
- Split Files → Extract from File (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/BikramMondal5/MagicFill/blob/3037cd5390c2e64e5d8414df6d9d413d57fa6625/resume.json](https://github.com/BikramMondal5/MagicFill/blob/3037cd5390c2e64e5d8414df6d9d413d57fa6625/resume.json). License: **MIT**; preserve [the notice](../../licenses/BikramMondal5--MagicFill.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
