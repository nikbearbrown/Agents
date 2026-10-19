# ClockifyBlockiaWorkflow

This folder contains the **ClockifyBlockiaWorkflow** workflow. Its executable nodes use `agent`, `executionData`, `lmChatOpenAi`, `memoryBufferWindow`, `slack`, `slackTrigger`, `toolCalculator`, `toolCode`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clockifyblockiaworkflow.json`](clockifyblockiaworkflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clockifyApi`, `openAiApi`, `slackApi`

**Entry nodes:** Slack Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Create New Time Entry | `toolHttpRequest` | POST |
| GetClientsTool | `toolHttpRequest` | Inspect parameters |
| Get All Time Entries | `toolHttpRequest` | Inspect parameters |
| Current loggedin user | `toolHttpRequest` | Inspect parameters |
| GetProjectsTool | `toolHttpRequest` | Inspect parameters |
| Update Time Entry | `toolHttpRequest` | PUT |
| Delete Time Entry | `toolHttpRequest` | DELETE |
| DateConverter | `toolCode` | Inspect parameters |
| ClockifyBlockia | `agent` | Inspect parameters |
| Slack Trigger | `slackTrigger` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Add reaction | `slack` | reaction |
| Send reply | `slack` | Inspect parameters |

## Connection map

- Calculator → ClockifyBlockia (`ai_tool`, output 0, input 0)
- DateConverter → ClockifyBlockia (`ai_tool`, output 0, input 0)
- Slack Trigger → Execution Data (`main`, output 0, input 0)
- Execution Data → ClockifyBlockia (`main`, output 0, input 0)
- Execution Data → Add reaction (`main`, output 0, input 0)
- GetClientsTool → ClockifyBlockia (`ai_tool`, output 0, input 0)
- ClockifyBlockia → Send reply (`main`, output 0, input 0)
- GetProjectsTool → ClockifyBlockia (`ai_tool`, output 0, input 0)
- Delete Time Entry → ClockifyBlockia (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → ClockifyBlockia (`ai_languageModel`, output 0, input 0)
- Update Time Entry → ClockifyBlockia (`ai_tool`, output 0, input 0)
- Get All Time Entries → ClockifyBlockia (`ai_tool`, output 0, input 0)
- Window Buffer Memory → ClockifyBlockia (`ai_memory`, output 0, input 0)
- Create New Time Entry → ClockifyBlockia (`ai_tool`, output 0, input 0)
- Current loggedin user → ClockifyBlockia (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executiondata/1754_Executiondata_Slack_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executiondata/1754_Executiondata_Slack_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
