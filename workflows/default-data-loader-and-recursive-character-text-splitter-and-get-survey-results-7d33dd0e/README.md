# default data loader and recursive character text splitter and get survey results 7d33dd0e

This folder contains the **default data loader and recursive character text splitter and get survey results 7d33dd0e** workflow. Its executable nodes use `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `httpRequest`, `if`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`default-data-loader-and-recursive-character-text-splitter-and-get-survey-results-7d33dd0e.json`](default-data-loader-and-recursive-character-text-splitter-and-get-survey-results-7d33dd0e.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `qdrantApi`

**Entry nodes:** Execute Workflow Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Convert to Question Answer Pairs | `set` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Get Survey Results | `googleSheets` | Inspect parameters |
| Get Survey Headers | `googleSheets` | Inspect parameters |
| Extract Questions | `set` | Inspect parameters |
| Questions to List | `splitOut` | Inspect parameters |
| Find All Answers | `httpRequest` | POST |
| Get Payload of Points | `httpRequest` | POST |
| Clusters To List | `splitOut` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Prep Output For Export | `set` | Inspect parameters |
| Export To Sheets | `googleSheets` | append |
| Export To Sheets1 | `googleSheets` | append |
| For Each Question... | `splitInBatches` | Inspect parameters |
| Trigger Insights | `executeWorkflow` | Inspect parameters |
| Prep Values For Trigger | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Create Insights Sheet | `googleSheets` | create |
| Prep Values For Export | `set` | Inspect parameters |
| QA Pairs to List | `splitOut` | Inspect parameters |
| Has Clusters? | `if` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Sheet Details | `httpRequest` | Inspect parameters |
| Only Clusters With 3+ points | `filter` | Inspect parameters |
| Apply K-means Clustering Algorithm | `code` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Survey Insights Agent | `informationExtractor` | Inspect parameters |

## Connection map

- Has Clusters? → Clusters To List (`main`, output 0, input 0)
- Has Clusters? → Prep Values For Export (`main`, output 1, input 0)
- Set Variables → Create Insights Sheet (`main`, output 0, input 0)
- Clusters To List → Only Clusters With 3+ points (`main`, output 0, input 0)
- Export To Sheets → For Each Question... (`main`, output 0, input 0)
- Find All Answers → Apply K-means Clustering Algorithm (`main`, output 0, input 0)
- QA Pairs to List → Qdrant Vector Store (`main`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Export To Sheets1 → For Each Question... (`main`, output 0, input 0)
- Extract Questions → Questions to List (`main`, output 0, input 0)
- Get Sheet Details → Set Variables (`main`, output 0, input 0)
- OpenAI Chat Model → Survey Insights Agent (`ai_languageModel`, output 0, input 0)
- Questions to List → For Each Question... (`main`, output 0, input 0)
- Get Survey Headers → Extract Questions (`main`, output 0, input 0)
- Get Survey Results → Convert to Question Answer Pairs (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store → Prep Values For Trigger (`main`, output 0, input 0)
- For Each Question... → Find All Answers (`main`, output 1, input 0)
- Create Insights Sheet → Get Survey Headers (`main`, output 0, input 0)
- Get Payload of Points → Survey Insights Agent (`main`, output 0, input 0)
- Survey Insights Agent → Prep Output For Export (`main`, output 0, input 0)
- Prep Output For Export → Export To Sheets (`main`, output 0, input 0)
- Prep Values For Export → Export To Sheets1 (`main`, output 0, input 0)
- Prep Values For Trigger → Trigger Insights (`main`, output 0, input 0)
- Execute Workflow Trigger → Get Sheet Details (`main`, output 0, input 0)
- Only Clusters With 3+ points → Get Payload of Points (`main`, output 0, input 0)
- Convert to Question Answer Pairs → QA Pairs to List (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Survey Results (`main`, output 0, input 0)
- Apply K-means Clustering Algorithm → Has Clusters? (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1678_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1678_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
