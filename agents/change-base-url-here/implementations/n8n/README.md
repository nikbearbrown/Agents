# 🚨 Change Base URL here!

This folder contains the **🚨 Change Base URL here!** workflow. Its executable nodes use `airtable`, `chainLlm`, `extractFromFile`, `form`, `formTrigger`, `httpRequest`, `lmChatOpenAi`, `outputParserStructured`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`change-base-url-here.json`](change-base-url-here.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`

**Entry nodes:** Step 1 of 2 - Upload CV, Step 2 of 2 - Application Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract from File | `extractFromFile` | pdf |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Step 1 of 2 - Upload CV | `formTrigger` | Inspect parameters |
| Save to Airtable | `airtable` | create |
| Classify Document | `textClassifier` | Inspect parameters |
| Upload File to Record | `httpRequest` | POST |
| Form Success | `form` | completion |
| Save to Airtable1 | `airtable` | update |
| Step 2 of 2 - Application Form | `formTrigger` | Inspect parameters |
| Application Suitability Agent | `chainLlm` | Inspect parameters |
| File Upload Retry | `form` | Inspect parameters |
| Redirect To Step 2 of 2 | `form` | completion |
| Submission Success | `form` | Inspect parameters |

## Connection map

- Save to Airtable → Upload File to Record (`main`, output 0, input 0)
- Classify Document → Application Suitability Agent (`main`, output 0, input 0)
- Classify Document → File Upload Retry (`main`, output 1, input 0)
- Extract from File → Classify Document (`main`, output 0, input 0)
- File Upload Retry → Extract from File (`main`, output 0, input 0)
- Save to Airtable1 → Form Success (`main`, output 0, input 0)
- Save to Airtable1 → Form Success (`main`, output 1, input 0)
- OpenAI Chat Model1 → Application Suitability Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Classify Document (`ai_languageModel`, output 0, input 0)
- Submission Success → Redirect To Step 2 of 2 (`main`, output 0, input 0)
- Upload File to Record → Submission Success (`main`, output 0, input 0)
- Step 1 of 2 - Upload CV → Extract from File (`main`, output 0, input 0)
- Structured Output Parser → Application Suitability Agent (`ai_outputParser`, output 0, input 0)
- Application Suitability Agent → Save to Airtable (`main`, output 0, input 0)
- Step 2 of 2 - Application Form → Save to Airtable1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0646_Extractfromfile_Form_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0646_Extractfromfile_Form_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
