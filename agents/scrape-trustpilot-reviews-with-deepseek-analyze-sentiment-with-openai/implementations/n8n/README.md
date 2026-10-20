# Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI

This folder contains the **Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI** workflow. Its executable nodes use `googleSheets`, `html`, `httpRequest`, `if`, `informationExtractor`, `limit`, `lmChatOpenAi`, `manualTrigger`, `sentimentAnalysis`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-trustpilot-reviews-with-deepseek-analyze-sentiment-with-openai.json`](scrape-trustpilot-reviews-with-deepseek-analyze-sentiment-with-openai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| If | `if` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Limit1 | `limit` | Inspect parameters |
| Set Parameters | `set` | Inspect parameters |
| Get reviews | `httpRequest` | Inspect parameters |
| Extract | `html` | extractHtmlContent |
| Get rows | `googleSheets` | Inspect parameters |
| Get Google Sheets | `googleSheets` | appendOrUpdate |
| Get Single review | `httpRequest` | Inspect parameters |
| Extract review | `html` | extractHtmlContent |
| Update sheet | `googleSheets` | appendOrUpdate |
| Sentiment Analysis | `sentimentAnalysis` | Inspect parameters |
| DeepSeek Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- If → Get Single review (`main`, output 0, input 0)
- Limit1 → Get Google Sheets (`main`, output 0, input 0)
- Extract → Split Out (`main`, output 0, input 0)
- Get rows → If (`main`, output 0, input 0)
- Split Out → Limit1 (`main`, output 0, input 0)
- Get reviews → Extract (`main`, output 0, input 0)
- Extract review → Information Extractor (`main`, output 0, input 0)
- Set Parameters → Get reviews (`main`, output 0, input 0)
- Get Google Sheets → Get rows (`main`, output 0, input 0)
- Get Single review → Extract review (`main`, output 0, input 0)
- OpenAI Chat Model → Sentiment Analysis (`ai_languageModel`, output 0, input 0)
- Sentiment Analysis → Update sheet (`main`, output 0, input 0)
- Sentiment Analysis → Update sheet (`main`, output 1, input 0)
- Sentiment Analysis → Update sheet (`main`, output 2, input 0)
- DeepSeek Chat Model → Information Extractor (`ai_languageModel`, output 0, input 0)
- Information Extractor → Sentiment Analysis (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Parameters (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1645_Limit_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1645_Limit_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
