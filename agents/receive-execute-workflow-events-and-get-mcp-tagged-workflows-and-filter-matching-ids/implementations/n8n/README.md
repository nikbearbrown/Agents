# receive execute workflow events and get mcp tagged workflows and filter matching ids

This folder contains the **receive execute workflow events and get mcp tagged workflows and filter matching ids** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `if`, `lmChatOpenAi`, `mcpClientTool`, `mcpTrigger`, `memoryBufferWindow`, `n8n`, `redis`, `set`, `splitOut`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-execute-workflow-events-and-get-mcp-tagged-workflows-and-filter-matching-ids.json`](receive-execute-workflow-events-and-get-mcp-tagged-workflows-and-filter-matching-ids.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `openAiApi`, `redis`

**Entry nodes:** When Executed by Another Workflow, When chat message received, N8N Workflows MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Simplify Workflows | `set` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Operations | `switch` | Inspect parameters |
| Get MCP-tagged Workflows | `n8n` | Inspect parameters |
| Filter Matching Ids | `filter` | Inspect parameters |
| Store In Memory | `redis` | set |
| AddTool Success | `set` | Inspect parameters |
| AddTool Error | `set` | Inspect parameters |
| Get Memory | `redis` | get |
| Split Out | `splitOut` | Inspect parameters |
| Filter Matching IDs | `filter` | Inspect parameters |
| Store In Memory1 | `redis` | set |
| Remove Tool Success | `set` | Inspect parameters |
| Convert to JSON | `set` | Inspect parameters |
| listTools Success | `set` | Inspect parameters |
| Get MCP-tagged Workflows1 | `n8n` | Inspect parameters |
| Simplify Workflows1 | `set` | Inspect parameters |
| listTools Success1 | `aggregate` | Inspect parameters |
| Get Parameters | `set` | Inspect parameters |
| executeTool Result | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| MCP Client | `mcpClientTool` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Convert to JSON1 | `set` | Inspect parameters |
| Has Workflow Available? | `if` | Inspect parameters |
| ExecuteTool Error | `set` | Inspect parameters |
| Workflow Exists? | `if` | Inspect parameters |
| N8N Workflows MCP Server | `mcpTrigger` | Inspect parameters |
| Add Workflow | `toolWorkflow` | Inspect parameters |
| RemoveWorkflow | `toolWorkflow` | Inspect parameters |
| List Workflows | `toolWorkflow` | Inspect parameters |
| SearchWorkflows | `toolWorkflow` | Inspect parameters |
| ExecuteWorkflow | `toolWorkflow` | Inspect parameters |
| Execute Workflow with PassThrough Variables | `executeWorkflow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Is Empty Array? | `if` | Inspect parameters |
| Delete Key | `redis` | delete |

## Connection map

- Split Out → Filter Matching IDs (`main`, output 0, input 0)
- Delete Key → Remove Tool Success (`main`, output 0, input 0)
- Get Memory → Operations (`main`, output 0, input 0)
- MCP Client → AI Agent (`ai_tool`, output 0, input 0)
- Operations → Get MCP-tagged Workflows (`main`, output 0, input 0)
- Operations → Convert to JSON (`main`, output 1, input 0)
- Operations → listTools Success (`main`, output 2, input 0)
- Operations → Get MCP-tagged Workflows1 (`main`, output 3, input 0)
- Operations → Convert to JSON1 (`main`, output 4, input 0)
- Add Workflow → N8N Workflows MCP Server (`ai_tool`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Get Parameters → Execute Workflow with PassThrough Variables (`main`, output 0, input 0)
- List Workflows → N8N Workflows MCP Server (`ai_tool`, output 0, input 0)
- RemoveWorkflow → N8N Workflows MCP Server (`ai_tool`, output 0, input 0)
- Convert to JSON → Split Out (`main`, output 0, input 0)
- ExecuteWorkflow → N8N Workflows MCP Server (`ai_tool`, output 0, input 0)
- Is Empty Array? → Delete Key (`main`, output 0, input 0)
- Is Empty Array? → Store In Memory1 (`main`, output 1, input 0)
- SearchWorkflows → N8N Workflows MCP Server (`ai_tool`, output 0, input 0)
- Store In Memory → AddTool Success (`main`, output 0, input 0)
- Convert to JSON1 → Has Workflow Available? (`main`, output 0, input 0)
- Store In Memory1 → Remove Tool Success (`main`, output 0, input 0)
- Workflow Exists? → Simplify Workflows (`main`, output 0, input 0)
- Workflow Exists? → AddTool Error (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Simplify Workflows → Store In Memory (`main`, output 0, input 0)
- Filter Matching IDs → Is Empty Array? (`main`, output 0, input 0)
- Filter Matching Ids → Workflow Exists? (`main`, output 0, input 0)
- Simplify Workflows1 → listTools Success1 (`main`, output 0, input 0)
- Has Workflow Available? → Get Parameters (`main`, output 0, input 0)
- Has Workflow Available? → ExecuteTool Error (`main`, output 1, input 0)
- Get MCP-tagged Workflows → Filter Matching Ids (`main`, output 0, input 0)
- Get MCP-tagged Workflows1 → Simplify Workflows1 (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Get Memory (`main`, output 0, input 0)
- Execute Workflow with PassThrough Variables → executeTool Result (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0894_Splitout_Redis_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0894_Splitout_Redis_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
