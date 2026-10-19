# sort and split pdf into images and extract zip file

This folder contains the **sort and split pdf into images and extract zip file** workflow. Its executable nodes use `agent`, `aggregate`, `airtable`, `airtableTool`, `airtableTrigger`, `chainLlm`, `chatTrigger`, `code`, `compression`, `convertToFile`, `documentDefaultDataLoader`, `editImage`, `embeddingsOpenAi`, `executeWorkflow`, `executeWorkflowTrigger`, `extractFromFile`, `httpRequest`, `if`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `merge`, `noOp`, `set`, `sort`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sort-and-split-pdf-into-images-and-extract-zip-file.json`](sort-and-split-pdf-into-images-and-extract-zip-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger, Airtable Trigger For Pending Rows, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Sort Pages | `sort` | Inspect parameters |
| Split PDF into Images | `httpRequest` | POST |
| Extract Zip File | `compression` | Inspect parameters |
| Images To List | `code` | Inspect parameters |
| Resize Images For AI | `editImage` | resize |
| Combine All Pages | `aggregate` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Delete Existing Vectors | `httpRequest` | POST |
| Continue With Pages Only | `merge` | Inspect parameters |
| Update Pitchdecks Table | `airtable` | upsert |
| Search Pending Rows | `airtable` | search |
| Get Row | `set` | Inspect parameters |
| Prequisites Met | `if` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Extract from File | `extractFromFile` | binaryToPropery |
| Convert to File | `convertToFile` | toBinary |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Vector Store Tool | `toolVectorStore` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model4 | `lmChatOpenAi` | Inspect parameters |
| Generate Report | `informationExtractor` | Inspect parameters |
| Download Deck From Airtable | `httpRequest` | Inspect parameters |
| Airtable Trigger For Pending Rows | `airtableTrigger` | Inspect parameters |
| Transcribe to Markdown | `chainLlm` | Inspect parameters |
| Identify Companies In Question | `informationExtractor` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Ask Questions About Pitchdecks | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Check Pitch Deck Exists | `airtableTool` | search |
| When chat message received | `chatTrigger` | Inspect parameters |
| Pitchdecks Vector Store | `vectorStoreQdrant` | Inspect parameters |

## Connection map

- Get Row → Prequisites Met (`main`, output 0, input 0)
- Sort Pages → Resize Images For AI (`main`, output 0, input 0)
- Images To List → Sort Pages (`main`, output 0, input 0)
- Convert to File → Split PDF into Images (`main`, output 0, input 0)
- Generate Report → Update Pitchdecks Table (`main`, output 0, input 0)
- Prequisites Met → Execute Workflow (`main`, output 0, input 0)
- Prequisites Met → No Operation, do nothing (`main`, output 1, input 0)
- Extract Zip File → Images To List (`main`, output 0, input 0)
- Combine All Pages → Generate Report (`main`, output 0, input 0)
- Embeddings OpenAI → Pitchdecks Vector Store (`ai_embedding`, output 0, input 0)
- Extract from File → Convert to File (`main`, output 0, input 0)
- OpenAI Chat Model → Ask Questions About Pitchdecks (`ai_languageModel`, output 0, input 0)
- Vector Store Tool → Ask Questions About Pitchdecks (`ai_tool`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → Identify Companies In Question (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Generate Report (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Vector Store Tool (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model4 → Transcribe to Markdown (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Pitchdecks Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store → Vector Store Tool (`ai_vectorStore`, output 0, input 0)
- Search Pending Rows → Get Row (`main`, output 0, input 0)
- Resize Images For AI → Transcribe to Markdown (`main`, output 0, input 0)
- Window Buffer Memory → Ask Questions About Pitchdecks (`ai_memory`, output 0, input 0)
- Split PDF into Images → Extract Zip File (`main`, output 0, input 0)
- Transcribe to Markdown → Combine All Pages (`main`, output 0, input 0)
- Transcribe to Markdown → Continue With Pages Only (`main`, output 0, input 0)
- Transcribe to Markdown → Delete Existing Vectors (`main`, output 0, input 0)
- Check Pitch Deck Exists → Ask Questions About Pitchdecks (`ai_tool`, output 0, input 0)
- Delete Existing Vectors → Continue With Pages Only (`main`, output 0, input 1)
- Continue With Pages Only → Pitchdecks Vector Store (`main`, output 0, input 0)
- Execute Workflow Trigger → Download Deck From Airtable (`main`, output 0, input 0)
- When chat message received → Identify Companies In Question (`main`, output 0, input 0)
- Download Deck From Airtable → Extract from File (`main`, output 0, input 0)
- Identify Companies In Question → Ask Questions About Pitchdecks (`main`, output 0, input 0)
- Airtable Trigger For Pending Rows → Get Row (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Search Pending Rows (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0600_Code_Extractfromfile_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0600_Code_Extractfromfile_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
