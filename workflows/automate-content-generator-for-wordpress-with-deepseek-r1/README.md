# Automate Content Generator for WordPress with DeepSeek R1

This folder contains the **Automate Content Generator for WordPress with DeepSeek R1** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `manualTrigger`, `openAi`, `set`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-content-generator-for-wordpress-with-deepseek-r1.json`](automate-content-generator-for-wordpress-with-deepseek-r1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `wooCommerceApi`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Ideas | `googleSheets` | Inspect parameters |
| Set your prompt | `set` | Inspect parameters |
| Create post on Wordpress | `wordpress` | Inspect parameters |
| Upload image | `httpRequest` | POST |
| Set Image | `httpRequest` | POST |
| Update Sheet | `googleSheets` | update |
| Generate article with DeepSeek | `openAi` | Inspect parameters |
| Generate title with DeepSeek | `openAi` | Inspect parameters |
| Generate Image with DALL-E | `openAi` | image |

## Connection map

- Get Ideas → Set your prompt (`main`, output 0, input 0)
- Set Image → Update Sheet (`main`, output 0, input 0)
- Upload image → Set Image (`main`, output 0, input 0)
- Set your prompt → Generate article with DeepSeek (`main`, output 0, input 0)
- Create post on Wordpress → Generate Image with DALL-E (`main`, output 0, input 0)
- Generate Image with DALL-E → Upload image (`main`, output 0, input 0)
- Generate title with DeepSeek → Create post on Wordpress (`main`, output 0, input 0)
- Generate article with DeepSeek → Generate title with DeepSeek (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Ideas (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/1949_Wordpress_Manual_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/1949_Wordpress_Manual_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
