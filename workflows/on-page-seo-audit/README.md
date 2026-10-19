# 🤖 On-Page SEO Audit

This folder contains the **🤖 On-Page SEO Audit** workflow. Its executable nodes use `agent`, `aggregate`, `formTrigger`, `gmail`, `httpRequest`, `lmChatOpenAi`, `markdown`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`on-page-seo-audit.json`](on-page-seo-audit.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Landing Page Url

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Landing Page Url | `formTrigger` | Inspect parameters |
| Scrape Website | `httpRequest` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Content Audit | `agent` | Inspect parameters |
| Technical Audit | `agent` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |

## Connection map

- Merge → Aggregate (`main`, output 0, input 0)
- Markdown → Gmail (`main`, output 0, input 0)
- Aggregate → Markdown (`main`, output 0, input 0)
- Content Audit → Merge (`main`, output 0, input 1)
- Scrape Website → Content Audit (`main`, output 0, input 0)
- Scrape Website → Technical Audit (`main`, output 0, input 0)
- Technical Audit → Merge (`main`, output 0, input 0)
- Landing Page Url → Scrape Website (`main`, output 0, input 0)
- OpenAI Chat Model → Technical Audit (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Content Audit (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1886_Form_Markdown_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1886_Form_Markdown_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
