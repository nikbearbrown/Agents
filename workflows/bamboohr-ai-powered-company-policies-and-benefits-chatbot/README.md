# BambooHR AI-Powered Company Policies and Benefits Chatbot

This folder contains the **BambooHR AI-Powered Company Policies and Benefits Chatbot** workflow. Its executable nodes use `agent`, `aggregate`, `bambooHr`, `chainLlm`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflowTrigger`, `filter`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `outputParserAutofixing`, `outputParserStructured`, `set`, `splitOut`, `textClassifier`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `toolWorkflow`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`bamboohr-ai-powered-company-policies-and-benefits-chatbot.json`](bamboohr-ai-powered-company-policies-and-benefits-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `bambooHrApi`, `openAiApi`, `supabaseApi`

**Entry nodes:** When clicking ‘Test workflow’, Employee initiates a conversation, AI-Powered HR Benefits and Company Policies Chatbot

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Vector Store Tool | `toolVectorStore` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Employee Lookup Tool | `toolWorkflow` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model4 | `lmChatOpenAi` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| OpenAI Chat Model5 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| GET all files | `bambooHr` | file / getAll |
| Filter out files from undesired categories | `filter` | Inspect parameters |
| Split out individual files | `splitOut` | Inspect parameters |
| Filter out non-pdf files | `filter` | Inspect parameters |
| Download file from BambooHR | `bambooHr` | file / download |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Employee initiates a conversation | `chatTrigger` | Inspect parameters |
| Supabase Vector Store Retrieval | `vectorStoreSupabase` | Inspect parameters |
| AI-Powered HR Benefits and Company Policies Chatbot | `executeWorkflowTrigger` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| GET all employees | `bambooHr` | getAll |
| Filter out other employees | `filter` | Inspect parameters |
| Stringify employee record for response | `set` | Inspect parameters |
| GET all employees (second path) | `bambooHr` | getAll |
| Extract departments | `aggregate` | Inspect parameters |
| Ensure uniqueness in department list | `set` | Inspect parameters |
| Extract department | `informationExtractor` | Inspect parameters |
| Retrieve all employees | `bambooHr` | getAll |
| Filter out other departments | `filter` | Inspect parameters |
| Extract relevant employee fields | `aggregate` | Inspect parameters |
| Identify most senior employee | `chainLlm` | Inspect parameters |
| Format name for response | `set` | Inspect parameters |
| HR AI Agent | `agent` | Inspect parameters |

## Connection map

- GET all files → Filter out files from undesired categories (`main`, output 0, input 0)
- Text Classifier → GET all employees (`main`, output 0, input 0)
- Text Classifier → GET all employees (second path) (`main`, output 1, input 0)
- Embeddings OpenAI → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- GET all employees → Filter out other employees (`main`, output 0, input 0)
- OpenAI Chat Model → HR AI Agent (`ai_languageModel`, output 0, input 0)
- Vector Store Tool → HR AI Agent (`ai_tool`, output 0, input 0)
- Embeddings OpenAI1 → Supabase Vector Store Retrieval (`ai_embedding`, output 0, input 0)
- Extract department → Retrieve all employees (`main`, output 0, input 0)
- OpenAI Chat Model1 → Vector Store Tool (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Text Classifier (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Extract department (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model4 → Identify most senior employee (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model5 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Supabase Vector Store (`ai_document`, output 0, input 0)
- Extract departments → Ensure uniqueness in department list (`main`, output 0, input 0)
- Employee Lookup Tool → HR AI Agent (`ai_tool`, output 0, input 0)
- Window Buffer Memory → HR AI Agent (`ai_memory`, output 0, input 0)
- Retrieve all employees → Filter out other departments (`main`, output 0, input 0)
- Filter out non-pdf files → Download file from BambooHR (`main`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Identify most senior employee (`ai_outputParser`, output 0, input 0)
- Filter out other employees → Stringify employee record for response (`main`, output 0, input 0)
- Split out individual files → Filter out non-pdf files (`main`, output 0, input 0)
- Download file from BambooHR → Supabase Vector Store (`main`, output 0, input 0)
- Filter out other departments → Extract relevant employee fields (`main`, output 0, input 0)
- Identify most senior employee → Format name for response (`main`, output 0, input 0)
- GET all employees (second path) → Extract departments (`main`, output 0, input 0)
- Supabase Vector Store Retrieval → Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Extract relevant employee fields → Identify most senior employee (`main`, output 0, input 0)
- Employee initiates a conversation → HR AI Agent (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → GET all files (`main`, output 0, input 0)
- Ensure uniqueness in department list → Extract department (`main`, output 0, input 0)
- Filter out files from undesired categories → Split out individual files (`main`, output 0, input 0)
- AI-Powered HR Benefits and Company Policies Chatbot → Text Classifier (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1352_Splitout_Filter_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1352_Splitout_Filter_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
