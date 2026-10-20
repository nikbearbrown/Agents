# Selenium Ultimate Scraper Workflow

This folder contains the **Selenium Ultimate Scraper Workflow** workflow. Its executable nodes use `code`, `convertToFile`, `html`, `httpRequest`, `if`, `informationExtractor`, `limit`, `lmChatOpenAi`, `openAi`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`selenium-ultimate-scraper-workflow.json`](selenium-ultimate-scraper-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract First Url Match | `html` | extractHtmlContent |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Clean Webdriver  | `httpRequest` | POST |
| Delete Session | `httpRequest` | DELETE |
| Delete Session2 | `httpRequest` | DELETE |
| If Block1 | `if` | Inspect parameters |
| Delete Session3 | `httpRequest` | DELETE |
| Limit | `limit` | Inspect parameters |
| Delete Session1 | `httpRequest` | DELETE |
| Delete Session4 | `httpRequest` | DELETE |
| Success with cookie | `respondToWebhook` | Inspect parameters |
| Respond to Webhook2 | `respondToWebhook` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Delete Session5 | `httpRequest` | DELETE |
| Error | `respondToWebhook` | Inspect parameters |
| Error1 | `respondToWebhook` | Inspect parameters |
| Error2 | `respondToWebhook` | Inspect parameters |
| If | `if` | Inspect parameters |
| Inject Cookie | `httpRequest` | POST |
| Respond to Webhook3 | `respondToWebhook` | Inspect parameters |
| Success | `respondToWebhook` | Inspect parameters |
| Go on url | `httpRequest` | POST |
| Delete Session6 | `httpRequest` | DELETE |
| Error3 | `respondToWebhook` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| Check if empty of NA | `if` | Inspect parameters |
| If Block | `if` | Inspect parameters |
| Google search Query  | `httpRequest` | Inspect parameters |
| Create Selenium Session | `httpRequest` | POST |
| Get ScreenShot 1 | `httpRequest` | Inspect parameters |
| Refresh browser | `httpRequest` | POST |
| Get ScreenShot  | `httpRequest` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Convert to File1 | `convertToFile` | toBinary |
| Delete Session7 | `httpRequest` | DELETE |
| Edit Fields (For testing prupose ) | `set` | Inspect parameters |
| Get ScreenShot 2 | `httpRequest` | Inspect parameters |
| Convert to File2 | `convertToFile` | toBinary |
| Go on ip-api.com | `httpRequest` | POST |
| Delete Session8 | `httpRequest` | DELETE |
| Error can't find url | `respondToWebhook` | Inspect parameters |
| Resize browser window | `httpRequest` | POST |
| OpenAI | `openAi` | image / analyze |
| OpenAI1 | `openAi` | image / analyze |
| Information Extractor1 | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Information Extractor2 | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| If Target Url | `if` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Go on url1 | `httpRequest` | POST |
| If2 | `if` | Inspect parameters |
| Go on url2 | `httpRequest` | POST |
| If3 | `if` | Inspect parameters |
| Go on url3 | `httpRequest` | POST |

## Connection map

- If → If3 (`main`, output 0, input 0)
- If → Delete Session5 (`main`, output 1, input 0)
- If1 → Go on url (`main`, output 0, input 0)
- If1 → Go on url1 (`main`, output 1, input 0)
- If2 → If (`main`, output 0, input 0)
- If2 → If1 (`main`, output 1, input 0)
- If3 → Go on url2 (`main`, output 0, input 0)
- If3 → Go on url3 (`main`, output 1, input 0)
- Code → Inject Cookie (`main`, output 0, input 0)
- Limit → Refresh browser (`main`, output 0, input 0)
- OpenAI → If Block1 (`main`, output 0, input 0)
- OpenAI1 → If Block (`main`, output 0, input 0)
- OpenAI1 → Delete Session6 (`main`, output 1, input 0)
- Webhook → Edit Fields (For testing prupose ) (`main`, output 0, input 0)
- If Block → Delete Session1 (`main`, output 0, input 0)
- If Block → Delete Session (`main`, output 1, input 0)
- Go on url → Get ScreenShot 1 (`main`, output 0, input 0)
- Go on url → Delete Session6 (`main`, output 1, input 0)
- If Block1 → Delete Session2 (`main`, output 0, input 0)
- If Block1 → Delete Session3 (`main`, output 1, input 0)
- Go on url1 → Get ScreenShot 1 (`main`, output 0, input 0)
- Go on url1 → Delete Session6 (`main`, output 1, input 0)
- Go on url2 → Code (`main`, output 0, input 0)
- Go on url2 → Delete Session4 (`main`, output 1, input 0)
- Go on url3 → Code (`main`, output 0, input 0)
- Go on url3 → Delete Session4 (`main`, output 1, input 0)
- If Target Url → Google search Query  (`main`, output 0, input 0)
- If Target Url → Create Selenium Session (`main`, output 1, input 0)
- Inject Cookie → Limit (`main`, output 0, input 0)
- Delete Session → Information Extractor1 (`main`, output 0, input 0)
- Convert to File → OpenAI (`main`, output 0, input 0)
- Convert to File → Delete Session4 (`main`, output 1, input 0)
- Delete Session1 → Respond to Webhook3 (`main`, output 0, input 0)
- Delete Session2 → Respond to Webhook2 (`main`, output 0, input 0)
- Delete Session3 → Information Extractor2 (`main`, output 0, input 0)
- Delete Session4 → Error1 (`main`, output 0, input 0)
- Delete Session5 → Error (`main`, output 0, input 0)
- Delete Session6 → Error3 (`main`, output 0, input 0)
- Delete Session7 → Error2 (`main`, output 0, input 0)
- Get ScreenShot  → Convert to File (`main`, output 0, input 0)
- Get ScreenShot  → Delete Session4 (`main`, output 1, input 0)
- Refresh browser → Get ScreenShot  (`main`, output 0, input 0)
- Refresh browser → Delete Session4 (`main`, output 1, input 0)
- Clean Webdriver  → If2 (`main`, output 0, input 0)
- Convert to File1 → OpenAI1 (`main`, output 0, input 0)
- Convert to File1 → Delete Session6 (`main`, output 1, input 0)
- Get ScreenShot 1 → Convert to File1 (`main`, output 0, input 0)
- Get ScreenShot 1 → Delete Session6 (`main`, output 1, input 0)
- Get ScreenShot 2 → Convert to File2 (`main`, output 0, input 0)
- Get ScreenShot 2 → Delete Session8 (`main`, output 1, input 0)
- Go on ip-api.com → Get ScreenShot 2 (`main`, output 0, input 0)
- Go on ip-api.com → Delete Session8 (`main`, output 1, input 0)
- OpenAI Chat Model → Information Extractor (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Information Extractor1 (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Information Extractor2 (`ai_languageModel`, output 0, input 0)
- Check if empty of NA → Error can't find url (`main`, output 0, input 0)
- Check if empty of NA → Create Selenium Session (`main`, output 1, input 0)
- Google search Query  → Extract First Url Match (`main`, output 0, input 0)
- Information Extractor → Check if empty of NA (`main`, output 0, input 0)
- Resize browser window → Clean Webdriver  (`main`, output 0, input 0)
- Information Extractor1 → Success (`main`, output 0, input 0)
- Information Extractor2 → Success with cookie (`main`, output 0, input 0)
- Create Selenium Session → Resize browser window (`main`, output 0, input 0)
- Create Selenium Session → Delete Session7 (`main`, output 1, input 0)
- Extract First Url Match → Information Extractor (`main`, output 0, input 0)
- Edit Fields (For testing prupose ) → If Target Url (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1900_Limit_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1900_Limit_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
