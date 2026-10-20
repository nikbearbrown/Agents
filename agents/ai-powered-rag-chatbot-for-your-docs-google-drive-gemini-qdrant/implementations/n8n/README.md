# 🤖 AI Powered RAG Chatbot for Your Docs + Google Drive + Gemini + Qdrant

This folder contains the **🤖 AI Powered RAG Chatbot for Your Docs + Google Drive + Gemini + Qdrant** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `googleDocs`, `googleDrive`, `if`, `informationExtractor`, `lmChatGoogleGemini`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `merge`, `set`, `splitInBatches`, `summarize`, `telegram`, `textSplitterTokenSplitter`, `vectorStoreQdrant`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-rag-chatbot-for-your-docs-google-drive-gemini-qdrant.json`](ai-powered-rag-chatbot-for-your-docs-google-drive-gemini-qdrant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `googleDriveOAuth2Api`, `googlePalmApi`, `openAiApi`, `qdrantApi`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Webhook, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Extract Meta Data | `informationExtractor` | Inspect parameters |
| Get File Contents | `extractFromFile` | text |
| Download File From Google Drive | `googleDrive` | download |
| Find File Ids in Google Drive Folder | `googleDrive` | fileFolder |
| text-embeddings-3-large | `embeddingsOpenAi` | Inspect parameters |
| Google Folder ID | `set` | Inspect parameters |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| Delete Qdrant Points by File ID | `code` | Inspect parameters |
| Qdrant Collection Name | `set` | Inspect parameters |
| File Id List | `summarize` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Confirm Qdrant Delete Points | `telegram` | sendAndWait |
| If | `if` | Inspect parameters |
| Send Declined Message | `telegram` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| text-embeddings-3-large1 | `embeddingsOpenAi` | Inspect parameters |
| Google Drive | `googleDrive` | createFromText |
| Respond to User | `set` | Inspect parameters |
| Update Chat History | `googleDocs` | update |
| Qdrant Vector Store Tool | `vectorStoreQdrant` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Send Completed Message | `telegram` | Inspect parameters |

## Connection map

- If → Delete Qdrant Points by File ID (`main`, output 0, input 0)
- If → Send Declined Message (`main`, output 1, input 0)
- Wait → Loop Over Items (`main`, output 0, input 0)
- Merge → Qdrant Vector Store (`main`, output 0, input 0)
- Merge1 → Confirm Qdrant Delete Points (`main`, output 0, input 0)
- Merge2 → Loop Over Items (`main`, output 0, input 0)
- Webhook → Google Folder ID (`main`, output 0, input 0)
- AI Agent → Update Chat History (`main`, output 0, input 0)
- AI Agent → Respond to User (`main`, output 0, input 0)
- Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- File Id List → Merge1 (`main`, output 0, input 1)
- gpt-4o-mini1 → Delete Qdrant Points by File ID (`ai_languageModel`, output 0, input 0)
- Token Splitter → Data Loader (`ai_textSplitter`, output 0, input 0)
- Loop Over Items → Send Completed Message (`main`, output 0, input 0)
- Loop Over Items → Download File From Google Drive (`main`, output 1, input 0)
- Google Folder ID → Find File Ids in Google Drive Folder (`main`, output 0, input 0)
- Extract Meta Data → Merge (`main`, output 0, input 0)
- Get File Contents → Extract Meta Data (`main`, output 0, input 0)
- Qdrant Vector Store → Wait (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Qdrant Collection Name → Merge1 (`main`, output 0, input 0)
- text-embeddings-3-large → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → Extract Meta Data (`ai_languageModel`, output 0, input 0)
- Qdrant Vector Store Tool → AI Agent (`ai_tool`, output 0, input 0)
- text-embeddings-3-large1 → Qdrant Vector Store Tool (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Confirm Qdrant Delete Points → If (`main`, output 0, input 0)
- Delete Qdrant Points by File ID → Merge2 (`main`, output 0, input 1)
- Download File From Google Drive → Get File Contents (`main`, output 0, input 0)
- Download File From Google Drive → Merge (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Google Folder ID (`main`, output 0, input 0)
- Find File Ids in Google Drive Folder → File Id List (`main`, output 0, input 0)
- Find File Ids in Google Drive Folder → Qdrant Collection Name (`main`, output 0, input 0)
- Find File Ids in Google Drive Folder → Merge2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1185_Telegram_Wait_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1185_Telegram_Wait_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
