# Discord Agent

This folder contains the **Discord Agent** workflow. Its executable nodes use `agent`, `chatTrigger`, `discordTool`, `executeWorkflowTrigger`, `lmChatOpenAi`, `memoryBufferWindow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`discord-agent.json`](discord-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Discord | `discordTool` | message |
| Discord1 | `discordTool` | getAll |
| Discord2 | `discordTool` | message |

## Connection map

- Discord → AI Agent (`ai_tool`, output 0, input 0)
- Discord1 → AI Agent (`ai_tool`, output 0, input 0)
- Discord2 → AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Discordtool/1242_Discordtool_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Discordtool/1242_Discordtool_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
