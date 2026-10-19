# Generate Company Stories from LinkedIn with Bright Data & Google Gemini

This folder contains the **Generate Company Stories from LinkedIn with Bright Data & Google Gemini** workflow. Its executable nodes use `chainSummarization`, `documentDefaultDataLoader`, `httpRequest`, `if`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-company-stories-from-linkedin-with-bright-data-google-gemini.json`](generate-company-stories-from-linkedin-with-bright-data-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Snapshot Id | `set` | Inspect parameters |
| Download Snapshot | `httpRequest` | Inspect parameters |
| Set LinkedIn URL | `set` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Check on the errors | `if` | Inspect parameters |
| Perform LinkedIn Web Request | `httpRequest` | POST |
| Check Snapshot Status | `httpRequest` | Inspect parameters |
| LinkedIn Data Extractor | `informationExtractor` | Inspect parameters |
| Concise Summary Generator | `chainSummarization` | Inspect parameters |
| Webhook Notifier for Data Extractor | `httpRequest` | Inspect parameters |
| Webhook Notifier for Summary Generator | `httpRequest` | Inspect parameters |
| Wait for 30 seconds | `wait` | Inspect parameters |

## Connection map

- If → Check on the errors (`main`, output 0, input 0)
- If → Wait for 30 seconds (`main`, output 1, input 0)
- Set Snapshot Id → Check Snapshot Status (`main`, output 0, input 0)
- Set LinkedIn URL → Perform LinkedIn Web Request (`main`, output 0, input 0)
- Download Snapshot → LinkedIn Data Extractor (`main`, output 0, input 0)
- Check on the errors → Download Snapshot (`main`, output 0, input 0)
- Default Data Loader → Concise Summary Generator (`ai_document`, output 0, input 0)
- Wait for 30 seconds → Check Snapshot Status (`main`, output 0, input 0)
- Check Snapshot Status → If (`main`, output 0, input 0)
- LinkedIn Data Extractor → Concise Summary Generator (`main`, output 0, input 0)
- LinkedIn Data Extractor → Webhook Notifier for Data Extractor (`main`, output 0, input 0)
- Google Gemini Chat Model → Concise Summary Generator (`ai_languageModel`, output 0, input 0)
- Concise Summary Generator → Webhook Notifier for Summary Generator (`main`, output 0, input 0)
- Google Gemini Chat Model1 → LinkedIn Data Extractor (`ai_languageModel`, output 0, input 0)
- Perform LinkedIn Web Request → Set Snapshot Id (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Set LinkedIn URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1960_Manual_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1960_Manual_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
