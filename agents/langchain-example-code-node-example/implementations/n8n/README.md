# LangChain - Example - Code Node Example

This folder contains the **LangChain - Example - Code Node Example** workflow. Its executable nodes use `agent`, `code`, `lmChatOpenAi`, `lmOpenAi`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`langchain-example-code-node-example.json`](langchain-example-code-node-example.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI | `lmOpenAi` | Inspect parameters |
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Set1 | `set` | Inspect parameters |
| Chat OpenAI | `lmChatOpenAi` | Inspect parameters |
| Custom - Wikipedia | `code` | Inspect parameters |
| Custom - LLM Chain Node | `code` | Inspect parameters |
| Agent | `agent` | Inspect parameters |

## Connection map

- Set → Custom - LLM Chain Node (`main`, output 0, input 0)
- Set1 → Agent (`main`, output 0, input 0)
- OpenAI → Custom - LLM Chain Node (`ai_languageModel`, output 0, input 0)
- Chat OpenAI → Agent (`ai_languageModel`, output 0, input 0)
- Custom - Wikipedia → Agent (`ai_tool`, output 0, input 0)
- When clicking "Execute Workflow" → Set (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Set1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1397_Manual_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1397_Manual_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
