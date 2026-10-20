# Spot Workplace Discrimination Patterns with AI

This folder contains the **Spot Workplace Discrimination Patterns with AI** workflow. Its executable nodes use `chainLlm`, `code`, `html`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `merge`, `quickChart`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`spot-workplace-discrimination-patterns-with-ai.json`](spot-workplace-discrimination-patterns-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpQueryAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| SET company_name | `set` | Inspect parameters |
| Define dictionary of demographic keys | `set` | Inspect parameters |
| ScrapingBee Search Glassdoor | `httpRequest` | Inspect parameters |
| Extract company url path | `html` | extractHtmlContent |
| ScrapingBee GET company page contents | `httpRequest` | Inspect parameters |
| Extract reviews page url path | `html` | extractHtmlContent |
| ScrapingBee GET Glassdoor Reviews Content | `httpRequest` | Inspect parameters |
| Extract Overall Review Summary | `html` | extractHtmlContent |
| Extract Demographics Module | `html` | extractHtmlContent |
| Extract overall ratings and distribution percentages | `informationExtractor` | Inspect parameters |
| Extract demographic distributions | `informationExtractor` | Inspect parameters |
| Define contributions to variance | `set` | Inspect parameters |
| Set variance and std_dev | `set` | Inspect parameters |
| Calculate P-Scores | `code` | Inspect parameters |
| Sort Effect Sizes | `set` | Inspect parameters |
| Calculate Z-Scores and Effect Sizes | `set` | Inspect parameters |
| Format dataset for scatterplot | `code` | Inspect parameters |
| Specify additional parameters for scatterplot | `set` | Inspect parameters |
| Quickchart Scatterplot | `httpRequest` | Inspect parameters |
| QuickChart Bar Chart | `quickChart` | Inspect parameters |
| Text Analysis of Bias Data | `chainLlm` | Inspect parameters |

## Connection map

- Merge → Calculate Z-Scores and Effect Sizes (`main`, output 0, input 0)
- SET company_name → Define dictionary of demographic keys (`main`, output 0, input 0)
- OpenAI Chat Model → Text Analysis of Bias Data (`ai_languageModel`, output 0, input 0)
- Sort Effect Sizes → QuickChart Bar Chart (`main`, output 0, input 0)
- Sort Effect Sizes → Text Analysis of Bias Data (`main`, output 0, input 0)
- Calculate P-Scores → Sort Effect Sizes (`main`, output 0, input 0)
- OpenAI Chat Model1 → Extract demographic distributions (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Extract overall ratings and distribution percentages (`ai_languageModel`, output 0, input 0)
- Extract company url path → ScrapingBee GET company page contents (`main`, output 0, input 0)
- Set variance and std_dev → Merge (`main`, output 0, input 0)
- Extract Demographics Module → Extract demographic distributions (`main`, output 0, input 0)
- ScrapingBee Search Glassdoor → Extract company url path (`main`, output 0, input 0)
- Extract reviews page url path → ScrapingBee GET Glassdoor Reviews Content (`main`, output 0, input 0)
- Extract Overall Review Summary → Extract overall ratings and distribution percentages (`main`, output 0, input 0)
- Format dataset for scatterplot → Specify additional parameters for scatterplot (`main`, output 0, input 0)
- Define contributions to variance → Set variance and std_dev (`main`, output 0, input 0)
- Extract demographic distributions → Merge (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → SET company_name (`main`, output 0, input 0)
- Calculate Z-Scores and Effect Sizes → Calculate P-Scores (`main`, output 0, input 0)
- Calculate Z-Scores and Effect Sizes → Format dataset for scatterplot (`main`, output 0, input 0)
- Define dictionary of demographic keys → ScrapingBee Search Glassdoor (`main`, output 0, input 0)
- ScrapingBee GET company page contents → Extract reviews page url path (`main`, output 0, input 0)
- ScrapingBee GET Glassdoor Reviews Content → Extract Demographics Module (`main`, output 0, input 0)
- ScrapingBee GET Glassdoor Reviews Content → Extract Overall Review Summary (`main`, output 0, input 0)
- Specify additional parameters for scatterplot → Quickchart Scatterplot (`main`, output 0, input 0)
- Extract overall ratings and distribution percentages → Define contributions to variance (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1994_Code_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1994_Code_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
