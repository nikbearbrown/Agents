# extracthtmlcontent html and reviews to list and default data loader

This folder contains the **extracthtmlcontent html and reviews to list and default data loader** workflow. Its executable nodes use `code`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `html`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `set`, `splitOut`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extracthtmlcontent-html-and-reviews-to-list-and-default-data-loader.json`](extracthtmlcontent-html-and-reviews-to-list-and-default-data-loader.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `qdrantApi`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Zip Entries | `set` | Inspect parameters |
| Extract Reviews | `html` | extractHtmlContent |
| Reviews to List | `splitOut` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Get Payload of Points | `httpRequest` | POST |
| Clusters To List | `splitOut` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Only Clusters With 3+ points | `filter` | Inspect parameters |
| Set Variables1 | `set` | Inspect parameters |
| Find Reviews | `httpRequest` | POST |
| Prep Output For Export | `set` | Inspect parameters |
| Export To Sheets | `googleSheets` | append |
| Clear Existing Reviews | `httpRequest` | POST |
| Trigger Insights | `executeWorkflow` | Inspect parameters |
| Prep Values For Trigger | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Get TrustPilot Page | `httpRequest` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Apply K-means Clustering Algorithm | `code` | Inspect parameters |
| Customer Insights Agent | `informationExtractor` | Inspect parameters |

## Connection map

- Zip Entries → Reviews to List (`main`, output 0, input 0)
- Find Reviews → Apply K-means Clustering Algorithm (`main`, output 0, input 0)
- Set Variables → Clear Existing Reviews (`main`, output 0, input 0)
- Set Variables1 → Find Reviews (`main`, output 0, input 0)
- Extract Reviews → Zip Entries (`main`, output 0, input 0)
- Reviews to List → Qdrant Vector Store (`main`, output 0, input 0)
- Clusters To List → Only Clusters With 3+ points (`main`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Customer Insights Agent (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Get TrustPilot Page → Extract Reviews (`main`, output 0, input 0)
- Qdrant Vector Store → Prep Values For Trigger (`main`, output 0, input 0)
- Get Payload of Points → Customer Insights Agent (`main`, output 0, input 0)
- Clear Existing Reviews → Get TrustPilot Page (`main`, output 0, input 0)
- Prep Output For Export → Export To Sheets (`main`, output 0, input 0)
- Customer Insights Agent → Prep Output For Export (`main`, output 0, input 0)
- Prep Values For Trigger → Trigger Insights (`main`, output 0, input 0)
- Execute Workflow Trigger → Set Variables1 (`main`, output 0, input 0)
- Only Clusters With 3+ points → Get Payload of Points (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Variables (`main`, output 0, input 0)
- Apply K-means Clustering Algorithm → Clusters To List (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0555_Splitout_Code_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0555_Splitout_Code_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `extracthtmlcontent-html-and-reviews-to-list-and-default-data-loader-9ce3fb67` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
