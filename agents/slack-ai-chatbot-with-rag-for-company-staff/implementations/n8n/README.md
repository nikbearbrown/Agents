# Slack AI Chatbot with RAG for company staff

This folder contains the **Slack AI Chatbot with RAG for company staff** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `googleDrive`, `httpRequest`, `lmChatAnthropic`, `manualTrigger`, `memoryBufferWindow`, `slack`, `slackTrigger`, `textSplitterTokenSplitter`, `toolCalculator`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`slack-ai-chatbot-with-rag-for-company-staff.json`](slack-ai-chatbot-with-rag-for-company-staff.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `qdrantApi`, `slackApi`

**Entry nodes:** Get message, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| RAG | `vectorStoreQdrant` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Get message | `slackTrigger` | Inspect parameters |
| Send message | `slack` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Create collection | `httpRequest` | POST |
| Refresh collection | `httpRequest` | POST |
| Get folder | `googleDrive` | fileFolder |
| Download Files | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |

## Connection map

- RAG → AI Agent (`ai_tool`, output 0, input 0)
- AI Agent → Send message (`main`, output 0, input 0)
- Calculator → AI Agent (`ai_tool`, output 0, input 0)
- Get folder → Download Files (`main`, output 0, input 0)
- Get message → AI Agent (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Download Files → Qdrant Vector Store1 (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Embeddings OpenAI1 → RAG (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Refresh collection → Get folder (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store1 (`ai_document`, output 0, input 0)
- Anthropic Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Create collection (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/1643_Slack_Manual_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/1643_Slack_Manual_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
