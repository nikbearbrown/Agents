# request youtube transcript and summarization of a youtube script and receive form events

This folder contains the **request youtube transcript and summarization of a youtube script and receive form events** workflow. Its executable nodes use `chainSummarization`, `formTrigger`, `httpRequest`, `lmChatOpenAi`, `noOp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`request-youtube-transcript-and-summarization-of-a-youtube-script-and-receive-form-events.json`](request-youtube-transcript-and-summarization-of-a-youtube-script-and-receive-form-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** YouTube video URL

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Request YouTube Transcript | `httpRequest` | POST |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Summarization of a YouTube script | `chainSummarization` | Inspect parameters |
| YouTube video URL | `formTrigger` | Inspect parameters |
| Summarization Engine | `lmChatOpenAi` | Inspect parameters |

## Connection map

- YouTube video URL → Request YouTube Transcript (`main`, output 0, input 0)
- Summarization Engine → Summarization of a YouTube script (`ai_languageModel`, output 0, input 0)
- Request YouTube Transcript → Summarization of a YouTube script (`main`, output 0, input 0)
- Summarization of a YouTube script → No Operation, do nothing (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0687_HTTP_Form_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0687_HTTP_Form_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
