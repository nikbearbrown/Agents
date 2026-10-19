# Personal Portfolio Resume CV Chatbot

This folder contains the **Personal Portfolio Resume CV Chatbot** workflow. Its executable nodes use `agent`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `gmail`, `googleDrive`, `googleDriveTrigger`, `html`, `lmChatGoogleGemini`, `memoryBufferWindow`, `nocoDb`, `respondToWebhook`, `scheduleTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStorePinecone`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`personal-portfolio-resume-cv-chatbot.json`](personal-portfolio-resume-cv-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googlePalmApi`, `nocoDbApiToken`, `pineconeApi`

**Entry nodes:** Schedule Trigger, Google Drive - Resume CV File Created, Google Drive - Resume CV File Updated, Chat API - webhook, Save Conversation API - Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Drive - Resume CV File Created | `googleDriveTrigger` | Inspect parameters |
| Google Drive - Resume CV File Updated | `googleDriveTrigger` | Inspect parameters |
| Download CV File From Google Drive | `googleDrive` | download |
| Pinecone - Vector Store forr CV Content | `vectorStorePinecone` | Inspect parameters |
| CV File Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| CV content - Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Chat API - webhook | `webhook` | Inspect parameters |
| Personal CV AI Agent Assistant | `agent` | Inspect parameters |
| Chat API Response - Webhook | `respondToWebhook` | Inspect parameters |
| Chat Memory -  Window Buffer | `memoryBufferWindow` | Inspect parameters |
| Resume lookup : Vector Store Tool | `toolVectorStore` | Inspect parameters |
| Resume Vector Store (Retrieval) | `vectorStorePinecone` | Inspect parameters |
| Resume Embeddings Google Gemini (retrieval) | `embeddingsGoogleGemini` | Inspect parameters |
| Resume Google Gemini Chat Model (retrieval) | `lmChatGoogleGemini` | Inspect parameters |
| Save Conversation API - Webhook | `webhook` | Inspect parameters |
| Save Conversation - NocoDB | `nocoDb` | create |
| Save Conversation API Webhook - Response | `respondToWebhook` | Inspect parameters |
| NocoDB - get all todays conversation | `nocoDb` | getAll |
| Group Conversation By Unique Session + Email - Code | `code` | Inspect parameters |
| Format HTML Display  For email | `html` | Inspect parameters |
| Send Report To Gmail | `gmail` | Inspect parameters |

## Connection map

- Schedule Trigger → NocoDB - get all todays conversation (`main`, output 0, input 0)
- Chat API - webhook → Personal CV AI Agent Assistant (`main`, output 0, input 0)
- CV File Data Loader → Pinecone - Vector Store forr CV Content (`ai_document`, output 0, input 0)
- Embeddings Google Gemini → Pinecone - Vector Store forr CV Content (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → Personal CV AI Agent Assistant (`ai_languageModel`, output 0, input 0)
- Save Conversation - NocoDB → Save Conversation API Webhook - Response (`main`, output 0, input 0)
- Chat Memory -  Window Buffer → Personal CV AI Agent Assistant (`ai_memory`, output 0, input 0)
- Format HTML Display  For email → Send Report To Gmail (`main`, output 0, input 0)
- Personal CV AI Agent Assistant → Chat API Response - Webhook (`main`, output 0, input 0)
- Resume Vector Store (Retrieval) → Resume lookup : Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Save Conversation API - Webhook → Save Conversation - NocoDB (`main`, output 0, input 0)
- Resume lookup : Vector Store Tool → Personal CV AI Agent Assistant (`ai_tool`, output 0, input 0)
- Download CV File From Google Drive → Pinecone - Vector Store forr CV Content (`main`, output 0, input 0)
- NocoDB - get all todays conversation → Group Conversation By Unique Session + Email - Code (`main`, output 0, input 0)
- Google Drive - Resume CV File Created → Download CV File From Google Drive (`main`, output 0, input 0)
- Google Drive - Resume CV File Updated → Download CV File From Google Drive (`main`, output 0, input 0)
- Resume Embeddings Google Gemini (retrieval) → Resume Vector Store (Retrieval) (`ai_embedding`, output 0, input 0)
- Resume Google Gemini Chat Model (retrieval) → Resume lookup : Vector Store Tool (`ai_languageModel`, output 0, input 0)
- CV content - Recursive Character Text Splitter → CV File Data Loader (`ai_textSplitter`, output 0, input 0)
- Group Conversation By Unique Session + Email - Code → Format HTML Display  For email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1881_Webhook_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1881_Webhook_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
