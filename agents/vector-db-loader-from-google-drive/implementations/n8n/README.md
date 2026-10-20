# Vector DB Loader from Google Drive

This folder contains the **Vector DB Loader from Google Drive** workflow. Its executable nodes use `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `googleDrive`, `manualTrigger`, `scheduleTrigger`, `splitInBatches`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePGVector`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`vector-db-loader-from-google-drive.json`](vector-db-loader-from-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `postgres`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Postgres PGVector Store | `vectorStorePGVector` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Move File | `googleDrive` | move |
| Download File | `googleDrive` | download |
| Search Folder | `googleDrive` | fileFolder |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Extract from PDF | `extractFromFile` | pdf |
| Extract from Text | `extractFromFile` | text |
| Extract from JSON | `extractFromFile` | fromJson |

## Connection map

- Switch → Extract from PDF (`main`, output 0, input 0)
- Switch → Extract from Text (`main`, output 1, input 0)
- Switch → Extract from JSON (`main`, output 2, input 0)
- Move File → Loop Over Items (`main`, output 0, input 0)
- Download File → Switch (`main`, output 0, input 0)
- Search Folder → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Download File (`main`, output 1, input 0)
- Extract from PDF → Postgres PGVector Store (`main`, output 0, input 0)
- Schedule Trigger → Search Folder (`main`, output 0, input 0)
- Embeddings OpenAI → Postgres PGVector Store (`ai_embedding`, output 0, input 0)
- Extract from JSON → Postgres PGVector Store (`main`, output 0, input 0)
- Extract from Text → Postgres PGVector Store (`main`, output 0, input 0)
- Default Data Loader → Postgres PGVector Store (`ai_document`, output 0, input 0)
- Postgres PGVector Store → Move File (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- When clicking ‘Test workflow’ → Search Folder (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1750_Schedule_Extractfromfile_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1750_Schedule_Extractfromfile_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
