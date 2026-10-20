# Here you can modify the prompt

This folder contains the **Here you can modify the prompt** workflow. Its executable nodes use `chainLlm`, `code`, `emailSend`, `googleSheets`, `googleSheetsTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`here-you-can-modify-the-prompt.json`](here-you-can-modify-the-prompt.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `smtp`

**Entry nodes:** Google Sheets Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set your company's variables | `set` | Inspect parameters |
| Get linkedin Posts | `httpRequest` | Inspect parameters |
| Get twitter ID | `httpRequest` | Inspect parameters |
| Get tweets | `httpRequest` | Inspect parameters |
| Extract and limit Linkedin | `code` | Inspect parameters |
| Exract and limit X | `code` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Generate Subject and cover letter based on match | `chainLlm` | Inspect parameters |
| Send Cover letter and CC me | `emailSend` | Inspect parameters |
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| Google Sheets | `googleSheets` | update |
| If | `if` | Inspect parameters |

## Connection map

- If → Set your company's variables (`main`, output 0, input 0)
- Get tweets → Exract and limit X (`main`, output 0, input 0)
- Get twitter ID → Get tweets (`main`, output 0, input 0)
- OpenAI Chat Model → Generate Subject and cover letter based on match (`ai_languageModel`, output 0, input 0)
- Exract and limit X → Get linkedin Posts (`main`, output 0, input 0)
- Get linkedin Posts → Extract and limit Linkedin (`main`, output 0, input 0)
- Google Sheets Trigger → If (`main`, output 0, input 0)
- Structured Output Parser → Generate Subject and cover letter based on match (`ai_outputParser`, output 0, input 0)
- Extract and limit Linkedin → Generate Subject and cover letter based on match (`main`, output 0, input 0)
- Send Cover letter and CC me → Google Sheets (`main`, output 0, input 0)
- Set your company's variables → Get twitter ID (`main`, output 0, input 0)
- Generate Subject and cover letter based on match → Send Cover letter and CC me (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1664_Code_HTTP_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1664_Code_HTTP_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
