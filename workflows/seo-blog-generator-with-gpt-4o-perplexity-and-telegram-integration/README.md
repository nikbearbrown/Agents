# SEO Blog Generator with GPT-4o, Perplexity, and Telegram Integration

This folder contains the **SEO Blog Generator with GPT-4o, Perplexity, and Telegram Integration** workflow. Its executable nodes use `agent`, `aggregate`, `formTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `outputParserStructured`, `telegram`, `telegramTrigger`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`seo-blog-generator-with-gpt-4o-perplexity-and-telegram-integration.json`](seo-blog-generator-with-gpt-4o-perplexity-and-telegram-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** On form submission, Tele HoangSP_Social_Media

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Metadata Generator | `agent` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Blog Content Generator | `agent` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Combine Blog Details | `aggregate` | Inspect parameters |
| Perplexity_Searcher | `toolWorkflow` | Inspect parameters |
| Tele HoangSP_Social_Media | `telegramTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Metadata Extractor | `outputParserStructured` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Simple Memory1 | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Merge → Telegram (`main`, output 0, input 0)
- Merge → Combine Blog Details (`main`, output 0, input 0)
- AI Agent → Copywriter AI Agent (`main`, output 0, input 0)
- AI Agent1 → Merge (`main`, output 0, input 1)
- gpt-4o-mini → Copywriter AI Agent (`ai_languageModel`, output 0, input 0)
- Simple Memory → AI Agent1 (`ai_memory`, output 0, input 0)
- Simple Memory1 → Create Title, Slug, Meta (`ai_memory`, output 0, input 0)
- OpenAI Chat Model → Create Title, Slug, Meta (`ai_languageModel`, output 0, input 0)
- On form submission → AI Agent (`main`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- Copywriter AI Agent → Create Title, Slug, Meta (`main`, output 0, input 0)
- Copywriter AI Agent → AI Agent1 (`main`, output 0, input 0)
- Call n8n Workflow Tool → AI Agent (`ai_tool`, output 0, input 0)
- Create Title, Slug, Meta → Merge (`main`, output 0, input 0)
- Structured Output Parser → Create Title, Slug, Meta (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → AI Agent1 (`ai_outputParser`, output 0, input 0)
- Tele HoangSP_Social_Media → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_source": 4, "missing_connection_target": 6}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1762_Form_Aggregate_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1762_Form_Aggregate_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
