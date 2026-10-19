# Get Gong Calls and Supporting Data

This folder contains the **Get Gong Calls and Supporting Data** workflow. Its executable nodes use `aggregate`, `compareDatasets`, `executeWorkflow`, `executeWorkflowTrigger`, `gong`, `googleSheets`, `manualTrigger`, `merge`, `noOp`, `notion`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-gong-calls-and-supporting-data.json`](get-gong-calls-and-supporting-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gongApi`, `googleSheetsOAuth2Api`, `notionApi`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Gong | `gong` | Inspect parameters |
| Transcript Processor | `executeWorkflow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Call Aggregator | `aggregate` | Inspect parameters |
| Integration Aggregator | `aggregate` | Inspect parameters |
| Get Integrations | `googleSheets` | Inspect parameters |
| Comma Separate Integrations | `set` | Inspect parameters |
| Comma separate competitors | `set` | Inspect parameters |
| Get list of Competitors | `notion` | database |
| Merge 3 objects into one | `merge` | Inspect parameters |
| Aggregate Call Data | `aggregate` | Inspect parameters |
| Split Out Call Data and Competitors | `splitOut` | Inspect parameters |
| Reduce down to 1 object | `aggregate` | Inspect parameters |
| Get Previous Phone Calls | `notion` | databasePage / getAll |
| Isolate Only Call IDs | `set` | Inspect parameters |
| Only Process New Calls | `compareDatasets` | Inspect parameters |
| Loop Over Calls | `splitInBatches` | Inspect parameters |
| Process All Call Transcripts | `executeWorkflow` | Inspect parameters |
| Receive all Transcripts | `noOp` | Inspect parameters |

## Connection map

- Gong → Call Aggregator (`main`, output 0, input 0)
- Call Aggregator → Merge 3 objects into one (`main`, output 0, input 0)
- Loop Over Calls → Receive all Transcripts (`main`, output 0, input 0)
- Loop Over Calls → Transcript Processor (`main`, output 1, input 0)
- Get Integrations → Integration Aggregator (`main`, output 0, input 0)
- Aggregate Call Data → Split Out Call Data and Competitors (`main`, output 0, input 0)
- Transcript Processor → Loop Over Calls (`main`, output 0, input 0)
- Isolate Only Call IDs → Only Process New Calls (`main`, output 0, input 1)
- Integration Aggregator → Comma Separate Integrations (`main`, output 0, input 0)
- Only Process New Calls → Loop Over Calls (`main`, output 0, input 0)
- Get list of Competitors → Comma separate competitors (`main`, output 0, input 0)
- Receive all Transcripts → Process All Call Transcripts (`main`, output 0, input 0)
- Reduce down to 1 object → Get Previous Phone Calls (`main`, output 0, input 0)
- Execute Workflow Trigger → Gong (`main`, output 0, input 0)
- Execute Workflow Trigger → Get list of Competitors (`main`, output 0, input 0)
- Execute Workflow Trigger → Get Integrations (`main`, output 0, input 0)
- Get Previous Phone Calls → Isolate Only Call IDs (`main`, output 0, input 0)
- Merge 3 objects into one → Aggregate Call Data (`main`, output 0, input 0)
- Merge 3 objects into one → Reduce down to 1 object (`main`, output 0, input 0)
- Comma separate competitors → Merge 3 objects into one (`main`, output 0, input 2)
- Comma Separate Integrations → Merge 3 objects into one (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Gong (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Integrations (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get list of Competitors (`main`, output 0, input 0)
- Split Out Call Data and Competitors → Only Process New Calls (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0759_Splitout_Comparedatasets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0759_Splitout_Comparedatasets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
