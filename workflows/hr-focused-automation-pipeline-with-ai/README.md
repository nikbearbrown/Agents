# HR-focused automation pipeline with AI

This folder contains the **HR-focused automation pipeline with AI** workflow. Its executable nodes use `chainLlm`, `chainSummarization`, `extractFromFile`, `formTrigger`, `googleDrive`, `googleSheets`, `informationExtractor`, `lmChatOpenAi`, `merge`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hr-focused-automation-pipeline-with-ai.json`](hr-focused-automation-pipeline-with-ai.json): sanitized, inactive import copy with an overview sticky note.
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
| Extract from File | `extractFromFile` | pdf |
| Qualifications | `informationExtractor` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Profile Wanted | `set` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| HR Expert | `chainLlm` | Inspect parameters |
| Personal Data | `informationExtractor` | Inspect parameters |
| Upload CV | `googleDrive` | Inspect parameters |
| OpenAI | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Merge → Summarization Chain (`main`, output 0, input 0)
- OpenAI → Qualifications (`ai_languageModel`, output 0, input 0)
- OpenAI → Summarization Chain (`ai_languageModel`, output 0, input 0)
- OpenAI → HR Expert (`ai_languageModel`, output 0, input 0)
- OpenAI → Personal Data (`ai_languageModel`, output 0, input 0)
- HR Expert → Google Sheets (`main`, output 0, input 0)
- Personal Data → Merge (`main`, output 0, input 0)
- Profile Wanted → HR Expert (`main`, output 0, input 0)
- Qualifications → Merge (`main`, output 0, input 1)
- Extract from File → Qualifications (`main`, output 0, input 0)
- Extract from File → Personal Data (`main`, output 0, input 0)
- On form submission → Extract from File (`main`, output 0, input 0)
- On form submission → Upload CV (`main`, output 0, input 0)
- Summarization Chain → Profile Wanted (`main`, output 0, input 0)
- Structured Output Parser → HR Expert (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1254_Extractfromfile_Form_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1254_Extractfromfile_Form_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
