# AI CV Screening Workflow

This folder contains the **AI CV Screening Workflow** workflow. Its executable nodes use `chainLlm`, `extractFromFile`, `formTrigger`, `gmail`, `googleSheets`, `lmChatGoogleGemini`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-cv-screening-workflow.json`](ai-cv-screening-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `googleSheetsOAuth2Api`

**Entry nodes:** Application Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Confirmation of CV Submission | `gmail` | Inspect parameters |
| Inform HR New CV Received | `gmail` | Inspect parameters |
| Using AI Analysis & Rating | `chainLlm` | Inspect parameters |
| Convert Binary to Json | `extractFromFile` | pdf |
| Application Form | `formTrigger` | Inspect parameters |
| Candidate Lists | `googleSheets` | append |

## Connection map

- Candidate Lists → Inform HR New CV Received (`main`, output 0, input 0)
- Application Form → Convert Binary to Json (`main`, output 0, input 0)
- Convert Binary to Json → Using AI Analysis & Rating (`main`, output 0, input 0)
- Google Gemini Chat Model → Using AI Analysis & Rating (`ai_languageModel`, output 0, input 0)
- Inform HR New CV Received → Confirmation of CV Submission (`main`, output 0, input 0)
- Using AI Analysis & Rating → Candidate Lists (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1649_Form_Extractfromfile_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1649_Form_Extractfromfile_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
