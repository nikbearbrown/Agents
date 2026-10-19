# 🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research

This folder contains the **🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research** workflow. Its executable nodes use `agent`, `aggregate`, `formTrigger`, `httpRequest`, `lmChatOpenAi`, `merge`, `openAi`, `outputParserStructured`, `set`, `telegram`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-seo-optimized-wordpress-content-with-perplexity-research.json`](generate-seo-optimized-wordpress-content-with-perplexity-research.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `telegramApi`, `wordpressApi`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Wordpress | `wordpress` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Create Title, Slug, Meta | `agent` | Inspect parameters |
| Create HTML | `openAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Upload Image to Wordpress | `httpRequest` | POST |
| Set Image on Wordpress Post | `httpRequest` | POST |
| On form submission | `formTrigger` | Inspect parameters |
| Perplexity Research | `httpRequest` | POST |
| Cleanup Links | `set` | Inspect parameters |
| Copywriter AI Agent | `agent` | Inspect parameters |
| Cleanup HTML  | `set` | Inspect parameters |
| GET Image | `httpRequest` | Inspect parameters |
| Set Image URL | `set` | Inspect parameters |
| Send Success Message to Telegram | `telegram` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Combine Blog Details | `aggregate` | Inspect parameters |

## Connection map

- Merge → Combine Blog Details (`main`, output 0, input 0)
- GET Image → Upload Image to Wordpress (`main`, output 0, input 0)
- Wordpress → Set Image URL (`main`, output 0, input 0)
- Create HTML → Merge (`main`, output 0, input 0)
- gpt-4o-mini → Copywriter AI Agent (`ai_languageModel`, output 0, input 0)
- Cleanup HTML  → Wordpress (`main`, output 0, input 0)
- Cleanup Links → Copywriter AI Agent (`main`, output 0, input 0)
- Set Image URL → GET Image (`main`, output 0, input 0)
- OpenAI Chat Model → Create Title, Slug, Meta (`ai_languageModel`, output 0, input 0)
- On form submission → Perplexity Research (`main`, output 0, input 0)
- Copywriter AI Agent → Create HTML (`main`, output 0, input 0)
- Copywriter AI Agent → Create Title, Slug, Meta (`main`, output 0, input 0)
- Copywriter AI Agent → Merge (`main`, output 0, input 1)
- Perplexity Research → Cleanup Links (`main`, output 0, input 0)
- Combine Blog Details → Cleanup HTML  (`main`, output 0, input 0)
- Create Title, Slug, Meta → Merge (`main`, output 0, input 2)
- Structured Output Parser → Create Title, Slug, Meta (`ai_outputParser`, output 0, input 0)
- Upload Image to Wordpress → Set Image on Wordpress Post (`main`, output 0, input 0)
- Set Image on Wordpress Post → Send Success Message to Telegram (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1070_Telegram_Wordpress_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1070_Telegram_Wordpress_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
