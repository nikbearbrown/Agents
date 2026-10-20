# Airtop Web Agent

This folder contains the **Airtop Web Agent** workflow. Its executable nodes use `agent`, `airtop`, `airtopTool`, `executeWorkflowTrigger`, `formTrigger`, `lmChatAnthropic`, `outputParserStructured`, `set`, `slack`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`airtop-web-agent.json`](airtop-web-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtopApi`, `anthropicApi`, `slackOAuth2Api`

**Entry nodes:** On form submission, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| Click | `airtopTool` | interaction |
| Query | `airtopTool` | extraction / query |
| Load URL | `airtopTool` | window / load |
| End session | `airtopTool` | terminate |
| Type | `airtopTool` | interaction / type |
| Start browser | `toolWorkflow` | Inspect parameters |
| Claude 3.5 Haiku | `lmChatAnthropic` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Output | `set` | Inspect parameters |
| Session | `airtop` | Inspect parameters |
| Window | `airtop` | window |
| Return IDs | `set` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Slack1 | `slack` | Inspect parameters |

## Connection map

- Type → AI Agent (`ai_tool`, output 0, input 0)
- Click → AI Agent (`ai_tool`, output 0, input 0)
- Query → AI Agent (`ai_tool`, output 0, input 0)
- Slack → Return IDs (`main`, output 0, input 0)
- Output → Slack1 (`main`, output 0, input 0)
- Window → Slack (`main`, output 0, input 0)
- Session → Window (`main`, output 0, input 0)
- AI Agent → Output (`main`, output 0, input 0)
- Load URL → AI Agent (`ai_tool`, output 0, input 0)
- End session → AI Agent (`ai_tool`, output 0, input 0)
- Start browser → AI Agent (`ai_tool`, output 0, input 0)
- Claude 3.5 Haiku → AI Agent (`ai_languageModel`, output 0, input 0)
- On form submission → AI Agent (`main`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- When Executed by Another Workflow → Session (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Airtoptool/1681_Airtoptool_Slack_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Airtoptool/1681_Airtoptool_Slack_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
