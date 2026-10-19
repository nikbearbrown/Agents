# Some questions to try

This folder contains the **Some questions to try** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `filter`, `googleSheetsTool`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `toolCalculator`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`some-questions-to-try.json`](some-questions-to-try.json): sanitized, inactive import copy with an overview sticky note.
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
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Code | `code` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Records by date | `toolWorkflow` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Google Sheets request | `httpRequest` | Inspect parameters |
| Get transactions by product name | `googleSheetsTool` | Inspect parameters |
| Get all transactions | `googleSheetsTool` | Inspect parameters |
| Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Filter by status | `filter` | Inspect parameters |
| Get transactions by status | `googleSheetsTool` | Inspect parameters |

## Connection map

- Code → Filter by status (`main`, output 0, input 0)
- Calculator → AI Agent (`ai_tool`, output 0, input 0)
- Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Records by date → AI Agent (`ai_tool`, output 0, input 0)
- Filter by status → Aggregate (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Get all transactions → AI Agent (`ai_tool`, output 0, input 0)
- Google Sheets request → Code (`main`, output 0, input 0)
- Get transactions by status → AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Get transactions by product name → AI Agent (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → Google Sheets request (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0767_Code_Filter_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0767_Code_Filter_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
