# Tech Radar

This folder contains the **Tech Radar** workflow. Its executable nodes use `agent`, `chainLlm`, `code`, `cron`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `executeWorkflow`, `executeWorkflowTrigger`, `googleDocs`, `googleDrive`, `googleDriveTrigger`, `googleSheets`, `if`, `lmChatAnthropic`, `lmChatGoogleGemini`, `lmChatGroq`, `memoryBufferWindow`, `mySql`, `mySqlTool`, `respondToWebhook`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStorePinecone`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`tech-radar.json`](tech-radar.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `googleApi`, `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `groqApi`, `mySql`, `pineconeApi`

**Entry nodes:** Cron, Google Drive - Doc File Updated, When Executed by Another Workflow, API Request - Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Download Doc File From Google Drive | `googleDrive` | download |
| Doc File Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| MySQL -delete all data | `mySql` | deleteTable |
| MySQL - insert all from sheets | `mySql` | Inspect parameters |
| Google Sheets - Tech Radar | `googleSheets` | Inspect parameters |
| Code - Transform table into rows | `code` | Inspect parameters |
| Google Docs - Update GDoc | `googleDocs` | update |
| Google Drive - Doc File Updated | `googleDriveTrigger` | Inspect parameters |
| Content - Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Google Sheets - Read TechRadar | `googleSheets` | Inspect parameters |
| Code - Simplify Mapping to Original Query | `code` | Inspect parameters |
| Codes - Simplify Mapping to Original Query | `code` | Inspect parameters |
| Execute Workflow - Sql Agent | `executeWorkflow` | Inspect parameters |
| Execute Workflow - RAG Agent | `executeWorkflow` | Inspect parameters |
| AI Agent - Output Guardrail | `agent` | Inspect parameters |
| LLM - Determine - Agent Input Router | `chainLlm` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| 1_Get DB Schema and Tables List | `mySqlTool` | executeQuery |
| 2_Get Table Definition | `mySqlTool` | executeQuery |
| 3_Execute actual query | `mySqlTool` | executeQuery |
| AI Agent -DB Sql Agent | `agent` | Inspect parameters |
| Pinecone Vector Store (Retrieval) | `vectorStorePinecone` | Inspect parameters |
| 4_RagTool | `toolVectorStore` | Inspect parameters |
| AI Agent - RAG | `agent` | Inspect parameters |
| Embeddings - Tech Radar Data Embedding | `embeddingsGoogleGemini` | Inspect parameters |
| Pinecone - Vector Store for Embedding Content | `vectorStorePinecone` | Inspect parameters |
| Retrieve Embeddings - Tech Radar Vector DB | `embeddingsGoogleGemini` | Inspect parameters |
| AI Agent - Retrieval | `lmChatGoogleGemini` | Inspect parameters |
| AI Chat Model - Claude 3.5 Sonnet | `lmChatAnthropic` | Inspect parameters |
| AI Chat Model - QwQ 32b | `lmChatGroq` | Inspect parameters |
| AI Chatmodel - Deepseek 32B | `lmChatGroq` | Inspect parameters |
| AI Chat Model - llama3-8b | `lmChatGroq` | Inspect parameters |
| API Response - Respond to Webhook | `respondToWebhook` | Inspect parameters |
| API Request - Webhook | `webhook` | Inspect parameters |
| Determine if  is 'RAG' | `if` | Inspect parameters |
| User Conversation history | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Cron → MySQL -delete all data (`main`, output 0, input 0)
- 4_RagTool → AI Agent - RAG (`ai_tool`, output 0, input 0)
- AI Agent - Retrieval → 4_RagTool (`ai_languageModel`, output 0, input 0)
- Doc File Data Loader → Pinecone - Vector Store for Embedding Content (`ai_document`, output 0, input 0)
- API Request - Webhook → LLM - Determine - Agent Input Router (`main`, output 0, input 0)
- 2_Get Table Definition → AI Agent -DB Sql Agent (`ai_tool`, output 0, input 0)
- 3_Execute actual query → AI Agent -DB Sql Agent (`ai_tool`, output 0, input 0)
- Determine if  is 'RAG' → Code - Simplify Mapping to Original Query (`main`, output 0, input 0)
- Determine if  is 'RAG' → Codes - Simplify Mapping to Original Query (`main`, output 1, input 0)
- MySQL -delete all data → Google Sheets - Read TechRadar (`main`, output 0, input 0)
- AI Chat Model - QwQ 32b → AI Agent - RAG (`ai_languageModel`, output 0, input 0)
- AI Chat Model - llama3-8b → AI Agent - Output Guardrail (`ai_languageModel`, output 0, input 0)
- User Conversation history → AI Agent - Output Guardrail (`ai_memory`, output 0, input 0)
- Google Sheets - Tech Radar → Code - Transform table into rows (`main`, output 0, input 0)
- AI Agent - Output Guardrail → API Response - Respond to Webhook (`main`, output 0, input 0)
- AI Chatmodel - Deepseek 32B → LLM - Determine - Agent Input Router (`ai_languageModel`, output 0, input 0)
- Execute Workflow - RAG Agent → AI Agent - Output Guardrail (`main`, output 0, input 0)
- Execute Workflow - Sql Agent → AI Agent - Output Guardrail (`main`, output 0, input 0)
- Google Sheets - Read TechRadar → MySQL - insert all from sheets (`main`, output 0, input 0)
- 1_Get DB Schema and Tables List → AI Agent -DB Sql Agent (`ai_tool`, output 0, input 0)
- Google Drive - Doc File Updated → Download Doc File From Google Drive (`main`, output 0, input 0)
- Code - Transform table into rows → Google Docs - Update GDoc (`main`, output 0, input 0)
- AI Chat Model - Claude 3.5 Sonnet → AI Agent -DB Sql Agent (`ai_languageModel`, output 0, input 0)
- Pinecone Vector Store (Retrieval) → 4_RagTool (`ai_vectorStore`, output 0, input 0)
- When Executed by Another Workflow → AI Agent -DB Sql Agent (`main`, output 0, input 0)
- Download Doc File From Google Drive → Pinecone - Vector Store for Embedding Content (`main`, output 0, input 0)
- LLM - Determine - Agent Input Router → Determine if  is 'RAG' (`main`, output 0, input 0)
- Embeddings - Tech Radar Data Embedding → Pinecone - Vector Store for Embedding Content (`ai_embedding`, output 0, input 0)
- Code - Simplify Mapping to Original Query → Execute Workflow - RAG Agent (`main`, output 0, input 0)
- Codes - Simplify Mapping to Original Query → Execute Workflow - Sql Agent (`main`, output 0, input 0)
- Retrieve Embeddings - Tech Radar Vector DB → Pinecone Vector Store (Retrieval) (`ai_embedding`, output 0, input 0)
- Content - Recursive Character Text Splitter → Doc File Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1836_Code_Googledocs_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1836_Code_Googledocs_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
