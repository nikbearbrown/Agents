# Extract text from PDF and image using Vertex AI (Gemini) into CSV

This folder contains the **Extract text from PDF and image using Vertex AI (Gemini) into CSV** workflow. Its executable nodes use `chainLlm`, `convertToFile`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `lmChatGoogleGemini`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-text-from-pdf-and-image-using-vertex-ai-gemini-into-csv.json`](extract-text-from-pdf-and-image-using-vertex-ai-gemini-into-csv.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `googlePalmApi`, `httpHeaderAuth`

**Entry nodes:** Get PDF or Images

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Get PDF or Images | `googleDriveTrigger` | Inspect parameters |
| Route based on PDF or Image | `switch` | Inspect parameters |
| Download PDF | `googleDrive` | download |
| Download Image | `googleDrive` | download |
| Extract data from PDF | `extractFromFile` | pdf |
| Send data to A.I. | `httpRequest` | POST |
| Convert to CSV | `convertToFile` | Inspect parameters |
| Upload to Google Drive | `googleDrive` | Inspect parameters |
| Convert to CSV2 | `convertToFile` | Inspect parameters |
| Upload to Google Drive1 | `googleDrive` | Inspect parameters |
| Vertex A.I. extract text | `chainLlm` | Inspect parameters |

## Connection map

- Download PDF → Extract data from PDF (`main`, output 0, input 0)
- Convert to CSV → Upload to Google Drive (`main`, output 0, input 0)
- Download Image → Vertex A.I. extract text (`main`, output 0, input 0)
- Convert to CSV2 → Upload to Google Drive1 (`main`, output 0, input 0)
- Get PDF or Images → Route based on PDF or Image (`main`, output 0, input 0)
- Send data to A.I. → Convert to CSV (`main`, output 0, input 0)
- Extract data from PDF → Send data to A.I. (`main`, output 0, input 0)
- Google Gemini Chat Model → Vertex A.I. extract text (`ai_languageModel`, output 0, input 0)
- Vertex A.I. extract text → Convert to CSV2 (`main`, output 0, input 0)
- Route based on PDF or Image → Download PDF (`main`, output 0, input 0)
- Route based on PDF or Image → Download Image (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1444_Extractfromfile_Converttofile_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1444_Extractfromfile_Converttofile_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
