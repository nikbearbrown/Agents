# Attachments Gmail to drive and google sheets

This folder contains the **Attachments Gmail to drive and google sheets** workflow. Its executable nodes use `chainLlm`, `extractFromFile`, `gmail`, `gmailTrigger`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `lmOpenAi`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`attachments-gmail-to-drive-and-google-sheets.json`](attachments-gmail-to-drive-and-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** Gmail Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger1 | `gmailTrigger` | Inspect parameters |
| Setup1 | `set` | Inspect parameters |
| Upload PDF to Drive1 | `httpRequest` | POST |
| Rename file1 | `googleDrive` | update |
| Move to the correct folder1 | `googleDrive` | move |
| Gmail | `gmail` | markAsRead |
| Extract from File2 | `extractFromFile` | pdf |
| Google Drive | `googleDrive` | download |
| OpenAI Model | `lmOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Append to Reconciliation Sheet | `googleSheets` | append |
| Map Output | `set` | Inspect parameters |
| Apply Data Extraction Rules | `chainLlm` | Inspect parameters |
| Only invoice mails with attachments | `if` | Inspect parameters |

## Connection map

- Setup1 → Only invoice mails with attachments (`main`, output 0, input 0)
- Map Output → Append to Reconciliation Sheet (`main`, output 0, input 0)
- Google Drive → Extract from File2 (`main`, output 0, input 0)
- OpenAI Model → Apply Data Extraction Rules (`ai_languageModel`, output 0, input 0)
- Rename file1 → Move to the correct folder1 (`main`, output 0, input 0)
- Gmail Trigger1 → Setup1 (`main`, output 0, input 0)
- Extract from File2 → Apply Data Extraction Rules (`main`, output 0, input 0)
- Upload PDF to Drive1 → Rename file1 (`main`, output 0, input 0)
- Structured Output Parser → Apply Data Extraction Rules (`ai_outputParser`, output 0, input 0)
- Apply Data Extraction Rules → Map Output (`main`, output 0, input 0)
- Move to the correct folder1 → Gmail (`main`, output 0, input 0)
- Move to the correct folder1 → Google Drive (`main`, output 0, input 0)
- Only invoice mails with attachments → Upload PDF to Drive1 (`main`, output 0, input 0)
- Only invoice mails with attachments → Gmail (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1764_Extractfromfile_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1764_Extractfromfile_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
