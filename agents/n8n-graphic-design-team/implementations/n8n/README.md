# n8n Graphic Design Team

This folder contains the **n8n Graphic Design Team** workflow. Its executable nodes use `chainLlm`, `convertToFile`, `formTrigger`, `gmail`, `googleDrive`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `outputParserStructured`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-graphic-design-team.json`](n8n-graphic-design-team.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’, On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Sheets | `googleSheets` | append |
| SetImageData | `set` | Inspect parameters |
| Google Drive | `googleDrive` | Inspect parameters |
| Download Image3 | `httpRequest` | Inspect parameters |
| ideogram Remix | `httpRequest` | POST |
| Set Upload Fields1 | `set` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Switch1 | `switch` | Inspect parameters |
| Image Reviewer | `chainLlm` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Google Drive Remix Image | `googleDrive` | Inspect parameters |
| Google Sheets - Add Remix | `googleSheets` | append |
| genImageURL1 | `set` | Inspect parameters |
| genImageURL2 | `set` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| TheImageURL | `set` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| creative brief | `set` | Inspect parameters |
| Ideogram Image generator | `httpRequest` | POST |
| GET image | `httpRequest` | Inspect parameters |
| RE creative brief | `set` | Inspect parameters |
| Get Remixed Image | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Convert to File | `convertToFile` | Inspect parameters |
| Spreadsheet | `set` | Inspect parameters |
| Google Drive - Create Folder | `googleDrive` | folder |
| Google Drive - Create Generations Folder | `googleDrive` | folder |
| Google Drive - Upload Spreadsheet | `googleDrive` | Inspect parameters |
| Gmail - Send Setup Details | `gmail` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |

## Connection map

- Switch1 → Gmail (`main`, output 0, input 0)
- Switch1 → RE creative brief (`main`, output 1, input 0)
- GET image → Google Drive (`main`, output 0, input 0)
- Spreadsheet → Convert to File (`main`, output 0, input 0)
- TheImageURL → Download Image (`main`, output 0, input 0)
- Google Drive → Google Sheets (`main`, output 0, input 0)
- SetImageData → GET image (`main`, output 0, input 0)
- genImageURL1 → TheImageURL (`main`, output 0, input 0)
- genImageURL2 → TheImageURL (`main`, output 0, input 0)
- Google Sheets → genImageURL1 (`main`, output 0, input 0)
- Download Image → Image Reviewer (`main`, output 0, input 0)
- Image Reviewer → Switch1 (`main`, output 0, input 0)
- creative brief → Ideogram Image generator (`main`, output 0, input 0)
- ideogram Remix → Set Upload Fields1 (`main`, output 0, input 0)
- Convert to File → Google Drive - Upload Spreadsheet (`main`, output 0, input 0)
- Download Image3 → ideogram Remix (`main`, output 0, input 0)
- Get Remixed Image → Google Drive Remix Image (`main`, output 0, input 0)
- RE creative brief → Download Image3 (`main`, output 0, input 0)
- On form submission → creative brief (`main`, output 0, input 0)
- OpenAI Chat Model1 → Image Reviewer (`ai_languageModel`, output 0, input 0)
- Set Upload Fields1 → Get Remixed Image (`main`, output 0, input 0)
- Google Drive Remix Image → Google Sheets - Add Remix (`main`, output 0, input 0)
- Ideogram Image generator → SetImageData (`main`, output 0, input 0)
- Google Sheets - Add Remix → genImageURL2 (`main`, output 0, input 0)
- Structured Output Parser1 → Image Reviewer (`ai_outputParser`, output 0, input 0)
- Google Drive - Create Folder → Google Drive - Create Generations Folder (`main`, output 0, input 0)
- Google Drive - Upload Spreadsheet → Gmail - Send Setup Details (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Google Drive - Create Folder (`main`, output 0, input 0)
- Google Drive - Create Generations Folder → Spreadsheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Converttofile/1985_Converttofile_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Converttofile/1985_Converttofile_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
