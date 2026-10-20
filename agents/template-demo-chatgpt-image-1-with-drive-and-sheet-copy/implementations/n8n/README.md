# template-demo-chatgpt-image-1-with-drive-and-sheet copy

This folder contains the **template-demo-chatgpt-image-1-with-drive-and-sheet copy** workflow. Its executable nodes use `aggregate`, `chatTrigger`, `convertToFile`, `googleDrive`, `googleSheets`, `httpRequest`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`template-demo-chatgpt-image-1-with-drive-and-sheet-copy.json`](template-demo-chatgpt-image-1-with-drive-and-sheet-copy.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking 'Test workflow', When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking 'Test workflow' | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Google Drive | `googleDrive` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Edit Fields-file_name | `set` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Sheets1 | `googleSheets` | append |
| Aggregate | `aggregate` | Inspect parameters |

## Connection map

- Aggregate → Google Sheets1 (`main`, output 0, input 0)
- Split Out → Loop Over Items (`main`, output 0, input 0)
- Edit Fields1 → Google Sheets (`main`, output 0, input 0)
- Google Drive → Edit Fields1 (`main`, output 0, input 0)
- HTTP Request → Split Out (`main`, output 0, input 0)
- Google Sheets → Loop Over Items (`main`, output 0, input 0)
- Convert to File → Google Drive (`main`, output 0, input 0)
- Loop Over Items → Aggregate (`main`, output 0, input 0)
- Loop Over Items → Edit Fields-file_name (`main`, output 1, input 0)
- Edit Fields-file_name → Convert to File (`main`, output 0, input 0)
- When chat message received → HTTP Request (`main`, output 0, input 0)
- When clicking 'Test workflow' → HTTP Request (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1983_Splitout_Converttofile_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1983_Splitout_Converttofile_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
