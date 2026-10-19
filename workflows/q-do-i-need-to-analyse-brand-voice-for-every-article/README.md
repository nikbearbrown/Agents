# Q. Do I need to analyse Brand Voice for every article?

This folder contains the **Q. Do I need to analyse Brand Voice for every article?** workflow. Its executable nodes use `aggregate`, `chainLlm`, `html`, `httpRequest`, `informationExtractor`, `limit`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `merge`, `set`, `splitOut`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`q-do-i-need-to-analyse-brand-voice-for-every-article.json`](q-do-i-need-to-analyse-brand-voice-for-every-article.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Extract Voice Characteristics | `informationExtractor` | Inspect parameters |
| Get Blog | `httpRequest` | Inspect parameters |
| Get Article | `httpRequest` | Inspect parameters |
| Extract Article URLs | `html` | extractHtmlContent |
| Split Out URLs | `splitOut` | Inspect parameters |
| Latest Articles | `limit` | Inspect parameters |
| Extract Article Content | `html` | extractHtmlContent |
| Combine Articles | `aggregate` | Inspect parameters |
| Article Style & Brand Voice | `merge` | Inspect parameters |
| Save as Draft | `wordpress` | Inspect parameters |
| Capture Existing Article Structure | `chainLlm` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Content Generation Agent | `informationExtractor` | Inspect parameters |
| New Article Instruction | `set` | Inspect parameters |

## Connection map

- Get Blog → Extract Article URLs (`main`, output 0, input 0)
- Markdown → Combine Articles (`main`, output 0, input 0)
- Get Article → Extract Article Content (`main`, output 0, input 0)
- Split Out URLs → Latest Articles (`main`, output 0, input 0)
- Latest Articles → Get Article (`main`, output 0, input 0)
- Combine Articles → Capture Existing Article Structure (`main`, output 0, input 0)
- Combine Articles → Extract Voice Characteristics (`main`, output 0, input 0)
- OpenAI Chat Model → Extract Voice Characteristics (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Content Generation Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Capture Existing Article Structure (`ai_languageModel`, output 0, input 0)
- Extract Article URLs → Split Out URLs (`main`, output 0, input 0)
- Extract Article Content → Markdown (`main`, output 0, input 0)
- New Article Instruction → Content Generation Agent (`main`, output 0, input 0)
- Content Generation Agent → Save as Draft (`main`, output 0, input 0)
- Article Style & Brand Voice → New Article Instruction (`main`, output 0, input 0)
- Extract Voice Characteristics → Article Style & Brand Voice (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Get Blog (`main`, output 0, input 0)
- Capture Existing Article Structure → Article Style & Brand Voice (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0664_Splitout_Limit_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0664_Splitout_Limit_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
