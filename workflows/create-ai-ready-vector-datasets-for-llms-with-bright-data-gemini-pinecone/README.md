# Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini & Pinecone

This folder contains the **Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini & Pinecone** workflow. Its executable nodes use `agent`, `chainLlm`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `outputParserStructured`, `set`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-ai-ready-vector-datasets-for-llms-with-bright-data-gemini-pinecone.json`](create-ai-ready-vector-datasets-for-llms-with-bright-data-gemini-pinecone.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpHeaderAuth`, `pineconeApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Set Fields - URL and Webhook URL | `set` | Inspect parameters |
| Make a web request | `httpRequest` | POST |
| Structured JSON Data Formatter | `chainLlm` | Inspect parameters |
| Webhook for structured data | `httpRequest` | Inspect parameters |
| Webhook for structured AI agent response | `httpRequest` | Inspect parameters |
| Information Extractor with Data Formatter | `informationExtractor` | Inspect parameters |

## Connection map

- AI Agent → Pinecone Vector Store (`main`, output 0, input 0)
- AI Agent → Webhook for structured AI agent response (`main`, output 0, input 0)
- Make a web request → Structured JSON Data Formatter (`main`, output 0, input 0)
- Make a web request → Information Extractor with Data Formatter (`main`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- Embeddings Google Gemini → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → Information Extractor with Data Formatter (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Google Gemini Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Structured JSON Data Formatter (`ai_languageModel`, output 0, input 0)
- Structured JSON Data Formatter → Webhook for structured data (`main`, output 0, input 0)
- Set Fields - URL and Webhook URL → Make a web request (`main`, output 0, input 0)
- Set Fields - URL and Webhook URL → Webhook for structured data (`main`, output 0, input 0)
- Set Fields - URL and Webhook URL → Webhook for structured AI agent response (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Fields - URL and Webhook URL (`main`, output 0, input 0)
- Information Extractor with Data Formatter → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0933_Manual_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0933_Manual_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
