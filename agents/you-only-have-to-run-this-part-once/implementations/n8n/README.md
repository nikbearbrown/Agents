# You only have to run this part once!

This folder contains the **You only have to run this part once!** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStoreInMemory`, `whatsApp`, `whatsAppTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`you-only-have-to-run-this-part-once.json`](you-only-have-to-run-this-part-once.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `whatsAppApi`, `whatsAppTriggerApi`

**Entry nodes:** WhatsApp Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| WhatsApp Trigger | `whatsAppTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Vector Store Tool | `toolVectorStore` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| get Product Brochure | `httpRequest` | Inspect parameters |
| Reply To User | `whatsApp` | send |
| Reply To User1 | `whatsApp` | send |
| Product Catalogue | `vectorStoreInMemory` | Inspect parameters |
| Create Product Catalogue | `vectorStoreInMemory` | Inspect parameters |
| Handle Message Types | `switch` | Inspect parameters |
| AI Sales Agent | `agent` | Inspect parameters |

## Connection map

- AI Sales Agent → Reply To User (`main`, output 0, input 0)
- WhatsApp Trigger → Handle Message Types (`main`, output 0, input 0)
- Embeddings OpenAI → Product Catalogue (`ai_embedding`, output 0, input 0)
- Extract from File → Create Product Catalogue (`main`, output 0, input 0)
- OpenAI Chat Model → AI Sales Agent (`ai_languageModel`, output 0, input 0)
- Product Catalogue → Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Vector Store Tool → AI Sales Agent (`ai_tool`, output 0, input 0)
- Embeddings OpenAI1 → Create Product Catalogue (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → Vector Store Tool (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Create Product Catalogue (`ai_document`, output 0, input 0)
- Handle Message Types → AI Sales Agent (`main`, output 0, input 0)
- Handle Message Types → Reply To User1 (`main`, output 1, input 0)
- Window Buffer Memory → AI Sales Agent (`ai_memory`, output 0, input 0)
- get Product Brochure → Extract from File (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → get Product Brochure (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1365_Extractfromfile_Manual_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1365_Extractfromfile_Manual_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
