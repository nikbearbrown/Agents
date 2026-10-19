# receive local file events and default data loader and recursive character text splitter af37f64c

This folder contains the **receive local file events and default data loader and recursive character text splitter af37f64c** workflow. Its executable nodes use `aggregate`, `chainLlm`, `chainRetrievalQa`, `chainSummarization`, `convertToFile`, `documentDefaultDataLoader`, `embeddingsMistralCloud`, `extractFromFile`, `lmChatMistralCloud`, `localFileTrigger`, `merge`, `outputParserItemList`, `readWriteFile`, `retrieverVectorStore`, `set`, `splitInBatches`, `splitOut`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-local-file-events-and-default-data-loader-and-recursive-character-text-splitter-af37f64c.json`](receive-local-file-events-and-default-data-loader-and-recursive-character-text-splitter-af37f64c.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mistralCloudApi`, `qdrantApi`

**Entry nodes:** Local File Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Local File Trigger | `localFileTrigger` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings Mistral Cloud | `embeddingsMistralCloud` | Inspect parameters |
| Mistral Cloud Chat Model | `lmChatMistralCloud` | Inspect parameters |
| Mistral Cloud Chat Model1 | `lmChatMistralCloud` | Inspect parameters |
| Prep Incoming Doc | `set` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Get Doc Types | `set` | Inspect parameters |
| Split Out Doc Types | `splitOut` | Inspect parameters |
| For Each Doc Type... | `splitInBatches` | Inspect parameters |
| Item List Output Parser | `outputParserItemList` | Inspect parameters |
| Vector Store Retriever | `retrieverVectorStore` | Inspect parameters |
| Embeddings Mistral Cloud1 | `embeddingsMistralCloud` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Mistral Cloud Chat Model2 | `lmChatMistralCloud` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Mistral Cloud Chat Model3 | `lmChatMistralCloud` | Inspect parameters |
| Discover | `chainRetrievalQa` | Inspect parameters |
| 2secs | `wait` | Inspect parameters |
| Get Generated Documents | `set` | Inspect parameters |
| Generate | `chainLlm` | Inspect parameters |
| Prep For AI | `set` | Inspect parameters |
| To Binary | `convertToFile` | toText |
| Export to Folder | `readWriteFile` | write |
| Get FileType | `switch` | Inspect parameters |
| Import File | `readWriteFile` | Inspect parameters |
| Extract from PDF | `extractFromFile` | pdf |
| Extract from DOCX | `extractFromFile` | ods |
| Extract from TEXT | `extractFromFile` | text |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Interview | `chainLlm` | Inspect parameters |

## Connection map

- 2secs → For Each Doc Type... (`main`, output 0, input 0)
- Merge → Prep For AI (`main`, output 0, input 0)
- Discover → Aggregate (`main`, output 0, input 0)
- Generate → 2secs (`main`, output 0, input 0)
- Settings → Import File (`main`, output 0, input 0)
- Aggregate → Generate (`main`, output 0, input 0)
- Interview → Split Out (`main`, output 0, input 0)
- Split Out → Discover (`main`, output 0, input 0)
- To Binary → Export to Folder (`main`, output 0, input 0)
- Import File → Get FileType (`main`, output 0, input 0)
- Prep For AI → Get Doc Types (`main`, output 0, input 0)
- Get FileType → Extract from PDF (`main`, output 0, input 0)
- Get FileType → Extract from DOCX (`main`, output 1, input 0)
- Get FileType → Extract from TEXT (`main`, output 2, input 0)
- Get Doc Types → Split Out Doc Types (`main`, output 0, input 0)
- Extract from PDF → Prep Incoming Doc (`main`, output 0, input 0)
- Extract from DOCX → Prep Incoming Doc (`main`, output 0, input 0)
- Extract from TEXT → Prep Incoming Doc (`main`, output 0, input 0)
- Prep Incoming Doc → Qdrant Vector Store (`main`, output 0, input 0)
- Prep Incoming Doc → Summarization Chain (`main`, output 0, input 0)
- Local File Trigger → Settings (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store → Merge (`main`, output 0, input 1)
- Split Out Doc Types → For Each Doc Type... (`main`, output 0, input 0)
- Summarization Chain → Merge (`main`, output 0, input 0)
- For Each Doc Type... → Get Generated Documents (`main`, output 0, input 0)
- For Each Doc Type... → Interview (`main`, output 1, input 0)
- Qdrant Vector Store1 → Vector Store Retriever (`ai_vectorStore`, output 0, input 0)
- Vector Store Retriever → Discover (`ai_retriever`, output 0, input 0)
- Get Generated Documents → To Binary (`main`, output 0, input 0)
- Item List Output Parser → Interview (`ai_outputParser`, output 0, input 0)
- Embeddings Mistral Cloud → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Mistral Cloud Chat Model → Interview (`ai_languageModel`, output 0, input 0)
- Embeddings Mistral Cloud1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Mistral Cloud Chat Model1 → Summarization Chain (`ai_languageModel`, output 0, input 0)
- Mistral Cloud Chat Model2 → Discover (`ai_languageModel`, output 0, input 0)
- Mistral Cloud Chat Model3 → Generate (`ai_languageModel`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Localfile/1357_Localfile_Wait_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Localfile/1357_Localfile_Wait_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
