# My workflow 3

This folder contains the **My workflow 3** workflow. Its executable nodes use `agent`, `aggregate`, `chainRetrievalQa`, `chatTrigger`, `code`, `convertToFile`, `documentDefaultDataLoader`, `embeddingsMistralCloud`, `formTrigger`, `gmail`, `httpRequest`, `if`, `informationExtractor`, `lmChatGoogleGemini`, `markdown`, `retrieverVectorStore`, `splitInBatches`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-form-events-and-aggregate-and-parsing-the-document.json`](receive-form-events-and-aggregate-and-parsing-the-document.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** On form submission4, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission4 | `formTrigger` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| Google Gemini Chat Model5 | `lmChatGoogleGemini` | Inspect parameters |
| split the binary item | `code` | Inspect parameters |
| Parsing the document | `httpRequest` | POST |
| Check the parsing status | `httpRequest` | Inspect parameters |
| Provide the markdown | `httpRequest` | Inspect parameters |
| Google Gemini Chat Model6 | `lmChatGoogleGemini` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| AI Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Convert to File4 | `convertToFile` | toText |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Embeddings Mistral Cloud | `embeddingsMistralCloud` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Pinecone Vector Store1 | `vectorStorePinecone` | Inspect parameters |
| Embeddings Mistral Cloud1 | `embeddingsMistralCloud` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Translator Agent | `agent` | Inspect parameters |
| Analyzer Agent | `agent` | Inspect parameters |

## Connection map

- If2 → Provide the markdown (`main`, output 0, input 0)
- If2 → Check the parsing status (`main`, output 1, input 0)
- Code → Convert to File (`main`, output 0, input 0)
- Markdown → Code (`main`, output 0, input 0)
- Aggregate1 → Translator Agent (`main`, output 0, input 0)
- Analyzer Agent → Markdown (`main`, output 0, input 0)
- Analyzer Agent → AI Agent (`main`, output 0, input 0)
- Analyzer Agent → Information Extractor (`main`, output 0, input 0)
- Analyzer Agent → Convert to File4 (`main`, output 0, input 0)
- Convert to File → Gmail (`main`, output 0, input 0)
- Convert to File4 → Pinecone Vector Store (`main`, output 0, input 0)
- Loop Over Items1 → Aggregate1 (`main`, output 0, input 0)
- Loop Over Items1 → Parsing the document (`main`, output 1, input 0)
- Translator Agent → Analyzer Agent (`main`, output 0, input 0)
- Translator Agent → Convert to File4 (`main`, output 0, input 0)
- Default Data Loader → Pinecone Vector Store (`ai_document`, output 0, input 0)
- On form submission4 → split the binary item (`main`, output 0, input 0)
- Parsing the document → Check the parsing status (`main`, output 0, input 0)
- Provide the markdown → Loop Over Items1 (`main`, output 0, input 0)
- split the binary item → Loop Over Items1 (`main`, output 0, input 0)
- Pinecone Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Question and Answer Chain (`ai_retriever`, output 0, input 0)
- Check the parsing status → If2 (`main`, output 0, input 0)
- Embeddings Mistral Cloud → Pinecone Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Embeddings Mistral Cloud1 → Pinecone Vector Store1 (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model1 → Information Extractor (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Question and Answer Chain (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model3 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model5 → Translator Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model6 → Analyzer Agent (`ai_languageModel`, output 0, input 0)
- Question and Answer Chain → AI Agent1 (`main`, output 0, input 0)
- When chat message received → Question and Answer Chain (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1818_Code_Converttofile_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1818_Code_Converttofile_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
