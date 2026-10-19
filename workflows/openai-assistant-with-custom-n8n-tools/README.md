# OpenAI Assistant with custom n8n tools

This folder contains the **OpenAI Assistant with custom n8n tools** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `if`, `manualChatTrigger`, `merge`, `openAiAssistant`, `set`, `summarize`, `toolCode`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`openai-assistant-with-custom-n8n-tools.json`](openai-assistant-with-custom-n8n-tools.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** On new manual Chat Message, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On new manual Chat Message | `manualChatTrigger` | Inspect parameters |
| OpenAI Assistant | `openAiAssistant` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Mapping data | `code` | Inspect parameters |
| List countries? | `if` | Inspect parameters |
| Mapping data1 | `code` | Inspect parameters |
| Return country list | `set` | Inspect parameters |
| Return specific capital | `set` | Inspect parameters |
| Tool to call the workflow below | `toolWorkflow` | Inspect parameters |
| Concatenate country names | `summarize` | Inspect parameters |
| Get the matching country's details | `merge` | Inspect parameters |
| Tool: Get current date and time | `toolCode` | Inspect parameters |

## Connection map

- Mapping data → Concatenate country names (`main`, output 0, input 0)
- Mapping data1 → Get the matching country's details (`main`, output 0, input 1)
- List countries? → Mapping data (`main`, output 0, input 0)
- List countries? → Get the matching country's details (`main`, output 1, input 0)
- Execute Workflow Trigger → List countries? (`main`, output 0, input 0)
- Concatenate country names → Return country list (`main`, output 0, input 0)
- On new manual Chat Message → OpenAI Assistant (`main`, output 0, input 0)
- Tool to call the workflow below → OpenAI Assistant (`ai_tool`, output 0, input 0)
- Tool: Get current date and time → OpenAI Assistant (`ai_tool`, output 0, input 0)
- Get the matching country's details → Return specific capital (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Summarize/1582_Summarize_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Summarize/1582_Summarize_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
