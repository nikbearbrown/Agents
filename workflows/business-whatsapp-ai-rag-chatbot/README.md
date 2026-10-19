# Business WhatsApp AI RAG Chatbot

This folder contains the **Business WhatsApp AI RAG Chatbot** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `respondToWebhook`, `textSplitterTokenSplitter`, `vectorStoreQdrant`, `webhook`, `whatsApp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`business-whatsapp-ai-rag-chatbot.json`](business-whatsapp-ai-rag-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`, `whatsAppApi`

**Entry nodes:** When clicking ‘Test workflow’, Verify, Respond

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Create collection | `httpRequest` | POST |
| Refresh collection | `httpRequest` | POST |
| Get folder | `googleDrive` | fileFolder |
| Download Files | `googleDrive` | download |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Verify | `webhook` | Inspect parameters |
| Respond | `webhook` | Inspect parameters |
| is Message? | `if` | Inspect parameters |
| Only message | `whatsApp` | send |
| Send | `whatsApp` | send |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Verify → Respond to Webhook (`main`, output 0, input 0)
- Respond → is Message? (`main`, output 0, input 0)
- AI Agent → Send (`main`, output 0, input 0)
- Get folder → Download Files (`main`, output 0, input 0)
- is Message? → AI Agent (`main`, output 0, input 0)
- is Message? → Only message (`main`, output 1, input 0)
- Download Files → Qdrant Vector Store (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Refresh collection → Get folder (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- When clicking ‘Test workflow’ → Create collection (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1385_Webhook_Respondtowebhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1385_Webhook_Respondtowebhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
