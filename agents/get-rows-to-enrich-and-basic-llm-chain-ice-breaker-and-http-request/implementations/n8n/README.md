# get rows to enrich and basic llm chain ice breaker and http request

This folder contains the **get rows to enrich and basic llm chain ice breaker and http request** workflow. Its executable nodes use `chainLlm`, `googleSheets`, `httpRequest`, `if`, `lmChatAnthropic`, `manualTrigger`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-rows-to-enrich-and-basic-llm-chain-ice-breaker-and-http-request.json`](get-rows-to-enrich-and-basic-llm-chain-ice-breaker-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** When clicking "Test workflow", Run Workflow on a certain Schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Get rows to enrich | `googleSheets` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Basic LLM Chain- Ice Breaker | `chainLlm` | Inspect parameters |
| BrightData_Get_Linkedin | `httpRequest` | Inspect parameters |
| Adjust_input_for_loop | `set` | Inspect parameters |
| HTTP_Request_Post_Request_BrightData | `httpRequest` | POST |
| Wait_For_API_Call_Results | `wait` | Inspect parameters |
| API_Call_Snapshot_Progress | `httpRequest` | Inspect parameters |
| IF-Checking_Status_API_Call | `if` | Inspect parameters |
| Google Sheets - Update Row with data From API | `googleSheets` | update |
| Google Sheets - Update Row with Ice Breaker | `googleSheets` | update |
| Run Workflow on a certain Schedule | `scheduleTrigger` | Inspect parameters |
| Loop Over Items- All Prospects | `splitInBatches` | Inspect parameters |

## Connection map

- Get rows to enrich → Adjust_input_for_loop (`main`, output 0, input 0)
- Anthropic Chat Model → Basic LLM Chain- Ice Breaker (`ai_languageModel`, output 0, input 0)
- Adjust_input_for_loop → Loop Over Items- All Prospects (`main`, output 0, input 0)
- BrightData_Get_Linkedin → Google Sheets - Update Row with data From API (`main`, output 0, input 0)
- Wait_For_API_Call_Results → API_Call_Snapshot_Progress (`main`, output 0, input 0)
- API_Call_Snapshot_Progress → IF-Checking_Status_API_Call (`main`, output 0, input 0)
- IF-Checking_Status_API_Call → Wait_For_API_Call_Results (`main`, output 0, input 0)
- IF-Checking_Status_API_Call → BrightData_Get_Linkedin (`main`, output 1, input 0)
- Basic LLM Chain- Ice Breaker → Google Sheets - Update Row with Ice Breaker (`main`, output 0, input 0)
- When clicking "Test workflow" → Get rows to enrich (`main`, output 0, input 0)
- Loop Over Items- All Prospects → HTTP_Request_Post_Request_BrightData (`main`, output 1, input 0)
- Run Workflow on a certain Schedule → Get rows to enrich (`main`, output 0, input 0)
- HTTP_Request_Post_Request_BrightData → Wait_For_API_Call_Results (`main`, output 0, input 0)
- Google Sheets - Update Row with Ice Breaker → Loop Over Items- All Prospects (`main`, output 0, input 0)
- Google Sheets - Update Row with data From API → Basic LLM Chain- Ice Breaker (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0858_Wait_Schedule_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0858_Wait_Schedule_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
