# Technical Analysis Tool

This folder contains the **Technical Analysis Tool** workflow. Its executable nodes use `agent`, `code`, `emailSend`, `executeWorkflowTrigger`, `formTrigger`, `html`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `openAi`, `outputParserStructured`, `scheduleTrigger`, `set`, `toolThink`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`technical-analysis-tool.json`](technical-analysis-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `smtp`

**Entry nodes:** Workflow Input Trigger, Schedule Trigger1, On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| GPT 4o | `lmChatOpenAi` | Inspect parameters |
| Generate HTML | `html` | Inspect parameters |
| Send Stock Analysis | `emailSend` | Inspect parameters |
| Adjust HTML Colors | `code` | Inspect parameters |
| Think | `toolThink` | Inspect parameters |
| Generate Variables For API | `code` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Get News Data | `httpRequest` | Inspect parameters |
| Analyse API Input | `code` | Inspect parameters |
| Workflow Input Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Download Chart | `httpRequest` | Inspect parameters |
| Get Chart URL | `httpRequest` | POST |
| Get Price History | `httpRequest` | Inspect parameters |
| Get Bollinger Bands | `httpRequest` | Inspect parameters |
| Get MACD | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Calculate Support Resistance | `code` | Inspect parameters |
| Organizing Data | `code` | Inspect parameters |
| Merge-2 | `merge` | Inspect parameters |
| ChatGPT 4o | `openAi` | Inspect parameters |
| Set Variable | `set` | Inspect parameters |
| Warp as JSON for GPT | `code` | Inspect parameters |
| Set Final Response | `set` | Inspect parameters |
| Set Stock Symbol and API Key | `set` | Inspect parameters |
| First Technical Analysis | `openAi` | image / analyze |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |
| Technical Analysis Tool | `toolWorkflow` | Inspect parameters |
| Trends Analysis Tool | `toolWorkflow` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Refine Text | `openAi` | Inspect parameters |

## Connection map

- Merge → Organizing Data (`main`, output 0, input 0)
- Think → AI Agent (`ai_tool`, output 0, input 0)
- GPT 4o → AI Agent (`ai_languageModel`, output 0, input 0)
- Merge-2 → Warp as JSON for GPT (`main`, output 0, input 0)
- AI Agent → Refine Text (`main`, output 0, input 0)
- Get MACD → Merge (`main`, output 0, input 2)
- ChatGPT 4o → Set Final Response (`main`, output 0, input 0)
- Refine Text → Generate HTML (`main`, output 0, input 0)
- Set Variable → Merge-2 (`main`, output 0, input 0)
- Generate HTML → Adjust HTML Colors (`main`, output 0, input 0)
- Get Chart URL → Download Chart (`main`, output 0, input 0)
- Get News Data → Analyse API Input (`main`, output 0, input 0)
- Set Variables → Get News Data (`main`, output 0, input 0)
- Download Chart → First Technical Analysis (`main`, output 0, input 0)
- Organizing Data → Merge-2 (`main`, output 0, input 1)
- Get Price History → Calculate Support Resistance (`main`, output 0, input 0)
- Schedule Trigger1 → Generate Variables For API (`main`, output 0, input 0)
- Adjust HTML Colors → Send Stock Analysis (`main`, output 0, input 0)
- On form submission → AI Agent (`main`, output 0, input 0)
- Get Bollinger Bands → Merge (`main`, output 0, input 1)
- Trends Analysis Tool → AI Agent (`ai_tool`, output 0, input 0)
- Warp as JSON for GPT → ChatGPT 4o (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Workflow Input Trigger → Set Stock Symbol and API Key (`main`, output 0, input 0)
- Technical Analysis Tool → AI Agent (`ai_tool`, output 0, input 0)
- First Technical Analysis → Set Variable (`main`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Generate Variables For API → Set Variables (`main`, output 0, input 0)
- Calculate Support Resistance → Merge (`main`, output 0, input 0)
- Set Stock Symbol and API Key → Get Chart URL (`main`, output 0, input 0)
- Set Stock Symbol and API Key → Get Price History (`main`, output 0, input 0)
- Set Stock Symbol and API Key → Get Bollinger Bands (`main`, output 0, input 0)
- Set Stock Symbol and API Key → Get MACD (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0898_Code_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0898_Code_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
