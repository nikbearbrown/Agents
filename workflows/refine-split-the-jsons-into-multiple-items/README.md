# Refine/Split the jsons into multiple items

This folder contains the **Refine/Split the jsons into multiple items** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `googleSheets`, `if`, `informationExtractor`, `lmChatOpenAi`, `memoryBufferWindow`, `noOp`, `splitInBatches`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`refine-split-the-jsons-into-multiple-items.json`](refine-split-the-jsons-into-multiple-items.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** Triggered on Restaurant Chat workflow, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Information Extractor | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| If | `if` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| Code | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Replace Me | `noOp` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Triggered on Restaurant Chat workflow | `executeWorkflowTrigger` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Call n8n Workflow Tool | `toolWorkflow` | Inspect parameters |
| Last 5 conversations Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- If → No Operation, do nothing (`main`, output 0, input 0)
- If → Code (`main`, output 1, input 0)
- Code → Loop Over Items (`main`, output 0, input 0)
- Replace Me → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Google Sheets (`main`, output 0, input 0)
- Loop Over Items → Replace Me (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Information Extractor (`ai_languageModel`, output 0, input 0)
- Information Extractor → If (`main`, output 0, input 0)
- Call n8n Workflow Tool → AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Last 5 conversations Memory → AI Agent (`ai_memory`, output 0, input 0)
- Triggered on Restaurant Chat workflow → Information Extractor (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0918_Code_Noop_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0918_Code_Noop_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
