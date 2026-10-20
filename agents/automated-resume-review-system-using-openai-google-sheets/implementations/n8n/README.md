# Automated Resume Review System Using OpenAI + Google Sheets

This folder contains the **Automated Resume Review System Using OpenAI + Google Sheets** workflow. Its executable nodes use `chainLlm`, `chainSummarization`, `extractFromFile`, `formTrigger`, `googleDrive`, `googleSheets`, `informationExtractor`, `lmChatOpenAi`, `merge`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-resume-review-system-using-openai-google-sheets.json`](automated-resume-review-system-using-openai-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| Personal Info | `informationExtractor` | Inspect parameters |
| Qualification | `informationExtractor` | Inspect parameters |
| HR Expert | `chainLlm` | Inspect parameters |
| Upload to google drive | `googleDrive` | Inspect parameters |
| Resume extraction | `extractFromFile` | pdf |
| wanted profile | `set` | Inspect parameters |
| Summarizer | `chainSummarization` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Merge → Summarizer (`main`, output 0, input 0)
- HR Expert → Google Sheets (`main`, output 0, input 0)
- Summarizer → wanted profile (`main`, output 0, input 0)
- Personal Info → Merge (`main`, output 0, input 1)
- Qualification → Merge (`main`, output 0, input 0)
- wanted profile → HR Expert (`main`, output 0, input 0)
- OpenAI Chat Model → Qualification (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model → Personal Info (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model → Summarizer (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model → HR Expert (`ai_languageModel`, output 0, input 0)
- Resume extraction → Personal Info (`main`, output 0, input 0)
- Resume extraction → Qualification (`main`, output 0, input 0)
- On form submission → Upload to google drive (`main`, output 0, input 0)
- On form submission → Resume extraction (`main`, output 0, input 0)
- Structured Output Parser → HR Expert (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1501_Extractfromfile_Form_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1501_Extractfromfile_Form_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
