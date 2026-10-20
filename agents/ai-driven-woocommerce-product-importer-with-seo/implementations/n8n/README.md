# AI-Driven WooCommerce Product Importer with SEO

This folder contains the **AI-Driven WooCommerce Product Importer with SEO** workflow. Its executable nodes use `chainLlm`, `code`, `googleSheets`, `lmChatOpenRouter`, `manualTrigger`, `outputParserStructured`, `splitInBatches`, `telegram`, `wooCommerce`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-driven-woocommerce-product-importer-with-seo.json`](ai-driven-woocommerce-product-importer-with-seo.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openRouterApi`, `telegramApi`, `wooCommerceApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| SEO Expert | `chainLlm` | Inspect parameters |
| Get products | `googleSheets` | Inspect parameters |
| Map categories | `code` | Inspect parameters |
| Create product | `wooCommerce` | product / create |
| Creation done | `googleSheets` | update |
| Update meta | `googleSheets` | update |
| Set SEO meta | `wooCommerce` | product / update |
| Loop products | `splitInBatches` | Inspect parameters |
| Send message | `telegram` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |

## Connection map

- SEO Expert → Set SEO meta (`main`, output 0, input 0)
- Update meta → Loop products (`main`, output 0, input 0)
- Get products → Loop products (`main`, output 0, input 0)
- Set SEO meta → Update meta (`main`, output 0, input 0)
- Creation done → SEO Expert (`main`, output 0, input 0)
- Loop products → Send message (`main`, output 0, input 0)
- Loop products → Map categories (`main`, output 1, input 0)
- Create product → Creation done (`main`, output 0, input 0)
- Map categories → Create product (`main`, output 0, input 0)
- OpenRouter Chat Model → SEO Expert (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → SEO Expert (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Get products (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1775_Telegram_Code_Import_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1775_Telegram_Code_Import_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
