# ✨🔪 Advanced AI Powered Document Parsing & Text Extraction with Llama Parse

This folder contains the **✨🔪 Advanced AI Powered Document Parsing & Text Extraction with Llama Parse** workflow. Its executable nodes use `aggregate`, `chainLlm`, `gmail`, `gmailTrigger`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `limit`, `lmChatOpenAi`, `merge`, `noOp`, `set`, `telegram`, `textClassifier`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`advanced-ai-powered-document-parsing-text-extraction-with-llama-parse.json`](advanced-ai-powered-document-parsing-text-extraction-with-llama-parse.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Webhook, Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Gmail | `gmail` | getAll |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Get Message | `gmail` | get |
| Parse Document with LlamaParse | `httpRequest` | POST |
| Summarize Email | `chainLlm` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Save LlamaParse ID and Summary to Google Sheets | `googleSheets` | appendOrUpdate |
| Save Document to Google Drive | `googleDrive` | Inspect parameters |
| Extract Invoice Details as JSON | `chainLlm` | Inspect parameters |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| gpt-4o-mini2 | `lmChatOpenAi` | Inspect parameters |
| Update Google Sheet by LlamaParse ID | `googleSheets` | update |
| Invoice Details | `set` | Inspect parameters |
| Prepare Message | `set` | Inspect parameters |
| Send Invoice Details as Telegram Message | `telegram` | Inspect parameters |
| gpt-4o-mini3 | `lmChatOpenAi` | Inspect parameters |
| Send Error Message 2 | `telegram` | Inspect parameters |
| Send Error Message 1 | `telegram` | Inspect parameters |
| Send Document Summary as Telegram Message | `telegram` | Inspect parameters |
| Summarize Document | `chainLlm` | Inspect parameters |
| Classify Parsed Document | `textClassifier` | Inspect parameters |
| Get Parsed Markdown | `set` | Inspect parameters |
| Prepare Data | `set` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Is there an Email Attachement | `if` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Merge Email Processing | `merge` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| If Supported File Extensions | `if` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| No Operation, do nothing1 | `noOp` | Inspect parameters |
| Save Summarized Document to Google Drive | `googleDrive` | createFromText |
| Save Parsed Document to Google Drive | `googleDrive` | createFromText |

## Connection map

- Gmail → Limit (`main`, output 0, input 0)
- Limit → Get Message (`main`, output 0, input 0)
- Merge → Parse Document with LlamaParse (`main`, output 0, input 0)
- Merge → Save Document to Google Drive (`main`, output 0, input 0)
- Merge → Summarize Email (`main`, output 0, input 0)
- Webhook → Get Parsed Markdown (`main`, output 0, input 0)
- Aggregate → Edit Fields (`main`, output 0, input 0)
- Edit Fields → If Supported File Extensions (`main`, output 0, input 0)
- Get Message → Is there an Email Attachement (`main`, output 0, input 0)
- gpt-4o-mini → Summarize Email (`ai_languageModel`, output 0, input 0)
- HTTP Request → Aggregate (`main`, output 0, input 0)
- Prepare Data → Merge Email Processing (`main`, output 0, input 1)
- gpt-4o-mini1 → Classify Parsed Document (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini2 → Extract Invoice Details as JSON (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini3 → Summarize Document (`ai_languageModel`, output 0, input 0)
- Gmail Trigger → Gmail (`main`, output 0, input 0)
- Invoice Details → Prepare Message (`main`, output 0, input 0)
- Invoice Details → Update Google Sheet by LlamaParse ID (`main`, output 0, input 0)
- Prepare Message → Send Invoice Details as Telegram Message (`main`, output 0, input 0)
- Summarize Email → Merge Email Processing (`main`, output 0, input 2)
- Summarize Document → Send Document Summary as Telegram Message (`main`, output 0, input 0)
- Summarize Document → Save Summarized Document to Google Drive (`main`, output 0, input 0)
- Summarize Document → Send Error Message 1 (`main`, output 1, input 0)
- Get Parsed Markdown → Classify Parsed Document (`main`, output 0, input 0)
- Get Parsed Markdown → Save Parsed Document to Google Drive (`main`, output 0, input 0)
- Merge Email Processing → Save LlamaParse ID and Summary to Google Sheets (`main`, output 0, input 0)
- Classify Parsed Document → Summarize Document (`main`, output 0, input 0)
- Classify Parsed Document → Extract Invoice Details as JSON (`main`, output 1, input 0)
- If Supported File Extensions → Merge (`main`, output 0, input 1)
- If Supported File Extensions → No Operation, do nothing1 (`main`, output 1, input 0)
- Is there an Email Attachement → HTTP Request (`main`, output 0, input 0)
- Is there an Email Attachement → Merge (`main`, output 0, input 0)
- Is there an Email Attachement → No Operation, do nothing (`main`, output 1, input 0)
- Save Document to Google Drive → Prepare Data (`main`, output 0, input 0)
- Parse Document with LlamaParse → Merge Email Processing (`main`, output 0, input 0)
- Extract Invoice Details as JSON → Invoice Details (`main`, output 0, input 0)
- Extract Invoice Details as JSON → Send Error Message 2 (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1904_Telegram_Limit_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1904_Telegram_Limit_Process_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
