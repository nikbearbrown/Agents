# transcribing bank statements to markdown using gemini vision ai

This folder contains the **transcribing bank statements to markdown using gemini vision ai** workflow. Its executable nodes use `code`, `extractFromFile`, `filter`, `httpRequest`, `if`, `lmChatGoogleGemini`, `markdown`, `microsoftExcel`, `microsoftOutlook`, `noOp`, `scheduleTrigger`, `set`, `splitInBatches`, `textClassifier`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`transcribing-bank-statements-to-markdown-using-gemini-vision-ai.json`](transcribing-bank-statements-to-markdown-using-gemini-vision-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `microsoftExcelOAuth2Api`, `microsoftOutlookOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Attachments | `code` | Inspect parameters |
| Download Attachments | `microsoftOutlook` | get |
| Parse Output | `set` | Inspect parameters |
| For Each Message | `splitInBatches` | Inspect parameters |
| Message Ref | `noOp` | Inspect parameters |
| Message Classifier | `textClassifier` | Inspect parameters |
| Extract from File | `extractFromFile` | binaryToPropery |
| Markdown | `markdown` | Inspect parameters |
| Empty Response | `set` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Filter Invoices | `filter` | Inspect parameters |
| Has Invoice? | `if` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Recent Messages | `microsoftOutlook` | getAll |
| Model | `lmChatGoogleGemini` | Inspect parameters |
| Microsoft Excel 365 | `microsoftExcel` | worksheet / append |
| Invoice Classifier With Gemini 2.0 | `httpRequest` | POST |
| File-Based OCR with Gemini 2.0 | `httpRequest` | POST |

## Connection map

- Wait → For Each Message (`main`, output 0, input 0)
- Model → Message Classifier (`ai_languageModel`, output 0, input 0)
- Markdown → Message Classifier (`main`, output 0, input 0)
- Message Ref → Download Attachments (`main`, output 0, input 0)
- Has Invoice? → File-Based OCR with Gemini 2.0 (`main`, output 0, input 0)
- Has Invoice? → Empty Response (`main`, output 1, input 0)
- Parse Output → Wait (`main`, output 0, input 0)
- Empty Response → Wait (`main`, output 0, input 0)
- Filter Invoices → Has Invoice? (`main`, output 0, input 0)
- For Each Message → Microsoft Excel 365 (`main`, output 0, input 0)
- For Each Message → Message Ref (`main`, output 1, input 0)
- Schedule Trigger → Get Recent Messages (`main`, output 0, input 0)
- Extract from File → Invoice Classifier With Gemini 2.0 (`main`, output 0, input 0)
- Split Attachments → Extract from File (`main`, output 0, input 0)
- Message Classifier → For Each Message (`main`, output 0, input 0)
- Get Recent Messages → Markdown (`main`, output 0, input 0)
- Download Attachments → Split Attachments (`main`, output 0, input 0)
- File-Based OCR with Gemini 2.0 → Parse Output (`main`, output 0, input 0)
- File-Based OCR with Gemini 2.0 → Empty Response (`main`, output 1, input 0)
- Invoice Classifier With Gemini 2.0 → Filter Invoices (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0820_Wait_Code_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0820_Wait_Code_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
