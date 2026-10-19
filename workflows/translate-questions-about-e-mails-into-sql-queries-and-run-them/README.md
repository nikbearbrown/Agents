# Translate questions about e-mails into SQL queries and run them

This folder contains the **Translate questions about e-mails into SQL queries and run them** workflow. Its executable nodes use `agent`, `chatTrigger`, `convertToFile`, `executeWorkflowTrigger`, `extractFromFile`, `if`, `lmChatOllama`, `manualTrigger`, `merge`, `postgres`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`translate-questions-about-e-mails-into-sql-queries-and-run-them.json`](translate-questions-about-e-mails-into-sql-queries-and-run-them.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Chat Trigger, When clicking "Test workflow", WorkflowTrigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Add table name to output | `set` | Inspect parameters |
| Convert data to binary | `convertToFile` | toJson |
| Save file locally | `readWriteFile` | write |
| Extract data from file | `extractFromFile` | fromJson |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Combine schema data and chat input | `set` | Inspect parameters |
| Load the schema from the local file | `readWriteFile` | Inspect parameters |
| Extract SQL query | `set` | Inspect parameters |
| Check if query exists | `if` | Inspect parameters |
| Format query results | `set` | Inspect parameters |
| Combine query result and chat answer | `merge` | Inspect parameters |
| List all columns in a table | `postgres` | executeQuery |
| List all tables in a database | `postgres` | executeQuery |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| Postgres | `postgres` | executeQuery |
| Add trailing semicolon | `set` | Inspect parameters |
| Check for trailing semicolon | `if` | Inspect parameters |
| WorkflowTrigger | `executeWorkflowTrigger` | Inspect parameters |
| If ran manually | `if` | Inspect parameters |
| If file exists or already retried generating it | `if` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Format empty output | `set` | Inspect parameters |

## Connection map

- AI Agent → Extract SQL query (`main`, output 0, input 0)
- Postgres → Format query results (`main`, output 0, input 0)
- Chat Trigger → Load the schema from the local file (`main`, output 0, input 0)
- If ran manually → Load the schema from the local file (`main`, output 1, input 0)
- WorkflowTrigger → Load the schema from the local file (`main`, output 0, input 0)
- Extract SQL query → Check for trailing semicolon (`main`, output 0, input 0)
- Ollama Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Save file locally → If ran manually (`main`, output 0, input 0)
- Format query results → Combine query result and chat answer (`main`, output 0, input 0)
- Check if query exists → Combine query result and chat answer (`main`, output 0, input 1)
- Check if query exists → Postgres (`main`, output 0, input 0)
- Check if query exists → Format empty output (`main`, output 1, input 0)
- Add trailing semicolon → Check if query exists (`main`, output 0, input 0)
- Convert data to binary → Save file locally (`main`, output 0, input 0)
- Extract data from file → Combine schema data and chat input (`main`, output 0, input 0)
- Add table name to output → Convert data to binary (`main`, output 0, input 0)
- List all columns in a table → Add table name to output (`main`, output 0, input 0)
- Check for trailing semicolon → Add trailing semicolon (`main`, output 0, input 0)
- Check for trailing semicolon → Check if query exists (`main`, output 1, input 0)
- List all tables in a database → List all columns in a table (`main`, output 0, input 0)
- When clicking "Test workflow" → List all tables in a database (`main`, output 0, input 0)
- Combine schema data and chat input → AI Agent (`main`, output 0, input 0)
- Load the schema from the local file → If file exists or already retried generating it (`main`, output 0, input 0)
- If file exists or already retried generating it → Extract data from file (`main`, output 0, input 0)
- If file exists or already retried generating it → List all tables in a database (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1245_Postgres_Extractfromfile_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1245_Postgres_Extractfromfile_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
