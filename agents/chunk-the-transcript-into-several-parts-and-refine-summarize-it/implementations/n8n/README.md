# Chunk the transcript into several parts, and refine-summarize it

This folder contains the **Chunk the transcript into several parts, and refine-summarize it** workflow. Its executable nodes use `agent`, `chainSummarization`, `code`, `documentDefaultDataLoader`, `gmail`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`chunk-the-transcript-into-several-parts-and-refine-summarize-it.json`](chunk-the-transcript-into-several-parts-and-refine-summarize-it.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Podcast Episode Transcript | `code` | Inspect parameters |
| Summarize Transcript | `chainSummarization` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Extract Topics & Questions | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Topics | `splitOut` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Format topic text & title | `code` | Inspect parameters |
| Send Digest | `gmail` | Inspect parameters |

## Connection map

- Topics → AI Agent (`main`, output 0, input 0)
- AI Agent → Format topic text & title (`main`, output 0, input 0)
- Wikipedia → AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Summarize Transcript (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Extract Topics & Questions (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Summarize Transcript (`ai_document`, output 0, input 0)
- Summarize Transcript → Extract Topics & Questions (`main`, output 0, input 0)
- Format topic text & title → Send Digest (`main`, output 0, input 0)
- Extract Topics & Questions → Topics (`main`, output 0, input 0)
- Podcast Episode Transcript → Summarize Transcript (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Podcast Episode Transcript (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0322_Splitout_Code_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0322_Splitout_Code_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
