# Automate PDF Image Extraction & Analysis with GPT-4o and Google Drive

This folder contains the **Automate PDF Image Extraction & Analysis with GPT-4o and Google Drive** workflow. Its executable nodes use `code`, `convertToFile`, `googleDrive`, `httpRequest`, `manualTrigger`, `openAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-pdf-image-extraction-analysis-with-gpt-4o-and-google-drive.json`](automate-pdf-image-extraction-analysis-with-gpt-4o-and-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get pdf file | `googleDrive` | download |
| Get all img_url | `set` | Inspect parameters |
| Analyze image | `openAi` | image / analyze |
| Extract pdf image | `httpRequest` | POST |
| Get image data | `splitOut` | Inspect parameters |
| Get image analyze content | `set` | Inspect parameters |
| Integrate all content to a a content | `code` | Inspect parameters |
| Output content to a .txt file | `convertToFile` | toText |

## Connection map

- Get pdf file → Extract pdf image (`main`, output 0, input 0)
- Analyze image → Get image analyze content (`main`, output 0, input 0)
- Get image data → Get all img_url (`main`, output 0, input 0)
- Get all img_url → Analyze image (`main`, output 0, input 0)
- Extract pdf image → Get image data (`main`, output 0, input 0)
- Get image analyze content → Integrate all content to a a content (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get pdf file (`main`, output 0, input 0)
- Integrate all content to a a content → Output content to a .txt file (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1559_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1559_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
