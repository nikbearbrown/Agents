# DeepSeek v3.1

This folder contains the **DeepSeek v3.1** workflow. Its executable nodes use `agent`, `gmailTool`, `lmChatDeepSeek`, `mcpClientTool`, `notionTrigger`, `set`, `wordpressTool`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`deepseek-v3-1.json`](deepseek-v3-1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `deepSeekApi`, `gmailOAuth2`, `mcpClientApi`, `notionApi`, `wordpressApi`

**Entry nodes:** Watch Notion Updates

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Watch Notion Updates | `notionTrigger` | Inspect parameters |
| AI Task Planner | `agent` | Inspect parameters |
| Send Email | `gmailTool` | Inspect parameters |
| Publish Blog Post | `wordpressTool` | Inspect parameters |
| Notion List Available Tools | `mcpClientTool` | Inspect parameters |
| Notion Run a Tool | `mcpClientTool` | executeTool |
| Edit Workflow Variables | `set` | Inspect parameters |
| DeepSeek Chat Model | `lmChatDeepSeek` | Inspect parameters |

## Connection map

- Send Email → AI Task Planner (`ai_tool`, output 0, input 0)
- Notion Run a Tool → AI Task Planner (`ai_tool`, output 0, input 0)
- Publish Blog Post → AI Task Planner (`ai_tool`, output 0, input 0)
- DeepSeek Chat Model → AI Task Planner (`ai_languageModel`, output 0, input 0)
- Watch Notion Updates → Edit Workflow Variables (`main`, output 0, input 0)
- Edit Workflow Variables → AI Task Planner (`main`, output 0, input 0)
- Notion List Available Tools → AI Task Planner (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmailtool/1142_Gmailtool_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmailtool/1142_Gmailtool_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
