# 🦙👁️👁️ Find the Best Local Ollama Vision Models by Comparison

This folder contains the **🦙👁️👁️ Find the Best Local Ollama Vision Models by Comparison** workflow. Its executable nodes use `extractFromFile`, `googleDocs`, `googleDrive`, `httpRequest`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`find-the-best-local-ollama-vision-models-by-comparison.json`](find-the-best-local-ollama-vision-models-by-comparison.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `googleDriveOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Ollama LLM Request | `httpRequest` | POST |
| Create Request Body | `set` | Inspect parameters |
| Loop Over Ollama Models | `splitInBatches` | Inspect parameters |
| Create Result Objects | `set` | Inspect parameters |
| General Image Prompt | `set` | Inspect parameters |
| Real Estate Spreadsheet Prompt | `set` | Inspect parameters |
| List of Vision Models | `set` | Inspect parameters |
| Get Base64 String | `extractFromFile` | binaryToPropery |
| Download Image File from Google Drive | `googleDrive` | download |
| Split List of Vision Models for Looping | `splitOut` | Inspect parameters |
| Google Doc Image Id | `set` | Inspect parameters |
| Save Image Descriptions to Google Docs | `googleDocs` | update |

## Connection map

- Get Base64 String → List of Vision Models (`main`, output 0, input 0)
- Ollama LLM Request → Loop Over Ollama Models (`main`, output 0, input 0)
- Create Request Body → Ollama LLM Request (`main`, output 0, input 0)
- Google Doc Image Id → Download Image File from Google Drive (`main`, output 0, input 0)
- General Image Prompt → Create Request Body (`main`, output 0, input 0)
- Create Result Objects → Save Image Descriptions to Google Docs (`main`, output 0, input 0)
- List of Vision Models → Split List of Vision Models for Looping (`main`, output 0, input 0)
- Loop Over Ollama Models → Create Result Objects (`main`, output 0, input 0)
- Loop Over Ollama Models → General Image Prompt (`main`, output 1, input 0)
- When clicking ‘Test workflow’ → Google Doc Image Id (`main`, output 0, input 0)
- Download Image File from Google Drive → Get Base64 String (`main`, output 0, input 0)
- Split List of Vision Models for Looping → Loop Over Ollama Models (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1903_Splitout_Googledocs_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1903_Splitout_Googledocs_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
