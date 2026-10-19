# youtube chapter generator

This folder contains the **youtube chapter generator** workflow. Its executable nodes use `chainLlm`, `extractFromFile`, `httpRequest`, `lmChatGoogleGemini`, `manualTrigger`, `outputParserStructured`, `set`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-chapter-generator.json`](youtube-chapter-generator.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `youTubeOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Caption ID | `httpRequest` | Inspect parameters |
| Get Captions | `httpRequest` | Inspect parameters |
| Extract Captions | `extractFromFile` | text |
| Structured Captions | `outputParserStructured` | Inspect parameters |
| Get Video Meta Data | `youTube` | video / get |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Set Video ID | `set` | Inspect parameters |
| Update Chapters | `youTube` | video / update |
| Tag Chapters in Description | `chainLlm` | Inspect parameters |

## Connection map

- Get Captions → Extract Captions (`main`, output 0, input 0)
- Set Video ID → Get Video Meta Data (`main`, output 0, input 0)
- Get Caption ID → Get Captions (`main`, output 0, input 0)
- Extract Captions → Tag Chapters in Description (`main`, output 0, input 0)
- Get Video Meta Data → Get Caption ID (`main`, output 0, input 0)
- Structured Captions → Tag Chapters in Description (`ai_outputParser`, output 0, input 0)
- Google Gemini Chat Model → Tag Chapters in Description (`ai_languageModel`, output 0, input 0)
- Tag Chapters in Description → Update Chapters (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Video ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1641_Extractfromfile_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1641_Extractfromfile_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
