# Ask a human

This folder contains the **Ask a human** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `slack`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ask-a-human.json`](ask-a-human.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Execute Workflow Trigger, Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Not sure? | `toolWorkflow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Prompt the user to provide an email | `code` | Inspect parameters |
| Confirm that we've messaged a human | `code` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Check if user has provided email | `if` | Inspect parameters |
| Message Slack for help | `slack` | Inspect parameters |
| GPT4 | `lmChatOpenAi` | Inspect parameters |

## Connection map

- GPT4 → AI Agent (`ai_languageModel`, output 0, input 0)
- Not sure? → AI Agent (`ai_tool`, output 0, input 0)
- Chat Trigger → AI Agent (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Message Slack for help → Confirm that we've messaged a human (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if user has provided email (`main`, output 0, input 0)
- Check if user has provided email → Message Slack for help (`main`, output 0, input 0)
- Check if user has provided email → Prompt the user to provide an email (`main`, output 1, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/1318_Slack_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/1318_Slack_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
