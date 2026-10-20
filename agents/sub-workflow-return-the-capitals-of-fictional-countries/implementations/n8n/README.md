# Sub-workflow: Return the capitals of fictional countries

This folder contains the **Sub-workflow: Return the capitals of fictional countries** workflow. Its executable nodes use `chatTrigger`, `code`, `executeWorkflowTrigger`, `if`, `memoryBufferWindow`, `merge`, `openAi`, `set`, `summarize`, `toolCode`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sub-workflow-return-the-capitals-of-fictional-countries.json`](sub-workflow-return-the-capitals-of-fictional-countries.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI | `openAi` | assistant |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Tool to call the workflow below | `toolWorkflow` | Inspect parameters |
| Tool: Get current date and time | `toolCode` | Inspect parameters |
| List countries? | `if` | Inspect parameters |
| Mapping data | `code` | Inspect parameters |
| Concatenate country names | `summarize` | Inspect parameters |
| Return country list | `set` | Inspect parameters |
| Mapping data1 | `code` | Inspect parameters |
| Get the matching country's details | `merge` | Inspect parameters |
| Return specific capital | `set` | Inspect parameters |

## Connection map

- Mapping data → Concatenate country names (`main`, output 0, input 0)
- Mapping data1 → Get the matching country's details (`main`, output 0, input 1)
- Simple Memory → OpenAI (`ai_memory`, output 0, input 0)
- List countries? → Mapping data (`main`, output 0, input 0)
- List countries? → Get the matching country's details (`main`, output 1, input 0)
- List countries? → Mapping data1 (`main`, output 1, input 0)
- Concatenate country names → Return country list (`main`, output 0, input 0)
- When chat message received → OpenAI (`main`, output 0, input 0)
- Tool to call the workflow below → OpenAI (`ai_tool`, output 0, input 0)
- Tool: Get current date and time → OpenAI (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → List countries? (`main`, output 0, input 0)
- Get the matching country's details → Return specific capital (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0371_Executeworkflow_Summarize_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0371_Executeworkflow_Summarize_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
