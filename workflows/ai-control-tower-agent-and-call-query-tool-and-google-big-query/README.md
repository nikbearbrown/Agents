# ai control tower agent and call query tool and google big query

This folder contains the **ai control tower agent and call query tool and google big query** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `googleBigQuery`, `lmChatOpenAi`, `memoryBufferWindow`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-control-tower-agent-and-call-query-tool-and-google-big-query.json`](ai-control-tower-agent-and-call-query-tool-and-google-big-query.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Trigger Executed by the AI Tool, Chat with the User

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| AI Control Tower Agent | `agent` | Inspect parameters |
| Call Query Tool | `toolWorkflow` | Inspect parameters |
| Query Database | `googleBigQuery` | Inspect parameters |
| Trigger Executed by the AI Tool | `executeWorkflowTrigger` | Inspect parameters |
| Sanitising the Query | `code` | Inspect parameters |
| Chat Memory | `memoryBufferWindow` | Inspect parameters |
| Chat with the User | `chatTrigger` | Inspect parameters |

## Connection map

- Chat Memory → AI Control Tower Agent (`ai_memory`, output 0, input 0)
- Call Query Tool → AI Control Tower Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → AI Control Tower Agent (`ai_languageModel`, output 0, input 0)
- Chat with the User → AI Control Tower Agent (`main`, output 0, input 0)
- Sanitising the Query → Query Database (`main`, output 0, input 0)
- Trigger Executed by the AI Tool → Sanitising the Query (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlebigquery/0806_Googlebigquery_Stickynote_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlebigquery/0806_Googlebigquery_Stickynote_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
