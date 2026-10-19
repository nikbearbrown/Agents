# Blog Automation TEMPLATE

This folder contains the **Blog Automation TEMPLATE** workflow. Its executable nodes use `chainLlm`, `code`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`blog-automation-template.json`](blog-automation-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** ScheduleTrigger, ManualTrigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Settings | `set` | Inspect parameters |
| ScheduleTrigger | `scheduleTrigger` | Inspect parameters |
| ManualTrigger | `manualTrigger` | Inspect parameters |
| Schedule | `googleSheets` | Inspect parameters |
| Config | `code` | Inspect parameters |
| fetchConfig | `googleSheets` | Inspect parameters |
| AgentLLM | `lmChatOpenAi` | Inspect parameters |
| IfScheduledNow | `if` | Inspect parameters |
| PreparedData | `code` | Inspect parameters |
| RecombinedDataRow | `code` | Inspect parameters |
| SaveBackToSheet | `googleSheets` | update |
| IfActionPublish | `if` | Inspect parameters |
| IfTakeAction | `if` | Inspect parameters |
| IfPromptExists | `if` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| CreatePost | `httpRequest` | POST |
| SetToPublish | `googleSheets` | update |
| PrepareXmlPost | `code` | Inspect parameters |
| HandleXMLRPCResponse | `code` | Inspect parameters |
| PostingSuccessful | `if` | Inspect parameters |
| LogStatus | `googleSheets` | append |
| LogPublished | `googleSheets` | append |

## Connection map

- AgentLLM → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Schedule → PreparedData (`main`, output 0, input 0)
- Settings → fetchConfig (`main`, output 0, input 0)
- Settings → Schedule (`main`, output 0, input 0)
- LogStatus → SaveBackToSheet (`main`, output 0, input 0)
- CreatePost → HandleXMLRPCResponse (`main`, output 0, input 0)
- fetchConfig → Config (`main`, output 0, input 0)
- IfTakeAction → IfActionPublish (`main`, output 0, input 0)
- LogPublished → PostingSuccessful (`main`, output 0, input 0)
- PreparedData → IfTakeAction (`main`, output 0, input 0)
- ManualTrigger → Settings (`main`, output 0, input 0)
- IfPromptExists → Basic LLM Chain (`main`, output 0, input 0)
- IfScheduledNow → PrepareXmlPost (`main`, output 0, input 0)
- PrepareXmlPost → CreatePost (`main`, output 0, input 0)
- Basic LLM Chain → RecombinedDataRow (`main`, output 0, input 0)
- IfActionPublish → IfScheduledNow (`main`, output 0, input 0)
- IfActionPublish → IfPromptExists (`main`, output 1, input 0)
- ScheduleTrigger → Settings (`main`, output 0, input 0)
- PostingSuccessful → SetToPublish (`main`, output 0, input 0)
- RecombinedDataRow → LogStatus (`main`, output 0, input 0)
- HandleXMLRPCResponse → LogPublished (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1320_Code_Schedule_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1320_Code_Schedule_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
