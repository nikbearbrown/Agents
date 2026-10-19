# Automate Etsy Data Mining with Bright Data Scrape & Google Gemini

This folder contains the **Automate Etsy Data Mining with Bright Data Scrape & Google Gemini** workflow. Its executable nodes use `function`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `lmChatOpenAi`, `manualTrigger`, `readWriteFile`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-etsy-data-mining-with-bright-data-scrape-google-gemini.json`](automate-etsy-data-mining-with-bright-data-scrape-google-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set Esty Search Query | `set` | Inspect parameters |
| Perform Esty Web Request | `httpRequest` | POST |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Perform Esty web request over the loop | `httpRequest` | POST |
| Initiate a Webhook Notification for the extracted data | `httpRequest` | Inspect parameters |
| Extract Item List with the Product Info | `informationExtractor` | Inspect parameters |
| Google Gemini Chat Model for product info | `lmChatGoogleGemini` | Inspect parameters |
| Extract Paginated Resultset | `informationExtractor` | Inspect parameters |
| Write the scraped content to disk | `readWriteFile` | write |
| Create a binary data | `function` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Extract Paginated Resultset With OpenAI | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Split Out → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Perform Esty web request over the loop (`main`, output 1, input 0)
- OpenAI Chat Model → Extract Paginated Resultset With OpenAI (`ai_languageModel`, output 0, input 0)
- Create a binary data → Write the scraped content to disk (`main`, output 0, input 0)
- Set Esty Search Query → Perform Esty Web Request (`main`, output 0, input 0)
- Google Gemini Chat Model → Extract Paginated Resultset (`ai_languageModel`, output 0, input 0)
- Perform Esty Web Request → Extract Paginated Resultset (`main`, output 0, input 0)
- Extract Paginated Resultset → Split Out (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Esty Search Query (`main`, output 0, input 0)
- Perform Esty web request over the loop → Extract Item List with the Product Info (`main`, output 0, input 0)
- Extract Item List with the Product Info → Initiate a Webhook Notification for the extracted data (`main`, output 0, input 0)
- Extract Item List with the Product Info → Create a binary data (`main`, output 0, input 0)
- Google Gemini Chat Model for product info → Extract Item List with the Product Info (`ai_languageModel`, output 0, input 0)
- Initiate a Webhook Notification for the extracted data → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1721_Splitout_Manual_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1721_Splitout_Manual_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
