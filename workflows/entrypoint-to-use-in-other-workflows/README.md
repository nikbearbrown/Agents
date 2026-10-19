# Entrypoint to use in other workflows

This folder contains the **Entrypoint to use in other workflows** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `executeWorkflowTrigger`, `filter`, `lmChatOllama`, `lmOllama`, `manualTrigger`, `merge`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`entrypoint-to-use-in-other-workflows.json`](entrypoint-to-use-in-other-workflows.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`

**Entry nodes:** When clicking ‘Test workflow’, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Code | `code` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Basic LLM Chain4 | `chainLlm` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Ollama Model | `lmOllama` | Inspect parameters |

## Connection map

- Code → Merge1 (`main`, output 0, input 1)
- Merge → Filter (`main`, output 0, input 0)
- Filter → Aggregate (`main`, output 0, input 0)
- Merge1 → Split Out1 (`main`, output 0, input 0)
- Aggregate → Basic LLM Chain (`main`, output 0, input 0)
- Split Out1 → Merge (`main`, output 0, input 0)
- Split Out1 → Basic LLM Chain4 (`main`, output 0, input 0)
- Edit Fields → Code (`main`, output 0, input 0)
- Edit Fields → Merge1 (`main`, output 0, input 0)
- Ollama Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Basic LLM Chain4 → Merge (`main`, output 0, input 1)
- Ollama Chat Model → Basic LLM Chain4 (`ai_languageModel`, output 0, input 0)
- When Executed by Another Workflow → Code (`main`, output 0, input 0)
- When Executed by Another Workflow → Merge1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0725_Splitout_Code_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0725_Splitout_Code_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
