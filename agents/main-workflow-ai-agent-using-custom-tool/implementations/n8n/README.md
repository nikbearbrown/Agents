# Main workflow: AI agent using custom tool

This folder contains the **Main workflow: AI agent using custom tool** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `filter`, `googleSheets`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`main-workflow-ai-agent-using-custom-tool.json`](main-workflow-ai-agent-using-custom-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| List columns tool | `toolWorkflow` | Inspect parameters |
| Get column values tool | `toolWorkflow` | Inspect parameters |
| Get customer tool | `toolWorkflow` | Inspect parameters |
| Set Google Sheet URL | `set` | Inspect parameters |
| Get Google sheet contents | `googleSheets` | Inspect parameters |
| Check operation | `switch` | Inspect parameters |
| Get column names | `set` | Inspect parameters |
| Prepare column data | `set` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Prepare output | `code` | Inspect parameters |

## Connection map

- Filter → Prepare output (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Check operation → Get column names (`main`, output 0, input 0)
- Check operation → Prepare column data (`main`, output 1, input 0)
- Check operation → Filter (`main`, output 2, input 0)
- Get column names → Prepare output (`main`, output 0, input 0)
- Get customer tool → AI Agent (`ai_tool`, output 0, input 0)
- List columns tool → AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- Prepare column data → Prepare output (`main`, output 0, input 0)
- Set Google Sheet URL → Get Google sheet contents (`main`, output 0, input 0)
- Get column values tool → AI Agent (`ai_tool`, output 0, input 0)
- Get Google sheet contents → Check operation (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Set Google Sheet URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0401_Code_Filter_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0401_Code_Filter_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
