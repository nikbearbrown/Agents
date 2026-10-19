# SearchApi Youtube Video Summary

This folder contains the **SearchApi Youtube Video Summary** workflow. Its executable nodes use `chainSummarization`, `lmChatOpenAi`, `manualTrigger`, `searchApi`, `splitOut`, `summarize`, `textSplitterRecursiveCharacterTextSplitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`searchapi-youtube-video-summary.json`](searchapi-youtube-video-summary.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Summarize | `summarize` | Inspect parameters |
| SearchApi | `searchApi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- SearchApi → Split Out (`main`, output 0, input 0)
- Split Out → Summarize (`main`, output 0, input 0)
- Summarize → Summarization Chain (`main`, output 0, input 0)
- OpenAI Chat Model → Summarization Chain (`ai_languageModel`, output 0, input 0)
- Recursive Character Text Splitter → Summarization Chain (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → SearchApi (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1552_Manual_Summarize_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1552_Manual_Summarize_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
