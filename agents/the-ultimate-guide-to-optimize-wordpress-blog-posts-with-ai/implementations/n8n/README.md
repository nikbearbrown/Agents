# The Ultimate Guide to Optimize WordPress Blog Posts with AI

This folder contains the **The Ultimate Guide to Optimize WordPress Blog Posts with AI** workflow. Its executable nodes use `chainLlm`, `googleSheets`, `httpRequest`, `lmChatOpenRouter`, `manualTrigger`, `openAi`, `outputParserStructured`, `set`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`the-ultimate-guide-to-optimize-wordpress-blog-posts-with-ai.json`](the-ultimate-guide-to-optimize-wordpress-blog-posts-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpBasicAuth`, `openAiApi`, `openRouterApi`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get context | `googleSheets` | Inspect parameters |
| Set context | `set` | Inspect parameters |
| Generate title | `openAi` | Inspect parameters |
| Generate article | `openAi` | Inspect parameters |
| Add draft to WP | `wordpress` | Inspect parameters |
| Generate image | `openAi` | image |
| Upload image | `httpRequest` | POST |
| Set image | `httpRequest` | POST |
| Update Sheet | `googleSheets` | update |
| SEO Expert | `chainLlm` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Set metatag | `httpRequest` | PUT |
| Finish work | `googleSheets` | update |

## Connection map

- Set image → Update Sheet (`main`, output 0, input 0)
- SEO Expert → Set metatag (`main`, output 0, input 0)
- Get context → Set context (`main`, output 0, input 0)
- Set context → Generate article (`main`, output 0, input 0)
- Set metatag → Finish work (`main`, output 0, input 0)
- Update Sheet → SEO Expert (`main`, output 0, input 0)
- Upload image → Set image (`main`, output 0, input 0)
- Generate image → Upload image (`main`, output 0, input 0)
- Generate title → Add draft to WP (`main`, output 0, input 0)
- Add draft to WP → Generate image (`main`, output 0, input 0)
- Generate article → Generate title (`main`, output 0, input 0)
- OpenRouter Chat Model → SEO Expert (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → SEO Expert (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Get context (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/1550_Wordpress_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/1550_Wordpress_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
