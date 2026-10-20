# Error Alert and Summarizer

This folder contains the **Error Alert and Summarizer** workflow. Its executable nodes use `agent`, `code`, `errorTrigger`, `gmail`, `if`, `lmChatOpenAi`, `n8n`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`error-alert-and-summarizer.json`](error-alert-and-summarizer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `n8nApi`, `openAiApi`

**Entry nodes:** Error Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Error Trigger | `errorTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| SET EMAIL | `set` | Inspect parameters |
| Remove Manual Exec | `if` | Inspect parameters |
| Get Failed Exec | `n8n` | execution / get |
| Extract Error Details | `code` | Inspect parameters |
| Error Solver Agent | `agent` | Inspect parameters |
| Set Diagnosis Fields | `set` | Inspect parameters |
| Send Gmail | `gmail` | Inspect parameters |
| Generate Email | `code` | Inspect parameters |

## Connection map

- SET EMAIL → Get Failed Exec (`main`, output 0, input 0)
- Error Trigger → SET EMAIL (`main`, output 0, input 0)
- Generate Email → Send Gmail (`main`, output 0, input 0)
- Get Failed Exec → Remove Manual Exec (`main`, output 0, input 0)
- OpenAI Chat Model → Error Solver Agent (`ai_languageModel`, output 0, input 0)
- Error Solver Agent → Set Diagnosis Fields (`main`, output 0, input 0)
- Remove Manual Exec → Extract Error Details (`main`, output 0, input 0)
- Set Diagnosis Fields → Generate Email (`main`, output 0, input 0)
- Extract Error Details → Error Solver Agent (`main`, output 0, input 0)
- Structured Output Parser → Error Solver Agent (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"javascript_syntax": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/0945_Error_Code_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/0945_Error_Code_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
