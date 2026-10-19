# AI Phone Agent with RetellAI

This folder contains the **AI Phone Agent with RetellAI** workflow. Its executable nodes use `agent`, `chainLlm`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `filter`, `googleCalendar`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `outputParserStructured`, `respondToWebhook`, `set`, `telegram`, `textSplitterTokenSplitter`, `toolVectorStore`, `vectorStoreQdrant`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-phone-agent-with-retellai.json`](ai-phone-agent-with-retellai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`, `telegramApi`

**Entry nodes:** n8n_rag_function, n8n_call, n8n_check_available, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter | `filter` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| n8n_rag_function | `webhook` | Inspect parameters |
| Retrive Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| RAG | `toolVectorStore` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Google Calendar | `googleCalendar` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| n8n_call | `webhook` | Inspect parameters |
| n8n_check_available | `webhook` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Create collection | `httpRequest` | POST |
| Refresh collection | `httpRequest` | POST |
| Get folder | `googleDrive` | fileFolder |
| Download Files | `googleDrive` | download |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Set call fields | `set` | Inspect parameters |
| Extract key points | `chainLlm` | Inspect parameters |
| Concert start date | `chainLlm` | Inspect parameters |
| Retrive Agent | `agent` | Inspect parameters |

## Connection map

- RAG → Retrive Agent (`ai_tool`, output 0, input 0)
- Filter → Set call fields (`main`, output 0, input 0)
- n8n_call → Filter (`main`, output 0, input 0)
- Get folder → Download Files (`main`, output 0, input 0)
- Retrive Agent → Respond to Webhook (`main`, output 0, input 0)
- Download Files → Qdrant Vector Store (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Set call fields → Extract key points (`main`, output 0, input 0)
- n8n_rag_function → Retrive Agent (`main`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Extract key points (`ai_languageModel`, output 0, input 0)
- Concert start date → Google Calendar (`main`, output 0, input 0)
- Embeddings OpenAI2 → Retrive Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Extract key points → Telegram (`main`, output 0, input 0)
- OpenAI Chat Model1 → RAG (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Retrive Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Concert start date (`ai_languageModel`, output 0, input 0)
- Refresh collection → Get folder (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- n8n_check_available → Concert start date (`main`, output 0, input 0)
- Structured Output Parser → Extract key points (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → Concert start date (`ai_outputParser`, output 0, input 0)
- Retrive Qdrant Vector Store → RAG (`ai_vectorStore`, output 0, input 0)
- When clicking ‘Test workflow’ → Create collection (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0735_Telegram_GoogleCalendar_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0735_Telegram_GoogleCalendar_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
