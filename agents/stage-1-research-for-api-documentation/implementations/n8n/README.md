# Stage 1 - Research for API Documentation

This folder contains the **Stage 1 - Research for API Documentation** workflow. Its executable nodes use `aggregate`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `filter`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `removeDuplicates`, `set`, `splitInBatches`, `splitOut`, `switch`, `textClassifier`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`stage-1-research-for-api-documentation.json`](stage-1-research-for-api-documentation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Web Search For API Schema | `httpRequest` | POST |
| Scrape Webpage Contents | `httpRequest` | Inspect parameters |
| Results to List | `splitOut` | Inspect parameters |
| Recursive Character Text Splitter1 | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Content Chunking @ 50k Chars | `set` | Inspect parameters |
| Split Out Chunks | `splitOut` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Set Embedding Variables | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| EventRouter | `switch` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Successful Runs | `filter` | Inspect parameters |
| For Each Document... | `splitInBatches` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Has API Documentation? | `textClassifier` | Inspect parameters |
| Store Document Embeddings | `vectorStoreQdrant` | Inspect parameters |
| Embeddings Google Gemini1 | `embeddingsGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Extract API Operations | `informationExtractor` | Inspect parameters |
| Search in Relevant Docs | `vectorStoreQdrant` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Remove Dupes | `removeDuplicates` | Inspect parameters |
| Filter Results | `filter` | Inspect parameters |
| Research | `executeWorkflow` | Inspect parameters |
| Has Results? | `if` | Inspect parameters |
| Response Empty | `set` | Inspect parameters |
| Response OK | `set` | Inspect parameters |
| Combine Docs | `aggregate` | Inspect parameters |
| Template to List | `splitOut` | Inspect parameters |
| Query Templates | `set` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| For Each Template... | `splitInBatches` | Inspect parameters |
| Query & Docs | `set` | Inspect parameters |
| Identify Service Products | `informationExtractor` | Inspect parameters |
| Extract API Templates | `set` | Inspect parameters |
| Embeddings Google Gemini2 | `embeddingsGoogleGemini` | Inspect parameters |
| Search in Relevant Docs1 | `vectorStoreQdrant` | Inspect parameters |
| Combine Docs1 | `aggregate` | Inspect parameters |
| Query & Docs1 | `set` | Inspect parameters |
| For Each Template...1 | `splitInBatches` | Inspect parameters |
| Merge Lists | `code` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Append Row | `googleSheets` | append |
| Response OK1 | `set` | Inspect parameters |
| Has Operations? | `if` | Inspect parameters |
| Response Empty1 | `set` | Inspect parameters |
| Research Pending | `googleSheets` | update |
| Research Result | `googleSheets` | update |
| Research Error | `googleSheets` | update |
| Extract Pending | `googleSheets` | update |
| Research Event | `set` | Inspect parameters |
| Extract Event | `set` | Inspect parameters |
| Extract | `executeWorkflow` | Inspect parameters |
| Extract Result | `googleSheets` | update |
| Extract Error | `googleSheets` | update |
| Get API Operations | `googleSheets` | Inspect parameters |
| Contruct JSON Schema | `code` | Inspect parameters |
| Upload to Drive | `googleDrive` | createFromText |
| Set Upload Fields | `set` | Inspect parameters |
| Response OK2 | `set` | Inspect parameters |
| Generate Event | `set` | Inspect parameters |
| Generate Pending | `googleSheets` | update |
| Generate | `executeWorkflow` | Inspect parameters |
| Generate Error | `googleSheets` | update |
| Generate Result | `googleSheets` | update |
| Get All Extract | `googleSheets` | Inspect parameters |
| Get All Research | `googleSheets` | Inspect parameters |
| For Each Research... | `splitInBatches` | Inspect parameters |
| For Each Extract... | `splitInBatches` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| All Research Done? | `if` | Inspect parameters |
| All Extract Done? | `if` | Inspect parameters |
| Get All Generate | `googleSheets` | Inspect parameters |
| All Generate Done? | `if` | Inspect parameters |
| For Each Generate... | `splitInBatches` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| Has Results?1 | `if` | Inspect parameters |
| Response Scrape Error | `set` | Inspect parameters |
| Has Results?3 | `if` | Inspect parameters |
| Response No API Docs | `set` | Inspect parameters |

## Connection map

- Wait → For Each Research... (`main`, output 0, input 0)
- Wait1 → For Each Extract... (`main`, output 0, input 0)
- Wait2 → For Each Generate... (`main`, output 0, input 0)
- Extract → Extract Result (`main`, output 0, input 0)
- Extract → Extract Error (`main`, output 1, input 0)
- Generate → Generate Result (`main`, output 0, input 0)
- Generate → Generate Error (`main`, output 1, input 0)
- Research → Research Result (`main`, output 0, input 0)
- Research → Research Error (`main`, output 1, input 0)
- Append Row → Response OK1 (`main`, output 0, input 0)
- EventRouter → Web Search For API Schema (`main`, output 0, input 0)
- EventRouter → Query Templates (`main`, output 1, input 0)
- EventRouter → Get API Operations (`main`, output 2, input 0)
- Merge Lists → Has Operations? (`main`, output 0, input 0)
- Combine Docs → Query & Docs (`main`, output 0, input 0)
- Has Results? → Results to List (`main`, output 0, input 0)
- Has Results? → Response Empty (`main`, output 1, input 0)
- Query & Docs → For Each Template... (`main`, output 0, input 0)
- Remove Dupes → Scrape Webpage Contents (`main`, output 0, input 0)
- Combine Docs1 → Query & Docs1 (`main`, output 0, input 0)
- Extract Error → Wait1 (`main`, output 0, input 0)
- Extract Event → Extract (`main`, output 0, input 0)
- Has Results?1 → Has API Documentation? (`main`, output 0, input 0)
- Has Results?1 → Response Scrape Error (`main`, output 1, input 0)
- Has Results?3 → Set Embedding Variables (`main`, output 0, input 0)
- Has Results?3 → Response No API Docs (`main`, output 1, input 0)
- Query & Docs1 → For Each Template...1 (`main`, output 0, input 0)
- Execution Data → EventRouter (`main`, output 0, input 0)
- Extract Result → Wait1 (`main`, output 0, input 0)
- Filter Results → Remove Dupes (`main`, output 0, input 0)
- Generate Error → Wait2 (`main`, output 0, input 0)
- Generate Event → Generate (`main`, output 0, input 0)
- Research Error → Wait (`main`, output 0, input 0)
- Research Event → Research (`main`, output 0, input 0)
- Extract Pending → Extract Event (`main`, output 0, input 0)
- Generate Result → Wait2 (`main`, output 0, input 0)
- Get All Extract → All Extract Done? (`main`, output 0, input 0)
- Has Operations? → Remove Duplicates (`main`, output 0, input 0)
- Has Operations? → Response Empty1 (`main`, output 1, input 0)
- Query Templates → Template to List (`main`, output 0, input 0)
- Research Result → Wait (`main`, output 0, input 0)
- Results to List → Filter Results (`main`, output 0, input 0)
- Successful Runs → Has Results?1 (`main`, output 0, input 0)
- Upload to Drive → Response OK2 (`main`, output 0, input 0)
- Generate Pending → Generate Event (`main`, output 0, input 0)
- Get All Generate → All Generate Done? (`main`, output 0, input 0)
- Get All Research → All Research Done? (`main`, output 0, input 0)
- Research Pending → Research Event (`main`, output 0, input 0)
- Split Out Chunks → Store Document Embeddings (`main`, output 0, input 0)
- Template to List → For Each Template... (`main`, output 0, input 0)
- All Extract Done? → Get All Generate (`main`, output 0, input 0)
- All Extract Done? → For Each Extract... (`main`, output 1, input 0)
- Remove Duplicates → Append Row (`main`, output 0, input 0)
- Set Upload Fields → Upload to Drive (`main`, output 0, input 0)
- All Generate Done? → For Each Generate... (`main`, output 1, input 0)
- All Research Done? → Get All Extract (`main`, output 0, input 0)
- All Research Done? → For Each Research... (`main`, output 1, input 0)
- Get API Operations → Contruct JSON Schema (`main`, output 0, input 0)
- Default Data Loader → Store Document Embeddings (`ai_document`, output 0, input 0)
- For Each Extract... → Get All Generate (`main`, output 0, input 0)
- For Each Extract... → Extract Pending (`main`, output 1, input 0)
- Contruct JSON Schema → Set Upload Fields (`main`, output 0, input 0)
- For Each Document... → Response OK (`main`, output 0, input 0)
- For Each Document... → Content Chunking @ 50k Chars (`main`, output 1, input 0)
- For Each Generate... → Generate Pending (`main`, output 1, input 0)
- For Each Research... → Get All Extract (`main`, output 0, input 0)
- For Each Research... → Research Pending (`main`, output 1, input 0)
- For Each Template... → Identify Service Products (`main`, output 0, input 0)
- For Each Template... → Search in Relevant Docs (`main`, output 1, input 0)
- Extract API Templates → For Each Template...1 (`main`, output 0, input 0)
- For Each Template...1 → Extract API Operations (`main`, output 0, input 0)
- For Each Template...1 → Search in Relevant Docs1 (`main`, output 1, input 0)
- Extract API Operations → Merge Lists (`main`, output 0, input 0)
- Has API Documentation? → Has Results?3 (`main`, output 0, input 0)
- Scrape Webpage Contents → Successful Runs (`main`, output 0, input 0)
- Search in Relevant Docs → Combine Docs (`main`, output 0, input 0)
- Set Embedding Variables → For Each Document... (`main`, output 0, input 0)
- Embeddings Google Gemini → Store Document Embeddings (`ai_embedding`, output 0, input 0)
- Execute Workflow Trigger → Execution Data (`main`, output 0, input 0)
- Google Gemini Chat Model → Has API Documentation? (`ai_languageModel`, output 0, input 0)
- Search in Relevant Docs1 → Combine Docs1 (`main`, output 0, input 0)
- Embeddings Google Gemini1 → Search in Relevant Docs (`ai_embedding`, output 0, input 0)
- Embeddings Google Gemini2 → Search in Relevant Docs1 (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model1 → Extract API Operations (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Identify Service Products (`ai_languageModel`, output 0, input 0)
- Identify Service Products → Extract API Templates (`main`, output 0, input 0)
- Store Document Embeddings → For Each Document... (`main`, output 0, input 0)
- Web Search For API Schema → Has Results? (`main`, output 0, input 0)
- Content Chunking @ 50k Chars → Split Out Chunks (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get All Research (`main`, output 0, input 0)
- Recursive Character Text Splitter1 → Default Data Loader (`ai_textSplitter`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0668_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0668_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
