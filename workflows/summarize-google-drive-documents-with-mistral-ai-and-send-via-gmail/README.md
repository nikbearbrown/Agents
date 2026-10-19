# Summarize Google Drive Documents with Mistral AI and Send via Gmail

This folder contains the **Summarize Google Drive Documents with Mistral AI and Send via Gmail** workflow. Its executable nodes use `chainSummarization`, `gmail`, `googleDrive`, `lmChatMistralCloud`, `manualTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`summarize-google-drive-documents-with-mistral-ai-and-send-via-gmail.json`](summarize-google-drive-documents-with-mistral-ai-and-send-via-gmail.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `mistralCloudApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Mistral Cloud Chat Model | `lmChatMistralCloud` | Inspect parameters |
| Download uploaded File from Google Drive | `googleDrive` | download |
| Summarization Chain to summarize a file | `chainSummarization` | Inspect parameters |
| Send Summarized text to Gmail | `gmail` | Inspect parameters |

## Connection map

- Mistral Cloud Chat Model → Summarization Chain to summarize a file (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Download uploaded File from Google Drive (`main`, output 0, input 0)
- Summarization Chain to summarize a file → Send Summarized text to Gmail (`main`, output 0, input 0)
- Download uploaded File from Google Drive → Summarization Chain to summarize a file (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1528_Manual_Gmail_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1528_Manual_Gmail_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
