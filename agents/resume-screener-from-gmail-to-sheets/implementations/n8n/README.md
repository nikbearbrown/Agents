# Resume Screener from Gmail to Sheets

This folder contains the **Resume Screener from Gmail to Sheets** workflow. Its executable nodes use `agent`, `extractFromFile`, `gmailTrigger`, `googleSheets`, `lmChatOpenAi`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`resume-screener-from-gmail-to-sheets.json`](resume-screener-from-gmail-to-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** Trigger on new Email Received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Extract text from PDF File | `extractFromFile` | pdf |
| AI Agent to evaluate Resume | `agent` | Inspect parameters |
| OpenAI Chat Model (GPT 4o-mini) | `lmChatOpenAi` | Inspect parameters |
| Add Resume Evaluation to Google Sheets | `googleSheets` | append |
| Trigger on new Email Received | `gmailTrigger` | Inspect parameters |

## Connection map

- Structured Output Parser → AI Agent to evaluate Resume (`ai_outputParser`, output 0, input 0)
- Extract text from PDF File → AI Agent to evaluate Resume (`main`, output 0, input 0)
- AI Agent to evaluate Resume → Add Resume Evaluation to Google Sheets (`main`, output 0, input 0)
- Trigger on new Email Received → Extract text from PDF File (`main`, output 0, input 0)
- OpenAI Chat Model (GPT 4o-mini) → AI Agent to evaluate Resume (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmail/0852_Gmail_GoogleSheets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmail/0852_Gmail_GoogleSheets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
