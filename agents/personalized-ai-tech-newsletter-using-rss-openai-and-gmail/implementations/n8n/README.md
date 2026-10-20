# Personalized AI Tech Newsletter Using RSS, OpenAI and Gmail

This folder contains the **Personalized AI Tech Newsletter Using RSS, OpenAI and Gmail** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `gmail`, `lmChatOpenAi`, `markdown`, `rssFeedRead`, `scheduleTrigger`, `set`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreInMemory`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`personalized-ai-tech-newsletter-using-rss-openai-and-gmail.json`](personalized-ai-tech-newsletter-using-rss-openai-and-gmail.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Get Articles Daily, Send Weekly Summary

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Normalize Fields | `set` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Get Articles Daily | `scheduleTrigger` | Inspect parameters |
| Send Weekly Summary | `scheduleTrigger` | Inspect parameters |
| News reader AI | `agent` | Inspect parameters |
| Send Newsletter | `gmail` | Inspect parameters |
| Convert Response to an Email-Friendly Format | `markdown` | Inspect parameters |
| Your topics of interest | `set` | Inspect parameters |
| Store News Articles | `vectorStoreInMemory` | Inspect parameters |
| Set Tech News RSS Feeds | `set` | Inspect parameters |
| Read RSS News Feeds | `rssFeedRead` | Inspect parameters |
| Get News Articles | `vectorStoreInMemory` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |

## Connection map

- Split Out → Read RSS News Feeds (`main`, output 0, input 0)
- News reader AI → Convert Response to an Email-Friendly Format (`main`, output 0, input 0)
- Normalize Fields → Store News Articles (`main`, output 0, input 0)
- Embeddings OpenAI → Store News Articles (`ai_embedding`, output 0, input 0)
- Get News Articles → News reader AI (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → News reader AI (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI2 → Get News Articles (`ai_embedding`, output 0, input 0)
- Get Articles Daily → Set Tech News RSS Feeds (`main`, output 0, input 0)
- Default Data Loader → Store News Articles (`ai_document`, output 0, input 0)
- Read RSS News Feeds → Normalize Fields (`main`, output 0, input 0)
- Send Weekly Summary → Your topics of interest (`main`, output 0, input 0)
- Set Tech News RSS Feeds → Split Out (`main`, output 0, input 0)
- Your topics of interest → News reader AI (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Convert Response to an Email-Friendly Format → Send Newsletter (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1934_Splitout_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1934_Splitout_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
