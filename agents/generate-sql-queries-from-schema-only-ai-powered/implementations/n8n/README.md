# Generate SQL queries from schema only - AI-powered

This folder contains the **Generate SQL queries from schema only - AI-powered** workflow. Its executable nodes use `agent`, `chatTrigger`, `convertToFile`, `extractFromFile`, `if`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `merge`, `mySql`, `noOp`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-sql-queries-from-schema-only-ai-powered.json`](generate-sql-queries-from-schema-only-ai-powered.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`, `openAiApi`

**Entry nodes:** Chat Trigger, When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| List all tables in a database | `mySql` | executeQuery |
| Extract database schema | `mySql` | executeQuery |
| Add table name to output | `set` | Inspect parameters |
| Convert data to binary | `convertToFile` | toJson |
| Save file locally | `readWriteFile` | write |
| Extract data from file | `extractFromFile` | fromJson |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Combine schema data and chat input | `set` | Inspect parameters |
| Load the schema from the local file | `readWriteFile` | Inspect parameters |
| Extract SQL query | `set` | Inspect parameters |
| Check if query exists | `if` | Inspect parameters |
| Format query results | `set` | Inspect parameters |
| Run SQL query | `mySql` | executeQuery |
| Prepare final output | `set` | Inspect parameters |
| Combine query result and chat answer | `merge` | Inspect parameters |

## Connection map

- AI Agent → Extract SQL query (`main`, output 0, input 0)
- Chat Trigger → Load the schema from the local file (`main`, output 0, input 0)
- Run SQL query → Format query results (`main`, output 0, input 0)
- Extract SQL query → Check if query exists (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Format query results → Combine query result and chat answer (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Check if query exists → Run SQL query (`main`, output 0, input 0)
- Check if query exists → Combine query result and chat answer (`main`, output 0, input 1)
- Check if query exists → No Operation, do nothing (`main`, output 1, input 0)
- Convert data to binary → Save file locally (`main`, output 0, input 0)
- Extract data from file → Combine schema data and chat input (`main`, output 0, input 0)
- Extract database schema → Add table name to output (`main`, output 0, input 0)
- Add table name to output → Convert data to binary (`main`, output 0, input 0)
- List all tables in a database → Extract database schema (`main`, output 0, input 0)
- When clicking "Test workflow" → List all tables in a database (`main`, output 0, input 0)
- Combine schema data and chat input → AI Agent (`main`, output 0, input 0)
- Load the schema from the local file → Extract data from file (`main`, output 0, input 0)
- Combine query result and chat answer → Prepare final output (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1590_Extractfromfile_Converttofile_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1590_Extractfromfile_Converttofile_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
