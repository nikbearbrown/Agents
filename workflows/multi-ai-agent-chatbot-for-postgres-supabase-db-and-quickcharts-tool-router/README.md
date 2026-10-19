# ✨📊Multi-AI Agent Chatbot for Postgres/Supabase DB and QuickCharts + Tool Router

This folder contains the **✨📊Multi-AI Agent Chatbot for Postgres/Supabase DB and QuickCharts + Tool Router** workflow. Its executable nodes use `agent`, `chatTrigger`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryPostgresChat`, `outputParserStructured`, `postgresTool`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`multi-ai-agent-chatbot-for-postgres-supabase-db-and-quickcharts-tool-router.json`](multi-ai-agent-chatbot-for-postgres-supabase-db-and-quickcharts-tool-router.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Execute SQL Query | `postgresTool` | executeQuery |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| query_db_tool | `toolWorkflow` | Inspect parameters |
| generate_quickchart_tool | `toolWorkflow` | Inspect parameters |
| Create QuickChart | `httpRequest` | Inspect parameters |
| QuickChart Object Schema | `outputParserStructured` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| gpt-4o-mini-2 | `lmChatOpenAi` | Inspect parameters |
| 🤖Primary Agent | `agent` | Inspect parameters |
| 🤖Secondary Postgres Agent | `agent` | Inspect parameters |
| 🤖Secondary QuickChart Agent | `agent` | Inspect parameters |
| 🔀Tool Agent Router | `switch` | Inspect parameters |
| Table Definitions | `postgresTool` | executeQuery |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Final QuickChart URL | `set` | Inspect parameters |
| QuickChart GET URL | `set` | Inspect parameters |
| DB Schema and Tables | `postgresTool` | executeQuery |
| gpt-40-mini-1 | `lmChatOpenAi` | Inspect parameters |

## Connection map

- gpt-4o-mini → 🤖Primary Agent (`ai_languageModel`, output 0, input 0)
- gpt-40-mini-1 → 🤖Secondary Postgres Agent (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini-2 → 🤖Secondary QuickChart Agent (`ai_languageModel`, output 0, input 0)
- query_db_tool → 🤖Primary Agent (`ai_tool`, output 0, input 0)
- Create QuickChart → Final QuickChart URL (`main`, output 0, input 0)
- Execute SQL Query → 🤖Secondary Postgres Agent (`ai_tool`, output 0, input 0)
- Table Definitions → 🤖Secondary Postgres Agent (`ai_tool`, output 0, input 0)
- QuickChart GET URL → Create QuickChart (`main`, output 0, input 0)
- DB Schema and Tables → 🤖Secondary Postgres Agent (`ai_tool`, output 0, input 0)
- Postgres Chat Memory → 🤖Primary Agent (`ai_memory`, output 0, input 0)
- 🔀Tool Agent Router → 🤖Secondary Postgres Agent (`main`, output 0, input 0)
- 🔀Tool Agent Router → 🤖Secondary QuickChart Agent (`main`, output 1, input 0)
- QuickChart Object Schema → 🤖Secondary QuickChart Agent (`ai_outputParser`, output 0, input 0)
- generate_quickchart_tool → 🤖Primary Agent (`ai_tool`, output 0, input 0)
- When chat message received → 🤖Primary Agent (`main`, output 0, input 0)
- 🤖Secondary QuickChart Agent → QuickChart GET URL (`main`, output 0, input 0)
- When Executed by Another Workflow → 🔀Tool Agent Router (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1558_HTTP_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1558_HTTP_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
