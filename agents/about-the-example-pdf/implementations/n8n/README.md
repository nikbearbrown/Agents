# 💡 About the Example PDF

This folder contains the **💡 About the Example PDF** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `compression`, `editImage`, `googleDrive`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `sort`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`about-the-example-pdf.json`](about-the-example-pdf.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Sort Pages | `sort` | Inspect parameters |
| Get Bank Statement | `googleDrive` | download |
| Split PDF into Images | `httpRequest` | POST |
| Extract Zip File | `compression` | Inspect parameters |
| Images To List | `code` | Inspect parameters |
| Resize Images For AI | `editImage` | resize |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Combine All Pages | `aggregate` | Inspect parameters |
| Extract All Deposit Table Rows | `informationExtractor` | Inspect parameters |
| Transcribe to Markdown | `chainLlm` | Inspect parameters |

## Connection map

- Sort Pages → Resize Images For AI (`main`, output 0, input 0)
- Images To List → Sort Pages (`main`, output 0, input 0)
- Extract Zip File → Images To List (`main`, output 0, input 0)
- Combine All Pages → Extract All Deposit Table Rows (`main`, output 0, input 0)
- Get Bank Statement → Split PDF into Images (`main`, output 0, input 0)
- Resize Images For AI → Transcribe to Markdown (`main`, output 0, input 0)
- Split PDF into Images → Extract Zip File (`main`, output 0, input 0)
- Transcribe to Markdown → Combine All Pages (`main`, output 0, input 0)
- Google Gemini Chat Model → Transcribe to Markdown (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model1 → Extract All Deposit Table Rows (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Bank Statement (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0580_Code_Editimage_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0580_Code_Editimage_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
