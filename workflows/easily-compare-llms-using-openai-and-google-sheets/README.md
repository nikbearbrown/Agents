# Easily Compare LLMs Using OpenAI and Google Sheets

This folder contains the **Easily Compare LLMs Using OpenAI and Google Sheets** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `googleSheets`, `lmChatOpenRouter`, `memoryBufferWindow`, `memoryManager`, `set`, `splitInBatches`, `splitOut`, `summarize`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`easily-compare-llms-using-openai-and-google-sheets.json`](easily-compare-llms-using-openai-and-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `openRouterApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Chat Memory Manager | `memoryManager` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Set model, sessionId, chatInput, sessionIdBase | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Concatenate Chat Answers | `summarize` | Inspect parameters |
| Group Model Outputs for Evaluation | `aggregate` | Inspect parameters |
| Add Model Results to Google Sheet | `googleSheets` | append |
| Prepare Data for Chat and Google Sheets | `set` | Inspect parameters |
| Define Models to Compare | `set` | Inspect parameters |
| Split Models into Items | `splitOut` | Inspect parameters |
| Set Output for Chat UI | `set` | Inspect parameters |

## Connection map

- AI Agent → Chat Memory Manager (`main`, output 0, input 0)
- Simple Memory → Chat Memory Manager (`ai_memory`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Loop Over Items → Concatenate Chat Answers (`main`, output 0, input 0)
- Loop Over Items → Group Model Outputs for Evaluation (`main`, output 0, input 0)
- Loop Over Items → AI Agent (`main`, output 1, input 0)
- Chat Memory Manager → Prepare Data for Chat and Google Sheets (`main`, output 0, input 0)
- OpenRouter Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Split Models into Items → Set model, sessionId, chatInput, sessionIdBase (`main`, output 0, input 0)
- Concatenate Chat Answers → Set Output for Chat UI (`main`, output 0, input 0)
- Define Models to Compare → Split Models into Items (`main`, output 0, input 0)
- When chat message received → Define Models to Compare (`main`, output 0, input 0)
- Group Model Outputs for Evaluation → Add Model Results to Google Sheet (`main`, output 0, input 0)
- Prepare Data for Chat and Google Sheets → Loop Over Items (`main`, output 0, input 0)
- Set model, sessionId, chatInput, sessionIdBase → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1790_Splitout_Summarize_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1790_Splitout_Summarize_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
