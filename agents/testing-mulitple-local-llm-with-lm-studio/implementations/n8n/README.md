# Testing Mulitple Local LLM with LM Studio

This folder contains the **Testing Mulitple Local LLM with LM Studio** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `dateTime`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`testing-mulitple-local-llm-with-lm-studio.json`](testing-mulitple-local-llm-with-lm-studio.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Models | `httpRequest` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Get timeDifference | `dateTime` | getTimeBetweenDates |
| Run Model with Dunamic Inputs | `lmChatOpenAi` | Inspect parameters |
| Analyze LLM Response Metrics | `code` | Inspect parameters |
| Save Results to Google Sheets | `googleSheets` | append |
| Capture End Time | `dateTime` | Inspect parameters |
| Capture Start Time | `dateTime` | Inspect parameters |
| Prepare Data for Analysis | `set` | Inspect parameters |
| Extract Model IDsto Run Separately | `splitOut` | Inspect parameters |
| Add System Prompt | `set` | Inspect parameters |
| LLM Response Analysis | `chainLlm` | Inspect parameters |

## Connection map

- Get Models → Extract Model IDsto Run Separately (`main`, output 0, input 0)
- Capture End Time → Get timeDifference (`main`, output 0, input 0)
- Add System Prompt → LLM Response Analysis (`main`, output 0, input 0)
- Capture Start Time → Add System Prompt (`main`, output 0, input 0)
- Get timeDifference → Prepare Data for Analysis (`main`, output 0, input 0)
- LLM Response Analysis → Capture End Time (`main`, output 0, input 0)
- Prepare Data for Analysis → Analyze LLM Response Metrics (`main`, output 0, input 0)
- When chat message received → Get Models (`main`, output 0, input 0)
- Analyze LLM Response Metrics → Save Results to Google Sheets (`main`, output 0, input 0)
- Run Model with Dunamic Inputs → LLM Response Analysis (`ai_languageModel`, output 0, input 0)
- Extract Model IDsto Run Separately → Capture Start Time (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/2050_Datetime_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/2050_Datetime_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
