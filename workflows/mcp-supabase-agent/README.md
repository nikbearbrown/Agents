# MCP_SUPABASE_AGENT

This folder contains the **MCP_SUPABASE_AGENT** workflow. Its executable nodes use `embeddingsOpenAi`, `mcpTrigger`, `supabaseTool`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mcp-supabase-agent.json`](mcp-supabase-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `supabaseApi`

**Entry nodes:** MCP_SUPABASE

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| MCP_SUPABASE | `mcpTrigger` | Inspect parameters |
| RAG | `vectorStoreSupabase` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| DELETE_ROW_INSCRICOES_CURSOS | `supabaseTool` | delete |
| GET_ROW_AGENT_MESSAGE | `supabaseTool` | get |
| CREATE_ROW_AGENT_MESSAGE | `supabaseTool` | Inspect parameters |
| DELETE_ROW_AGENT_MESSAGE | `supabaseTool` | delete |
| UPDATE_ROW_AGENT_MESSAGE | `supabaseTool` | update |
| GET_MANY_ROW_AGENT_MESSAGE | `supabaseTool` | getAll |
| CREATE_ROW_AGENT_TASKS | `supabaseTool` | Inspect parameters |
| GET_ROW_AGENT_TASKS | `supabaseTool` | get |
| DELETE_ROW_AGENT_TASKS | `supabaseTool` | delete |
| UPDATE_ROW_AGENT_TASKS | `supabaseTool` | update |
| GET_MANY_ROW_AGENT_TASKS | `supabaseTool` | getAll |
| CREATE_ROW_AGENT_STATUS | `supabaseTool` | Inspect parameters |
| GET_ROW_AGENT_STATUS | `supabaseTool` | get |
| DELETE_ROW_AGENT_STATUS | `supabaseTool` | delete |
| UPDATE_ROW_AGENT_STATUS | `supabaseTool` | update |
| GET_MANY_ROW_AGENT_STATUS | `supabaseTool` | getAll |
| CREATE_ROW_AGENT_KNOWLEDGE | `supabaseTool` | Inspect parameters |
| GET_ROW_AGENT_KNOWLEDGE | `supabaseTool` | get |
| UPDATE_ROW_INSCRICOES_AGENT_KNOWLEDGE | `supabaseTool` | update |
| GET_MANY_ROW_AGENT_KNOWLEDGE | `supabaseTool` | getAll |

## Connection map

- RAG → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- Embeddings OpenAI → RAG (`ai_embedding`, output 0, input 0)
- GET_ROW_AGENT_TASKS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_ROW_AGENT_STATUS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_ROW_AGENT_MESSAGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- CREATE_ROW_AGENT_TASKS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- DELETE_ROW_AGENT_TASKS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- UPDATE_ROW_AGENT_TASKS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- CREATE_ROW_AGENT_STATUS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- DELETE_ROW_AGENT_STATUS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_ROW_AGENT_KNOWLEDGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- UPDATE_ROW_AGENT_STATUS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- CREATE_ROW_AGENT_MESSAGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- DELETE_ROW_AGENT_MESSAGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_MANY_ROW_AGENT_TASKS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- UPDATE_ROW_AGENT_MESSAGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_MANY_ROW_AGENT_STATUS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- CREATE_ROW_AGENT_KNOWLEDGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_MANY_ROW_AGENT_MESSAGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- DELETE_ROW_INSCRICOES_CURSOS → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- GET_MANY_ROW_AGENT_KNOWLEDGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)
- UPDATE_ROW_INSCRICOES_AGENT_KNOWLEDGE → MCP_SUPABASE (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1947_Stickynote_Supabasetool_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1947_Stickynote_Supabasetool_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
