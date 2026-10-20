# SHEETS RAG

This folder contains the **SHEETS RAG** workflow. Its executable nodes use `agent`, `code`, `executeWorkflowTrigger`, `googleDriveTrigger`, `googleSheets`, `if`, `lmChatGoogleGemini`, `manualChatTrigger`, `postgres`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sheets-rag.json`](sheets-rag.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `postgres`

**Entry nodes:** Google Drive Trigger, Execute Workflow Trigger, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| create table query | `code` | Inspect parameters |
| create insertion query | `code` | Inspect parameters |
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| execute_query_tool | `toolWorkflow` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| get_postgres_schema | `toolWorkflow` | Inspect parameters |
| change_this | `set` | Inspect parameters |
| is not in database | `if` | Inspect parameters |
| table exists? | `postgres` | executeQuery |
| fetch sheet data | `googleSheets` | Inspect parameters |
| remove table | `postgres` | executeQuery |
| create table | `postgres` | executeQuery |
| perform insertion | `postgres` | executeQuery |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| When chat message received | `manualChatTrigger` | Inspect parameters |
| response output | `set` | Inspect parameters |
| sql query executor | `postgres` | executeQuery |
| schema finder | `postgres` | executeQuery |
| schema to string | `code` | Inspect parameters |
| AI Agent With SQL Query Prompt | `agent` | Inspect parameters |

## Connection map

- change_this → table exists? (`main`, output 0, input 0)
- create table → create insertion query (`main`, output 0, input 0)
- remove table → create table query (`main`, output 0, input 0)
- schema finder → schema to string (`main`, output 0, input 0)
- table exists? → fetch sheet data (`main`, output 0, input 0)
- fetch sheet data → is not in database (`main`, output 0, input 0)
- create table query → create table (`main`, output 0, input 0)
- execute_query_tool → AI Agent With SQL Query Prompt (`ai_tool`, output 0, input 0)
- is not in database → create table query (`main`, output 0, input 0)
- is not in database → remove table (`main`, output 1, input 0)
- sql query executor → response output (`main`, output 0, input 0)
- get_postgres_schema → AI Agent With SQL Query Prompt (`ai_tool`, output 0, input 0)
- Google Drive Trigger → change_this (`main`, output 0, input 0)
- create insertion query → perform insertion (`main`, output 0, input 0)
- Execute Workflow Trigger → sql query executor (`main`, output 0, input 0)
- Execute Workflow Trigger → schema finder (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent With SQL Query Prompt (`ai_languageModel`, output 0, input 0)
- When chat message received → AI Agent With SQL Query Prompt (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1144_Postgres_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1144_Postgres_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
