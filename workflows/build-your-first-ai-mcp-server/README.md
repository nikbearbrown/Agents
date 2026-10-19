# Build your first AI MCP Server

This folder contains the **Build your first AI MCP Server** workflow. Its executable nodes use `agent`, `chatTrigger`, `debugHelper`, `executeWorkflowTrigger`, `googleCalendarTool`, `httpRequest`, `lmChatOpenAi`, `mcpClientTool`, `mcpTrigger`, `memoryBufferWindow`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`build-your-first-ai-mcp-server.json`](build-your-first-ai-mcp-server.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `openAiApi`

**Entry nodes:** Google Calendar MCP, When Executed by Another Workflow, When chat message received, My Functions Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| SearchEvent | `googleCalendarTool` | getAll |
| CreateEvent | `googleCalendarTool` | Inspect parameters |
| UpdateEvent | `googleCalendarTool` | update |
| DeleteEvent | `googleCalendarTool` | delete |
| Google Calendar MCP | `mcpTrigger` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Convert Text to Upper Case | `set` | Inspect parameters |
| Convert Text to Lower Case | `set` | Inspect parameters |
| Convert Text | `toolWorkflow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Calendar MCP | `mcpClientTool` | Inspect parameters |
| My Functions | `mcpClientTool` | Inspect parameters |
| My Functions Server | `mcpTrigger` | Inspect parameters |
| Random user data | `debugHelper` | Inspect parameters |
| Generate random user data | `toolWorkflow` | Inspect parameters |
| Return only some fields | `set` | Inspect parameters |
| Joke Request | `httpRequest` | Inspect parameters |
| Random Jokes | `toolWorkflow` | Inspect parameters |
| OpenAI 4o | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Switch → Convert Text to Upper Case (`main`, output 0, input 0)
- Switch → Convert Text to Lower Case (`main`, output 1, input 0)
- Switch → Random user data (`main`, output 2, input 0)
- Switch → Joke Request (`main`, output 3, input 0)
- OpenAI 4o → AI Agent (`ai_languageModel`, output 0, input 0)
- CreateEvent → Google Calendar MCP (`ai_tool`, output 0, input 0)
- DeleteEvent → Google Calendar MCP (`ai_tool`, output 0, input 0)
- SearchEvent → Google Calendar MCP (`ai_tool`, output 0, input 0)
- UpdateEvent → Google Calendar MCP (`ai_tool`, output 0, input 0)
- Calendar MCP → AI Agent (`ai_tool`, output 0, input 0)
- Convert Text → My Functions Server (`ai_tool`, output 0, input 0)
- My Functions → AI Agent (`ai_tool`, output 0, input 0)
- Random Jokes → My Functions Server (`ai_tool`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Random user data → Return only some fields (`main`, output 0, input 0)
- Generate random user data → My Functions Server (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Switch (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Debughelper/1184_Debughelper_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Debughelper/1184_Debughelper_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
