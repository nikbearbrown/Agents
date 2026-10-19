# Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion

This folder contains the **Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion** workflow. Its executable nodes use `agent`, `aggregate`, `chainLlm`, `code`, `filter`, `httpRequest`, `lmChatGoogleGemini`, `lmChatOpenRouter`, `markdown`, `memoryBufferWindow`, `notion`, `openAi`, `outputParserStructured`, `respondToWebhook`, `set`, `splitInBatches`, `splitOut`, `switch`, `telegramTrigger`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`deep-research-report-generation-using-open-router-google-search-webhook-telegram-and-notion.json`](deep-research-report-generation-using-open-router-google-search-webhook-telegram-and-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Telegram Trigger, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Strategy Agent | `agent` | Inspect parameters |
| Search Query Agent | `agent` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Loop Over Queries | `splitInBatches` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Edit Fields | `set` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| HTTP Request1 | `httpRequest` | POST |
| Aggregate | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI1 | `openAi` | Inspect parameters |
| Notion | `notion` | databasePage |
| Notion1 | `notion` | databasePage / update |
| HTTP Request2 | `httpRequest` | PATCH |
| Convert to HTML | `markdown` | Inspect parameters |
| HTML to Array | `set` | Inspect parameters |
| Tags to Items | `splitOut` | Inspect parameters |
| Notion Block Generator | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Parse JSON blocks | `set` | Inspect parameters |
| Valid Blocks | `filter` | Inspect parameters |
| For Each Block... | `splitInBatches` | Inspect parameters |
| Get Existing Row | `notion` | databasePage / getAll |
| Code | `code` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model1 | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model2 | `lmChatOpenRouter` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Respond to Webhook1 | `respondToWebhook` | Inspect parameters |
| HTTP Request3 | `httpRequest` | POST |

## Connection map

- Simple Memory → Strategy Agent (`ai_memory`, output 0, input 0)
- Structured Output Parser → Strategy Agent (`ai_outputParser`, output 0, input 0)
- Switch → Respond to Webhook (`main`, output 0, input 0)
- Switch → Respond to Webhook1 (`main`, output 1, input 0)
- Strategy Agent → Switch (`main`, output 0, input 0)
- Structured Output Parser1 → Search Query Agent (`ai_outputParser`, output 0, input 0)
- Search Query Agent → Split Out (`main`, output 0, input 0)
- Split Out → Loop Over Queries (`main`, output 0, input 0)
- Loop Over Queries → Aggregate (`main`, output 0, input 0)
- Loop Over Queries → HTTP Request (`main`, output 1, input 0)
- HTTP Request → Edit Fields (`main`, output 0, input 0)
- Edit Fields → OpenAI (`main`, output 0, input 0)
- OpenAI → HTTP Request1 (`main`, output 0, input 0)
- HTTP Request1 → Loop Over Queries (`main`, output 0, input 0)
- Aggregate → AI Agent (`main`, output 0, input 0)
- AI Agent → Get Existing Row (`main`, output 0, input 0)
- OpenAI1 → Notion (`main`, output 0, input 0)
- Notion1 → HTTP Request3 (`main`, output 0, input 0)
- Convert to HTML → HTML to Array (`main`, output 0, input 0)
- HTML to Array → Tags to Items (`main`, output 0, input 0)
- Tags to Items → Notion Block Generator (`main`, output 0, input 0)
- Google Gemini Chat Model → Notion Block Generator (`ai_languageModel`, output 0, input 0)
- Notion Block Generator → Parse JSON blocks (`main`, output 0, input 0)
- Parse JSON blocks → Valid Blocks (`main`, output 0, input 0)
- Valid Blocks → For Each Block... (`main`, output 0, input 0)
- For Each Block... → Aggregate1 (`main`, output 0, input 0)
- For Each Block... → HTTP Request2 (`main`, output 1, input 0)
- HTTP Request2 → For Each Block... (`main`, output 0, input 0)
- Get Existing Row → Convert to HTML (`main`, output 0, input 0)
- Code → OpenAI1 (`main`, output 0, input 0)
- Aggregate1 → Notion1 (`main`, output 0, input 0)
- Notion → Search Query Agent (`main`, output 0, input 0)
- OpenRouter Chat Model → Strategy Agent (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model1 → Search Query Agent (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model2 → AI Agent (`ai_languageModel`, output 0, input 0)
- Webhook → Strategy Agent (`main`, output 0, input 0)
- Respond to Webhook1 → Code (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/2054_Deep_Research_Report_Generation_With_Open_Router_Google_Search_Webhook_Telegram_and_Notion.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/2054_Deep_Research_Report_Generation_With_Open_Router_Google_Search_Webhook_Telegram_and_Notion.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
