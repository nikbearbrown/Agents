# http request and generate french audio and translate text to english

This folder contains the **http request and generate french audio and translate text to english** workflow. Its executable nodes use `chainLlm`, `code`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-generate-french-audio-and-translate-text-to-english.json`](http-request-and-generate-french-audio-and-translate-text-to-english.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Transcribe audio | `httpRequest` | POST |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Set ElevenLabs voice ID and text | `set` | Inspect parameters |
| Generate French Audio | `httpRequest` | POST |
| Translate Text to English | `chainLlm` | Inspect parameters |
| Translate English text to speech | `httpRequest` | POST |
| Add Filename | `code` | Inspect parameters |

## Connection map

- Add Filename → Transcribe audio (`main`, output 0, input 0)
- Transcribe audio → Translate Text to English (`main`, output 0, input 0)
- OpenAI Chat Model1 → Translate Text to English (`ai_languageModel`, output 0, input 0)
- Generate French Audio → Add Filename (`main`, output 0, input 0)
- Translate Text to English → Translate English text to speech (`main`, output 0, input 0)
- Set ElevenLabs voice ID and text → Generate French Audio (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Set ElevenLabs voice ID and text (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0400_Manual_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0400_Manual_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
