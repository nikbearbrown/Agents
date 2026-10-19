# receive chat events and query workflow credentials database and workflow credentials helper agent f7e6772d

This folder contains the **receive chat events and query workflow credentials database and workflow credentials helper agent f7e6772d** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `n8n`, `set`, `toolCode`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-chat-events-and-query-workflow-credentials-database-and-workflow-credentials-helper-agent-f7e6772d.json`](receive-chat-events-and-query-workflow-credentials-database-and-workflow-credentials-helper-agent-f7e6772d.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `openAiApi`

**Entry nodes:** When clicking "Test workflow", Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Map Workflows & Credentials | `set` | Inspect parameters |
| Save to Database | `code` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Query Workflow Credentials Database | `toolCode` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Workflow Credentials Helper Agent | `agent` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |

## Connection map

- n8n → Map Workflows & Credentials (`main`, output 0, input 0)
- Chat Trigger → Workflow Credentials Helper Agent (`main`, output 0, input 0)
- OpenAI Chat Model → Workflow Credentials Helper Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Workflow Credentials Helper Agent (`ai_memory`, output 0, input 0)
- Map Workflows & Credentials → Save to Database (`main`, output 0, input 0)
- When clicking "Test workflow" → n8n (`main`, output 0, input 0)
- Query Workflow Credentials Database → Workflow Credentials Helper Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1622_Manual_N8N_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1622_Manual_N8N_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
