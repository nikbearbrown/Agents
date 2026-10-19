# Scrape latest Paul Graham essays

This folder contains the **Scrape latest Paul Graham essays** workflow. Its executable nodes use `chainSummarization`, `documentDefaultDataLoader`, `html`, `httpRequest`, `limit`, `lmChatOpenAi`, `manualTrigger`, `merge`, `set`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-latest-paul-graham-essays-49a09065.json`](scrape-latest-paul-graham-essays-49a09065.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Fetch essay list | `httpRequest` | Inspect parameters |
| Extract essay names | `html` | extractHtmlContent |
| Fetch essay texts | `httpRequest` | Inspect parameters |
| Extract title | `html` | extractHtmlContent |
| Clean up | `set` | Inspect parameters |
| Split out into items | `splitOut` | Inspect parameters |
| Limit to first 3 | `limit` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |

## Connection map

- Merge → Clean up (`main`, output 0, input 0)
- Extract title → Merge (`main`, output 0, input 0)
- Fetch essay list → Extract essay names (`main`, output 0, input 0)
- Limit to first 3 → Fetch essay texts (`main`, output 0, input 0)
- Fetch essay texts → Extract title (`main`, output 0, input 0)
- Fetch essay texts → Summarization Chain (`main`, output 0, input 0)
- OpenAI Chat Model1 → Summarization Chain (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Summarization Chain (`ai_document`, output 0, input 0)
- Extract essay names → Split out into items (`main`, output 0, input 0)
- Summarization Chain → Merge (`main`, output 0, input 1)
- Split out into items → Limit to first 3 (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Fetch essay list (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1647_Splitout_Limit_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1647_Splitout_Limit_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
